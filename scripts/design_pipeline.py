#!/usr/bin/env python3
"""
Design Pipeline Helper

Utilities for recording and validating generated templates so Claude can focus
on generation while we keep a clean, deduped index.

Commands:
  init                              Initialize folders and empty index files
  add-generated  ...                Copy a generated file into data/generated
                                    and append an entry to data/index/generated.json
  dedupe                            Compute duplicate clusters and write
                                    data/index/generated_dedupe.json
  stats                             Print counts and basic breakdowns

Example add-generated:
  python3 scripts/design_pipeline.py add-generated \
    --id welcome_alt_a1 \
    --origin original \
    --category Welcome \
    --style apple_light \
    --score 92 \
    --map '["header_nav","hero","1col_text","cta_band","footer_simple"]' \
    --seeds '[]' \
    --format html \
    --file /tmp/new_welcome.html

Notes:
- For HTML files, we run a basic validation (template_validator).
- For structure hash, we compute a simple tag-shingle signature.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
from pathlib import Path
from typing import Dict, Any, List


ROOT = Path(__file__).resolve().parents[1]
GEN_DIR = ROOT / "data/generated"
GEN_INDEX = ROOT / "data/index/generated.json"
GEN_DEDUPE = ROOT / "data/index/generated_dedupe.json"


def ensure_dirs() -> None:
    GEN_DIR.mkdir(parents=True, exist_ok=True)
    (ROOT / "data/index").mkdir(parents=True, exist_ok=True)


def load_json(path: Path, default):
    if path.exists():
        try:
            return json.loads(path.read_text())
        except Exception:
            return default
    return default


def save_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2))


def sha256_path(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()


def structure_signature_from_html(text: str, shingle: int = 4) -> Dict[str, Any]:
    # Strip script/style and collapse to tag sequence
    low = re.sub(r"<\s*(script|style)[^>]*>[\s\S]*?<\s*/\s*\1\s*>", " ", text, flags=re.IGNORECASE)
    tags = re.findall(r"<\s*([a-zA-Z0-9]+)(\s|>)", low)
    seq = [t[0].lower() for t in tags]
    shingles = ["/".join(seq[i:i+shingle]) for i in range(max(0, len(seq)-shingle+1))]
    digest = hashlib.sha256("|".join(shingles).encode('utf-8')).hexdigest() if shingles else None
    return {"shingle": shingle, "count": len(shingles), "hash": digest}


def validate_html(text: str) -> Dict[str, Any]:
    try:
        from template_validator import validate_template
        result = validate_template({"html": text, "type": "generated"})
        return result
    except Exception as e:
        return {"valid": True, "errors": [], "warnings": [f"validator_unavailable: {e}"]}


def cmd_init(args):
    ensure_dirs()
    if not GEN_INDEX.exists():
        save_json(GEN_INDEX, {"items": []})
    if not GEN_DEDUPE.exists():
        save_json(GEN_DEDUPE, {"clusters": []})
    print("Initialized data/generated and data/index files.")


def cmd_add_generated(args):
    ensure_dirs()
    src = Path(args.file)
    if not src.exists():
        raise SystemExit(f"File not found: {src}")

    # Normalize paths
    target_dir = GEN_DIR / args.category / args.id
    target_dir.mkdir(parents=True, exist_ok=True)
    ext = '.mjml' if args.format == 'mjml' else '.html'
    dest = target_dir / (args.id + ext)
    shutil.copyfile(src, dest)

    content = dest.read_text(errors='ignore')
    content_hash = sha256_path(dest)

    structure = None
    validation = None
    if args.format == 'html':
        structure = structure_signature_from_html(content)
        validation = validate_html(content)

    try:
        section_map = json.loads(args.map)
    except Exception:
        section_map = []
    try:
        seeds = json.loads(args.seeds)
    except Exception:
        seeds = []

    record = {
        "id": args.id,
        "origin": args.origin,  # inspired | original
        "tags": ["generated", args.origin],
        "category": args.category,
        "style": args.style,
        "score": int(args.score),
        "section_map": section_map,
        "source_seeds": seeds,
        "format": args.format,
        "file_path": str(dest),
        "content_hash": content_hash,
        "structure": structure,
        "validation": validation,
    }

    idx = load_json(GEN_INDEX, {"items": []})
    idx["items"].append(record)
    save_json(GEN_INDEX, idx)
    print(f"Added: {args.id} -> {dest}")
    if validation:
        print(f"  valid={validation.get('valid')} errors={len(validation.get('errors', []))} warnings={len(validation.get('warnings', []))}")


def cmd_dedupe(args):
    idx = load_json(GEN_INDEX, {"items": []})
    items = idx.get("items", [])
    by_hash: Dict[str, List[Dict[str, Any]]] = {}
    for it in items:
        by_hash.setdefault(it.get("content_hash", ""), []).append(it)
    clusters = []
    for h, group in by_hash.items():
        if h and len(group) > 1:
            keeper = max(group, key=lambda x: (x.get("score", 0), len(x.get("structure", {}).get("count", 0) if x.get("structure") else "")))
            drop = [g["id"] for g in group if g is not keeper]
            clusters.append({"content_hash": h, "keep": keeper["id"], "drop": drop})
    save_json(GEN_DEDUPE, {"clusters": clusters})
    print(f"Duplicate clusters: {len(clusters)} written -> {GEN_DEDUPE}")


def cmd_stats(args):
    idx = load_json(GEN_INDEX, {"items": []})
    items = idx.get("items", [])
    print(f"Items: {len(items)}")
    by_origin: Dict[str, int] = {}
    by_cat: Dict[str, int] = {}
    valid = 0
    html = 0
    for it in items:
        by_origin[it.get("origin", "?")] = by_origin.get(it.get("origin", "?"), 0) + 1
        by_cat[it.get("category", "?")] = by_cat.get(it.get("category", "?"), 0) + 1
        if it.get("format") == 'html':
            html += 1
            v = it.get("validation") or {}
            if v.get("valid"):
                valid += 1
    print("By origin:", by_origin)
    print("By category:", {k: by_cat[k] for k in sorted(by_cat)})
    if html:
        print(f"HTML valid: {valid}/{html}")


def build_parser():
    p = argparse.ArgumentParser(description="Design pipeline helper")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init")

    add = sub.add_parser("add-generated")
    add.add_argument("--id", required=True)
    add.add_argument("--origin", required=True, choices=["inspired", "original"])
    add.add_argument("--category", required=True)
    add.add_argument("--style", required=True)
    add.add_argument("--score", required=True)
    add.add_argument("--map", required=True, help="JSON array of section types in order")
    add.add_argument("--seeds", required=True, help="JSON array of seed ids/notes")
    add.add_argument("--format", required=True, choices=["html", "mjml"])
    add.add_argument("--file", required=True)

    sub.add_parser("dedupe")
    sub.add_parser("stats")
    return p


def main():
    parser = build_parser()
    args = parser.parse_args()
    if args.cmd == 'init':
        cmd_init(args)
    elif args.cmd == 'add-generated':
        cmd_add_generated(args)
    elif args.cmd == 'dedupe':
        cmd_dedupe(args)
    elif args.cmd == 'stats':
        cmd_stats(args)


if __name__ == "__main__":
    main()


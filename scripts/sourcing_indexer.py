#!/usr/bin/env python3
"""
Sourcing Indexer

Lightweight helper to standardize where Claude saves raw templates and how it
indexes them. This does NOT fetch network content; it only organizes files and
metadata that Claude downloads or generates.

Folders created:
  - data/raw/<source_id>/...               (raw HTML/MJML files)
  - data/index/templates.json              (append-only master index)
  - data/index/dedupe.json                 (simple duplicate map by content hash)

CLI:
  - init                        Create folders + empty index files
  - add --source-id ...         Add an item to the index for an existing file
  - dedupe                      Compute simple duplicate clusters by content hash
  - stats                       Print index counts and basic summary

Example:
  python3 scripts/sourcing_indexer.py init
  # After Claude saves a file to data/raw/mjml_templates/welcome.mjml
  python3 scripts/sourcing_indexer.py add \
    --source-id mjml_templates \
    --source-name "MJML Email Templates" \
    --url "https://mjml.io/templates/welcome" \
    --license "MIT" \
    --type mjml \
    --file data/raw/mjml_templates/welcome.mjml
  python3 scripts/sourcing_indexer.py dedupe
  python3 scripts/sourcing_indexer.py stats
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
from typing import Dict, List, Any


RAW_DIR = Path("data/raw")
INDEX_DIR = Path("data/index")
INDEX_FILE = INDEX_DIR / "templates.json"
DEDUPE_FILE = INDEX_DIR / "dedupe.json"


def ensure_dirs() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    INDEX_DIR.mkdir(parents=True, exist_ok=True)


def load_json(path: Path, default):
    if path.exists():
        try:
            return json.loads(path.read_text())
        except Exception:
            return default
    return default


def save_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, indent=2))


def compute_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def quick_features_from_text(text: str) -> Dict[str, Any]:
    low = text.lower()
    return {
        "sections_detected": sum(1 for k in (
            "hero", "cta", "product", "testimonial", "footer", "header", "grid"
        ) if k in low),
        "has_media_queries": ("@media" in low),
        "table_count": low.count("<table"),
    }


def cmd_init(args) -> None:
    ensure_dirs()
    if not INDEX_FILE.exists():
        save_json(INDEX_FILE, {"items": []})
    if not DEDUPE_FILE.exists():
        save_json(DEDUPE_FILE, {"clusters": []})
    print("Initialized data/raw and data/index.")


def cmd_add(args) -> None:
    ensure_dirs()
    file_path = Path(args.file)
    if not file_path.exists():
        raise SystemExit(f"File not found: {file_path}")

    content = file_path.read_text(errors="ignore")
    rec = {
        "id": hashlib.md5((str(file_path) + args.url).encode("utf-8")).hexdigest(),
        "source_id": args.source_id,
        "source_name": args.source_name,
        "url": args.url,
        "license": args.license,
        "type": args.type,
        "file_path": str(file_path),
        "byte_size": file_path.stat().st_size,
        "content_hash": compute_sha256(file_path),
        "quick_features": quick_features_from_text(content),
    }

    index = load_json(INDEX_FILE, {"items": []})
    index["items"].append(rec)
    save_json(INDEX_FILE, index)
    print(f"Indexed: {file_path} [{args.source_id}] -> {INDEX_FILE}")


def cmd_dedupe(args) -> None:
    ensure_dirs()
    index = load_json(INDEX_FILE, {"items": []})
    items = index.get("items", [])
    by_hash: Dict[str, List[Dict[str, Any]]] = {}
    for it in items:
        by_hash.setdefault(it.get("content_hash", ""), []).append(it)

    clusters = []
    for content_hash, group in by_hash.items():
        if content_hash and len(group) > 1:
            # Keep the largest file in the cluster
            keeper = max(group, key=lambda x: x.get("byte_size", 0))
            dupes = [g for g in group if g is not keeper]
            clusters.append({
                "content_hash": content_hash,
                "keep": keeper["id"],
                "drop": [d["id"] for d in dupes],
            })

    save_json(DEDUPE_FILE, {"clusters": clusters})
    print(f"Wrote {len(clusters)} duplicate clusters -> {DEDUPE_FILE}")


def cmd_stats(args) -> None:
    index = load_json(INDEX_FILE, {"items": []})
    items = index.get("items", [])
    unique_hashes = len({i.get("content_hash") for i in items})
    print("Index stats:")
    print(f"  Items:         {len(items)}")
    print(f"  Unique hashes: {unique_hashes}")
    by_type = {}
    for it in items:
        by_type[it.get("type", "?")] = by_type.get(it.get("type", "?"), 0) + 1
    print(f"  Types:         {by_type}")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="TemplateForge sourcing indexer")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init")

    add = sub.add_parser("add")
    add.add_argument("--source-id", required=True)
    add.add_argument("--source-name", required=True)
    add.add_argument("--url", required=True)
    add.add_argument("--license", required=True)
    add.add_argument("--type", required=True, choices=["html", "mjml"]) 
    add.add_argument("--file", required=True, help="Path to saved HTML/MJML file under data/raw")

    sub.add_parser("dedupe")
    sub.add_parser("stats")
    return p


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if args.cmd == "init":
        cmd_init(args)
    elif args.cmd == "add":
        cmd_add(args)
    elif args.cmd == "dedupe":
        cmd_dedupe(args)
    elif args.cmd == "stats":
        cmd_stats(args)


if __name__ == "__main__":
    main()


#!/usr/bin/env python3
"""
Score compiled (sourced) templates and curate a Top 300 list for review.

Outputs:
- data/index/templates_scored.json
- data/index/curated_top300.json

Scoring (0–100):
- Responsiveness (media queries): 20
- Structure (table_count): 0–20 (>=10 tables -> 20, linear scale)
- CTA presence (anchor with btn/button classes or common labels): 0/20
- Aesthetics proxy (background color usage + style block): 0–20
- Legitimacy (unsubscribe present): 0/10
- Safety/size (no <script> and 10–350KB): 0–10
"""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
import hashlib
import re
from typing import Dict, Any, List

ROOT = Path(__file__).resolve().parents[1]
COMPILED_DIR = ROOT / "data/compiled"
INDEX_DIR = ROOT / "data/index"
SCORED_FILE = INDEX_DIR / "templates_scored.json"
CURATED_FILE = INDEX_DIR / "curated_top300.json"


def gather_compiled() -> List[Path]:
    return sorted([p for p in COMPILED_DIR.rglob("*.html")])


def score_html(text: str, size_bytes: int) -> Dict[str, Any]:
    low = text.lower()
    score = 0
    # Responsiveness
    has_media = ("@media" in low)
    score += 20 if has_media else 0

    # Structure (tables)
    table_count = low.count("<table")
    structure_pts = max(0, min(20, int((table_count / 10) * 20)))  # 10+ tables -> 20
    score += structure_pts

    # CTA presence
    cta_label = re.search(r"<a[^>]*>(\s*(shop now|buy now|get started|learn more|view deal|view offer|subscribe|sign up)\s*)</a>", low)
    cta_class = re.search(r"<a[^>]+class=\"[^\"]*(btn|button)[^\"]*\"", low)
    has_cta = bool(cta_label or cta_class)
    score += 20 if has_cta else 0

    # Aesthetics proxy
    has_style = ("<style" in low)
    bg_colors = len(re.findall(r"background(-color)?:\s*#[0-9a-f]{3,6}", low))
    aesthetics_pts = 0
    if has_style:
        aesthetics_pts += 10
    aesthetics_pts += min(10, bg_colors)  # up to +10 for multiple surfaces
    score += aesthetics_pts

    # Legitimacy: unsubscribe
    score += 10 if "unsubscribe" in low else 0

    # Safety/size
    safe = ("<script" not in low)
    in_size = 10 * 1024 <= size_bytes <= 350 * 1024
    if safe and in_size:
        score += 10

    return {
        "score": min(100, score),
        "has_media": has_media,
        "table_count": table_count,
        "has_cta": has_cta,
        "has_style": has_style,
        "bg_colors": bg_colors,
        "unsubscribe": ("unsubscribe" in low),
        "safe": safe,
        "in_size": in_size,
    }


def structure_hash(text: str, shingle: int = 4) -> str:
    low = re.sub(r"<\s*(script|style)[^>]*>[\s\S]*?<\s*/\s*\1\s*>", " ", text, flags=re.IGNORECASE)
    tags = re.findall(r"<\s*([a-zA-Z0-9]+)(\s|>)", low)
    seq = [t[0].lower() for t in tags]
    shingles = ["/".join(seq[i:i+shingle]) for i in range(max(0, len(seq)-shingle+1))]
    return hashlib.sha256("|".join(shingles).encode('utf-8')).hexdigest() if shingles else None


def main() -> None:
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    files = gather_compiled()
    scored: List[Dict[str, Any]] = []
    for p in files:
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
            size = p.stat().st_size
            metrics = score_html(text, size)
            rel = str(p.relative_to(COMPILED_DIR))
            content_hash = hashlib.sha256(text.encode('utf-8', errors='ignore')).hexdigest()
            struct_hash = structure_hash(text)
            record = {
                "file": rel.replace("\\", "/"),
                "abs_path": str(p),
                "size": size,
                "content_hash": content_hash,
                "structure_hash": struct_hash,
                **metrics,
            }
            scored.append(record)
        except Exception as e:
            # Skip problematic files
            continue

    # Save scored
    SCORED_FILE.write_text(json.dumps({"items": scored}, indent=2))

    # Deduplicate by content hash, keep the highest score (prefer larger size on tie)
    best_by_hash: Dict[str, Dict[str, Any]] = {}
    for r in scored:
        # Prefer structure hash for dedupe; fallback to content hash
        h = r.get("structure_hash") or r.get("content_hash")
        if not h:
            continue
        prev = best_by_hash.get(h)
        if not prev or (r["score"], r["size"]) > (prev["score"], prev["size"]):
            best_by_hash[h] = r
    deduped = list(best_by_hash.values())

    # Curate Top 300 from deduped set
    top = sorted(deduped, key=lambda x: (x["score"], x["has_cta"], x["table_count"]), reverse=True)[:300]
    CURATED_FILE.write_text(json.dumps({"items": top}, indent=2))

    print(f"Scored: {len(scored)} compiled files; deduped: {len(deduped)}")
    print(f"Curated Top: {len(top)} -> {CURATED_FILE}")


if __name__ == "__main__":
    main()

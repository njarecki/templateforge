#!/usr/bin/env python3
"""
Enrich the sourcing index by compiling source templates (when possible) and
adding better metrics + category tags for downstream selection.

Behavior:
- For each item in data/index/templates.json:
  - If type == mjml and MJML CLI is available, compile to HTML and save under
    data/compiled/<source_id>/<basename>.html
  - Load compiled HTML (or raw HTML for type==html) and compute metrics:
    - has_media_queries, table_count, approx_section_hints, byte_size_html
  - Tag categories using simple keyword heuristics (Welcome, Newsletter,
    Ecommerce, Promo, Transactional) — can be refined later.
- Write results to data/index/templates_enriched.json (does not overwrite the
  original index file).

Note: This script avoids network access; it uses local files only. For MJML
compilation you need the MJML CLI installed (npm install -g mjml).
"""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Dict, Any, List


ROOT = Path(__file__).resolve().parents[1]
INDEX_FILE = ROOT / "data/index/templates.json"
ENRICHED_FILE = ROOT / "data/index/templates_enriched.json"
COMPILED_DIR = ROOT / "data/compiled"


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


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""


def compute_html_metrics(html: str) -> Dict[str, Any]:
    low = html.lower()
    return {
        "has_media_queries": ("@media" in low),
        "table_count": low.count("<table"),
        "approx_section_hints": sum(1 for k in (
            "hero", "cta", "product", "grid", "testimonial", "footer", "header", "pricing"
        ) if k in low),
        "byte_size_html": len(html.encode("utf-8")),
    }


CATEGORY_KEYWORDS: Dict[str, List[str]] = {
    "Welcome": ["welcome", "getting started", "thanks for joining", "onboard"],
    "Ecommerce": ["order", "cart", "shop", "product", "purchase", "shipping", "receipt", "invoice"],
    "Newsletter": ["newsletter", "digest", "weekly", "monthly", "update", "news", "edition", "issue"],
    "Promo": ["sale", "discount", "offer", "deal", "promo", "limited", "exclusive", "black friday", "christmas", "holiday"],
    "Transactional": ["reset", "verify", "confirm", "security", "alert", "notification", "otp", "code"],
}


def tag_categories(filename: str, content: str) -> List[str]:
    low_name = filename.lower()
    low = content.lower()
    tags = []
    for cat, kws in CATEGORY_KEYWORDS.items():
        hit = 0
        for kw in kws:
            if kw in low_name:
                hit += 2  # filename hit is stronger
            if kw in low:
                hit += 1
        if hit >= 2:
            tags.append(cat)
    if not tags:
        # default to Newsletter if generic
        tags = ["Newsletter"]
    return tags


def compile_mjml_string(mjml_content: str) -> Dict[str, Any]:
    # Local import to avoid heavy deps at module import time
    import sys
    sys.path.insert(0, str(ROOT))
    from mjml_converter import compile_mjml_to_html
    return compile_mjml_to_html(mjml_content, minify=False, beautify=False)


def maybe_compile_mjml(item: Dict[str, Any]) -> Dict[str, Any]:
    file_path = Path(item.get("file_path", ""))
    if not file_path.exists():
        return {"compiled": False, "error": "file_missing"}
    mjml = read_text(file_path)
    result = compile_mjml_string(mjml)
    if result.get("success"):
        # save compiled html
        rel_dir = COMPILED_DIR / item.get("source_id", "unknown")
        rel_dir.mkdir(parents=True, exist_ok=True)
        out_path = rel_dir / (file_path.stem + ".html")
        out_path.write_text(result["html"])  # write compiled
        return {"compiled": True, "path": str(out_path), "error": None}
    return {"compiled": False, "error": result.get("error")}


def enrich(args) -> None:
    idx = load_json(INDEX_FILE, {"items": []})
    items = idx.get("items", [])
    enriched_items = []
    compiled_count = 0

    for it in items:
        et: Dict[str, Any] = {**it}
        typ = it.get("type")
        fp = Path(it.get("file_path", ""))
        compiled_html = None
        compilation = {"compiled": False, "error": None, "path": None}

        if typ == "mjml":
            compilation = maybe_compile_mjml(it)
            if compilation.get("compiled") and compilation.get("path"):
                compiled_html = read_text(Path(compilation["path"]))
                compiled_count += 1
        # Fall back to raw for html or failed compilation
        html_text = compiled_html if compiled_html is not None else read_text(fp)

        metrics = compute_html_metrics(html_text)
        categories = tag_categories(fp.name, html_text)

        et["enriched"] = {
            "compiled": compilation,
            "metrics": metrics,
            "categories": categories,
        }
        enriched_items.append(et)

    out = {"items": enriched_items}
    save_json(ENRICHED_FILE, out)
    print(f"Enriched {len(enriched_items)} items. Compiled MJML: {compiled_count}")
    print(f"Wrote: {ENRICHED_FILE}")


def main():
    p = argparse.ArgumentParser(description="Enrich sourcing index with compiled metrics and categories")
    p.add_argument("--run", action="store_true", help="Run enrichment once")
    args = p.parse_args()
    enrich(args)


if __name__ == "__main__":
    main()


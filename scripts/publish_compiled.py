#!/usr/bin/env python3
"""
Publish compiled/browsable HTML for all sourced templates.

Actions:
1) For HTML items in templates_enriched.json, copy raw HTML to
   data/compiled/<source_id>/<basename>.html so it can be served by the
   static server (http://127.0.0.1:8090).
2) Ensure enriched index has a browsable path under enriched.compiled.path
   for both MJML-compiled and copied HTML items.
3) Build a simple gallery at data/compiled/index.html grouped by category.

This script does not fetch network content; it only manipulates local files.
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Dict, Any, List

ROOT = Path(__file__).resolve().parents[1]
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


def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def publish_copies(items: List[Dict[str, Any]]) -> int:
    """Copy raw HTML items to data/compiled and inject path into enriched index."""
    copied = 0
    for it in items:
        typ = it.get("type")
        if typ != "html":
            continue
        enr = it.get("enriched") or {}
        comp = enr.get("compiled") or {}
        # If we already have a compiled/published path, skip
        if comp.get("path") and Path(comp["path"]).exists():
            continue
        src = Path(it.get("file_path", ""))
        if not src.exists():
            continue
        dest_dir = COMPILED_DIR / it.get("source_id", "unknown")
        ensure_dir(dest_dir)
        # Normalize extension
        dest = dest_dir / (src.stem + ".html")
        try:
            shutil.copyfile(src, dest)
            comp = {
                "compiled": True,  # published for viewing
                "path": str(dest),
                "error": None,
                "note": "copied_raw_html",
            }
            enr["compiled"] = comp
            it["enriched"] = enr
            copied += 1
        except Exception as e:
            # Record error but continue
            comp = {
                "compiled": False,
                "path": None,
                "error": f"copy_failed: {e}",
                "note": "copied_raw_html",
            }
            enr["compiled"] = comp
            it["enriched"] = enr
    return copied


def build_gallery(items: List[Dict[str, Any]]) -> str:
    # Build a minimal HTML gallery grouped by first category
    groups: Dict[str, List[Dict[str, Any]]] = {}
    for it in items:
        cats = (it.get("enriched", {}).get("categories") or ["Uncategorized"]) or ["Uncategorized"]
        cat = cats[0]
        groups.setdefault(cat, []).append(it)

    # Sort categories alphabetically, items by source then filename
    html_parts = []
    html_parts.append("<!DOCTYPE html><html><head><meta charset='utf-8'><title>Compiled Gallery</title>\n")
    html_parts.append("<style>body{font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif;background:#0a0a0a;color:#eee;padding:24px;} .cat{margin:24px 0;} h2{border-left:3px solid #3b82f6;padding-left:8px;} a{color:#9bd;} ul{list-style:none;padding-left:0;} li{margin:4px 0;} .meta{color:#aaa;font-size:12px;margin-left:8px}</style></head><body>")
    html_parts.append("<h1>Compiled Template Gallery</h1><p>Links point to files under data/compiled/</p>")

    for cat in sorted(groups.keys()):
        html_parts.append(f"<div class='cat'><h2>{cat}</h2><ul>")
        def sort_key(x):
            compx = (x.get('enriched',{}).get('compiled',{}) or {})
            p = compx.get('path') or ''
            name = ''
            if p:
                try:
                    name = Path(p).name
                except Exception:
                    name = p
            return (x.get('source_id',''), name)

        for it in sorted(groups[cat], key=sort_key):
            comp = (it.get("enriched", {}).get("compiled") or {})
            path = comp.get("path") or ''
            if not path:
                continue
            # Make link relative to COMPILED_DIR
            # Find 'data/compiled/' anchor in absolute path
            i = path.find("/data/compiled/")
            rel = path
            if i >= 0:
                rel = path[i+len("/data/compiled/"):]
            name = Path(rel).name
            src = it.get("source_id", "?")
            html_parts.append(f"<li><a href='/{rel}' target='_blank'>{name}</a><span class='meta'>[{src}]</span></li>")
        html_parts.append("</ul></div>")

    html_parts.append("</body></html>")
    return "".join(html_parts)


def main() -> None:
    data = load_json(ENRICHED_FILE, {"items": []})
    items = data.get("items", [])
    copied = publish_copies(items)
    # Save back enriched index (now includes 'compiled.path' for HTML items)
    save_json(ENRICHED_FILE, {"items": items})

    # Build gallery index
    index_html = build_gallery(items)
    (COMPILED_DIR / "index.html").write_text(index_html)

    print(f"Published {copied} HTML files to {COMPILED_DIR}")
    print(f"Gallery written to: {COMPILED_DIR / 'index.html'}")


if __name__ == "__main__":
    main()

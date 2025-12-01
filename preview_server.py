#!/usr/bin/env python3
"""
TemplateForge Preview Server

A simple HTTP server to preview email templates in the browser.
Supports live template generation with different skins and formats.
"""

import json
import re
import os
import os
import http.server
import socketserver
import urllib.parse
from functools import partial

from template_generator import (
    generate_template,
    list_template_types,
    TEMPLATE_TYPES,
)
from design_system import DESIGN_SKINS, IMAGE_PLACEHOLDERS
import urllib.parse
from section_library import list_section_types
from template_validator import fix_template_issues
from mjml_converter import convert_template_to_mjml


DEFAULT_PORT = 8080


def _svg_data_uri(width: int, height: int, label: str) -> str:
    """Create a simple gray SVG placeholder as a data URI."""
    svg = f"""
<svg xmlns='http://www.w3.org/2000/svg' width='{width}' height='{height}'>
  <rect width='100%' height='100%' fill='#e5e7eb'/>
  <rect x='0.5' y='0.5' width='{width-1}' height='{height-1}' fill='none' stroke='#9ca3af' stroke-width='1'/>
  <text x='50%' y='50%' dominant-baseline='middle' text-anchor='middle'
        font-family='-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif'
        font-size='{max(12, min(width, height)//10)}' fill='#6b7280'>{label}</text>
</svg>
""".strip()
    return "data:image/svg+xml;charset=UTF-8," + urllib.parse.quote(svg)


def inline_placeholder_images(html: str) -> str:
    """Replace remote placeholder image URLs with visible inline SVG placeholders for preview only."""
    # Map each known placeholder URL to an appropriately sized SVG
    size_map = {
        IMAGE_PLACEHOLDERS.get('hero'): (640, 320, '640×320'),
        IMAGE_PLACEHOLDERS.get('product'): (300, 300, '300×300'),
        IMAGE_PLACEHOLDERS.get('icon'): (64, 64, '64×64'),
        IMAGE_PLACEHOLDERS.get('logo'): (150, 50, '150×50'),
        IMAGE_PLACEHOLDERS.get('avatar'): (80, 80, '80×80'),
    }
    result = html
    for url, (w, h, label) in size_map.items():
        if url:
            result = result.replace(url, _svg_data_uri(w, h, label))
    return result


def replace_placeholders_with_boxes(html: str) -> str:
    """Replace known placeholder <img> tags with styled box divs of correct size.

    This is a compatibility fallback for environments that block data URIs or images entirely.
    """
    size_map = {
        IMAGE_PLACEHOLDERS.get('hero'): (640, 320, '640×320'),
        IMAGE_PLACEHOLDERS.get('product'): (300, 300, '300×300'),
        IMAGE_PLACEHOLDERS.get('icon'): (64, 64, '64×64'),
        IMAGE_PLACEHOLDERS.get('logo'): (150, 50, '150×50'),
        IMAGE_PLACEHOLDERS.get('avatar'): (80, 80, '80×80'),
    }

    result = html
    for url, (w, h, label) in size_map.items():
        if not url:
            continue
        box = (
            f"<div style=\"width:{w}px;height:{h}px;background:#e5e7eb;"
            f"border:1px solid #9ca3af;color:#6b7280;"
            f"display:flex;align-items:center;justify-content:center;"
            f"font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;"
            f"font-size:12px;\">{label}</div>"
        )
        # Replace only occurrences referencing the known placeholder URL
        result = result.replace(f'src="{url}"', f'src="" data-replaced="box"')
        # Replace the entire img tag conservatively by swapping common patterns
        result = result.replace(
            f'<img src="{url}"',
            box
        )
    return result


def localize_placeholder_images(html: str) -> str:
    """Rewrite placeholder image URLs to local endpoints served by the preview server."""
    mapping = {
        IMAGE_PLACEHOLDERS.get('hero'): '/__placeholders__/hero.svg',
        IMAGE_PLACEHOLDERS.get('product'): '/__placeholders__/product.svg',
        IMAGE_PLACEHOLDERS.get('icon'): '/__placeholders__/icon.svg',
        IMAGE_PLACEHOLDERS.get('logo'): '/__placeholders__/logo.svg',
        IMAGE_PLACEHOLDERS.get('avatar'): '/__placeholders__/avatar.svg',
    }
    result = html
    for url, local in mapping.items():
        if url:
            result = result.replace(url, local)
    return result


def get_template_preview(template_type, skin="apple_light", output_format="html", inline=False, inline_mode="local"):
    """Generate a template and return HTML or MJML."""
    template = generate_template(template_type, skin)
    template = fix_template_issues(template)

    if output_format == "mjml":
        template["mjml"] = convert_template_to_mjml(template)
        return template["mjml"], "text/plain"

    html = template["html"]
    if inline:
        if inline_mode == "box":
            html = replace_placeholders_with_boxes(html)
        elif inline_mode == "svg":
            html = inline_placeholder_images(html)
        else:
            html = localize_placeholder_images(html)
    return html, "text/html"


def get_index_page():
    """Generate the index page with all templates listed."""
    templates = list_template_types()
    skins = list(DESIGN_SKINS.keys())

    # Group templates by category
    categories = {}
    for t in templates:
        cat = t["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(t)

    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TemplateForge Preview</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #0a0a0a;
            color: #e5e5e5;
            line-height: 1.6;
            padding: 2rem;
        }
        .container { max-width: 1200px; margin: 0 auto; }
        header {
            text-align: center;
            margin-bottom: 3rem;
            padding-bottom: 2rem;
            border-bottom: 1px solid #333;
        }
        h1 {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }
        h1 span { color: #3b82f6; }
        .subtitle { color: #888; font-size: 1.1rem; }
        .stats {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-top: 1.5rem;
        }
        .stat {
            text-align: center;
            padding: 1rem 2rem;
            background: #1a1a1a;
            border-radius: 8px;
        }
        .stat-value { font-size: 2rem; font-weight: 700; color: #3b82f6; }
        .stat-label { font-size: 0.85rem; color: #888; }
        .controls {
            background: #1a1a1a;
            padding: 1.5rem;
            border-radius: 12px;
            margin-bottom: 2rem;
            display: flex;
            gap: 1.5rem;
            flex-wrap: wrap;
            align-items: center;
        }
        .control-group {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }
        .control-group label {
            font-size: 0.85rem;
            color: #888;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        select {
            padding: 0.75rem 1rem;
            font-size: 1rem;
            border: 1px solid #333;
            border-radius: 6px;
            background: #0a0a0a;
            color: #e5e5e5;
            cursor: pointer;
            min-width: 200px;
        }
        select:focus { outline: none; border-color: #3b82f6; }
        .category {
            margin-bottom: 2.5rem;
        }
        .category-title {
            font-size: 1.25rem;
            font-weight: 600;
            margin-bottom: 1rem;
            padding-left: 0.5rem;
            border-left: 3px solid #3b82f6;
        }
        .template-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 1rem;
        }
        .template-card {
            background: #1a1a1a;
            border: 1px solid #333;
            border-radius: 10px;
            padding: 1.25rem;
            transition: all 0.2s ease;
        }
        .template-card:hover {
            border-color: #3b82f6;
            transform: translateY(-2px);
        }
        .template-name {
            font-weight: 600;
            font-size: 1.05rem;
            margin-bottom: 0.25rem;
        }
        .template-type {
            font-size: 0.85rem;
            color: #666;
            font-family: monospace;
            margin-bottom: 0.75rem;
        }
        .template-sections {
            font-size: 0.8rem;
            color: #888;
            margin-bottom: 1rem;
        }
        .template-actions {
            display: flex;
            gap: 0.5rem;
        }
        .btn {
            padding: 0.5rem 1rem;
            font-size: 0.85rem;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            text-decoration: none;
            transition: all 0.15s ease;
            font-weight: 500;
        }
        .btn-primary {
            background: #3b82f6;
            color: white;
        }
        .btn-primary:hover { background: #2563eb; }
        .btn-secondary {
            background: #333;
            color: #e5e5e5;
        }
        .btn-secondary:hover { background: #444; }
        footer {
            text-align: center;
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 1px solid #333;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Template<span>Forge</span></h1>
            <p class="subtitle">Email Template Generation Pipeline</p>
            <div class="stats">
                <div class="stat">
                    <div class="stat-value">""" + str(len(templates)) + """</div>
                    <div class="stat-label">Template Types</div>
                </div>
                <div class="stat">
                    <div class="stat-value">""" + str(len(skins)) + """</div>
                    <div class="stat-label">Design Skins</div>
                </div>
                <div class="stat">
                    <div class="stat-value">""" + str(len(list_section_types())) + """</div>
                    <div class="stat-label">Section Types</div>
                </div>
            </div>
        </header>

        <div class="controls">
            <div class="control-group">
                <label>Default Skin</label>
                <select id="skinSelect">"""

    for skin_id, skin_data in DESIGN_SKINS.items():
        selected = "selected" if skin_id == "apple_light" else ""
        html += f'<option value="{skin_id}" {selected}>{skin_data["name"]}</option>'

    html += """
                </select>
            </div>
            <div class="control-group">
                <label>Output Format</label>
                <select id="formatSelect">
                    <option value="html" selected>HTML (rendered)</option>
                    <option value="mjml">MJML (source)</option>
                </select>
            </div>
        </div>
"""

    # Curated Top 300 (from scoring) – show first
    try:
        with open(os.path.join('data','index','curated_top300.json'),'r') as f:
            curated = json.load(f).get('items', [])
    except Exception:
        curated = []
    if curated:
        html += """
        <div class=\"category\">\n            <h2 class=\"category-title\">Curated Top 300 (Scored)</h2>\n            <div class=\"template-grid\">"""
        for item in curated[:60]:
            rel = item.get('file','')
            name = os.path.basename(rel)
            score = item.get('score', 0)
            link = f"/compiled/{rel}"
            html += f"""
                <div class=\"template-card\">\n                    <div class=\"template-name\">{name}</div>\n                    <div class=\"template-type\">score {score}</div>\n                    <div class=\"template-actions\">\n                        <a href=\"{link}\" class=\"btn btn-primary\">Open</a>\n                    </div>\n                </div>"""
        html += """
            </div>\n            <div style=\"margin-top:8px;\"><a class=\"btn btn-secondary\" href=\"/curated\">View All 300</a></div>\n        </div>"""

    # Add generated templates section (newest first) if available
    try:
        with open(os.path.join('data','index','generated.json'), 'r') as f:
            gen_idx = json.load(f)
        gen_items = gen_idx.get('items', [])
        if gen_items:
            def _mtime(it):
                p = it.get('file_path') or ''
                try:
                    return os.path.getmtime(p)
                except Exception:
                    return 0
            latest = sorted(gen_items, key=_mtime, reverse=True)[:24]
            html += """
        <div class="category">
            <h2 class="category-title">Generated (Newest)</h2>
            <div class="template-grid">"""
            for it in latest:
                tid = it.get('id','unknown')
                origin = it.get('origin','generated')
                style = it.get('style','')
                category = it.get('category','Generated')
                sections = it.get('section_map') or []
                sections_str = ", ".join(sections[:3]) + ("..." if len(sections)>3 else "")
                html += f"""
                <div class=\"template-card\" data-type=\"{tid}\">
                    <div class=\"template-name\">{category} — {style}</div>
                    <div class=\"template-type\">{tid} ({origin})</div>
                    <div class=\"template-sections\">{sections_str}</div>
                    <div class=\"template-actions\">
                        <a href=\"/generated/{tid}\" class=\"btn btn-primary\">Open</a>
                    </div>
                </div>"""
            html += """
            </div>
        </div>"""
    except Exception:
        pass

    # If no generated items, show latest compiled files for quick access
    try:
        compiled_files = []
        for root, dirs, files in os.walk(os.path.join('data','compiled')):
            for name in files:
                if name.lower().endswith('.html'):
                    full = os.path.join(root, name)
                    compiled_files.append((full, os.path.getmtime(full)))
        if compiled_files:
            compiled_files.sort(key=lambda x: x[1], reverse=True)
            latest_c = [c[0] for c in compiled_files[:24]]
            html += """
        <div class=\"category\">
            <h2 class=\"category-title\">Latest Compiled</h2>
            <div class=\"template-grid\">"""
            for full in latest_c:
                # Build relative path reliably under data/compiled
                try:
                    rel = os.path.relpath(full, os.path.join('data','compiled'))
                except Exception:
                    rel = os.path.basename(full)
                rel = rel.replace('\\\\','/')
                name = os.path.basename(full)
                html += f"""
                <div class=\"template-card\">
                    <div class=\"template-name\">{name}</div>
                    <div class=\"template-type\">compiled</div>
                    <div class=\"template-actions\">
                        <a href=\"/compiled/{rel}\" class=\"btn btn-primary\">Open</a>
                    </div>
                </div>"""
            html += """
            </div>
        </div>"""
    except Exception:
        pass

    # Curated Top 300 (from scoring) at the top
    try:
        with open(os.path.join('data','index','curated_top300.json'),'r') as f:
            top = json.load(f).get('items', [])
        if top:
            html += """
        <div class=\"category\">
            <h2 class=\"category-title\">Curated Top 300 (Scored)</h2>
            <div class=\"template-grid\">"""
            for item in top[:24]:
                rel = item.get('file','')
                name = os.path.basename(rel)
                score = item.get('score', 0)
                html += f"""
                <div class=\"template-card\">\n                    <div class=\"template-name\">{name}</div>\n                    <div class=\"template-type\">score {score}</div>\n                    <div class=\"template-actions\">\n                        <a href=\"/compiled/{rel}\" class=\"btn btn-primary\">Open</a>\n                    </div>\n                </div>"""
            html += """
            </div>
        </div>"""
    except Exception:
        pass

    for category, cat_templates in categories.items():
        html += f"""
        <div class="category">
            <h2 class="category-title">{category}</h2>
            <div class="template-grid">"""

        for t in cat_templates:
            sections = t.get("sections", [])[:3]
            sections_str = ", ".join(sections) + ("..." if len(t.get("sections", [])) > 3 else "")
            html += f"""
                <div class="template-card" data-type="{t['type']}">
                    <div class="template-name">{t['name']}</div>
                    <div class="template-type">{t['type']}</div>
                    <div class="template-sections">{sections_str}</div>
                    <div class="template-actions">
                        <a href="#" class="btn btn-primary preview-btn" data-type="{t['type']}">Preview</a>
                        <a href="#" class="btn btn-secondary source-btn" data-type="{t['type']}">Source</a>
                    </div>
                </div>"""

        html += """
            </div>
        </div>"""

    html += """
        <footer>
            <p>TemplateForge &mdash; Generating production-ready email templates</p>
        </footer>
    </div>

    <script>
        function getPreviewUrl(type) {
            const skin = document.getElementById('skinSelect').value;
            const format = document.getElementById('formatSelect').value;
            return `/preview/${type}?skin=${skin}&format=${format}&inline=1`;
        }

        document.querySelectorAll('.preview-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                const type = btn.dataset.type;
                window.open(getPreviewUrl(type), '_blank');
            });
        });

        document.querySelectorAll('.source-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                const type = btn.dataset.type;
                const skin = document.getElementById('skinSelect').value;
                window.open(`/preview/${type}?skin=${skin}&format=mjml`, '_blank');
            });
        });
    </script>
</body>
</html>"""

    return html


def get_comparison_page(template_type):
    """Generate a page showing all skins side by side for comparison."""
    skins = list(DESIGN_SKINS.items())

    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Skin Comparison - """ + template_type + """</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #0a0a0a;
            color: #e5e5e5;
            padding: 1rem;
        }
        header {
            text-align: center;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        h1 { font-size: 1.5rem; }
        .back-link {
            color: #3b82f6;
            text-decoration: none;
            display: inline-block;
            margin-bottom: 0.5rem;
        }
        .comparison-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 1rem;
        }
        .skin-preview {
            background: #1a1a1a;
            border-radius: 8px;
            overflow: hidden;
        }
        .skin-header {
            padding: 0.75rem 1rem;
            background: #222;
            font-weight: 600;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .skin-frame {
            width: 100%;
            height: 600px;
            border: none;
        }
        .open-btn {
            padding: 0.4rem 0.8rem;
            background: #3b82f6;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            text-decoration: none;
            font-size: 0.85rem;
        }
    </style>
</head>
<body>
    <header>
        <a href="/" class="back-link">&larr; Back to Templates</a>
        <h1>Comparing Skins: """ + template_type + """</h1>
    </header>
    <div class="comparison-grid">"""

    for skin_id, skin_data in skins:
        html += f"""
        <div class="skin-preview">
            <div class="skin-header">
                <span>{skin_data['name']}</span>
                <a href="/preview/{template_type}?skin={skin_id}" target="_blank" class="open-btn">Open</a>
            </div>
            <iframe class="skin-frame" src="/preview/{template_type}?skin={skin_id}"></iframe>
        </div>"""

    html += """
    </div>
</body>
</html>"""

    return html


class PreviewHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP request handler for template previews."""

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)

        # Local placeholder images (SVG)
        if path.startswith("/__placeholders__/"):
            name = path.split("/")[-1]
            sizes = {
                'hero.svg': (640, 320, '640×320'),
                'product.svg': (300, 300, '300×300'),
                'icon.svg': (64, 64, '64×64'),
                'logo.svg': (150, 50, '150×50'),
                'avatar.svg': (80, 80, '80×80'),
            }
            if name in sizes:
                w, h, label = sizes[name]
                svg_data_uri = _svg_data_uri(w, h, label)
                # Extract raw SVG from data URI
                svg_raw = urllib.parse.unquote(svg_data_uri.split(',', 1)[1]).encode('utf-8')
                self.send_response(200)
                self.send_header("Content-type", "image/svg+xml;charset=UTF-8")
                self.end_headers()
                self.wfile.write(svg_raw)
                return
            else:
                self.send_error(404, "Unknown placeholder")
                return

        # Index page
        if path == "/" or path == "/index.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(get_index_page().encode())
            return

        # Curated Top 300 full view
        if path == "/curated":
            try:
                with open(os.path.join('data','index','curated_top300.json'),'r') as f:
                    items = json.load(f).get('items', [])
            except Exception:
                items = []

            html = """<!DOCTYPE html>
<html lang=\"en\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"><title>Curated Top 300</title>
<style>
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:#0a0a0a;color:#e5e5e5;padding:24px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px}
.card{background:#1a1a1a;border:1px solid #333;border-radius:10px;padding:12px}
.name{font-weight:600;margin-bottom:6px}
.meta{color:#aaa;font-size:12px;margin-bottom:8px}
.btn{display:inline-block;padding:6px 10px;background:#3b82f6;color:#fff;text-decoration:none;border-radius:6px}
a{color:#9bd}
</style></head><body>
<h1>Curated Top 300 (Scored)</h1>
<p><a href=\"/\">&larr; Back</a></p>
<div class=\"grid\">"""

            for it in items:
                rel = it.get('file','')
                name = os.path.basename(rel)
                score = it.get('score',0)
                link = f"/compiled/{rel}"
                html += f"""
  <div class=\"card\">\n    <div class=\"name\">{name}</div>\n    <div class=\"meta\">score {score}</div>\n    <a class=\"btn\" href=\"{link}\">Open</a>\n  </div>"""

            html += """</div></body></html>"""

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode())
            return

        # Template preview
        if path.startswith("/preview/"):
            template_type = path.replace("/preview/", "").strip("/")

            if template_type not in TEMPLATE_TYPES:
                self.send_error(404, f"Unknown template type: {template_type}")
                return

            skin = query.get("skin", ["apple_light"])[0]
            output_format = query.get("format", ["html"])[0]
            inline = query.get("inline", ["0"])[0] in ("1", "true", "yes")
            inline_mode = query.get("placeholder", ["local"])[0]

            if skin not in DESIGN_SKINS:
                skin = "apple_light"

            try:
                content, content_type = get_template_preview(
                    template_type, skin, output_format, inline=inline, inline_mode=inline_mode
                )
                self.send_response(200)
                self.send_header("Content-type", content_type)
                self.end_headers()
                self.wfile.write(content.encode())
            except Exception as e:
                self.send_error(500, f"Error generating template: {str(e)}")
            return

        # Generated template view by id
        if path.startswith("/generated/"):
            gen_id = path.replace("/generated/", "").strip("/")
            try:
                with open(os.path.join('data','index','generated.json'), 'r') as f:
                    gen_idx = json.load(f)
                items = gen_idx.get('items', [])
                match = next((it for it in items if it.get('id') == gen_id), None)
                file_path = None
                fmt = 'html'
                if match:
                    file_path = match.get('file_path')
                    fmt = match.get('format','html')
                # Fallback: search under data/generated for a file named <id>.html or .mjml
                if not file_path or not os.path.isfile(file_path):
                    # Try direct relative paths (category/id/id.html)
                    candidates = []
                    base_html = gen_id + '.html'
                    base_mjml = gen_id + '.mjml'
                    for root, dirs, files in os.walk(os.path.join('data','generated')):
                        for name in files:
                            if name == base_html or name == base_mjml:
                                candidates.append(os.path.join(root, name))
                    if candidates:
                        # Pick newest
                        candidates.sort(key=lambda p: os.path.getmtime(p), reverse=True)
                        file_path = candidates[0]
                        fmt = 'mjml' if file_path.lower().endswith('.mjml') else 'html'
                if not file_path or not os.path.isfile(file_path):
                    self.send_error(404, f"File missing for template: {gen_id}")
                    return
                # Serve content (compile MJML if possible)
                if fmt == 'html':
                    content_type = "text/html"
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                else:
                    try:
                        from mjml_converter import compile_mjml_to_html
                        mjml = open(file_path, 'r', encoding='utf-8', errors='ignore').read()
                        res = compile_mjml_to_html(mjml)
                        if res.get('success'):
                            content = res['html']
                            content_type = "text/html"
                        else:
                            content = mjml
                            content_type = "text/plain"
                    except Exception:
                        mjml = open(file_path, 'r', encoding='utf-8', errors='ignore').read()
                        content = mjml
                        content_type = "text/plain"
                self.send_response(200)
                self.send_header("Content-type", content_type)
                self.end_headers()
                self.wfile.write(content.encode())
            except Exception as e:
                self.send_error(500, f"Error loading generated template: {str(e)}")
            return

        # Skin comparison page
        if path.startswith("/compare/"):
            template_type = path.replace("/compare/", "").strip("/")

            if template_type not in TEMPLATE_TYPES:
                self.send_error(404, f"Unknown template type: {template_type}")
                return

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(get_comparison_page(template_type).encode())
            return

        # Serve compiled files from data/compiled
        if path.startswith("/compiled/"):
            rel = path.replace("/compiled/", "", 1)
            # URL-decode
            try:
                rel = urllib.parse.unquote(rel)
            except Exception:
                pass
            # prevent directory traversal
            if ".." in rel or rel.startswith('/'):
                self.send_error(400, "Bad path")
                return
            full = os.path.join('data','compiled', rel)
            if not os.path.isfile(full):
                self.send_error(404, "Compiled file not found")
                return
            try:
                content = open(full, 'r', encoding='utf-8', errors='ignore').read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode())
            except Exception as e:
                self.send_error(500, f"Error reading compiled file: {e}")
            return

        # API: list templates
        if path == "/api/templates":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(list_template_types()).encode())
            return

        # API: list skins
        if path == "/api/skins":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            skins_list = [
                {"id": k, "name": v["name"]} for k, v in DESIGN_SKINS.items()
            ]
            self.wfile.write(json.dumps(skins_list).encode())
            return

        # Fallback: serve files directly from data/compiled or data/generated by URL path
        # This lets paths like /mailchimp_blueprints/transactional_tabular.html work.
        rel = path.lstrip('/')
        if rel:
            try:
                rel_decoded = urllib.parse.unquote(rel)
            except Exception:
                rel_decoded = rel
            for base in (os.path.join('data','compiled'), os.path.join('data','generated')):
                full = os.path.join(base, rel_decoded)
                if os.path.isfile(full):
                    try:
                        if full.lower().endswith('.html'):
                            content = open(full, 'r', encoding='utf-8', errors='ignore').read()
                            self.send_response(200)
                            self.send_header("Content-type", "text/html")
                            self.end_headers()
                            self.wfile.write(content.encode())
                            return
                        elif full.lower().endswith('.mjml'):
                            try:
                                from mjml_converter import compile_mjml_to_html
                                mjml = open(full, 'r', encoding='utf-8', errors='ignore').read()
                                res = compile_mjml_to_html(mjml)
                                if res.get('success'):
                                    self.send_response(200)
                                    self.send_header("Content-type", "text/html")
                                    self.end_headers()
                                    self.wfile.write(res['html'].encode())
                                    return
                                else:
                                    self.send_response(200)
                                    self.send_header("Content-type", "text/plain")
                                    self.end_headers()
                                    self.wfile.write(mjml.encode())
                                    return
                            except Exception:
                                mjml = open(full, 'r', encoding='utf-8', errors='ignore').read()
                                self.send_response(200)
                                self.send_header("Content-type", "text/plain")
                                self.end_headers()
                                self.wfile.write(mjml.encode())
                                return
                    except Exception as e:
                        self.send_error(500, f"Error serving file: {e}")
                        return

        # 404 for other paths
        self.send_error(404, "Not Found")

    def log_message(self, format, *args):
        """Custom log format."""
        print(f"[{self.log_date_time_string()}] {args[0]}")


def run_server(port=DEFAULT_PORT):
    """Start the preview server bound to localhost only."""
    handler = PreviewHandler

    # Bind explicitly to 127.0.0.1 to avoid interface restrictions in sandboxes
    with socketserver.TCPServer(("127.0.0.1", port), handler) as httpd:
        print("=" * 50)
        print("TemplateForge Preview Server")
        print("=" * 50)
        print()
        print(f"Server running at: http://127.0.0.1:{port}")
        print()
        print("Endpoints:")
        print(f"  /                     - Template gallery")
        print(f"  /preview/<type>       - Preview template")
        print(f"  /compare/<type>       - Compare all skins")
        print(f"  /api/templates        - List templates (JSON)")
        print(f"  /api/skins            - List skins (JSON)")
        print()
        print("Query parameters:")
        print("  ?skin=<skin_id>       - Select design skin")
        print("  ?format=html|mjml     - Output format")
        print()
        print("Press Ctrl+C to stop the server")
        print()

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="TemplateForge Preview Server"
    )
    parser.add_argument(
        "--port", "-p",
        type=int,
        default=DEFAULT_PORT,
        help=f"Port to run the server on (default: {DEFAULT_PORT})"
    )

    args = parser.parse_args()
    run_server(args.port)


if __name__ == "__main__":
    main()

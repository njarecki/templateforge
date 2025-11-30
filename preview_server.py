#!/usr/bin/env python3
"""
TemplateForge Preview Server

A simple HTTP server to preview email templates in the browser.
Supports live template generation with different skins and formats.
"""

import json
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
from section_library import list_section_types
from template_validator import fix_template_issues
from mjml_converter import convert_template_to_mjml


DEFAULT_PORT = 8080


TRANSPARENT_PNG_DATA_URI = (
    "data:image/png;base64,"
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGMAAQAABQAB" 
    "J9i8WQAAAABJRU5ErkJggg=="
)


def inline_placeholder_images(html: str) -> str:
    """Replace remote placeholder image URLs with inline transparent PNGs for preview."""
    result = html
    for url in IMAGE_PLACEHOLDERS.values():
        result = result.replace(url, TRANSPARENT_PNG_DATA_URI)
    return result


def get_template_preview(template_type, skin="apple_light", output_format="html", inline=False):
    """Generate a template and return HTML or MJML."""
    template = generate_template(template_type, skin)
    template = fix_template_issues(template)

    if output_format == "mjml":
        template["mjml"] = convert_template_to_mjml(template)
        return template["mjml"], "text/plain"

    html = template["html"]
    if inline:
        html = inline_placeholder_images(html)
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
            return `/preview/${type}?skin=${skin}&format=${format}`;
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

        # Index page
        if path == "/" or path == "/index.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(get_index_page().encode())
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

            if skin not in DESIGN_SKINS:
                skin = "apple_light"

            try:
                content, content_type = get_template_preview(
                    template_type, skin, output_format, inline=inline
                )
                self.send_response(200)
                self.send_header("Content-type", content_type)
                self.end_headers()
                self.wfile.write(content.encode())
            except Exception as e:
                self.send_error(500, f"Error generating template: {str(e)}")
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

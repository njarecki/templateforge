#!/usr/bin/env python3
"""
Generate a single-page HTML review tool for rapid template curation.

Features:
- Renders all tokenized templates with a consistent design skin
- Click to exclude/include templates
- Filter by category
- Export final selection
"""

import json
import os
from pathlib import Path

# Design skin to render templates with
DESIGN_SKIN = {
    'brandBG': '#ffffff',
    'brandPrimary': '#1a1a1a',
    'brandSecondary': '#666666',
    'brandText': '#333333',
    'brandAccent': '#2563eb',
    'brandFont': 'Inter, system-ui, sans-serif',
}


def apply_skin(html: str, skin: dict) -> str:
    """Apply design skin to tokenized template."""
    result = html
    for token, value in skin.items():
        result = result.replace('{' + token + '}', value)
    return result


def generate_review_html(templates: list, output_path: str):
    """Generate the review page HTML."""

    html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Template Review Tool</title>
    <style>
        * { box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #0a0a0a;
            color: #fff;
            margin: 0;
            padding: 20px;
        }
        .header {
            position: sticky;
            top: 0;
            background: #0a0a0a;
            padding: 20px 0;
            z-index: 1000;
            border-bottom: 1px solid #333;
            margin-bottom: 20px;
        }
        .header h1 { margin: 0 0 10px 0; }
        .stats {
            display: flex;
            gap: 20px;
            align-items: center;
            flex-wrap: wrap;
        }
        .stat {
            background: #1a1a1a;
            padding: 8px 16px;
            border-radius: 8px;
        }
        .stat.selected { background: #166534; }
        .stat.excluded { background: #991b1b; }
        .filters {
            display: flex;
            gap: 10px;
            margin-top: 15px;
            flex-wrap: wrap;
        }
        .filter-btn {
            padding: 8px 16px;
            border: 1px solid #444;
            background: transparent;
            color: #fff;
            border-radius: 20px;
            cursor: pointer;
            transition: all 0.2s;
        }
        .filter-btn:hover { background: #333; }
        .filter-btn.active { background: #2563eb; border-color: #2563eb; }
        .actions {
            display: flex;
            gap: 10px;
            margin-top: 15px;
        }
        .action-btn {
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
        }
        .action-btn.primary { background: #2563eb; color: white; }
        .action-btn.secondary { background: #333; color: white; }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
            gap: 20px;
        }
        .template-card {
            background: #1a1a1a;
            border-radius: 12px;
            overflow: hidden;
            transition: all 0.2s;
            cursor: pointer;
            border: 3px solid transparent;
        }
        .template-card:hover { transform: translateY(-2px); }
        .template-card.selected { border-color: #22c55e; }
        .template-card.excluded {
            opacity: 0.3;
            border-color: #ef4444;
        }
        .template-card.hidden { display: none; }
        .preview-frame {
            width: 100%;
            height: 500px;
            border: none;
            background: white;
            pointer-events: none;
        }
        .card-info {
            padding: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .card-title {
            font-size: 12px;
            color: #888;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            max-width: 200px;
        }
        .card-meta {
            display: flex;
            gap: 8px;
        }
        .tag {
            font-size: 10px;
            padding: 4px 8px;
            border-radius: 4px;
            background: #333;
        }
        .tag.cat-Welcome { background: #7c3aed; }
        .tag.cat-Newsletter { background: #0891b2; }
        .tag.cat-Promo { background: #ea580c; }
        .tag.cat-Transactional { background: #4f46e5; }
        .tag.cat-Ecommerce { background: #059669; }
        .score {
            font-size: 12px;
            font-weight: 600;
            color: #22c55e;
        }
        .status-indicator {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #666;
        }
        .template-card.selected .status-indicator { background: #22c55e; }
        .template-card.excluded .status-indicator { background: #ef4444; }
        #export-modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0,0,0,0.8);
            z-index: 2000;
            align-items: center;
            justify-content: center;
        }
        #export-modal.show { display: flex; }
        .modal-content {
            background: #1a1a1a;
            padding: 30px;
            border-radius: 12px;
            max-width: 600px;
            width: 90%;
        }
        .modal-content textarea {
            width: 100%;
            height: 300px;
            background: #0a0a0a;
            border: 1px solid #333;
            color: #fff;
            padding: 10px;
            font-family: monospace;
            font-size: 12px;
            border-radius: 8px;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Template Review Tool</h1>
        <p style="color: #888; margin: 0 0 15px 0;">Click templates to select (green) or exclude (red). Double-click to toggle exclude.</p>
        <div class="stats">
            <div class="stat">Total: <strong id="total-count">0</strong></div>
            <div class="stat selected">Selected: <strong id="selected-count">0</strong></div>
            <div class="stat excluded">Excluded: <strong id="excluded-count">0</strong></div>
        </div>
        <div class="filters">
            <button class="filter-btn active" data-category="all">All</button>
            <button class="filter-btn" data-category="Welcome">Welcome</button>
            <button class="filter-btn" data-category="Newsletter">Newsletter</button>
            <button class="filter-btn" data-category="Promo">Promo</button>
            <button class="filter-btn" data-category="Transactional">Transactional</button>
            <button class="filter-btn" data-category="Ecommerce">Ecommerce</button>
        </div>
        <div class="actions">
            <button class="action-btn primary" onclick="exportSelection()">Export Selection</button>
            <button class="action-btn secondary" onclick="selectAll()">Select All Visible</button>
            <button class="action-btn secondary" onclick="clearAll()">Clear Selection</button>
        </div>
    </div>

    <div class="grid" id="template-grid">
'''

    # Add each template
    for i, t in enumerate(templates):
        file_path = os.path.join('data/tokenized', os.path.dirname(t['file']), os.path.basename(t['file']))
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                template_html = f.read()
        except:
            continue

        # Apply skin
        rendered = apply_skin(template_html, DESIGN_SKIN)

        # Escape for srcdoc
        escaped = rendered.replace('&', '&amp;').replace('"', '&quot;')

        # Get categories
        categories = t.get('categories', ['Unknown'])
        cat_tags = ''.join(f'<span class="tag cat-{c}">{c}</span>' for c in categories[:2])

        html += f'''
        <div class="template-card" data-id="{i}" data-file="{t['file']}" data-categories="{','.join(categories)}" data-score="{t.get('original_score', 0)}">
            <iframe class="preview-frame" srcdoc="{escaped}"></iframe>
            <div class="card-info">
                <span class="card-title" title="{t['file']}">{t['file']}</span>
                <div class="card-meta">
                    {cat_tags}
                    <span class="score">{t.get('original_score', 0)}</span>
                    <div class="status-indicator"></div>
                </div>
            </div>
        </div>
'''

    html += '''
    </div>

    <div id="export-modal">
        <div class="modal-content">
            <h2>Export Selection</h2>
            <p>Copy this JSON to save your selection:</p>
            <textarea id="export-data" readonly></textarea>
            <br><br>
            <button class="action-btn secondary" onclick="closeModal()">Close</button>
            <button class="action-btn primary" onclick="copyExport()">Copy to Clipboard</button>
        </div>
    </div>

    <script>
        // State
        const state = {
            selected: new Set(),
            excluded: new Set(),
            currentFilter: 'all'
        };

        // Load from localStorage
        const saved = localStorage.getItem('templateReviewState');
        if (saved) {
            const parsed = JSON.parse(saved);
            state.selected = new Set(parsed.selected || []);
            state.excluded = new Set(parsed.excluded || []);
        }

        // Apply initial state
        document.querySelectorAll('.template-card').forEach(card => {
            const id = card.dataset.id;
            if (state.selected.has(id)) card.classList.add('selected');
            if (state.excluded.has(id)) card.classList.add('excluded');
        });
        updateCounts();

        // Click handlers
        document.querySelectorAll('.template-card').forEach(card => {
            card.addEventListener('click', (e) => {
                const id = card.dataset.id;

                if (state.excluded.has(id)) {
                    // Excluded -> Unselected
                    state.excluded.delete(id);
                    card.classList.remove('excluded');
                } else if (state.selected.has(id)) {
                    // Selected -> Excluded
                    state.selected.delete(id);
                    state.excluded.add(id);
                    card.classList.remove('selected');
                    card.classList.add('excluded');
                } else {
                    // Unselected -> Selected
                    state.selected.add(id);
                    card.classList.add('selected');
                }

                saveState();
                updateCounts();
            });
        });

        // Filter handlers
        document.querySelectorAll('.filter-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                state.currentFilter = btn.dataset.category;
                applyFilter();
            });
        });

        function applyFilter() {
            document.querySelectorAll('.template-card').forEach(card => {
                const cats = card.dataset.categories.split(',');
                if (state.currentFilter === 'all' || cats.includes(state.currentFilter)) {
                    card.classList.remove('hidden');
                } else {
                    card.classList.add('hidden');
                }
            });
            updateCounts();
        }

        function updateCounts() {
            const visible = document.querySelectorAll('.template-card:not(.hidden)');
            document.getElementById('total-count').textContent = visible.length;

            let selected = 0, excluded = 0;
            visible.forEach(card => {
                const id = card.dataset.id;
                if (state.selected.has(id)) selected++;
                if (state.excluded.has(id)) excluded++;
            });

            document.getElementById('selected-count').textContent = state.selected.size;
            document.getElementById('excluded-count').textContent = state.excluded.size;
        }

        function saveState() {
            localStorage.setItem('templateReviewState', JSON.stringify({
                selected: Array.from(state.selected),
                excluded: Array.from(state.excluded)
            }));
        }

        function selectAll() {
            document.querySelectorAll('.template-card:not(.hidden):not(.excluded)').forEach(card => {
                const id = card.dataset.id;
                state.selected.add(id);
                card.classList.add('selected');
            });
            saveState();
            updateCounts();
        }

        function clearAll() {
            state.selected.clear();
            state.excluded.clear();
            document.querySelectorAll('.template-card').forEach(card => {
                card.classList.remove('selected', 'excluded');
            });
            saveState();
            updateCounts();
        }

        function exportSelection() {
            const selectedTemplates = [];
            document.querySelectorAll('.template-card').forEach(card => {
                const id = card.dataset.id;
                if (state.selected.has(id)) {
                    selectedTemplates.push({
                        file: card.dataset.file,
                        categories: card.dataset.categories.split(','),
                        score: parseInt(card.dataset.score)
                    });
                }
            });

            document.getElementById('export-data').value = JSON.stringify({
                count: selectedTemplates.length,
                exported_at: new Date().toISOString(),
                items: selectedTemplates
            }, null, 2);

            document.getElementById('export-modal').classList.add('show');
        }

        function closeModal() {
            document.getElementById('export-modal').classList.remove('show');
        }

        function copyExport() {
            const textarea = document.getElementById('export-data');
            textarea.select();
            document.execCommand('copy');
            alert('Copied to clipboard!');
        }
    </script>
</body>
</html>
'''

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Review page generated: {output_path}")
    print(f"Total templates: {len(templates)}")


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Generate template review page')
    parser.add_argument('--input', '-i', default='data/tokenized/tokenized_index.json',
                        help='Input index file')
    parser.add_argument('--output', '-o', default='review.html',
                        help='Output HTML file')
    args = parser.parse_args()

    with open(args.input) as f:
        data = json.load(f)

    templates = data.get('items', data)
    generate_review_html(templates, args.output)


if __name__ == '__main__':
    main()

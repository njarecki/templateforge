#!/usr/bin/env python3
"""
Generate a review page showing ORIGINAL templates with real images.
No tokenization - pure originals for visual evaluation.
"""

import json
import os

def generate_review_html(templates: list, output_path: str):
    """Generate the review page HTML with original templates."""

    html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Template Review - Original Graphics</title>
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
        .instructions {
            color: #888;
            margin: 0 0 15px 0;
            font-size: 14px;
        }
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
        .actions {
            display: flex;
            gap: 10px;
            margin-top: 15px;
            flex-wrap: wrap;
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
        .action-btn.danger { background: #dc2626; color: white; }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(500px, 1fr));
            gap: 24px;
        }
        .template-card {
            background: #1a1a1a;
            border-radius: 12px;
            overflow: hidden;
            transition: all 0.2s;
            cursor: pointer;
            border: 4px solid transparent;
        }
        .template-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 30px rgba(0,0,0,0.5);
        }
        .template-card.selected { border-color: #22c55e; }
        .template-card.excluded {
            opacity: 0.15;
            border-color: #ef4444;
            transform: scale(0.95);
        }
        .preview-frame {
            width: 100%;
            height: 600px;
            border: none;
            background: white;
        }
        .card-info {
            padding: 16px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #111;
        }
        .card-title {
            font-size: 13px;
            color: #aaa;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            max-width: 300px;
        }
        .card-meta {
            display: flex;
            gap: 12px;
            align-items: center;
        }
        .score {
            font-size: 14px;
            font-weight: 700;
            padding: 4px 10px;
            border-radius: 6px;
            background: #22c55e;
            color: #000;
        }
        .status-indicator {
            width: 16px;
            height: 16px;
            border-radius: 50%;
            background: #444;
            border: 2px solid #666;
        }
        .template-card.selected .status-indicator {
            background: #22c55e;
            border-color: #22c55e;
        }
        .template-card.excluded .status-indicator {
            background: #ef4444;
            border-color: #ef4444;
        }
        .idx {
            font-size: 11px;
            color: #666;
            font-weight: 600;
        }
        #export-modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0,0,0,0.9);
            z-index: 2000;
            align-items: center;
            justify-content: center;
        }
        #export-modal.show { display: flex; }
        .modal-content {
            background: #1a1a1a;
            padding: 30px;
            border-radius: 12px;
            max-width: 700px;
            width: 90%;
        }
        .modal-content h2 { margin-top: 0; }
        .modal-content textarea {
            width: 100%;
            height: 350px;
            background: #0a0a0a;
            border: 1px solid #333;
            color: #fff;
            padding: 15px;
            font-family: 'SF Mono', Monaco, monospace;
            font-size: 11px;
            border-radius: 8px;
            resize: vertical;
        }
        .modal-buttons {
            margin-top: 20px;
            display: flex;
            gap: 10px;
        }
        .progress-bar {
            height: 4px;
            background: #333;
            border-radius: 2px;
            overflow: hidden;
            margin-top: 10px;
        }
        .progress-fill {
            height: 100%;
            background: #22c55e;
            transition: width 0.3s;
        }
        .keyboard-hint {
            font-size: 12px;
            color: #666;
            margin-top: 10px;
        }
        .keyboard-hint kbd {
            background: #333;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: monospace;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Template Review - Original Graphics</h1>
        <p class="instructions">
            <strong>Click</strong> to select (green) &nbsp;|&nbsp;
            <strong>Click again</strong> to exclude (red/dimmed) &nbsp;|&nbsp;
            <strong>Click third time</strong> to reset
        </p>
        <div class="stats">
            <div class="stat">Total: <strong id="total-count">0</strong></div>
            <div class="stat selected">Selected: <strong id="selected-count">0</strong></div>
            <div class="stat excluded">Excluded: <strong id="excluded-count">0</strong></div>
        </div>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 0%"></div>
        </div>
        <div class="actions">
            <button class="action-btn primary" onclick="exportSelection()">Export Selected</button>
            <button class="action-btn secondary" onclick="selectAllUnreviewed()">Select All Unreviewed</button>
            <button class="action-btn danger" onclick="clearAll()">Reset All</button>
        </div>
        <div class="keyboard-hint">
            Tip: Use <kbd>j</kbd>/<kbd>k</kbd> to navigate, <kbd>s</kbd> to select, <kbd>x</kbd> to exclude
        </div>
    </div>

    <div class="grid" id="template-grid">
'''

    # Add each template
    for i, t in enumerate(templates):
        abs_path = t.get('abs_path', '')
        if not abs_path or not os.path.exists(abs_path):
            continue

        try:
            with open(abs_path, 'r', encoding='utf-8', errors='ignore') as f:
                template_html = f.read()
        except:
            continue

        # Escape for srcdoc
        escaped = template_html.replace('&', '&amp;').replace('"', '&quot;')

        file_name = t.get('file', os.path.basename(abs_path))
        score = t.get('score', 0)

        html += f'''
        <div class="template-card" data-id="{i}" data-file="{file_name}" data-score="{score}">
            <iframe class="preview-frame" srcdoc="{escaped}" loading="lazy"></iframe>
            <div class="card-info">
                <div>
                    <span class="idx">#{i+1}</span>
                    <span class="card-title" title="{file_name}">{file_name}</span>
                </div>
                <div class="card-meta">
                    <span class="score">{score}</span>
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
            <p style="color: #888;">Copy this JSON and save it to <code>data/index/final_curated.json</code></p>
            <textarea id="export-data" readonly></textarea>
            <div class="modal-buttons">
                <button class="action-btn secondary" onclick="closeModal()">Close</button>
                <button class="action-btn primary" onclick="copyExport()">Copy to Clipboard</button>
            </div>
        </div>
    </div>

    <script>
        const state = {
            selected: new Set(),
            excluded: new Set(),
            currentIndex: 0
        };

        const cards = document.querySelectorAll('.template-card');
        const total = cards.length;

        // Load from localStorage
        const saved = localStorage.getItem('originalReviewState');
        if (saved) {
            const parsed = JSON.parse(saved);
            state.selected = new Set(parsed.selected || []);
            state.excluded = new Set(parsed.excluded || []);
        }

        // Apply initial state
        cards.forEach(card => {
            const id = card.dataset.id;
            if (state.selected.has(id)) card.classList.add('selected');
            if (state.excluded.has(id)) card.classList.add('excluded');
        });
        updateCounts();

        // Click handlers
        cards.forEach(card => {
            card.addEventListener('click', () => toggleCard(card));
        });

        function toggleCard(card) {
            const id = card.dataset.id;

            if (state.excluded.has(id)) {
                state.excluded.delete(id);
                card.classList.remove('excluded');
            } else if (state.selected.has(id)) {
                state.selected.delete(id);
                state.excluded.add(id);
                card.classList.remove('selected');
                card.classList.add('excluded');
            } else {
                state.selected.add(id);
                card.classList.add('selected');
            }

            saveState();
            updateCounts();
        }

        function updateCounts() {
            document.getElementById('total-count').textContent = total;
            document.getElementById('selected-count').textContent = state.selected.size;
            document.getElementById('excluded-count').textContent = state.excluded.size;

            const reviewed = state.selected.size + state.excluded.size;
            const pct = (reviewed / total * 100).toFixed(0);
            document.getElementById('progress-fill').style.width = pct + '%';
        }

        function saveState() {
            localStorage.setItem('originalReviewState', JSON.stringify({
                selected: Array.from(state.selected),
                excluded: Array.from(state.excluded)
            }));
        }

        function selectAllUnreviewed() {
            cards.forEach(card => {
                const id = card.dataset.id;
                if (!state.selected.has(id) && !state.excluded.has(id)) {
                    state.selected.add(id);
                    card.classList.add('selected');
                }
            });
            saveState();
            updateCounts();
        }

        function clearAll() {
            if (!confirm('Reset all selections?')) return;
            state.selected.clear();
            state.excluded.clear();
            cards.forEach(card => card.classList.remove('selected', 'excluded'));
            saveState();
            updateCounts();
        }

        function exportSelection() {
            const selectedTemplates = [];
            cards.forEach(card => {
                const id = card.dataset.id;
                if (state.selected.has(id)) {
                    selectedTemplates.push({
                        file: card.dataset.file,
                        score: parseInt(card.dataset.score),
                        id: id
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
            alert('Copied! Save to data/index/final_curated.json');
        }

        // Keyboard navigation
        document.addEventListener('keydown', (e) => {
            if (e.target.tagName === 'TEXTAREA') return;

            const visibleCards = Array.from(cards).filter(c => !c.classList.contains('excluded'));

            switch(e.key) {
                case 'j':
                    state.currentIndex = Math.min(state.currentIndex + 1, visibleCards.length - 1);
                    visibleCards[state.currentIndex]?.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    break;
                case 'k':
                    state.currentIndex = Math.max(state.currentIndex - 1, 0);
                    visibleCards[state.currentIndex]?.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    break;
                case 's':
                    if (visibleCards[state.currentIndex]) {
                        const card = visibleCards[state.currentIndex];
                        const id = card.dataset.id;
                        if (!state.selected.has(id)) {
                            state.selected.add(id);
                            card.classList.add('selected');
                            saveState();
                            updateCounts();
                        }
                    }
                    break;
                case 'x':
                    if (visibleCards[state.currentIndex]) {
                        const card = visibleCards[state.currentIndex];
                        const id = card.dataset.id;
                        state.selected.delete(id);
                        state.excluded.add(id);
                        card.classList.remove('selected');
                        card.classList.add('excluded');
                        saveState();
                        updateCounts();
                    }
                    break;
            }
        });
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

    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', default='data/index/curated_top300.json')
    parser.add_argument('--output', '-o', default='review_originals.html')
    args = parser.parse_args()

    with open(args.input) as f:
        data = json.load(f)

    templates = data.get('items', data)
    generate_review_html(templates, args.output)


if __name__ == '__main__':
    main()

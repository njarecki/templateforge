#!/usr/bin/env python3
"""
Auto-tokenize scraped templates for reuse with design tokens.

This script:
1. Extracts color palette from each template
2. Maps colors to design tokens ({brandBG}, {brandPrimary}, etc.)
3. Replaces broken images with placeholders
4. Outputs tokenized templates ready for AI customization
"""

import re
import json
import os
import hashlib
from pathlib import Path
from collections import Counter
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
import colorsys

# Design tokens to use
DESIGN_TOKENS = {
    'bg': '{brandBG}',
    'primary': '{brandPrimary}',
    'secondary': '{brandSecondary}',
    'text': '{brandText}',
    'accent': '{brandAccent}',
}

FONT_TOKEN = '{brandFont}'

# Common placeholder service
PLACEHOLDER_BASE = 'https://placehold.co'


@dataclass
class ColorInfo:
    """Information about a color extracted from a template."""
    hex_value: str
    count: int
    contexts: List[str]  # 'background', 'text', 'border', 'button'
    luminance: float


def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 3:
        hex_color = ''.join(c * 2 for c in hex_color)
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def get_luminance(hex_color: str) -> float:
    """Calculate relative luminance of a color (0=black, 1=white)."""
    try:
        r, g, b = hex_to_rgb(hex_color)
        # Normalize to 0-1
        r, g, b = r/255, g/255, b/255
        # Apply gamma correction
        r = r/12.92 if r <= 0.03928 else ((r+0.055)/1.055)**2.4
        g = g/12.92 if g <= 0.03928 else ((g+0.055)/1.055)**2.4
        b = b/12.92 if b <= 0.03928 else ((b+0.055)/1.055)**2.4
        return 0.2126*r + 0.7152*g + 0.0722*b
    except:
        return 0.5


def extract_colors(html: str) -> Dict[str, ColorInfo]:
    """Extract all colors from HTML with usage context."""
    colors = {}

    # Find hex colors
    hex_pattern = r'#([0-9a-fA-F]{3,6})\b'

    # Different context patterns
    bg_patterns = [
        r'background[-\s]*color\s*:\s*(#[0-9a-fA-F]{3,6})',
        r'background\s*:\s*(#[0-9a-fA-F]{3,6})',
        r'bgcolor\s*=\s*["\']?(#[0-9a-fA-F]{3,6})',
    ]

    text_patterns = [
        r'(?<!background-)color\s*:\s*(#[0-9a-fA-F]{3,6})',
    ]

    border_patterns = [
        r'border[-\w]*\s*:\s*[^;]*(#[0-9a-fA-F]{3,6})',
    ]

    # Extract with context
    for pattern in bg_patterns:
        for match in re.finditer(pattern, html, re.I):
            hex_val = match.group(1).upper().lstrip('#')
            if len(hex_val) == 3:
                hex_val = ''.join(c*2 for c in hex_val)
            hex_val = '#' + hex_val
            if hex_val not in colors:
                colors[hex_val] = ColorInfo(hex_val, 0, [], get_luminance(hex_val))
            colors[hex_val].count += 1
            if 'background' not in colors[hex_val].contexts:
                colors[hex_val].contexts.append('background')

    for pattern in text_patterns:
        for match in re.finditer(pattern, html, re.I):
            hex_val = match.group(1).upper().lstrip('#')
            if len(hex_val) == 3:
                hex_val = ''.join(c*2 for c in hex_val)
            hex_val = '#' + hex_val
            if hex_val not in colors:
                colors[hex_val] = ColorInfo(hex_val, 0, [], get_luminance(hex_val))
            colors[hex_val].count += 1
            if 'text' not in colors[hex_val].contexts:
                colors[hex_val].contexts.append('text')

    # Find button/CTA colors (look for buttons, links with background)
    button_patterns = [
        r'<a[^>]*style\s*=\s*["\'][^"\']*background[-\s]*color\s*:\s*(#[0-9a-fA-F]{3,6})',
        r'<a[^>]*style\s*=\s*["\'][^"\']*background\s*:\s*(#[0-9a-fA-F]{3,6})',
        r'class\s*=\s*["\'][^"\']*(?:btn|button|cta)[^"\']*["\'][^>]*style\s*=\s*["\'][^"\']*(?:background|bgcolor)\s*[:\s=]\s*(#[0-9a-fA-F]{3,6})',
    ]

    for pattern in button_patterns:
        for match in re.finditer(pattern, html, re.I):
            hex_val = match.group(1).upper().lstrip('#')
            if len(hex_val) == 3:
                hex_val = ''.join(c*2 for c in hex_val)
            hex_val = '#' + hex_val
            if hex_val not in colors:
                colors[hex_val] = ColorInfo(hex_val, 0, [], get_luminance(hex_val))
            colors[hex_val].count += 1
            if 'button' not in colors[hex_val].contexts:
                colors[hex_val].contexts.append('button')

    return colors


def map_colors_to_tokens(colors: Dict[str, ColorInfo]) -> Dict[str, str]:
    """
    Map extracted colors to design tokens.

    Strategy:
    - Highest luminance background color → brandBG (or lowest if dark theme)
    - Button colors → brandAccent
    - Most common text color → brandText
    - Heading/primary color → brandPrimary
    - Lighter text → brandSecondary
    """
    if not colors:
        return {}

    mapping = {}
    used_tokens = set()

    # Sort colors by different criteria
    bg_colors = [(h, c) for h, c in colors.items() if 'background' in c.contexts]
    text_colors = [(h, c) for h, c in colors.items() if 'text' in c.contexts]
    button_colors = [(h, c) for h, c in colors.items() if 'button' in c.contexts]

    # Determine if dark or light theme based on most common background
    is_dark_theme = False
    if bg_colors:
        main_bg = max(bg_colors, key=lambda x: x[1].count)
        is_dark_theme = main_bg[1].luminance < 0.5

    # Map background color
    if bg_colors:
        # Pick the most common background
        main_bg = max(bg_colors, key=lambda x: x[1].count)
        mapping[main_bg[0]] = DESIGN_TOKENS['bg']
        used_tokens.add('bg')

    # Map button/accent color
    if button_colors:
        # Pick the most common button color (excluding white/black)
        accent_candidates = [(h, c) for h, c in button_colors if 0.1 < c.luminance < 0.9]
        if accent_candidates:
            accent = max(accent_candidates, key=lambda x: x[1].count)
            if accent[0] not in mapping:
                mapping[accent[0]] = DESIGN_TOKENS['accent']
                used_tokens.add('accent')

    # Map text colors
    if text_colors:
        # Sort by count
        sorted_text = sorted(text_colors, key=lambda x: -x[1].count)

        for hex_val, info in sorted_text:
            if hex_val in mapping:
                continue

            # Very dark or very light text → brandText
            if 'text' not in used_tokens and (info.luminance < 0.2 or info.luminance > 0.8):
                mapping[hex_val] = DESIGN_TOKENS['text']
                used_tokens.add('text')
            # Medium luminance text → brandSecondary
            elif 'secondary' not in used_tokens and 0.3 < info.luminance < 0.7:
                mapping[hex_val] = DESIGN_TOKENS['secondary']
                used_tokens.add('secondary')
            # Otherwise → brandPrimary
            elif 'primary' not in used_tokens:
                mapping[hex_val] = DESIGN_TOKENS['primary']
                used_tokens.add('primary')

    # Fill in any remaining common colors
    all_colors = sorted(colors.items(), key=lambda x: -x[1].count)
    for hex_val, info in all_colors:
        if hex_val in mapping:
            continue

        # Skip near-white and near-black for remaining slots
        if info.luminance < 0.05 or info.luminance > 0.95:
            continue

        if 'accent' not in used_tokens and 0.2 < info.luminance < 0.8:
            mapping[hex_val] = DESIGN_TOKENS['accent']
            used_tokens.add('accent')
        elif 'primary' not in used_tokens:
            mapping[hex_val] = DESIGN_TOKENS['primary']
            used_tokens.add('primary')
        elif 'secondary' not in used_tokens:
            mapping[hex_val] = DESIGN_TOKENS['secondary']
            used_tokens.add('secondary')

    return mapping


def extract_fonts(html: str) -> List[str]:
    """Extract font families from HTML."""
    font_pattern = r'font-family\s*:\s*([^;}"\']+)'
    fonts = re.findall(font_pattern, html, re.I)
    # Clean up
    cleaned = []
    for f in fonts:
        f = f.strip().strip('"\'')
        if f and f not in cleaned:
            cleaned.append(f)
    return cleaned


def fix_images(html: str) -> str:
    """Replace broken/external images with placeholders."""

    def get_placeholder(width: int, height: int, text: str = '') -> str:
        """Generate placehold.co URL."""
        if text:
            return f"{PLACEHOLDER_BASE}/{width}x{height}/png?text={text.replace(' ', '+')}"
        return f"{PLACEHOLDER_BASE}/{width}x{height}/png"

    def replace_img(match):
        full_tag = match.group(0)
        src = match.group(1) or match.group(2) or match.group(3)

        # Skip data URIs and local placeholders
        if src.startswith('data:') or 'placehold' in src.lower():
            return full_tag

        # Try to extract dimensions
        width_match = re.search(r'width\s*=\s*["\']?(\d+)', full_tag, re.I)
        height_match = re.search(r'height\s*=\s*["\']?(\d+)', full_tag, re.I)

        width = int(width_match.group(1)) if width_match else 300
        height = int(height_match.group(1)) if height_match else 200

        # Cap dimensions
        width = min(width, 640)
        height = min(height, 480)

        # Determine placeholder text based on context
        alt_match = re.search(r'alt\s*=\s*["\']([^"\']*)["\']', full_tag, re.I)
        text = alt_match.group(1) if alt_match else 'Image'
        text = text[:20]  # Truncate

        new_src = get_placeholder(width, height, text)

        # Replace src in the tag
        new_tag = re.sub(r'src\s*=\s*["\'][^"\']*["\']', f'src="{new_src}"', full_tag)
        return new_tag

    # Match img tags with src attribute
    img_pattern = r'<img[^>]*src\s*=\s*(?:"([^"]*)"|\'([^\']*)\'|([^\s>]+))[^>]*>'

    return re.sub(img_pattern, replace_img, html, flags=re.I)


def tokenize_template(html: str) -> Tuple[str, Dict]:
    """
    Tokenize a template by replacing colors and fonts with design tokens.

    Returns:
        Tuple of (tokenized_html, metadata)
    """
    # Extract colors and map to tokens
    colors = extract_colors(html)
    color_mapping = map_colors_to_tokens(colors)

    # Extract fonts
    fonts = extract_fonts(html)

    # Apply color replacements (case-insensitive)
    tokenized = html
    for hex_color, token in color_mapping.items():
        # Handle both formats: #FFFFFF and #ffffff
        pattern = re.compile(re.escape(hex_color), re.I)
        tokenized = pattern.sub(token, tokenized)

    # Replace fonts with token
    for font in fonts:
        if font.strip():
            tokenized = tokenized.replace(font, FONT_TOKEN)

    # Fix broken images
    tokenized = fix_images(tokenized)

    # Build metadata
    metadata = {
        'original_colors': {k: {'count': v.count, 'contexts': v.contexts, 'luminance': v.luminance}
                           for k, v in colors.items()},
        'color_mapping': color_mapping,
        'original_fonts': fonts,
        'tokens_used': list(set(color_mapping.values())) + ([FONT_TOKEN] if fonts else []),
    }

    return tokenized, metadata


def categorize_template(html: str, filename: str) -> List[str]:
    """
    Auto-categorize a template based on content and filename.

    Returns list of categories.
    """
    categories = []
    html_lower = html.lower()
    filename_lower = filename.lower()

    # Category keywords
    category_rules = {
        'Welcome': ['welcome', 'onboard', 'getting started', 'join', 'signup', 'sign up'],
        'Newsletter': ['newsletter', 'digest', 'weekly', 'monthly', 'roundup', 'stories', 'article'],
        'Promo': ['sale', 'discount', 'off', 'promo', 'deal', 'offer', 'launch', 'announce', 'new arrival'],
        'Transactional': ['receipt', 'invoice', 'confirm', 'order', 'ship', 'track', 'password', 'reset', 'verify', 'notification'],
        'Ecommerce': ['cart', 'abandon', 'product', 'shop', 'buy', 'purchase', 'review', 'recommend'],
    }

    for category, keywords in category_rules.items():
        for kw in keywords:
            if kw in html_lower or kw in filename_lower:
                if category not in categories:
                    categories.append(category)
                break

    # Default to Newsletter if no match
    if not categories:
        categories = ['Newsletter']

    return categories


def process_template(input_path: str, output_dir: str) -> Optional[Dict]:
    """
    Process a single template file.

    Returns metadata dict or None if failed.
    """
    try:
        with open(input_path, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()

        # Tokenize
        tokenized_html, metadata = tokenize_template(html)

        # Categorize
        categories = categorize_template(html, os.path.basename(input_path))

        # Generate output path
        rel_path = os.path.basename(input_path)
        output_path = os.path.join(output_dir, rel_path)

        # Write tokenized template
        os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else output_dir, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(tokenized_html)

        return {
            'input_path': input_path,
            'output_path': output_path,
            'categories': categories,
            'tokens_used': metadata['tokens_used'],
            'color_mapping': metadata['color_mapping'],
        }

    except Exception as e:
        print(f"Error processing {input_path}: {e}")
        return None


def main():
    """Process all curated templates."""
    import argparse

    parser = argparse.ArgumentParser(description='Tokenize email templates')
    parser.add_argument('--input', '-i', default='data/index/curated_top300.json',
                        help='Input index file (default: curated_top300.json)')
    parser.add_argument('--output-dir', '-o', default='data/tokenized',
                        help='Output directory for tokenized templates')
    parser.add_argument('--limit', '-n', type=int, default=0,
                        help='Limit number of templates to process (0 = all)')
    args = parser.parse_args()

    # Load input index
    with open(args.input) as f:
        data = json.load(f)

    items = data.get('items', data) if isinstance(data, dict) else data

    if args.limit > 0:
        items = items[:args.limit]

    print(f"Processing {len(items)} templates...")

    # Process each template
    results = []
    os.makedirs(args.output_dir, exist_ok=True)

    for i, item in enumerate(items):
        input_path = item.get('abs_path', item.get('file_path'))
        if not input_path:
            continue

        # Create subdirectory structure
        rel_file = item.get('file', os.path.basename(input_path))
        output_subdir = os.path.join(args.output_dir, os.path.dirname(rel_file))
        os.makedirs(output_subdir, exist_ok=True)

        result = process_template(input_path, output_subdir)
        if result:
            result['original_score'] = item.get('score', 0)
            result['file'] = rel_file
            results.append(result)

        if (i + 1) % 50 == 0:
            print(f"  Processed {i + 1}/{len(items)}...")

    # Save results index
    output_index = os.path.join(args.output_dir, 'tokenized_index.json')
    with open(output_index, 'w') as f:
        json.dump({'items': results, 'count': len(results)}, f, indent=2)

    print(f"\nDone! Processed {len(results)} templates")
    print(f"Output directory: {args.output_dir}")
    print(f"Index file: {output_index}")

    # Print category distribution
    from collections import Counter
    all_cats = []
    for r in results:
        all_cats.extend(r['categories'])
    print(f"\nCategory distribution:")
    for cat, count in Counter(all_cats).most_common():
        print(f"  {cat}: {count}")


if __name__ == '__main__':
    main()

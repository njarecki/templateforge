#!/usr/bin/env python3
"""
External Template Sources

Fetches and parses email templates from public MJML/HTML sources.
Converts them to TopMail design system format.
"""

import re
import json
import urllib.request
import urllib.error
from typing import Dict, List, Optional, Any
from html.parser import HTMLParser


# Public MJML template repositories and sources
EXTERNAL_SOURCES = {
    "mjml_templates": {
        "name": "MJML Email Templates",
        "base_url": "https://raw.githubusercontent.com/mjmlio/email-templates/master/templates",
        "templates": [
            "welcome-email.mjml",
            "newsletter.mjml",
            "receipt-email.mjml",
            "reactivation-email.mjml",
            "referral-email.mjml",
            "black-friday.mjml",
            "christmas.mjml",
            "card.mjml",
            "basic.mjml",
            "onepage.mjml",
        ],
        "type": "mjml"
    },
    "foundation_emails": {
        "name": "Foundation for Emails",
        "base_url": "https://raw.githubusercontent.com/foundation/foundation-emails/develop/templates",
        "templates": [
            "newsletter.html",
            "drip.html",
            "marketing.html",
            "sidebar.html",
            "sidebar-hero.html",
        ],
        "type": "html"
    },
}


class MJMLParser(HTMLParser):
    """Parse MJML to extract structure and content."""

    def __init__(self):
        super().__init__()
        self.sections = []
        self.current_section = None
        self.current_content = []
        self.in_text = False
        self.mjml_tags = {
            'mj-hero': 'hero',
            'mj-section': 'section',
            'mj-column': 'column',
            'mj-text': 'text',
            'mj-button': 'button',
            'mj-image': 'image',
            'mj-divider': 'divider',
            'mj-social': 'social',
            'mj-navbar': 'navbar',
            'mj-table': 'table',
        }

    def handle_starttag(self, tag, attrs):
        tag_lower = tag.lower()
        if tag_lower in self.mjml_tags:
            self.current_section = {
                'mjml_tag': tag_lower,
                'section_type': self.mjml_tags[tag_lower],
                'attrs': dict(attrs),
                'content': []
            }
        if tag_lower == 'mj-text':
            self.in_text = True
            self.current_content = []

    def handle_endtag(self, tag):
        tag_lower = tag.lower()
        if tag_lower == 'mj-text' and self.in_text:
            self.in_text = False
            if self.current_section:
                self.current_section['content'].append(''.join(self.current_content))
        if tag_lower in self.mjml_tags and self.current_section:
            if self.current_section['mjml_tag'] == tag_lower:
                self.sections.append(self.current_section)
                self.current_section = None

    def handle_data(self, data):
        if self.in_text:
            self.current_content.append(data.strip())


class HTMLEmailParser(HTMLParser):
    """Parse HTML emails to extract structure."""

    def __init__(self):
        super().__init__()
        self.sections = []
        self.current_depth = 0
        self.in_table = False
        self.table_depth = 0
        self.current_section_content = []

    def handle_starttag(self, tag, attrs):
        if tag == 'table':
            self.table_depth += 1
            if self.table_depth == 2:  # Main content tables
                self.current_section_content = []
        self.current_section_content.append(f'<{tag}>')

    def handle_endtag(self, tag):
        self.current_section_content.append(f'</{tag}>')
        if tag == 'table':
            if self.table_depth == 2 and self.current_section_content:
                self.sections.append({
                    'html': ''.join(self.current_section_content),
                    'type': 'extracted_section'
                })
            self.table_depth -= 1

    def handle_data(self, data):
        if data.strip():
            self.current_section_content.append(data)


def fetch_url(url: str, timeout: int = 10) -> Optional[str]:
    """Fetch content from a URL."""
    try:
        headers = {
            'User-Agent': 'TemplateForge/1.0 (Email Template Generator)'
        }
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        print(f"  HTTP Error {e.code}: {url}")
        return None
    except urllib.error.URLError as e:
        print(f"  URL Error: {e.reason}")
        return None
    except Exception as e:
        print(f"  Error fetching {url}: {e}")
        return None


def parse_mjml_structure(mjml_content: str) -> Dict[str, Any]:
    """Parse MJML content and extract structure."""
    parser = MJMLParser()
    try:
        parser.feed(mjml_content)
    except Exception as e:
        print(f"  MJML parsing error: {e}")
        return {'sections': [], 'raw': mjml_content}

    return {
        'sections': parser.sections,
        'raw': mjml_content
    }


def parse_html_structure(html_content: str) -> Dict[str, Any]:
    """Parse HTML email content and extract structure."""
    parser = HTMLEmailParser()
    try:
        parser.feed(html_content)
    except Exception as e:
        print(f"  HTML parsing error: {e}")
        return {'sections': [], 'raw': html_content}

    return {
        'sections': parser.sections,
        'raw': html_content
    }


def map_mjml_to_section_type(mjml_tag: str, attrs: dict) -> str:
    """Map MJML tags to TopMail section types."""
    mapping = {
        'mj-hero': 'hero',
        'mj-navbar': 'header_nav',
        'mj-button': 'cta_band',
        'mj-social': 'social_icons',
        'mj-divider': 'divider',
        'mj-table': 'order_summary',
    }

    if mjml_tag == 'mj-section':
        # Infer type from attributes or content
        if attrs.get('full-width') == 'full-width':
            return 'hero'
        if 'background-color' in attrs:
            return 'cta_band'
        return '1col_text'

    return mapping.get(mjml_tag, '1col_text')


def normalize_external_template(parsed_template: Dict, source_name: str) -> Dict:
    """Convert a parsed template to TopMail normalized format."""
    sections_used = []

    for section in parsed_template.get('sections', []):
        if 'mjml_tag' in section:
            section_type = map_mjml_to_section_type(
                section['mjml_tag'],
                section.get('attrs', {})
            )
        else:
            section_type = section.get('type', 'generic')

        if section_type not in sections_used:
            sections_used.append(section_type)

    # Ensure we have header and footer
    if 'header_nav' not in sections_used:
        sections_used.insert(0, 'header_nav')
    if 'footer_simple' not in sections_used:
        sections_used.append('footer_simple')

    return {
        'source': source_name,
        'sections_extracted': sections_used,
        'section_count': len(sections_used),
        'raw_content': parsed_template.get('raw', '')[:500] + '...'  # Truncated for reference
    }


def fetch_templates_from_source(source_id: str, verbose: bool = True) -> List[Dict]:
    """Fetch all templates from a specific source."""
    if source_id not in EXTERNAL_SOURCES:
        raise ValueError(f"Unknown source: {source_id}")

    source = EXTERNAL_SOURCES[source_id]
    templates = []

    if verbose:
        print(f"Fetching from {source['name']}...")

    for template_file in source['templates']:
        url = f"{source['base_url']}/{template_file}"

        if verbose:
            print(f"  Fetching: {template_file}")

        content = fetch_url(url)
        if not content:
            continue

        # Parse based on type
        if source['type'] == 'mjml':
            parsed = parse_mjml_structure(content)
        else:
            parsed = parse_html_structure(content)

        normalized = normalize_external_template(
            parsed,
            f"{source['name']}/{template_file}"
        )

        templates.append({
            'filename': template_file,
            'source_id': source_id,
            'source_name': source['name'],
            'type': source['type'],
            'parsed': parsed,
            'normalized': normalized
        })

    return templates


def fetch_all_external_templates(verbose: bool = True) -> Dict[str, Any]:
    """Fetch templates from all configured sources."""
    results = {
        'sources_queried': [],
        'templates_fetched': [],
        'errors': [],
        'summary': {
            'total_sources': len(EXTERNAL_SOURCES),
            'total_templates': 0,
            'successful_fetches': 0,
            'failed_fetches': 0
        }
    }

    if verbose:
        print("=" * 50)
        print("Fetching External Templates")
        print("=" * 50)

    for source_id in EXTERNAL_SOURCES.keys():
        source_info = EXTERNAL_SOURCES[source_id]
        results['sources_queried'].append({
            'id': source_id,
            'name': source_info['name'],
            'template_count': len(source_info['templates'])
        })

        try:
            templates = fetch_templates_from_source(source_id, verbose)
            results['templates_fetched'].extend(templates)
            results['summary']['successful_fetches'] += len(templates)
        except Exception as e:
            results['errors'].append({
                'source': source_id,
                'error': str(e)
            })
            results['summary']['failed_fetches'] += len(source_info['templates'])

    results['summary']['total_templates'] = len(results['templates_fetched'])

    if verbose:
        print()
        print(f"Summary: {results['summary']['total_templates']} templates fetched")
        print(f"  Successful: {results['summary']['successful_fetches']}")
        print(f"  Failed: {results['summary']['failed_fetches']}")

    return results


def extract_section_patterns(templates: List[Dict]) -> List[Dict]:
    """Extract unique section patterns from fetched templates."""
    patterns = {}

    for template in templates:
        normalized = template.get('normalized', {})
        for section_type in normalized.get('sections_extracted', []):
            if section_type not in patterns:
                patterns[section_type] = {
                    'type': section_type,
                    'occurrences': 0,
                    'sources': []
                }
            patterns[section_type]['occurrences'] += 1
            patterns[section_type]['sources'].append(template['filename'])

    return list(patterns.values())


def list_available_sources() -> List[Dict]:
    """List all configured external sources."""
    return [
        {
            'id': source_id,
            'name': source['name'],
            'type': source['type'],
            'template_count': len(source['templates']),
            'templates': source['templates']
        }
        for source_id, source in EXTERNAL_SOURCES.items()
    ]


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Fetch external email templates from public sources"
    )
    parser.add_argument(
        "--list-sources",
        action="store_true",
        help="List available template sources"
    )
    parser.add_argument(
        "--source", "-s",
        help="Fetch from specific source (mjml_templates, foundation_emails)"
    )
    parser.add_argument(
        "--output", "-o",
        help="Output file for fetched templates (JSON)"
    )
    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Suppress output"
    )

    args = parser.parse_args()

    if args.list_sources:
        print("Available external sources:")
        for source in list_available_sources():
            print(f"\n  {source['id']}:")
            print(f"    Name: {source['name']}")
            print(f"    Type: {source['type']}")
            print(f"    Templates: {', '.join(source['templates'])}")
        exit(0)

    verbose = not args.quiet

    if args.source:
        templates = fetch_templates_from_source(args.source, verbose)
        results = {'templates': templates}
    else:
        results = fetch_all_external_templates(verbose)

    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        if verbose:
            print(f"\nSaved to: {args.output}")
    elif not args.quiet:
        print("\nExtracted section patterns:")
        templates_list = results.get('templates_fetched', results.get('templates', []))
        patterns = extract_section_patterns(templates_list)
        for pattern in sorted(patterns, key=lambda x: -x['occurrences']):
            print(f"  {pattern['type']}: {pattern['occurrences']} occurrences")

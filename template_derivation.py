#!/usr/bin/env python3
"""
Template Derivation

Automatically derives new template types from external template sources.
Analyzes fetched MJML/HTML templates and creates matching template definitions.
"""

import re
from typing import Dict, List, Optional, Any, Tuple
from external_sources import (
    fetch_all_external_templates,
    fetch_templates_from_source,
    parse_mjml_structure,
    parse_html_structure,
)
from section_library import list_section_types


# Keywords to identify template category/intent
CATEGORY_KEYWORDS = {
    "Welcome": ["welcome", "hello", "hi there", "getting started", "get started", "thanks for joining", "onboard"],
    "Ecommerce": ["order", "cart", "shop", "product", "purchase", "buy", "shipping", "delivery", "receipt", "invoice"],
    "Newsletter": ["newsletter", "digest", "weekly", "monthly", "update", "news", "edition", "issue"],
    "Promo": ["sale", "discount", "offer", "deal", "promo", "flash", "limited", "exclusive", "black friday", "christmas", "holiday"],
    "SaaS": ["feature", "subscription", "plan", "upgrade", "trial", "account", "password", "verify", "confirm"],
    "Transactional": ["reset", "verify", "confirm", "security", "alert", "notification", "receipt"],
}

# MJML tag to section type mapping
MJML_SECTION_MAP = {
    "mj-hero": "hero",
    "mj-navbar": "header_nav",
    "mj-button": "cta_band",
    "mj-social": "social_icons",
    "mj-image": "hero",  # Large standalone images often act as hero
    "mj-divider": "divider",
    "mj-table": "order_summary",
    "mj-accordion": "accordion_faq",
}

# Content patterns that suggest certain section types
CONTENT_PATTERNS = {
    r"(star|rating|review|★)": "rating_stars",
    r"(price|\\$|€|£|\\d+\\.\\d{2}).*?/month|/year": "pricing_table",
    r"(progress|step\s+\d|complete)": "progress_tracker",
    r"(countdown|expires|ends in|hours|minutes)": "countdown_timer",
    r"(play|watch|video|youtube|vimeo)": "video_placeholder",
    r"(faq|question|answer|Q:|A:)": "accordion_faq",
    r"(team|meet|about us|our team)": "team_members",
    r"(compare|vs|versus|features)": "comparison_table",
    r"(stat|metric|\\d+[%+K])": "stats_metrics",
    r"(download|app store|google play|ios|android)": "app_store_badges",
    r"(event|webinar|conference|join us|rsvp)": "event_details",
    r"(order|shipping|tracking|delivery)": "shipping_tracker",
    r"(cart|items in|checkout)": "cart_item",
    r"(referral|invite|friend|share)": "1col_text",
    r"(reactivate|come back|miss you|inactive)": "1col_text",
}


def identify_category(template_data: Dict) -> str:
    """Identify the likely category of a template based on filename and content."""
    filename = template_data.get("filename", "").lower()
    raw_content = template_data.get("parsed", {}).get("raw", "").lower()

    # Check filename first for strong signals
    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in filename:
                return category

    # Check content for category keywords
    for category, keywords in CATEGORY_KEYWORDS.items():
        match_count = sum(1 for kw in keywords if kw in raw_content)
        if match_count >= 2:  # At least 2 keywords found
            return category

    # Default to Newsletter for generic templates
    return "Newsletter"


def infer_sections_from_mjml(parsed: Dict, available_sections: List[str]) -> List[str]:
    """Infer section types from parsed MJML structure."""
    sections = []
    seen_header = False
    seen_footer = False

    for section in parsed.get("sections", []):
        mjml_tag = section.get("mjml_tag", "")
        attrs = section.get("attrs", {})
        content = " ".join(section.get("content", [])).lower()

        # Map MJML tag to section type
        section_type = None

        if mjml_tag == "mj-navbar":
            section_type = "header_nav"
            seen_header = True
        elif mjml_tag == "mj-hero":
            section_type = "hero"
        elif mjml_tag == "mj-social":
            section_type = "social_icons"
        elif mjml_tag == "mj-divider":
            section_type = "divider"
        elif mjml_tag == "mj-button" and not sections:
            # Button at top might be part of hero
            continue
        elif mjml_tag == "mj-button":
            section_type = "cta_band"
        elif mjml_tag == "mj-section":
            # Analyze content patterns for mj-section
            section_type = infer_section_from_content(content, attrs, available_sections)

        if section_type and section_type in available_sections:
            if section_type not in sections[-3:] if sections else True:  # Avoid repetition
                sections.append(section_type)

    # Ensure header and footer
    if not seen_header and sections:
        sections.insert(0, "header_nav")
    if "footer" not in str(sections):
        sections.append("footer_simple")

    return sections


def infer_section_from_content(content: str, attrs: Dict, available_sections: List[str]) -> str:
    """Infer section type from text content and attributes."""
    # Check content patterns
    for pattern, section_type in CONTENT_PATTERNS.items():
        if re.search(pattern, content, re.IGNORECASE):
            if section_type in available_sections:
                return section_type

    # Check for column layouts
    if "column" in attrs.get("css-class", ""):
        return "2col_text_image"

    # Check for background color (often CTA bands)
    if "background-color" in attrs:
        return "cta_band"

    # Check for full-width (often hero)
    if attrs.get("full-width") == "full-width":
        return "hero"

    # Default to text block
    return "1col_text"


def infer_sections_from_html(parsed: Dict, available_sections: List[str]) -> List[str]:
    """Infer section types from parsed HTML structure."""
    sections = ["header_nav"]  # Start with header
    raw = parsed.get("raw", "").lower()

    # Look for common patterns in HTML
    if re.search(r"<img[^>]+hero|banner|header", raw, re.IGNORECASE):
        sections.append("hero")
    else:
        sections.append("subhero")

    # Check for various content patterns
    patterns_found = []
    for pattern, section_type in CONTENT_PATTERNS.items():
        if re.search(pattern, raw, re.IGNORECASE):
            if section_type in available_sections and section_type not in patterns_found:
                patterns_found.append(section_type)

    sections.extend(patterns_found[:3])  # Add up to 3 inferred sections

    # Add default content sections if nothing specific found
    if len(sections) < 4:
        sections.append("1col_text")

    # Add CTA and footer
    sections.append("cta_band")
    sections.append("footer_simple")

    return sections


def generate_template_name(filename: str, category: str) -> Tuple[str, str]:
    """Generate a template type ID and human-readable name from filename."""
    # Clean the filename
    base = filename.lower()
    base = re.sub(r"\.(mjml|html)$", "", base)
    base = re.sub(r"[^a-z0-9]+", "_", base)
    base = base.strip("_")

    # Generate type ID
    type_id = f"derived_{base}"

    # Generate human name
    words = base.split("_")
    name = " ".join(w.capitalize() for w in words)
    name = f"{name} ({category})"

    return type_id, name


def derive_template_from_external(template_data: Dict, available_sections: List[str]) -> Optional[Dict]:
    """Derive a template definition from an external template."""
    filename = template_data.get("filename", "unknown")
    template_type = template_data.get("type", "html")
    parsed = template_data.get("parsed", {})

    # Identify category
    category = identify_category(template_data)

    # Infer sections based on template type
    if template_type == "mjml":
        sections = infer_sections_from_mjml(parsed, available_sections)
    else:
        sections = infer_sections_from_html(parsed, available_sections)

    # Validate we have meaningful sections
    if len(sections) < 3:
        sections = ["header_nav", "hero", "1col_text", "cta_band", "footer_simple"]

    # Generate template identifiers
    type_id, name = generate_template_name(filename, category)

    return {
        "type_id": type_id,
        "definition": {
            "name": name,
            "category": category,
            "sections": sections,
            "description": f"Derived from {template_data.get('source_name', 'external source')}/{filename}",
        },
        "source": {
            "filename": filename,
            "source_name": template_data.get("source_name", "Unknown"),
            "type": template_type,
        }
    }


def derive_all_templates(verbose: bool = True) -> Dict[str, Any]:
    """
    Fetch external templates and derive template definitions from them.

    Returns a dictionary with:
    - derived_templates: List of derived template definitions
    - template_code: Python code to add these templates
    - summary: Statistics about derivation
    """
    if verbose:
        print("=" * 60)
        print("Template Derivation from External Sources")
        print("=" * 60)
        print()

    # Get available section types
    available_sections = list_section_types()
    if verbose:
        print(f"Available section types: {len(available_sections)}")

    # Fetch external templates
    if verbose:
        print("\nFetching external templates...")

    external_results = fetch_all_external_templates(verbose=verbose)
    templates = external_results.get("templates_fetched", [])

    if not templates:
        if verbose:
            print("No templates fetched. Using offline derivation.")
        return {
            "derived_templates": [],
            "template_code": "",
            "summary": {"total": 0, "successful": 0, "failed": 0}
        }

    # Derive templates
    if verbose:
        print(f"\nDeriving template definitions from {len(templates)} templates...")

    derived = []
    failed = []

    for template_data in templates:
        try:
            result = derive_template_from_external(template_data, available_sections)
            if result:
                derived.append(result)
                if verbose:
                    print(f"  ✓ {result['type_id']}: {len(result['definition']['sections'])} sections ({result['definition']['category']})")
        except Exception as e:
            failed.append({"filename": template_data.get("filename", "unknown"), "error": str(e)})
            if verbose:
                print(f"  ✗ {template_data.get('filename', 'unknown')}: {e}")

    # Generate code snippet for adding to template_generator.py
    code_lines = ["\n# Derived templates from external sources"]
    for d in derived:
        type_id = d["type_id"]
        defn = d["definition"]
        code_lines.append(f'    "{type_id}": {{')
        code_lines.append(f'        "name": "{defn["name"]}",')
        code_lines.append(f'        "category": "{defn["category"]}",')
        code_lines.append(f'        "sections": {defn["sections"]},')
        code_lines.append(f'        "description": "{defn["description"]}"')
        code_lines.append('    },')

    template_code = "\n".join(code_lines)

    if verbose:
        print()
        print("=" * 60)
        print(f"Derivation Summary:")
        print(f"  Templates fetched: {len(templates)}")
        print(f"  Successfully derived: {len(derived)}")
        print(f"  Failed: {len(failed)}")
        print("=" * 60)

    return {
        "derived_templates": derived,
        "template_code": template_code,
        "summary": {
            "total": len(templates),
            "successful": len(derived),
            "failed": len(failed),
            "categories": {}
        }
    }


def get_derived_template_types() -> Dict[str, Dict]:
    """
    Get derived template types ready to use with template_generator.

    Returns a dictionary suitable for merging with TEMPLATE_TYPES.
    """
    result = derive_all_templates(verbose=False)

    derived_types = {}
    for d in result.get("derived_templates", []):
        derived_types[d["type_id"]] = d["definition"]

    return derived_types


def print_derivation_report(results: Dict) -> None:
    """Print a detailed derivation report."""
    print("\n" + "=" * 70)
    print("TEMPLATE DERIVATION REPORT")
    print("=" * 70)

    derived = results.get("derived_templates", [])

    if not derived:
        print("\nNo templates were derived.")
        return

    # Group by category
    by_category = {}
    for d in derived:
        cat = d["definition"]["category"]
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(d)

    print(f"\nTotal derived: {len(derived)} templates\n")

    for category in sorted(by_category.keys()):
        templates = by_category[category]
        print(f"\n{category} ({len(templates)}):")
        print("-" * 40)
        for t in templates:
            print(f"  {t['type_id']}:")
            print(f"    Sections: {' → '.join(t['definition']['sections'][:5])}")
            if len(t['definition']['sections']) > 5:
                print(f"              ... and {len(t['definition']['sections']) - 5} more")
            print(f"    Source: {t['source']['source_name']}/{t['source']['filename']}")

    print("\n" + "=" * 70)
    print("CODE TO ADD TO template_generator.py:")
    print("=" * 70)
    print(results.get("template_code", ""))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Derive template types from external sources"
    )
    parser.add_argument(
        "--output", "-o",
        help="Output file for derived templates (JSON)"
    )
    parser.add_argument(
        "--code-output", "-c",
        help="Output file for Python code snippet"
    )
    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Suppress output"
    )
    parser.add_argument(
        "--report", "-r",
        action="store_true",
        help="Print detailed derivation report"
    )

    args = parser.parse_args()

    verbose = not args.quiet
    results = derive_all_templates(verbose=verbose)

    if args.output:
        import json
        with open(args.output, 'w') as f:
            json.dump(results["derived_templates"], f, indent=2)
        if verbose:
            print(f"\nSaved derived templates to: {args.output}")

    if args.code_output:
        with open(args.code_output, 'w') as f:
            f.write(results["template_code"])
        if verbose:
            print(f"Saved code snippet to: {args.code_output}")

    if args.report:
        print_derivation_report(results)

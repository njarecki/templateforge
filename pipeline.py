#!/usr/bin/env python3
"""
TemplateForge Pipeline

Main entry point for generating email templates.
Executes the full 7-step pipeline as defined in OBJECTIVE.md.
"""

import json
import sys
import os
from datetime import datetime, timezone

from template_generator import (
    generate_full_batch,
    generate_template,
    generate_all_skins_for_template,
    generate_layout_variant,
    list_template_types,
    TEMPLATE_TYPES,
)
from design_system import DESIGN_SKINS
from section_library import get_all_sections, list_section_types
from template_validator import validate_template, validate_batch, fix_template_issues


def run_pipeline(output_file=None, verbose=True):
    """
    Execute the full TemplateForge pipeline.

    Steps:
    1. Find/Reconstruct Templates (using built-in template definitions)
    2. Extract Section Modules
    3. Normalize Into TopMail Design System
    4. Generate 5 Design Skins For Each Template
    5. Generate 3 Layout Variants Per Template
    6. Self-Critique + Auto-Fix
    7. Return Final Output
    """
    if verbose:
        print("=" * 60)
        print("TemplateForge Pipeline")
        print("=" * 60)
        print()

    # Step 1: Source templates (built-in)
    if verbose:
        print("STEP 1: Initializing template sources...")
        print(f"  - {len(TEMPLATE_TYPES)} template types available")
        print(f"  - Categories: Welcome, SaaS, Ecommerce, Newsletter, Promo")
        print()

    # Step 2: Extract sections
    if verbose:
        print("STEP 2: Extracting section modules...")
        sections = list_section_types()
        print(f"  - {len(sections)} section types in library")
        print(f"  - Sections: {', '.join(sections[:8])}...")
        print()

    # Step 3-5: Generate full batch (normalized + skins + variants)
    if verbose:
        print("STEP 3-5: Generating templates...")
        print("  - Normalizing templates to TopMail design system")
        print("  - Generating 5 design skins per template")
        print("  - Generating 3 layout variants per template")
        print()

    batch = generate_full_batch()

    if verbose:
        print(f"  Generated:")
        print(f"    - {len(batch['normalizedTemplates'])} normalized templates")
        print(f"    - {len(batch['reskinnedTemplates'])} reskinned templates")
        print(f"    - {len(batch['layoutVariants'])} layout variants")
        print(f"    - {batch['metadata']['total_templates']} total templates")
        print()

    # Step 6: Validate and fix
    if verbose:
        print("STEP 6: Self-critique and auto-fix...")

    all_templates = (
        batch["normalizedTemplates"] +
        batch["reskinnedTemplates"] +
        batch["layoutVariants"]
    )

    validation_results = validate_batch(all_templates)

    if verbose:
        print(f"  - Validated {validation_results['total']} templates")
        print(f"  - Passed: {validation_results['passed']}")
        print(f"  - Fixed: {validation_results['fixed']}")
        if validation_results['issues']:
            print(f"  - Issues found: {len(validation_results['issues'])}")
        print()

    # Apply fixes to batch
    batch["normalizedTemplates"] = [
        fix_template_issues(t) for t in batch["normalizedTemplates"]
    ]
    batch["reskinnedTemplates"] = [
        fix_template_issues(t) for t in batch["reskinnedTemplates"]
    ]
    batch["layoutVariants"] = [
        fix_template_issues(t) for t in batch["layoutVariants"]
    ]

    # Add generation metadata
    batch["metadata"]["generated_at"] = datetime.now(timezone.utc).isoformat()
    batch["metadata"]["pipeline_version"] = "1.0.0"
    batch["metadata"]["validation"] = validation_results

    # Step 7: Output
    if verbose:
        print("STEP 7: Generating output...")
        print()

    if output_file:
        with open(output_file, "w") as f:
            json.dump(batch, f, indent=2)
        if verbose:
            print(f"Output saved to: {output_file}")
            print(f"File size: {os.path.getsize(output_file) / 1024:.1f} KB")
    else:
        if verbose:
            print("Returning JSON output...")

    if verbose:
        print()
        print("=" * 60)
        print("Pipeline complete!")
        print("=" * 60)

    return batch


def run_single_template(template_type, skin="apple_light", output_file=None):
    """Generate a single template with optional output to file."""
    template = generate_template(template_type, skin)
    template = fix_template_issues(template)

    if output_file:
        if output_file.endswith(".html"):
            with open(output_file, "w") as f:
                f.write(template["html"])
        else:
            with open(output_file, "w") as f:
                json.dump(template, f, indent=2)

    return template


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="TemplateForge - Email Template Generation Pipeline"
    )
    parser.add_argument(
        "--output", "-o",
        help="Output file path (JSON or HTML)",
        default=None
    )
    parser.add_argument(
        "--template", "-t",
        help="Generate single template type",
        choices=list(TEMPLATE_TYPES.keys()),
        default=None
    )
    parser.add_argument(
        "--skin", "-s",
        help="Design skin to use",
        choices=list(DESIGN_SKINS.keys()),
        default="apple_light"
    )
    parser.add_argument(
        "--list-templates",
        action="store_true",
        help="List available template types"
    )
    parser.add_argument(
        "--list-skins",
        action="store_true",
        help="List available design skins"
    )
    parser.add_argument(
        "--list-sections",
        action="store_true",
        help="List available section types"
    )
    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Suppress progress output"
    )
    parser.add_argument(
        "--json-only",
        action="store_true",
        help="Output only JSON (no progress messages)"
    )

    args = parser.parse_args()

    # List commands
    if args.list_templates:
        print("Available template types:")
        for t in list_template_types():
            print(f"  {t['type']:30} {t['name']} ({t['category']})")
        return

    if args.list_skins:
        print("Available design skins:")
        for skin_id, skin_data in DESIGN_SKINS.items():
            print(f"  {skin_id:20} {skin_data['name']}")
        return

    if args.list_sections:
        print("Available section types:")
        for section_type in list_section_types():
            print(f"  {section_type}")
        return

    # Generate single template
    if args.template:
        result = run_single_template(
            args.template,
            args.skin,
            args.output
        )
        if not args.output:
            if args.json_only:
                print(json.dumps(result, indent=2))
            else:
                print(f"Generated: {result['name']} ({result['skin_name']})")
                print(f"Sections: {', '.join(result['sections_used'])}")
                if not args.quiet:
                    print("\nHTML Preview (first 500 chars):")
                    print(result['html'][:500] + "...")
        return

    # Run full pipeline
    verbose = not (args.quiet or args.json_only)
    result = run_pipeline(args.output, verbose=verbose)

    if args.json_only and not args.output:
        print(json.dumps(result))


if __name__ == "__main__":
    main()

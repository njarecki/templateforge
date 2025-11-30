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
    register_derived_templates,
    TEMPLATE_TYPES,
)
from design_system import DESIGN_SKINS
from section_library import get_all_sections, list_section_types
from template_validator import validate_template, validate_batch, fix_template_issues
from external_sources import (
    fetch_all_external_templates,
    fetch_templates_from_source,
    list_available_sources,
    extract_section_patterns,
    EXTERNAL_SOURCES,
)
from mjml_converter import convert_template_to_mjml, generate_mjml_template
from preview_server import run_server as run_preview_server
from template_derivation import (
    derive_all_templates,
    get_derived_template_types,
    print_derivation_report,
)


def run_pipeline(output_file=None, verbose=True, output_format="html"):
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

    Args:
        output_file: Path to save output JSON
        verbose: Whether to print progress messages
        output_format: 'html' or 'mjml' - determines template output format
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

    # Convert to MJML if requested
    if output_format == "mjml":
        if verbose:
            print("Converting templates to MJML format...")

        for template in batch["normalizedTemplates"]:
            template["mjml"] = convert_template_to_mjml(template)

        for template in batch["reskinnedTemplates"]:
            template["mjml"] = convert_template_to_mjml(template)

        for template in batch["layoutVariants"]:
            template["mjml"] = convert_template_to_mjml(template)

        if verbose:
            print(f"  - Converted {batch['metadata']['total_templates']} templates to MJML")
            print()

    # Add generation metadata
    batch["metadata"]["generated_at"] = datetime.now(timezone.utc).isoformat()
    batch["metadata"]["pipeline_version"] = "1.0.0"
    batch["metadata"]["validation"] = validation_results
    batch["metadata"]["output_format"] = output_format

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


def run_single_template(template_type, skin="apple_light", output_file=None, output_format="html"):
    """Generate a single template with optional output to file."""
    template = generate_template(template_type, skin)
    template = fix_template_issues(template)

    # Add MJML conversion if requested
    if output_format == "mjml":
        template["mjml"] = convert_template_to_mjml(template)

    if output_file:
        if output_file.endswith(".html"):
            with open(output_file, "w") as f:
                f.write(template["html"])
        elif output_file.endswith(".mjml"):
            # Output raw MJML file
            if "mjml" not in template:
                template["mjml"] = convert_template_to_mjml(template)
            with open(output_file, "w") as f:
                f.write(template["mjml"])
        else:
            with open(output_file, "w") as f:
                json.dump(template, f, indent=2)

    return template


def run_external_fetch(source_id=None, output_file=None, verbose=True):
    """
    Fetch templates from external public sources.

    This implements Step 1 of the OBJECTIVE.md pipeline:
    "Find high-quality public email HTML/MJML templates from legal/open sources"
    """
    if verbose:
        print("=" * 60)
        print("TemplateForge External Template Sourcing")
        print("=" * 60)
        print()

    if source_id:
        if source_id not in EXTERNAL_SOURCES:
            print(f"Unknown source: {source_id}")
            print(f"Available: {', '.join(EXTERNAL_SOURCES.keys())}")
            return None
        if verbose:
            print(f"Fetching from: {source_id}")
        templates = fetch_templates_from_source(source_id, verbose)
        results = {
            'source': source_id,
            'templates_fetched': templates,
            'summary': {
                'total_templates': len(templates)
            }
        }
    else:
        results = fetch_all_external_templates(verbose)

    # Extract patterns for analysis
    templates_list = results.get('templates_fetched', [])
    patterns = extract_section_patterns(templates_list)
    results['section_patterns'] = patterns

    if verbose:
        print()
        print("Section patterns extracted:")
        for pattern in sorted(patterns, key=lambda x: -x['occurrences']):
            print(f"  {pattern['type']}: {pattern['occurrences']} occurrences")
        print()

    # Save if output specified
    if output_file:
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
        if verbose:
            print(f"Saved to: {output_file}")
            print(f"File size: {os.path.getsize(output_file) / 1024:.1f} KB")

    if verbose:
        print()
        print("=" * 60)
        print("External fetch complete!")
        print("=" * 60)

    return results


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
    parser.add_argument(
        "--fetch-external",
        action="store_true",
        help="Fetch templates from external public sources (MJML, Foundation)"
    )
    parser.add_argument(
        "--external-source",
        help="Specific external source to fetch (mjml_templates, foundation_emails)"
    )
    parser.add_argument(
        "--list-external-sources",
        action="store_true",
        help="List available external template sources"
    )
    parser.add_argument(
        "--format", "-f",
        help="Output format: html (default) or mjml",
        choices=["html", "mjml"],
        default="html"
    )
    parser.add_argument(
        "--preview",
        action="store_true",
        help="Start the preview server to browse templates in browser"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8080,
        help="Port for preview server (default: 8080)"
    )
    parser.add_argument(
        "--derive-templates",
        action="store_true",
        help="Derive new template types from external sources"
    )
    parser.add_argument(
        "--derive-report",
        action="store_true",
        help="Show detailed derivation report"
    )
    parser.add_argument(
        "--include-derived",
        action="store_true",
        help="Include derived templates from external sources in batch generation"
    )
    parser.add_argument(
        "--derived-template",
        help="Generate a specific derived template (fetches from external sources)"
    )

    args = parser.parse_args()

    # Preview server mode
    if args.preview:
        run_preview_server(args.port)
        return

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

    if args.list_external_sources:
        print("Available external template sources:")
        for source in list_available_sources():
            print(f"\n  {source['id']}:")
            print(f"    Name: {source['name']}")
            print(f"    Type: {source['type']}")
            print(f"    Templates ({source['template_count']}): {', '.join(source['templates'][:5])}...")
        return

    # External fetch mode
    if args.fetch_external or args.external_source:
        verbose = not (args.quiet or args.json_only)
        result = run_external_fetch(
            source_id=args.external_source,
            output_file=args.output,
            verbose=verbose
        )
        if args.json_only and not args.output:
            print(json.dumps(result))
        return

    # Template derivation mode
    if args.derive_templates or args.derive_report:
        verbose = not (args.quiet or args.json_only)
        results = derive_all_templates(verbose=verbose)

        if args.derive_report:
            print_derivation_report(results)

        if args.output:
            with open(args.output, 'w') as f:
                json.dump(results["derived_templates"], f, indent=2)
            if verbose:
                print(f"\nSaved derived templates to: {args.output}")

        if args.json_only and not args.output:
            print(json.dumps(results["derived_templates"]))
        return

    # Generate derived template
    if args.derived_template:
        verbose = not (args.quiet or args.json_only)
        if verbose:
            print("Fetching and deriving templates from external sources...")

        # Get derived template types
        derived_types = get_derived_template_types()
        register_derived_templates(derived_types)

        if args.derived_template not in TEMPLATE_TYPES:
            print(f"Error: Template '{args.derived_template}' not found.")
            print("\nAvailable derived templates:")
            for tid in sorted(derived_types.keys()):
                print(f"  {tid}: {derived_types[tid]['name']}")
            return

        result = run_single_template(
            args.derived_template,
            args.skin,
            args.output,
            output_format=args.format
        )
        if not args.output:
            if args.json_only:
                print(json.dumps(result, indent=2))
            else:
                print(f"Generated: {result['name']} ({result['skin_name']})")
                print(f"Sections: {', '.join(result['sections_used'])}")
                print(f"Format: {args.format.upper()}")
        return

    # Generate single template
    if args.template:
        result = run_single_template(
            args.template,
            args.skin,
            args.output,
            output_format=args.format
        )
        if not args.output:
            if args.json_only:
                print(json.dumps(result, indent=2))
            else:
                print(f"Generated: {result['name']} ({result['skin_name']})")
                print(f"Sections: {', '.join(result['sections_used'])}")
                print(f"Format: {args.format.upper()}")
                if not args.quiet:
                    if args.format == "mjml" and "mjml" in result:
                        print("\nMJML Preview (first 500 chars):")
                        print(result['mjml'][:500] + "...")
                    else:
                        print("\nHTML Preview (first 500 chars):")
                        print(result['html'][:500] + "...")
        return

    # Include derived templates if requested
    if args.include_derived:
        if not (args.quiet or args.json_only):
            print("Including derived templates from external sources...")
        derived_types = get_derived_template_types()
        register_derived_templates(derived_types)
        if not (args.quiet or args.json_only):
            print(f"  Added {len(derived_types)} derived template types\n")

    # Run full pipeline
    verbose = not (args.quiet or args.json_only)
    result = run_pipeline(args.output, verbose=verbose, output_format=args.format)

    if args.json_only and not args.output:
        print(json.dumps(result))


if __name__ == "__main__":
    main()

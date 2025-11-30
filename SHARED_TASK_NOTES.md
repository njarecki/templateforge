# TemplateForge Task Notes

## Current State
Core pipeline is complete with MJML output support added. Run `python3 pipeline.py --output output_batch.json` to generate a full batch.

## What's Working
- 16 template types across 6 categories (Welcome, SaaS, Ecommerce, Newsletter, Promo, Transactional)
- 24 section components in the library
- 5 design skins (Linear Dark, Apple Light, DTC Pastel, Editorial Serif, Brutalist Bold)
- 3 layout variants per template
- Validation and auto-fix for accessibility/best practices
- Generates 144 total templates per run
- External template fetching from MJML and Foundation repos
- **NEW**: MJML output format support for easier downstream editing

## MJML Output Support
Templates can now be output in MJML format alongside HTML:
```bash
python3 pipeline.py -f mjml -o batch_mjml.json     # Full batch with MJML
python3 pipeline.py -t welcome -f mjml             # Single template MJML
python3 pipeline.py -t welcome -o template.mjml    # Direct .mjml file output
```

The `mjml_converter.py` module converts all 24 section types to native MJML components:
- mj-section, mj-column for layout
- mj-text, mj-button, mj-image for content
- mj-social for social icons
- mj-divider, mj-spacer for spacing

## Next Steps
1. **Preview server** - Add a simple HTTP server to preview templates in browser

2. **Expand section library** - Add countdown timer, video placeholder, accordion sections

3. **Template derivation** - Use fetched external templates to derive new template types automatically

4. **MJML compilation** - Add option to compile MJML to HTML using mjml CLI (requires npm)

## File Structure
```
pipeline.py            # Main entry point
mjml_converter.py      # MJML output support (NEW)
external_sources.py    # External template fetching
design_system.py       # Tokens, skins, spacing rules
section_library.py     # 24 section components
template_generator.py  # 16 template types
template_validator.py  # Validation and auto-fix
```

## Quick Commands
```bash
python3 pipeline.py --help                    # All options
python3 pipeline.py --list-templates          # 16 template types
python3 pipeline.py --list-skins              # 5 design skins
python3 pipeline.py --list-sections           # 24 section types
python3 pipeline.py --list-external-sources   # External sources
python3 pipeline.py --fetch-external -o ext.json  # Fetch external
python3 pipeline.py -t password_reset -s linear_dark  # Single template
python3 pipeline.py -t welcome -f mjml -o out.mjml    # MJML output
```

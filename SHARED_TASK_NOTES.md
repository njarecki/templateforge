# TemplateForge Task Notes

## Current State
Core pipeline is complete with external template sourcing now added. Run `python3 pipeline.py --output output_batch.json` to generate a full batch.

## What's Working
- 16 template types across 6 categories (Welcome, SaaS, Ecommerce, Newsletter, Promo, Transactional)
- 24 section components in the library
- 5 design skins (Linear Dark, Apple Light, DTC Pastel, Editorial Serif, Brutalist Bold)
- 3 layout variants per template
- Validation and auto-fix for accessibility/best practices
- Generates 144 total templates per run
- **NEW**: External template fetching from MJML and Foundation repos

## External Template Sourcing
Fetches templates from public sources and extracts section patterns:
- **mjml_templates**: 10 MJML templates (welcome, newsletter, receipt, promo, etc.)
- **foundation_emails**: 5 HTML templates (newsletter, drip, marketing, sidebar)

```bash
python3 pipeline.py --fetch-external                    # Fetch all external
python3 pipeline.py --external-source mjml_templates    # Specific source
python3 pipeline.py --list-external-sources             # List sources
```

## Next Steps
1. **MJML output support** - Add MJML output format for easier downstream editing

2. **Preview server** - Add a simple HTTP server to preview templates in browser

3. **Expand section library** - Add countdown timer, video placeholder, accordion sections

4. **Template derivation** - Use fetched external templates to derive new template types automatically

## File Structure
```
pipeline.py            # Main entry point
external_sources.py    # External template fetching (NEW)
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
```

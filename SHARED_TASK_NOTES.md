# TemplateForge Task Notes

## Current State
Core pipeline is complete with template derivation from external sources.

## What's Working
- 27 built-in template types across 6 categories
- 36 section components in the library
- 5 design skins (Linear Dark, Apple Light, DTC Pastel, Editorial Serif, Brutalist Bold)
- 3 layout variants per template
- Validation and auto-fix for accessibility/best practices
- External template fetching from MJML and Foundation repos
- MJML output format support
- Preview server for browsing templates in browser
- **Template derivation** - automatically derives new templates from external sources
  - Fetches 15 external templates and creates 14 unique derived types
  - Derives from MJML official templates + Foundation for Emails
  - **369 total templates when including derived** (vs 243 base)

## New in This Iteration
- `template_derivation.py` - Analyzes external templates and creates new template type definitions
- Pipeline flags: `--derive-templates`, `--derive-report`, `--include-derived`, `--derived-template`

## Quick Commands
```bash
# Standard generation
python3 pipeline.py -o batch.json                     # 243 templates
python3 pipeline.py --include-derived -o batch.json   # 369 templates (with derived)

# Derivation
python3 pipeline.py --derive-templates                # See derived templates
python3 pipeline.py --derive-report                   # Detailed derivation report
python3 pipeline.py --derived-template derived_welcome_email -s linear_dark

# Other
python3 pipeline.py --preview                         # Start preview server
python3 pipeline.py --list-templates                  # 27 built-in types
```

## Next Steps
1. **MJML compilation** - Add option to compile MJML to HTML using mjml CLI (requires npm)

2. **More section types to consider** - referral program, loyalty points, gift card, subscription renewal

3. **Improve derivation accuracy** - Better content pattern matching for more precise section inference

## File Structure
```
pipeline.py            # Main entry point
template_derivation.py # NEW: External template derivation
preview_server.py      # HTTP preview server
mjml_converter.py      # MJML output support
external_sources.py    # External template fetching
design_system.py       # Tokens, skins, spacing rules
section_library.py     # 36 section components
template_generator.py  # 27 template types
template_validator.py  # Validation and auto-fix
```

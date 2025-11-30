# TemplateForge Task Notes

## Current State
Core pipeline is complete with expanded section library and template types.

## What's Working
- 24 template types across 6 categories (Welcome, SaaS, Ecommerce, Newsletter, Promo, Transactional)
- 33 section components in the library
- 5 design skins (Linear Dark, Apple Light, DTC Pastel, Editorial Serif, Brutalist Bold)
- 3 layout variants per template
- Validation and auto-fix for accessibility/best practices
- **Generates 192 total templates per run** (24 x 5 skins + 24 x 3 variants)
- External template fetching from MJML and Foundation repos
- MJML output format support for easier downstream editing
- Preview server for browsing templates in browser

## New Sections Added (Latest)
- `team_members` - 3-person team grid with avatars and roles
- `comparison_table` - Feature comparison table with 4 rows and 2 columns
- `stats_metrics` - 4-stat metrics row for key numbers

## New Template Types (Latest)
- `company_update` - Uses stats_metrics and team_members for company newsletters
- `product_comparison` - Uses comparison_table for product feature comparisons
- `annual_report` - Uses stats_metrics, story_block, and team_members for year-in-review emails

## Next Steps
1. **Template derivation** - Use fetched external templates to derive new template types automatically

2. **MJML compilation** - Add option to compile MJML to HTML using mjml CLI (requires npm)

3. **More section types to consider** - rating stars, countdown timer variants, gallery carousel, multi-step form

## File Structure
```
pipeline.py            # Main entry point
preview_server.py      # HTTP preview server
mjml_converter.py      # MJML output support
external_sources.py    # External template fetching
design_system.py       # Tokens, skins, spacing rules
section_library.py     # 33 section components
template_generator.py  # 24 template types
template_validator.py  # Validation and auto-fix
```

## Quick Commands
```bash
python3 pipeline.py --help                    # All options
python3 pipeline.py --preview                 # Start preview server
python3 pipeline.py --list-templates          # 24 template types
python3 pipeline.py --list-skins              # 5 design skins
python3 pipeline.py -t company_update -s apple_light     # Company update template
python3 pipeline.py -t product_comparison -s linear_dark # Product comparison template
python3 pipeline.py -t annual_report -s editorial_serif  # Annual report template
python3 pipeline.py -o batch.json             # Full batch generation
```

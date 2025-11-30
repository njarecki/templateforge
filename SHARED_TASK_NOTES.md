# TemplateForge Task Notes

## Current State
Core pipeline is complete with preview server and expanded section library.

## What's Working
- 21 template types across 6 categories (Welcome, SaaS, Ecommerce, Newsletter, Promo, Transactional)
- 30 section components in the library
- 5 design skins (Linear Dark, Apple Light, DTC Pastel, Editorial Serif, Brutalist Bold)
- 3 layout variants per template
- Validation and auto-fix for accessibility/best practices
- **Generates 168 total templates per run** (21 x 5 skins + 21 x 3 variants)
- External template fetching from MJML and Foundation repos
- MJML output format support for easier downstream editing
- Preview server for browsing templates in browser

## New Sections Added (Latest)
- `pricing_table` - 3-tier pricing comparison table for SaaS
- `progress_tracker` - 4-step onboarding/process progress indicator
- `app_store_badges` - App Store and Google Play download badges

## New Template Types (Latest)
- `subscription_plans` - Uses pricing_table and accordion_faq for SaaS pricing emails
- `mobile_app_launch` - Uses app_store_badges for app promotion
- `onboarding_progress` - Uses progress_tracker for step-based onboarding

## Next Steps
1. **Template derivation** - Use fetched external templates to derive new template types automatically

2. **MJML compilation** - Add option to compile MJML to HTML using mjml CLI (requires npm)

3. **More section variations** - Consider adding: team members grid, comparison table, stats/metrics row

## File Structure
```
pipeline.py            # Main entry point
preview_server.py      # HTTP preview server
mjml_converter.py      # MJML output support
external_sources.py    # External template fetching
design_system.py       # Tokens, skins, spacing rules
section_library.py     # 30 section components
template_generator.py  # 21 template types
template_validator.py  # Validation and auto-fix
```

## Quick Commands
```bash
python3 pipeline.py --help                    # All options
python3 pipeline.py --preview                 # Start preview server
python3 pipeline.py --list-templates          # 21 template types
python3 pipeline.py --list-skins              # 5 design skins
python3 pipeline.py -t subscription_plans -s apple_light  # Pricing table template
python3 pipeline.py -t mobile_app_launch -s linear_dark   # App launch template
python3 pipeline.py -t onboarding_progress -s dtc_pastel  # Progress tracker template
python3 pipeline.py -o batch.json             # Full batch generation
```

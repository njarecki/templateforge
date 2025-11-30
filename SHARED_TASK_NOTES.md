# TemplateForge Task Notes

## Current State
Core pipeline is complete with full MJML support for all 36 section types.

## What's Working
- 27 built-in template types across 6 categories
- 36 section components in the library
- **36 MJML converters** (100% coverage - all sections now have MJML support)
- 5 design skins (Linear Dark, Apple Light, DTC Pastel, Editorial Serif, Brutalist Bold)
- 3 layout variants per template
- Validation and auto-fix for accessibility/best practices
- External template fetching from MJML and Foundation repos
- MJML output format support
- Preview server for browsing templates in browser
- Template derivation from external sources (369 total templates when including derived)

## Recent Updates
- Added MJML converters for remaining 12 sections:
  - countdown_timer, video_placeholder, accordion_faq, pricing_table
  - progress_tracker, app_store_badges, team_members, comparison_table
  - stats_metrics, rating_stars, gallery_carousel, multi_step_form

## Quick Commands
```bash
# Standard generation
python3 pipeline.py -o batch.json                     # 243 templates
python3 pipeline.py --include-derived -o batch.json   # 369 templates (with derived)
python3 pipeline.py --format mjml -o batch.json       # MJML output

# Single template with MJML
python3 pipeline.py --template subscription_plans --skin linear_dark --format mjml

# Other
python3 pipeline.py --preview                         # Start preview server
python3 pipeline.py --list-templates                  # 27 built-in types
```

## Next Steps
1. **MJML to HTML compilation** - Add option to compile MJML to final HTML using mjml CLI (requires npm install mjml)

2. **More section types to consider** - referral program, loyalty points, gift card, subscription renewal

3. **Improve derivation accuracy** - Better content pattern matching for more precise section inference

## File Structure
```
pipeline.py            # Main entry point
template_derivation.py # External template derivation
preview_server.py      # HTTP preview server
mjml_converter.py      # MJML output support (36 converters)
external_sources.py    # External template fetching
design_system.py       # Tokens, skins, spacing rules
section_library.py     # 36 section components
template_generator.py  # 27 template types
template_validator.py  # Validation and auto-fix
```

# TemplateForge Task Notes

## Current State
Core pipeline is complete with preview server and expanded section library.

## What's Working
- 18 template types across 6 categories (Welcome, SaaS, Ecommerce, Newsletter, Promo, Transactional)
- 27 section components in the library
- 5 design skins (Linear Dark, Apple Light, DTC Pastel, Editorial Serif, Brutalist Bold)
- 3 layout variants per template
- Validation and auto-fix for accessibility/best practices
- **Generates 162 total templates per run** (18 × 5 skins + 18 × 3 variants)
- External template fetching from MJML and Foundation repos
- MJML output format support for easier downstream editing
- Preview server for browsing templates in browser

## New Sections Added
- `countdown_timer` - Countdown timer for sales, launches, or events
- `video_placeholder` - Video thumbnail with play button overlay
- `accordion_faq` - FAQ section with expandable-style question/answer blocks

## New Template Types
- `product_launch` - Uses countdown_timer for launch announcements
- `video_tutorial` - Uses video_placeholder and accordion_faq for tutorials/demos

## Next Steps
1. **Template derivation** - Use fetched external templates to derive new template types automatically

2. **MJML compilation** - Add option to compile MJML to HTML using mjml CLI (requires npm)

3. **More section variations** - Consider adding: pricing table, team members, app store badges, progress tracker

## File Structure
```
pipeline.py            # Main entry point
preview_server.py      # HTTP preview server
mjml_converter.py      # MJML output support
external_sources.py    # External template fetching
design_system.py       # Tokens, skins, spacing rules
section_library.py     # 27 section components
template_generator.py  # 18 template types
template_validator.py  # Validation and auto-fix
```

## Quick Commands
```bash
python3 pipeline.py --help                    # All options
python3 pipeline.py --preview                 # Start preview server
python3 pipeline.py --list-templates          # 18 template types
python3 pipeline.py --list-skins              # 5 design skins
python3 pipeline.py -t product_launch -s linear_dark  # New countdown template
python3 pipeline.py -t video_tutorial -f mjml         # New video/FAQ template
python3 pipeline.py -o batch.json             # Full batch generation
```

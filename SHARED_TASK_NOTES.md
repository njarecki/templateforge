# TemplateForge Task Notes

## Current State
Core pipeline is complete with expanded section library and template types.

## What's Working
- 27 template types across 6 categories (Welcome, SaaS, Ecommerce, Newsletter, Promo, Transactional)
- 36 section components in the library
- 5 design skins (Linear Dark, Apple Light, DTC Pastel, Editorial Serif, Brutalist Bold)
- 3 layout variants per template
- Validation and auto-fix for accessibility/best practices
- **Generates 243 total templates per run** (27 x 5 skins + 27 x 3 variants + 27 normalized)
- External template fetching from MJML and Foundation repos
- MJML output format support for easier downstream editing
- Preview server for browsing templates in browser

## New Sections Added (Latest)
- `rating_stars` - Star rating display with product image and review snippet
- `gallery_carousel` - 4-image product gallery with labels and links
- `multi_step_form` - Form with progress bar and 3 input fields

## New Template Types (Latest)
- `product_review_request` - Uses rating_stars for post-purchase review requests
- `collection_showcase` - Uses gallery_carousel for product collections
- `survey_invitation` - Uses multi_step_form for feedback/survey emails

## Next Steps
1. **Template derivation** - Use fetched external templates to derive new template types automatically

2. **MJML compilation** - Add option to compile MJML to HTML using mjml CLI (requires npm)

3. **More section types to consider** - referral program, loyalty points, gift card, subscription renewal

## File Structure
```
pipeline.py            # Main entry point
preview_server.py      # HTTP preview server
mjml_converter.py      # MJML output support
external_sources.py    # External template fetching
design_system.py       # Tokens, skins, spacing rules
section_library.py     # 36 section components
template_generator.py  # 27 template types
template_validator.py  # Validation and auto-fix
```

## Quick Commands
```bash
python3 pipeline.py --help                    # All options
python3 pipeline.py --preview                 # Start preview server
python3 pipeline.py --list-templates          # 27 template types
python3 pipeline.py --list-skins              # 5 design skins
python3 pipeline.py -t product_review_request -s apple_light  # Review request template
python3 pipeline.py -t collection_showcase -s dtc_pastel      # Collection showcase
python3 pipeline.py -t survey_invitation -s linear_dark       # Survey invitation
python3 pipeline.py -o batch.json             # Full batch generation
```

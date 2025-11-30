# TemplateForge Task Notes

## Current State
Core pipeline is complete and functional. Run `python3 pipeline.py --output output_batch.json` to generate a full batch.

## What's Working
- 16 template types across 6 categories (Welcome, SaaS, Ecommerce, Newsletter, Promo, Transactional)
- 24 section components in the library
- 5 design skins (Linear Dark, Apple Light, DTC Pastel, Editorial Serif, Brutalist Bold)
- 3 layout variants per template
- Validation and auto-fix for accessibility/best practices
- Generates 144 total templates per run

## Template Categories
- **Welcome**: welcome, welcome_minimal
- **SaaS**: saas_onboarding, saas_feature_announcement, event_invitation
- **Ecommerce**: ecommerce_promo, ecommerce_order_confirmation, abandoned_cart, shipping_notification, review_request
- **Newsletter**: newsletter, newsletter_digest
- **Promo**: sale_announcement, flash_sale
- **Transactional**: password_reset, account_verification

## Next Steps
1. **External template sourcing** - Currently templates are generated from built-in definitions. Could add capability to fetch/parse templates from MJML galleries or GitHub repos.

2. **MJML support** - Add MJML input/output option for easier editing downstream.

3. **Preview server** - Add a simple HTTP server to preview templates in browser.

4. **Expand section library** - Add more specialized sections (countdown timer, video placeholder, accordion, etc.)

## File Structure
```
pipeline.py           # Main entry point - run this
design_system.py      # Tokens, skins, spacing rules
section_library.py    # All section components (24 sections)
template_generator.py # Template composition logic (16 templates)
template_validator.py # Validation and auto-fix
output_batch.json     # Generated output (1.6MB+)
```

## Quick Commands
```bash
python3 pipeline.py --help              # Show all options
python3 pipeline.py --list-templates    # List template types (16)
python3 pipeline.py --list-skins        # List design skins
python3 pipeline.py --list-sections     # List section types (24)
python3 pipeline.py -t password_reset -s linear_dark  # Single template
python3 pipeline.py --json-only         # Pure JSON output
```

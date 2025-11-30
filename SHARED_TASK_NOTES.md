# TemplateForge Task Notes

## Current State
Core pipeline is complete with full MJML support for all 53 section types and MJML-to-HTML compilation.

## What's Working
- **47 built-in template types** across 6 categories (added 4 new: order_hold, subscription_paused, referral_success, wishlist_price_drop)
- **53 section components** in the library (added 3 new: order_hold, subscription_paused, referral_success)
- **53 MJML converters** (100% coverage)
- **MJML to HTML compilation** via `--compile` flag (requires mjml npm package)
- 5 design skins (Linear Dark, Apple Light, DTC Pastel, Editorial Serif, Brutalist Bold)
- 3 layout variants per template
- Validation and auto-fix for accessibility/best practices
- External template fetching from MJML and Foundation repos
- MJML output format support
- Preview server for browsing templates in browser
- Template derivation from external sources (500+ total templates when including derived)

## Quick Commands
```bash
# Standard generation
python3 pipeline.py -o batch.json                     # 423 templates (47 types x 5 skins + variants)
python3 pipeline.py --include-derived -o batch.json   # 500+ templates (with derived)
python3 pipeline.py --format mjml -o batch.json       # MJML output

# MJML compilation to production HTML
python3 pipeline.py --compile -o batch.json           # Generate + compile all templates
python3 pipeline.py --template welcome --compile      # Single template compiled

# Install MJML CLI (required for --compile)
npm install mjml                                      # Local install
npm install -g mjml                                   # Global install

# Other
python3 pipeline.py --preview                         # Start preview server
python3 pipeline.py --list-templates                  # 47 built-in types
```

## Next Steps
1. **Improve derivation accuracy** - Better content pattern matching for more precise section inference

2. **Template analytics** - Track which sections/skins are most commonly used

3. **Additional specialized templates** - Consider more niche templates (order_returned, account_reactivated, loyalty_tier_upgrade, password_changed)

## File Structure
```
pipeline.py            # Main entry point
template_derivation.py # External template derivation
preview_server.py      # HTTP preview server
mjml_converter.py      # MJML output support (53 converters) + compilation
external_sources.py    # External template fetching
design_system.py       # Tokens, skins, spacing rules
section_library.py     # 53 section components
template_generator.py  # 47 template types
template_validator.py  # Validation and auto-fix
```

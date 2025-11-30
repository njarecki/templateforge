# TemplateForge Task Notes

## Current State
Core pipeline is complete with full MJML support for all 40 section types and MJML-to-HTML compilation.

## What's Working
- **33 built-in template types** across 6 categories (added 6 new: referral_invite, gift_card_delivery, subscription_reminder, loyalty_status, subscription_canceled, gift_card_purchase)
- **40 section components** in the library
- **40 MJML converters** (100% coverage)
- **MJML to HTML compilation** via `--compile` flag (requires mjml npm package)
- 5 design skins (Linear Dark, Apple Light, DTC Pastel, Editorial Serif, Brutalist Bold)
- 3 layout variants per template
- Validation and auto-fix for accessibility/best practices
- External template fetching from MJML and Foundation repos
- MJML output format support
- Preview server for browsing templates in browser
- Template derivation from external sources (417 total templates when including derived)

## Quick Commands
```bash
# Standard generation
python3 pipeline.py -o batch.json                     # 297 templates
python3 pipeline.py --include-derived -o batch.json   # 417+ templates (with derived)
python3 pipeline.py --format mjml -o batch.json       # MJML output

# MJML compilation to production HTML
python3 pipeline.py --compile -o batch.json           # Generate + compile all templates
python3 pipeline.py --template welcome --compile      # Single template compiled

# Install MJML CLI (required for --compile)
npm install mjml                                      # Local install
npm install -g mjml                                   # Global install

# Other
python3 pipeline.py --preview                         # Start preview server
python3 pipeline.py --list-templates                  # 33 built-in types
```

## Next Steps
1. **Improve derivation accuracy** - Better content pattern matching for more precise section inference

2. **Template analytics** - Track which sections/skins are most commonly used

3. **Additional template refinements** - Consider adding more specialized ecommerce templates (wishlist, back-in-stock, price drop alerts)

## File Structure
```
pipeline.py            # Main entry point
template_derivation.py # External template derivation
preview_server.py      # HTTP preview server
mjml_converter.py      # MJML output support (40 converters) + compilation
external_sources.py    # External template fetching
design_system.py       # Tokens, skins, spacing rules
section_library.py     # 40 section components
template_generator.py  # 33 template types
template_validator.py  # Validation and auto-fix
```

# TemplateForge Task Notes

## Current State
Core pipeline is complete and functional. Run `python3 pipeline.py --output output_batch.json` to generate a full batch.

## What's Working
- 10 template types across 5 categories (Welcome, SaaS, Ecommerce, Newsletter, Promo)
- 17 section components in the library
- 5 design skins (Linear Dark, Apple Light, DTC Pastel, Editorial Serif, Brutalist Bold)
- 3 layout variants per template
- Validation and auto-fix for accessibility/best practices
- Generates 90 total templates per run

## Next Steps
1. **Add more template types** - The objective mentions "5-10 source templates" minimum; we have 10 but could add more specialized ones (password reset, shipping notification, abandoned cart, etc.)

2. **External template sourcing** - Currently templates are generated from built-in definitions. Could add capability to fetch/parse templates from MJML galleries or GitHub repos.

3. **MJML support** - Add MJML input/output option for easier editing downstream.

4. **Preview server** - Add a simple HTTP server to preview templates in browser.

5. **Expand section library** - Add more specialized sections (countdown timer, video placeholder, accordion, etc.)

## File Structure
```
pipeline.py           # Main entry point - run this
design_system.py      # Tokens, skins, spacing rules
section_library.py    # All section components
template_generator.py # Template composition logic
template_validator.py # Validation and auto-fix
output_batch.json     # Generated output (1MB+)
```

## Quick Commands
```bash
python3 pipeline.py --help              # Show all options
python3 pipeline.py --list-templates    # List template types
python3 pipeline.py --list-skins        # List design skins
python3 pipeline.py -t welcome -s linear_dark  # Single template
python3 pipeline.py --json-only         # Pure JSON output
```

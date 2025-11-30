# TemplateForge Task Notes

## Current State
Core pipeline is complete with preview server added. Run `python3 pipeline.py --preview` to browse templates in browser.

## What's Working
- 16 template types across 6 categories (Welcome, SaaS, Ecommerce, Newsletter, Promo, Transactional)
- 24 section components in the library
- 5 design skins (Linear Dark, Apple Light, DTC Pastel, Editorial Serif, Brutalist Bold)
- 3 layout variants per template
- Validation and auto-fix for accessibility/best practices
- Generates 144 total templates per run
- External template fetching from MJML and Foundation repos
- MJML output format support for easier downstream editing
- **NEW**: Preview server for browsing templates in browser

## Preview Server
Start the server with:
```bash
python3 pipeline.py --preview              # Starts on port 8080
python3 pipeline.py --preview --port 3000  # Custom port
python3 preview_server.py                  # Direct run
```

Endpoints:
- `/` - Template gallery with all 16 types grouped by category
- `/preview/<type>?skin=<skin>&format=html|mjml` - Render individual template
- `/compare/<type>` - Side-by-side comparison of all 5 skins
- `/api/templates` - JSON list of templates
- `/api/skins` - JSON list of skins

## Next Steps
1. **Expand section library** - Add countdown timer, video placeholder, accordion sections

2. **Template derivation** - Use fetched external templates to derive new template types automatically

3. **MJML compilation** - Add option to compile MJML to HTML using mjml CLI (requires npm)

## File Structure
```
pipeline.py            # Main entry point
preview_server.py      # HTTP preview server (NEW)
mjml_converter.py      # MJML output support
external_sources.py    # External template fetching
design_system.py       # Tokens, skins, spacing rules
section_library.py     # 24 section components
template_generator.py  # 16 template types
template_validator.py  # Validation and auto-fix
```

## Quick Commands
```bash
python3 pipeline.py --help                    # All options
python3 pipeline.py --preview                 # Start preview server
python3 pipeline.py --list-templates          # 16 template types
python3 pipeline.py --list-skins              # 5 design skins
python3 pipeline.py -t welcome -f mjml -o out.mjml  # Single MJML template
python3 pipeline.py -o batch.json             # Full batch generation
```

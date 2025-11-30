# TemplateForge - Sourcing Progress Notes

## Current Status
- **25 unique templates sourced** (14 MJML, 11 HTML)
- No duplicates detected yet
- Goal: 300+ unique templates

## Sources Completed
1. **MJML Official Templates** (13 templates) - MIT license
   - Located at: `data/raw/mjml_official/`
   - All indexed with proper metadata

2. **Foundation for Emails** (11 templates) - MIT license
   - Located at: `data/raw/foundation_emails/`
   - Inky templating syntax (HTML)

3. **MJML.io GitHub Collection** (1 template started)
   - Located at: `data/raw/mjmlio_email_templates/`
   - Has 22 templates total, many overlap with official

## Next Steps (Priority Order)
1. Continue mjmlio/email-templates repo - fetch remaining unique templates:
   - basic.mjml, newsletter.mjml, onepage.mjml, racoon.mjml
   - recast.mjml, receipt-email.mjml, ticketshop.mjml, worldly.mjml
   - (Content already fetched, needs saving and indexing)

2. Explore Easy-Email-Pro/email-templates repo (MIT)

3. Search GitHub for more MJML packs:
   - "email mjml templates"
   - "responsive html email templates free"
   - "open-source mjml templates"

4. Check Stripo/Beefree free template galleries

## Usage Commands
```bash
# Check current progress
python3 scripts/sourcing_indexer.py stats

# Add a new template
python3 scripts/sourcing_indexer.py add \
  --source-id <id> \
  --source-name "<name>" \
  --url <url> \
  --license <license> \
  --type <html|mjml> \
  --file data/raw/<source_id>/<slug>.<html|mjml>

# Run deduplication
python3 scripts/sourcing_indexer.py dedupe
```

## Template Sources Still Available
- Stripo free templates: https://stripo.email/templates/
- Beefree free templates: https://beefree.io/templates/
- Litmus community examples
- GitHub searches for email template packs

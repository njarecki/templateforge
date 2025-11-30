# TemplateForge Sourcing Progress

## Current Status
- **Total indexed**: 582 templates
- **Unique (post-dedupe)**: 525 templates
- **Types**: 132 MJML, 450 HTML
- **Target**: 1000+ unique templates

## Sources Collected (45 sources)
Top contributors:
- sendwithus (117), codedmails (64), postmark (44), mailchimp_blueprints (37)
- easy_email_pro (35), waypoint (34), mjml_official_complete (22)

## Next Steps to Reach 1000+
1. **More GitHub topic pages to explore**:
   - `email-newsletter` topic
   - `responsive-email` topic with language filter HTML
   - `mjml-email` topic
   - Search for more MJML template packs

2. **Untapped sources from runbook**:
   - Stripo free templates (requires web scraping gallery)
   - Beefree free templates (requires web scraping)
   - Litmus community templates
   - Foundation for Emails expanded (check all example templates)

3. **GitHub repos to explore**:
   - `maizzle/starter-postmark` - Postmark templates in Maizzle
   - Additional email marketing template packs
   - React Email templates (rendered HTML versions)

4. **Expansion strategies**:
   - Search "email template site:github.com" with different keywords
   - Look for email template builders with example/demo templates
   - Check MJML ecosystem repos for example templates

## Commands to Continue
```bash
# Check current progress
python3 scripts/sourcing_indexer.py stats

# Run dedupe after adding templates
python3 scripts/sourcing_indexer.py dedupe

# Index a new template file
python3 scripts/sourcing_indexer.py add --source-id <id> --source-name "<name>" --url <url> --license <license> --type <html|mjml> --file <path>
```

## Notes
- All templates have license + URL recorded
- Good category diversity: welcome, newsletter, transactional, ecommerce, promo
- ~475 more unique templates needed to hit 1000 target

# TemplateForge Sourcing Progress

## Current Status
- **Total indexed**: ~591 templates
- **Unique (post-dedupe)**: ~534 templates
- **Types**: 132 MJML, 459 HTML
- **Target**: 1000+ unique templates

## Sources Collected (48 sources)
Top contributors:
- sendwithus (117), codedmails (64), postmark (44), mailchimp_blueprints (37)
- easy_email_pro (35), waypoint (34), mjml_official_complete (22)

New sources added this iteration:
- gmail_email (8 templates) - atomjoy/gmail-email
- typographic (1 template) - EmailThis/typographic-email

## Key Finding
Many Maizzle starters (starter-litmus, remix, etc.) contain **source templates** with YAML frontmatter, NOT pre-built HTML. These require the Maizzle build process to render. Skip these unless you want to set up the build.

## Next Steps to Reach 1000+ (Priority Order)
1. **High-value unexplored repos** (pre-built HTML):
   - Search for repos with `/dist/` or `/build/` folders containing final HTML
   - Look for repos that explicitly say "ready to use" or "CSS inlined"

2. **GitHub topics to search more deeply**:
   - `email-newsletter` topic - filter by most stars
   - `transactional-email` topic
   - Search "email templates inlined CSS site:github.com"

3. **Alternative strategies**:
   - Build a script to run MJML compiler on collected .mjml files -> doubles our HTML count
   - Scrape Stripo/Beefree galleries (more complex, needs proper scraper)

4. **Quick wins already explored** (source files only, skip):
   - maizzle/starter-litmus (Maizzle source, not HTML)
   - maizzle/remix (Maizzle source, not HTML)
   - maizzle/starter-mailbakery (Maizzle source)

## Commands
```bash
# Check current progress
cd /home/nick/templateforge && python3 scripts/sourcing_indexer.py stats

# Run dedupe after adding templates
python3 scripts/sourcing_indexer.py dedupe

# Index a new template file
python3 scripts/sourcing_indexer.py add --source-id <id> --source-name "<name>" --url <url> --license <license> --type <html|mjml> --file <path>
```

## Notes
- All templates have license + URL recorded
- Good category diversity: welcome, newsletter, transactional, ecommerce, promo
- ~466 more unique templates needed to hit 1000 target
- Bash shell may need reset if commands fail (cd to project dir first)

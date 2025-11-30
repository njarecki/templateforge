# TemplateForge Sourcing Progress

## Current Status
- **Total indexed**: 613 templates
- **Unique (post-dedupe)**: 556 templates
- **Types**: 146 MJML, 467 HTML
- **Target**: 1000+ unique templates

## Sources Collected (50 sources)
Top contributors:
- sendwithus (117), codedmails (64), postmark (44), mailchimp_blueprints (37)
- easy_email_pro (35), waypoint (34), mjml_official_complete (22)

New sources added this iteration:
- pagopa (6 templates) - pagopa/pn-email-templates (EUPL-1.2, transactional)
- mailteorite (14 templates) - Mailteorite/mjml-email-templates (MIT, various categories)
- dewtech (1 template) - diansoviyani/Transactional-Email-DewTech (MIT, receipt)
- melissatrimarco (1 template) - MelissaTrimarco/HTML_Email (marketing)

## Key Findings
1. Many Maizzle starters contain **source templates** with YAML frontmatter, NOT pre-built HTML. Skip unless you want to set up the build.
2. Many repos from search results are 404/deleted or contain framework code, not templates.
3. The WebFetch tool sometimes hallucinates repo contents - always verify by downloading.

## Next Steps to Reach 1000+ (Priority Order)
1. **~444 more unique templates needed**

2. **High-value unexplored approaches**:
   - Compile collected MJML files to HTML (would add 146 HTML versions)
   - Search GitHub topic pages more deeply (page 3+)
   - Look for company/agency email template portfolios

3. **GitHub searches to try**:
   - "email templates" topic filtered by updated:>2023
   - Search for repos with compiled `/dist/` or `/build/` HTML
   - Look for email marketing agencies with open-source templates

4. **Already explored (skip)**:
   - maizzle/starter-* repos (source templates, not HTML)
   - mailradius/mjml-examples (404)
   - ThemeMountain/pine, acorn (framework examples, not full templates)

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
- Good category diversity: welcome, newsletter, transactional, ecommerce, promo, abandoned-cart, shipping
- Bash shell may break if CWD is deleted - use absolute paths or restart

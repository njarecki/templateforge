# TemplateForge Sourcing Progress

## Current Status
- **Total indexed**: 678 templates
- **Unique (post-dedupe)**: 614 templates
- **Types**: 176 MJML, 502 HTML
- **Target**: 1000+ unique templates
- **Sources**: 67 distinct repositories

## Top Source Contributors
sendwithus (117), codedmails (64), postmark (44), mailchimp_blueprints (37), easy_email_pro (35), waypoint (34), mjml_official_complete (22), colorlib (20)

## New Sources Added This Iteration
- email_boilerplate (4 templates) - seanpowell/Email-Boilerplate (MIT, boilerplate variants)
- mailmunch (2 templates) - mailmunch/email-templates (MIT, christmas/webinar)
- chartblocks (1 template) - ChartBlocks/html-email-template (MIT, system notification)
- bbulakh_ecommerce (5 templates) - bbulakh/ecommerce-email (MIT, MJML ecommerce)
- supertokens (5 templates) - supertokens/email-sms-templates (Apache-2.0, auth/OTP)

## Key Findings
1. Many Maizzle starters contain **source templates** with YAML frontmatter, NOT pre-built HTML. Skip unless you want to set up the build.
2. Many repos from search results are 404/deleted or contain framework code, not templates.
3. The WebFetch tool sometimes hallucinates repo contents - always verify by downloading.
4. MJML component/partial files (headers, footers) are useful but not standalone templates.
5. React-email templates are TSX components, not standalone HTML - need compilation.
6. usewaypoint/responsive-transactional-email-templates - 33 templates but NOT accessible via raw GitHub URLs (needs clone).

## Next Steps to Reach 1000+ (Priority Order)
1. **~386 more unique templates needed**

2. **Highest-value approaches**:
   - **Clone usewaypoint repo**: Has 33+ modern transactional templates (git clone required)
   - **Compile MJML to HTML**: 176 MJML files could yield new HTML versions (run `mjml` CLI)
   - **Stripo/Beefree templates**: Require browser automation (Playwright/Selenium) to download
   - Consider email template marketplace APIs or commercial sources with open licenses

3. **Promising unexplored GitHub searches**:
   - "email templates" language:html stars:>5 pushed:>2024
   - Company open-source email repos (Stripe, Airbnb, Uber, etc.)
   - Non-English repos (German, French, Spanish email templates)
   - appcues/email-templates (has Html Templates folder)

4. **Already explored (skip)**:
   - maizzle/starter-* repos (source templates with YAML, not HTML)
   - mailradius/mjml-examples (404)
   - ThemeMountain/pine, acorn (framework examples, not full templates)
   - dubem-design/saas-email-templates (Node.js project, no templates)
   - moiseshp/email-templates-for-developers (404 files)
   - customerio/layouts (Inky source, not compiled HTML)
   - slowfound/react-email-tailwind-templates (TSX components, not HTML)
   - leemunroe/htmlemail (docs only, templates on external site)
   - codeskills-dev/responsive-react-email-examples (TSX, not HTML)

## Commands
```bash
# Check current progress
python3 /home/nick/templateforge/scripts/sourcing_indexer.py stats

# Run dedupe after adding templates
python3 /home/nick/templateforge/scripts/sourcing_indexer.py dedupe

# Index a new template file
python3 /home/nick/templateforge/scripts/sourcing_indexer.py add --source-id <id> --source-name "<name>" --url <url> --license <license> --type <html|mjml> --file <path>

# Clone a git repo to get templates
cd /home/nick/templateforge/data/raw && git clone <repo_url>
```

## Notes
- All templates have license + URL recorded
- Good category diversity: welcome, newsletter, transactional, ecommerce, promo, abandoned-cart, shipping, OTP, auth
- Use absolute paths with python3 - shell CWD may be lost

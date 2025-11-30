# TemplateForge Sourcing Progress

## Current Status
- **Total indexed**: 894 templates
- **Unique (post-dedupe)**: 772 templates
- **Types**: 176 MJML, 718 HTML
- **Target**: 1000+ unique templates
- **Sources**: 96 distinct repositories

## Top Source Contributors
codedmails (64), postmark (55), mailchimp_blueprints (37), easy_email_pro (35), easy_email_compiled (35), waypoint (34), usewaypoint_transactional (34), nirajrajgor (28), mjml_official_complete (22), mjml_complete_compiled (22), colorlib (20)

## New Sources Added This Iteration
- ckissi (6 templates) - ckissi/responsive-html-email-templates (MIT, transactional)
- email_framework (7 templates) - g13nn/Email-Framework (MIT, grids/boilerplate)
- mailersend (15 templates) - mailersend/transactional-email-templates (MIT, transactional)
- hng_boilerplate (20 templates) - oyerohabib/hng-boilerplate-email-templates (MIT, various)
- usewaypoint_transactional (34 templates) - usewaypoint/responsive-transactional-email-templates (MIT, SaaS/marketplace)
- moiseshp (9 templates) - moiseshp/email-templates-for-developers (MIT, password/verification)
- nirajrajgor (14 templates) - nirajrajgor/email-templates (MIT, ecommerce/promotional)
- sundartech (10 templates) - sundardsTechMind/E-mail-Templates (MIT, KYC/newsletter)
- hermes (10 templates) - matcornic/hermes (MIT, default/flat themes)

## Key Achievements This Iteration
1. **Compiled MJML to HTML**: Created HTML versions from 176 MJML files using `npx mjml`
   - mjml_compiled (13), mjml_complete_compiled (22), easy_email_compiled (35)
   - nedssoft_compiled (7), greeeg_compiled (3), modunisa_compiled (3), bbulakh_compiled (5)
2. **Cloned usewaypoint repo** successfully: Got 34 modern transactional templates
3. **Added 158+ unique templates** this iteration (from 614 to 772)

## Key Findings
1. Many Maizzle starters contain **source templates** with YAML frontmatter, NOT pre-built HTML. Skip unless you want to set up the build.
2. Many repos from search results are 404/deleted or contain framework code, not templates.
3. MJML component/partial files (headers, footers) are useful but not standalone templates.
4. React-email templates are TSX components, not standalone HTML - need compilation.
5. **MJML compilation works well**: `npx mjml <file>.mjml -o <file>.html` creates valid HTML

## Next Steps to Reach 1000+ (Priority Order)
1. **~228 more unique templates needed**

2. **Highest-value approaches**:
   - Search for more niche GitHub repos (event, booking, fitness, education, etc.)
   - Look for email template generator projects with example outputs
   - Find company open-source email repos (Auth0, Stripe, etc.)
   - Check Stripo/Beefree if browser automation is available

3. **Promising unexplored GitHub searches**:
   - "email templates" language:html stars:>5 pushed:>2024
   - Company open-source email repos (Stripe, Airbnb, Uber, Auth0, etc.)
   - Non-English repos (German, French, Spanish email templates)
   - Email generator libs with example outputs (more like hermes)

4. **Already explored (skip)**:
   - maizzle/starter-* repos (source templates with YAML, not HTML)
   - mailradius/mjml-examples (404)
   - ThemeMountain/pine, acorn (framework examples, not full templates)
   - customerio/layouts (Inky source, not compiled HTML)
   - react-email based templates (TSX components, not HTML)
   - MODatUniSA/mod-email-templates (already indexed as modunisa)

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

# Compile MJML to HTML
npx mjml <file>.mjml -o <file>.html
```

## Notes
- All templates have license + URL recorded
- Good category diversity: welcome, newsletter, transactional, ecommerce, promo, abandoned-cart, shipping, OTP, auth, KYC, banking, social
- Use absolute paths with python3 - shell CWD may be lost
- MJML must be installed: `npm install mjml` in project root

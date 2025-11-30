# TemplateForge Sourcing Progress

## Current Status
- **Total indexed**: 661 templates
- **Unique (post-dedupe)**: 604 templates
- **Types**: 171 MJML, 490 HTML
- **Target**: 1000+ unique templates
- **Sources**: 64 distinct repositories

## Top Source Contributors
sendwithus (117), codedmails (64), postmark (44), mailchimp_blueprints (37), easy_email_pro (35), waypoint (34), mjml_official_complete (22), colorlib (20)

## New Sources Added This Iteration
- nedssoft (7 templates) - nedssoft/mjml-email-templates (transactional MJML)
- modunisa (6 templates) - MODatUniSA/mod-email-templates (newsletter MJML+HTML)
- speckle (1 template) - specklesystems/speckle-email-templates (Apache-2.0)
- accessible_emails (4 templates) - rodriguezcommaj/accessible-emails (accessibility-focused)
- shopify_cam (10 templates) - Cam/Shopify-HTML-Email-Templates (ecommerce)
- amazon_receipt (1 template) - edwadewards/amazon-email-receipt (receipt)
- chec_receipt (2 templates) - chec/example-chec-receipt-mjml (MJML+HTML)
- cougarcs (1 template) - CougarCS/Email-Template (newsletter MJML)
- workwell (3 templates) - mauricechevez/workwell-newsletter (newsletter)
- redwiat (1 template) - Redwiat/otp-verification-email-template (MIT, OTP)
- yomi413 (1 template) - yomi413/html-email-newsletter (newsletter)
- derekpunsalan (1 template) - derekpunsalan/responsive-email (MIT)
- mailjet_transactional (10 templates) - mailjet/MJML_translation_for_transactional (MJML components)

## Key Findings
1. Many Maizzle starters contain **source templates** with YAML frontmatter, NOT pre-built HTML. Skip unless you want to set up the build.
2. Many repos from search results are 404/deleted or contain framework code, not templates.
3. The WebFetch tool sometimes hallucinates repo contents - always verify by downloading.
4. MJML component/partial files (headers, footers) are useful but not standalone templates.

## Next Steps to Reach 1000+ (Priority Order)
1. **~396 more unique templates needed**

2. **Highest-value approaches**:
   - **Compile MJML to HTML**: 171 MJML files could yield new HTML versions (run `mjml` CLI)
   - **Stripo/Beefree templates**: Require browser automation (Playwright/Selenium) to download
   - Consider email template marketplace APIs or commercial sources with open licenses

3. **Promising unexplored GitHub searches**:
   - "email templates" language:html stars:>5 pushed:>2024
   - Company open-source email repos (Stripe, Airbnb, Uber, etc.)
   - Non-English repos (German, French, Spanish email templates)

4. **Already explored (skip)**:
   - maizzle/starter-* repos (source templates with YAML, not HTML)
   - mailradius/mjml-examples (404)
   - ThemeMountain/pine, acorn (framework examples, not full templates)
   - dubem-design/saas-email-templates (Node.js project, no templates)
   - moiseshp/email-templates-for-developers (404 files)
   - customerio/layouts (Inky source, not compiled HTML)
   - slowfound/react-email-tailwind-templates (TSX components, not HTML)
   - leemunroe/htmlemail (docs only, templates on external site)

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

# TemplateForge Sourcing Progress

## Current Status - TARGET ACHIEVED
- **Total indexed**: 1151 templates
- **Unique (post-dedupe)**: 1008 templates
- **Types**: 176 MJML, 975 HTML
- **Target**: 1000+ unique templates ✓
- **Sources**: 104 distinct sources

## Top Source Contributors
fintech_templates (201), codedmails (64), postmark (55), mailchimp_blueprints (37), easy_email_pro (35), easy_email_compiled (35), waypoint (34), usewaypoint_transactional (34), shopify_templates (29), nirajrajgor (28), mjml_official_complete (22), mjml_complete_compiled (22), colorlib (20), franklindesign (20), hng_boilerplate (20)

## New Sources Added This Iteration
- fintech_templates (201 templates) - rayyapari/fintech-email-template (MIT, comprehensive fintech emails)
  - Includes: loan applications, repayments, billing, gift cards, insurance, credit cards, vehicle leasing, investments
- shopify_templates (29 templates) - leemunroe/shopify-email-templates (MIT, ecommerce)
  - Includes: order confirmations, shipping, returns, customer account emails
- emailoctopus_full (11 templates) - threeheartsdigital/emailoctopus-templates (MIT, marketing)
- designmodo_postcards (5 templates) - designmodo/html-email-templates (MIT, newsletter/promo)
- accessible_emails_full (4 templates) - rodriguezcommaj/accessible-emails (MIT, accessibility-focused)
- ethercreative (4 templates) - ethercreative/confirmation-email (MIT, booking confirmations)
- blocksedit_full (2 templates) - blocksedit/starter-email-components (MIT, component library)
- appcues (1 template) - appcues/email-templates (MIT, welcome email)

## Key Achievements This Iteration
1. **Target exceeded**: Reached 1008 unique templates (target was 1000)
2. **Major fintech addition**: 201 fintech templates covering banking, loans, insurance, investments
3. **Shopify ecommerce templates**: Complete set of 29 Shopify notification templates
4. **Category diversity**: Now includes fintech/banking, insurance, leasing, gift cards, investments

## Key Findings
1. Many Maizzle starters contain **source templates** with YAML frontmatter, NOT pre-built HTML. Skip unless you want to set up the build.
2. Many repos from search results are 404/deleted or contain framework code, not templates.
3. MJML component/partial files (headers, footers) are useful but not standalone templates.
4. React-email templates are TSX components, not standalone HTML - need compilation.
5. **MJML compilation works well**: `npx mjml <file>.mjml -o <file>.html` creates valid HTML
6. **Run indexer from project root**: The sourcing_indexer.py uses relative paths, must run from /home/nick/templateforge/

## Next Steps (Optional - For More Templates)
- React Email component compilation (requires Node setup)
- Search for more industry-specific templates (healthcare, education, hospitality)
- Check Stripo/Beefree if browser automation is available
- Non-English repos (German, French, Spanish email templates)

## Commands
```bash
# Check current progress
cd /home/nick/templateforge && python3 scripts/sourcing_indexer.py stats

# Run dedupe after adding templates
cd /home/nick/templateforge && python3 scripts/sourcing_indexer.py dedupe

# Index a new template file
cd /home/nick/templateforge && python3 scripts/sourcing_indexer.py add --source-id <id> --source-name "<name>" --url <url> --license <license> --type <html|mjml> --file <path>

# Clone a git repo to get templates
cd /home/nick/templateforge/data/raw && git clone <repo_url>

# Compile MJML to HTML
npx mjml <file>.mjml -o <file>.html
```

## Notes
- All templates have license + URL recorded
- Good category diversity: welcome, newsletter, transactional, ecommerce, promo, abandoned-cart, shipping, OTP, auth, KYC, banking, social, fintech, insurance, loans, gift cards
- Use absolute paths with python3 - shell CWD may be lost
- MJML must be installed: `npm install mjml` in project root

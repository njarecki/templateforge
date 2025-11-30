# TemplateForge - Sourcing Progress Notes

## Current Status
- **132 unique templates sourced** (66 MJML, 85 HTML)
- 151 total items, 19 duplicates detected
- Goal: 300+ unique templates

## Sources Completed
1. **MJML Official Templates** (13 templates) - MIT license
   - Located at: `data/raw/mjml_official/`

2. **Foundation for Emails** (11 templates) - MIT license
   - Located at: `data/raw/foundation_emails/`
   - Inky templating syntax (HTML)

3. **MJML.io GitHub Collection** (9 templates) - MIT license
   - Located at: `data/raw/mjmlio_email_templates/`
   - basic, newsletter, onepage, racoon, recast, receipt-email, ticketshop, worldly, amario

4. **Easy-Email-Pro** (35 templates) - MIT license
   - Located at: `data/raw/easy_email_pro/`
   - template1 through template35

5. **E-commerce Email by bbulakh** (5 templates) - MIT license
   - Located at: `data/raw/ecommerce_email/`
   - welcome, cart-reminder, order-confirmation, new-feature, survey

6. **Cerberus** (3 templates) - MIT license
   - Located at: `data/raw/cerberus/`
   - cerberus-fluid, cerberus-hybrid, cerberus-responsive

7. **Postmark Transactional** (11 templates) - MIT license
   - Located at: `data/raw/postmark/`
   - comment-notification, dunning, example, invoice, password-reset, etc.

8. **Mailgun Transactional** (3 templates) - MIT license
   - Located at: `data/raw/mailgun/`
   - action, alert, billing

9. **ColorlibHQ** (20 templates) - MIT license
   - Located at: `data/raw/colorlib/`
   - template1 through template20

10. **Sendwithus** (13 templates) - Apache-2.0 license
    - Located at: `data/raw/sendwithus/`
    - airmail, cleave, go, goldstar, mantra, meow, etc.

11. **Greeeg MJML Templates** (3 templates) - MIT license
    - Located at: `data/raw/greeeg_mjml/`
    - dropbox-product-update, miro-onboarding, stripe-notification

12. **Lee Munroe** (1 template) - MIT license
    - Located at: `data/raw/leemunroe/`

13. **Antwort** (3 templates) - MIT license
    - Located at: `data/raw/antwort/`
    - single-column, three-cols-images, two-cols-simple

14. **Konsav** (3 templates) - MIT license
    - Located at: `data/raw/konsav/`
    - explorational, general, promotional

15. **MailPace** (6 templates) - MIT license
    - Located at: `data/raw/mailpace/`
    - account_deleted, confirmation, password_reset, receipt, etc.

16. **SendGrid** (10 templates) - MIT license
    - Located at: `data/raw/sendgrid/`
    - base, digest, email-confirmation, password-reset, receipt, welcome, etc.

17. **Responsive HTML Email Template** (1 template) - MIT license
    - Located at: `data/raw/responsive_html_email/`

18. **Three11** (1 template) - MIT license
    - Located at: `data/raw/three11_email/`

## Next Steps (Priority Order)
1. Search more GitHub repos with explicit MIT/Apache licenses
2. Explore Stripo/Beefree free template galleries (if available via API)
3. Litmus community examples (check availability)
4. Look for more MJML-specific repositories

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

## Template Sources Still To Explore
- GitHub topic searches: "newsletter-template", "html-email"
- More transactional template collections
- Industry-specific email templates (SaaS, e-commerce)
- Marketing campaign templates

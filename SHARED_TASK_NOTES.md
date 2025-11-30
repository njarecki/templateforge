# TemplateForge Sourcing Task Notes

## Current Status (Updated 2025-11-30)
- **Indexed**: 1,437 items
- **Unique hashes**: 1,218 (after dedupe)
- **Target**: 10,000 unique templates
- **Gap**: ~8,800 more templates needed
- **Sources tapped**: ~161 directories in data/raw/

## Run Commands
```bash
# Check progress
python3 scripts/sourcing_indexer.py stats

# Dedupe after adding templates
python3 scripts/sourcing_indexer.py dedupe

# Index a new template file
python3 scripts/sourcing_indexer.py add \
  --source-id <source_id> \
  --source-name "<Name>" \
  --url "<source_url>" \
  --license <MIT|Apache|Other> \
  --type <html|mjml> \
  --file data/raw/<source_id>/<filename>
```

## Recently Added (This Iteration)
- **kazuki_shopify** (24 HTML) - From Kazuki-tam/shopify-email-notification - Shopify transactional templates
- **simplepleb_laravel** (4 HTML) - From simplepleb/laravel-email-templates - Laravel Blade email templates
- **bootstrap_email** (3 HTML) - From bootstrap-email/bootstrap-email - Bootstrap-styled email examples
- **danielrussellLA** (1 HTML) - From danielrussellLA/responsive-email-templates

## Quality Gates (from runbook)
- Size: >10KB and <350KB
- Must have media queries OR be from responsive framework (MJML/Cerberus/etc)
- Table count >= 5
- Must have CTA/link + footer/unsubscribe
- Uniqueness: Jaccard < 0.90 vs existing

## File Structure
```
data/raw/<source_id>/<slug>.{html|mjml}
data/index/templates.json - master index
data/index/dedupe.json - duplicate clusters
```

## Next Steps (Priority Order)

1. **Explore React-email demo outputs** - The react-email package has demo outputs that might be compilable
   ```bash
   git clone https://github.com/resend/react-email.git /tmp/react-email
   # Check for pre-compiled HTML in examples/demos
   ```

2. **Check jsx-email demo templates** - Similar to react-email, may have compiled outputs
   ```bash
   git clone https://github.com/shellscape/jsx-email.git /tmp/jsx-email
   ```

3. **Web scraping template galleries** (with rate limiting, robots.txt respect):
   - Stripo.email free templates (login-gated, but may have public HTML)
   - Beefree.io free templates (similar situation)
   - Really Good Emails archives

4. **Framework starters with pre-built examples**:
   - More Maizzle starters (check if any new ones)
   - Foundation for Emails example apps

## Reality Check

The 10,000 target remains very challenging. After extensive GitHub searching:

**What we've found:**
- ~161 source directories indexed
- ~1,218 unique templates after deduplication
- Most high-quality open-source repos have been tapped

**Why the gap exists:**
- Quality email templates are scarce compared to website templates
- Most bulk collections (Stripo 1,600+, Beefree 1,000+) are behind paywalls/accounts
- Many repos have components/snippets, not complete templates
- React-email/jsx-email templates need compilation (TSX -> HTML)
- Liquid/Handlebars templates need compilation
- Many templates fail quality gates (under 10KB, no media queries)

**Repos checked but failed quality gates (this iteration):**
- dynamicart/responsive-email-template - 9.4KB (under 10KB threshold)
- ohsik/Simple-Responsive-HTML-Email-Template - 4.9KB (under 10KB)
- sandervanhooft/invoice-templates-generator - 8KB (under 10KB)
- sahrullahh/invoice-template-html - 3.2KB (under 10KB)
- stencila/email-templates - Uses mj-include, needs compilation
- rayyapari/fintech-email-template - Uses Handlebars partials, needs build

**Template Repos Already Fully Tapped:**
All previously listed repos plus:
- bootstrap-email/bootstrap-email (example outputs)
- Kazuki-tam/shopify-email-notification (Shopify transactional)
- simplepleb/laravel-email-templates (Laravel)

## GitHub API Rate Limiting
Note: GitHub API has rate limits (60 requests/hour unauthenticated). If hitting limits, use git clone directly.

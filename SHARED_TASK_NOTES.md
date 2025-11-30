# TemplateForge Sourcing Task Notes

## Current Status (Updated 2025-11-30)
- **Indexed**: 1,405 items
- **Unique hashes**: 1,186 (after dedupe)
- **Target**: 10,000 unique templates
- **Gap**: ~8,800 more templates needed
- **Sources tapped**: ~158 directories in data/raw/

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
- **mail_plates** (20 HTML) - From Pro-Bandey/Mail-Plates
- **email_starter_kit** (3 HTML) - From timothylong/email-starter-kit
- **tigerruslan_saas** (6 HTML) - From TigerRuslan/Email-Templated-HTML-Responsive-

## Untapped/Underexplored Sources

### High Priority (Tier 1 - Should Have Bulk Content)
1. **Stripo** - 1,600+ templates but requires account to export. Try API or find exports.
2. **Beefree** - Similar to Stripo, large collection behind login.
3. **Litmus Community** - May have shared templates.
4. **Really Good Emails** - Curated gallery, may have HTML exports somewhere.

### GitHub Repos to Check
Most major repos have been tapped. Remaining opportunities:
- Forks of popular repos (leemunroe, ckissi) may have additions
- Component libraries that can be assembled into full templates

### Search Queries That Work
```bash
# GitHub API
https://api.github.com/search/repositories?q=email+template+mjml&sort=stars
https://api.github.com/search/repositories?q=email-templates+fork:false&sort=stars

# GitHub Topics (browsable)
https://github.com/topics/email-templates
https://github.com/topics/html-email-templates
https://github.com/topics/mjml-template
```

### Template Repos Already Fully Tapped
- mjmlio/email-templates (22 MJML)
- Easy-Email-Pro/email-templates (35 MJML + HTML)
- sendwithus/templates (117 HTML)
- ColorlibHQ/email-templates (20 HTML)
- hunzaboy/CodedMailsFree (64 HTML)
- ActiveCampaign/postmark-templates (33 HTML)
- mailchimp/email-blueprints (44 HTML)
- All Maizzle starters (litmus, postmark, emailoctopus, amp4email, netlify, mailbakery)
- fintech_templates/fintech_clone (~200 HTML)
- stuartsantos_clone (~67 HTML)
- Pro-Bandey/Mail-Plates (20 HTML)
- TigerRuslan/Email-Templated-HTML-Responsive- (6 HTML)
- timothylong/email-starter-kit (3 HTML)

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

1. **Compile React-email templates** - Install react-email, compile TSX to HTML
   ```bash
   git clone https://github.com/resend/react-email.git /tmp/react-email
   cd /tmp/react-email && npm install && npm run build
   # Then harvest compiled HTML from output
   ```

2. **Web scrape template galleries** (with rate limiting, robots.txt respect):
   - unlayer.com/templates (free section)
   - templateflip.com/email-templates
   - htmlemaildesigns.com

3. **Search GitHub forks** - Popular repos have forks with potential additions
   ```bash
   # API to find forks
   https://api.github.com/repos/leemunroe/responsive-html-email-template/forks
   https://api.github.com/repos/ckissi/responsive-html-email-templates/forks
   ```

4. **Check for email templates in unexpected places**:
   - CMS plugins (WordPress email templates)
   - E-commerce platforms (WooCommerce, Magento notification templates)
   - CRM/Marketing tools (HubSpot, Salesforce community templates)

## Reality Check

The 10,000 target is challenging. After extensive GitHub searching across multiple iterations:

**What we've found:**
- ~160 source directories indexed
- ~1,200 unique templates after deduplication
- Most high-quality open-source repos have been tapped

**Why the gap exists:**
- Quality email templates are scarce compared to website templates
- Most bulk collections (Stripo 1,600+, Beefree) are behind paywalls/accounts
- Many repos have components/snippets, not complete templates
- React-email/jsx-email templates need compilation
- Liquid/Handlebars templates need compilation

**Realistic options to reach 10k:**
1. Web scraping (requires careful implementation, robots.txt compliance)
2. Lowering quality thresholds (not recommended per runbook)
3. Including compiled framework output (React-email, Maizzle builds)
4. Adjusting target to reflect available open-source supply

## GitHub API Rate Limiting
Note: GitHub API has rate limits (60 requests/hour unauthenticated). If hitting limits, use git clone directly or wait an hour.

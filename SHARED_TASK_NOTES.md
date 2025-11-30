# TemplateForge Sourcing Task Notes

## Current Status (Updated)
- **Indexed**: ~1,287 items
- **Unique hashes**: ~1,100 (after dedupe)
- **Target**: 10,000 unique templates
- **Gap**: ~8,900 more templates needed
- **Sources tapped**: ~140+ directories in data/raw/

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

## Untapped/Underexplored Sources

### High Priority (Tier 1 - Should Have Bulk Content)
1. **Stripo** - 1,600+ templates but requires account to export. Try API or find exports.
2. **Beefree** - Similar to Stripo, large collection behind login.
3. **Litmus Community** - May have shared templates.
4. **Really Good Emails** - Curated gallery, may have HTML exports somewhere.

### GitHub Repos to Check
These may have more templates not yet fetched:
- `mailchimp/email-blueprints` - We have 37, repo has ~44
- `sendwithus/templates` - We have 117, appears complete
- Search for forks of popular template repos that might have additions

### Search Queries That Work
```bash
# GitHub API
https://api.github.com/search/repositories?q=email+template+mjml&sort=stars
https://api.github.com/search/repositories?q=email-templates+fork:false&sort=stars
```

### Template Repos Already Fully Tapped
- mjmlio/email-templates (22 MJML)
- Easy-Email-Pro/email-templates (35 MJML + HTML)
- sendwithus/templates (117 HTML)
- ColorlibHQ/email-templates (20 HTML)
- hunzaboy/CodedMailsFree (64 HTML)
- ActiveCampaign/postmark-templates (33 HTML)
- mailchimp/email-blueprints (44 HTML - now complete)
- Maizzle/starter-litmus (10 HTML - CEEJ + Slate themes)
- fintech_templates/fintech_clone (~200 HTML)
- stuartsantos_clone (~67 HTML)

## Strategy for Reaching 10k

Given the gap (~8,900), options include:

1. **More GitHub Mining** - Search for lesser-known repos with templates
2. **Web Scraping** - Carefully scrape gallery sites (respect robots.txt)
3. **Convert Framework Examples** - React-email, vue-email have TSX that compile to HTML
4. **Quality Over Quantity Adjustment** - If 10k is unrealistic, document actual available volume

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

1. **Compile React-email templates** - Install react-email, compile TSX to HTML (22+ templates)
   ```bash
   # In resend/react-email repo
   npm install && npm run build
   # Then harvest compiled HTML from output
   ```

2. **Search GitHub forks** - Many popular repos have forks with additional templates
   ```bash
   # API to find forks
   https://api.github.com/repos/leemunroe/responsive-html-email-template/forks
   ```

3. **Web scrape template galleries** (with rate limiting, robots.txt respect):
   - unlayer.com/templates (free section)
   - templateflip.com/email-templates
   - htmlemaildesigns.com

4. **Check NPM packages** - Some email libraries include template examples
   - @react-email/components
   - email-templates (npm package has examples)

5. **Track category balance** (from runbook):
   - Target 15-20% each: Welcome, Promo, Ecommerce, Newsletter, Transactional
   - Run analysis on current templates to identify gaps

## Reality Check
The 10,000 target is ambitious. Open-source/free HTML email templates are relatively scarce compared to website templates. Most quality templates are:
- Behind paywalls (Litmus, Stripo premium, Beefree premium)
- Require accounts to export
- Generated dynamically (not static files)

Consider:
- Adjusting target based on available quality sources
- Focusing on quality over quantity
- Documenting the practical ceiling for open-source templates

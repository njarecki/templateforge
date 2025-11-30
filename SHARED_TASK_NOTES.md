# TemplateForge Sourcing Task Notes

## Current Status (Updated 2025-11-30)
- **Indexed**: 1,437 items
- **Unique hashes**: 1,218 (after dedupe)
- **Target**: 10,000 unique templates
- **Gap**: ~8,800 more templates needed
- **Sources tapped**: ~160 directories in data/raw/

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

1. **Compile react-email/jsx-email TSX templates to HTML**
   - Both repos have TSX email templates that need compilation
   - Would add ~20-30 high-quality brand-inspired templates if compiled
   - Requires: Node.js build step

2. **Web scraping template galleries** (with rate limiting, robots.txt respect):
   - Stripo.email free templates (login-gated, but may have public HTML)
   - Beefree.io free templates (similar situation)
   - Really Good Emails archives

3. **Consider lowering quality gates** to increase yield:
   - 10KB threshold eliminates many usable templates
   - Table count >= 5 may be too strict for modern div-based layouts

## Reality Check

The 10,000 target is extremely challenging. After this iteration's extensive GitHub searching:

**Exhaustive search completed:**
- Checked 50+ potential repos via git clone
- Most named email template repos don't exist or are empty
- The awesome-emails list has been fully explored

**Repos confirmed not available or empty:**
- sendwithus/templates - ALREADY INDEXED
- wildbit/postmark-templates - ALREADY INDEXED
- konsav/email-templates - ALREADY INDEXED
- All Maizzle starters - ALREADY INDEXED
- hermes templates - ALREADY INDEXED
- Most email provider repos (Klaviyo, ActiveCampaign, etc) - don't exist publicly

**Repos checked but failed quality gates (this iteration):**
- resend/react-email - TSX only, no pre-compiled HTML
- shellscape/jsx-email - TSX only, no pre-compiled HTML
- thememountain/acorn - Components <10KB, not complete templates
- thememountain/pine - Components <10KB, not complete templates
- mautic/mautic - Only 1-2 tables (needs >=5)
- mailpoet/mailpoet - No media queries
- Mailtrain-org/mailtrain - Mosaico editor template (ko-bindings)

**Why the gap exists:**
- Quality email templates are scarce compared to website templates
- Most bulk collections (Stripo 1,600+, Beefree 1,000+) are behind paywalls/accounts
- Many repos have components/snippets, not complete templates
- React-email/jsx-email templates need compilation (TSX -> HTML)
- Many templates fail quality gates (under 10KB, no media queries, low table count)

**Conclusion:**
The open-source GitHub ecosystem has been thoroughly searched. To reach 10,000:
1. Compile TSX templates (react-email, jsx-email)
2. Scrape template galleries (Stripo, Beefree, Really Good Emails)
3. Lower quality gates to increase yield
4. Generate synthetic templates based on existing patterns

## GitHub API Rate Limiting
Note: GitHub API has rate limits (60 requests/hour unauthenticated). Using git clone directly avoids this.

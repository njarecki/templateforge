# TemplateForge Sourcing Task Notes

## Current Status (Updated 2025-11-30 - Iteration 6)
- **Indexed**: 1,453 items
- **Unique hashes**: 1,230 (after dedupe)
- **Target**: 10,000 unique templates
- **Gap**: ~8,770 more templates needed
- **Sources tapped**: ~165 directories in data/raw/

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

## New Sources Added This Iteration

1. **react_email_codeskills** - 2 templates (CodeSkills React-Email, compiled)
2. **bootstrap_email** - 3 templates (lyft, product-hunt, integration)
3. **mailjet_transactional** - 2 templates (MJML transactional)
4. **email_system_mjml** - 3 templates (Hoffmander email system)
5. **mjml_boilerplate** - 4 templates (Mikezotov transactional)
6. **premail** - 1 template (Premail MJML)
7. **maizzle_rss** - 1 template (Laracasts RSS)

Total added: ~16 templates, ~12 unique after dedupe

## Next Steps (Priority Order)

1. **Compile official react-email demo templates**
   - Requires full monorepo setup (workspace dependencies + Tailwind config)
   - Has ~20 brand-inspired templates (Stripe, Nike, GitHub, Notion, etc.)
   - Alternative: Create standalone compilation setup

2. **Web scraping template galleries** (with rate limiting, robots.txt respect):
   - Stripo.email free templates (1,600+ but login-gated)
   - Beefree.io free templates (1,000+ but login-gated)
   - Really Good Emails archives

3. **Consider lowering quality gates** to increase yield:
   - 10KB threshold eliminates many usable templates
   - Table count >= 5 may be too strict for modern div-based layouts
   - Media queries requirement blocks many table-based responsive templates

## Reality Check

The 10,000 target is extremely challenging. After 6 iterations:

**Exhaustive GitHub search completed:**
- All popular template repos (mjmlio, sendwithus, postmark, mailgun, etc.) - INDEXED
- All Maizzle starters - INDEXED
- All easy-email-pro templates - INDEXED
- Most GitHub Topics pages for email templates explored
- awesome-emails, awesome-opensource-email lists fully explored

**Major template sources that could add 1000+ templates:**
1. **Stripo.email** - 1,600+ templates (requires account/login)
2. **Beefree.io** - 1,000+ templates (requires account/login)
3. **Really Good Emails** - 5,000+ templates (may be scrapable)
4. **Litmus Community** - Unknown count (requires exploration)

**Why quality gates block many templates:**
- Many templates <10KB (especially transactional/simple ones)
- Table count <5 is common in modern div-based layouts
- Media queries absent in inline-styled templates (still responsive)
- Strict uniqueness check causes valid variations to be marked duplicates

**Conclusion:**
Open-source GitHub has been thoroughly searched. Remaining paths:
1. Web scraping commercial galleries (Stripo, Beefree, RGE)
2. Lower quality gates significantly
3. Generate synthetic templates from existing patterns
4. Compile TSX sources with full build setup

## Technical Notes

### React-Email Compilation
- Official react-email demo templates need full monorepo setup
- Tailwind config is shared across templates via imports
- Simple templates can be compiled with `npx email export`
- Package versions: react-email@5.0.5, @react-email/components@0.0.37

### MJML Compilation
- MJML templates compile to HTML with `npx mjml <file.mjml>`
- Some templates use mj-include (fragments) - need full file
- MJML 4.x produces responsive HTML with media queries

# TemplateForge — Sourcing-First Runbook (Do Not Quit)

Goal: Pull as many high-quality, legally safe email templates (HTML/MJML) as possible. Produce a clean catalog + raw files only. No generation, skins, or variants yet.

Non-Quit Rules
- Do not output “complete” or stop early; keep sourcing until explicitly told to stop or time budget ends.
- If a source is exhausted, move to the next; then broaden GitHub queries.

Scope & Legality
- Only public, legally reproducible sources: free/MIT/OSS templates, public galleries, vendor samples meant for display.
- Record license and URL for every item. Do not copy brand assets for later use; this step only collects raw HTML/MJML.

Target Sources (prioritized)
1) MJML Official Templates (MIT) — https://mjml.io/templates
2) Foundation for Emails examples — https://github.com/foundation/foundation-emails
3) Stripo Free Templates — https://stripo.email/templates/ (free filter)
4) Beefree Free Templates — https://beefree.io/templates/
5) Litmus community/public examples — https://litmus.com/community
6) Mailchimp sample templates — public examples/docs
7) Klaviyo/Shopify public examples (welcome/promo/newsletter)
8) GitHub packs: queries such as “email mjml templates”, “responsive html email templates free”, “open-source mjml templates”.

Quality Bar (Sourcing Stage)
- Prefer battle‑tested, responsive, section‑based layouts with modern patterns.
- Skip low-quality/spammy templates; focus on vendor galleries and reputable packs.

Output Artifacts
- Raw files: save as data/raw/<source_id>/<slug>.{html|mjml}
- Index: data/index/templates_<timestamp>.json with records:
  - id, source_id, source_name, url, license, type(html|mjml), file_path, content_hash, byte_size
  - quick_features: { sections_detected, has_media_queries, table_count }
- Dedupe map: data/index/dedupe_<timestamp>.json listing clusters and chosen keepers.

Dedupe Procedure
- Compute content_hash (sha256) and a structure_hash:
  - Strip text, keep tags/attrs, collapse whitespace. Shingle n=4 tag tokens; hash.
- Consider duplicates when content_hash matches OR Jaccard(structure_shingles) ≥ 0.85.
- Keep item from the more reputable source or larger byte_size; record others as duplicates.

Operational Settings
- Rate limit: 1–3 req/s per domain; exponential backoff on 429/5xx.
- Respect robots.txt; set UA: TemplateForge/1.0 (research, non-commercial).
- Retry up to 3x; skip on persistent failure; log errors.

Status Reporting (every 30–60 minutes)
- Print counts: fetched, unique, deduped out, sources done, errors.
- Never say “complete”; continue until STOP.

Start Now
- Harvest ≥300 unique base templates across sources above, maximizing diversity (welcome, promo, ecommerce, newsletter, transactional).
- Populate data/raw and data/index with accurate metadata and dedupe results.
- When done with all listed sources, expand GitHub queries and continue.

Helper Script (must use)
- Initialize folders: `python3 scripts/sourcing_indexer.py init`
- After saving each file under `data/raw/<source_id>/<slug>.<html|mjml>`, index it:
  `python3 scripts/sourcing_indexer.py add --source-id <id> --source-name "<name>" --url <url> --license <license> --type <html|mjml> --file data/raw/<source_id>/<slug>.<html|mjml>`
- Periodically dedupe: `python3 scripts/sourcing_indexer.py dedupe`
- Show progress: `python3 scripts/sourcing_indexer.py stats`

Index record includes: id, source_id, source_name, url, license, type, file_path, byte_size, content_hash, quick_features.

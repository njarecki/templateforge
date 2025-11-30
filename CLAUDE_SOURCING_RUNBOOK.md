# TemplateForge — Sourcing-First Runbook (Do Not Quit)

Goal (v3): Pull 10,000+ high‑quality, legally safe email templates (HTML/MJML) with strict early quality gates. Produce a clean catalog + raw files only. No generation, skins, or variants yet.

Non-Quit Rules
- Do not output “complete” or stop early; keep sourcing until explicitly told to stop or time budget ends.
- If a source is exhausted, move to the next; then broaden GitHub queries.
 - Target is ≥10,000 unique post‑dedupe. Never stop before that.

Scope & Legality
- Only public, legally reproducible sources: free/MIT/OSS templates, public galleries, vendor samples meant for display.
- Record license and URL for every item. Do not copy brand assets for later use; this step only collects raw HTML/MJML.

Source Tiers (pull by weight)
- Tier 1 (weight 5): MJML official (MIT), Postmark, Mailchimp Blueprints, Codedmails, Cerberus, Antwort, SendGrid/Paste, Shopify official, Foundation Emails (compiled example HTML).
- Tier 2 (weight 3): Beefree Free, Stripo Free, MailBakery public examples, Designmodo/Postcards samples, Waypoint/usewaypoint transactional.
- Tier 3 (weight 1): Reputable community GitHub packs (only keep if they pass gates below).

Seed URLs (Quick Start)
- MJML official raw repo (MIT):
  - Listing: https://github.com/mjmlio/email-templates/tree/master/templates
  - Raw files: https://raw.githubusercontent.com/mjmlio/email-templates/master/templates/<name>.mjml
  - Examples: arturia.mjml, austin.mjml, black-friday.mjml, christmas.mjml, welcome-email.mjml
- Foundation for Emails examples (Inky → HTML examples):
  - Listing: https://github.com/foundation/foundation-emails/tree/develop/templates
  - Raw files: https://raw.githubusercontent.com/foundation/foundation-emails/develop/templates/<name>.html
  - Examples: newsletter.html, marketing.html, sidebar.html, sidebar-hero.html, order.html
- Stripo free gallery:
  - Listing: https://stripo.email/templates/?price=free (paginate and collect detail pages)
  - Each template page exposes HTML export; record URL + license note as per site terms.
- Beefree free templates:
  - Listing: https://beefree.io/templates/ (filter to Free)
  - Collect detail pages; many allow public HTML preview/export.
- Litmus community/public examples:
  - Listing: https://litmus.com/community (filter for “Resources”, “Templates”)
- Mailchimp examples:
  - Guides/samples: https://mailchimp.com/resources/ and https://mailchimp.com/help/
  - Public sample templates pages often embed full HTML.
- Klaviyo/Shopify public examples:
  - Klaviyo: curated examples via blog/resources (search: site:klaviyo.com "email template")
  - Shopify: search queries like “site:shopify.com email template example welcome promo newsletter”.
- Popular GitHub packs (pull raw files):
  - https://github.com/leemunroe/responsive-html-email-template
  - https://github.com/TedGoas/Cerberus
  - https://github.com/mailgun/transactional-email-templates
  - https://github.com/mjmlio/mjml (examples under packages/mjml-*/)
  - https://github.com/InterNations/antwort (responsive patterns)
  - For each repo, use raw URLs: https://raw.githubusercontent.com/<owner>/<repo>/<branch>/<path>

Discovery Queries (expand when needed)
- "email mjml template pack", "responsive html email templates free", "open-source mjml templates", "newsletter html template github", "transactional email templates html".

Early Quality Gates (reject during harvest unless overridden)
- Size: raw/compiled file > 10 KB and < 350 KB.
- Responsiveness: media queries present in compiled HTML OR known responsive framework (MJML/Antwort/Cerberus/Foundation).
- Structure: table_count ≥ 5; must include obvious CTA/link AND footer/unsubscribe string.
- Uniqueness: reject if structure_hash Jaccard ≥ 0.90 vs. an existing item in the same source family.
- Red flags: inline base64 hero > 1 MB, heavy tracker scripts, excessive external font loads (>3 families).

Category Balance Targets
- Keep running tallies; aim ≥15–20% each for Welcome, Promo, Ecommerce, Newsletter, Transactional.
- If a category is underrepresented, backfill from Tier 1/2 sources first.

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
- Print: fetched, unique, deduped out, pass/fail by gate (size/responsive/structure/uniqueness/red‑flags), source mix, category mix, errors.
- Never say “complete”; continue until STOP. Keep a rolling top‑sources table by unique count.

Start Now
- Harvest ≥10,000 unique base templates (post‑dedupe) with the gates above. Keep going until the index shows at least 10,000 unique items.
- Populate data/raw and data/index with accurate metadata and dedupe results; keep category tallies balanced.
- Prioritize Tier 1/2 sources; only pull Tier 3 if passing gates AND needed for category balance.
- Expand GitHub queries aggressively after Tier 1/2 are saturated.

Helper Script (must use)
- Initialize folders: `python3 scripts/sourcing_indexer.py init`
- After saving each file under `data/raw/<source_id>/<slug>.<html|mjml>`, index it:
  `python3 scripts/sourcing_indexer.py add --source-id <id> --source-name "<name>" --url <url> --license <license> --type <html|mjml> --file data/raw/<source_id>/<slug>.<html|mjml>`
- Periodically dedupe: `python3 scripts/sourcing_indexer.py dedupe`
- Show progress: `python3 scripts/sourcing_indexer.py stats`

Success Criteria (do not stop before this)
- ≥10,000 indexed items after dedupe.
- ≥95% records with both license and URL populated.
- Healthy mix of `mjml` and `html`; prioritize MJML when available.
- Source diversity (≥10 sources, weighted to Tier 1/2) and category diversity (all five present within 15–25% bands).

Index record includes: id, source_id, source_name, url, license, type, file_path, byte_size, content_hash, quick_features.

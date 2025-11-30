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
- Harvest ≥1000 unique base templates across sources above, maximizing diversity (welcome, promo, ecommerce, newsletter, transactional). Keep going until the index shows at least 1000 unique (post‑dedupe) items.
- Populate data/raw and data/index with accurate metadata and dedupe results.
- Aim for breadth: at least 6 distinct sources and representation from all five categories.
- When done with all listed sources, expand GitHub queries and continue until the 1000 unique target is reached.

Helper Script (must use)
- Initialize folders: `python3 scripts/sourcing_indexer.py init`
- After saving each file under `data/raw/<source_id>/<slug>.<html|mjml>`, index it:
  `python3 scripts/sourcing_indexer.py add --source-id <id> --source-name "<name>" --url <url> --license <license> --type <html|mjml> --file data/raw/<source_id>/<slug>.<html|mjml>`
- Periodically dedupe: `python3 scripts/sourcing_indexer.py dedupe`
- Show progress: `python3 scripts/sourcing_indexer.py stats`

Success Criteria (do not stop before this)
- At least 1000 indexed items after dedupe.
- ≥95% records with both license and URL populated.
- Healthy mix of `mjml` and `html`; prioritize MJML when available.
- Source diversity (≥6 sources) and category diversity (welcome, promo, ecommerce, newsletter, transactional all present).

Index record includes: id, source_id, source_name, url, license, type, file_path, byte_size, content_hash, quick_features.

# TemplateForge — Compile & Enrich Runbook (Do Not Quit)

Goal: Continuously compile sourced templates and enrich the index with real HTML metrics and category tags, using your tokens where helpful. Do not stop until coverage is complete or explicitly told to STOP.

Non‑Quit Rules
- Never output “complete” or CONTINUOUS_CLAUDE_PROJECT_COMPLETE.
- Loop until 100% of `data/index/templates.json` items have an enriched entry in `data/index/templates_enriched.json`.

Prereqs
- Install MJML CLI (for compiling MJML): `npm install -g mjml`
- Repo scripts are local only; no network fetch needed here.

Core Loop
1) Initialize (if needed)
   - Ensure `data/index/templates.json` exists from the sourcing phase.
2) Compile & Enrich
   - Run: `python3 scripts/enrich_index.py --run`
   - This will:
     - Compile MJML to HTML (saves under `data/compiled/<source>/<name>.html` when possible)
     - Compute metrics on compiled (or raw) HTML: media queries, table counts, section hints, byte size
     - Tag categories via heuristics (Welcome, Newsletter, Ecommerce, Promo, Transactional)
     - Write `data/index/templates_enriched.json`
3) Gap Check
   - Compare counts between `templates.json` and `templates_enriched.json`. If any items missing or compilation failed, re‑run enrichment.
   - If MJML compilation fails, you may retry after installing MJML CLI or skip and record `compiled=false`.
4) Token Assist (classification polish)
   - Use your tokens to spot‑check and correct category tags when heuristics look weak (e.g., filenames with no strong keywords). Update enriched file accordingly.
5) Reporting (every 30–60 minutes)
   - Print: total indexed, enriched count, MJML compiled count, failure reasons, category distribution, media‑query rate.

Success Criteria
- 100% of items present in `templates_enriched.json` with metrics + categories.
- MJML items compiled where possible; failures recorded with error messages.
- Categories present for every item (at least one per item).

Next Steps (after enrichment)
- Proceed to normalization + quality scoring runs using the enriched index to filter the best candidates.

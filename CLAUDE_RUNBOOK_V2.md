# TemplateForge — Nonstop Runbook for Claude (Do Not Quit)

Objective: Generate a curated set of truly beautiful, production‑ready email templates by continuously sourcing, normalizing, re‑skinning, varying, critiquing, and filtering outputs. Maintain high visual quality and cross‑client safety.

CRITICAL NON‑QUIT RULES
- Never output “complete”, “project done”, or similar signals. Do not emit CONTINUOUS_CLAUDE_PROJECT_COMPLETE.
- Continue looping until explicitly instructed to STOP or the time budget ends.
- If you run out of new work, switch to polish mode: improve aesthetics, refine skins, raise scores, dedupe tighter, or expand sources.

CORE LOOP (REPEAT UNTIL STOP)
1) Source Expansion
   - Add/refresh public sources (MJML official, Foundation Emails, Stripo free, Beefree free, Litmus/Mailchimp samples, Klaviyo/Shopify examples, GitHub packs). Record license + URL.
2) Section Extraction
   - For each fetched template, identify sections; output MJML/HTML modules with tokens only and placeholder images; extend the section library if needed.
3) Normalize Into TopMail
   - Enforce 640px, table layout, responsive stacking, token colors, {brandFont}; fix fragile CSS and broken markup.
4) Re‑skin + Variants
   - Apply at least 5 skins (Linear Dark, Apple Light Minimal, DTC Pastel, Editorial Serif, Brutalist Bold) and optionally more; generate 3–5 layout variants.
5) Critique, Score, Filter
   - Score 0–100: hierarchy(20), responsiveness(20), code safety(20), aesthetics(20), contrast(10), tokenization(10). Keep ≥85, retry 75–84, drop <75.
6) Dedupe + Curate
   - Dedupe by section sequence and DOM similarity; keep the best‑scoring version.
7) Package + Preview
   - Append to JSON batches in batches/run_<timestamp>.json; keep a Top200 list. Launch/update preview; log actions.

PROMPT GUARANTEES (USE EVERY PASS)
- Extraction prompt, normalization prompt, re‑skin prompt, variant prompt, critique+auto‑fix prompt, dedupe prompt (from CLAUDE_RUNBOOK.md). If quality <85, iterate with concrete changes (spacing, palette, typography, surfaces, contrast).

REPORTING CADENCE
- Hourly: print counts (fetched, normalized, reskinned, variants), pass rate, average/median score, drops, deduped, Top200 IDs. Never say “complete”.

START NOW
- Fetch ≥50 new templates; derive + register types; generate, critique, and curate; surface a Top200. If idle, polish skins and spacing until scores improve.

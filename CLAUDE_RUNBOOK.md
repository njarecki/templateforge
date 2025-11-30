# TemplateForge — Claude Runbook (Next 20 Hours)

Goal: Produce a large set of genuinely beautiful, production-ready email templates. Bias toward quality and breadth. You have ample tokens for deep search, multi-pass critique/fixes, and style exploration.

## Operating Principles
- Honor TopMail rules: 640px max width, table layout, responsive stacking, tokens only, placeholder images, no brand assets.
- Prefer MJML for manipulation; compile to HTML for cross-client checks.
- Automate extraction → normalization → re-skin → variants → critique → filter.
- Keep only high-quality outputs; aggressively drop mediocre results.

## Sources (Expand and Harvest)
Target public, legally safe templates. For each, capture license/URL.
- Primary: MJML official templates, Foundation for Emails.
- Add now: Stripo (free), Beefree (free), Litmus public examples, Mailchimp samples, Klaviyo, Shopify examples, curated GitHub packs (query: “email mjml template pack”, “responsive html email templates free”).
- Deliver 150+ unique base templates before re-skinning. De-duplicate by layout (see Dedupe section).

Suggested fetch commands (save raw HTML/MJML + metadata):
- Use/extend `external_sources.py` to add new sources; then `python3 pipeline.py --fetch-external --output external_batch.json`.

## High-Level Plan (Timeboxed)
1) Hours 0–3: Expand sources, fetch ≥150 base templates. Record license + URL.
2) Hours 3–6: Section extraction to modules (MJML/HTML). Build/extend section types as needed.
3) Hours 6–10: Normalize into tokens + TopMail rules. Ensure clean, minimal HTML/MJML.
4) Hours 10–14: Re-skin into at least 5 styles (Linear Dark, Apple Light Minimal, DTC Pastel, Editorial Serif, Brutalist Bold) and optionally 3–5 extra styles.
5) Hours 14–16: Generate 3–5 layout variants per template.
6) Hours 16–19: Multi-pass critique + auto-fix. Score, rank, and drop weak ones. Dedupe.
7) Hour 19–20: Final packaging, stats, and preview pass.

## Prompt Kits (Copy/Paste)
Use these repeatedly. Keep HTML self-contained and production-ready.

- Section Extraction Prompt:
```
Given this email HTML/MJML, identify logical sections (hero, 1col_text, 2col_text_image, product_grid, testimonial, cta_band, header_nav, offer_banner, order_summary, social_icons, footer_*). For each section:
- type, variant, brief description
- output email-safe HTML or MJML with placeholders and tokens
Replace all content with tokens: {{headline}}, {{subheadline}}, {{bodyText}}, {{ctaLabel}}, {{footerText}}. Replace images with placeholders. Keep table layout and responsive stacking.
Return JSON array of sections.
```

- Normalization Prompt:
```
Rewrite this template to the TopMail system:
- 640px max; centered table wrapper; tables for layout
- Spacing increments: 8/12/16/24px
- Tokens only: {brandBG}, {brandPrimary}, {brandSecondary}, {brandText}, {brandAccent}, {brandFont}
- Placeholder images only (hero 640x320, product 300, icon 64)
- Mobile stacking; Outlook-safe CSS; remove fragile CSS
Output clean, production HTML or MJML. Do not introduce brand assets.
```

- Re-skin Prompt:
```
Keep layout; apply style SKIN_NAME using tokens only. Ensure cohesive typography, spacing, contrast, and aesthetic quality. Output full HTML/MJML.
Skins: Linear Dark, Apple Light Minimal, DTC Pastel, Editorial Serif, Brutalist Bold.
```

- Layout Variant Prompt:
```
Produce 3–5 structural variants by reordering sections and optionally inserting/removing non-critical blocks (e.g., testimonial, cta_band). Preserve responsiveness and quality.
```

- Critique + Auto-Fix Prompt:
```
Critique this email for: visual hierarchy, CTA clarity, spacing consistency, mobile stacking, color contrast, accessibility (alt text), Outlook-safety, broken tables/tags. List issues succinctly, then return a corrected template. Repeat until no issues remain.
```

- Dedupe Prompt:
```
Compare these two templates’ section sequences and DOM structure. If ≥85% similar, keep only the higher-quality version (based on critique score). Explain briefly.
```

## Quality Gate (Score + Filter)
- Score 0–100 using weighted rubric: hierarchy(20), responsiveness(20), contrast(10), code safety(20), tokenization(10), aesthetics(20).
- Keep only ≥85. Re-critique and fix borderline 75–84. Drop <75.
- Enforce: 640px width; tokens only; placeholder images; no inline brand colors; role="presentation" on tables; alt text on images.

## Dedupe Strategy
- Canonicalize to section-type sequence (e.g., header_nav → hero → 1col_text → cta_band → footer_simple).
- Hash shingled n-grams of sequences (n=3–4). Merge near-duplicates (Jaccard ≥0.8).
- Secondary: DOM-based similarity on compiled HTML.

## Output & Artifacts
- For each base template: normalized, 5+ re-skins, 3–5 variants. Include metadata: source, license, category, tags, sections, score.
- Save batches as JSON: `batches/run_<timestamp>.json` matching the shape from `OBJECTIVE.md`.
- Optionally compile MJML to HTML using `python3 pipeline.py --compile --format mjml`.

## Repo Integration Notes
- `pipeline.py` already supports: batch generation, validation, MJML convert/compile, preview server.
- `external_sources.py` + `template_derivation.py`: extend sources and register derived templates; then generate via pipeline for skins/variants.
- Consider adding a sourcing-first mode in `pipeline.py` that: fetches → derives → registers → runs full batch.

## Stretch Styles (Optional)
If time allows, add: Gradient Pop, Neon Gaming, Warm Beige Luxury, Black & Gold Premium, Minimal White Space. Keep tokens-only discipline.

## Final Deliverables (End of 20 Hours)
- JSON package(s) with ≥200–300 high-quality templates after filtering.
- A brief quality report: counts, pass rate, dropped duplicates, average score, top styles.
- Optional: Start `preview_server.py` and spot-check 10 random outputs.

---
Stay rigorous: if a template looks merely “okay,” fix or drop it. Beauty and robustness over raw quantity.

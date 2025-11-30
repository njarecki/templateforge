# TemplateForge — Design Generation Runbook (Do Not Quit)

Goal: Generate 10,000 production‑ready templates for review (this phase is generation only). Use Claude to synthesize high‑quality designs via (1) recombining strong layouts from our corpus and (2) Claude’s own creativity under the design guidelines. Never quit early.

Generation Mix (strict)
- 50% Inspired: derived from seed layouts in our corpus (recombined/abstracted, not copied).
- 50% Original: Claude‑original layouts that follow our section library and TopMail rules.

Non‑Quit Rules
- Do not output “complete” or CONTINUOUS_CLAUDE_PROJECT_COMPLETE.
- Keep looping: select seeds → synthesize layouts → style → critique → score → dedupe → package, until explicitly told to STOP.

Inputs
- Enriched index: `data/index/templates_enriched.json` (use compiled HTML when available)
- Compiled HTML: `data/compiled/<source>/<file>.html`
- Generated index (output): `data/index/generated.json`
 - Validator: `template_validator.py` (used by the helper script to ensure files work)

Core Loop (repeat until 10,000 kept ≥85 score)
1) Seed Selection (balance diversity)
   - Pick 200–400 high‑quality seeds (score proxies: has_media_queries=true, table_count≥8, byte_size_html 20–220 KB, categories evenly split across Welcome/Promo/Ecommerce/Newsletter/Transactional).
   - Prefer Tier‑1/2 sources; avoid near‑duplicates via structure hash.

2) Abstract + Recombine Layouts
   - From each seed, extract a simple section map (e.g., header_nav → hero → 2col_text_image → product_grid → testimonial → cta_band → footer).
   - Generate 3–5 novel maps per seed by:
     - Reordering blocks (keep CTA above fold in ≥1 variant)
     - Swapping equivalent blocks (subhero vs hero, 2col vs 1col+image)
     - Inserting/removing one optional block (testimonial/offer/pricing)
   - Enforce constraints: 640px max width, table layout, role="presentation" on tables, CTA present, footer/unsubscribe present.

3) Synthesize Fresh Templates (MJML or HTML)
   - For each new map, ask Claude to generate clean MJML (preferred) or email‑safe HTML using TopMail tokens and placeholders only. No brand assets.
   - Tokens/colors: `{brandBG, brandPrimary, brandSecondary, brandText, brandAccent, brandFont}`; images = placeholders.
   - Ensure files work: if HTML, they should pass basic validation (doctype, viewport, tables present, alt text) — the helper script will check and report.

4) Style Synthesis (apply + extend)
   - Apply the 5 core skins (Linear Dark, Apple Light Minimal, DTC Pastel, Editorial Serif, Brutalist Bold).
   - Add at least 5 extra style packs (tokens only): Minimal White, Warm Neutral, Modern Gradient, Black & Gold Premium, Neon Gaming.

5) Critique + Auto‑Improve (iterate)
   - Validate visual hierarchy, spacing rhythm, CTA clarity, responsive stacking, accessibility (alt), Outlook‑safe code.
   - Score 0–100: hierarchy(20), responsiveness(20), code safety(20), aesthetics(20), contrast(10), tokenization(10).
   - Fix issues and re‑score up to 2 iterations. Keep only ≥85.

6) Dedupe + Uniqueness
   - Compute structure hash from section map + DOM shingles; drop if Jaccard ≥0.85 vs. existing generated or sourced items.
   - Keep best‑scoring representative per cluster.

7) Package (tag origin and validate)
   - Use the helper:
     `python3 scripts/design_pipeline.py add-generated \
        --id <id> \
        --origin <inspired|original> \
        --category <cat> \
        --style <style> \
        --score <0-100> \
        --map '<[...]>' \
        --seeds '<[...]>' \
        --format <html|mjml> \
        --file <path>`
   - The script stores files under `data/generated/<category>/<id>/` and appends to `data/index/generated.json` with: id, origin (inspired|original), tags (includes origin and "generated"), source_seeds, section_map, style, score, categories (if known), file paths, validation results.

CLI Helper (must use)
- Initialize: `python3 scripts/design_pipeline.py init`
- Add a template (validates HTML): `python3 scripts/design_pipeline.py add-generated --id ... --origin <inspired|original> --category ... --style ... --score ... --map '<[...]>' --seeds '<[...]>' --format <html|mjml> --file <path>`
- Dedupe: `python3 scripts/design_pipeline.py dedupe` (writes `data/index/generated_dedupe.json`)
- Stats: `python3 scripts/design_pipeline.py stats`

Prompt Kits (copy/paste)
- Layout Abstraction:
  """
  You are extracting an abstract section map from this HTML/MJML. Return a JSON list of section types in order using this library: hero, subhero, 1col_text, 2col_text_image, 3col_features, product_grid, testimonial, story_block, cta_band, header_nav, offer_banner, order_summary, social_icons, footer_simple, footer_complex, divider, spacer.
  """
- Layout Synthesis:
  """
  Given this section map, produce 5 novel maps that keep a strong hero→content→CTA flow, insert/remove at most one optional block, and keep responsiveness. Keep CTA and footer.
  """
- MJML/HTML Generation:
  """
  Generate a complete email in MJML using the given section map. Constraints: 640px max, table layout, tokens only ({brand*}), placeholders for all images, alt text present, role="presentation" on tables, responsive stacking. Output MJML only.
  """
- Style Application:
  """
  Apply the SKIN style to the same layout using tokens only. Ensure cohesive typography, spacing, contrast. Return full MJML.
  """
- Critique + Improve:
  """
  Critique the email for hierarchy, spacing, CTA clarity, responsiveness, accessibility, Outlook safety. List issues and return a corrected version. Target score ≥85.
  """

Acceptance Criteria
- Each batch yields ≥500 new, unique, high‑quality templates (score ≥85) across categories and styles. Maintain a 50/50 split: Inspired vs Original.
- 0 brand assets; all images are placeholders; tokens only.
- Uniqueness enforced via structure hash and DOM shingles (Jaccard < 0.85).

Reporting (hourly)
- Seeds used, synthesized layouts, generated MJML/HTML, pass/fail counts, average/median score, dropped duplicates, style distribution.

Stop Conditions
- Only stop when explicitly instructed OR when `data/index/generated.json` shows ≥10,000 unique (post‑dedupe) items scored ≥85. Otherwise keep improving aesthetics and diversity (industries, tones, styles) using the same loop.

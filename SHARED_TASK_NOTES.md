# TemplateForge Generation Task Notes

## Current Status (Updated 2025-11-30)
- **Generated**: 158 templates (79 original, 79 inspired)
- **Target**: 10,000 unique templates (score ≥85)
- **Required split**: 50% inspired / 50% original
- **Current split**: 50% original / 50% inspired (perfectly balanced)
- **All templates**: Valid HTML, MJML-compiled, 0 duplicates

## Run Commands
```bash
# Check progress
python3 scripts/design_pipeline.py stats

# Add a generated template
python3 scripts/design_pipeline.py add-generated \
  --id <id> \
  --origin <inspired|original> \
  --category <Welcome|Promo|Ecommerce|Newsletter|Transactional> \
  --style <style_name> \
  --score <0-100> \
  --map '<["section1","section2",...]>' \
  --seeds '<["seed1","seed2"]>' \
  --format html \
  --file <path>

# Compile MJML to HTML (use relative paths from project root)
npx mjml temp_generation/input.mjml -o temp_generation/output.html
```

## Category Distribution (Current)
- Ecommerce: 34
- Transactional: 32
- Newsletter: 31
- Promo: 31
- Welcome: 30

## Section Library (from runbook)
hero, subhero, 1col_text, 2col_text_image, 3col_features, product_grid, testimonial, story_block, cta_band, header_nav, offer_banner, order_summary, social_icons, footer_simple, footer_complex, divider, spacer, countdown, numbered_list

## Style Packs
Core: Linear Dark, Apple Light Minimal, DTC Pastel, Editorial Serif, Brutalist Bold
Extra: Minimal White, Warm Neutral, Modern Gradient, Black & Gold Premium, Neon Gaming

## Token Reference
Colors: {brandBG}, {brandPrimary}, {brandSecondary}, {brandText}, {brandAccent}
Typography: {brandFont}
All images: placeholder URLs from placehold.co

## Next Steps (Priority)

1. **Scale up volume** (need 100x+ more per iteration):
   - Target 100-200 new templates per iteration to reach 10,000
   - At current pace (~20/iteration), would take ~500 iterations
   - Need to parallelize and automate more

2. **Batch MJML workflow (works well)**:
   - Create MJML files in temp_generation/
   - Compile all at once: `for f in temp_generation/*.mjml; do npx mjml "$f" -o "${f%.mjml}.html"; done`
   - Add each with metadata via design_pipeline.py
   - Run dedupe after each batch

3. **Style variety (good coverage)**:
   - All 10 style packs being used
   - Continue rotating through styles per category

## Latest Batch Added (24 new templates)

**Original (13):**
- welcome_original_014 (Welcome, Warm Neutral, score 91)
- welcome_original_015 (Welcome, Linear Dark, score 92)
- promo_original_012 (Promo, DTC Pastel, score 92)
- promo_original_013 (Promo, Apple Light Minimal, score 91)
- promo_original_014 (Promo, Neon Gaming, score 92)
- ecommerce_original_012 (Ecommerce, Minimal White, score 91)
- ecommerce_original_013 (Ecommerce, Editorial Serif, score 92)
- ecommerce_original_014 (Ecommerce, DTC Pastel, score 91)
- newsletter_original_014 (Newsletter, Modern Gradient, score 91)
- newsletter_original_015 (Newsletter, Brutalist Bold, score 92)
- newsletter_original_016 (Newsletter, Warm Neutral, score 91)
- transactional_original_011 (Transactional, Warm Neutral, score 91)
- transactional_original_012 (Transactional, Apple Light Minimal, score 90)

**Inspired (11):**
- welcome_inspired_014 (Welcome, Neon Gaming, score 90)
- welcome_inspired_015 (Welcome, Black & Gold Premium, score 91)
- promo_inspired_013 (Promo, Linear Dark, score 91)
- promo_inspired_014 (Promo, DTC Pastel, score 90)
- ecommerce_inspired_014 (Ecommerce, Warm Neutral, score 91)
- ecommerce_inspired_015 (Ecommerce, Modern Gradient, score 91)
- newsletter_inspired_014 (Newsletter, Apple Light Minimal, score 90)
- newsletter_inspired_015 (Newsletter, Editorial Serif, score 92)
- transactional_inspired_013 (Transactional, Minimal White, score 90)
- transactional_inspired_014 (Transactional, Linear Dark, score 91)
- transactional_inspired_015 (Transactional, Brutalist Bold, score 90)

## Quality Criteria (from runbook)
- Score ≥85 to keep
- 640px max width
- Table layout with role="presentation"
- CTA present and above fold in ≥1 variant
- Footer with unsubscribe present
- Alt text on all images
- Responsive stacking via media queries

## Files
- Generated templates: `data/generated/<category>/<id>/`
- Generated index: `data/index/generated.json`
- Source seeds: `data/index/templates_enriched.json`
- Compiled seeds: `data/compiled/`
- Temp workspace: `temp_generation/`

## Quality Seeds Available (381 total)
High-quality seeds with: media queries, table_count≥8, 20-220KB HTML
- Ecommerce: 229 seeds
- Newsletter: 139 seeds
- Transactional: 76 seeds
- Promo: 67 seeds
- Welcome: 23 seeds

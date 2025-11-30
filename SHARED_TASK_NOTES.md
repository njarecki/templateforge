# TemplateForge Generation Task Notes

## Current Status (Updated 2025-11-30)
- **Generated**: 45 templates (23 original, 22 inspired)
- **Target**: 10,000 unique templates (score ≥85)
- **Required split**: 50% inspired / 50% original
- **Current split**: 51% original / 49% inspired (nearly balanced)
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

# Compile MJML to HTML
npx mjml input.mjml -o output.html
```

## Category Distribution (Current)
- Ecommerce: 10
- Transactional: 10
- Welcome: 9
- Promo: 8
- Newsletter: 8

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

1. **Scale up volume** (need 10x-20x more per iteration):
   - Target 100+ new templates per iteration to reach 10,000
   - Maintain 50/50 original/inspired balance
   - Use batch MJML generation workflow

2. **Increase batch efficiency**:
   - Create multiple MJML templates in temp_generation/
   - Compile all at once with loop: `for f in *.mjml; do npx mjml "$f" -o "${f%.mjml}.html"; done`
   - Add each with proper metadata via design_pipeline.py
   - Run dedupe after each batch

3. **Style variety**:
   - Ensure all 10 style packs are being used
   - Create style variants of existing layouts

## Templates Added Latest Batch (11 new)
**Original (6):**
- welcome_original_004 (Welcome, Warm Neutral, score 89)
- welcome_original_005 (Welcome, Modern Gradient, score 90)
- promo_original_002 (Promo, Black & Gold Premium, score 91)
- ecommerce_original_002 (Ecommerce, Editorial Serif, score 92)
- transactional_original_002 (Transactional, Apple Light Minimal, score 91)
- newsletter_original_004 (Newsletter, Editorial Serif, score 90)

**Inspired (5):**
- promo_inspired_003 (Promo, DTC Pastel, score 90)
- ecommerce_inspired_003 (Ecommerce, Apple Light Minimal, score 89)
- transactional_inspired_003 (Transactional, Linear Dark, score 91)
- welcome_inspired_004 (Welcome, Minimal White, score 88)
- newsletter_inspired_004 (Newsletter, Modern Gradient, score 90)

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

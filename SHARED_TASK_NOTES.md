# TemplateForge Generation Task Notes

## Current Status (Updated 2025-11-30)
- **Generated**: 34 templates (17 original, 17 inspired)
- **Target**: 10,000 unique templates (score ≥85)
- **Required split**: 50% inspired / 50% original
- **Current split**: 50% original / 50% inspired (BALANCED)
- **All templates**: Valid HTML, MJML-compiled

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
- Ecommerce: 8
- Transactional: 8
- Promo: 6
- Newsletter: 6
- Welcome: 6

## Section Library (from runbook)
hero, subhero, 1col_text, 2col_text_image, 3col_features, product_grid, testimonial, story_block, cta_band, header_nav, offer_banner, order_summary, social_icons, footer_simple, footer_complex, divider, spacer

## Style Packs
Core: Linear Dark, Apple Light Minimal, DTC Pastel, Editorial Serif, Brutalist Bold
Extra: Minimal White, Warm Neutral, Modern Gradient, Black & Gold Premium, Neon Gaming

## Token Reference
Colors: {brandBG}, {brandPrimary}, {brandSecondary}, {brandText}, {brandAccent}
Typography: {brandFont}
All images: placeholder URLs from placehold.co

## Next Steps (Priority)

1. **Scale up volume** (50/50 balance achieved):
   - Target 50+ new templates per iteration
   - Continue until 10,000 unique templates reached
   - Maintain 50/50 original/inspired balance

2. **Apply style variations**:
   - Create 2-3 style variants per template
   - All 10 style packs being used

3. **Batch generation workflow**:
   - Create MJML templates in temp_generation/
   - Compile: `cd temp_generation && npx mjml <file>.mjml -o <file>.html`
   - Add each with proper metadata via design_pipeline.py
   - Run dedupe after each batch

## Templates Added This Iteration (14 new)
**Original (9):**
- welcome_original_001 (Welcome, Linear Dark, score 88)
- welcome_original_002 (Welcome, Apple Light Minimal, score 89)
- welcome_original_003 (Welcome, DTC Pastel, score 90)
- newsletter_original_001 (Newsletter, Editorial Serif, score 91)
- newsletter_original_002 (Newsletter, Minimal White, score 90)
- newsletter_original_003 (Newsletter, Brutalist Bold, score 88)
- promo_original_001 (Promo, Brutalist Bold, score 92)
- ecommerce_original_001 (Ecommerce, Apple Light Minimal, score 91)
- transactional_original_001 (Transactional, Linear Dark, score 90)

**Inspired (5):**
- welcome_inspired_003 (Welcome, Modern Gradient, score 89)
- newsletter_inspired_003 (Newsletter, Editorial Serif, score 90)
- promo_inspired_002 (Promo, DTC Pastel, score 91)
- ecommerce_inspired_002 (Ecommerce, Warm Neutral, score 89)
- transactional_inspired_002 (Transactional, Linear Dark, score 90)

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

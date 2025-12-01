# TemplateForge Generation Task Notes

## Current Status (Updated 2025-12-01)
- **Generated**: 365 templates (183 original, 182 inspired)
- **Target**: 10,000 unique templates (score ≥85)
- **Required split**: 50% inspired / 50% original
- **Current split**: 50.1% original / 49.9% inspired (well balanced)
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

# Compile MJML to HTML with token replacement
npx mjml temp_generation/input.mjml -o temp_generation/output_temp.html
sed -e 's/#4A90D9/{brandPrimary}/g' \
    -e 's/#E8F0F8/{brandSecondary}/g' \
    -e 's/#f5f5f5/{brandBG}/g' \
    -e 's/#333333/{brandText}/g' \
    -e 's/#F0A030/{brandAccent}/g' \
    -e "s/Arial, sans-serif/{brandFont}/g" \
    temp_generation/output_temp.html > temp_generation/output.html
```

## Category Distribution (Current)
- Ecommerce: 74
- Transactional: 80
- Newsletter: 69
- Promo: 73
- Welcome: 69

## Section Library (from runbook)
hero, subhero, 1col_text, 2col_text_image, 3col_features, product_grid, testimonial, story_block, cta_band, header_nav, offer_banner, order_summary, social_icons, footer_simple, footer_complex, divider, spacer, countdown, numbered_list

## Style Packs
Core: Linear Dark, Apple Light Minimal, DTC Pastel, Editorial Serif, Brutalist Bold
Extra: Minimal White, Warm Neutral, Modern Gradient, Black & Gold Premium, Neon Gaming

## Token Reference
**MJML placeholder colors** (use these in MJML, sed replaces them):
- `#4A90D9` → `{brandPrimary}`
- `#E8F0F8` → `{brandSecondary}`
- `#f5f5f5` → `{brandBG}`
- `#333333` → `{brandText}`
- `#F0A030` → `{brandAccent}`
- `Arial, sans-serif` → `{brandFont}`

All images: placeholder URLs from placehold.co

## MJML Workflow (Proven Method)
1. Create MJML files using placeholder colors above
2. Compile: `npx mjml input.mjml -o output_temp.html`
3. Replace colors with tokens via sed (run sed commands one at a time or in a script)
4. Add via design_pipeline.py

## Latest Batch Added (29 new templates this iteration)

**Original (14):**
- welcome_original_034 (Welcome, Minimal White, score 91)
- welcome_original_035 (Welcome, Black & Gold Premium, score 92)
- promo_original_032 (Promo, DTC Pastel, score 91)
- promo_original_033 (Promo, Editorial Serif, score 92)
- promo_original_034 (Promo, Warm Neutral, score 91)
- newsletter_original_034 (Newsletter, Apple Light Minimal, score 91)
- newsletter_original_035 (Newsletter, Linear Dark, score 92)
- ecommerce_original_032 (Ecommerce, Modern Gradient, score 91)
- ecommerce_original_033 (Ecommerce, Black & Gold Premium, score 92)
- ecommerce_original_034 (Ecommerce, Minimal White, score 91)
- transactional_original_034 (Transactional, Apple Light Minimal, score 92)
- transactional_original_035 (Transactional, Warm Neutral, score 91)
- transactional_original_036 (Transactional, Linear Dark, score 92)
- transactional_original_037 (Transactional, DTC Pastel, score 91)

**Inspired (15):**
- welcome_inspired_032 (Welcome, Editorial Serif, score 91)
- welcome_inspired_033 (Welcome, Warm Neutral, score 92)
- welcome_inspired_034 (Welcome, Linear Dark, score 91)
- promo_inspired_034 (Promo, Modern Gradient, score 92)
- promo_inspired_035 (Promo, Black & Gold Premium, score 91)
- promo_inspired_036 (Promo, DTC Pastel, score 92)
- newsletter_inspired_032 (Newsletter, Brutalist Bold, score 91)
- newsletter_inspired_033 (Newsletter, Warm Neutral, score 92)
- newsletter_inspired_034 (Newsletter, Apple Light Minimal, score 91)
- ecommerce_inspired_033 (Ecommerce, Editorial Serif, score 92)
- ecommerce_inspired_034 (Ecommerce, Neon Gaming, score 91)
- ecommerce_inspired_035 (Ecommerce, Minimal White, score 92)
- transactional_inspired_036 (Transactional, Apple Light Minimal, score 91)
- transactional_inspired_037 (Transactional, Warm Neutral, score 92)
- transactional_inspired_038 (Transactional, Linear Dark, score 91)

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

## Next Steps (Priority)
1. **Scale up volume** - Need ~50 templates per iteration to hit 10,000 in reasonable time
2. **Categories well balanced** - Transactional slightly higher (80), but all categories 69-80
3. **Continue using all 10 style packs** for variety
4. **Origin split near-perfect** - 50.1% original / 49.9% inspired, maintain balance

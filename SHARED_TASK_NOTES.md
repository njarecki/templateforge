# TemplateForge Generation Task Notes

## Current Status (Updated 2025-11-30)
- **Generated**: 10 templates (8 original, 2 inspired)
- **Target**: 10,000 unique templates (score ≥85)
- **Required split**: 50% inspired / 50% original
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
- Ecommerce: 3
- Transactional: 3
- Promo: 2
- Newsletter: 1
- Welcome: 1

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

1. **Generate more "inspired" templates** - Currently at 20% inspired, need 50%
   - Use seed templates from `data/index/templates_enriched.json`
   - Abstract section maps and recombine with variations
   - Focus on high-quality seeds (has_media_queries, table_count≥8, 20-220KB)

2. **Increase volume across categories**:
   - Welcome: More onboarding flows
   - Newsletter: Blog digests, weekly roundups
   - Ecommerce: Cart recovery, product launches, reviews
   - Transactional: Account confirmations, receipts
   - Promo: Flash sales, seasonal, loyalty

3. **Apply style variations**:
   - Each template should have 2-3 style variants
   - Use all 10 style packs for diversity

4. **Batch generation approach**:
   - Create 50 templates per session
   - Compile all MJML → HTML
   - Add to index with proper metadata
   - Run dedupe after each batch

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

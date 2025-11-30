# TemplateForge Generation Task Notes

## Current Status (Updated 2025-11-30)
- **Generated**: 20 templates (8 original, 12 inspired)
- **Target**: 10,000 unique templates (score ≥85)
- **Required split**: 50% inspired / 50% original
- **Current split**: 40% original / 60% inspired
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
- Ecommerce: 6
- Transactional: 6
- Promo: 4
- Newsletter: 2
- Welcome: 2

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

1. **Generate more "original" templates** - Currently at 40% original, need 50%
   - Create diverse original layouts using section library
   - Focus on underrepresented categories: Welcome, Newsletter

2. **Scale up volume**:
   - Batch generate 50+ templates per session
   - Continue until 10,000 unique templates reached
   - Categories needed most: Welcome, Newsletter

3. **Apply style variations**:
   - Create 2-3 style variants per template
   - All 10 style packs now being used

4. **Batch generation workflow**:
   - Create MJML templates in temp_generation/
   - Compile all: `for f in *.mjml; do npx mjml "$f" -o "${f%.mjml}.html"; done`
   - Add each with proper metadata via design_pipeline.py
   - Run dedupe after each batch

## Templates Added This Session (10 inspired)
- welcome_inspired_002 (Welcome, Apple Light Minimal, score 88)
- receipt_inspired_001 (Transactional, Linear Dark, score 89)
- cart_inspired_001 (Ecommerce, DTC Pastel, score 90)
- newsletter_inspired_002 (Newsletter, Editorial Serif, score 91)
- promo_inspired_001 (Promo, Brutalist Bold, score 90)
- account_confirm_inspired_001 (Transactional, Minimal White, score 87)
- product_launch_inspired_001 (Ecommerce, Black & Gold Premium, score 92)
- review_request_inspired_001 (Transactional, Warm Neutral, score 88)
- event_invite_inspired_001 (Promo, Modern Gradient, score 91)
- loyalty_program_inspired_001 (Ecommerce, Neon Gaming, score 89)

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

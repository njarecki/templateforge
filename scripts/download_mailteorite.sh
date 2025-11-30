#!/bin/bash
cd /home/nick/templateforge
mkdir -p data/raw/mailteorite

# Download from correct paths
base_url="https://raw.githubusercontent.com/Mailteorite/mjml-email-templates/main"

# Welcome
curl -sL "${base_url}/mjml/welcome/01-welcome-classic.mjml" -o data/raw/mailteorite/welcome_01.mjml
curl -sL "${base_url}/mjml/welcome/02-welcome-tutorial.mjml" -o data/raw/mailteorite/welcome_02.mjml
curl -sL "${base_url}/mjml/welcome/03-welcome-benefits.mjml" -o data/raw/mailteorite/welcome_03.mjml

# Password Reset
curl -sL "${base_url}/mjml/password-reset/01-password-reset-simple.mjml" -o data/raw/mailteorite/password_reset_01.mjml
curl -sL "${base_url}/mjml/password-reset/02-password-reset-security.mjml" -o data/raw/mailteorite/password_reset_02.mjml
curl -sL "${base_url}/mjml/password-reset/03-password-changed.mjml" -o data/raw/mailteorite/password_reset_03.mjml

# Receipt Invoice
curl -sL "${base_url}/mjml/receipt-invoice/01-receipt-simple.mjml" -o data/raw/mailteorite/receipt_01.mjml
curl -sL "${base_url}/mjml/receipt-invoice/02-receipt-detailed.mjml" -o data/raw/mailteorite/receipt_02.mjml
curl -sL "${base_url}/mjml/receipt-invoice/03-invoice-business.mjml" -o data/raw/mailteorite/invoice_01.mjml

# Product Launch
curl -sL "${base_url}/mjml/product-launch/01-product-launch-hero.mjml" -o data/raw/mailteorite/product_launch_01.mjml
curl -sL "${base_url}/mjml/product-launch/02-promo-discount.mjml" -o data/raw/mailteorite/promo_discount.mjml
curl -sL "${base_url}/mjml/product-launch/03-flash-sale.mjml" -o data/raw/mailteorite/flash_sale.mjml

# Abandoned Cart
curl -sL "${base_url}/mjml/abandoned-cart/01-cart-reminder.mjml" -o data/raw/mailteorite/cart_reminder_01.mjml
curl -sL "${base_url}/mjml/abandoned-cart/02-cart-incentive.mjml" -o data/raw/mailteorite/cart_incentive.mjml
curl -sL "${base_url}/mjml/abandoned-cart/03-cart-final-chance.mjml" -o data/raw/mailteorite/cart_final_chance.mjml

# Reengagement
curl -sL "${base_url}/mjml/reengagement/01-reengagement-soft.mjml" -o data/raw/mailteorite/reengagement_soft.mjml
curl -sL "${base_url}/mjml/reengagement/02-winback-offer.mjml" -o data/raw/mailteorite/winback_offer.mjml
curl -sL "${base_url}/mjml/reengagement/03-final-goodbye.mjml" -o data/raw/mailteorite/final_goodbye.mjml

# Shipping Update
curl -sL "${base_url}/mjml/shipping-update/01-shipped-confirmation.mjml" -o data/raw/mailteorite/shipped_confirmation.mjml
curl -sL "${base_url}/mjml/shipping-update/02-out-for-delivery.mjml" -o data/raw/mailteorite/out_for_delivery.mjml
curl -sL "${base_url}/mjml/shipping-update/03-delivered.mjml" -o data/raw/mailteorite/delivered.mjml

# Upsell
curl -sL "${base_url}/mjml/upsell/01-upsell-premium.mjml" -o data/raw/mailteorite/upsell_premium.mjml
curl -sL "${base_url}/mjml/upsell/02-cross-sell-related.mjml" -o data/raw/mailteorite/cross_sell.mjml
curl -sL "${base_url}/mjml/upsell/03-post-purchase.mjml" -o data/raw/mailteorite/post_purchase.mjml

echo "Downloaded files:"
ls -la data/raw/mailteorite/

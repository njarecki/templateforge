"""
Template Generator

Generates complete email templates by composing sections and applying design skins.
"""

import json
from design_system import (
    MAX_WIDTH,
    DESIGN_SKINS,
    get_base_styles,
    get_outlook_conditionals,
)
from section_library import get_section, get_all_sections, list_section_types


# Template type definitions with their section compositions
TEMPLATE_TYPES = {
    "welcome": {
        "name": "Welcome Email",
        "category": "Welcome",
        "sections": ["header_nav", "hero", "1col_text", "3col_features", "cta_band", "footer_simple"],
        "description": "Standard welcome email with hero, features, and CTA"
    },
    "welcome_minimal": {
        "name": "Welcome Minimal",
        "category": "Welcome",
        "sections": ["header_nav", "hero", "1col_text", "footer_simple"],
        "description": "Minimal welcome email with essential content only"
    },
    "saas_onboarding": {
        "name": "SaaS Onboarding",
        "category": "SaaS",
        "sections": ["header_nav", "hero", "3col_features", "1col_text", "cta_band", "social_icons", "footer_simple"],
        "description": "SaaS onboarding with feature highlights"
    },
    "saas_feature_announcement": {
        "name": "Feature Announcement",
        "category": "SaaS",
        "sections": ["header_nav", "subhero", "2col_text_image", "1col_text", "cta_band", "footer_simple"],
        "description": "New feature announcement for SaaS products"
    },
    "ecommerce_promo": {
        "name": "E-commerce Promo",
        "category": "Ecommerce",
        "sections": ["offer_banner", "header_nav", "hero", "product_grid", "cta_band", "social_icons", "footer_complex"],
        "description": "Promotional email with product showcase"
    },
    "ecommerce_order_confirmation": {
        "name": "Order Confirmation",
        "category": "Ecommerce",
        "sections": ["header_nav", "1col_text", "order_summary", "1col_text", "footer_simple"],
        "description": "Order confirmation with summary details"
    },
    "newsletter": {
        "name": "Newsletter",
        "category": "Newsletter",
        "sections": ["header_nav", "hero", "story_block", "divider", "story_block", "cta_band", "social_icons", "footer_complex"],
        "description": "Newsletter with multiple story blocks"
    },
    "newsletter_digest": {
        "name": "Newsletter Digest",
        "category": "Newsletter",
        "sections": ["header_nav", "1col_text", "2col_text_image", "divider", "2col_text_image", "cta_band", "footer_simple"],
        "description": "Digest-style newsletter with mixed content"
    },
    "sale_announcement": {
        "name": "Sale Announcement",
        "category": "Promo",
        "sections": ["offer_banner", "header_nav", "hero", "product_grid", "product_grid", "cta_band", "footer_simple"],
        "description": "Sale announcement with product grid"
    },
    "flash_sale": {
        "name": "Flash Sale",
        "category": "Promo",
        "sections": ["offer_banner", "hero", "cta_band", "product_grid", "cta_band", "footer_simple"],
        "description": "Urgent flash sale with multiple CTAs"
    },
    # Transactional templates
    "password_reset": {
        "name": "Password Reset",
        "category": "Transactional",
        "sections": ["header_nav", "security_alert", "verification_code", "1col_text", "footer_simple"],
        "description": "Password reset request with verification code"
    },
    "account_verification": {
        "name": "Account Verification",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "verification_code", "1col_text", "footer_simple"],
        "description": "Email verification for new account signup"
    },
    "abandoned_cart": {
        "name": "Abandoned Cart",
        "category": "Ecommerce",
        "sections": ["header_nav", "1col_text", "cart_item", "cart_item", "urgency_banner", "cta_band", "footer_simple"],
        "description": "Cart abandonment recovery email"
    },
    "shipping_notification": {
        "name": "Shipping Notification",
        "category": "Ecommerce",
        "sections": ["header_nav", "1col_text", "shipping_tracker", "order_summary", "cta_band", "footer_simple"],
        "description": "Shipment tracking and delivery notification"
    },
    "event_invitation": {
        "name": "Event Invitation",
        "category": "SaaS",
        "sections": ["header_nav", "hero", "event_details", "1col_text", "rsvp_buttons", "footer_simple"],
        "description": "Event or webinar invitation with RSVP"
    },
    "review_request": {
        "name": "Review Request",
        "category": "Ecommerce",
        "sections": ["header_nav", "1col_text", "product_grid", "cta_band", "testimonial", "footer_simple"],
        "description": "Post-purchase review solicitation"
    },
    "product_launch": {
        "name": "Product Launch",
        "category": "Promo",
        "sections": ["header_nav", "hero", "countdown_timer", "3col_features", "cta_band", "footer_simple"],
        "description": "Product launch announcement with countdown timer"
    },
    "video_tutorial": {
        "name": "Video Tutorial",
        "category": "SaaS",
        "sections": ["header_nav", "1col_text", "video_placeholder", "accordion_faq", "cta_band", "footer_simple"],
        "description": "Tutorial or demo video with FAQ section"
    },
    "subscription_plans": {
        "name": "Subscription Plans",
        "category": "SaaS",
        "sections": ["header_nav", "hero", "pricing_table", "accordion_faq", "cta_band", "footer_simple"],
        "description": "SaaS pricing page email with tiered plans and FAQ"
    },
    "mobile_app_launch": {
        "name": "Mobile App Launch",
        "category": "Promo",
        "sections": ["header_nav", "hero", "3col_features", "app_store_badges", "testimonial", "cta_band", "footer_simple"],
        "description": "Mobile app launch announcement with download badges"
    },
    "onboarding_progress": {
        "name": "Onboarding Progress",
        "category": "SaaS",
        "sections": ["header_nav", "progress_tracker", "1col_text", "3col_features", "cta_band", "footer_simple"],
        "description": "Onboarding email showing user progress and next steps"
    },
    "company_update": {
        "name": "Company Update",
        "category": "Newsletter",
        "sections": ["header_nav", "hero", "stats_metrics", "1col_text", "team_members", "cta_band", "footer_complex"],
        "description": "Company update newsletter with stats and team highlights"
    },
    "product_comparison": {
        "name": "Product Comparison",
        "category": "Ecommerce",
        "sections": ["header_nav", "hero", "comparison_table", "testimonial", "cta_band", "footer_simple"],
        "description": "Product comparison email with feature table"
    },
    "annual_report": {
        "name": "Annual Report",
        "category": "Newsletter",
        "sections": ["header_nav", "hero", "stats_metrics", "story_block", "team_members", "cta_band", "social_icons", "footer_complex"],
        "description": "Year-in-review or annual report style email"
    },
    "product_review_request": {
        "name": "Product Review Request",
        "category": "Ecommerce",
        "sections": ["header_nav", "1col_text", "rating_stars", "cta_band", "testimonial", "footer_simple"],
        "description": "Post-purchase review request with star rating display"
    },
    "collection_showcase": {
        "name": "Collection Showcase",
        "category": "Ecommerce",
        "sections": ["header_nav", "hero", "gallery_carousel", "1col_text", "cta_band", "social_icons", "footer_simple"],
        "description": "Product collection showcase with gallery carousel"
    },
    "survey_invitation": {
        "name": "Survey Invitation",
        "category": "SaaS",
        "sections": ["header_nav", "1col_text", "multi_step_form", "1col_text", "footer_simple"],
        "description": "Survey or feedback form invitation email"
    },
    # New template types using recently added sections
    "referral_invite": {
        "name": "Referral Invite",
        "category": "Promo",
        "sections": ["header_nav", "hero", "referral_program", "testimonial", "cta_band", "footer_simple"],
        "description": "Referral program invitation with reward details and sharing options"
    },
    "gift_card_delivery": {
        "name": "Gift Card Delivery",
        "category": "Ecommerce",
        "sections": ["header_nav", "1col_text", "gift_card", "1col_text", "footer_simple"],
        "description": "Gift card delivery email with redemption code and message"
    },
    "subscription_reminder": {
        "name": "Subscription Reminder",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "subscription_renewal", "accordion_faq", "footer_simple"],
        "description": "Subscription renewal reminder with plan details and management options"
    },
    "loyalty_status": {
        "name": "Loyalty Status Update",
        "category": "Ecommerce",
        "sections": ["header_nav", "hero", "loyalty_points", "product_grid", "cta_band", "footer_simple"],
        "description": "Loyalty program status update with points balance and reward opportunities"
    },
    "subscription_canceled": {
        "name": "Subscription Canceled",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "subscription_renewal", "testimonial", "cta_band", "footer_simple"],
        "description": "Subscription cancellation confirmation with reactivation option"
    },
    "gift_card_purchase": {
        "name": "Gift Card Purchase Confirmation",
        "category": "Ecommerce",
        "sections": ["header_nav", "1col_text", "gift_card", "order_summary", "footer_simple"],
        "description": "Gift card purchase confirmation with delivery details"
    },
    # Specialized ecommerce notification templates
    "wishlist_reminder": {
        "name": "Wishlist Reminder",
        "category": "Ecommerce",
        "sections": ["header_nav", "1col_text", "wishlist_item", "wishlist_item", "cta_band", "footer_simple"],
        "description": "Reminder email about items saved in customer's wishlist"
    },
    "back_in_stock_alert": {
        "name": "Back In Stock Alert",
        "category": "Ecommerce",
        "sections": ["header_nav", "1col_text", "back_in_stock", "product_grid", "cta_band", "footer_simple"],
        "description": "Alert notification when a previously out-of-stock item becomes available"
    },
    "price_drop_alert": {
        "name": "Price Drop Alert",
        "category": "Ecommerce",
        "sections": ["header_nav", "1col_text", "price_alert", "urgency_banner", "cta_band", "footer_simple"],
        "description": "Alert notification when a tracked item's price drops"
    },
    # New transactional templates
    "invoice": {
        "name": "Invoice",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "invoice_details", "cta_band", "footer_simple"],
        "description": "Professional invoice with line items, billing details, and payment due date"
    },
    "receipt": {
        "name": "Receipt",
        "category": "Transactional",
        "sections": ["header_nav", "receipt_summary", "1col_text", "footer_simple"],
        "description": "Payment receipt confirming successful transaction with itemized breakdown"
    },
    "delivery_confirmed": {
        "name": "Delivery Confirmation",
        "category": "Ecommerce",
        "sections": ["header_nav", "delivery_confirmation", "cta_band", "social_icons", "footer_simple"],
        "description": "Delivery confirmation email with proof of delivery and order details"
    },
    # New specialized templates
    "appointment_reminder": {
        "name": "Appointment Reminder",
        "category": "Transactional",
        "sections": ["header_nav", "appointment_reminder", "1col_text", "footer_simple"],
        "description": "Appointment reminder with date, time, location, and calendar integration"
    },
    "two_factor_auth": {
        "name": "Two-Factor Authentication",
        "category": "Transactional",
        "sections": ["header_nav", "two_factor_code", "1col_text", "footer_simple"],
        "description": "Two-factor authentication code email for secure login verification"
    },
    "account_suspended": {
        "name": "Account Suspended",
        "category": "Transactional",
        "sections": ["header_nav", "account_suspended", "1col_text", "footer_simple"],
        "description": "Account suspension notification with reason and appeal options"
    },
    "payment_failed": {
        "name": "Payment Failed",
        "category": "Transactional",
        "sections": ["header_nav", "payment_failed", "accordion_faq", "footer_simple"],
        "description": "Payment failure notification with retry and update payment options"
    },
    # Additional specialized templates
    "order_hold": {
        "name": "Order Hold",
        "category": "Ecommerce",
        "sections": ["header_nav", "order_hold", "1col_text", "footer_simple"],
        "description": "Order hold notification with action required and deadline warning"
    },
    "subscription_paused": {
        "name": "Subscription Paused",
        "category": "Transactional",
        "sections": ["header_nav", "subscription_paused", "1col_text", "footer_simple"],
        "description": "Subscription pause confirmation with resume option and feature reminder"
    },
    "referral_success": {
        "name": "Referral Success",
        "category": "Promo",
        "sections": ["header_nav", "referral_success", "testimonial", "cta_band", "footer_simple"],
        "description": "Referral reward earned notification with stats and share options"
    },
    "wishlist_price_drop": {
        "name": "Wishlist Price Drop",
        "category": "Ecommerce",
        "sections": ["header_nav", "1col_text", "wishlist_item", "price_alert", "urgency_banner", "cta_band", "footer_simple"],
        "description": "Price drop notification for items in customer wishlist with urgency"
    },
    # Additional specialized templates
    "order_returned": {
        "name": "Order Returned",
        "category": "Ecommerce",
        "sections": ["header_nav", "order_returned", "1col_text", "cta_band", "footer_simple"],
        "description": "Return received confirmation with refund status and timeline"
    },
    "account_reactivated": {
        "name": "Account Reactivated",
        "category": "Transactional",
        "sections": ["header_nav", "account_reactivated", "3col_features", "cta_band", "footer_simple"],
        "description": "Welcome back email after account reactivation with what's new"
    },
    "loyalty_tier_upgrade": {
        "name": "Loyalty Tier Upgrade",
        "category": "Ecommerce",
        "sections": ["header_nav", "loyalty_tier_upgrade", "testimonial", "cta_band", "footer_simple"],
        "description": "Loyalty tier upgrade notification with new benefits and rewards"
    },
    "password_changed": {
        "name": "Password Changed",
        "category": "Transactional",
        "sections": ["header_nav", "password_changed", "1col_text", "footer_simple"],
        "description": "Password change confirmation with security notice and account protection"
    },
    # ========== WELCOME & ONBOARDING TEMPLATES ==========
    "welcome_premium": {
        "name": "Welcome Premium",
        "category": "Welcome",
        "sections": ["header_nav", "hero", "stats_metrics", "testimonial", "3col_features", "cta_band", "footer_complex"],
        "description": "Premium welcome email with stats and social proof"
    },
    "welcome_creator": {
        "name": "Welcome Creator",
        "category": "Welcome",
        "sections": ["header_nav", "hero", "1col_text", "video_placeholder", "cta_band", "social_icons", "footer_simple"],
        "description": "Creator/influencer welcome with video introduction"
    },
    "welcome_b2b": {
        "name": "Welcome B2B",
        "category": "Welcome",
        "sections": ["header_nav", "hero", "3col_features", "team_members", "cta_band", "footer_complex"],
        "description": "B2B welcome email with team introduction and enterprise features"
    },
    "welcome_trial": {
        "name": "Welcome Trial",
        "category": "Welcome",
        "sections": ["header_nav", "hero", "progress_tracker", "3col_features", "cta_band", "footer_simple"],
        "description": "Trial welcome with progress tracking and feature highlights"
    },
    "welcome_app": {
        "name": "Welcome App Download",
        "category": "Welcome",
        "sections": ["header_nav", "hero", "3col_features", "app_store_badges", "cta_band", "footer_simple"],
        "description": "Welcome email encouraging app download with app store links"
    },
    "onboarding_step1": {
        "name": "Onboarding Step 1",
        "category": "SaaS",
        "sections": ["header_nav", "progress_tracker", "1col_text", "video_placeholder", "cta_band", "footer_simple"],
        "description": "First onboarding step with tutorial video"
    },
    "onboarding_step2": {
        "name": "Onboarding Step 2",
        "category": "SaaS",
        "sections": ["header_nav", "progress_tracker", "2col_text_image", "3col_features", "cta_band", "footer_simple"],
        "description": "Second onboarding step with feature exploration"
    },
    "onboarding_step3": {
        "name": "Onboarding Step 3",
        "category": "SaaS",
        "sections": ["header_nav", "progress_tracker", "1col_text", "testimonial", "cta_band", "footer_simple"],
        "description": "Third onboarding step with success stories"
    },
    "onboarding_complete": {
        "name": "Onboarding Complete",
        "category": "SaaS",
        "sections": ["header_nav", "hero", "stats_metrics", "3col_features", "cta_band", "social_icons", "footer_complex"],
        "description": "Onboarding completion celebration with next steps"
    },
    # ========== SAAS TEMPLATES ==========
    "saas_upgrade_prompt": {
        "name": "SaaS Upgrade Prompt",
        "category": "SaaS",
        "sections": ["header_nav", "1col_text", "pricing_table", "comparison_table", "cta_band", "footer_simple"],
        "description": "Upgrade prompt with pricing comparison"
    },
    "saas_usage_report": {
        "name": "SaaS Usage Report",
        "category": "SaaS",
        "sections": ["header_nav", "hero", "stats_metrics", "progress_tracker", "cta_band", "footer_simple"],
        "description": "Monthly or weekly usage statistics report"
    },
    "saas_trial_ending": {
        "name": "Trial Ending",
        "category": "SaaS",
        "sections": ["header_nav", "urgency_banner", "1col_text", "pricing_table", "testimonial", "cta_band", "footer_simple"],
        "description": "Trial expiration warning with pricing options"
    },
    "saas_trial_expired": {
        "name": "Trial Expired",
        "category": "SaaS",
        "sections": ["header_nav", "1col_text", "pricing_table", "3col_features", "cta_band", "footer_simple"],
        "description": "Post-trial conversion email with plan options"
    },
    "saas_new_integration": {
        "name": "New Integration",
        "category": "SaaS",
        "sections": ["header_nav", "hero", "2col_text_image", "3col_features", "cta_band", "footer_simple"],
        "description": "New integration announcement with setup guide"
    },
    "saas_api_update": {
        "name": "API Update",
        "category": "SaaS",
        "sections": ["header_nav", "1col_text", "comparison_table", "accordion_faq", "cta_band", "footer_simple"],
        "description": "API version update with migration guide and FAQ"
    },
    "saas_downtime": {
        "name": "Scheduled Maintenance",
        "category": "SaaS",
        "sections": ["header_nav", "security_alert", "1col_text", "accordion_faq", "footer_simple"],
        "description": "Scheduled downtime notification with timeline"
    },
    "saas_incident_resolved": {
        "name": "Incident Resolved",
        "category": "SaaS",
        "sections": ["header_nav", "1col_text", "stats_metrics", "cta_band", "footer_simple"],
        "description": "Service incident resolution notification"
    },
    "saas_tips_tricks": {
        "name": "Tips & Tricks",
        "category": "SaaS",
        "sections": ["header_nav", "hero", "3col_features", "video_placeholder", "cta_band", "social_icons", "footer_simple"],
        "description": "Product tips and best practices email"
    },
    "saas_case_study": {
        "name": "Case Study",
        "category": "SaaS",
        "sections": ["header_nav", "hero", "stats_metrics", "testimonial", "1col_text", "cta_band", "footer_complex"],
        "description": "Customer case study with metrics and testimonial"
    },
    # ========== ECOMMERCE TEMPLATES ==========
    "ecommerce_new_arrivals": {
        "name": "New Arrivals",
        "category": "Ecommerce",
        "sections": ["header_nav", "hero", "product_grid", "product_grid", "cta_band", "social_icons", "footer_complex"],
        "description": "New product arrivals showcase"
    },
    "ecommerce_bestsellers": {
        "name": "Bestsellers",
        "category": "Ecommerce",
        "sections": ["header_nav", "hero", "product_grid", "testimonial", "cta_band", "footer_simple"],
        "description": "Bestselling products showcase with social proof"
    },
    "ecommerce_restock": {
        "name": "Restock Alert",
        "category": "Ecommerce",
        "sections": ["header_nav", "back_in_stock", "product_grid", "urgency_banner", "cta_band", "footer_simple"],
        "description": "Popular items restocked notification"
    },
    "ecommerce_vip_early_access": {
        "name": "VIP Early Access",
        "category": "Ecommerce",
        "sections": ["offer_banner", "header_nav", "hero", "countdown_timer", "product_grid", "cta_band", "footer_simple"],
        "description": "Exclusive VIP early access to sale or products"
    },
    "ecommerce_birthday": {
        "name": "Birthday Offer",
        "category": "Ecommerce",
        "sections": ["header_nav", "hero", "gift_card", "product_grid", "cta_band", "footer_simple"],
        "description": "Birthday greeting with special offer or gift"
    },
    "ecommerce_anniversary": {
        "name": "Customer Anniversary",
        "category": "Ecommerce",
        "sections": ["header_nav", "hero", "stats_metrics", "loyalty_points", "cta_band", "footer_simple"],
        "description": "Customer anniversary celebration with rewards"
    },
    "ecommerce_thank_you": {
        "name": "Thank You Post-Purchase",
        "category": "Ecommerce",
        "sections": ["header_nav", "1col_text", "order_summary", "product_grid", "social_icons", "footer_simple"],
        "description": "Post-purchase thank you with recommendations"
    },
    "ecommerce_category_sale": {
        "name": "Category Sale",
        "category": "Ecommerce",
        "sections": ["offer_banner", "header_nav", "hero", "product_grid", "product_grid", "cta_band", "footer_complex"],
        "description": "Category-specific sale with product highlights"
    },
    "ecommerce_seasonal": {
        "name": "Seasonal Collection",
        "category": "Ecommerce",
        "sections": ["header_nav", "hero", "gallery_carousel", "product_grid", "cta_band", "footer_simple"],
        "description": "Seasonal collection showcase"
    },
    "ecommerce_bundle_offer": {
        "name": "Bundle Offer",
        "category": "Ecommerce",
        "sections": ["header_nav", "hero", "product_grid", "comparison_table", "cta_band", "footer_simple"],
        "description": "Product bundle or kit offer with value comparison"
    },
    "ecommerce_pre_order": {
        "name": "Pre-Order Available",
        "category": "Ecommerce",
        "sections": ["header_nav", "hero", "countdown_timer", "3col_features", "cta_band", "footer_simple"],
        "description": "Pre-order announcement with countdown and features"
    },
    "ecommerce_exclusive_drop": {
        "name": "Exclusive Drop",
        "category": "Ecommerce",
        "sections": ["header_nav", "hero", "countdown_timer", "gallery_carousel", "urgency_banner", "cta_band", "footer_simple"],
        "description": "Limited edition exclusive product drop"
    },
    "ecommerce_clearance": {
        "name": "Clearance Sale",
        "category": "Ecommerce",
        "sections": ["offer_banner", "header_nav", "hero", "product_grid", "product_grid", "urgency_banner", "footer_simple"],
        "description": "Clearance sale with deep discounts"
    },
    "ecommerce_order_update": {
        "name": "Order Update",
        "category": "Ecommerce",
        "sections": ["header_nav", "1col_text", "shipping_tracker", "1col_text", "footer_simple"],
        "description": "General order status update notification"
    },
    "ecommerce_exchange_processed": {
        "name": "Exchange Processed",
        "category": "Ecommerce",
        "sections": ["header_nav", "1col_text", "order_summary", "shipping_tracker", "footer_simple"],
        "description": "Exchange order processed and shipping notification"
    },
    # ========== NEWSLETTER TEMPLATES ==========
    "newsletter_weekly": {
        "name": "Weekly Digest",
        "category": "Newsletter",
        "sections": ["header_nav", "hero", "story_block", "divider", "story_block", "divider", "story_block", "cta_band", "footer_complex"],
        "description": "Weekly digest with multiple stories"
    },
    "newsletter_monthly": {
        "name": "Monthly Roundup",
        "category": "Newsletter",
        "sections": ["header_nav", "hero", "stats_metrics", "story_block", "product_grid", "cta_band", "social_icons", "footer_complex"],
        "description": "Monthly roundup with stats and highlights"
    },
    "newsletter_curated": {
        "name": "Curated Links",
        "category": "Newsletter",
        "sections": ["header_nav", "1col_text", "story_block", "story_block", "story_block", "cta_band", "footer_simple"],
        "description": "Curated links and reading list style newsletter"
    },
    "newsletter_interview": {
        "name": "Interview Feature",
        "category": "Newsletter",
        "sections": ["header_nav", "hero", "team_members", "1col_text", "testimonial", "cta_band", "footer_complex"],
        "description": "Interview or Q&A feature newsletter"
    },
    "newsletter_industry_news": {
        "name": "Industry News",
        "category": "Newsletter",
        "sections": ["header_nav", "hero", "story_block", "2col_text_image", "stats_metrics", "cta_band", "footer_complex"],
        "description": "Industry news and market insights newsletter"
    },
    "newsletter_tips": {
        "name": "Tips Newsletter",
        "category": "Newsletter",
        "sections": ["header_nav", "subhero", "3col_features", "1col_text", "cta_band", "social_icons", "footer_simple"],
        "description": "Tips and how-to focused newsletter"
    },
    "newsletter_spotlight": {
        "name": "Community Spotlight",
        "category": "Newsletter",
        "sections": ["header_nav", "hero", "team_members", "testimonial", "story_block", "cta_band", "footer_complex"],
        "description": "Community member or customer spotlight"
    },
    "newsletter_product_update": {
        "name": "Product Update Newsletter",
        "category": "Newsletter",
        "sections": ["header_nav", "hero", "3col_features", "video_placeholder", "cta_band", "footer_simple"],
        "description": "Product updates and changelog newsletter"
    },
    # ========== PROMO TEMPLATES ==========
    "promo_holiday": {
        "name": "Holiday Promo",
        "category": "Promo",
        "sections": ["offer_banner", "header_nav", "hero", "countdown_timer", "product_grid", "gift_card", "cta_band", "footer_complex"],
        "description": "Holiday themed promotional email"
    },
    "promo_weekend": {
        "name": "Weekend Sale",
        "category": "Promo",
        "sections": ["offer_banner", "header_nav", "hero", "countdown_timer", "product_grid", "cta_band", "footer_simple"],
        "description": "Weekend-only sale promotion"
    },
    "promo_member_exclusive": {
        "name": "Member Exclusive",
        "category": "Promo",
        "sections": ["header_nav", "hero", "loyalty_points", "product_grid", "cta_band", "footer_simple"],
        "description": "Members-only exclusive offer"
    },
    "promo_last_chance": {
        "name": "Last Chance",
        "category": "Promo",
        "sections": ["urgency_banner", "header_nav", "hero", "countdown_timer", "product_grid", "cta_band", "footer_simple"],
        "description": "Last chance to buy promotional email"
    },
    "promo_partner": {
        "name": "Partner Offer",
        "category": "Promo",
        "sections": ["header_nav", "hero", "2col_text_image", "1col_text", "cta_band", "footer_complex"],
        "description": "Partner or collaboration promotional offer"
    },
    "promo_giveaway": {
        "name": "Giveaway",
        "category": "Promo",
        "sections": ["header_nav", "hero", "1col_text", "gallery_carousel", "rsvp_buttons", "social_icons", "footer_simple"],
        "description": "Contest or giveaway announcement"
    },
    "promo_reward": {
        "name": "Reward Earned",
        "category": "Promo",
        "sections": ["header_nav", "hero", "loyalty_points", "gift_card", "cta_band", "footer_simple"],
        "description": "Reward or cashback earned notification"
    },
    "promo_double_points": {
        "name": "Double Points",
        "category": "Promo",
        "sections": ["offer_banner", "header_nav", "hero", "loyalty_points", "product_grid", "cta_band", "footer_simple"],
        "description": "Double points promotion period"
    },
    # ========== TRANSACTIONAL TEMPLATES ==========
    "transactional_welcome_verify": {
        "name": "Welcome with Verification",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "verification_code", "3col_features", "footer_simple"],
        "description": "Welcome email with email verification requirement"
    },
    "transactional_login_alert": {
        "name": "New Login Alert",
        "category": "Transactional",
        "sections": ["header_nav", "security_alert", "1col_text", "cta_band", "footer_simple"],
        "description": "New device or location login notification"
    },
    "transactional_email_changed": {
        "name": "Email Changed",
        "category": "Transactional",
        "sections": ["header_nav", "security_alert", "1col_text", "footer_simple"],
        "description": "Email address change confirmation"
    },
    "transactional_profile_updated": {
        "name": "Profile Updated",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "cta_band", "footer_simple"],
        "description": "Account profile update confirmation"
    },
    "transactional_invite_accepted": {
        "name": "Invite Accepted",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "team_members", "cta_band", "footer_simple"],
        "description": "Team or workspace invite accepted notification"
    },
    "transactional_team_invite": {
        "name": "Team Invite",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "team_members", "cta_band", "footer_simple"],
        "description": "Invitation to join team or workspace"
    },
    "transactional_billing_updated": {
        "name": "Billing Updated",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "invoice_details", "footer_simple"],
        "description": "Billing information update confirmation"
    },
    "transactional_payment_method_expiring": {
        "name": "Payment Method Expiring",
        "category": "Transactional",
        "sections": ["header_nav", "urgency_banner", "1col_text", "cta_band", "footer_simple"],
        "description": "Payment method expiration warning"
    },
    "transactional_refund_processed": {
        "name": "Refund Processed",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "receipt_summary", "footer_simple"],
        "description": "Refund confirmation with transaction details"
    },
    "transactional_account_deleted": {
        "name": "Account Deleted",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "testimonial", "cta_band", "footer_simple"],
        "description": "Account deletion confirmation with reactivation option"
    },
    "transactional_data_export": {
        "name": "Data Export Ready",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "cta_band", "accordion_faq", "footer_simple"],
        "description": "Data export download ready notification"
    },
    # ========== NEW TEMPLATES - BATCH 2 (111 new templates to reach 2000+) ==========
    # ========== HEALTHCARE TEMPLATES ==========
    "healthcare_appointment_confirm": {
        "name": "Healthcare Appointment Confirmation",
        "category": "Transactional",
        "sections": ["header_nav", "appointment_reminder", "1col_text", "accordion_faq", "footer_simple"],
        "description": "Medical appointment confirmation with preparation instructions"
    },
    "healthcare_lab_results": {
        "name": "Lab Results Ready",
        "category": "Transactional",
        "sections": ["header_nav", "security_alert", "1col_text", "cta_band", "footer_simple"],
        "description": "Notification that lab results are available in patient portal"
    },
    "healthcare_prescription_ready": {
        "name": "Prescription Ready",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "order_summary", "cta_band", "footer_simple"],
        "description": "Pharmacy pickup notification for prescription"
    },
    "healthcare_wellness_tips": {
        "name": "Wellness Tips Newsletter",
        "category": "Newsletter",
        "sections": ["header_nav", "hero", "3col_features", "story_block", "cta_band", "footer_complex"],
        "description": "Health and wellness tips newsletter"
    },
    "healthcare_vaccination_reminder": {
        "name": "Vaccination Reminder",
        "category": "Transactional",
        "sections": ["header_nav", "urgency_banner", "1col_text", "appointment_reminder", "cta_band", "footer_simple"],
        "description": "Reminder to schedule vaccination appointment"
    },
    "healthcare_telehealth_invite": {
        "name": "Telehealth Appointment",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "video_placeholder", "appointment_reminder", "cta_band", "footer_simple"],
        "description": "Virtual appointment link and instructions"
    },
    # ========== REAL ESTATE TEMPLATES ==========
    "realestate_new_listing": {
        "name": "New Property Listing",
        "category": "Promo",
        "sections": ["header_nav", "hero", "gallery_carousel", "3col_features", "cta_band", "footer_complex"],
        "description": "New property listing announcement with photos"
    },
    "realestate_open_house": {
        "name": "Open House Invitation",
        "category": "Promo",
        "sections": ["header_nav", "hero", "event_details", "gallery_carousel", "rsvp_buttons", "footer_simple"],
        "description": "Open house event invitation with property details"
    },
    "realestate_price_reduction": {
        "name": "Price Reduction Alert",
        "category": "Promo",
        "sections": ["header_nav", "price_alert", "gallery_carousel", "urgency_banner", "cta_band", "footer_simple"],
        "description": "Property price reduction notification"
    },
    "realestate_market_report": {
        "name": "Market Report",
        "category": "Newsletter",
        "sections": ["header_nav", "hero", "stats_metrics", "story_block", "comparison_table", "cta_band", "footer_complex"],
        "description": "Local real estate market analysis report"
    },
    "realestate_saved_search": {
        "name": "Saved Search Results",
        "category": "Ecommerce",
        "sections": ["header_nav", "1col_text", "product_grid", "product_grid", "cta_band", "footer_simple"],
        "description": "New properties matching saved search criteria"
    },
    "realestate_offer_accepted": {
        "name": "Offer Accepted",
        "category": "Transactional",
        "sections": ["header_nav", "hero", "1col_text", "progress_tracker", "cta_band", "footer_simple"],
        "description": "Notification that property offer was accepted"
    },
    "realestate_closing_reminder": {
        "name": "Closing Reminder",
        "category": "Transactional",
        "sections": ["header_nav", "appointment_reminder", "accordion_faq", "1col_text", "footer_simple"],
        "description": "Real estate closing date reminder with checklist"
    },
    # ========== EDUCATION TEMPLATES ==========
    "education_course_enrollment": {
        "name": "Course Enrollment Confirmation",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "3col_features", "cta_band", "footer_simple"],
        "description": "Course enrollment confirmation with schedule"
    },
    "education_assignment_due": {
        "name": "Assignment Due Reminder",
        "category": "Transactional",
        "sections": ["header_nav", "urgency_banner", "1col_text", "countdown_timer", "cta_band", "footer_simple"],
        "description": "Upcoming assignment deadline reminder"
    },
    "education_grade_posted": {
        "name": "Grade Posted",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "stats_metrics", "cta_band", "footer_simple"],
        "description": "Notification that grades have been posted"
    },
    "education_course_complete": {
        "name": "Course Completion Certificate",
        "category": "Transactional",
        "sections": ["header_nav", "hero", "stats_metrics", "testimonial", "social_icons", "footer_complex"],
        "description": "Course completion congratulations with certificate"
    },
    "education_new_course": {
        "name": "New Course Available",
        "category": "Promo",
        "sections": ["header_nav", "hero", "video_placeholder", "3col_features", "pricing_table", "cta_band", "footer_simple"],
        "description": "New course announcement with preview"
    },
    "education_scholarship": {
        "name": "Scholarship Opportunity",
        "category": "Promo",
        "sections": ["header_nav", "hero", "1col_text", "accordion_faq", "cta_band", "footer_simple"],
        "description": "Scholarship application announcement"
    },
    "education_parent_update": {
        "name": "Parent Update",
        "category": "Newsletter",
        "sections": ["header_nav", "1col_text", "stats_metrics", "story_block", "cta_band", "footer_complex"],
        "description": "Student progress update for parents"
    },
    "education_alumni_newsletter": {
        "name": "Alumni Newsletter",
        "category": "Newsletter",
        "sections": ["header_nav", "hero", "team_members", "story_block", "stats_metrics", "cta_band", "social_icons", "footer_complex"],
        "description": "Alumni news and updates newsletter"
    },
    # ========== TRAVEL & HOSPITALITY TEMPLATES ==========
    "travel_booking_confirm": {
        "name": "Travel Booking Confirmation",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "order_summary", "appointment_reminder", "cta_band", "footer_simple"],
        "description": "Travel reservation confirmation with itinerary"
    },
    "travel_checkin_reminder": {
        "name": "Check-in Reminder",
        "category": "Transactional",
        "sections": ["header_nav", "urgency_banner", "1col_text", "cta_band", "footer_simple"],
        "description": "Flight or hotel check-in reminder"
    },
    "travel_trip_itinerary": {
        "name": "Trip Itinerary",
        "category": "Transactional",
        "sections": ["header_nav", "hero", "order_summary", "1col_text", "accordion_faq", "footer_complex"],
        "description": "Complete trip itinerary with all bookings"
    },
    "travel_destination_guide": {
        "name": "Destination Guide",
        "category": "Newsletter",
        "sections": ["header_nav", "hero", "gallery_carousel", "3col_features", "story_block", "cta_band", "footer_complex"],
        "description": "Travel destination guide with tips"
    },
    "travel_deal_alert": {
        "name": "Travel Deal Alert",
        "category": "Promo",
        "sections": ["offer_banner", "header_nav", "hero", "product_grid", "countdown_timer", "cta_band", "footer_simple"],
        "description": "Limited time travel deal notification"
    },
    "travel_loyalty_status": {
        "name": "Travel Loyalty Update",
        "category": "Ecommerce",
        "sections": ["header_nav", "hero", "loyalty_points", "progress_tracker", "cta_band", "footer_simple"],
        "description": "Travel rewards program status update"
    },
    "travel_review_request": {
        "name": "Trip Review Request",
        "category": "Ecommerce",
        "sections": ["header_nav", "1col_text", "rating_stars", "testimonial", "cta_band", "footer_simple"],
        "description": "Post-trip review request"
    },
    "travel_cancellation": {
        "name": "Booking Cancellation",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "receipt_summary", "cta_band", "footer_simple"],
        "description": "Travel booking cancellation confirmation"
    },
    # ========== FITNESS & WELLNESS TEMPLATES ==========
    "fitness_workout_summary": {
        "name": "Workout Summary",
        "category": "Newsletter",
        "sections": ["header_nav", "hero", "stats_metrics", "progress_tracker", "cta_band", "footer_simple"],
        "description": "Weekly workout summary with stats"
    },
    "fitness_class_reminder": {
        "name": "Fitness Class Reminder",
        "category": "Transactional",
        "sections": ["header_nav", "appointment_reminder", "1col_text", "cta_band", "footer_simple"],
        "description": "Upcoming fitness class reminder"
    },
    "fitness_membership_renewal": {
        "name": "Gym Membership Renewal",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "subscription_renewal", "pricing_table", "cta_band", "footer_simple"],
        "description": "Gym membership renewal notice"
    },
    "fitness_challenge_invite": {
        "name": "Fitness Challenge",
        "category": "Promo",
        "sections": ["header_nav", "hero", "countdown_timer", "3col_features", "rsvp_buttons", "footer_simple"],
        "description": "Fitness challenge invitation"
    },
    "fitness_goal_achieved": {
        "name": "Goal Achieved",
        "category": "Transactional",
        "sections": ["header_nav", "hero", "stats_metrics", "testimonial", "social_icons", "footer_simple"],
        "description": "Fitness goal achievement celebration"
    },
    "fitness_nutrition_tips": {
        "name": "Nutrition Tips",
        "category": "Newsletter",
        "sections": ["header_nav", "hero", "3col_features", "story_block", "cta_band", "footer_complex"],
        "description": "Weekly nutrition and diet tips"
    },
    # ========== FOOD & RESTAURANT TEMPLATES ==========
    "restaurant_reservation_confirm": {
        "name": "Reservation Confirmation",
        "category": "Transactional",
        "sections": ["header_nav", "appointment_reminder", "1col_text", "cta_band", "footer_simple"],
        "description": "Restaurant reservation confirmation"
    },
    "restaurant_order_confirm": {
        "name": "Food Order Confirmation",
        "category": "Ecommerce",
        "sections": ["header_nav", "1col_text", "order_summary", "shipping_tracker", "footer_simple"],
        "description": "Food delivery order confirmation"
    },
    "restaurant_menu_update": {
        "name": "New Menu Items",
        "category": "Promo",
        "sections": ["header_nav", "hero", "gallery_carousel", "product_grid", "cta_band", "footer_simple"],
        "description": "New menu items announcement"
    },
    "restaurant_loyalty_reward": {
        "name": "Restaurant Reward",
        "category": "Promo",
        "sections": ["header_nav", "hero", "loyalty_points", "gift_card", "cta_band", "footer_simple"],
        "description": "Restaurant loyalty reward notification"
    },
    "restaurant_weekly_special": {
        "name": "Weekly Special",
        "category": "Promo",
        "sections": ["offer_banner", "header_nav", "hero", "product_grid", "countdown_timer", "cta_band", "footer_simple"],
        "description": "Weekly special menu promotion"
    },
    "restaurant_catering_inquiry": {
        "name": "Catering Follow-up",
        "category": "SaaS",
        "sections": ["header_nav", "1col_text", "multi_step_form", "testimonial", "cta_band", "footer_complex"],
        "description": "Catering inquiry follow-up"
    },
    # ========== FINANCE & BANKING TEMPLATES ==========
    "finance_statement_ready": {
        "name": "Statement Ready",
        "category": "Transactional",
        "sections": ["header_nav", "security_alert", "1col_text", "cta_band", "footer_simple"],
        "description": "Monthly statement available notification"
    },
    "finance_payment_confirm": {
        "name": "Payment Confirmation",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "receipt_summary", "footer_simple"],
        "description": "Bill payment confirmation"
    },
    "finance_fraud_alert": {
        "name": "Fraud Alert",
        "category": "Transactional",
        "sections": ["header_nav", "security_alert", "1col_text", "cta_band", "footer_simple"],
        "description": "Suspicious activity fraud alert"
    },
    "finance_credit_score": {
        "name": "Credit Score Update",
        "category": "Newsletter",
        "sections": ["header_nav", "hero", "stats_metrics", "progress_tracker", "cta_band", "footer_simple"],
        "description": "Monthly credit score update"
    },
    "finance_investment_report": {
        "name": "Investment Report",
        "category": "Newsletter",
        "sections": ["header_nav", "hero", "stats_metrics", "comparison_table", "cta_band", "footer_complex"],
        "description": "Portfolio performance report"
    },
    "finance_loan_approved": {
        "name": "Loan Approved",
        "category": "Transactional",
        "sections": ["header_nav", "hero", "1col_text", "order_summary", "cta_band", "footer_simple"],
        "description": "Loan application approval notification"
    },
    "finance_tax_documents": {
        "name": "Tax Documents Ready",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "accordion_faq", "cta_band", "footer_simple"],
        "description": "Tax documents available for download"
    },
    "finance_savings_goal": {
        "name": "Savings Goal Update",
        "category": "Newsletter",
        "sections": ["header_nav", "1col_text", "progress_tracker", "stats_metrics", "cta_band", "footer_simple"],
        "description": "Savings goal progress update"
    },
    # ========== NONPROFIT & CHARITY TEMPLATES ==========
    "nonprofit_donation_thank": {
        "name": "Donation Thank You",
        "category": "Transactional",
        "sections": ["header_nav", "hero", "1col_text", "receipt_summary", "social_icons", "footer_complex"],
        "description": "Donation receipt and thank you"
    },
    "nonprofit_impact_report": {
        "name": "Impact Report",
        "category": "Newsletter",
        "sections": ["header_nav", "hero", "stats_metrics", "story_block", "testimonial", "cta_band", "footer_complex"],
        "description": "Donor impact report showing results"
    },
    "nonprofit_fundraising_campaign": {
        "name": "Fundraising Campaign",
        "category": "Promo",
        "sections": ["header_nav", "hero", "progress_tracker", "story_block", "cta_band", "social_icons", "footer_complex"],
        "description": "Fundraising campaign with progress"
    },
    "nonprofit_volunteer_invite": {
        "name": "Volunteer Opportunity",
        "category": "Promo",
        "sections": ["header_nav", "hero", "event_details", "3col_features", "rsvp_buttons", "footer_simple"],
        "description": "Volunteer opportunity invitation"
    },
    "nonprofit_event_ticket": {
        "name": "Charity Event Ticket",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "event_details", "1col_text", "social_icons", "footer_simple"],
        "description": "Charity event ticket confirmation"
    },
    "nonprofit_matching_gift": {
        "name": "Matching Gift",
        "category": "Promo",
        "sections": ["offer_banner", "header_nav", "hero", "countdown_timer", "cta_band", "footer_simple"],
        "description": "Matching gift campaign announcement"
    },
    "nonprofit_year_end_appeal": {
        "name": "Year-End Appeal",
        "category": "Promo",
        "sections": ["header_nav", "hero", "stats_metrics", "story_block", "countdown_timer", "cta_band", "footer_complex"],
        "description": "Year-end giving appeal"
    },
    # ========== EVENT & CONFERENCE TEMPLATES ==========
    "event_ticket_confirm": {
        "name": "Event Ticket Confirmation",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "event_details", "1col_text", "footer_simple"],
        "description": "Event ticket purchase confirmation"
    },
    "event_speaker_lineup": {
        "name": "Speaker Lineup",
        "category": "Promo",
        "sections": ["header_nav", "hero", "team_members", "3col_features", "cta_band", "footer_complex"],
        "description": "Conference speaker lineup announcement"
    },
    "event_agenda_release": {
        "name": "Event Agenda",
        "category": "Newsletter",
        "sections": ["header_nav", "hero", "accordion_faq", "1col_text", "cta_band", "footer_simple"],
        "description": "Event schedule and agenda release"
    },
    "event_countdown": {
        "name": "Event Countdown",
        "category": "Promo",
        "sections": ["header_nav", "hero", "countdown_timer", "3col_features", "cta_band", "social_icons", "footer_simple"],
        "description": "Event countdown reminder"
    },
    "event_session_reminder": {
        "name": "Session Reminder",
        "category": "Transactional",
        "sections": ["header_nav", "appointment_reminder", "1col_text", "cta_band", "footer_simple"],
        "description": "Upcoming session reminder"
    },
    "event_feedback_request": {
        "name": "Event Feedback",
        "category": "SaaS",
        "sections": ["header_nav", "1col_text", "rating_stars", "multi_step_form", "footer_simple"],
        "description": "Post-event feedback survey request"
    },
    "event_recording_available": {
        "name": "Event Recording",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "video_placeholder", "cta_band", "footer_simple"],
        "description": "Event recording now available"
    },
    "event_early_bird": {
        "name": "Early Bird Registration",
        "category": "Promo",
        "sections": ["offer_banner", "header_nav", "hero", "pricing_table", "countdown_timer", "cta_band", "footer_simple"],
        "description": "Early bird pricing announcement"
    },
    # ========== AUTOMOTIVE TEMPLATES ==========
    "auto_service_reminder": {
        "name": "Service Reminder",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "appointment_reminder", "cta_band", "footer_simple"],
        "description": "Vehicle service appointment reminder"
    },
    "auto_service_complete": {
        "name": "Service Complete",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "invoice_details", "cta_band", "footer_simple"],
        "description": "Vehicle service completion notification"
    },
    "auto_recall_notice": {
        "name": "Recall Notice",
        "category": "Transactional",
        "sections": ["header_nav", "security_alert", "1col_text", "cta_band", "footer_simple"],
        "description": "Vehicle recall safety notice"
    },
    "auto_new_model": {
        "name": "New Model Announcement",
        "category": "Promo",
        "sections": ["header_nav", "hero", "gallery_carousel", "3col_features", "comparison_table", "cta_band", "footer_complex"],
        "description": "New vehicle model announcement"
    },
    "auto_lease_ending": {
        "name": "Lease Ending",
        "category": "Transactional",
        "sections": ["header_nav", "urgency_banner", "1col_text", "comparison_table", "cta_band", "footer_simple"],
        "description": "Vehicle lease ending notification"
    },
    "auto_test_drive": {
        "name": "Test Drive Confirmation",
        "category": "Transactional",
        "sections": ["header_nav", "appointment_reminder", "1col_text", "gallery_carousel", "footer_simple"],
        "description": "Test drive appointment confirmation"
    },
    # ========== ENTERTAINMENT & MEDIA TEMPLATES ==========
    "media_new_release": {
        "name": "New Release",
        "category": "Promo",
        "sections": ["header_nav", "hero", "video_placeholder", "3col_features", "cta_band", "social_icons", "footer_simple"],
        "description": "New content release announcement"
    },
    "media_subscription_confirm": {
        "name": "Subscription Confirmation",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "3col_features", "cta_band", "app_store_badges", "footer_simple"],
        "description": "Media subscription confirmation"
    },
    "media_personalized_picks": {
        "name": "Personalized Picks",
        "category": "Newsletter",
        "sections": ["header_nav", "hero", "product_grid", "product_grid", "cta_band", "footer_simple"],
        "description": "Personalized content recommendations"
    },
    "media_watchlist_reminder": {
        "name": "Watchlist Reminder",
        "category": "Newsletter",
        "sections": ["header_nav", "1col_text", "product_grid", "cta_band", "footer_simple"],
        "description": "Reminder about saved content"
    },
    "media_season_premiere": {
        "name": "Season Premiere",
        "category": "Promo",
        "sections": ["header_nav", "hero", "countdown_timer", "video_placeholder", "cta_band", "social_icons", "footer_simple"],
        "description": "New season premiere announcement"
    },
    "media_creator_update": {
        "name": "Creator Update",
        "category": "Newsletter",
        "sections": ["header_nav", "hero", "team_members", "story_block", "cta_band", "social_icons", "footer_complex"],
        "description": "Creator/artist update newsletter"
    },
    # ========== GAMING TEMPLATES ==========
    "gaming_account_created": {
        "name": "Gaming Account Created",
        "category": "Welcome",
        "sections": ["header_nav", "hero", "3col_features", "app_store_badges", "cta_band", "social_icons", "footer_simple"],
        "description": "Gaming account welcome email"
    },
    "gaming_achievement": {
        "name": "Achievement Unlocked",
        "category": "Transactional",
        "sections": ["header_nav", "hero", "stats_metrics", "social_icons", "footer_simple"],
        "description": "Gaming achievement notification"
    },
    "gaming_friend_invite": {
        "name": "Friend Invite",
        "category": "Promo",
        "sections": ["header_nav", "hero", "referral_program", "cta_band", "footer_simple"],
        "description": "Invite friends to play together"
    },
    "gaming_tournament": {
        "name": "Tournament Invitation",
        "category": "Promo",
        "sections": ["header_nav", "hero", "event_details", "countdown_timer", "rsvp_buttons", "footer_simple"],
        "description": "Gaming tournament invitation"
    },
    "gaming_in_game_purchase": {
        "name": "In-Game Purchase",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "receipt_summary", "footer_simple"],
        "description": "In-game purchase confirmation"
    },
    "gaming_season_pass": {
        "name": "Season Pass",
        "category": "Promo",
        "sections": ["header_nav", "hero", "3col_features", "pricing_table", "cta_band", "footer_simple"],
        "description": "New season pass announcement"
    },
    # ========== PROFESSIONAL SERVICES TEMPLATES ==========
    "legal_document_ready": {
        "name": "Document Ready",
        "category": "Transactional",
        "sections": ["header_nav", "security_alert", "1col_text", "cta_band", "footer_simple"],
        "description": "Legal document ready for review"
    },
    "legal_case_update": {
        "name": "Case Status Update",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "progress_tracker", "cta_band", "footer_simple"],
        "description": "Legal case status update"
    },
    "consulting_proposal": {
        "name": "Proposal Sent",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "pricing_table", "accordion_faq", "cta_band", "footer_complex"],
        "description": "Consulting proposal delivery"
    },
    "consulting_project_kickoff": {
        "name": "Project Kickoff",
        "category": "Transactional",
        "sections": ["header_nav", "hero", "team_members", "progress_tracker", "cta_band", "footer_complex"],
        "description": "Project kickoff announcement"
    },
    "consulting_milestone": {
        "name": "Project Milestone",
        "category": "Newsletter",
        "sections": ["header_nav", "1col_text", "stats_metrics", "progress_tracker", "cta_band", "footer_simple"],
        "description": "Project milestone completion update"
    },
    # ========== INSURANCE TEMPLATES ==========
    "insurance_policy_confirm": {
        "name": "Policy Confirmation",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "order_summary", "accordion_faq", "footer_complex"],
        "description": "Insurance policy purchase confirmation"
    },
    "insurance_renewal_reminder": {
        "name": "Renewal Reminder",
        "category": "Transactional",
        "sections": ["header_nav", "urgency_banner", "1col_text", "subscription_renewal", "cta_band", "footer_simple"],
        "description": "Insurance policy renewal reminder"
    },
    "insurance_claim_received": {
        "name": "Claim Received",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "progress_tracker", "accordion_faq", "footer_simple"],
        "description": "Insurance claim receipt confirmation"
    },
    "insurance_claim_update": {
        "name": "Claim Update",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "progress_tracker", "1col_text", "footer_simple"],
        "description": "Insurance claim status update"
    },
    "insurance_quote_ready": {
        "name": "Quote Ready",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "pricing_table", "comparison_table", "cta_band", "footer_simple"],
        "description": "Insurance quote comparison"
    },
    # ========== SUBSCRIPTION BOX TEMPLATES ==========
    "subscription_box_shipped": {
        "name": "Box Shipped",
        "category": "Ecommerce",
        "sections": ["header_nav", "1col_text", "shipping_tracker", "gallery_carousel", "cta_band", "footer_simple"],
        "description": "Subscription box shipment notification"
    },
    "subscription_box_reveal": {
        "name": "Box Reveal",
        "category": "Ecommerce",
        "sections": ["header_nav", "hero", "gallery_carousel", "product_grid", "social_icons", "footer_simple"],
        "description": "Monthly box contents reveal"
    },
    "subscription_box_customize": {
        "name": "Customize Your Box",
        "category": "Ecommerce",
        "sections": ["header_nav", "1col_text", "countdown_timer", "product_grid", "cta_band", "footer_simple"],
        "description": "Box customization reminder"
    },
    "subscription_box_review": {
        "name": "Rate Your Box",
        "category": "Ecommerce",
        "sections": ["header_nav", "1col_text", "rating_stars", "product_grid", "cta_band", "footer_simple"],
        "description": "Subscription box review request"
    },
    "subscription_box_gift": {
        "name": "Gift a Subscription",
        "category": "Promo",
        "sections": ["header_nav", "hero", "gift_card", "pricing_table", "cta_band", "footer_simple"],
        "description": "Gift subscription promotion"
    },
    # ========== PET INDUSTRY TEMPLATES ==========
    "pet_order_confirm": {
        "name": "Pet Supply Order",
        "category": "Ecommerce",
        "sections": ["header_nav", "1col_text", "order_summary", "product_grid", "footer_simple"],
        "description": "Pet supply order confirmation"
    },
    "pet_vet_reminder": {
        "name": "Vet Appointment Reminder",
        "category": "Transactional",
        "sections": ["header_nav", "appointment_reminder", "1col_text", "cta_band", "footer_simple"],
        "description": "Veterinary appointment reminder"
    },
    "pet_prescription_refill": {
        "name": "Prescription Refill",
        "category": "Transactional",
        "sections": ["header_nav", "urgency_banner", "1col_text", "order_summary", "cta_band", "footer_simple"],
        "description": "Pet medication refill reminder"
    },
    "pet_birthday": {
        "name": "Pet Birthday",
        "category": "Promo",
        "sections": ["header_nav", "hero", "gift_card", "product_grid", "cta_band", "footer_simple"],
        "description": "Pet birthday special offer"
    },
    "pet_adoption_update": {
        "name": "Adoption Update",
        "category": "Newsletter",
        "sections": ["header_nav", "hero", "gallery_carousel", "story_block", "cta_band", "social_icons", "footer_complex"],
        "description": "Pet adoption center update"
    },
    # ========== HOME SERVICES TEMPLATES ==========
    "home_service_scheduled": {
        "name": "Service Scheduled",
        "category": "Transactional",
        "sections": ["header_nav", "appointment_reminder", "1col_text", "team_members", "footer_simple"],
        "description": "Home service appointment scheduled"
    },
    "home_service_complete": {
        "name": "Service Complete",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "invoice_details", "rating_stars", "footer_simple"],
        "description": "Home service completion with invoice"
    },
    "home_maintenance_reminder": {
        "name": "Maintenance Reminder",
        "category": "Newsletter",
        "sections": ["header_nav", "1col_text", "3col_features", "cta_band", "footer_simple"],
        "description": "Seasonal home maintenance tips"
    },
    "home_quote_ready": {
        "name": "Quote Ready",
        "category": "Transactional",
        "sections": ["header_nav", "1col_text", "pricing_table", "cta_band", "accordion_faq", "footer_simple"],
        "description": "Home service quote delivery"
    },
    "home_referral_reward": {
        "name": "Referral Reward",
        "category": "Promo",
        "sections": ["header_nav", "hero", "referral_success", "gift_card", "cta_band", "footer_simple"],
        "description": "Home service referral reward earned"
    },
    # ========== BEAUTY & COSMETICS TEMPLATES ==========
    "beauty_new_collection": {
        "name": "New Beauty Collection",
        "category": "Ecommerce",
        "sections": ["header_nav", "hero", "gallery_carousel", "product_grid", "cta_band", "social_icons", "footer_complex"],
        "description": "New beauty collection launch"
    },
    "beauty_routine_tips": {
        "name": "Beauty Routine Tips",
        "category": "Newsletter",
        "sections": ["header_nav", "hero", "video_placeholder", "3col_features", "product_grid", "cta_band", "footer_simple"],
        "description": "Skincare and beauty routine tips"
    },
    "beauty_replenishment": {
        "name": "Product Replenishment",
        "category": "Ecommerce",
        "sections": ["header_nav", "1col_text", "product_grid", "urgency_banner", "cta_band", "footer_simple"],
        "description": "Beauty product replenishment reminder"
    },
    "beauty_quiz_results": {
        "name": "Quiz Results",
        "category": "SaaS",
        "sections": ["header_nav", "hero", "3col_features", "product_grid", "cta_band", "footer_simple"],
        "description": "Personalized beauty quiz results"
    },
    "beauty_sample_offer": {
        "name": "Free Sample Offer",
        "category": "Promo",
        "sections": ["offer_banner", "header_nav", "hero", "product_grid", "cta_band", "footer_simple"],
        "description": "Free beauty sample promotion"
    },
}


def generate_html_wrapper(content, skin_name="apple_light"):
    """Wraps section content in a complete HTML email document."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    # Build inline styles with skin values
    styles = get_base_styles()
    for token, value in skin.items():
        styles = styles.replace(f"{{{token}}}", str(value))

    outlook = get_outlook_conditionals()

    return f'''<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="x-apple-disable-message-reformatting">
    <meta name="format-detection" content="telephone=no,address=no,email=no,date=no,url=no">
    <title>{{{{emailSubject}}}}</title>
    {outlook}
    {styles}
</head>
<body style="margin: 0; padding: 0; background-color: {skin['brandBG']};">
    <!-- Hidden preheader text -->
    <div style="display: none; max-height: 0; overflow: hidden;">
        {{{{preheader}}}}
        &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
    </div>

    <!-- Email wrapper -->
    <table role="presentation" class="wrapper" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: {skin['brandBG']};">
        <tr>
            <td align="center" style="padding: 24px 16px;">
                <!-- Main container -->
                <table role="presentation" class="main" width="{MAX_WIDTH}" cellpadding="0" cellspacing="0" border="0" style="max-width: {MAX_WIDTH}px; width: 100%; background-color: {skin['brandBG']};">
{content}
                </table>
            </td>
        </tr>
    </table>
</body>
</html>'''


def apply_skin_to_section(section_html, skin_name):
    """Apply a design skin's values to section HTML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])
    result = section_html

    # Replace all token placeholders with skin values
    for token, value in skin.items():
        result = result.replace(f"{{{{brandBG}}}}", skin["brandBG"])
        result = result.replace(f"{{{{brandPrimary}}}}", skin["brandPrimary"])
        result = result.replace(f"{{{{brandSecondary}}}}", skin["brandSecondary"])
        result = result.replace(f"{{{{brandText}}}}", skin["brandText"])
        result = result.replace(f"{{{{brandAccent}}}}", skin["brandAccent"])
        result = result.replace(f"{{{{brandFont}}}}", skin["brandFont"])

    # Also handle the single-brace format used in styles
    result = result.replace("{brandBG}", skin["brandBG"])
    result = result.replace("{brandPrimary}", skin["brandPrimary"])
    result = result.replace("{brandSecondary}", skin["brandSecondary"])
    result = result.replace("{brandText}", skin["brandText"])
    result = result.replace("{brandAccent}", skin["brandAccent"])
    result = result.replace("{brandFont}", skin["brandFont"])

    return result


def generate_template(template_type, skin_name="apple_light"):
    """Generate a complete template from a template type and skin."""
    if template_type not in TEMPLATE_TYPES:
        raise ValueError(f"Unknown template type: {template_type}")

    template_def = TEMPLATE_TYPES[template_type]
    sections_html = []

    for section_type in template_def["sections"]:
        section = get_section(section_type)
        if section:
            skinned_html = apply_skin_to_section(section["html"], skin_name)
            sections_html.append(f"                    <tr><td>{skinned_html}</td></tr>")

    content = "\n".join(sections_html)
    full_html = generate_html_wrapper(content, skin_name)

    return {
        "type": template_type,
        "name": template_def["name"],
        "category": template_def["category"],
        "description": template_def["description"],
        "skin": skin_name,
        "skin_name": DESIGN_SKINS[skin_name]["name"],
        "sections_used": template_def["sections"],
        "html": full_html,
    }


def generate_all_skins_for_template(template_type):
    """Generate a template in all 5 design skins."""
    results = []
    for skin_name in DESIGN_SKINS.keys():
        template = generate_template(template_type, skin_name)
        results.append(template)
    return results


def generate_layout_variant(template_type, variant_num, skin_name="apple_light"):
    """Generate a layout variant by rearranging or modifying sections."""
    if template_type not in TEMPLATE_TYPES:
        raise ValueError(f"Unknown template type: {template_type}")

    original_sections = TEMPLATE_TYPES[template_type]["sections"].copy()
    template_def = TEMPLATE_TYPES[template_type]

    if variant_num == 1:
        # Variant 1: Add a testimonial before CTA
        new_sections = []
        for section in original_sections:
            if section == "cta_band":
                new_sections.append("testimonial")
            new_sections.append(section)
        variant_sections = new_sections
        variant_desc = "Added testimonial before CTA"

    elif variant_num == 2:
        # Variant 2: Swap 2-column layout positions, add dividers
        new_sections = []
        for i, section in enumerate(original_sections):
            new_sections.append(section)
            if section in ["hero", "story_block", "product_grid"] and i < len(original_sections) - 2:
                new_sections.append("spacer")
        variant_sections = new_sections
        variant_desc = "Added spacing between major sections"

    else:
        # Variant 3: Minimal version - remove optional sections
        keep_sections = ["header_nav", "hero", "1col_text", "cta_band", "footer_simple"]
        variant_sections = [s for s in original_sections if s in keep_sections]
        if not variant_sections:
            variant_sections = ["header_nav", "hero", "cta_band", "footer_simple"]
        variant_desc = "Minimal streamlined version"

    # Generate the variant template
    sections_html = []
    for section_type in variant_sections:
        section = get_section(section_type)
        if section:
            skinned_html = apply_skin_to_section(section["html"], skin_name)
            sections_html.append(f"                    <tr><td>{skinned_html}</td></tr>")

    content = "\n".join(sections_html)
    full_html = generate_html_wrapper(content, skin_name)

    return {
        "type": f"{template_type}_variant_{variant_num}",
        "base_type": template_type,
        "name": f"{template_def['name']} - Variant {variant_num}",
        "category": template_def["category"],
        "description": variant_desc,
        "skin": skin_name,
        "skin_name": DESIGN_SKINS[skin_name]["name"],
        "sections_used": variant_sections,
        "html": full_html,
    }


def generate_full_batch():
    """Generate a complete batch of templates with all skins and variants."""
    result = {
        "metadata": {
            "version": "1.0",
            "total_templates": 0,
            "design_skins": list(DESIGN_SKINS.keys()),
            "template_types": list(TEMPLATE_TYPES.keys()),
        },
        "sectionLibraryExtracted": [],
        "normalizedTemplates": [],
        "reskinnedTemplates": [],
        "layoutVariants": [],
        "sourceTemplatesUsed": [],
    }

    # Extract section library
    all_sections = get_all_sections()
    for section_type, section_data in all_sections.items():
        result["sectionLibraryExtracted"].append({
            "type": section_data["type"],
            "name": section_data["name"],
            "html": section_data["html"],
        })

    # Generate normalized templates (using apple_light as base)
    for template_type in TEMPLATE_TYPES.keys():
        template = generate_template(template_type, "apple_light")
        result["normalizedTemplates"].append(template)
        result["sourceTemplatesUsed"].append({
            "type": template_type,
            "name": TEMPLATE_TYPES[template_type]["name"],
            "source": "Generated based on modern email best practices",
            "category": TEMPLATE_TYPES[template_type]["category"],
        })

    # Generate reskinned versions (all 5 skins for each template)
    for template_type in TEMPLATE_TYPES.keys():
        skinned_templates = generate_all_skins_for_template(template_type)
        result["reskinnedTemplates"].extend(skinned_templates)

    # Generate layout variants (3 variants per template, in default skin)
    for template_type in TEMPLATE_TYPES.keys():
        for variant_num in [1, 2, 3]:
            variant = generate_layout_variant(template_type, variant_num, "apple_light")
            result["layoutVariants"].append(variant)

    # Update totals
    result["metadata"]["total_templates"] = (
        len(result["normalizedTemplates"]) +
        len(result["reskinnedTemplates"]) +
        len(result["layoutVariants"])
    )
    result["metadata"]["section_count"] = len(result["sectionLibraryExtracted"])

    return result


def register_derived_templates(derived_types: dict):
    """
    Register derived template types from external sources.

    Args:
        derived_types: Dictionary of template type definitions from template_derivation
    """
    TEMPLATE_TYPES.update(derived_types)


def get_all_template_types():
    """Get all template types including any registered derived types."""
    return TEMPLATE_TYPES


def list_template_types():
    """List all available template types."""
    return [
        {"type": t, "name": d["name"], "category": d["category"], "description": d["description"]}
        for t, d in TEMPLATE_TYPES.items()
    ]


if __name__ == "__main__":
    # Generate and output a sample template
    import sys

    if len(sys.argv) > 1:
        template_type = sys.argv[1]
        skin = sys.argv[2] if len(sys.argv) > 2 else "apple_light"
        template = generate_template(template_type, skin)
        print(json.dumps(template, indent=2))
    else:
        print("Available template types:")
        for t in list_template_types():
            print(f"  - {t['type']}: {t['name']} ({t['category']})")
        print("\nAvailable skins:", list(DESIGN_SKINS.keys()))
        print("\nUsage: python template_generator.py <template_type> [skin]")

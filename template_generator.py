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

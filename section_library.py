"""
Section Library

Contains all modular section components for email templates.
Each section is a reusable building block following TopMail design system.
"""

from design_system import IMAGE_PLACEHOLDERS, COPY_TOKENS


def section_hero():
    """Full-width hero section with image, headline, and CTA."""
    return {
        "type": "hero",
        "name": "Hero Section",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td align="center" style="padding: 0;">
            <img src="{IMAGE_PLACEHOLDERS['hero']}" alt="{{{{heroAlt}}}}" width="640" style="width: 100%; max-width: 640px; height: auto; display: block;" />
        </td>
    </tr>
    <tr>
        <td align="center" style="padding: 24px 24px 16px;">
            <h1 class="headline" style="font-family: {{brandFont}}; font-size: 32px; color: {{brandPrimary}}; margin: 0;">{COPY_TOKENS['headline']}</h1>
        </td>
    </tr>
    <tr>
        <td align="center" style="padding: 0 24px 24px;">
            <p class="subheadline" style="font-family: {{brandFont}}; font-size: 18px; color: {{brandSecondary}}; margin: 0;">{COPY_TOKENS['subheadline']}</p>
        </td>
    </tr>
    <tr>
        <td align="center" style="padding: 0 24px 32px;">
            <a href="{{{{ctaUrl}}}}" class="cta-button" style="display: inline-block; padding: 16px 32px; background-color: {{brandAccent}}; color: #ffffff; font-family: {{brandFont}}; font-size: 16px; font-weight: 600; text-decoration: none; border-radius: 8px;">{COPY_TOKENS['ctaLabel']}</a>
        </td>
    </tr>
</table>
'''
    }


def section_subhero():
    """Secondary hero with smaller image and text."""
    return {
        "type": "subhero",
        "name": "Sub-Hero Section",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td align="center" style="padding: 24px;">
            <img src="{IMAGE_PLACEHOLDERS['product']}" alt="{{{{imageAlt}}}}" width="300" style="max-width: 300px; height: auto; display: block;" />
        </td>
    </tr>
    <tr>
        <td align="center" style="padding: 0 24px 16px;">
            <h2 style="font-family: {{brandFont}}; font-size: 24px; color: {{brandPrimary}}; margin: 0;">{COPY_TOKENS['headline']}</h2>
        </td>
    </tr>
    <tr>
        <td align="center" style="padding: 0 24px 24px;">
            <p style="font-family: {{brandFont}}; font-size: 16px; color: {{brandText}}; margin: 0; line-height: 1.6;">{COPY_TOKENS['bodyText']}</p>
        </td>
    </tr>
</table>
'''
    }


def section_1col_text():
    """Single column text block."""
    return {
        "type": "1col_text",
        "name": "Single Column Text",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <h2 style="font-family: {{brandFont}}; font-size: 24px; color: {{brandPrimary}}; margin: 0 0 12px;">{COPY_TOKENS['headline']}</h2>
            <p style="font-family: {{brandFont}}; font-size: 16px; color: {{brandText}}; margin: 0; line-height: 1.6;">{COPY_TOKENS['bodyText']}</p>
        </td>
    </tr>
</table>
'''
    }


def section_2col_text_image():
    """Two-column layout with text and image."""
    return {
        "type": "2col_text_image",
        "name": "Two Column Text & Image",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <!--[if mso]>
            <table role="presentation" width="100%"><tr><td width="50%" valign="top">
            <![endif]-->
            <div style="display: inline-block; width: 100%; max-width: 296px; vertical-align: top;">
                <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                    <tr>
                        <td style="padding-right: 12px;">
                            <h3 style="font-family: {{brandFont}}; font-size: 20px; color: {{brandPrimary}}; margin: 0 0 12px;">{COPY_TOKENS['headline']}</h3>
                            <p style="font-family: {{brandFont}}; font-size: 14px; color: {{brandText}}; margin: 0; line-height: 1.5;">{COPY_TOKENS['bodyText']}</p>
                        </td>
                    </tr>
                </table>
            </div>
            <!--[if mso]>
            </td><td width="50%" valign="top">
            <![endif]-->
            <div style="display: inline-block; width: 100%; max-width: 296px; vertical-align: top;">
                <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                    <tr>
                        <td style="padding-left: 12px;">
                            <img src="{IMAGE_PLACEHOLDERS['product']}" alt="{{{{imageAlt}}}}" width="284" style="width: 100%; max-width: 284px; height: auto; display: block;" />
                        </td>
                    </tr>
                </table>
            </div>
            <!--[if mso]>
            </td></tr></table>
            <![endif]-->
        </td>
    </tr>
</table>
'''
    }


def section_3col_features():
    """Three-column feature grid with icons."""
    return {
        "type": "3col_features",
        "name": "Three Column Features",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                <tr>
                    <!--[if mso]>
                    <td width="33%" valign="top">
                    <![endif]-->
                    <!--[if !mso]><!-->
                    <td style="display: inline-block; width: 100%; max-width: 192px; vertical-align: top; padding: 8px;" class="mobile-full">
                    <!--<![endif]-->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr><td align="center" style="padding-bottom: 12px;"><img src="{IMAGE_PLACEHOLDERS['icon']}" alt="" width="64" height="64" style="display: block;" /></td></tr>
                            <tr><td align="center"><h4 style="font-family: {{brandFont}}; font-size: 16px; color: {{brandPrimary}}; margin: 0 0 8px;">{{{{feature1Title}}}}</h4></td></tr>
                            <tr><td align="center"><p style="font-family: {{brandFont}}; font-size: 14px; color: {{brandSecondary}}; margin: 0;">{{{{feature1Text}}}}</p></td></tr>
                        </table>
                    </td>
                    <!--[if mso]>
                    </td><td width="33%" valign="top">
                    <![endif]-->
                    <!--[if !mso]><!-->
                    <td style="display: inline-block; width: 100%; max-width: 192px; vertical-align: top; padding: 8px;" class="mobile-full">
                    <!--<![endif]-->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr><td align="center" style="padding-bottom: 12px;"><img src="{IMAGE_PLACEHOLDERS['icon']}" alt="" width="64" height="64" style="display: block;" /></td></tr>
                            <tr><td align="center"><h4 style="font-family: {{brandFont}}; font-size: 16px; color: {{brandPrimary}}; margin: 0 0 8px;">{{{{feature2Title}}}}</h4></td></tr>
                            <tr><td align="center"><p style="font-family: {{brandFont}}; font-size: 14px; color: {{brandSecondary}}; margin: 0;">{{{{feature2Text}}}}</p></td></tr>
                        </table>
                    </td>
                    <!--[if mso]>
                    </td><td width="33%" valign="top">
                    <![endif]-->
                    <!--[if !mso]><!-->
                    <td style="display: inline-block; width: 100%; max-width: 192px; vertical-align: top; padding: 8px;" class="mobile-full">
                    <!--<![endif]-->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr><td align="center" style="padding-bottom: 12px;"><img src="{IMAGE_PLACEHOLDERS['icon']}" alt="" width="64" height="64" style="display: block;" /></td></tr>
                            <tr><td align="center"><h4 style="font-family: {{brandFont}}; font-size: 16px; color: {{brandPrimary}}; margin: 0 0 8px;">{{{{feature3Title}}}}</h4></td></tr>
                            <tr><td align="center"><p style="font-family: {{brandFont}}; font-size: 14px; color: {{brandSecondary}}; margin: 0;">{{{{feature3Text}}}}</p></td></tr>
                        </table>
                    </td>
                    <!--[if mso]>
                    </td>
                    <![endif]-->
                </tr>
            </table>
        </td>
    </tr>
</table>
'''
    }


def section_product_grid():
    """Product grid with 2 products per row."""
    return {
        "type": "product_grid",
        "name": "Product Grid",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                <tr>
                    <td width="50%" valign="top" style="padding: 8px;" class="mobile-full">
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr><td align="center"><img src="{IMAGE_PLACEHOLDERS['product']}" alt="{{{{product1Alt}}}}" width="280" style="width: 100%; max-width: 280px; height: auto; display: block;" /></td></tr>
                            <tr><td align="center" style="padding-top: 12px;"><h4 style="font-family: {{brandFont}}; font-size: 16px; color: {{brandPrimary}}; margin: 0;">{{{{product1Name}}}}</h4></td></tr>
                            <tr><td align="center" style="padding-top: 4px;"><p style="font-family: {{brandFont}}; font-size: 14px; color: {{brandAccent}}; margin: 0; font-weight: 600;">{{{{product1Price}}}}</p></td></tr>
                        </table>
                    </td>
                    <td width="50%" valign="top" style="padding: 8px;" class="mobile-full">
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr><td align="center"><img src="{IMAGE_PLACEHOLDERS['product']}" alt="{{{{product2Alt}}}}" width="280" style="width: 100%; max-width: 280px; height: auto; display: block;" /></td></tr>
                            <tr><td align="center" style="padding-top: 12px;"><h4 style="font-family: {{brandFont}}; font-size: 16px; color: {{brandPrimary}}; margin: 0;">{{{{product2Name}}}}</h4></td></tr>
                            <tr><td align="center" style="padding-top: 4px;"><p style="font-family: {{brandFont}}; font-size: 14px; color: {{brandAccent}}; margin: 0; font-weight: 600;">{{{{product2Price}}}}</p></td></tr>
                        </table>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
'''
    }


def section_testimonial():
    """Testimonial quote block."""
    return {
        "type": "testimonial",
        "name": "Testimonial",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 32px 24px; background-color: {{brandSecondary}}20;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                <tr>
                    <td align="center">
                        <img src="{IMAGE_PLACEHOLDERS['avatar']}" alt="" width="80" height="80" style="border-radius: 50%; display: block;" />
                    </td>
                </tr>
                <tr>
                    <td align="center" style="padding-top: 16px;">
                        <p style="font-family: {{brandFont}}; font-size: 18px; font-style: italic; color: {{brandText}}; margin: 0; line-height: 1.6;">&ldquo;{COPY_TOKENS['testimonialQuote']}&rdquo;</p>
                    </td>
                </tr>
                <tr>
                    <td align="center" style="padding-top: 12px;">
                        <p style="font-family: {{brandFont}}; font-size: 14px; color: {{brandSecondary}}; margin: 0; font-weight: 600;">{COPY_TOKENS['testimonialAuthor']}</p>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
'''
    }


def section_story_block():
    """Narrative content block with image."""
    return {
        "type": "story_block",
        "name": "Story Block",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <img src="{IMAGE_PLACEHOLDERS['hero']}" alt="{{{{storyImageAlt}}}}" width="592" style="width: 100%; max-width: 592px; height: auto; display: block; margin-bottom: 16px;" />
            <h2 style="font-family: {{brandFont}}; font-size: 24px; color: {{brandPrimary}}; margin: 0 0 12px;">{COPY_TOKENS['headline']}</h2>
            <p style="font-family: {{brandFont}}; font-size: 16px; color: {{brandText}}; margin: 0 0 16px; line-height: 1.6;">{COPY_TOKENS['bodyText']}</p>
            <a href="{{{{readMoreUrl}}}}" style="font-family: {{brandFont}}; font-size: 14px; color: {{brandAccent}}; text-decoration: underline;">Read more &rarr;</a>
        </td>
    </tr>
</table>
'''
    }


def section_cta_band():
    """Full-width CTA banner."""
    return {
        "type": "cta_band",
        "name": "CTA Band",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td align="center" style="padding: 32px 24px; background-color: {{brandAccent}};">
            <h2 style="font-family: {{brandFont}}; font-size: 24px; color: #ffffff; margin: 0 0 16px;">{COPY_TOKENS['headline']}</h2>
            <a href="{{{{ctaUrl}}}}" style="display: inline-block; padding: 14px 28px; background-color: #ffffff; color: {{brandAccent}}; font-family: {{brandFont}}; font-size: 16px; font-weight: 600; text-decoration: none; border-radius: 8px;">{COPY_TOKENS['ctaLabel']}</a>
        </td>
    </tr>
</table>
'''
    }


def section_header_nav():
    """Header with logo and navigation."""
    return {
        "type": "header_nav",
        "name": "Header with Navigation",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 16px 24px; border-bottom: 1px solid {{brandSecondary}}20;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                <tr>
                    <td width="150" valign="middle">
                        <img src="{IMAGE_PLACEHOLDERS['logo']}" alt="{{{{brandName}}}}" width="150" height="50" style="display: block;" />
                    </td>
                    <td align="right" valign="middle" class="mobile-hide">
                        <a href="{{{{navLink1Url}}}}" style="font-family: {{brandFont}}; font-size: 14px; color: {{brandText}}; text-decoration: none; margin-left: 24px;">{{{{navLink1}}}}</a>
                        <a href="{{{{navLink2Url}}}}" style="font-family: {{brandFont}}; font-size: 14px; color: {{brandText}}; text-decoration: none; margin-left: 24px;">{{{{navLink2}}}}</a>
                        <a href="{{{{navLink3Url}}}}" style="font-family: {{brandFont}}; font-size: 14px; color: {{brandText}}; text-decoration: none; margin-left: 24px;">{{{{navLink3}}}}</a>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
'''
    }


def section_offer_banner():
    """Promotional offer banner."""
    return {
        "type": "offer_banner",
        "name": "Offer Banner",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td align="center" style="padding: 12px 24px; background-color: {{brandPrimary}};">
            <p style="font-family: {{brandFont}}; font-size: 14px; color: {{brandBG}}; margin: 0;">{{{{offerText}}}} &bull; <a href="{{{{offerUrl}}}}" style="color: {{brandAccent}}; text-decoration: underline;">Shop Now</a></p>
        </td>
    </tr>
</table>
'''
    }


def section_order_summary():
    """Order/receipt summary table."""
    return {
        "type": "order_summary",
        "name": "Order Summary",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <h3 style="font-family: {{brandFont}}; font-size: 20px; color: {{brandPrimary}}; margin: 0 0 16px; border-bottom: 2px solid {{brandSecondary}}20; padding-bottom: 12px;">Order Summary</h3>
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                <tr>
                    <td width="80"><img src="{IMAGE_PLACEHOLDERS['icon']}" alt="" width="64" height="64" style="display: block;" /></td>
                    <td style="padding-left: 12px;" valign="middle">
                        <p style="font-family: {{brandFont}}; font-size: 14px; color: {{brandPrimary}}; margin: 0; font-weight: 600;">{{{{orderItem1Name}}}}</p>
                        <p style="font-family: {{brandFont}}; font-size: 12px; color: {{brandSecondary}}; margin: 4px 0 0;">Qty: {{{{orderItem1Qty}}}}</p>
                    </td>
                    <td align="right" valign="middle">
                        <p style="font-family: {{brandFont}}; font-size: 14px; color: {{brandPrimary}}; margin: 0;">{{{{orderItem1Price}}}}</p>
                    </td>
                </tr>
            </table>
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-top: 16px; border-top: 1px solid {{brandSecondary}}20; padding-top: 16px;">
                <tr>
                    <td><p style="font-family: {{brandFont}}; font-size: 14px; color: {{brandSecondary}}; margin: 0;">Subtotal</p></td>
                    <td align="right"><p style="font-family: {{brandFont}}; font-size: 14px; color: {{brandPrimary}}; margin: 0;">{{{{orderSubtotal}}}}</p></td>
                </tr>
                <tr>
                    <td style="padding-top: 8px;"><p style="font-family: {{brandFont}}; font-size: 14px; color: {{brandSecondary}}; margin: 0;">Shipping</p></td>
                    <td align="right" style="padding-top: 8px;"><p style="font-family: {{brandFont}}; font-size: 14px; color: {{brandPrimary}}; margin: 0;">{{{{orderShipping}}}}</p></td>
                </tr>
                <tr>
                    <td style="padding-top: 12px; border-top: 2px solid {{brandPrimary}};"><p style="font-family: {{brandFont}}; font-size: 16px; color: {{brandPrimary}}; margin: 0; font-weight: 700;">Total</p></td>
                    <td align="right" style="padding-top: 12px; border-top: 2px solid {{brandPrimary}};"><p style="font-family: {{brandFont}}; font-size: 16px; color: {{brandPrimary}}; margin: 0; font-weight: 700;">{{{{orderTotal}}}}</p></td>
                </tr>
            </table>
        </td>
    </tr>
</table>
'''
    }


def section_social_icons():
    """Social media icon row."""
    return {
        "type": "social_icons",
        "name": "Social Icons",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td align="center" style="padding: 24px;">
            <a href="{{{{facebookUrl}}}}" style="display: inline-block; margin: 0 8px;"><img src="{IMAGE_PLACEHOLDERS['icon']}" alt="Facebook" width="32" height="32" style="display: block;" /></a>
            <a href="{{{{twitterUrl}}}}" style="display: inline-block; margin: 0 8px;"><img src="{IMAGE_PLACEHOLDERS['icon']}" alt="Twitter" width="32" height="32" style="display: block;" /></a>
            <a href="{{{{instagramUrl}}}}" style="display: inline-block; margin: 0 8px;"><img src="{IMAGE_PLACEHOLDERS['icon']}" alt="Instagram" width="32" height="32" style="display: block;" /></a>
            <a href="{{{{linkedinUrl}}}}" style="display: inline-block; margin: 0 8px;"><img src="{IMAGE_PLACEHOLDERS['icon']}" alt="LinkedIn" width="32" height="32" style="display: block;" /></a>
        </td>
    </tr>
</table>
'''
    }


def section_footer_simple():
    """Simple footer with copyright."""
    return {
        "type": "footer_simple",
        "name": "Simple Footer",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td align="center" style="padding: 24px; border-top: 1px solid {{brandSecondary}}20;">
            <p style="font-family: {{brandFont}}; font-size: 12px; color: {{brandSecondary}}; margin: 0 0 8px;">{COPY_TOKENS['footerText']}</p>
            <p style="font-family: {{brandFont}}; font-size: 12px; color: {{brandSecondary}}; margin: 0;">
                <a href="{{{{unsubscribeUrl}}}}" style="color: {{brandSecondary}}; text-decoration: underline;">Unsubscribe</a> &bull;
                <a href="{{{{preferencesUrl}}}}" style="color: {{brandSecondary}}; text-decoration: underline;">Preferences</a> &bull;
                <a href="{{{{privacyUrl}}}}" style="color: {{brandSecondary}}; text-decoration: underline;">Privacy</a>
            </p>
        </td>
    </tr>
</table>
'''
    }


def section_footer_complex():
    """Complex footer with multiple columns."""
    return {
        "type": "footer_complex",
        "name": "Complex Footer",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 32px 24px; background-color: {{brandPrimary}};">
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                <tr>
                    <td width="33%" valign="top" class="mobile-full" style="padding: 8px;">
                        <img src="{IMAGE_PLACEHOLDERS['logo']}" alt="{{{{brandName}}}}" width="120" height="40" style="display: block; margin-bottom: 12px;" />
                        <p style="font-family: {{brandFont}}; font-size: 12px; color: {{brandBG}}; margin: 0; opacity: 0.8;">{{{{companyAddress}}}}</p>
                    </td>
                    <td width="33%" valign="top" class="mobile-full" style="padding: 8px;">
                        <h4 style="font-family: {{brandFont}}; font-size: 14px; color: {{brandBG}}; margin: 0 0 12px;">Quick Links</h4>
                        <p style="margin: 0;"><a href="{{{{aboutUrl}}}}" style="font-family: {{brandFont}}; font-size: 12px; color: {{brandBG}}; text-decoration: none; opacity: 0.8;">About Us</a></p>
                        <p style="margin: 4px 0 0;"><a href="{{{{contactUrl}}}}" style="font-family: {{brandFont}}; font-size: 12px; color: {{brandBG}}; text-decoration: none; opacity: 0.8;">Contact</a></p>
                        <p style="margin: 4px 0 0;"><a href="{{{{faqUrl}}}}" style="font-family: {{brandFont}}; font-size: 12px; color: {{brandBG}}; text-decoration: none; opacity: 0.8;">FAQ</a></p>
                    </td>
                    <td width="33%" valign="top" class="mobile-full" style="padding: 8px;">
                        <h4 style="font-family: {{brandFont}}; font-size: 14px; color: {{brandBG}}; margin: 0 0 12px;">Legal</h4>
                        <p style="margin: 0;"><a href="{{{{privacyUrl}}}}" style="font-family: {{brandFont}}; font-size: 12px; color: {{brandBG}}; text-decoration: none; opacity: 0.8;">Privacy Policy</a></p>
                        <p style="margin: 4px 0 0;"><a href="{{{{termsUrl}}}}" style="font-family: {{brandFont}}; font-size: 12px; color: {{brandBG}}; text-decoration: none; opacity: 0.8;">Terms of Service</a></p>
                        <p style="margin: 4px 0 0;"><a href="{{{{unsubscribeUrl}}}}" style="font-family: {{brandFont}}; font-size: 12px; color: {{brandBG}}; text-decoration: none; opacity: 0.8;">Unsubscribe</a></p>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
'''
    }


def section_divider():
    """Simple horizontal divider."""
    return {
        "type": "divider",
        "name": "Divider",
        "html": '''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 16px 24px;">
            <div style="border-top: 1px solid {brandSecondary}20; height: 1px;"></div>
        </td>
    </tr>
</table>
'''
    }


def section_spacer():
    """Vertical spacer."""
    return {
        "type": "spacer",
        "name": "Spacer",
        "html": '''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="height: 24px; line-height: 24px; font-size: 1px;">&nbsp;</td>
    </tr>
</table>
'''
    }


def section_security_alert():
    """Security/password reset alert box with icon."""
    return {
        "type": "security_alert",
        "name": "Security Alert",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: {{{{brandSecondary}}}}10; border-radius: 8px;">
                <tr>
                    <td style="padding: 24px;">
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td width="64" valign="top">
                                    <img src="{IMAGE_PLACEHOLDERS['icon']}" alt="Security" width="48" height="48" style="display: block;" />
                                </td>
                                <td style="padding-left: 16px;" valign="top">
                                    <h2 style="font-family: {{{{brandFont}}}}; font-size: 20px; color: {{{{brandPrimary}}}}; margin: 0 0 8px;">{{{{securityTitle}}}}</h2>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandText}}}}; margin: 0; line-height: 1.5;">{{{{securityMessage}}}}</p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
'''
    }


def section_verification_code():
    """Large verification code display."""
    return {
        "type": "verification_code",
        "name": "Verification Code",
        "html": '''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td align="center" style="padding: 32px 24px;">
            <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: {brandSecondary}10; border: 2px dashed {brandSecondary}40; border-radius: 8px;">
                <tr>
                    <td style="padding: 24px 48px;">
                        <p style="font-family: {brandFont}; font-size: 14px; color: {brandSecondary}; margin: 0 0 8px; text-transform: uppercase; letter-spacing: 1px;">Verification Code</p>
                        <p style="font-family: 'Courier New', monospace; font-size: 36px; color: {brandPrimary}; margin: 0; font-weight: 700; letter-spacing: 8px;">{{verificationCode}}</p>
                    </td>
                </tr>
            </table>
            <p style="font-family: {brandFont}; font-size: 12px; color: {brandSecondary}; margin: 16px 0 0;">This code expires in {{codeExpiry}}</p>
        </td>
    </tr>
</table>
'''
    }


def section_shipping_tracker():
    """Shipping status with tracking number."""
    return {
        "type": "shipping_tracker",
        "name": "Shipping Tracker",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: {{{{brandAccent}}}}10; border-radius: 8px;">
                <tr>
                    <td style="padding: 24px;">
                        <h3 style="font-family: {{{{brandFont}}}}; font-size: 18px; color: {{{{brandPrimary}}}}; margin: 0 0 16px;">{{{{shippingStatus}}}}</h3>
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td width="50%">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 0;">Tracking Number</p>
                                    <p style="font-family: 'Courier New', monospace; font-size: 14px; color: {{{{brandPrimary}}}}; margin: 4px 0 0; font-weight: 600;">{{{{trackingNumber}}}}</p>
                                </td>
                                <td width="50%">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 0;">Carrier</p>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}}; margin: 4px 0 0; font-weight: 600;">{{{{carrier}}}}</p>
                                </td>
                            </tr>
                        </table>
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-top: 16px;">
                            <tr>
                                <td width="50%">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 0;">Estimated Delivery</p>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandAccent}}}}; margin: 4px 0 0; font-weight: 600;">{{{{estimatedDelivery}}}}</p>
                                </td>
                                <td width="50%" align="right">
                                    <a href="{{{{trackingUrl}}}}" style="display: inline-block; padding: 10px 20px; background-color: {{{{brandAccent}}}}; color: #ffffff; font-family: {{{{brandFont}}}}; font-size: 14px; font-weight: 600; text-decoration: none; border-radius: 6px;">Track Package</a>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
'''
    }


def section_cart_item():
    """Abandoned cart product item."""
    return {
        "type": "cart_item",
        "name": "Cart Item",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 16px 24px;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="border: 1px solid {{{{brandSecondary}}}}20; border-radius: 8px;">
                <tr>
                    <td style="padding: 16px;">
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td width="120">
                                    <img src="{IMAGE_PLACEHOLDERS['product']}" alt="{{{{cartItemAlt}}}}" width="100" height="100" style="display: block; border-radius: 4px;" />
                                </td>
                                <td style="padding-left: 16px;" valign="middle">
                                    <h4 style="font-family: {{{{brandFont}}}}; font-size: 16px; color: {{{{brandPrimary}}}}; margin: 0 0 4px;">{{{{cartItemName}}}}</h4>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 0 0 8px;">{{{{cartItemVariant}}}}</p>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 18px; color: {{{{brandAccent}}}}; margin: 0; font-weight: 700;">{{{{cartItemPrice}}}}</p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
'''
    }


def section_urgency_banner():
    """Urgency/scarcity banner for abandoned cart."""
    return {
        "type": "urgency_banner",
        "name": "Urgency Banner",
        "html": '''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td align="center" style="padding: 16px 24px; background-color: {brandAccent}15;">
            <p style="font-family: {brandFont}; font-size: 14px; color: {brandAccent}; margin: 0; font-weight: 600;">
                ⏰ {{urgencyMessage}}
            </p>
        </td>
    </tr>
</table>
'''
    }


def section_event_details():
    """Event invitation details block."""
    return {
        "type": "event_details",
        "name": "Event Details",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: {{{{brandPrimary}}}}05; border-left: 4px solid {{{{brandAccent}}}}; border-radius: 0 8px 8px 0;">
                <tr>
                    <td style="padding: 24px;">
                        <h3 style="font-family: {{{{brandFont}}}}; font-size: 20px; color: {{{{brandPrimary}}}}; margin: 0 0 16px;">{{{{eventTitle}}}}</h3>
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td width="32" valign="top">
                                    <img src="{IMAGE_PLACEHOLDERS['icon']}" alt="" width="24" height="24" style="display: block;" />
                                </td>
                                <td style="padding-left: 8px; padding-bottom: 12px;">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 0;">Date & Time</p>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}}; margin: 4px 0 0; font-weight: 600;">{{{{eventDateTime}}}}</p>
                                </td>
                            </tr>
                            <tr>
                                <td width="32" valign="top">
                                    <img src="{IMAGE_PLACEHOLDERS['icon']}" alt="" width="24" height="24" style="display: block;" />
                                </td>
                                <td style="padding-left: 8px; padding-bottom: 12px;">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 0;">Location</p>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}}; margin: 4px 0 0; font-weight: 600;">{{{{eventLocation}}}}</p>
                                </td>
                            </tr>
                            <tr>
                                <td width="32" valign="top">
                                    <img src="{IMAGE_PLACEHOLDERS['icon']}" alt="" width="24" height="24" style="display: block;" />
                                </td>
                                <td style="padding-left: 8px;">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 0;">Host</p>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}}; margin: 4px 0 0; font-weight: 600;">{{{{eventHost}}}}</p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
'''
    }


def section_rsvp_buttons():
    """RSVP accept/decline buttons."""
    return {
        "type": "rsvp_buttons",
        "name": "RSVP Buttons",
        "html": '''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td align="center" style="padding: 24px;">
            <table cellpadding="0" cellspacing="0" border="0" role="presentation">
                <tr>
                    <td style="padding-right: 8px;">
                        <a href="{{rsvpAcceptUrl}}" style="display: inline-block; padding: 14px 32px; background-color: {brandAccent}; color: #ffffff; font-family: {brandFont}; font-size: 16px; font-weight: 600; text-decoration: none; border-radius: 8px;">Accept</a>
                    </td>
                    <td style="padding-left: 8px;">
                        <a href="{{rsvpDeclineUrl}}" style="display: inline-block; padding: 14px 32px; background-color: transparent; color: {brandSecondary}; font-family: {brandFont}; font-size: 16px; font-weight: 600; text-decoration: none; border-radius: 8px; border: 2px solid {brandSecondary};">Decline</a>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
'''
    }


def section_countdown_timer():
    """Countdown timer for sales, launches, or events."""
    return {
        "type": "countdown_timer",
        "name": "Countdown Timer",
        "html": '''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td align="center" style="padding: 32px 24px; background-color: {brandPrimary};">
            <p style="font-family: {brandFont}; font-size: 14px; color: {brandBG}; margin: 0 0 16px; text-transform: uppercase; letter-spacing: 2px;">{{countdownLabel}}</p>
            <table cellpadding="0" cellspacing="0" border="0" role="presentation">
                <tr>
                    <td align="center" style="padding: 0 12px;">
                        <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: {brandBG}; border-radius: 8px;">
                            <tr>
                                <td style="padding: 16px 20px;">
                                    <p style="font-family: {brandFont}; font-size: 36px; color: {brandPrimary}; margin: 0; font-weight: 700;">{{countdownDays}}</p>
                                </td>
                            </tr>
                        </table>
                        <p style="font-family: {brandFont}; font-size: 12px; color: {brandBG}; margin: 8px 0 0; text-transform: uppercase;">Days</p>
                    </td>
                    <td align="center" style="padding: 0 12px;">
                        <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: {brandBG}; border-radius: 8px;">
                            <tr>
                                <td style="padding: 16px 20px;">
                                    <p style="font-family: {brandFont}; font-size: 36px; color: {brandPrimary}; margin: 0; font-weight: 700;">{{countdownHours}}</p>
                                </td>
                            </tr>
                        </table>
                        <p style="font-family: {brandFont}; font-size: 12px; color: {brandBG}; margin: 8px 0 0; text-transform: uppercase;">Hours</p>
                    </td>
                    <td align="center" style="padding: 0 12px;">
                        <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: {brandBG}; border-radius: 8px;">
                            <tr>
                                <td style="padding: 16px 20px;">
                                    <p style="font-family: {brandFont}; font-size: 36px; color: {brandPrimary}; margin: 0; font-weight: 700;">{{countdownMins}}</p>
                                </td>
                            </tr>
                        </table>
                        <p style="font-family: {brandFont}; font-size: 12px; color: {brandBG}; margin: 8px 0 0; text-transform: uppercase;">Mins</p>
                    </td>
                    <td align="center" style="padding: 0 12px;">
                        <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: {brandBG}; border-radius: 8px;">
                            <tr>
                                <td style="padding: 16px 20px;">
                                    <p style="font-family: {brandFont}; font-size: 36px; color: {brandPrimary}; margin: 0; font-weight: 700;">{{countdownSecs}}</p>
                                </td>
                            </tr>
                        </table>
                        <p style="font-family: {brandFont}; font-size: 12px; color: {brandBG}; margin: 8px 0 0; text-transform: uppercase;">Secs</p>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
'''
    }


def section_video_placeholder():
    """Video placeholder with play button overlay."""
    return {
        "type": "video_placeholder",
        "name": "Video Placeholder",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td align="center" style="padding: 24px;">
            <a href="{{{{videoUrl}}}}" style="display: block; position: relative; text-decoration: none;">
                <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="position: relative;">
                    <tr>
                        <td>
                            <img src="{IMAGE_PLACEHOLDERS['hero']}" alt="{{{{videoAlt}}}}" width="592" style="width: 100%; max-width: 592px; height: auto; display: block; border-radius: 8px;" />
                        </td>
                    </tr>
                    <tr>
                        <td align="center" style="padding-top: 16px;">
                            <!--[if mso]>
                            <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="{{{{videoUrl}}}}" style="height:60px;v-text-anchor:middle;width:60px;" arcsize="50%" fillcolor="{{{{brandAccent}}}}" stroke="f">
                            <w:anchorlock/>
                            <center style="color:#ffffff;font-family:sans-serif;font-size:24px;">&#9658;</center>
                            </v:roundrect>
                            <![endif]-->
                            <!--[if !mso]><!-->
                            <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: {{{{brandAccent}}}}; border-radius: 50%; margin-top: -80px; position: relative;">
                                <tr>
                                    <td style="padding: 18px 22px 18px 26px;">
                                        <span style="font-size: 24px; color: #ffffff;">&#9658;</span>
                                    </td>
                                </tr>
                            </table>
                            <!--<![endif]-->
                        </td>
                    </tr>
                </table>
            </a>
            <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 16px 0 0;">{{{{videoCaption}}}}</p>
        </td>
    </tr>
</table>
'''
    }


def section_accordion_faq():
    """FAQ/Accordion section (static version for email)."""
    return {
        "type": "accordion_faq",
        "name": "Accordion FAQ",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <h2 style="font-family: {{{{brandFont}}}}; font-size: 24px; color: {{{{brandPrimary}}}}; margin: 0 0 24px;">Frequently Asked Questions</h2>

            <!-- FAQ Item 1 -->
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="border-bottom: 1px solid {{{{brandSecondary}}}}20; margin-bottom: 16px;">
                <tr>
                    <td style="padding-bottom: 16px;">
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td>
                                    <h3 style="font-family: {{{{brandFont}}}}; font-size: 16px; color: {{{{brandPrimary}}}}; margin: 0 0 8px; font-weight: 600;">{{{{faq1Question}}}}</h3>
                                </td>
                                <td width="24" valign="top" align="right">
                                    <span style="font-family: {{{{brandFont}}}}; font-size: 18px; color: {{{{brandAccent}}}}; font-weight: 600;">+</span>
                                </td>
                            </tr>
                        </table>
                        <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandText}}}}; margin: 0; line-height: 1.6;">{{{{faq1Answer}}}}</p>
                    </td>
                </tr>
            </table>

            <!-- FAQ Item 2 -->
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="border-bottom: 1px solid {{{{brandSecondary}}}}20; margin-bottom: 16px;">
                <tr>
                    <td style="padding-bottom: 16px;">
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td>
                                    <h3 style="font-family: {{{{brandFont}}}}; font-size: 16px; color: {{{{brandPrimary}}}}; margin: 0 0 8px; font-weight: 600;">{{{{faq2Question}}}}</h3>
                                </td>
                                <td width="24" valign="top" align="right">
                                    <span style="font-family: {{{{brandFont}}}}; font-size: 18px; color: {{{{brandAccent}}}}; font-weight: 600;">+</span>
                                </td>
                            </tr>
                        </table>
                        <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandText}}}}; margin: 0; line-height: 1.6;">{{{{faq2Answer}}}}</p>
                    </td>
                </tr>
            </table>

            <!-- FAQ Item 3 -->
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="border-bottom: 1px solid {{{{brandSecondary}}}}20; margin-bottom: 16px;">
                <tr>
                    <td style="padding-bottom: 16px;">
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td>
                                    <h3 style="font-family: {{{{brandFont}}}}; font-size: 16px; color: {{{{brandPrimary}}}}; margin: 0 0 8px; font-weight: 600;">{{{{faq3Question}}}}</h3>
                                </td>
                                <td width="24" valign="top" align="right">
                                    <span style="font-family: {{{{brandFont}}}}; font-size: 18px; color: {{{{brandAccent}}}}; font-weight: 600;">+</span>
                                </td>
                            </tr>
                        </table>
                        <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandText}}}}; margin: 0; line-height: 1.6;">{{{{faq3Answer}}}}</p>
                    </td>
                </tr>
            </table>

            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                <tr>
                    <td align="center" style="padding-top: 8px;">
                        <a href="{{{{faqUrl}}}}" style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandAccent}}}}; text-decoration: underline;">View all FAQs &rarr;</a>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
'''
    }


def section_pricing_table():
    """Pricing table with 3 tiers for SaaS/subscription plans."""
    return {
        "type": "pricing_table",
        "name": "Pricing Table",
        "html": '''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <h2 style="font-family: {brandFont}; font-size: 24px; color: {brandPrimary}; margin: 0 0 8px; text-align: center;">Choose Your Plan</h2>
            <p style="font-family: {brandFont}; font-size: 16px; color: {brandSecondary}; margin: 0 0 24px; text-align: center;">{{pricingSubheadline}}</p>

            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                <tr>
                    <!--[if mso]>
                    <td width="33%" valign="top">
                    <![endif]-->
                    <!--[if !mso]><!-->
                    <td style="display: inline-block; width: 100%; max-width: 192px; vertical-align: top; padding: 8px;" class="mobile-full">
                    <!--<![endif]-->
                        <!-- Basic Plan -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="border: 1px solid {brandSecondary}30; border-radius: 8px;">
                            <tr>
                                <td style="padding: 24px 16px; text-align: center;">
                                    <p style="font-family: {brandFont}; font-size: 14px; color: {brandSecondary}; margin: 0 0 8px; text-transform: uppercase; letter-spacing: 1px;">{{plan1Name}}</p>
                                    <p style="font-family: {brandFont}; font-size: 36px; color: {brandPrimary}; margin: 0; font-weight: 700;">{{plan1Price}}</p>
                                    <p style="font-family: {brandFont}; font-size: 12px; color: {brandSecondary}; margin: 4px 0 16px;">{{plan1Period}}</p>
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-bottom: 16px;">
                                        <tr><td style="padding: 6px 0;"><p style="font-family: {brandFont}; font-size: 13px; color: {brandText}; margin: 0;">&#10003; {{plan1Feature1}}</p></td></tr>
                                        <tr><td style="padding: 6px 0;"><p style="font-family: {brandFont}; font-size: 13px; color: {brandText}; margin: 0;">&#10003; {{plan1Feature2}}</p></td></tr>
                                        <tr><td style="padding: 6px 0;"><p style="font-family: {brandFont}; font-size: 13px; color: {brandText}; margin: 0;">&#10003; {{plan1Feature3}}</p></td></tr>
                                    </table>
                                    <a href="{{plan1Url}}" style="display: inline-block; padding: 10px 20px; background-color: transparent; color: {brandAccent}; font-family: {brandFont}; font-size: 14px; font-weight: 600; text-decoration: none; border: 2px solid {brandAccent}; border-radius: 6px;">Select Plan</a>
                                </td>
                            </tr>
                        </table>
                    </td>
                    <!--[if mso]>
                    </td><td width="33%" valign="top">
                    <![endif]-->
                    <!--[if !mso]><!-->
                    <td style="display: inline-block; width: 100%; max-width: 192px; vertical-align: top; padding: 8px;" class="mobile-full">
                    <!--<![endif]-->
                        <!-- Pro Plan (Featured) -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="border: 2px solid {brandAccent}; border-radius: 8px; background-color: {brandAccent}08;">
                            <tr>
                                <td style="padding: 8px 16px; background-color: {brandAccent}; text-align: center; border-radius: 6px 6px 0 0;">
                                    <p style="font-family: {brandFont}; font-size: 12px; color: #ffffff; margin: 0; text-transform: uppercase; letter-spacing: 1px;">Most Popular</p>
                                </td>
                            </tr>
                            <tr>
                                <td style="padding: 24px 16px; text-align: center;">
                                    <p style="font-family: {brandFont}; font-size: 14px; color: {brandSecondary}; margin: 0 0 8px; text-transform: uppercase; letter-spacing: 1px;">{{plan2Name}}</p>
                                    <p style="font-family: {brandFont}; font-size: 36px; color: {brandPrimary}; margin: 0; font-weight: 700;">{{plan2Price}}</p>
                                    <p style="font-family: {brandFont}; font-size: 12px; color: {brandSecondary}; margin: 4px 0 16px;">{{plan2Period}}</p>
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-bottom: 16px;">
                                        <tr><td style="padding: 6px 0;"><p style="font-family: {brandFont}; font-size: 13px; color: {brandText}; margin: 0;">&#10003; {{plan2Feature1}}</p></td></tr>
                                        <tr><td style="padding: 6px 0;"><p style="font-family: {brandFont}; font-size: 13px; color: {brandText}; margin: 0;">&#10003; {{plan2Feature2}}</p></td></tr>
                                        <tr><td style="padding: 6px 0;"><p style="font-family: {brandFont}; font-size: 13px; color: {brandText}; margin: 0;">&#10003; {{plan2Feature3}}</p></td></tr>
                                        <tr><td style="padding: 6px 0;"><p style="font-family: {brandFont}; font-size: 13px; color: {brandText}; margin: 0;">&#10003; {{plan2Feature4}}</p></td></tr>
                                    </table>
                                    <a href="{{plan2Url}}" style="display: inline-block; padding: 10px 20px; background-color: {brandAccent}; color: #ffffff; font-family: {brandFont}; font-size: 14px; font-weight: 600; text-decoration: none; border-radius: 6px;">Select Plan</a>
                                </td>
                            </tr>
                        </table>
                    </td>
                    <!--[if mso]>
                    </td><td width="33%" valign="top">
                    <![endif]-->
                    <!--[if !mso]><!-->
                    <td style="display: inline-block; width: 100%; max-width: 192px; vertical-align: top; padding: 8px;" class="mobile-full">
                    <!--<![endif]-->
                        <!-- Enterprise Plan -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="border: 1px solid {brandSecondary}30; border-radius: 8px;">
                            <tr>
                                <td style="padding: 24px 16px; text-align: center;">
                                    <p style="font-family: {brandFont}; font-size: 14px; color: {brandSecondary}; margin: 0 0 8px; text-transform: uppercase; letter-spacing: 1px;">{{plan3Name}}</p>
                                    <p style="font-family: {brandFont}; font-size: 36px; color: {brandPrimary}; margin: 0; font-weight: 700;">{{plan3Price}}</p>
                                    <p style="font-family: {brandFont}; font-size: 12px; color: {brandSecondary}; margin: 4px 0 16px;">{{plan3Period}}</p>
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-bottom: 16px;">
                                        <tr><td style="padding: 6px 0;"><p style="font-family: {brandFont}; font-size: 13px; color: {brandText}; margin: 0;">&#10003; {{plan3Feature1}}</p></td></tr>
                                        <tr><td style="padding: 6px 0;"><p style="font-family: {brandFont}; font-size: 13px; color: {brandText}; margin: 0;">&#10003; {{plan3Feature2}}</p></td></tr>
                                        <tr><td style="padding: 6px 0;"><p style="font-family: {brandFont}; font-size: 13px; color: {brandText}; margin: 0;">&#10003; {{plan3Feature3}}</p></td></tr>
                                        <tr><td style="padding: 6px 0;"><p style="font-family: {brandFont}; font-size: 13px; color: {brandText}; margin: 0;">&#10003; {{plan3Feature4}}</p></td></tr>
                                        <tr><td style="padding: 6px 0;"><p style="font-family: {brandFont}; font-size: 13px; color: {brandText}; margin: 0;">&#10003; {{plan3Feature5}}</p></td></tr>
                                    </table>
                                    <a href="{{plan3Url}}" style="display: inline-block; padding: 10px 20px; background-color: transparent; color: {brandAccent}; font-family: {brandFont}; font-size: 14px; font-weight: 600; text-decoration: none; border: 2px solid {brandAccent}; border-radius: 6px;">Contact Sales</a>
                                </td>
                            </tr>
                        </table>
                    </td>
                    <!--[if mso]>
                    </td>
                    <![endif]-->
                </tr>
            </table>
        </td>
    </tr>
</table>
'''
    }


def section_progress_tracker():
    """Progress/step tracker for onboarding or multi-step processes."""
    return {
        "type": "progress_tracker",
        "name": "Progress Tracker",
        "html": '''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                <tr>
                    <!-- Step 1 (Completed) -->
                    <td width="25%" align="center" valign="top">
                        <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: {brandAccent}; border-radius: 50%; width: 40px; height: 40px;">
                            <tr>
                                <td align="center" valign="middle" style="padding: 8px;">
                                    <span style="font-family: {brandFont}; font-size: 18px; color: #ffffff; font-weight: 700;">&#10003;</span>
                                </td>
                            </tr>
                        </table>
                        <p style="font-family: {brandFont}; font-size: 12px; color: {brandAccent}; margin: 8px 0 0; font-weight: 600;">{{step1Label}}</p>
                    </td>
                    <!-- Step 2 (Current) -->
                    <td width="25%" align="center" valign="top">
                        <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: {brandAccent}; border-radius: 50%; width: 40px; height: 40px;">
                            <tr>
                                <td align="center" valign="middle">
                                    <span style="font-family: {brandFont}; font-size: 18px; color: #ffffff; font-weight: 700;">2</span>
                                </td>
                            </tr>
                        </table>
                        <p style="font-family: {brandFont}; font-size: 12px; color: {brandPrimary}; margin: 8px 0 0; font-weight: 600;">{{step2Label}}</p>
                    </td>
                    <!-- Step 3 (Pending) -->
                    <td width="25%" align="center" valign="top">
                        <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: transparent; border: 2px solid {brandSecondary}40; border-radius: 50%; width: 40px; height: 40px;">
                            <tr>
                                <td align="center" valign="middle">
                                    <span style="font-family: {brandFont}; font-size: 18px; color: {brandSecondary}; font-weight: 700;">3</span>
                                </td>
                            </tr>
                        </table>
                        <p style="font-family: {brandFont}; font-size: 12px; color: {brandSecondary}; margin: 8px 0 0;">{{step3Label}}</p>
                    </td>
                    <!-- Step 4 (Pending) -->
                    <td width="25%" align="center" valign="top">
                        <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: transparent; border: 2px solid {brandSecondary}40; border-radius: 50%; width: 40px; height: 40px;">
                            <tr>
                                <td align="center" valign="middle">
                                    <span style="font-family: {brandFont}; font-size: 18px; color: {brandSecondary}; font-weight: 700;">4</span>
                                </td>
                            </tr>
                        </table>
                        <p style="font-family: {brandFont}; font-size: 12px; color: {brandSecondary}; margin: 8px 0 0;">{{step4Label}}</p>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
'''
    }


def section_app_store_badges():
    """App store download badges for mobile app promotion."""
    return {
        "type": "app_store_badges",
        "name": "App Store Badges",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td align="center" style="padding: 24px;">
            <p style="font-family: {{{{brandFont}}}}; font-size: 16px; color: {{{{brandPrimary}}}}; margin: 0 0 16px;">{{{{appStoreHeadline}}}}</p>
            <table cellpadding="0" cellspacing="0" border="0" role="presentation">
                <tr>
                    <td style="padding-right: 8px;">
                        <a href="{{{{appStoreUrl}}}}" style="display: block;">
                            <img src="{IMAGE_PLACEHOLDERS['product']}" alt="Download on the App Store" width="135" height="40" style="display: block; border-radius: 6px;" />
                        </a>
                    </td>
                    <td style="padding-left: 8px;">
                        <a href="{{{{playStoreUrl}}}}" style="display: block;">
                            <img src="{IMAGE_PLACEHOLDERS['product']}" alt="Get it on Google Play" width="135" height="40" style="display: block; border-radius: 6px;" />
                        </a>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
'''
    }


# Registry of all sections
SECTION_REGISTRY = {
    "hero": section_hero,
    "subhero": section_subhero,
    "1col_text": section_1col_text,
    "2col_text_image": section_2col_text_image,
    "3col_features": section_3col_features,
    "product_grid": section_product_grid,
    "testimonial": section_testimonial,
    "story_block": section_story_block,
    "cta_band": section_cta_band,
    "header_nav": section_header_nav,
    "offer_banner": section_offer_banner,
    "order_summary": section_order_summary,
    "social_icons": section_social_icons,
    "footer_simple": section_footer_simple,
    "footer_complex": section_footer_complex,
    "divider": section_divider,
    "spacer": section_spacer,
    "security_alert": section_security_alert,
    "verification_code": section_verification_code,
    "shipping_tracker": section_shipping_tracker,
    "cart_item": section_cart_item,
    "urgency_banner": section_urgency_banner,
    "event_details": section_event_details,
    "rsvp_buttons": section_rsvp_buttons,
    "countdown_timer": section_countdown_timer,
    "video_placeholder": section_video_placeholder,
    "accordion_faq": section_accordion_faq,
    "pricing_table": section_pricing_table,
    "progress_tracker": section_progress_tracker,
    "app_store_badges": section_app_store_badges,
}


def get_section(section_type):
    """Get a section by type."""
    if section_type in SECTION_REGISTRY:
        return SECTION_REGISTRY[section_type]()
    return None


def get_all_sections():
    """Get all available sections."""
    return {name: func() for name, func in SECTION_REGISTRY.items()}


def list_section_types():
    """List all available section types."""
    return list(SECTION_REGISTRY.keys())

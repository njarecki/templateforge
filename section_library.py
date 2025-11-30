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


def section_team_members():
    """Team members grid with photos and roles."""
    return {
        "type": "team_members",
        "name": "Team Members",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <h2 style="font-family: {{{{brandFont}}}}; font-size: 24px; color: {{{{brandPrimary}}}}; margin: 0 0 24px; text-align: center;">{{{{teamHeadline}}}}</h2>
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                <tr>
                    <!--[if mso]>
                    <td width="33%" valign="top">
                    <![endif]-->
                    <!--[if !mso]><!-->
                    <td style="display: inline-block; width: 100%; max-width: 192px; vertical-align: top; padding: 8px;" class="mobile-full">
                    <!--<![endif]-->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td align="center">
                                    <img src="{IMAGE_PLACEHOLDERS['avatar']}" alt="{{{{member1Name}}}}" width="100" height="100" style="display: block; border-radius: 50%;" />
                                </td>
                            </tr>
                            <tr>
                                <td align="center" style="padding-top: 12px;">
                                    <h4 style="font-family: {{{{brandFont}}}}; font-size: 16px; color: {{{{brandPrimary}}}}; margin: 0;">{{{{member1Name}}}}</h4>
                                </td>
                            </tr>
                            <tr>
                                <td align="center" style="padding-top: 4px;">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 0;">{{{{member1Role}}}}</p>
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
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td align="center">
                                    <img src="{IMAGE_PLACEHOLDERS['avatar']}" alt="{{{{member2Name}}}}" width="100" height="100" style="display: block; border-radius: 50%;" />
                                </td>
                            </tr>
                            <tr>
                                <td align="center" style="padding-top: 12px;">
                                    <h4 style="font-family: {{{{brandFont}}}}; font-size: 16px; color: {{{{brandPrimary}}}}; margin: 0;">{{{{member2Name}}}}</h4>
                                </td>
                            </tr>
                            <tr>
                                <td align="center" style="padding-top: 4px;">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 0;">{{{{member2Role}}}}</p>
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
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td align="center">
                                    <img src="{IMAGE_PLACEHOLDERS['avatar']}" alt="{{{{member3Name}}}}" width="100" height="100" style="display: block; border-radius: 50%;" />
                                </td>
                            </tr>
                            <tr>
                                <td align="center" style="padding-top: 12px;">
                                    <h4 style="font-family: {{{{brandFont}}}}; font-size: 16px; color: {{{{brandPrimary}}}}; margin: 0;">{{{{member3Name}}}}</h4>
                                </td>
                            </tr>
                            <tr>
                                <td align="center" style="padding-top: 4px;">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 0;">{{{{member3Role}}}}</p>
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


def section_comparison_table():
    """Feature comparison table for products/plans."""
    return {
        "type": "comparison_table",
        "name": "Comparison Table",
        "html": '''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <h2 style="font-family: {brandFont}; font-size: 24px; color: {brandPrimary}; margin: 0 0 24px; text-align: center;">{{comparisonHeadline}}</h2>
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="border: 1px solid {brandSecondary}30; border-radius: 8px; overflow: hidden;">
                <!-- Header Row -->
                <tr style="background-color: {brandPrimary};">
                    <td style="padding: 12px 16px; border-right: 1px solid {brandSecondary}30;">
                        <p style="font-family: {brandFont}; font-size: 14px; color: {brandBG}; margin: 0; font-weight: 600;">Feature</p>
                    </td>
                    <td style="padding: 12px 16px; border-right: 1px solid {brandSecondary}30; text-align: center;">
                        <p style="font-family: {brandFont}; font-size: 14px; color: {brandBG}; margin: 0; font-weight: 600;">{{compCol1}}</p>
                    </td>
                    <td style="padding: 12px 16px; text-align: center;">
                        <p style="font-family: {brandFont}; font-size: 14px; color: {brandBG}; margin: 0; font-weight: 600;">{{compCol2}}</p>
                    </td>
                </tr>
                <!-- Row 1 -->
                <tr style="background-color: {brandBG};">
                    <td style="padding: 12px 16px; border-right: 1px solid {brandSecondary}20; border-bottom: 1px solid {brandSecondary}20;">
                        <p style="font-family: {brandFont}; font-size: 14px; color: {brandText}; margin: 0;">{{compRow1Feature}}</p>
                    </td>
                    <td style="padding: 12px 16px; border-right: 1px solid {brandSecondary}20; border-bottom: 1px solid {brandSecondary}20; text-align: center;">
                        <p style="font-family: {brandFont}; font-size: 14px; color: {brandText}; margin: 0;">{{compRow1Col1}}</p>
                    </td>
                    <td style="padding: 12px 16px; border-bottom: 1px solid {brandSecondary}20; text-align: center;">
                        <p style="font-family: {brandFont}; font-size: 14px; color: {brandText}; margin: 0;">{{compRow1Col2}}</p>
                    </td>
                </tr>
                <!-- Row 2 -->
                <tr style="background-color: {brandSecondary}08;">
                    <td style="padding: 12px 16px; border-right: 1px solid {brandSecondary}20; border-bottom: 1px solid {brandSecondary}20;">
                        <p style="font-family: {brandFont}; font-size: 14px; color: {brandText}; margin: 0;">{{compRow2Feature}}</p>
                    </td>
                    <td style="padding: 12px 16px; border-right: 1px solid {brandSecondary}20; border-bottom: 1px solid {brandSecondary}20; text-align: center;">
                        <p style="font-family: {brandFont}; font-size: 14px; color: {brandText}; margin: 0;">{{compRow2Col1}}</p>
                    </td>
                    <td style="padding: 12px 16px; border-bottom: 1px solid {brandSecondary}20; text-align: center;">
                        <p style="font-family: {brandFont}; font-size: 14px; color: {brandText}; margin: 0;">{{compRow2Col2}}</p>
                    </td>
                </tr>
                <!-- Row 3 -->
                <tr style="background-color: {brandBG};">
                    <td style="padding: 12px 16px; border-right: 1px solid {brandSecondary}20; border-bottom: 1px solid {brandSecondary}20;">
                        <p style="font-family: {brandFont}; font-size: 14px; color: {brandText}; margin: 0;">{{compRow3Feature}}</p>
                    </td>
                    <td style="padding: 12px 16px; border-right: 1px solid {brandSecondary}20; border-bottom: 1px solid {brandSecondary}20; text-align: center;">
                        <p style="font-family: {brandFont}; font-size: 14px; color: {brandText}; margin: 0;">{{compRow3Col1}}</p>
                    </td>
                    <td style="padding: 12px 16px; border-bottom: 1px solid {brandSecondary}20; text-align: center;">
                        <p style="font-family: {brandFont}; font-size: 14px; color: {brandText}; margin: 0;">{{compRow3Col2}}</p>
                    </td>
                </tr>
                <!-- Row 4 -->
                <tr style="background-color: {brandSecondary}08;">
                    <td style="padding: 12px 16px; border-right: 1px solid {brandSecondary}20;">
                        <p style="font-family: {brandFont}; font-size: 14px; color: {brandText}; margin: 0;">{{compRow4Feature}}</p>
                    </td>
                    <td style="padding: 12px 16px; border-right: 1px solid {brandSecondary}20; text-align: center;">
                        <p style="font-family: {brandFont}; font-size: 14px; color: {brandText}; margin: 0;">{{compRow4Col1}}</p>
                    </td>
                    <td style="padding: 12px 16px; text-align: center;">
                        <p style="font-family: {brandFont}; font-size: 14px; color: {brandText}; margin: 0;">{{compRow4Col2}}</p>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
'''
    }


def section_stats_metrics():
    """Stats/metrics row with 3-4 key numbers."""
    return {
        "type": "stats_metrics",
        "name": "Stats Metrics",
        "html": '''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 32px 24px; background-color: {brandPrimary};">
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                <tr>
                    <!--[if mso]>
                    <td width="25%" valign="top">
                    <![endif]-->
                    <!--[if !mso]><!-->
                    <td style="display: inline-block; width: 100%; max-width: 144px; vertical-align: top; padding: 8px;" class="mobile-full">
                    <!--<![endif]-->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td align="center">
                                    <p style="font-family: {brandFont}; font-size: 36px; color: {brandBG}; margin: 0; font-weight: 700;">{{stat1Value}}</p>
                                </td>
                            </tr>
                            <tr>
                                <td align="center" style="padding-top: 4px;">
                                    <p style="font-family: {brandFont}; font-size: 14px; color: {brandBG}; margin: 0; opacity: 0.8;">{{stat1Label}}</p>
                                </td>
                            </tr>
                        </table>
                    </td>
                    <!--[if mso]>
                    </td><td width="25%" valign="top">
                    <![endif]-->
                    <!--[if !mso]><!-->
                    <td style="display: inline-block; width: 100%; max-width: 144px; vertical-align: top; padding: 8px;" class="mobile-full">
                    <!--<![endif]-->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td align="center">
                                    <p style="font-family: {brandFont}; font-size: 36px; color: {brandBG}; margin: 0; font-weight: 700;">{{stat2Value}}</p>
                                </td>
                            </tr>
                            <tr>
                                <td align="center" style="padding-top: 4px;">
                                    <p style="font-family: {brandFont}; font-size: 14px; color: {brandBG}; margin: 0; opacity: 0.8;">{{stat2Label}}</p>
                                </td>
                            </tr>
                        </table>
                    </td>
                    <!--[if mso]>
                    </td><td width="25%" valign="top">
                    <![endif]-->
                    <!--[if !mso]><!-->
                    <td style="display: inline-block; width: 100%; max-width: 144px; vertical-align: top; padding: 8px;" class="mobile-full">
                    <!--<![endif]-->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td align="center">
                                    <p style="font-family: {brandFont}; font-size: 36px; color: {brandBG}; margin: 0; font-weight: 700;">{{stat3Value}}</p>
                                </td>
                            </tr>
                            <tr>
                                <td align="center" style="padding-top: 4px;">
                                    <p style="font-family: {brandFont}; font-size: 14px; color: {brandBG}; margin: 0; opacity: 0.8;">{{stat3Label}}</p>
                                </td>
                            </tr>
                        </table>
                    </td>
                    <!--[if mso]>
                    </td><td width="25%" valign="top">
                    <![endif]-->
                    <!--[if !mso]><!-->
                    <td style="display: inline-block; width: 100%; max-width: 144px; vertical-align: top; padding: 8px;" class="mobile-full">
                    <!--<![endif]-->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td align="center">
                                    <p style="font-family: {brandFont}; font-size: 36px; color: {brandBG}; margin: 0; font-weight: 700;">{{stat4Value}}</p>
                                </td>
                            </tr>
                            <tr>
                                <td align="center" style="padding-top: 4px;">
                                    <p style="font-family: {brandFont}; font-size: 14px; color: {brandBG}; margin: 0; opacity: 0.8;">{{stat4Label}}</p>
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


def section_rating_stars():
    """Star rating display with numeric score for reviews/ratings."""
    return {
        "type": "rating_stars",
        "name": "Rating Stars",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: {{{{brandSecondary}}}}08; border-radius: 8px;">
                <tr>
                    <td style="padding: 24px;">
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td width="120" valign="middle">
                                    <img src="{IMAGE_PLACEHOLDERS['product']}" alt="{{{{ratingProductAlt}}}}" width="100" height="100" style="display: block; border-radius: 8px;" />
                                </td>
                                <td style="padding-left: 16px;" valign="middle">
                                    <h3 style="font-family: {{{{brandFont}}}}; font-size: 18px; color: {{{{brandPrimary}}}}; margin: 0 0 8px;">{{{{ratingProductName}}}}</h3>
                                    <table cellpadding="0" cellspacing="0" border="0" role="presentation">
                                        <tr>
                                            <td style="padding-right: 8px;">
                                                <!-- Star rating display using HTML entities -->
                                                <span style="font-size: 20px; color: {{{{brandAccent}}}}; letter-spacing: 2px;">&#9733;&#9733;&#9733;&#9733;&#9734;</span>
                                            </td>
                                            <td valign="middle">
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 16px; color: {{{{brandPrimary}}}}; margin: 0; font-weight: 700;">{{{{ratingScore}}}}</p>
                                            </td>
                                        </tr>
                                    </table>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 8px 0 0;">{{{{ratingCount}}}} reviews</p>
                                </td>
                            </tr>
                        </table>
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-top: 16px; padding-top: 16px; border-top: 1px solid {{{{brandSecondary}}}}20;">
                            <tr>
                                <td>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; font-style: italic; color: {{{{brandText}}}}; margin: 0; line-height: 1.5;">&ldquo;{{{{ratingReviewText}}}}&rdquo;</p>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 13px; color: {{{{brandSecondary}}}}; margin: 8px 0 0;">&mdash; {{{{ratingReviewAuthor}}}}</p>
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


def section_gallery_carousel():
    """Image gallery with 4 product images in a row (static carousel for email)."""
    return {
        "type": "gallery_carousel",
        "name": "Gallery Carousel",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <h2 style="font-family: {{{{brandFont}}}}; font-size: 24px; color: {{{{brandPrimary}}}}; margin: 0 0 16px; text-align: center;">{{{{galleryHeadline}}}}</h2>
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                <tr>
                    <!--[if mso]>
                    <td width="25%" valign="top">
                    <![endif]-->
                    <!--[if !mso]><!-->
                    <td style="display: inline-block; width: 100%; max-width: 144px; vertical-align: top; padding: 4px;" class="mobile-full">
                    <!--<![endif]-->
                        <a href="{{{{galleryItem1Url}}}}" style="display: block; text-decoration: none;">
                            <img src="{IMAGE_PLACEHOLDERS['product']}" alt="{{{{galleryItem1Alt}}}}" width="136" style="width: 100%; max-width: 136px; height: auto; display: block; border-radius: 8px;" />
                            <p style="font-family: {{{{brandFont}}}}; font-size: 13px; color: {{{{brandPrimary}}}}; margin: 8px 0 0; text-align: center;">{{{{galleryItem1Label}}}}</p>
                        </a>
                    </td>
                    <!--[if mso]>
                    </td><td width="25%" valign="top">
                    <![endif]-->
                    <!--[if !mso]><!-->
                    <td style="display: inline-block; width: 100%; max-width: 144px; vertical-align: top; padding: 4px;" class="mobile-full">
                    <!--<![endif]-->
                        <a href="{{{{galleryItem2Url}}}}" style="display: block; text-decoration: none;">
                            <img src="{IMAGE_PLACEHOLDERS['product']}" alt="{{{{galleryItem2Alt}}}}" width="136" style="width: 100%; max-width: 136px; height: auto; display: block; border-radius: 8px;" />
                            <p style="font-family: {{{{brandFont}}}}; font-size: 13px; color: {{{{brandPrimary}}}}; margin: 8px 0 0; text-align: center;">{{{{galleryItem2Label}}}}</p>
                        </a>
                    </td>
                    <!--[if mso]>
                    </td><td width="25%" valign="top">
                    <![endif]-->
                    <!--[if !mso]><!-->
                    <td style="display: inline-block; width: 100%; max-width: 144px; vertical-align: top; padding: 4px;" class="mobile-full">
                    <!--<![endif]-->
                        <a href="{{{{galleryItem3Url}}}}" style="display: block; text-decoration: none;">
                            <img src="{IMAGE_PLACEHOLDERS['product']}" alt="{{{{galleryItem3Alt}}}}" width="136" style="width: 100%; max-width: 136px; height: auto; display: block; border-radius: 8px;" />
                            <p style="font-family: {{{{brandFont}}}}; font-size: 13px; color: {{{{brandPrimary}}}}; margin: 8px 0 0; text-align: center;">{{{{galleryItem3Label}}}}</p>
                        </a>
                    </td>
                    <!--[if mso]>
                    </td><td width="25%" valign="top">
                    <![endif]-->
                    <!--[if !mso]><!-->
                    <td style="display: inline-block; width: 100%; max-width: 144px; vertical-align: top; padding: 4px;" class="mobile-full">
                    <!--<![endif]-->
                        <a href="{{{{galleryItem4Url}}}}" style="display: block; text-decoration: none;">
                            <img src="{IMAGE_PLACEHOLDERS['product']}" alt="{{{{galleryItem4Alt}}}}" width="136" style="width: 100%; max-width: 136px; height: auto; display: block; border-radius: 8px;" />
                            <p style="font-family: {{{{brandFont}}}}; font-size: 13px; color: {{{{brandPrimary}}}}; margin: 8px 0 0; text-align: center;">{{{{galleryItem4Label}}}}</p>
                        </a>
                    </td>
                    <!--[if mso]>
                    </td>
                    <![endif]-->
                </tr>
            </table>
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-top: 16px;">
                <tr>
                    <td align="center">
                        <a href="{{{{galleryViewAllUrl}}}}" style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandAccent}}}}; text-decoration: underline;">View all &rarr;</a>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
'''
    }


def section_multi_step_form():
    """Multi-step form with 3 input fields and progress indicator."""
    return {
        "type": "multi_step_form",
        "name": "Multi-Step Form",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: {{{{brandSecondary}}}}08; border-radius: 8px;">
                <tr>
                    <td style="padding: 24px;">
                        <h2 style="font-family: {{{{brandFont}}}}; font-size: 20px; color: {{{{brandPrimary}}}}; margin: 0 0 8px;">{{{{formHeadline}}}}</h2>
                        <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 0 0 20px;">{{{{formSubheadline}}}}</p>

                        <!-- Progress indicator -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-bottom: 24px;">
                            <tr>
                                <td>
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: {{{{brandSecondary}}}}20; border-radius: 4px; height: 8px;">
                                        <tr>
                                            <td width="33%" style="background-color: {{{{brandAccent}}}}; border-radius: 4px; height: 8px;"></td>
                                            <td width="67%"></td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            <tr>
                                <td style="padding-top: 8px;">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 0;">Step {{{{formCurrentStep}}}} of {{{{formTotalSteps}}}}</p>
                                </td>
                            </tr>
                        </table>

                        <!-- Form fields (static display for email) -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <!-- Field 1 -->
                            <tr>
                                <td style="padding-bottom: 16px;">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 13px; color: {{{{brandPrimary}}}}; margin: 0 0 6px; font-weight: 600;">{{{{formField1Label}}}}</p>
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="border: 1px solid {{{{brandSecondary}}}}40; border-radius: 6px; background-color: {{{{brandBG}}}};">
                                        <tr>
                                            <td style="padding: 12px 14px;">
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 0;">{{{{formField1Placeholder}}}}</p>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            <!-- Field 2 -->
                            <tr>
                                <td style="padding-bottom: 16px;">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 13px; color: {{{{brandPrimary}}}}; margin: 0 0 6px; font-weight: 600;">{{{{formField2Label}}}}</p>
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="border: 1px solid {{{{brandSecondary}}}}40; border-radius: 6px; background-color: {{{{brandBG}}}};">
                                        <tr>
                                            <td style="padding: 12px 14px;">
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 0;">{{{{formField2Placeholder}}}}</p>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            <!-- Field 3 -->
                            <tr>
                                <td style="padding-bottom: 20px;">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 13px; color: {{{{brandPrimary}}}}; margin: 0 0 6px; font-weight: 600;">{{{{formField3Label}}}}</p>
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="border: 1px solid {{{{brandSecondary}}}}40; border-radius: 6px; background-color: {{{{brandBG}}}};">
                                        <tr>
                                            <td style="padding: 12px 14px;">
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 0;">{{{{formField3Placeholder}}}}</p>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>

                        <!-- CTA Button -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td align="center">
                                    <a href="{{{{formContinueUrl}}}}" style="display: inline-block; padding: 14px 32px; background-color: {{{{brandAccent}}}}; color: #ffffff; font-family: {{{{brandFont}}}}; font-size: 16px; font-weight: 600; text-decoration: none; border-radius: 8px;">{{{{formContinueLabel}}}}</a>
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


def section_referral_program():
    """Referral program section with unique referral link and rewards info."""
    return {
        "type": "referral_program",
        "name": "Referral Program",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: {{{{brandAccent}}}}10; border-radius: 12px; border: 2px dashed {{{{brandAccent}}}}40;">
                <tr>
                    <td style="padding: 32px;" align="center">
                        <!-- Icon/Image -->
                        <table width="80" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td align="center" style="width: 80px; height: 80px; background-color: {{{{brandAccent}}}}; border-radius: 50%;">
                                    <img src="{IMAGE_PLACEHOLDERS['icon']}" alt="Refer" width="40" height="40" style="display: block;" />
                                </td>
                            </tr>
                        </table>

                        <h2 style="font-family: {{{{brandFont}}}}; font-size: 24px; color: {{{{brandPrimary}}}}; margin: 24px 0 8px;">{{{{referralHeadline}}}}</h2>
                        <p style="font-family: {{{{brandFont}}}}; font-size: 16px; color: {{{{brandSecondary}}}}; margin: 0 0 24px; max-width: 400px;">{{{{referralDescription}}}}</p>

                        <!-- Reward highlight -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="max-width: 360px; margin: 0 auto 24px;">
                            <tr>
                                <td width="50%" style="padding: 16px; background-color: {{{{brandBG}}}}; border-radius: 8px 0 0 8px; text-align: center;">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 0 0 4px; text-transform: uppercase;">You Get</p>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 24px; color: {{{{brandAccent}}}}; margin: 0; font-weight: 700;">{{{{referralYourReward}}}}</p>
                                </td>
                                <td width="50%" style="padding: 16px; background-color: {{{{brandBG}}}}; border-radius: 0 8px 8px 0; text-align: center; border-left: 2px solid {{{{brandSecondary}}}}20;">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 0 0 4px; text-transform: uppercase;">They Get</p>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 24px; color: {{{{brandAccent}}}}; margin: 0; font-weight: 700;">{{{{referralTheirReward}}}}</p>
                                </td>
                            </tr>
                        </table>

                        <!-- Referral link -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="max-width: 400px; margin: 0 auto 20px;">
                            <tr>
                                <td style="padding: 14px 20px; background-color: {{{{brandBG}}}}; border: 1px solid {{{{brandSecondary}}}}30; border-radius: 8px;">
                                    <p style="font-family: monospace; font-size: 14px; color: {{{{brandPrimary}}}}; margin: 0; word-break: break-all;">{{{{referralLink}}}}</p>
                                </td>
                            </tr>
                        </table>

                        <a href="{{{{referralShareUrl}}}}" style="display: inline-block; padding: 14px 32px; background-color: {{{{brandAccent}}}}; color: #ffffff; font-family: {{{{brandFont}}}}; font-size: 16px; font-weight: 600; text-decoration: none; border-radius: 8px;">{{{{referralCtaLabel}}}}</a>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
'''
    }


def section_loyalty_points():
    """Loyalty points section showing current balance, tier status, and rewards."""
    return {
        "type": "loyalty_points",
        "name": "Loyalty Points",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background: linear-gradient(135deg, {{{{brandPrimary}}}} 0%, {{{{brandAccent}}}} 100%); border-radius: 16px;">
                <tr>
                    <td style="padding: 32px;">
                        <!-- Header -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: #ffffff99; margin: 0 0 4px; text-transform: uppercase; letter-spacing: 1px;">{{{{loyaltyProgramName}}}}</p>
                                    <h2 style="font-family: {{{{brandFont}}}}; font-size: 28px; color: #ffffff; margin: 0;">{{{{loyaltyUserName}}}}</h2>
                                </td>
                                <td align="right" valign="top">
                                    <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: #ffffff20; border-radius: 20px; padding: 6px 16px;">
                                        <tr>
                                            <td>
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: #ffffff; margin: 0; font-weight: 600;">{{{{loyaltyTier}}}}</p>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>

                        <!-- Points display -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin: 24px 0;">
                            <tr>
                                <td align="center">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 56px; color: #ffffff; margin: 0; font-weight: 700; line-height: 1;">{{{{loyaltyPoints}}}}</p>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 16px; color: #ffffff99; margin: 8px 0 0;">points available</p>
                                </td>
                            </tr>
                        </table>

                        <!-- Progress to next tier -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-bottom: 24px;">
                            <tr>
                                <td>
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: #ffffff30; border-radius: 4px; height: 8px;">
                                        <tr>
                                            <td width="{{{{loyaltyProgressPercent}}}}%" style="background-color: #ffffff; border-radius: 4px; height: 8px;"></td>
                                            <td></td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            <tr>
                                <td style="padding-top: 8px;">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 13px; color: #ffffff99; margin: 0;">{{{{loyaltyPointsToNext}}}} points to {{{{loyaltyNextTier}}}}</p>
                                </td>
                            </tr>
                        </table>

                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td align="center">
                                    <a href="{{{{loyaltyRedeemUrl}}}}" style="display: inline-block; padding: 14px 32px; background-color: #ffffff; color: {{{{brandPrimary}}}}; font-family: {{{{brandFont}}}}; font-size: 16px; font-weight: 600; text-decoration: none; border-radius: 8px;">{{{{loyaltyCtaLabel}}}}</a>
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


def section_gift_card():
    """Gift card section with amount, code, and redemption info."""
    return {
        "type": "gift_card",
        "name": "Gift Card",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: {{{{brandPrimary}}}}; border-radius: 16px; overflow: hidden;">
                <tr>
                    <td style="padding: 0;">
                        <!-- Decorative header strip -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: {{{{brandAccent}}}};">
                            <tr>
                                <td style="padding: 16px 32px;">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: #ffffff; margin: 0; font-weight: 600; text-transform: uppercase; letter-spacing: 2px;">{{{{giftCardBrandName}}}}</p>
                                </td>
                            </tr>
                        </table>

                        <!-- Main gift card body -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td style="padding: 32px;">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 16px; color: #ffffff99; margin: 0 0 8px;">Gift Card</p>
                                    <h2 style="font-family: {{{{brandFont}}}}; font-size: 48px; color: #ffffff; margin: 0 0 24px; font-weight: 700;">{{{{giftCardAmount}}}}</h2>

                                    <!-- Gift card code -->
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: #ffffff15; border-radius: 8px; margin-bottom: 24px;">
                                        <tr>
                                            <td style="padding: 20px;">
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: #ffffff80; margin: 0 0 8px; text-transform: uppercase;">Your Gift Code</p>
                                                <p style="font-family: monospace; font-size: 28px; color: #ffffff; margin: 0; letter-spacing: 4px; font-weight: 600;">{{{{giftCardCode}}}}</p>
                                            </td>
                                        </tr>
                                    </table>

                                    <!-- From/To info -->
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-bottom: 24px;">
                                        <tr>
                                            <td width="50%">
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: #ffffff80; margin: 0 0 4px; text-transform: uppercase;">From</p>
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 16px; color: #ffffff; margin: 0;">{{{{giftCardFrom}}}}</p>
                                            </td>
                                            <td width="50%">
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: #ffffff80; margin: 0 0 4px; text-transform: uppercase;">To</p>
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 16px; color: #ffffff; margin: 0;">{{{{giftCardTo}}}}</p>
                                            </td>
                                        </tr>
                                    </table>

                                    <!-- Personal message -->
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="border-left: 3px solid {{{{brandAccent}}}}; padding-left: 16px; margin-bottom: 24px;">
                                        <tr>
                                            <td>
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 16px; color: #ffffff; margin: 0; font-style: italic;">"{{{{giftCardMessage}}}}"</p>
                                            </td>
                                        </tr>
                                    </table>

                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                                        <tr>
                                            <td align="center">
                                                <a href="{{{{giftCardRedeemUrl}}}}" style="display: inline-block; padding: 14px 32px; background-color: {{{{brandAccent}}}}; color: #ffffff; font-family: {{{{brandFont}}}}; font-size: 16px; font-weight: 600; text-decoration: none; border-radius: 8px;">{{{{giftCardCtaLabel}}}}</a>
                                            </td>
                                        </tr>
                                    </table>

                                    <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: #ffffff60; margin: 20px 0 0; text-align: center;">Valid until {{{{giftCardExpiry}}}}</p>
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


def section_subscription_renewal():
    """Subscription renewal section with plan details, renewal date, and action buttons."""
    return {
        "type": "subscription_renewal",
        "name": "Subscription Renewal",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="border: 1px solid {{{{brandSecondary}}}}20; border-radius: 12px;">
                <tr>
                    <td style="padding: 32px;">
                        <!-- Status indicator -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-bottom: 24px;">
                            <tr>
                                <td>
                                    <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: {{{{subscriptionStatusColor}}}}15; border-radius: 20px; padding: 6px 16px;">
                                        <tr>
                                            <td style="padding-right: 8px;">
                                                <table width="8" height="8" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: {{{{subscriptionStatusColor}}}}; border-radius: 50%;">
                                                    <tr><td></td></tr>
                                                </table>
                                            </td>
                                            <td>
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 13px; color: {{{{subscriptionStatusColor}}}}; margin: 0; font-weight: 600;">{{{{subscriptionStatus}}}}</p>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>

                        <h2 style="font-family: {{{{brandFont}}}}; font-size: 24px; color: {{{{brandPrimary}}}}; margin: 0 0 8px;">{{{{subscriptionHeadline}}}}</h2>
                        <p style="font-family: {{{{brandFont}}}}; font-size: 16px; color: {{{{brandSecondary}}}}; margin: 0 0 24px;">{{{{subscriptionDescription}}}}</p>

                        <!-- Plan details card -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: {{{{brandSecondary}}}}08; border-radius: 8px; margin-bottom: 24px;">
                            <tr>
                                <td style="padding: 24px;">
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                                        <tr>
                                            <td>
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 0 0 4px;">Current Plan</p>
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 20px; color: {{{{brandPrimary}}}}; margin: 0; font-weight: 600;">{{{{subscriptionPlanName}}}}</p>
                                            </td>
                                            <td align="right">
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 28px; color: {{{{brandPrimary}}}}; margin: 0; font-weight: 700;">{{{{subscriptionPrice}}}}</p>
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 0;">{{{{subscriptionBillingCycle}}}}</p>
                                            </td>
                                        </tr>
                                    </table>

                                    <!-- Divider -->
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin: 20px 0;">
                                        <tr>
                                            <td style="border-top: 1px solid {{{{brandSecondary}}}}20;"></td>
                                        </tr>
                                    </table>

                                    <!-- Renewal info -->
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                                        <tr>
                                            <td width="50%">
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 13px; color: {{{{brandSecondary}}}}; margin: 0 0 4px;">Renewal Date</p>
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 16px; color: {{{{brandPrimary}}}}; margin: 0; font-weight: 600;">{{{{subscriptionRenewalDate}}}}</p>
                                            </td>
                                            <td width="50%">
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 13px; color: {{{{brandSecondary}}}}; margin: 0 0 4px;">Payment Method</p>
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 16px; color: {{{{brandPrimary}}}}; margin: 0; font-weight: 600;">{{{{subscriptionPaymentMethod}}}}</p>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>

                        <!-- Action buttons -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td align="center" style="padding-right: 8px;">
                                    <a href="{{{{subscriptionManageUrl}}}}" style="display: inline-block; padding: 14px 24px; background-color: {{{{brandAccent}}}}; color: #ffffff; font-family: {{{{brandFont}}}}; font-size: 16px; font-weight: 600; text-decoration: none; border-radius: 8px;">{{{{subscriptionPrimaryCtaLabel}}}}</a>
                                </td>
                                <td align="center" style="padding-left: 8px;">
                                    <a href="{{{{subscriptionUpgradeUrl}}}}" style="display: inline-block; padding: 14px 24px; background-color: transparent; color: {{{{brandAccent}}}}; font-family: {{{{brandFont}}}}; font-size: 16px; font-weight: 600; text-decoration: none; border-radius: 8px; border: 2px solid {{{{brandAccent}}}};">{{{{subscriptionSecondaryCtaLabel}}}}</a>
                                </td>
                            </tr>
                        </table>

                        <p style="font-family: {{{{brandFont}}}}; font-size: 13px; color: {{{{brandSecondary}}}}; margin: 20px 0 0; text-align: center;">Questions? <a href="{{{{subscriptionHelpUrl}}}}" style="color: {{{{brandAccent}}}}; text-decoration: underline;">Contact Support</a></p>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
'''
    }


def section_wishlist_item():
    """Wishlist reminder product item with availability status."""
    return {
        "type": "wishlist_item",
        "name": "Wishlist Item",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 16px 24px;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="border: 1px solid {{{{brandSecondary}}}}20; border-radius: 8px;">
                <tr>
                    <td style="padding: 16px;">
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td width="120" valign="top">
                                    <img src="{IMAGE_PLACEHOLDERS['product']}" alt="{{{{wishlistItemAlt}}}}" width="100" height="100" style="display: block; border-radius: 4px;" />
                                </td>
                                <td style="padding-left: 16px;" valign="top">
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                                        <tr>
                                            <td>
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 0 0 4px; text-transform: uppercase; letter-spacing: 0.5px;">{{{{wishlistItemBrand}}}}</p>
                                                <h4 style="font-family: {{{{brandFont}}}}; font-size: 16px; color: {{{{brandPrimary}}}}; margin: 0 0 8px; font-weight: 600;">{{{{wishlistItemName}}}}</h4>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 18px; color: {{{{brandPrimary}}}}; margin: 0 0 8px; font-weight: 700;">{{{{wishlistItemPrice}}}}</p>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: {{{{wishlistItemStatusColor}}}}15; border-radius: 4px;">
                                                    <tr>
                                                        <td style="padding: 4px 10px;">
                                                            <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{wishlistItemStatusColor}}}}; margin: 0; font-weight: 600;">{{{{wishlistItemStatus}}}}</p>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td style="padding-top: 12px;">
                                                <a href="{{{{wishlistItemUrl}}}}" style="display: inline-block; padding: 10px 20px; background-color: {{{{brandAccent}}}}; color: #ffffff; font-family: {{{{brandFont}}}}; font-size: 14px; font-weight: 600; text-decoration: none; border-radius: 6px;">View Item</a>
                                            </td>
                                        </tr>
                                    </table>
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


def section_price_alert():
    """Price drop alert section showing original and new price."""
    return {
        "type": "price_alert",
        "name": "Price Alert",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="border: 2px solid {{{{brandAccent}}}}; border-radius: 12px; overflow: hidden;">
                <!-- Alert header -->
                <tr>
                    <td style="background-color: {{{{brandAccent}}}}; padding: 12px 20px;">
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: #ffffff; margin: 0; font-weight: 700;">🔔 PRICE DROP ALERT</p>
                                </td>
                                <td align="right">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: #ffffff; margin: 0; font-weight: 600;">{{{{priceAlertSavings}}}} OFF</p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <!-- Product details -->
                <tr>
                    <td style="padding: 20px;">
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td width="140" valign="top">
                                    <img src="{IMAGE_PLACEHOLDERS['product']}" alt="{{{{priceAlertItemAlt}}}}" width="120" height="120" style="display: block; border-radius: 8px;" />
                                </td>
                                <td style="padding-left: 20px;" valign="top">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 0 0 4px; text-transform: uppercase; letter-spacing: 0.5px;">{{{{priceAlertItemBrand}}}}</p>
                                    <h3 style="font-family: {{{{brandFont}}}}; font-size: 18px; color: {{{{brandPrimary}}}}; margin: 0 0 12px; font-weight: 600;">{{{{priceAlertItemName}}}}</h3>

                                    <!-- Price comparison -->
                                    <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-bottom: 16px;">
                                        <tr>
                                            <td style="padding-right: 12px;">
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 0; text-decoration: line-through;">{{{{priceAlertOriginalPrice}}}}</p>
                                            </td>
                                            <td>
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 24px; color: {{{{brandAccent}}}}; margin: 0; font-weight: 700;">{{{{priceAlertNewPrice}}}}</p>
                                            </td>
                                        </tr>
                                    </table>

                                    <a href="{{{{priceAlertItemUrl}}}}" style="display: inline-block; padding: 12px 24px; background-color: {{{{brandAccent}}}}; color: #ffffff; font-family: {{{{brandFont}}}}; font-size: 14px; font-weight: 600; text-decoration: none; border-radius: 6px;">Shop Now</a>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <!-- Urgency footer -->
                <tr>
                    <td style="background-color: {{{{brandSecondary}}}}08; padding: 12px 20px;">
                        <p style="font-family: {{{{brandFont}}}}; font-size: 13px; color: {{{{brandSecondary}}}}; margin: 0; text-align: center;">{{{{priceAlertUrgency}}}}</p>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
'''
    }


def section_invoice_details():
    """Invoice details section with line items, totals, and payment info."""
    return {
        "type": "invoice_details",
        "name": "Invoice Details",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <!-- Invoice header -->
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-bottom: 24px;">
                <tr>
                    <td>
                        <h2 style="font-family: {{{{brandFont}}}}; font-size: 24px; color: {{{{brandPrimary}}}}; margin: 0 0 8px; font-weight: 700;">INVOICE</h2>
                        <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 0;">Invoice #{{{{invoiceNumber}}}}</p>
                    </td>
                    <td align="right">
                        <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 0 0 4px;">Issue Date: {{{{invoiceDate}}}}</p>
                        <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 0;">Due Date: {{{{invoiceDueDate}}}}</p>
                    </td>
                </tr>
            </table>

            <!-- Billing info -->
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-bottom: 24px; border-top: 1px solid {{{{brandSecondary}}}}20; padding-top: 16px;">
                <tr>
                    <td width="50%" valign="top">
                        <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 0 0 8px; text-transform: uppercase; letter-spacing: 0.5px;">Bill To:</p>
                        <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}}; margin: 0 0 4px; font-weight: 600;">{{{{invoiceBillToName}}}}</p>
                        <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandText}}}}; margin: 0; line-height: 1.5;">{{{{invoiceBillToAddress}}}}</p>
                    </td>
                    <td width="50%" valign="top" align="right">
                        <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 0 0 8px; text-transform: uppercase; letter-spacing: 0.5px;">From:</p>
                        <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}}; margin: 0 0 4px; font-weight: 600;">{{{{companyName}}}}</p>
                        <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandText}}}}; margin: 0; line-height: 1.5;">{{{{companyAddress}}}}</p>
                    </td>
                </tr>
            </table>

            <!-- Line items table -->
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="border: 1px solid {{{{brandSecondary}}}}20; border-radius: 8px;">
                <!-- Header row -->
                <tr>
                    <td style="background-color: {{{{brandSecondary}}}}08; padding: 12px 16px; border-radius: 8px 0 0 0;">
                        <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 0; font-weight: 600; text-transform: uppercase;">Description</p>
                    </td>
                    <td width="80" align="center" style="background-color: {{{{brandSecondary}}}}08; padding: 12px 16px;">
                        <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 0; font-weight: 600; text-transform: uppercase;">Qty</p>
                    </td>
                    <td width="100" align="right" style="background-color: {{{{brandSecondary}}}}08; padding: 12px 16px;">
                        <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 0; font-weight: 600; text-transform: uppercase;">Rate</p>
                    </td>
                    <td width="100" align="right" style="background-color: {{{{brandSecondary}}}}08; padding: 12px 16px; border-radius: 0 8px 0 0;">
                        <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 0; font-weight: 600; text-transform: uppercase;">Amount</p>
                    </td>
                </tr>
                <!-- Line item 1 -->
                <tr>
                    <td style="padding: 16px; border-top: 1px solid {{{{brandSecondary}}}}10;">
                        <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}}; margin: 0 0 4px; font-weight: 500;">{{{{invoiceItem1Name}}}}</p>
                        <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 0;">{{{{invoiceItem1Description}}}}</p>
                    </td>
                    <td align="center" style="padding: 16px; border-top: 1px solid {{{{brandSecondary}}}}10;">
                        <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandText}}}}; margin: 0;">{{{{invoiceItem1Qty}}}}</p>
                    </td>
                    <td align="right" style="padding: 16px; border-top: 1px solid {{{{brandSecondary}}}}10;">
                        <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandText}}}}; margin: 0;">{{{{invoiceItem1Rate}}}}</p>
                    </td>
                    <td align="right" style="padding: 16px; border-top: 1px solid {{{{brandSecondary}}}}10;">
                        <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}}; margin: 0; font-weight: 600;">{{{{invoiceItem1Amount}}}}</p>
                    </td>
                </tr>
                <!-- Line item 2 -->
                <tr>
                    <td style="padding: 16px; border-top: 1px solid {{{{brandSecondary}}}}10;">
                        <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}}; margin: 0 0 4px; font-weight: 500;">{{{{invoiceItem2Name}}}}</p>
                        <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 0;">{{{{invoiceItem2Description}}}}</p>
                    </td>
                    <td align="center" style="padding: 16px; border-top: 1px solid {{{{brandSecondary}}}}10;">
                        <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandText}}}}; margin: 0;">{{{{invoiceItem2Qty}}}}</p>
                    </td>
                    <td align="right" style="padding: 16px; border-top: 1px solid {{{{brandSecondary}}}}10;">
                        <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandText}}}}; margin: 0;">{{{{invoiceItem2Rate}}}}</p>
                    </td>
                    <td align="right" style="padding: 16px; border-top: 1px solid {{{{brandSecondary}}}}10;">
                        <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}}; margin: 0; font-weight: 600;">{{{{invoiceItem2Amount}}}}</p>
                    </td>
                </tr>
            </table>

            <!-- Totals -->
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-top: 16px;">
                <tr>
                    <td width="60%"></td>
                    <td width="40%">
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td style="padding: 8px 0;">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 0;">Subtotal</p>
                                </td>
                                <td align="right" style="padding: 8px 0;">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandText}}}}; margin: 0;">{{{{invoiceSubtotal}}}}</p>
                                </td>
                            </tr>
                            <tr>
                                <td style="padding: 8px 0;">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 0;">Tax ({{{{invoiceTaxRate}}}})</p>
                                </td>
                                <td align="right" style="padding: 8px 0;">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandText}}}}; margin: 0;">{{{{invoiceTax}}}}</p>
                                </td>
                            </tr>
                            <tr>
                                <td style="padding: 12px 0; border-top: 2px solid {{{{brandPrimary}}}};">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 16px; color: {{{{brandPrimary}}}}; margin: 0; font-weight: 700;">Total Due</p>
                                </td>
                                <td align="right" style="padding: 12px 0; border-top: 2px solid {{{{brandPrimary}}}};">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 18px; color: {{{{brandPrimary}}}}; margin: 0; font-weight: 700;">{{{{invoiceTotal}}}}</p>
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


def section_receipt_summary():
    """Receipt summary section with transaction details and payment confirmation."""
    return {
        "type": "receipt_summary",
        "name": "Receipt Summary",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <!-- Receipt header with checkmark -->
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-bottom: 24px;">
                <tr>
                    <td align="center">
                        <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: #22c55e20; border-radius: 50%; width: 64px; height: 64px;">
                            <tr>
                                <td align="center" valign="middle" style="height: 64px;">
                                    <p style="font-size: 32px; margin: 0;">✓</p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td align="center" style="padding-top: 16px;">
                        <h2 style="font-family: {{{{brandFont}}}}; font-size: 24px; color: {{{{brandPrimary}}}}; margin: 0 0 8px; font-weight: 700;">Payment Successful</h2>
                        <p style="font-family: {{{{brandFont}}}}; font-size: 16px; color: {{{{brandSecondary}}}}; margin: 0;">Receipt #{{{{receiptNumber}}}}</p>
                    </td>
                </tr>
            </table>

            <!-- Amount paid highlight -->
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: {{{{brandAccent}}}}08; border-radius: 12px; margin-bottom: 24px;">
                <tr>
                    <td align="center" style="padding: 24px;">
                        <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 0 0 8px; text-transform: uppercase; letter-spacing: 0.5px;">Amount Paid</p>
                        <p style="font-family: {{{{brandFont}}}}; font-size: 36px; color: {{{{brandPrimary}}}}; margin: 0; font-weight: 700;">{{{{receiptAmount}}}}</p>
                    </td>
                </tr>
            </table>

            <!-- Transaction details -->
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="border: 1px solid {{{{brandSecondary}}}}20; border-radius: 8px;">
                <tr>
                    <td style="padding: 16px; border-bottom: 1px solid {{{{brandSecondary}}}}10;">
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 0;">Transaction ID</p>
                                </td>
                                <td align="right">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}}; margin: 0; font-weight: 500;">{{{{receiptTransactionId}}}}</p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td style="padding: 16px; border-bottom: 1px solid {{{{brandSecondary}}}}10;">
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 0;">Date & Time</p>
                                </td>
                                <td align="right">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}}; margin: 0; font-weight: 500;">{{{{receiptDateTime}}}}</p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td style="padding: 16px; border-bottom: 1px solid {{{{brandSecondary}}}}10;">
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 0;">Payment Method</p>
                                </td>
                                <td align="right">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}}; margin: 0; font-weight: 500;">{{{{receiptPaymentMethod}}}}</p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td style="padding: 16px;">
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 0;">Billed To</p>
                                </td>
                                <td align="right">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}}; margin: 0; font-weight: 500;">{{{{receiptBilledTo}}}}</p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>

            <!-- Items breakdown -->
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-top: 24px;">
                <tr>
                    <td>
                        <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 0 0 12px; text-transform: uppercase; letter-spacing: 0.5px; font-weight: 600;">Items</p>
                    </td>
                </tr>
                <tr>
                    <td style="padding: 12px 0; border-bottom: 1px solid {{{{brandSecondary}}}}10;">
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}}; margin: 0;">{{{{receiptItem1Name}}}}</p>
                                </td>
                                <td align="right">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandText}}}}; margin: 0;">{{{{receiptItem1Price}}}}</p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td style="padding: 12px 0; border-bottom: 1px solid {{{{brandSecondary}}}}10;">
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}}; margin: 0;">{{{{receiptItem2Name}}}}</p>
                                </td>
                                <td align="right">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandText}}}}; margin: 0;">{{{{receiptItem2Price}}}}</p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td style="padding: 12px 0;">
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}}; margin: 0; font-weight: 700;">Total</p>
                                </td>
                                <td align="right">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 16px; color: {{{{brandPrimary}}}}; margin: 0; font-weight: 700;">{{{{receiptTotal}}}}</p>
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


def section_delivery_confirmation():
    """Delivery confirmation section with delivery details and signature."""
    return {
        "type": "delivery_confirmation",
        "name": "Delivery Confirmation",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <!-- Delivery success header -->
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: #22c55e10; border-radius: 12px; margin-bottom: 24px;">
                <tr>
                    <td align="center" style="padding: 32px 24px;">
                        <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-bottom: 16px;">
                            <tr>
                                <td>
                                    <p style="font-size: 48px; margin: 0;">📦</p>
                                </td>
                            </tr>
                        </table>
                        <h2 style="font-family: {{{{brandFont}}}}; font-size: 24px; color: #22c55e; margin: 0 0 8px; font-weight: 700;">Delivered!</h2>
                        <p style="font-family: {{{{brandFont}}}}; font-size: 16px; color: {{{{brandSecondary}}}}; margin: 0;">Your package has arrived</p>
                    </td>
                </tr>
            </table>

            <!-- Delivery details card -->
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="border: 1px solid {{{{brandSecondary}}}}20; border-radius: 12px; margin-bottom: 24px;">
                <tr>
                    <td style="background-color: {{{{brandSecondary}}}}05; padding: 16px 20px; border-radius: 12px 12px 0 0;">
                        <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 0; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;">Delivery Details</p>
                    </td>
                </tr>
                <tr>
                    <td style="padding: 20px;">
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td style="padding-bottom: 16px;">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 0 0 4px; text-transform: uppercase;">Delivered To</p>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}}; margin: 0; font-weight: 500;">{{{{deliveryAddress}}}}</p>
                                </td>
                            </tr>
                            <tr>
                                <td style="padding-bottom: 16px;">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 0 0 4px; text-transform: uppercase;">Delivery Date & Time</p>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}}; margin: 0; font-weight: 500;">{{{{deliveryDateTime}}}}</p>
                                </td>
                            </tr>
                            <tr>
                                <td style="padding-bottom: 16px;">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 0 0 4px; text-transform: uppercase;">Signed By</p>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}}; margin: 0; font-weight: 500;">{{{{deliverySignedBy}}}}</p>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 0 0 4px; text-transform: uppercase;">Tracking Number</p>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandAccent}}}}; margin: 0; font-weight: 500;">{{{{deliveryTrackingNumber}}}}</p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>

            <!-- Delivery photo placeholder -->
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-bottom: 24px;">
                <tr>
                    <td>
                        <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 0 0 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;">Proof of Delivery</p>
                    </td>
                </tr>
                <tr>
                    <td>
                        <img src="{IMAGE_PLACEHOLDERS['product']}" alt="Delivery photo" width="300" style="display: block; border-radius: 8px; max-width: 100%;" />
                    </td>
                </tr>
            </table>

            <!-- Order summary -->
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="border: 1px solid {{{{brandSecondary}}}}20; border-radius: 8px;">
                <tr>
                    <td style="background-color: {{{{brandSecondary}}}}05; padding: 12px 16px; border-radius: 8px 8px 0 0;">
                        <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 0; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;">Order Summary</p>
                    </td>
                </tr>
                <tr>
                    <td style="padding: 16px;">
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 0;">Order Number</p>
                                </td>
                                <td align="right">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}}; margin: 0; font-weight: 500;">{{{{deliveryOrderNumber}}}}</p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td style="padding: 0 16px 16px;">
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 0;">Items Delivered</p>
                                </td>
                                <td align="right">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}}; margin: 0; font-weight: 500;">{{{{deliveryItemCount}}}} item(s)</p>
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


def section_back_in_stock():
    """Back-in-stock notification section with product details and quick-buy option."""
    return {
        "type": "back_in_stock",
        "name": "Back In Stock",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <!-- Back in stock banner -->
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-bottom: 20px;">
                <tr>
                    <td align="center" style="background: linear-gradient(135deg, {{{{brandAccent}}}}20 0%, {{{{brandPrimary}}}}10 100%); padding: 16px; border-radius: 8px;">
                        <p style="font-family: {{{{brandFont}}}}; font-size: 16px; color: {{{{brandAccent}}}}; margin: 0; font-weight: 700;">✨ BACK IN STOCK ✨</p>
                    </td>
                </tr>
            </table>

            <!-- Product card -->
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="border: 1px solid {{{{brandSecondary}}}}20; border-radius: 12px;">
                <tr>
                    <td style="padding: 24px;">
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td align="center" style="padding-bottom: 20px;">
                                    <img src="{IMAGE_PLACEHOLDERS['product']}" alt="{{{{backInStockItemAlt}}}}" width="200" height="200" style="display: block; border-radius: 8px;" />
                                </td>
                            </tr>
                            <tr>
                                <td align="center">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 0 0 8px; text-transform: uppercase; letter-spacing: 1px;">{{{{backInStockItemBrand}}}}</p>
                                    <h3 style="font-family: {{{{brandFont}}}}; font-size: 22px; color: {{{{brandPrimary}}}}; margin: 0 0 12px; font-weight: 600;">{{{{backInStockItemName}}}}</h3>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 20px; color: {{{{brandPrimary}}}}; margin: 0 0 20px; font-weight: 700;">{{{{backInStockItemPrice}}}}</p>
                                </td>
                            </tr>
                            <tr>
                                <td align="center">
                                    <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: #22c55e15; border-radius: 20px; margin-bottom: 20px;">
                                        <tr>
                                            <td style="padding: 8px 16px;">
                                                <table cellpadding="0" cellspacing="0" border="0" role="presentation">
                                                    <tr>
                                                        <td style="padding-right: 6px;">
                                                            <table width="8" height="8" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: #22c55e; border-radius: 50%;">
                                                                <tr><td></td></tr>
                                                            </table>
                                                        </td>
                                                        <td>
                                                            <p style="font-family: {{{{brandFont}}}}; font-size: 13px; color: #22c55e; margin: 0; font-weight: 600;">{{{{backInStockQuantity}}}} items available</p>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            <tr>
                                <td align="center">
                                    <a href="{{{{backInStockItemUrl}}}}" style="display: inline-block; padding: 14px 32px; background-color: {{{{brandAccent}}}}; color: #ffffff; font-family: {{{{brandFont}}}}; font-size: 16px; font-weight: 600; text-decoration: none; border-radius: 8px;">Buy Now</a>
                                </td>
                            </tr>
                            <tr>
                                <td align="center" style="padding-top: 16px;">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 13px; color: {{{{brandSecondary}}}}; margin: 0;">{{{{backInStockMessage}}}}</p>
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


def section_appointment_reminder():
    """Appointment reminder with date, time, location, and calendar options."""
    return {
        "type": "appointment_reminder",
        "name": "Appointment Reminder",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: {{{{brandAccent}}}}10; border-radius: 12px; border: 1px solid {{{{brandAccent}}}}20;">
                <tr>
                    <td style="padding: 32px;">
                        <!-- Header with calendar icon -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td align="center" style="padding-bottom: 20px;">
                                    <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: {{{{brandAccent}}}}; border-radius: 12px;">
                                        <tr>
                                            <td style="padding: 16px;">
                                                <img src="{IMAGE_PLACEHOLDERS['icon']}" alt="Calendar" width="32" height="32" style="display: block;" />
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            <tr>
                                <td align="center">
                                    <h2 style="font-family: {{{{brandFont}}}}; font-size: 24px; color: {{{{brandPrimary}}}}; margin: 0 0 8px;">{{{{appointmentTitle}}}}</h2>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 16px; color: {{{{brandSecondary}}}}; margin: 0;">{{{{appointmentMessage}}}}</p>
                                </td>
                            </tr>
                        </table>

                        <!-- Date and Time -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-top: 24px;">
                            <tr>
                                <td align="center">
                                    <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: #ffffff; border-radius: 8px; width: 100%;">
                                        <tr>
                                            <td style="padding: 20px; border-bottom: 1px solid {{{{brandSecondary}}}}15;">
                                                <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                                                    <tr>
                                                        <td width="40" valign="top">
                                                            <p style="font-size: 20px; margin: 0;">📅</p>
                                                        </td>
                                                        <td valign="top">
                                                            <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 0 0 4px; text-transform: uppercase; letter-spacing: 0.5px;">Date</p>
                                                            <p style="font-family: {{{{brandFont}}}}; font-size: 18px; color: {{{{brandPrimary}}}}; margin: 0; font-weight: 600;">{{{{appointmentDate}}}}</p>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td style="padding: 20px; border-bottom: 1px solid {{{{brandSecondary}}}}15;">
                                                <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                                                    <tr>
                                                        <td width="40" valign="top">
                                                            <p style="font-size: 20px; margin: 0;">⏰</p>
                                                        </td>
                                                        <td valign="top">
                                                            <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 0 0 4px; text-transform: uppercase; letter-spacing: 0.5px;">Time</p>
                                                            <p style="font-family: {{{{brandFont}}}}; font-size: 18px; color: {{{{brandPrimary}}}}; margin: 0; font-weight: 600;">{{{{appointmentTime}}}}</p>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td style="padding: 20px;">
                                                <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                                                    <tr>
                                                        <td width="40" valign="top">
                                                            <p style="font-size: 20px; margin: 0;">📍</p>
                                                        </td>
                                                        <td valign="top">
                                                            <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 0 0 4px; text-transform: uppercase; letter-spacing: 0.5px;">Location</p>
                                                            <p style="font-family: {{{{brandFont}}}}; font-size: 16px; color: {{{{brandPrimary}}}}; margin: 0;">{{{{appointmentLocation}}}}</p>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>

                        <!-- Action buttons -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-top: 24px;">
                            <tr>
                                <td align="center">
                                    <a href="{{{{addToCalendarUrl}}}}" style="display: inline-block; padding: 14px 28px; background-color: {{{{brandAccent}}}}; color: #ffffff; font-family: {{{{brandFont}}}}; font-size: 14px; font-weight: 600; text-decoration: none; border-radius: 8px; margin-right: 12px;">Add to Calendar</a>
                                    <a href="{{{{rescheduleUrl}}}}" style="display: inline-block; padding: 14px 28px; background-color: transparent; color: {{{{brandAccent}}}}; font-family: {{{{brandFont}}}}; font-size: 14px; font-weight: 600; text-decoration: none; border-radius: 8px; border: 2px solid {{{{brandAccent}}}};">Reschedule</a>
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


def section_two_factor_code():
    """Two-factor authentication code display with security info."""
    return {
        "type": "two_factor_code",
        "name": "Two Factor Code",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: {{{{brandSecondary}}}}05; border-radius: 12px;">
                <tr>
                    <td style="padding: 32px;">
                        <!-- Security badge -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td align="center" style="padding-bottom: 24px;">
                                    <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: #22c55e20; border-radius: 50%;">
                                        <tr>
                                            <td style="padding: 20px;">
                                                <img src="{IMAGE_PLACEHOLDERS['icon']}" alt="Security Shield" width="40" height="40" style="display: block;" />
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            <tr>
                                <td align="center">
                                    <h2 style="font-family: {{{{brandFont}}}}; font-size: 22px; color: {{{{brandPrimary}}}}; margin: 0 0 8px;">Two-Factor Authentication</h2>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 15px; color: {{{{brandSecondary}}}}; margin: 0;">Enter this code to verify your identity</p>
                                </td>
                            </tr>
                        </table>

                        <!-- 2FA Code Display -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-top: 24px;">
                            <tr>
                                <td align="center">
                                    <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: #ffffff; border: 2px solid {{{{brandPrimary}}}}; border-radius: 12px;">
                                        <tr>
                                            <td style="padding: 24px 48px;">
                                                <p style="font-family: 'SF Mono', 'Monaco', 'Consolas', monospace; font-size: 42px; color: {{{{brandPrimary}}}}; margin: 0; font-weight: 700; letter-spacing: 12px;">{{{{twoFactorCode}}}}</p>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>

                        <!-- Expiry and info -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-top: 20px;">
                            <tr>
                                <td align="center">
                                    <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: #f59e0b15; border-radius: 8px;">
                                        <tr>
                                            <td style="padding: 12px 20px;">
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 13px; color: #f59e0b; margin: 0; font-weight: 600;">⏱ Code expires in {{{{twoFactorExpiry}}}}</p>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>

                        <!-- Security notice -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-top: 24px;">
                            <tr>
                                <td align="center" style="border-top: 1px solid {{{{brandSecondary}}}}15; padding-top: 24px;">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 13px; color: {{{{brandSecondary}}}}; margin: 0 0 4px;">🔒 If you didn't request this code, please ignore this email.</p>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 13px; color: {{{{brandSecondary}}}}; margin: 0;">Never share this code with anyone.</p>
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


def section_account_suspended():
    """Account suspended notification with reason and appeal options."""
    return {
        "type": "account_suspended",
        "name": "Account Suspended",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: #ef444415; border-radius: 12px; border: 1px solid #ef444430;">
                <tr>
                    <td style="padding: 32px;">
                        <!-- Warning icon -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td align="center" style="padding-bottom: 20px;">
                                    <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: #ef4444; border-radius: 50%;">
                                        <tr>
                                            <td style="padding: 16px;">
                                                <p style="font-size: 28px; margin: 0; line-height: 1;">⚠️</p>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            <tr>
                                <td align="center">
                                    <h2 style="font-family: {{{{brandFont}}}}; font-size: 24px; color: #ef4444; margin: 0 0 8px;">Account Suspended</h2>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 15px; color: {{{{brandSecondary}}}}; margin: 0;">Your account has been temporarily suspended</p>
                                </td>
                            </tr>
                        </table>

                        <!-- Reason box -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-top: 24px;">
                            <tr>
                                <td>
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: #ffffff; border-radius: 8px;">
                                        <tr>
                                            <td style="padding: 20px;">
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 0 0 8px; text-transform: uppercase; letter-spacing: 0.5px; font-weight: 600;">Reason for Suspension</p>
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 15px; color: {{{{brandPrimary}}}}; margin: 0; line-height: 1.6;">{{{{suspensionReason}}}}</p>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>

                        <!-- Account details -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-top: 16px;">
                            <tr>
                                <td>
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: #ffffff; border-radius: 8px;">
                                        <tr>
                                            <td style="padding: 16px 20px; border-bottom: 1px solid {{{{brandSecondary}}}}10;">
                                                <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                                                    <tr>
                                                        <td style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}};">Account</td>
                                                        <td align="right" style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}}; font-weight: 500;">{{{{suspendedEmail}}}}</td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td style="padding: 16px 20px;">
                                                <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                                                    <tr>
                                                        <td style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}};">Suspended on</td>
                                                        <td align="right" style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}}; font-weight: 500;">{{{{suspensionDate}}}}</td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>

                        <!-- Action buttons -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-top: 24px;">
                            <tr>
                                <td align="center">
                                    <a href="{{{{appealUrl}}}}" style="display: inline-block; padding: 14px 32px; background-color: {{{{brandPrimary}}}}; color: #ffffff; font-family: {{{{brandFont}}}}; font-size: 14px; font-weight: 600; text-decoration: none; border-radius: 8px;">Appeal This Decision</a>
                                </td>
                            </tr>
                            <tr>
                                <td align="center" style="padding-top: 16px;">
                                    <a href="{{{{policyUrl}}}}" style="font-family: {{{{brandFont}}}}; font-size: 13px; color: {{{{brandSecondary}}}}; text-decoration: underline;">Review our Terms of Service</a>
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


def section_order_hold():
    """Order hold notification with reason and action items."""
    return {
        "type": "order_hold",
        "name": "Order Hold",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: #fbbf2410; border-radius: 12px; border: 1px solid #fbbf2425;">
                <tr>
                    <td style="padding: 32px;">
                        <!-- Alert header -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td align="center" style="padding-bottom: 20px;">
                                    <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: #fbbf24; border-radius: 12px;">
                                        <tr>
                                            <td style="padding: 14px;">
                                                <p style="font-size: 24px; margin: 0; line-height: 1;">⏸️</p>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            <tr>
                                <td align="center">
                                    <h2 style="font-family: {{{{brandFont}}}}; font-size: 24px; color: #fbbf24; margin: 0 0 8px;">Order On Hold</h2>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 15px; color: {{{{brandSecondary}}}}; margin: 0;">We need a bit more information to process your order</p>
                                </td>
                            </tr>
                        </table>

                        <!-- Order details -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-top: 24px;">
                            <tr>
                                <td>
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: #ffffff; border-radius: 8px;">
                                        <tr>
                                            <td style="padding: 16px 20px; border-bottom: 1px solid {{{{brandSecondary}}}}10;">
                                                <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                                                    <tr>
                                                        <td style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}};">Order Number</td>
                                                        <td align="right" style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}}; font-weight: 600;">{{{{orderNumber}}}}</td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td style="padding: 16px 20px; border-bottom: 1px solid {{{{brandSecondary}}}}10;">
                                                <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                                                    <tr>
                                                        <td style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}};">Order Date</td>
                                                        <td align="right" style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}};">{{{{orderDate}}}}</td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td style="padding: 16px 20px;">
                                                <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                                                    <tr>
                                                        <td style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}};">Hold Reason</td>
                                                        <td align="right" style="font-family: {{{{brandFont}}}}; font-size: 14px; color: #fbbf24; font-weight: 500;">{{{{holdReason}}}}</td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>

                        <!-- Action required -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-top: 20px;">
                            <tr>
                                <td>
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: {{{{brandSecondary}}}}05; border-radius: 8px;">
                                        <tr>
                                            <td style="padding: 16px 20px;">
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 13px; color: {{{{brandSecondary}}}}; margin: 0 0 8px; font-weight: 600;">Action Required</p>
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 13px; color: {{{{brandSecondary}}}}; margin: 0; line-height: 1.5;">{{{{holdActionRequired}}}}</p>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>

                        <!-- Deadline warning -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-top: 16px;">
                            <tr>
                                <td align="center">
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 13px; color: #ef4444; margin: 0;">⚠️ Please respond by {{{{holdDeadline}}}} to avoid cancellation</p>
                                </td>
                            </tr>
                        </table>

                        <!-- Action buttons -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-top: 24px;">
                            <tr>
                                <td align="center">
                                    <a href="{{{{resolveHoldUrl}}}}" style="display: inline-block; padding: 14px 32px; background-color: {{{{brandAccent}}}}; color: #ffffff; font-family: {{{{brandFont}}}}; font-size: 14px; font-weight: 600; text-decoration: none; border-radius: 8px;">Resolve Now</a>
                                </td>
                            </tr>
                            <tr>
                                <td align="center" style="padding-top: 16px;">
                                    <a href="{{{{cancelOrderUrl}}}}" style="font-family: {{{{brandFont}}}}; font-size: 13px; color: {{{{brandSecondary}}}}; text-decoration: underline;">Cancel this order</a>
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


def section_subscription_paused():
    """Subscription paused status notification with reactivation option."""
    return {
        "type": "subscription_paused",
        "name": "Subscription Paused",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: {{{{brandSecondary}}}}08; border-radius: 12px; border: 1px solid {{{{brandSecondary}}}}15;">
                <tr>
                    <td style="padding: 32px;">
                        <!-- Header -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td align="center" style="padding-bottom: 20px;">
                                    <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: {{{{brandSecondary}}}}; border-radius: 12px;">
                                        <tr>
                                            <td style="padding: 14px;">
                                                <p style="font-size: 24px; margin: 0; line-height: 1;">⏸️</p>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            <tr>
                                <td align="center">
                                    <h2 style="font-family: {{{{brandFont}}}}; font-size: 24px; color: {{{{brandPrimary}}}}; margin: 0 0 8px;">Subscription Paused</h2>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 15px; color: {{{{brandSecondary}}}}; margin: 0;">Your subscription has been paused as requested</p>
                                </td>
                            </tr>
                        </table>

                        <!-- Subscription details -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-top: 24px;">
                            <tr>
                                <td>
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: #ffffff; border-radius: 8px;">
                                        <tr>
                                            <td style="padding: 16px 20px; border-bottom: 1px solid {{{{brandSecondary}}}}10;">
                                                <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                                                    <tr>
                                                        <td style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}};">Plan</td>
                                                        <td align="right" style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}}; font-weight: 600;">{{{{subscriptionPlan}}}}</td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td style="padding: 16px 20px; border-bottom: 1px solid {{{{brandSecondary}}}}10;">
                                                <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                                                    <tr>
                                                        <td style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}};">Paused on</td>
                                                        <td align="right" style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}};">{{{{pauseDate}}}}</td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td style="padding: 16px 20px; border-bottom: 1px solid {{{{brandSecondary}}}}10;">
                                                <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                                                    <tr>
                                                        <td style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}};">Resume date</td>
                                                        <td align="right" style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}};">{{{{resumeDate}}}}</td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td style="padding: 16px 20px;">
                                                <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                                                    <tr>
                                                        <td style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}};">Status</td>
                                                        <td align="right">
                                                            <span style="display: inline-block; padding: 4px 12px; background-color: {{{{brandSecondary}}}}15; border-radius: 12px; font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; font-weight: 600;">PAUSED</span>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>

                        <!-- What you'll miss -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-top: 20px;">
                            <tr>
                                <td>
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: #ffffff; border-radius: 8px; border: 1px dashed {{{{brandSecondary}}}}30;">
                                        <tr>
                                            <td style="padding: 16px 20px;">
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 13px; color: {{{{brandSecondary}}}}; margin: 0 0 8px; font-weight: 600;">While paused, you won't have access to:</p>
                                                <ul style="font-family: {{{{brandFont}}}}; font-size: 13px; color: {{{{brandSecondary}}}}; margin: 0; padding-left: 20px; line-height: 1.8;">
                                                    <li>{{{{pausedFeature1}}}}</li>
                                                    <li>{{{{pausedFeature2}}}}</li>
                                                    <li>{{{{pausedFeature3}}}}</li>
                                                </ul>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>

                        <!-- Action buttons -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-top: 24px;">
                            <tr>
                                <td align="center">
                                    <a href="{{{{resumeNowUrl}}}}" style="display: inline-block; padding: 14px 32px; background-color: {{{{brandAccent}}}}; color: #ffffff; font-family: {{{{brandFont}}}}; font-size: 14px; font-weight: 600; text-decoration: none; border-radius: 8px;">Resume Subscription</a>
                                </td>
                            </tr>
                            <tr>
                                <td align="center" style="padding-top: 16px;">
                                    <a href="{{{{manageSubscriptionUrl}}}}" style="font-family: {{{{brandFont}}}}; font-size: 13px; color: {{{{brandSecondary}}}}; text-decoration: underline;">Manage subscription settings</a>
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


def section_referral_success():
    """Referral success notification with reward earned details."""
    return {
        "type": "referral_success",
        "name": "Referral Success",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: #10b98110; border-radius: 12px; border: 1px solid #10b98125;">
                <tr>
                    <td style="padding: 32px;">
                        <!-- Success header -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td align="center" style="padding-bottom: 20px;">
                                    <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: #10b981; border-radius: 50%;">
                                        <tr>
                                            <td style="padding: 16px;">
                                                <p style="font-size: 32px; margin: 0; line-height: 1;">🎉</p>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            <tr>
                                <td align="center">
                                    <h2 style="font-family: {{{{brandFont}}}}; font-size: 28px; color: #10b981; margin: 0 0 8px;">Referral Successful!</h2>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 16px; color: {{{{brandSecondary}}}}; margin: 0;">{{{{referredFriendName}}}} has joined thanks to you</p>
                                </td>
                            </tr>
                        </table>

                        <!-- Reward earned -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-top: 24px;">
                            <tr>
                                <td>
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: #ffffff; border-radius: 12px; overflow: hidden;">
                                        <tr>
                                            <td style="background-color: #10b981; padding: 12px 20px;">
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: #ffffff; margin: 0; text-transform: uppercase; font-weight: 600; letter-spacing: 1px;">Your Reward</p>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td align="center" style="padding: 24px;">
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 48px; color: {{{{brandPrimary}}}}; margin: 0; font-weight: 700;">{{{{referralReward}}}}</p>
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}}; margin: 8px 0 0;">{{{{referralRewardType}}}}</p>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>

                        <!-- Stats -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-top: 20px;">
                            <tr>
                                <td>
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: #ffffff; border-radius: 8px;">
                                        <tr>
                                            <td width="50%" align="center" style="padding: 20px; border-right: 1px solid {{{{brandSecondary}}}}10;">
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 32px; color: {{{{brandPrimary}}}}; margin: 0; font-weight: 700;">{{{{totalReferrals}}}}</p>
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 4px 0 0; text-transform: uppercase;">Total Referrals</p>
                                            </td>
                                            <td width="50%" align="center" style="padding: 20px;">
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 32px; color: #10b981; margin: 0; font-weight: 700;">{{{{totalEarned}}}}</p>
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 12px; color: {{{{brandSecondary}}}}; margin: 4px 0 0; text-transform: uppercase;">Total Earned</p>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>

                        <!-- Keep referring -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-top: 20px;">
                            <tr>
                                <td style="background-color: {{{{brandSecondary}}}}05; border-radius: 8px; padding: 16px 20px;">
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                                        <tr>
                                            <td>
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}}; margin: 0; font-weight: 600;">Keep the referrals coming!</p>
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 13px; color: {{{{brandSecondary}}}}; margin: 4px 0 0;">Share your unique link and earn {{{{referralRewardPerReferral}}}} for each friend who signs up.</p>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>

                        <!-- Share link -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-top: 16px;">
                            <tr>
                                <td>
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: #ffffff; border-radius: 8px; border: 1px solid {{{{brandSecondary}}}}20;">
                                        <tr>
                                            <td style="padding: 12px 16px;">
                                                <p style="font-family: monospace; font-size: 13px; color: {{{{brandAccent}}}}; margin: 0; word-break: break-all;">{{{{referralLink}}}}</p>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>

                        <!-- Action buttons -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-top: 24px;">
                            <tr>
                                <td align="center">
                                    <a href="{{{{shareReferralUrl}}}}" style="display: inline-block; padding: 14px 32px; background-color: {{{{brandAccent}}}}; color: #ffffff; font-family: {{{{brandFont}}}}; font-size: 14px; font-weight: 600; text-decoration: none; border-radius: 8px;">Share With More Friends</a>
                                </td>
                            </tr>
                            <tr>
                                <td align="center" style="padding-top: 16px;">
                                    <a href="{{{{viewRewardsUrl}}}}" style="font-family: {{{{brandFont}}}}; font-size: 13px; color: {{{{brandSecondary}}}}; text-decoration: underline;">View all rewards</a>
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


def section_payment_failed():
    """Payment failed notification with retry options and card info."""
    return {
        "type": "payment_failed",
        "name": "Payment Failed",
        "html": f'''
<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
    <tr>
        <td style="padding: 24px;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: #f59e0b10; border-radius: 12px; border: 1px solid #f59e0b25;">
                <tr>
                    <td style="padding: 32px;">
                        <!-- Alert header -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                            <tr>
                                <td align="center" style="padding-bottom: 20px;">
                                    <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: #f59e0b; border-radius: 12px;">
                                        <tr>
                                            <td style="padding: 14px;">
                                                <p style="font-size: 24px; margin: 0; line-height: 1;">💳</p>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            <tr>
                                <td align="center">
                                    <h2 style="font-family: {{{{brandFont}}}}; font-size: 24px; color: #f59e0b; margin: 0 0 8px;">Payment Failed</h2>
                                    <p style="font-family: {{{{brandFont}}}}; font-size: 15px; color: {{{{brandSecondary}}}}; margin: 0;">We couldn't process your payment</p>
                                </td>
                            </tr>
                        </table>

                        <!-- Payment details -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-top: 24px;">
                            <tr>
                                <td>
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: #ffffff; border-radius: 8px;">
                                        <tr>
                                            <td style="padding: 16px 20px; border-bottom: 1px solid {{{{brandSecondary}}}}10;">
                                                <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                                                    <tr>
                                                        <td style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}};">Amount</td>
                                                        <td align="right" style="font-family: {{{{brandFont}}}}; font-size: 16px; color: {{{{brandPrimary}}}}; font-weight: 600;">{{{{failedAmount}}}}</td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td style="padding: 16px 20px; border-bottom: 1px solid {{{{brandSecondary}}}}10;">
                                                <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                                                    <tr>
                                                        <td style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}};">Card ending in</td>
                                                        <td align="right" style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}}; font-weight: 500;">•••• {{{{cardLastFour}}}}</td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td style="padding: 16px 20px; border-bottom: 1px solid {{{{brandSecondary}}}}10;">
                                                <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                                                    <tr>
                                                        <td style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}};">Attempted on</td>
                                                        <td align="right" style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandPrimary}}}};">{{{{paymentDate}}}}</td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td style="padding: 16px 20px;">
                                                <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation">
                                                    <tr>
                                                        <td style="font-family: {{{{brandFont}}}}; font-size: 14px; color: {{{{brandSecondary}}}};">Reason</td>
                                                        <td align="right" style="font-family: {{{{brandFont}}}}; font-size: 14px; color: #ef4444; font-weight: 500;">{{{{failureReason}}}}</td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>

                        <!-- What happens next -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-top: 20px;">
                            <tr>
                                <td>
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="background-color: {{{{brandSecondary}}}}05; border-radius: 8px;">
                                        <tr>
                                            <td style="padding: 16px 20px;">
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 13px; color: {{{{brandSecondary}}}}; margin: 0 0 4px; font-weight: 600;">What happens next?</p>
                                                <p style="font-family: {{{{brandFont}}}}; font-size: 13px; color: {{{{brandSecondary}}}}; margin: 0; line-height: 1.5;">We'll automatically retry in {{{{retryDays}}}} days. To avoid service interruption, please update your payment method.</p>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>

                        <!-- Action buttons -->
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="margin-top: 24px;">
                            <tr>
                                <td align="center">
                                    <a href="{{{{updatePaymentUrl}}}}" style="display: inline-block; padding: 14px 32px; background-color: {{{{brandAccent}}}}; color: #ffffff; font-family: {{{{brandFont}}}}; font-size: 14px; font-weight: 600; text-decoration: none; border-radius: 8px; margin-right: 12px;">Update Payment Method</a>
                                    <a href="{{{{retryPaymentUrl}}}}" style="display: inline-block; padding: 14px 28px; background-color: transparent; color: {{{{brandAccent}}}}; font-family: {{{{brandFont}}}}; font-size: 14px; font-weight: 600; text-decoration: none; border-radius: 8px; border: 2px solid {{{{brandAccent}}}};">Retry Payment</a>
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
    "team_members": section_team_members,
    "comparison_table": section_comparison_table,
    "stats_metrics": section_stats_metrics,
    "rating_stars": section_rating_stars,
    "gallery_carousel": section_gallery_carousel,
    "multi_step_form": section_multi_step_form,
    "referral_program": section_referral_program,
    "loyalty_points": section_loyalty_points,
    "gift_card": section_gift_card,
    "subscription_renewal": section_subscription_renewal,
    "wishlist_item": section_wishlist_item,
    "price_alert": section_price_alert,
    "back_in_stock": section_back_in_stock,
    "invoice_details": section_invoice_details,
    "receipt_summary": section_receipt_summary,
    "delivery_confirmation": section_delivery_confirmation,
    "appointment_reminder": section_appointment_reminder,
    "two_factor_code": section_two_factor_code,
    "account_suspended": section_account_suspended,
    "payment_failed": section_payment_failed,
    "order_hold": section_order_hold,
    "subscription_paused": section_subscription_paused,
    "referral_success": section_referral_success,
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

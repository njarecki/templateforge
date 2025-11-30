"""
MJML Converter

Converts HTML email templates to MJML format for easier downstream editing.
MJML (Mailjet Markup Language) is an open-source framework for responsive emails.
"""

from design_system import IMAGE_PLACEHOLDERS, COPY_TOKENS, DESIGN_SKINS


def get_mjml_head(skin_name="apple_light"):
    """Generate MJML head section with styles and fonts."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''  <mj-head>
    <mj-title>{{{{emailSubject}}}}</mj-title>
    <mj-preview>{{{{preheader}}}}</mj-preview>
    <mj-attributes>
      <mj-all font-family="{skin['brandFont']}" />
      <mj-text font-size="16px" color="{skin['brandText']}" line-height="1.6" />
      <mj-button background-color="{skin['brandAccent']}" color="#ffffff" font-size="16px" font-weight="600" border-radius="8px" padding="16px 32px" />
      <mj-section background-color="{skin['brandBG']}" padding="24px" />
    </mj-attributes>
    <mj-style>
      .headline {{ font-size: 32px; line-height: 1.2; }}
      .subheadline {{ font-size: 18px; line-height: 1.4; }}
    </mj-style>
  </mj-head>'''


def section_to_mjml_hero(skin_name="apple_light"):
    """Convert hero section to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="0">
      <mj-column>
        <mj-image src="{IMAGE_PLACEHOLDERS['hero']}" alt="{{{{heroAlt}}}}" width="640px" />
      </mj-column>
    </mj-section>
    <mj-section padding="24px 24px 32px">
      <mj-column>
        <mj-text align="center" font-size="32px" color="{skin['brandPrimary']}" padding="0 0 16px">
          {COPY_TOKENS['headline']}
        </mj-text>
        <mj-text align="center" font-size="18px" color="{skin['brandSecondary']}" padding="0 0 24px">
          {COPY_TOKENS['subheadline']}
        </mj-text>
        <mj-button href="{{{{ctaUrl}}}}" background-color="{skin['brandAccent']}">
          {COPY_TOKENS['ctaLabel']}
        </mj-button>
      </mj-column>
    </mj-section>'''


def section_to_mjml_subhero(skin_name="apple_light"):
    """Convert subhero section to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column>
        <mj-image src="{IMAGE_PLACEHOLDERS['product']}" alt="{{{{imageAlt}}}}" width="300px" />
        <mj-text align="center" font-size="24px" color="{skin['brandPrimary']}" padding="16px 0 8px">
          {COPY_TOKENS['headline']}
        </mj-text>
        <mj-text align="center" color="{skin['brandText']}">
          {COPY_TOKENS['bodyText']}
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_1col_text(skin_name="apple_light"):
    """Convert single column text to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column>
        <mj-text font-size="24px" color="{skin['brandPrimary']}" padding="0 0 12px">
          {COPY_TOKENS['headline']}
        </mj-text>
        <mj-text color="{skin['brandText']}">
          {COPY_TOKENS['bodyText']}
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_2col_text_image(skin_name="apple_light"):
    """Convert two-column text/image to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column width="50%">
        <mj-text font-size="20px" color="{skin['brandPrimary']}" padding="0 12px 12px 0">
          {COPY_TOKENS['headline']}
        </mj-text>
        <mj-text font-size="14px" color="{skin['brandText']}" padding="0 12px 0 0">
          {COPY_TOKENS['bodyText']}
        </mj-text>
      </mj-column>
      <mj-column width="50%">
        <mj-image src="{IMAGE_PLACEHOLDERS['product']}" alt="{{{{imageAlt}}}}" />
      </mj-column>
    </mj-section>'''


def section_to_mjml_3col_features(skin_name="apple_light"):
    """Convert three-column features to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column width="33%">
        <mj-image src="{IMAGE_PLACEHOLDERS['icon']}" width="64px" align="center" />
        <mj-text align="center" font-size="16px" color="{skin['brandPrimary']}" padding="12px 8px 8px">
          {{{{feature1Title}}}}
        </mj-text>
        <mj-text align="center" font-size="14px" color="{skin['brandSecondary']}" padding="0 8px">
          {{{{feature1Text}}}}
        </mj-text>
      </mj-column>
      <mj-column width="33%">
        <mj-image src="{IMAGE_PLACEHOLDERS['icon']}" width="64px" align="center" />
        <mj-text align="center" font-size="16px" color="{skin['brandPrimary']}" padding="12px 8px 8px">
          {{{{feature2Title}}}}
        </mj-text>
        <mj-text align="center" font-size="14px" color="{skin['brandSecondary']}" padding="0 8px">
          {{{{feature2Text}}}}
        </mj-text>
      </mj-column>
      <mj-column width="33%">
        <mj-image src="{IMAGE_PLACEHOLDERS['icon']}" width="64px" align="center" />
        <mj-text align="center" font-size="16px" color="{skin['brandPrimary']}" padding="12px 8px 8px">
          {{{{feature3Title}}}}
        </mj-text>
        <mj-text align="center" font-size="14px" color="{skin['brandSecondary']}" padding="0 8px">
          {{{{feature3Text}}}}
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_product_grid(skin_name="apple_light"):
    """Convert product grid to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column width="50%">
        <mj-image src="{IMAGE_PLACEHOLDERS['product']}" alt="{{{{product1Alt}}}}" />
        <mj-text align="center" font-size="16px" color="{skin['brandPrimary']}" padding="12px 8px 4px">
          {{{{product1Name}}}}
        </mj-text>
        <mj-text align="center" font-size="14px" color="{skin['brandAccent']}" font-weight="600" padding="0 8px">
          {{{{product1Price}}}}
        </mj-text>
      </mj-column>
      <mj-column width="50%">
        <mj-image src="{IMAGE_PLACEHOLDERS['product']}" alt="{{{{product2Alt}}}}" />
        <mj-text align="center" font-size="16px" color="{skin['brandPrimary']}" padding="12px 8px 4px">
          {{{{product2Name}}}}
        </mj-text>
        <mj-text align="center" font-size="14px" color="{skin['brandAccent']}" font-weight="600" padding="0 8px">
          {{{{product2Price}}}}
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_testimonial(skin_name="apple_light"):
    """Convert testimonial to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="32px 24px" background-color="{skin['brandSecondary']}20">
      <mj-column>
        <mj-image src="{IMAGE_PLACEHOLDERS['avatar']}" width="80px" align="center" border-radius="50%" />
        <mj-text align="center" font-size="18px" font-style="italic" color="{skin['brandText']}" padding="16px 0 0">
          &ldquo;{COPY_TOKENS['testimonialQuote']}&rdquo;
        </mj-text>
        <mj-text align="center" font-size="14px" color="{skin['brandSecondary']}" font-weight="600" padding="12px 0 0">
          {COPY_TOKENS['testimonialAuthor']}
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_story_block(skin_name="apple_light"):
    """Convert story block to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column>
        <mj-image src="{IMAGE_PLACEHOLDERS['hero']}" alt="{{{{storyImageAlt}}}}" />
        <mj-text font-size="24px" color="{skin['brandPrimary']}" padding="16px 0 12px">
          {COPY_TOKENS['headline']}
        </mj-text>
        <mj-text color="{skin['brandText']}" padding="0 0 16px">
          {COPY_TOKENS['bodyText']}
        </mj-text>
        <mj-text>
          <a href="{{{{readMoreUrl}}}}" style="color: {skin['brandAccent']}; text-decoration: underline;">Read more &rarr;</a>
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_cta_band(skin_name="apple_light"):
    """Convert CTA band to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="32px 24px" background-color="{skin['brandAccent']}">
      <mj-column>
        <mj-text align="center" font-size="24px" color="#ffffff" padding="0 0 16px">
          {COPY_TOKENS['headline']}
        </mj-text>
        <mj-button href="{{{{ctaUrl}}}}" background-color="#ffffff" color="{skin['brandAccent']}">
          {COPY_TOKENS['ctaLabel']}
        </mj-button>
      </mj-column>
    </mj-section>'''


def section_to_mjml_header_nav(skin_name="apple_light"):
    """Convert header navigation to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="16px 24px">
      <mj-column width="40%">
        <mj-image src="{IMAGE_PLACEHOLDERS['logo']}" alt="{{{{brandName}}}}" width="150px" align="left" />
      </mj-column>
      <mj-column width="60%">
        <mj-text align="right" font-size="14px" color="{skin['brandText']}" css-class="mobile-hide">
          <a href="{{{{navLink1Url}}}}" style="color: {skin['brandText']}; text-decoration: none; margin-left: 24px;">{{{{navLink1}}}}</a>
          <a href="{{{{navLink2Url}}}}" style="color: {skin['brandText']}; text-decoration: none; margin-left: 24px;">{{{{navLink2}}}}</a>
          <a href="{{{{navLink3Url}}}}" style="color: {skin['brandText']}; text-decoration: none; margin-left: 24px;">{{{{navLink3}}}}</a>
        </mj-text>
      </mj-column>
    </mj-section>
    <mj-section padding="0">
      <mj-column>
        <mj-divider border-color="{skin['brandSecondary']}20" border-width="1px" />
      </mj-column>
    </mj-section>'''


def section_to_mjml_offer_banner(skin_name="apple_light"):
    """Convert offer banner to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="12px 24px" background-color="{skin['brandPrimary']}">
      <mj-column>
        <mj-text align="center" font-size="14px" color="{skin['brandBG']}">
          {{{{offerText}}}} &bull; <a href="{{{{offerUrl}}}}" style="color: {skin['brandAccent']}; text-decoration: underline;">Shop Now</a>
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_order_summary(skin_name="apple_light"):
    """Convert order summary to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column>
        <mj-text font-size="20px" color="{skin['brandPrimary']}" padding="0 0 16px" border-bottom="2px solid {skin['brandSecondary']}20">
          Order Summary
        </mj-text>
      </mj-column>
    </mj-section>
    <mj-section padding="0 24px">
      <mj-column width="20%">
        <mj-image src="{IMAGE_PLACEHOLDERS['icon']}" width="64px" />
      </mj-column>
      <mj-column width="50%">
        <mj-text font-size="14px" color="{skin['brandPrimary']}" font-weight="600">
          {{{{orderItem1Name}}}}
        </mj-text>
        <mj-text font-size="12px" color="{skin['brandSecondary']}" padding="4px 0 0">
          Qty: {{{{orderItem1Qty}}}}
        </mj-text>
      </mj-column>
      <mj-column width="30%">
        <mj-text align="right" font-size="14px" color="{skin['brandPrimary']}">
          {{{{orderItem1Price}}}}
        </mj-text>
      </mj-column>
    </mj-section>
    <mj-section padding="16px 24px">
      <mj-column>
        <mj-divider border-color="{skin['brandSecondary']}20" border-width="1px" />
      </mj-column>
    </mj-section>
    <mj-section padding="0 24px">
      <mj-column width="50%">
        <mj-text font-size="14px" color="{skin['brandSecondary']}">Subtotal</mj-text>
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="8px 0 0">Shipping</mj-text>
      </mj-column>
      <mj-column width="50%">
        <mj-text align="right" font-size="14px" color="{skin['brandPrimary']}">{{{{orderSubtotal}}}}</mj-text>
        <mj-text align="right" font-size="14px" color="{skin['brandPrimary']}" padding="8px 0 0">{{{{orderShipping}}}}</mj-text>
      </mj-column>
    </mj-section>
    <mj-section padding="12px 24px">
      <mj-column width="50%">
        <mj-text font-size="16px" color="{skin['brandPrimary']}" font-weight="700" border-top="2px solid {skin['brandPrimary']}" padding="12px 0 0">
          Total
        </mj-text>
      </mj-column>
      <mj-column width="50%">
        <mj-text align="right" font-size="16px" color="{skin['brandPrimary']}" font-weight="700" border-top="2px solid {skin['brandPrimary']}" padding="12px 0 0">
          {{{{orderTotal}}}}
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_social_icons(skin_name="apple_light"):
    """Convert social icons to MJML."""
    return '''    <mj-section padding="24px">
      <mj-column>
        <mj-social font-size="12px" icon-size="32px" mode="horizontal" align="center">
          <mj-social-element name="facebook" href="{{facebookUrl}}" />
          <mj-social-element name="twitter" href="{{twitterUrl}}" />
          <mj-social-element name="instagram" href="{{instagramUrl}}" />
          <mj-social-element name="linkedin" href="{{linkedinUrl}}" />
        </mj-social>
      </mj-column>
    </mj-section>'''


def section_to_mjml_footer_simple(skin_name="apple_light"):
    """Convert simple footer to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column>
        <mj-divider border-color="{skin['brandSecondary']}20" border-width="1px" padding="0 0 24px" />
        <mj-text align="center" font-size="12px" color="{skin['brandSecondary']}" padding="0 0 8px">
          {COPY_TOKENS['footerText']}
        </mj-text>
        <mj-text align="center" font-size="12px" color="{skin['brandSecondary']}">
          <a href="{{{{unsubscribeUrl}}}}" style="color: {skin['brandSecondary']}; text-decoration: underline;">Unsubscribe</a> &bull;
          <a href="{{{{preferencesUrl}}}}" style="color: {skin['brandSecondary']}; text-decoration: underline;">Preferences</a> &bull;
          <a href="{{{{privacyUrl}}}}" style="color: {skin['brandSecondary']}; text-decoration: underline;">Privacy</a>
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_footer_complex(skin_name="apple_light"):
    """Convert complex footer to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="32px 24px" background-color="{skin['brandPrimary']}">
      <mj-column width="33%">
        <mj-image src="{IMAGE_PLACEHOLDERS['logo']}" alt="{{{{brandName}}}}" width="120px" align="left" />
        <mj-text font-size="12px" color="{skin['brandBG']}" css-class="opacity-80" padding="12px 0 0">
          {{{{companyAddress}}}}
        </mj-text>
      </mj-column>
      <mj-column width="33%">
        <mj-text font-size="14px" color="{skin['brandBG']}" font-weight="600" padding="0 0 12px">
          Quick Links
        </mj-text>
        <mj-text font-size="12px" padding="0">
          <a href="{{{{aboutUrl}}}}" style="color: {skin['brandBG']}; text-decoration: none; opacity: 0.8;">About Us</a>
        </mj-text>
        <mj-text font-size="12px" padding="4px 0 0">
          <a href="{{{{contactUrl}}}}" style="color: {skin['brandBG']}; text-decoration: none; opacity: 0.8;">Contact</a>
        </mj-text>
        <mj-text font-size="12px" padding="4px 0 0">
          <a href="{{{{faqUrl}}}}" style="color: {skin['brandBG']}; text-decoration: none; opacity: 0.8;">FAQ</a>
        </mj-text>
      </mj-column>
      <mj-column width="33%">
        <mj-text font-size="14px" color="{skin['brandBG']}" font-weight="600" padding="0 0 12px">
          Legal
        </mj-text>
        <mj-text font-size="12px" padding="0">
          <a href="{{{{privacyUrl}}}}" style="color: {skin['brandBG']}; text-decoration: none; opacity: 0.8;">Privacy Policy</a>
        </mj-text>
        <mj-text font-size="12px" padding="4px 0 0">
          <a href="{{{{termsUrl}}}}" style="color: {skin['brandBG']}; text-decoration: none; opacity: 0.8;">Terms of Service</a>
        </mj-text>
        <mj-text font-size="12px" padding="4px 0 0">
          <a href="{{{{unsubscribeUrl}}}}" style="color: {skin['brandBG']}; text-decoration: none; opacity: 0.8;">Unsubscribe</a>
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_divider(skin_name="apple_light"):
    """Convert divider to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="16px 24px">
      <mj-column>
        <mj-divider border-color="{skin['brandSecondary']}20" border-width="1px" />
      </mj-column>
    </mj-section>'''


def section_to_mjml_spacer(skin_name="apple_light"):
    """Convert spacer to MJML."""
    return '''    <mj-section padding="0">
      <mj-column>
        <mj-spacer height="24px" />
      </mj-column>
    </mj-section>'''


def section_to_mjml_security_alert(skin_name="apple_light"):
    """Convert security alert to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column background-color="{skin['brandSecondary']}10" border-radius="8px" padding="24px">
        <mj-table>
          <tr>
            <td width="64" valign="top">
              <img src="{IMAGE_PLACEHOLDERS['icon']}" alt="Security" width="48" height="48" />
            </td>
            <td style="padding-left: 16px;">
              <p style="font-family: {skin['brandFont']}; font-size: 20px; color: {skin['brandPrimary']}; margin: 0 0 8px;">{{{{securityTitle}}}}</p>
              <p style="font-family: {skin['brandFont']}; font-size: 14px; color: {skin['brandText']}; margin: 0; line-height: 1.5;">{{{{securityMessage}}}}</p>
            </td>
          </tr>
        </mj-table>
      </mj-column>
    </mj-section>'''


def section_to_mjml_verification_code(skin_name="apple_light"):
    """Convert verification code to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="32px 24px">
      <mj-column>
        <mj-text align="center" background-color="{skin['brandSecondary']}10" border="2px dashed {skin['brandSecondary']}40" border-radius="8px" padding="24px 48px">
          <p style="font-size: 14px; color: {skin['brandSecondary']}; margin: 0 0 8px; text-transform: uppercase; letter-spacing: 1px;">Verification Code</p>
          <p style="font-family: 'Courier New', monospace; font-size: 36px; color: {skin['brandPrimary']}; margin: 0; font-weight: 700; letter-spacing: 8px;">{{{{verificationCode}}}}</p>
        </mj-text>
        <mj-text align="center" font-size="12px" color="{skin['brandSecondary']}" padding="16px 0 0">
          This code expires in {{{{codeExpiry}}}}
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_shipping_tracker(skin_name="apple_light"):
    """Convert shipping tracker to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column background-color="{skin['brandAccent']}10" border-radius="8px" padding="24px">
        <mj-text font-size="18px" color="{skin['brandPrimary']}" padding="0 0 16px">
          {{{{shippingStatus}}}}
        </mj-text>
        <mj-table>
          <tr>
            <td width="50%">
              <p style="font-size: 12px; color: {skin['brandSecondary']}; margin: 0;">Tracking Number</p>
              <p style="font-family: 'Courier New', monospace; font-size: 14px; color: {skin['brandPrimary']}; margin: 4px 0 0; font-weight: 600;">{{{{trackingNumber}}}}</p>
            </td>
            <td width="50%">
              <p style="font-size: 12px; color: {skin['brandSecondary']}; margin: 0;">Carrier</p>
              <p style="font-size: 14px; color: {skin['brandPrimary']}; margin: 4px 0 0; font-weight: 600;">{{{{carrier}}}}</p>
            </td>
          </tr>
        </mj-table>
        <mj-table padding="16px 0 0">
          <tr>
            <td width="50%">
              <p style="font-size: 12px; color: {skin['brandSecondary']}; margin: 0;">Estimated Delivery</p>
              <p style="font-size: 14px; color: {skin['brandAccent']}; margin: 4px 0 0; font-weight: 600;">{{{{estimatedDelivery}}}}</p>
            </td>
            <td width="50%" align="right">
              <a href="{{{{trackingUrl}}}}" style="display: inline-block; padding: 10px 20px; background-color: {skin['brandAccent']}; color: #ffffff; font-size: 14px; font-weight: 600; text-decoration: none; border-radius: 6px;">Track Package</a>
            </td>
          </tr>
        </mj-table>
      </mj-column>
    </mj-section>'''


def section_to_mjml_cart_item(skin_name="apple_light"):
    """Convert cart item to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="16px 24px">
      <mj-column border="1px solid {skin['brandSecondary']}20" border-radius="8px" padding="16px">
        <mj-table>
          <tr>
            <td width="120">
              <img src="{IMAGE_PLACEHOLDERS['product']}" alt="{{{{cartItemAlt}}}}" width="100" height="100" style="border-radius: 4px;" />
            </td>
            <td style="padding-left: 16px;" valign="middle">
              <p style="font-size: 16px; color: {skin['brandPrimary']}; margin: 0 0 4px; font-weight: 600;">{{{{cartItemName}}}}</p>
              <p style="font-size: 14px; color: {skin['brandSecondary']}; margin: 0 0 8px;">{{{{cartItemVariant}}}}</p>
              <p style="font-size: 18px; color: {skin['brandAccent']}; margin: 0; font-weight: 700;">{{{{cartItemPrice}}}}</p>
            </td>
          </tr>
        </mj-table>
      </mj-column>
    </mj-section>'''


def section_to_mjml_urgency_banner(skin_name="apple_light"):
    """Convert urgency banner to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="16px 24px" background-color="{skin['brandAccent']}15">
      <mj-column>
        <mj-text align="center" font-size="14px" color="{skin['brandAccent']}" font-weight="600">
          &#9200; {{{{urgencyMessage}}}}
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_event_details(skin_name="apple_light"):
    """Convert event details to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column background-color="{skin['brandPrimary']}05" border-left="4px solid {skin['brandAccent']}" border-radius="0 8px 8px 0" padding="24px">
        <mj-text font-size="20px" color="{skin['brandPrimary']}" padding="0 0 16px">
          {{{{eventTitle}}}}
        </mj-text>
        <mj-table>
          <tr>
            <td width="32" valign="top">
              <img src="{IMAGE_PLACEHOLDERS['icon']}" alt="" width="24" height="24" />
            </td>
            <td style="padding-left: 8px; padding-bottom: 12px;">
              <p style="font-size: 12px; color: {skin['brandSecondary']}; margin: 0;">Date &amp; Time</p>
              <p style="font-size: 14px; color: {skin['brandPrimary']}; margin: 4px 0 0; font-weight: 600;">{{{{eventDateTime}}}}</p>
            </td>
          </tr>
          <tr>
            <td width="32" valign="top">
              <img src="{IMAGE_PLACEHOLDERS['icon']}" alt="" width="24" height="24" />
            </td>
            <td style="padding-left: 8px; padding-bottom: 12px;">
              <p style="font-size: 12px; color: {skin['brandSecondary']}; margin: 0;">Location</p>
              <p style="font-size: 14px; color: {skin['brandPrimary']}; margin: 4px 0 0; font-weight: 600;">{{{{eventLocation}}}}</p>
            </td>
          </tr>
          <tr>
            <td width="32" valign="top">
              <img src="{IMAGE_PLACEHOLDERS['icon']}" alt="" width="24" height="24" />
            </td>
            <td style="padding-left: 8px;">
              <p style="font-size: 12px; color: {skin['brandSecondary']}; margin: 0;">Host</p>
              <p style="font-size: 14px; color: {skin['brandPrimary']}; margin: 4px 0 0; font-weight: 600;">{{{{eventHost}}}}</p>
            </td>
          </tr>
        </mj-table>
      </mj-column>
    </mj-section>'''


def section_to_mjml_rsvp_buttons(skin_name="apple_light"):
    """Convert RSVP buttons to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column width="50%">
        <mj-button href="{{{{rsvpAcceptUrl}}}}" background-color="{skin['brandAccent']}" align="right" padding="0 8px 0 0">
          Accept
        </mj-button>
      </mj-column>
      <mj-column width="50%">
        <mj-button href="{{{{rsvpDeclineUrl}}}}" background-color="transparent" color="{skin['brandSecondary']}" border="2px solid {skin['brandSecondary']}" align="left" padding="0 0 0 8px">
          Decline
        </mj-button>
      </mj-column>
    </mj-section>'''


# Registry mapping section types to MJML converters
MJML_SECTION_REGISTRY = {
    "hero": section_to_mjml_hero,
    "subhero": section_to_mjml_subhero,
    "1col_text": section_to_mjml_1col_text,
    "2col_text_image": section_to_mjml_2col_text_image,
    "3col_features": section_to_mjml_3col_features,
    "product_grid": section_to_mjml_product_grid,
    "testimonial": section_to_mjml_testimonial,
    "story_block": section_to_mjml_story_block,
    "cta_band": section_to_mjml_cta_band,
    "header_nav": section_to_mjml_header_nav,
    "offer_banner": section_to_mjml_offer_banner,
    "order_summary": section_to_mjml_order_summary,
    "social_icons": section_to_mjml_social_icons,
    "footer_simple": section_to_mjml_footer_simple,
    "footer_complex": section_to_mjml_footer_complex,
    "divider": section_to_mjml_divider,
    "spacer": section_to_mjml_spacer,
    "security_alert": section_to_mjml_security_alert,
    "verification_code": section_to_mjml_verification_code,
    "shipping_tracker": section_to_mjml_shipping_tracker,
    "cart_item": section_to_mjml_cart_item,
    "urgency_banner": section_to_mjml_urgency_banner,
    "event_details": section_to_mjml_event_details,
    "rsvp_buttons": section_to_mjml_rsvp_buttons,
}


def get_mjml_section(section_type, skin_name="apple_light"):
    """Get MJML output for a section type."""
    if section_type in MJML_SECTION_REGISTRY:
        return MJML_SECTION_REGISTRY[section_type](skin_name)
    return None


def generate_mjml_template(sections, skin_name="apple_light"):
    """Generate a complete MJML template from a list of section types."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    mjml_sections = []
    for section_type in sections:
        mjml_section = get_mjml_section(section_type, skin_name)
        if mjml_section:
            mjml_sections.append(mjml_section)

    body_content = "\n".join(mjml_sections)

    return f'''<mjml>
{get_mjml_head(skin_name)}
  <mj-body background-color="{skin['brandBG']}">
{body_content}
  </mj-body>
</mjml>'''


def convert_template_to_mjml(template_data):
    """
    Convert a template dictionary (with HTML) to MJML format.

    Args:
        template_data: Dict with 'sections_used' and 'skin' keys

    Returns:
        MJML string
    """
    sections = template_data.get('sections_used', [])
    skin_name = template_data.get('skin', 'apple_light')

    return generate_mjml_template(sections, skin_name)


def list_supported_sections():
    """List all section types that have MJML converters."""
    return list(MJML_SECTION_REGISTRY.keys())

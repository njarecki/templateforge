"""
MJML Converter

Converts HTML email templates to MJML format for easier downstream editing.
MJML (Mailjet Markup Language) is an open-source framework for responsive emails.

Also provides MJML to HTML compilation using the MJML CLI tool.
"""

import subprocess
import shutil
import tempfile
import os

from design_system import IMAGE_PLACEHOLDERS, COPY_TOKENS, DESIGN_SKINS


def get_mjml_path():
    """Get the path to the MJML CLI executable."""
    # Check global install first
    global_mjml = shutil.which("mjml")
    if global_mjml:
        return global_mjml

    # Check local node_modules
    local_paths = [
        os.path.join(os.path.dirname(__file__), "node_modules", ".bin", "mjml"),
        os.path.join(os.getcwd(), "node_modules", ".bin", "mjml"),
    ]
    for local_path in local_paths:
        if os.path.isfile(local_path) and os.access(local_path, os.X_OK):
            return local_path

    return None


def is_mjml_available():
    """Check if MJML CLI is installed and available."""
    return get_mjml_path() is not None


def compile_mjml_to_html(mjml_content, minify=True, beautify=False):
    """
    Compile MJML markup to production-ready HTML using the MJML CLI.

    Args:
        mjml_content: MJML string to compile
        minify: Whether to minify the output HTML (default: True)
        beautify: Whether to beautify the output HTML (default: False)

    Returns:
        dict with keys:
            - 'success': bool
            - 'html': compiled HTML string (if success)
            - 'error': error message (if failed)

    Note: Requires MJML CLI to be installed (`npm install -g mjml`)
    """
    mjml_bin = get_mjml_path()
    if not mjml_bin:
        return {
            'success': False,
            'error': 'MJML CLI not found. Install with: npm install -g mjml (or npm install mjml locally)',
            'html': None
        }

    try:
        # Create temporary file for MJML input
        with tempfile.NamedTemporaryFile(mode='w', suffix='.mjml', delete=False) as f:
            f.write(mjml_content)
            mjml_file_path = f.name

        try:
            # Build command
            cmd = [mjml_bin, mjml_file_path, '-s']  # -s outputs to stdout

            if minify:
                cmd.extend(['--config.minify', 'true'])
            if beautify:
                cmd.extend(['--config.beautify', 'true'])

            # Run MJML CLI
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode == 0:
                return {
                    'success': True,
                    'html': result.stdout,
                    'error': None
                }
            else:
                return {
                    'success': False,
                    'html': None,
                    'error': result.stderr or 'MJML compilation failed'
                }

        finally:
            # Clean up temp file
            os.unlink(mjml_file_path)

    except subprocess.TimeoutExpired:
        return {
            'success': False,
            'html': None,
            'error': 'MJML compilation timed out'
        }
    except Exception as e:
        return {
            'success': False,
            'html': None,
            'error': f'MJML compilation error: {str(e)}'
        }


def compile_template(template_data, minify=True):
    """
    Compile a template's MJML to HTML.

    Args:
        template_data: Dict with 'mjml' key containing MJML string
        minify: Whether to minify output

    Returns:
        Updated template_data with 'compiled_html' key added
    """
    if 'mjml' not in template_data:
        template_data['compiled_html'] = None
        template_data['compilation_error'] = 'No MJML content to compile'
        return template_data

    result = compile_mjml_to_html(template_data['mjml'], minify=minify)

    if result['success']:
        template_data['compiled_html'] = result['html']
        template_data['compilation_error'] = None
    else:
        template_data['compiled_html'] = None
        template_data['compilation_error'] = result['error']

    return template_data


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


def section_to_mjml_countdown_timer(skin_name="apple_light"):
    """Convert countdown timer to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="32px 24px" background-color="{skin['brandPrimary']}">
      <mj-column>
        <mj-text align="center" font-size="14px" color="{skin['brandBG']}" text-transform="uppercase" letter-spacing="2px" padding="0 0 16px">
          {{{{countdownLabel}}}}
        </mj-text>
      </mj-column>
    </mj-section>
    <mj-section padding="0 24px 32px" background-color="{skin['brandPrimary']}">
      <mj-column width="25%">
        <mj-text align="center" background-color="{skin['brandBG']}" border-radius="8px" padding="16px 8px">
          <p style="font-size: 36px; color: {skin['brandPrimary']}; margin: 0; font-weight: 700;">{{{{countdownDays}}}}</p>
        </mj-text>
        <mj-text align="center" font-size="12px" color="{skin['brandBG']}" text-transform="uppercase" padding="8px 0 0">
          Days
        </mj-text>
      </mj-column>
      <mj-column width="25%">
        <mj-text align="center" background-color="{skin['brandBG']}" border-radius="8px" padding="16px 8px">
          <p style="font-size: 36px; color: {skin['brandPrimary']}; margin: 0; font-weight: 700;">{{{{countdownHours}}}}</p>
        </mj-text>
        <mj-text align="center" font-size="12px" color="{skin['brandBG']}" text-transform="uppercase" padding="8px 0 0">
          Hours
        </mj-text>
      </mj-column>
      <mj-column width="25%">
        <mj-text align="center" background-color="{skin['brandBG']}" border-radius="8px" padding="16px 8px">
          <p style="font-size: 36px; color: {skin['brandPrimary']}; margin: 0; font-weight: 700;">{{{{countdownMins}}}}</p>
        </mj-text>
        <mj-text align="center" font-size="12px" color="{skin['brandBG']}" text-transform="uppercase" padding="8px 0 0">
          Mins
        </mj-text>
      </mj-column>
      <mj-column width="25%">
        <mj-text align="center" background-color="{skin['brandBG']}" border-radius="8px" padding="16px 8px">
          <p style="font-size: 36px; color: {skin['brandPrimary']}; margin: 0; font-weight: 700;">{{{{countdownSecs}}}}</p>
        </mj-text>
        <mj-text align="center" font-size="12px" color="{skin['brandBG']}" text-transform="uppercase" padding="8px 0 0">
          Secs
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_video_placeholder(skin_name="apple_light"):
    """Convert video placeholder to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column>
        <mj-image src="{IMAGE_PLACEHOLDERS['hero']}" alt="{{{{videoAlt}}}}" href="{{{{videoUrl}}}}" border-radius="8px" />
        <mj-button href="{{{{videoUrl}}}}" background-color="{skin['brandAccent']}" border-radius="50%" width="60px" height="60px" padding="0" css-class="video-play-btn">
          &#9658;
        </mj-button>
        <mj-text align="center" font-size="14px" color="{skin['brandSecondary']}" padding="16px 0 0">
          {{{{videoCaption}}}}
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_accordion_faq(skin_name="apple_light"):
    """Convert accordion FAQ to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column>
        <mj-text font-size="24px" color="{skin['brandPrimary']}" padding="0 0 24px">
          Frequently Asked Questions
        </mj-text>
        <!-- FAQ Item 1 -->
        <mj-text padding="0 0 8px" border-bottom="1px solid {skin['brandSecondary']}20">
          <h3 style="font-size: 16px; color: {skin['brandPrimary']}; margin: 0 0 8px; font-weight: 600;">{{{{faq1Question}}}}</h3>
          <p style="font-size: 14px; color: {skin['brandText']}; margin: 0 0 16px; line-height: 1.6;">{{{{faq1Answer}}}}</p>
        </mj-text>
        <!-- FAQ Item 2 -->
        <mj-text padding="16px 0 8px" border-bottom="1px solid {skin['brandSecondary']}20">
          <h3 style="font-size: 16px; color: {skin['brandPrimary']}; margin: 0 0 8px; font-weight: 600;">{{{{faq2Question}}}}</h3>
          <p style="font-size: 14px; color: {skin['brandText']}; margin: 0 0 16px; line-height: 1.6;">{{{{faq2Answer}}}}</p>
        </mj-text>
        <!-- FAQ Item 3 -->
        <mj-text padding="16px 0 8px" border-bottom="1px solid {skin['brandSecondary']}20">
          <h3 style="font-size: 16px; color: {skin['brandPrimary']}; margin: 0 0 8px; font-weight: 600;">{{{{faq3Question}}}}</h3>
          <p style="font-size: 14px; color: {skin['brandText']}; margin: 0 0 16px; line-height: 1.6;">{{{{faq3Answer}}}}</p>
        </mj-text>
        <mj-text align="center" padding="16px 0 0">
          <a href="{{{{faqUrl}}}}" style="font-size: 14px; color: {skin['brandAccent']}; text-decoration: underline;">View all FAQs &rarr;</a>
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_pricing_table(skin_name="apple_light"):
    """Convert pricing table to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column>
        <mj-text align="center" font-size="24px" color="{skin['brandPrimary']}" padding="0 0 8px">
          Choose Your Plan
        </mj-text>
        <mj-text align="center" font-size="16px" color="{skin['brandSecondary']}" padding="0 0 24px">
          {{{{pricingSubheadline}}}}
        </mj-text>
      </mj-column>
    </mj-section>
    <mj-section padding="0 24px 24px">
      <!-- Basic Plan -->
      <mj-column width="33%" border="1px solid {skin['brandSecondary']}30" border-radius="8px">
        <mj-text align="center" font-size="14px" color="{skin['brandSecondary']}" text-transform="uppercase" letter-spacing="1px" padding="24px 16px 8px">
          {{{{plan1Name}}}}
        </mj-text>
        <mj-text align="center" font-size="36px" color="{skin['brandPrimary']}" font-weight="700" padding="0 16px">
          {{{{plan1Price}}}}
        </mj-text>
        <mj-text align="center" font-size="12px" color="{skin['brandSecondary']}" padding="4px 16px 16px">
          {{{{plan1Period}}}}
        </mj-text>
        <mj-text font-size="13px" color="{skin['brandText']}" padding="0 16px 6px">
          &#10003; {{{{plan1Feature1}}}}
        </mj-text>
        <mj-text font-size="13px" color="{skin['brandText']}" padding="0 16px 6px">
          &#10003; {{{{plan1Feature2}}}}
        </mj-text>
        <mj-text font-size="13px" color="{skin['brandText']}" padding="0 16px 16px">
          &#10003; {{{{plan1Feature3}}}}
        </mj-text>
        <mj-button href="{{{{plan1Url}}}}" background-color="transparent" color="{skin['brandAccent']}" border="2px solid {skin['brandAccent']}" padding="0 16px 24px">
          Select Plan
        </mj-button>
      </mj-column>
      <!-- Pro Plan (Featured) -->
      <mj-column width="33%" border="2px solid {skin['brandAccent']}" border-radius="8px" background-color="{skin['brandAccent']}08">
        <mj-text align="center" font-size="12px" color="#ffffff" background-color="{skin['brandAccent']}" text-transform="uppercase" letter-spacing="1px" padding="8px 16px" border-radius="6px 6px 0 0">
          Most Popular
        </mj-text>
        <mj-text align="center" font-size="14px" color="{skin['brandSecondary']}" text-transform="uppercase" letter-spacing="1px" padding="16px 16px 8px">
          {{{{plan2Name}}}}
        </mj-text>
        <mj-text align="center" font-size="36px" color="{skin['brandPrimary']}" font-weight="700" padding="0 16px">
          {{{{plan2Price}}}}
        </mj-text>
        <mj-text align="center" font-size="12px" color="{skin['brandSecondary']}" padding="4px 16px 16px">
          {{{{plan2Period}}}}
        </mj-text>
        <mj-text font-size="13px" color="{skin['brandText']}" padding="0 16px 6px">
          &#10003; {{{{plan2Feature1}}}}
        </mj-text>
        <mj-text font-size="13px" color="{skin['brandText']}" padding="0 16px 6px">
          &#10003; {{{{plan2Feature2}}}}
        </mj-text>
        <mj-text font-size="13px" color="{skin['brandText']}" padding="0 16px 6px">
          &#10003; {{{{plan2Feature3}}}}
        </mj-text>
        <mj-text font-size="13px" color="{skin['brandText']}" padding="0 16px 16px">
          &#10003; {{{{plan2Feature4}}}}
        </mj-text>
        <mj-button href="{{{{plan2Url}}}}" background-color="{skin['brandAccent']}" padding="0 16px 24px">
          Select Plan
        </mj-button>
      </mj-column>
      <!-- Enterprise Plan -->
      <mj-column width="33%" border="1px solid {skin['brandSecondary']}30" border-radius="8px">
        <mj-text align="center" font-size="14px" color="{skin['brandSecondary']}" text-transform="uppercase" letter-spacing="1px" padding="24px 16px 8px">
          {{{{plan3Name}}}}
        </mj-text>
        <mj-text align="center" font-size="36px" color="{skin['brandPrimary']}" font-weight="700" padding="0 16px">
          {{{{plan3Price}}}}
        </mj-text>
        <mj-text align="center" font-size="12px" color="{skin['brandSecondary']}" padding="4px 16px 16px">
          {{{{plan3Period}}}}
        </mj-text>
        <mj-text font-size="13px" color="{skin['brandText']}" padding="0 16px 6px">
          &#10003; {{{{plan3Feature1}}}}
        </mj-text>
        <mj-text font-size="13px" color="{skin['brandText']}" padding="0 16px 6px">
          &#10003; {{{{plan3Feature2}}}}
        </mj-text>
        <mj-text font-size="13px" color="{skin['brandText']}" padding="0 16px 6px">
          &#10003; {{{{plan3Feature3}}}}
        </mj-text>
        <mj-text font-size="13px" color="{skin['brandText']}" padding="0 16px 6px">
          &#10003; {{{{plan3Feature4}}}}
        </mj-text>
        <mj-text font-size="13px" color="{skin['brandText']}" padding="0 16px 16px">
          &#10003; {{{{plan3Feature5}}}}
        </mj-text>
        <mj-button href="{{{{plan3Url}}}}" background-color="transparent" color="{skin['brandAccent']}" border="2px solid {skin['brandAccent']}" padding="0 16px 24px">
          Contact Sales
        </mj-button>
      </mj-column>
    </mj-section>'''


def section_to_mjml_progress_tracker(skin_name="apple_light"):
    """Convert progress tracker to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <!-- Step 1 (Completed) -->
      <mj-column width="25%">
        <mj-text align="center" background-color="{skin['brandAccent']}" border-radius="50%" padding="8px" css-class="step-circle">
          <span style="font-size: 18px; color: #ffffff; font-weight: 700;">&#10003;</span>
        </mj-text>
        <mj-text align="center" font-size="12px" color="{skin['brandAccent']}" font-weight="600" padding="8px 0 0">
          {{{{step1Label}}}}
        </mj-text>
      </mj-column>
      <!-- Step 2 (Current) -->
      <mj-column width="25%">
        <mj-text align="center" background-color="{skin['brandAccent']}" border-radius="50%" padding="8px" css-class="step-circle">
          <span style="font-size: 18px; color: #ffffff; font-weight: 700;">2</span>
        </mj-text>
        <mj-text align="center" font-size="12px" color="{skin['brandPrimary']}" font-weight="600" padding="8px 0 0">
          {{{{step2Label}}}}
        </mj-text>
      </mj-column>
      <!-- Step 3 (Pending) -->
      <mj-column width="25%">
        <mj-text align="center" border="2px solid {skin['brandSecondary']}40" border-radius="50%" padding="8px" css-class="step-circle">
          <span style="font-size: 18px; color: {skin['brandSecondary']}; font-weight: 700;">3</span>
        </mj-text>
        <mj-text align="center" font-size="12px" color="{skin['brandSecondary']}" padding="8px 0 0">
          {{{{step3Label}}}}
        </mj-text>
      </mj-column>
      <!-- Step 4 (Pending) -->
      <mj-column width="25%">
        <mj-text align="center" border="2px solid {skin['brandSecondary']}40" border-radius="50%" padding="8px" css-class="step-circle">
          <span style="font-size: 18px; color: {skin['brandSecondary']}; font-weight: 700;">4</span>
        </mj-text>
        <mj-text align="center" font-size="12px" color="{skin['brandSecondary']}" padding="8px 0 0">
          {{{{step4Label}}}}
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_app_store_badges(skin_name="apple_light"):
    """Convert app store badges to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column>
        <mj-text align="center" font-size="16px" color="{skin['brandPrimary']}" padding="0 0 16px">
          {{{{appStoreHeadline}}}}
        </mj-text>
      </mj-column>
    </mj-section>
    <mj-section padding="0 24px 24px">
      <mj-column width="50%">
        <mj-image src="{IMAGE_PLACEHOLDERS['product']}" alt="Download on the App Store" href="{{{{appStoreUrl}}}}" width="135px" align="right" border-radius="6px" />
      </mj-column>
      <mj-column width="50%">
        <mj-image src="{IMAGE_PLACEHOLDERS['product']}" alt="Get it on Google Play" href="{{{{playStoreUrl}}}}" width="135px" align="left" border-radius="6px" />
      </mj-column>
    </mj-section>'''


def section_to_mjml_team_members(skin_name="apple_light"):
    """Convert team members to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column>
        <mj-text align="center" font-size="24px" color="{skin['brandPrimary']}" padding="0 0 24px">
          {{{{teamHeadline}}}}
        </mj-text>
      </mj-column>
    </mj-section>
    <mj-section padding="0 24px 24px">
      <!-- Member 1 -->
      <mj-column width="33%">
        <mj-image src="{IMAGE_PLACEHOLDERS['avatar']}" alt="{{{{member1Name}}}}" width="100px" border-radius="50%" />
        <mj-text align="center" font-size="16px" color="{skin['brandPrimary']}" padding="12px 0 0">
          {{{{member1Name}}}}
        </mj-text>
        <mj-text align="center" font-size="14px" color="{skin['brandSecondary']}" padding="4px 0 0">
          {{{{member1Role}}}}
        </mj-text>
      </mj-column>
      <!-- Member 2 -->
      <mj-column width="33%">
        <mj-image src="{IMAGE_PLACEHOLDERS['avatar']}" alt="{{{{member2Name}}}}" width="100px" border-radius="50%" />
        <mj-text align="center" font-size="16px" color="{skin['brandPrimary']}" padding="12px 0 0">
          {{{{member2Name}}}}
        </mj-text>
        <mj-text align="center" font-size="14px" color="{skin['brandSecondary']}" padding="4px 0 0">
          {{{{member2Role}}}}
        </mj-text>
      </mj-column>
      <!-- Member 3 -->
      <mj-column width="33%">
        <mj-image src="{IMAGE_PLACEHOLDERS['avatar']}" alt="{{{{member3Name}}}}" width="100px" border-radius="50%" />
        <mj-text align="center" font-size="16px" color="{skin['brandPrimary']}" padding="12px 0 0">
          {{{{member3Name}}}}
        </mj-text>
        <mj-text align="center" font-size="14px" color="{skin['brandSecondary']}" padding="4px 0 0">
          {{{{member3Role}}}}
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_comparison_table(skin_name="apple_light"):
    """Convert comparison table to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column>
        <mj-text align="center" font-size="24px" color="{skin['brandPrimary']}" padding="0 0 24px">
          {{{{comparisonHeadline}}}}
        </mj-text>
        <mj-table border="1px solid {skin['brandSecondary']}30" border-radius="8px">
          <tr style="background-color: {skin['brandPrimary']}; color: {skin['brandBG']};">
            <td style="padding: 12px 16px; font-weight: 600;">Feature</td>
            <td style="padding: 12px 16px; text-align: center; font-weight: 600;">{{{{compCol1}}}}</td>
            <td style="padding: 12px 16px; text-align: center; font-weight: 600;">{{{{compCol2}}}}</td>
          </tr>
          <tr style="background-color: {skin['brandBG']};">
            <td style="padding: 12px 16px; border-bottom: 1px solid {skin['brandSecondary']}20;">{{{{compRow1Feature}}}}</td>
            <td style="padding: 12px 16px; text-align: center; border-bottom: 1px solid {skin['brandSecondary']}20;">{{{{compRow1Col1}}}}</td>
            <td style="padding: 12px 16px; text-align: center; border-bottom: 1px solid {skin['brandSecondary']}20;">{{{{compRow1Col2}}}}</td>
          </tr>
          <tr style="background-color: {skin['brandSecondary']}08;">
            <td style="padding: 12px 16px; border-bottom: 1px solid {skin['brandSecondary']}20;">{{{{compRow2Feature}}}}</td>
            <td style="padding: 12px 16px; text-align: center; border-bottom: 1px solid {skin['brandSecondary']}20;">{{{{compRow2Col1}}}}</td>
            <td style="padding: 12px 16px; text-align: center; border-bottom: 1px solid {skin['brandSecondary']}20;">{{{{compRow2Col2}}}}</td>
          </tr>
          <tr style="background-color: {skin['brandBG']};">
            <td style="padding: 12px 16px; border-bottom: 1px solid {skin['brandSecondary']}20;">{{{{compRow3Feature}}}}</td>
            <td style="padding: 12px 16px; text-align: center; border-bottom: 1px solid {skin['brandSecondary']}20;">{{{{compRow3Col1}}}}</td>
            <td style="padding: 12px 16px; text-align: center; border-bottom: 1px solid {skin['brandSecondary']}20;">{{{{compRow3Col2}}}}</td>
          </tr>
          <tr style="background-color: {skin['brandSecondary']}08;">
            <td style="padding: 12px 16px;">{{{{compRow4Feature}}}}</td>
            <td style="padding: 12px 16px; text-align: center;">{{{{compRow4Col1}}}}</td>
            <td style="padding: 12px 16px; text-align: center;">{{{{compRow4Col2}}}}</td>
          </tr>
        </mj-table>
      </mj-column>
    </mj-section>'''


def section_to_mjml_stats_metrics(skin_name="apple_light"):
    """Convert stats metrics to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="32px 24px" background-color="{skin['brandPrimary']}">
      <mj-column width="25%">
        <mj-text align="center" font-size="36px" color="{skin['brandBG']}" font-weight="700" padding="0">
          {{{{stat1Value}}}}
        </mj-text>
        <mj-text align="center" font-size="14px" color="{skin['brandBG']}" css-class="opacity-80" padding="4px 0 0">
          {{{{stat1Label}}}}
        </mj-text>
      </mj-column>
      <mj-column width="25%">
        <mj-text align="center" font-size="36px" color="{skin['brandBG']}" font-weight="700" padding="0">
          {{{{stat2Value}}}}
        </mj-text>
        <mj-text align="center" font-size="14px" color="{skin['brandBG']}" css-class="opacity-80" padding="4px 0 0">
          {{{{stat2Label}}}}
        </mj-text>
      </mj-column>
      <mj-column width="25%">
        <mj-text align="center" font-size="36px" color="{skin['brandBG']}" font-weight="700" padding="0">
          {{{{stat3Value}}}}
        </mj-text>
        <mj-text align="center" font-size="14px" color="{skin['brandBG']}" css-class="opacity-80" padding="4px 0 0">
          {{{{stat3Label}}}}
        </mj-text>
      </mj-column>
      <mj-column width="25%">
        <mj-text align="center" font-size="36px" color="{skin['brandBG']}" font-weight="700" padding="0">
          {{{{stat4Value}}}}
        </mj-text>
        <mj-text align="center" font-size="14px" color="{skin['brandBG']}" css-class="opacity-80" padding="4px 0 0">
          {{{{stat4Label}}}}
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_rating_stars(skin_name="apple_light"):
    """Convert rating stars to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column background-color="{skin['brandSecondary']}08" border-radius="8px" padding="24px">
        <mj-table>
          <tr>
            <td width="120" valign="middle">
              <img src="{IMAGE_PLACEHOLDERS['product']}" alt="{{{{ratingProductAlt}}}}" width="100" height="100" style="border-radius: 8px;" />
            </td>
            <td style="padding-left: 16px;" valign="middle">
              <h3 style="font-size: 18px; color: {skin['brandPrimary']}; margin: 0 0 8px;">{{{{ratingProductName}}}}</h3>
              <p style="font-size: 20px; color: {skin['brandAccent']}; margin: 0; letter-spacing: 2px;">&#9733;&#9733;&#9733;&#9733;&#9734; <span style="font-size: 16px; color: {skin['brandPrimary']}; font-weight: 700;">{{{{ratingScore}}}}</span></p>
              <p style="font-size: 14px; color: {skin['brandSecondary']}; margin: 8px 0 0;">{{{{ratingCount}}}} reviews</p>
            </td>
          </tr>
        </mj-table>
        <mj-divider border-color="{skin['brandSecondary']}20" border-width="1px" padding="16px 0" />
        <mj-text font-size="14px" font-style="italic" color="{skin['brandText']}" padding="0">
          &ldquo;{{{{ratingReviewText}}}}&rdquo;
        </mj-text>
        <mj-text font-size="13px" color="{skin['brandSecondary']}" padding="8px 0 0">
          &mdash; {{{{ratingReviewAuthor}}}}
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_gallery_carousel(skin_name="apple_light"):
    """Convert gallery carousel to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column>
        <mj-text align="center" font-size="24px" color="{skin['brandPrimary']}" padding="0 0 16px">
          {{{{galleryHeadline}}}}
        </mj-text>
      </mj-column>
    </mj-section>
    <mj-section padding="0 24px">
      <mj-column width="25%">
        <mj-image src="{IMAGE_PLACEHOLDERS['product']}" alt="{{{{galleryItem1Alt}}}}" href="{{{{galleryItem1Url}}}}" border-radius="8px" />
        <mj-text align="center" font-size="13px" color="{skin['brandPrimary']}" padding="8px 0 0">
          {{{{galleryItem1Label}}}}
        </mj-text>
      </mj-column>
      <mj-column width="25%">
        <mj-image src="{IMAGE_PLACEHOLDERS['product']}" alt="{{{{galleryItem2Alt}}}}" href="{{{{galleryItem2Url}}}}" border-radius="8px" />
        <mj-text align="center" font-size="13px" color="{skin['brandPrimary']}" padding="8px 0 0">
          {{{{galleryItem2Label}}}}
        </mj-text>
      </mj-column>
      <mj-column width="25%">
        <mj-image src="{IMAGE_PLACEHOLDERS['product']}" alt="{{{{galleryItem3Alt}}}}" href="{{{{galleryItem3Url}}}}" border-radius="8px" />
        <mj-text align="center" font-size="13px" color="{skin['brandPrimary']}" padding="8px 0 0">
          {{{{galleryItem3Label}}}}
        </mj-text>
      </mj-column>
      <mj-column width="25%">
        <mj-image src="{IMAGE_PLACEHOLDERS['product']}" alt="{{{{galleryItem4Alt}}}}" href="{{{{galleryItem4Url}}}}" border-radius="8px" />
        <mj-text align="center" font-size="13px" color="{skin['brandPrimary']}" padding="8px 0 0">
          {{{{galleryItem4Label}}}}
        </mj-text>
      </mj-column>
    </mj-section>
    <mj-section padding="16px 24px 24px">
      <mj-column>
        <mj-text align="center">
          <a href="{{{{galleryViewAllUrl}}}}" style="font-size: 14px; color: {skin['brandAccent']}; text-decoration: underline;">View all &rarr;</a>
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_multi_step_form(skin_name="apple_light"):
    """Convert multi-step form to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column background-color="{skin['brandSecondary']}08" border-radius="8px" padding="24px">
        <mj-text font-size="20px" color="{skin['brandPrimary']}" padding="0 0 8px">
          {{{{formHeadline}}}}
        </mj-text>
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="0 0 20px">
          {{{{formSubheadline}}}}
        </mj-text>
        <!-- Progress bar -->
        <mj-table padding="0 0 8px">
          <tr>
            <td style="background-color: {skin['brandSecondary']}20; border-radius: 4px; height: 8px;">
              <div style="background-color: {skin['brandAccent']}; border-radius: 4px; height: 8px; width: 33%;"></div>
            </td>
          </tr>
        </mj-table>
        <mj-text font-size="12px" color="{skin['brandSecondary']}" padding="0 0 24px">
          Step {{{{formCurrentStep}}}} of {{{{formTotalSteps}}}}
        </mj-text>
        <!-- Field 1 -->
        <mj-text font-size="13px" color="{skin['brandPrimary']}" font-weight="600" padding="0 0 6px">
          {{{{formField1Label}}}}
        </mj-text>
        <mj-text background-color="{skin['brandBG']}" border="1px solid {skin['brandSecondary']}40" border-radius="6px" padding="12px 14px" font-size="14px" color="{skin['brandSecondary']}">
          {{{{formField1Placeholder}}}}
        </mj-text>
        <!-- Field 2 -->
        <mj-text font-size="13px" color="{skin['brandPrimary']}" font-weight="600" padding="16px 0 6px">
          {{{{formField2Label}}}}
        </mj-text>
        <mj-text background-color="{skin['brandBG']}" border="1px solid {skin['brandSecondary']}40" border-radius="6px" padding="12px 14px" font-size="14px" color="{skin['brandSecondary']}">
          {{{{formField2Placeholder}}}}
        </mj-text>
        <!-- Field 3 -->
        <mj-text font-size="13px" color="{skin['brandPrimary']}" font-weight="600" padding="16px 0 6px">
          {{{{formField3Label}}}}
        </mj-text>
        <mj-text background-color="{skin['brandBG']}" border="1px solid {skin['brandSecondary']}40" border-radius="6px" padding="12px 14px 20px" font-size="14px" color="{skin['brandSecondary']}">
          {{{{formField3Placeholder}}}}
        </mj-text>
        <mj-button href="{{{{formContinueUrl}}}}" background-color="{skin['brandAccent']}" padding="0">
          {{{{formContinueLabel}}}}
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
    "countdown_timer": section_to_mjml_countdown_timer,
    "video_placeholder": section_to_mjml_video_placeholder,
    "accordion_faq": section_to_mjml_accordion_faq,
    "pricing_table": section_to_mjml_pricing_table,
    "progress_tracker": section_to_mjml_progress_tracker,
    "app_store_badges": section_to_mjml_app_store_badges,
    "team_members": section_to_mjml_team_members,
    "comparison_table": section_to_mjml_comparison_table,
    "stats_metrics": section_to_mjml_stats_metrics,
    "rating_stars": section_to_mjml_rating_stars,
    "gallery_carousel": section_to_mjml_gallery_carousel,
    "multi_step_form": section_to_mjml_multi_step_form,
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

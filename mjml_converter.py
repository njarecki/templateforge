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


def section_to_mjml_referral_program(skin_name="apple_light"):
    """Convert referral program section to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column background-color="{skin['brandAccent']}10" border="2px dashed {skin['brandAccent']}40" border-radius="12px" padding="32px">
        <!-- Icon -->
        <mj-image src="{IMAGE_PLACEHOLDERS['icon']}" alt="Refer" width="80px" background-color="{skin['brandAccent']}" border-radius="50%" padding="0" />
        <mj-text align="center" font-size="24px" color="{skin['brandPrimary']}" font-weight="600" padding="24px 0 8px">
          {{{{referralHeadline}}}}
        </mj-text>
        <mj-text align="center" font-size="16px" color="{skin['brandSecondary']}" padding="0 0 24px">
          {{{{referralDescription}}}}
        </mj-text>
      </mj-column>
    </mj-section>
    <mj-section padding="0 24px">
      <mj-column width="50%" background-color="{skin['brandBG']}" border-radius="8px 0 0 8px" padding="16px">
        <mj-text align="center" font-size="12px" color="{skin['brandSecondary']}" text-transform="uppercase" padding="0 0 4px">
          You Get
        </mj-text>
        <mj-text align="center" font-size="24px" color="{skin['brandAccent']}" font-weight="700" padding="0">
          {{{{referralYourReward}}}}
        </mj-text>
      </mj-column>
      <mj-column width="50%" background-color="{skin['brandBG']}" border-radius="0 8px 8px 0" border-left="2px solid {skin['brandSecondary']}20" padding="16px">
        <mj-text align="center" font-size="12px" color="{skin['brandSecondary']}" text-transform="uppercase" padding="0 0 4px">
          They Get
        </mj-text>
        <mj-text align="center" font-size="24px" color="{skin['brandAccent']}" font-weight="700" padding="0">
          {{{{referralTheirReward}}}}
        </mj-text>
      </mj-column>
    </mj-section>
    <mj-section padding="24px">
      <mj-column>
        <mj-text font-family="monospace" font-size="14px" color="{skin['brandPrimary']}" background-color="{skin['brandBG']}" border="1px solid {skin['brandSecondary']}30" border-radius="8px" padding="14px 20px" align="center">
          {{{{referralLink}}}}
        </mj-text>
        <mj-button href="{{{{referralShareUrl}}}}" background-color="{skin['brandAccent']}" padding="20px 0 0">
          {{{{referralCtaLabel}}}}
        </mj-button>
      </mj-column>
    </mj-section>'''


def section_to_mjml_loyalty_points(skin_name="apple_light"):
    """Convert loyalty points section to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column background-color="{skin['brandPrimary']}" border-radius="16px" padding="32px">
        <!-- Header row -->
        <mj-text font-size="14px" color="#ffffff99" text-transform="uppercase" letter-spacing="1px" padding="0 0 4px">
          {{{{loyaltyProgramName}}}}
        </mj-text>
        <mj-text font-size="28px" color="#ffffff" font-weight="600" padding="0 0 24px">
          {{{{loyaltyUserName}}}}
        </mj-text>
        <!-- Points display -->
        <mj-text align="center" font-size="56px" color="#ffffff" font-weight="700" line-height="1" padding="0">
          {{{{loyaltyPoints}}}}
        </mj-text>
        <mj-text align="center" font-size="16px" color="#ffffff99" padding="8px 0 24px">
          points available
        </mj-text>
        <!-- Tier badge -->
        <mj-text align="center" font-size="14px" color="#ffffff" font-weight="600" background-color="#ffffff20" border-radius="20px" padding="6px 16px">
          {{{{loyaltyTier}}}}
        </mj-text>
        <!-- Progress bar placeholder -->
        <mj-text align="center" font-size="13px" color="#ffffff99" padding="24px 0">
          {{{{loyaltyPointsToNext}}}} points to {{{{loyaltyNextTier}}}}
        </mj-text>
        <mj-button href="{{{{loyaltyRedeemUrl}}}}" background-color="#ffffff" color="{skin['brandPrimary']}" padding="0">
          {{{{loyaltyCtaLabel}}}}
        </mj-button>
      </mj-column>
    </mj-section>'''


def section_to_mjml_gift_card(skin_name="apple_light"):
    """Convert gift card section to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column background-color="{skin['brandPrimary']}" border-radius="16px" padding="0">
        <!-- Decorative header strip -->
        <mj-text font-size="14px" color="#ffffff" font-weight="600" text-transform="uppercase" letter-spacing="2px" background-color="{skin['brandAccent']}" padding="16px 32px">
          {{{{giftCardBrandName}}}}
        </mj-text>
        <!-- Main body -->
        <mj-text font-size="16px" color="#ffffff99" padding="32px 32px 8px">
          Gift Card
        </mj-text>
        <mj-text font-size="48px" color="#ffffff" font-weight="700" padding="0 32px 24px">
          {{{{giftCardAmount}}}}
        </mj-text>
        <!-- Gift card code -->
        <mj-text font-size="12px" color="#ffffff80" text-transform="uppercase" background-color="#ffffff15" border-radius="8px" padding="20px 20px 8px">
          Your Gift Code
        </mj-text>
        <mj-text font-family="monospace" font-size="28px" color="#ffffff" font-weight="600" letter-spacing="4px" background-color="#ffffff15" border-radius="8px" padding="0 20px 20px">
          {{{{giftCardCode}}}}
        </mj-text>
        <!-- From/To info -->
        <mj-text font-size="12px" color="#ffffff80" text-transform="uppercase" padding="24px 32px 4px">
          From: {{{{giftCardFrom}}}} | To: {{{{giftCardTo}}}}
        </mj-text>
        <!-- Personal message -->
        <mj-text font-size="16px" color="#ffffff" font-style="italic" border-left="3px solid {skin['brandAccent']}" padding="16px 32px 24px">
          "{{{{giftCardMessage}}}}"
        </mj-text>
        <mj-button href="{{{{giftCardRedeemUrl}}}}" background-color="{skin['brandAccent']}" padding="0 32px 24px">
          {{{{giftCardCtaLabel}}}}
        </mj-button>
        <mj-text align="center" font-size="12px" color="#ffffff60" padding="0 32px 32px">
          Valid until {{{{giftCardExpiry}}}}
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_subscription_renewal(skin_name="apple_light"):
    """Convert subscription renewal section to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column border="1px solid {skin['brandSecondary']}20" border-radius="12px" padding="32px">
        <!-- Status indicator -->
        <mj-text font-size="13px" color="{{{{subscriptionStatusColor}}}}" font-weight="600" background-color="{{{{subscriptionStatusColor}}}}15" border-radius="20px" padding="6px 16px">
          {{{{subscriptionStatus}}}}
        </mj-text>
        <mj-text font-size="24px" color="{skin['brandPrimary']}" font-weight="600" padding="24px 0 8px">
          {{{{subscriptionHeadline}}}}
        </mj-text>
        <mj-text font-size="16px" color="{skin['brandSecondary']}" padding="0 0 24px">
          {{{{subscriptionDescription}}}}
        </mj-text>
        <!-- Plan details card -->
        <mj-text font-size="14px" color="{skin['brandSecondary']}" background-color="{skin['brandSecondary']}08" border-radius="8px" padding="24px 24px 4px">
          Current Plan
        </mj-text>
        <mj-text font-size="20px" color="{skin['brandPrimary']}" font-weight="600" background-color="{skin['brandSecondary']}08" border-radius="8px" padding="0 24px 16px">
          {{{{subscriptionPlanName}}}}
        </mj-text>
        <mj-text font-size="28px" color="{skin['brandPrimary']}" font-weight="700" background-color="{skin['brandSecondary']}08" border-radius="8px" padding="0 24px 4px" align="right">
          {{{{subscriptionPrice}}}}
        </mj-text>
        <mj-text font-size="14px" color="{skin['brandSecondary']}" background-color="{skin['brandSecondary']}08" border-radius="8px" padding="0 24px 24px" align="right">
          {{{{subscriptionBillingCycle}}}}
        </mj-text>
        <mj-divider border-color="{skin['brandSecondary']}20" padding="0 24px" />
        <!-- Renewal info -->
        <mj-text font-size="13px" color="{skin['brandSecondary']}" padding="16px 0 4px">
          Renewal Date: {{{{subscriptionRenewalDate}}}}
        </mj-text>
        <mj-text font-size="13px" color="{skin['brandSecondary']}" padding="0 0 24px">
          Payment Method: {{{{subscriptionPaymentMethod}}}}
        </mj-text>
        <!-- Action buttons -->
        <mj-button href="{{{{subscriptionManageUrl}}}}" background-color="{skin['brandAccent']}" padding="0 0 12px">
          {{{{subscriptionPrimaryCtaLabel}}}}
        </mj-button>
        <mj-button href="{{{{subscriptionUpgradeUrl}}}}" background-color="transparent" color="{skin['brandAccent']}" border="2px solid {skin['brandAccent']}" padding="0 0 24px">
          {{{{subscriptionSecondaryCtaLabel}}}}
        </mj-button>
        <mj-text align="center" font-size="13px" color="{skin['brandSecondary']}" padding="0">
          Questions? <a href="{{{{subscriptionHelpUrl}}}}" style="color: {skin['brandAccent']}; text-decoration: underline;">Contact Support</a>
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_wishlist_item(skin_name="apple_light"):
    """Convert wishlist item section to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="16px 24px">
      <mj-column border="1px solid {skin['brandSecondary']}20" border-radius="8px" padding="16px">
        <mj-group>
          <mj-column width="120px" padding="0">
            <mj-image src="{IMAGE_PLACEHOLDERS['product']}" alt="{{{{wishlistItemAlt}}}}" width="100px" border-radius="4px" />
          </mj-column>
          <mj-column padding-left="16px">
            <mj-text font-size="12px" color="{skin['brandSecondary']}" text-transform="uppercase" letter-spacing="0.5px" padding="0 0 4px">
              {{{{wishlistItemBrand}}}}
            </mj-text>
            <mj-text font-size="16px" color="{skin['brandPrimary']}" font-weight="600" padding="0 0 8px">
              {{{{wishlistItemName}}}}
            </mj-text>
            <mj-text font-size="18px" color="{skin['brandPrimary']}" font-weight="700" padding="0 0 8px">
              {{{{wishlistItemPrice}}}}
            </mj-text>
            <mj-text font-size="12px" color="{{{{wishlistItemStatusColor}}}}" font-weight="600" background-color="{{{{wishlistItemStatusColor}}}}15" border-radius="4px" padding="4px 10px" width="auto">
              {{{{wishlistItemStatus}}}}
            </mj-text>
            <mj-button href="{{{{wishlistItemUrl}}}}" background-color="{skin['brandAccent']}" padding="12px 0 0" font-size="14px" border-radius="6px" inner-padding="10px 20px">
              View Item
            </mj-button>
          </mj-column>
        </mj-group>
      </mj-column>
    </mj-section>'''


def section_to_mjml_price_alert(skin_name="apple_light"):
    """Convert price alert section to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column border="2px solid {skin['brandAccent']}" border-radius="12px">
        <!-- Alert header -->
        <mj-section background-color="{skin['brandAccent']}" padding="12px 20px" full-width="full-width">
          <mj-column width="50%">
            <mj-text font-size="14px" color="#ffffff" font-weight="700">
              🔔 PRICE DROP ALERT
            </mj-text>
          </mj-column>
          <mj-column width="50%">
            <mj-text align="right" font-size="14px" color="#ffffff" font-weight="600">
              {{{{priceAlertSavings}}}} OFF
            </mj-text>
          </mj-column>
        </mj-section>
        <!-- Product details -->
        <mj-section padding="20px">
          <mj-column width="140px" padding="0">
            <mj-image src="{IMAGE_PLACEHOLDERS['product']}" alt="{{{{priceAlertItemAlt}}}}" width="120px" border-radius="8px" />
          </mj-column>
          <mj-column padding-left="20px">
            <mj-text font-size="12px" color="{skin['brandSecondary']}" text-transform="uppercase" letter-spacing="0.5px" padding="0 0 4px">
              {{{{priceAlertItemBrand}}}}
            </mj-text>
            <mj-text font-size="18px" color="{skin['brandPrimary']}" font-weight="600" padding="0 0 12px">
              {{{{priceAlertItemName}}}}
            </mj-text>
            <mj-text font-size="14px" color="{skin['brandSecondary']}" text-decoration="line-through" padding="0">
              {{{{priceAlertOriginalPrice}}}}
            </mj-text>
            <mj-text font-size="24px" color="{skin['brandAccent']}" font-weight="700" padding="0 0 16px">
              {{{{priceAlertNewPrice}}}}
            </mj-text>
            <mj-button href="{{{{priceAlertItemUrl}}}}" background-color="{skin['brandAccent']}" padding="0" font-size="14px" border-radius="6px" inner-padding="12px 24px">
              Shop Now
            </mj-button>
          </mj-column>
        </mj-section>
        <!-- Urgency footer -->
        <mj-section background-color="{skin['brandSecondary']}08" padding="12px 20px">
          <mj-column>
            <mj-text align="center" font-size="13px" color="{skin['brandSecondary']}">
              {{{{priceAlertUrgency}}}}
            </mj-text>
          </mj-column>
        </mj-section>
      </mj-column>
    </mj-section>'''


def section_to_mjml_back_in_stock(skin_name="apple_light"):
    """Convert back-in-stock section to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column>
        <!-- Back in stock banner -->
        <mj-text align="center" font-size="16px" color="{skin['brandAccent']}" font-weight="700" background-color="{skin['brandAccent']}20" border-radius="8px" padding="16px">
          ✨ BACK IN STOCK ✨
        </mj-text>
      </mj-column>
    </mj-section>
    <mj-section padding="0 24px 24px">
      <mj-column border="1px solid {skin['brandSecondary']}20" border-radius="12px" padding="24px">
        <mj-image src="{IMAGE_PLACEHOLDERS['product']}" alt="{{{{backInStockItemAlt}}}}" width="200px" border-radius="8px" padding-bottom="20px" />
        <mj-text align="center" font-size="12px" color="{skin['brandSecondary']}" text-transform="uppercase" letter-spacing="1px" padding="0 0 8px">
          {{{{backInStockItemBrand}}}}
        </mj-text>
        <mj-text align="center" font-size="22px" color="{skin['brandPrimary']}" font-weight="600" padding="0 0 12px">
          {{{{backInStockItemName}}}}
        </mj-text>
        <mj-text align="center" font-size="20px" color="{skin['brandPrimary']}" font-weight="700" padding="0 0 20px">
          {{{{backInStockItemPrice}}}}
        </mj-text>
        <mj-text align="center" font-size="13px" color="#22c55e" font-weight="600" background-color="#22c55e15" border-radius="20px" padding="8px 16px">
          {{{{backInStockQuantity}}}} items available
        </mj-text>
        <mj-button href="{{{{backInStockItemUrl}}}}" background-color="{skin['brandAccent']}" padding="20px 0" font-size="16px" border-radius="8px" inner-padding="14px 32px">
          Buy Now
        </mj-button>
        <mj-text align="center" font-size="13px" color="{skin['brandSecondary']}" padding="0">
          {{{{backInStockMessage}}}}
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_invoice_details(skin_name="apple_light"):
    """Convert invoice details section to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column>
        <!-- Invoice header -->
        <mj-text font-size="24px" color="{skin['brandPrimary']}" font-weight="700" padding="0 0 8px">
          INVOICE
        </mj-text>
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="0 0 16px">
          Invoice #{{{{invoiceNumber}}}}
        </mj-text>
      </mj-column>
      <mj-column>
        <mj-text align="right" font-size="14px" color="{skin['brandSecondary']}" padding="0 0 4px">
          Issue Date: {{{{invoiceDate}}}}
        </mj-text>
        <mj-text align="right" font-size="14px" color="{skin['brandSecondary']}" padding="0">
          Due Date: {{{{invoiceDueDate}}}}
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Billing info -->
    <mj-section padding="0 24px 24px" border-top="1px solid {skin['brandSecondary']}20">
      <mj-column>
        <mj-text font-size="12px" color="{skin['brandSecondary']}" text-transform="uppercase" letter-spacing="0.5px" padding="16px 0 8px">
          Bill To:
        </mj-text>
        <mj-text font-size="14px" color="{skin['brandPrimary']}" font-weight="600" padding="0 0 4px">
          {{{{invoiceBillToName}}}}
        </mj-text>
        <mj-text font-size="14px" color="{skin['brandText']}" line-height="1.5" padding="0">
          {{{{invoiceBillToAddress}}}}
        </mj-text>
      </mj-column>
      <mj-column>
        <mj-text align="right" font-size="12px" color="{skin['brandSecondary']}" text-transform="uppercase" letter-spacing="0.5px" padding="16px 0 8px">
          From:
        </mj-text>
        <mj-text align="right" font-size="14px" color="{skin['brandPrimary']}" font-weight="600" padding="0 0 4px">
          {{{{companyName}}}}
        </mj-text>
        <mj-text align="right" font-size="14px" color="{skin['brandText']}" line-height="1.5" padding="0">
          {{{{companyAddress}}}}
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Line items table -->
    <mj-section padding="0 24px" background-color="{skin['brandSecondary']}08">
      <mj-column width="40%">
        <mj-text font-size="12px" color="{skin['brandSecondary']}" font-weight="600" text-transform="uppercase" padding="12px 16px">
          Description
        </mj-text>
      </mj-column>
      <mj-column width="20%">
        <mj-text align="center" font-size="12px" color="{skin['brandSecondary']}" font-weight="600" text-transform="uppercase" padding="12px 16px">
          Qty
        </mj-text>
      </mj-column>
      <mj-column width="20%">
        <mj-text align="right" font-size="12px" color="{skin['brandSecondary']}" font-weight="600" text-transform="uppercase" padding="12px 16px">
          Rate
        </mj-text>
      </mj-column>
      <mj-column width="20%">
        <mj-text align="right" font-size="12px" color="{skin['brandSecondary']}" font-weight="600" text-transform="uppercase" padding="12px 16px">
          Amount
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Line item 1 -->
    <mj-section padding="0 24px" border-top="1px solid {skin['brandSecondary']}10">
      <mj-column width="40%">
        <mj-text font-size="14px" color="{skin['brandPrimary']}" font-weight="500" padding="16px 16px 4px">
          {{{{invoiceItem1Name}}}}
        </mj-text>
        <mj-text font-size="12px" color="{skin['brandSecondary']}" padding="0 16px 16px">
          {{{{invoiceItem1Description}}}}
        </mj-text>
      </mj-column>
      <mj-column width="20%">
        <mj-text align="center" font-size="14px" color="{skin['brandText']}" padding="16px">
          {{{{invoiceItem1Qty}}}}
        </mj-text>
      </mj-column>
      <mj-column width="20%">
        <mj-text align="right" font-size="14px" color="{skin['brandText']}" padding="16px">
          {{{{invoiceItem1Rate}}}}
        </mj-text>
      </mj-column>
      <mj-column width="20%">
        <mj-text align="right" font-size="14px" color="{skin['brandPrimary']}" font-weight="600" padding="16px">
          {{{{invoiceItem1Amount}}}}
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Line item 2 -->
    <mj-section padding="0 24px" border-top="1px solid {skin['brandSecondary']}10">
      <mj-column width="40%">
        <mj-text font-size="14px" color="{skin['brandPrimary']}" font-weight="500" padding="16px 16px 4px">
          {{{{invoiceItem2Name}}}}
        </mj-text>
        <mj-text font-size="12px" color="{skin['brandSecondary']}" padding="0 16px 16px">
          {{{{invoiceItem2Description}}}}
        </mj-text>
      </mj-column>
      <mj-column width="20%">
        <mj-text align="center" font-size="14px" color="{skin['brandText']}" padding="16px">
          {{{{invoiceItem2Qty}}}}
        </mj-text>
      </mj-column>
      <mj-column width="20%">
        <mj-text align="right" font-size="14px" color="{skin['brandText']}" padding="16px">
          {{{{invoiceItem2Rate}}}}
        </mj-text>
      </mj-column>
      <mj-column width="20%">
        <mj-text align="right" font-size="14px" color="{skin['brandPrimary']}" font-weight="600" padding="16px">
          {{{{invoiceItem2Amount}}}}
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Totals -->
    <mj-section padding="16px 24px 0">
      <mj-column width="60%"></mj-column>
      <mj-column width="40%">
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="8px 0">
          <span style="display: inline-block; width: 50%;">Subtotal</span>
          <span style="display: inline-block; width: 50%; text-align: right;">{{{{invoiceSubtotal}}}}</span>
        </mj-text>
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="8px 0">
          <span style="display: inline-block; width: 50%;">Tax ({{{{invoiceTaxRate}}}})</span>
          <span style="display: inline-block; width: 50%; text-align: right;">{{{{invoiceTax}}}}</span>
        </mj-text>
        <mj-divider border-color="{skin['brandPrimary']}" border-width="2px" padding="8px 0" />
        <mj-text font-size="16px" color="{skin['brandPrimary']}" font-weight="700" padding="4px 0">
          <span style="display: inline-block; width: 50%;">Total Due</span>
          <span style="display: inline-block; width: 50%; text-align: right; font-size: 18px;">{{{{invoiceTotal}}}}</span>
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_receipt_summary(skin_name="apple_light"):
    """Convert receipt summary section to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column>
        <!-- Success checkmark -->
        <mj-text align="center" font-size="32px" background-color="#22c55e20" border-radius="50%" padding="16px" css-class="checkmark-circle">
          ✓
        </mj-text>
        <mj-text align="center" font-size="24px" color="{skin['brandPrimary']}" font-weight="700" padding="16px 0 8px">
          Payment Successful
        </mj-text>
        <mj-text align="center" font-size="16px" color="{skin['brandSecondary']}" padding="0 0 24px">
          Receipt #{{{{receiptNumber}}}}
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Amount paid highlight -->
    <mj-section padding="0 24px 24px">
      <mj-column background-color="{skin['brandAccent']}08" border-radius="12px" padding="24px">
        <mj-text align="center" font-size="14px" color="{skin['brandSecondary']}" text-transform="uppercase" letter-spacing="0.5px" padding="0 0 8px">
          Amount Paid
        </mj-text>
        <mj-text align="center" font-size="36px" color="{skin['brandPrimary']}" font-weight="700" padding="0">
          {{{{receiptAmount}}}}
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Transaction details -->
    <mj-section padding="0 24px 24px">
      <mj-column border="1px solid {skin['brandSecondary']}20" border-radius="8px">
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px" border-bottom="1px solid {skin['brandSecondary']}10">
          <span style="display: inline-block; width: 50%;">Transaction ID</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: {skin['brandPrimary']}; font-weight: 500;">{{{{receiptTransactionId}}}}</span>
        </mj-text>
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px" border-bottom="1px solid {skin['brandSecondary']}10">
          <span style="display: inline-block; width: 50%;">Date &amp; Time</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: {skin['brandPrimary']}; font-weight: 500;">{{{{receiptDateTime}}}}</span>
        </mj-text>
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px" border-bottom="1px solid {skin['brandSecondary']}10">
          <span style="display: inline-block; width: 50%;">Payment Method</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: {skin['brandPrimary']}; font-weight: 500;">{{{{receiptPaymentMethod}}}}</span>
        </mj-text>
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px">
          <span style="display: inline-block; width: 50%;">Billed To</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: {skin['brandPrimary']}; font-weight: 500;">{{{{receiptBilledTo}}}}</span>
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Items breakdown -->
    <mj-section padding="0 24px 24px">
      <mj-column>
        <mj-text font-size="14px" color="{skin['brandSecondary']}" text-transform="uppercase" letter-spacing="0.5px" font-weight="600" padding="0 0 12px">
          Items
        </mj-text>
        <mj-text font-size="14px" color="{skin['brandPrimary']}" padding="12px 0" border-bottom="1px solid {skin['brandSecondary']}10">
          <span style="display: inline-block; width: 70%;">{{{{receiptItem1Name}}}}</span>
          <span style="display: inline-block; width: 30%; text-align: right;">{{{{receiptItem1Price}}}}</span>
        </mj-text>
        <mj-text font-size="14px" color="{skin['brandPrimary']}" padding="12px 0" border-bottom="1px solid {skin['brandSecondary']}10">
          <span style="display: inline-block; width: 70%;">{{{{receiptItem2Name}}}}</span>
          <span style="display: inline-block; width: 30%; text-align: right;">{{{{receiptItem2Price}}}}</span>
        </mj-text>
        <mj-text font-size="14px" color="{skin['brandPrimary']}" font-weight="700" padding="12px 0">
          <span style="display: inline-block; width: 70%;">Total</span>
          <span style="display: inline-block; width: 30%; text-align: right; font-size: 16px;">{{{{receiptTotal}}}}</span>
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_delivery_confirmation(skin_name="apple_light"):
    """Convert delivery confirmation section to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <mj-section padding="24px">
      <mj-column background-color="#22c55e10" border-radius="12px" padding="32px 24px">
        <mj-text align="center" font-size="48px" padding="0 0 16px">
          📦
        </mj-text>
        <mj-text align="center" font-size="24px" color="#22c55e" font-weight="700" padding="0 0 8px">
          Delivered!
        </mj-text>
        <mj-text align="center" font-size="16px" color="{skin['brandSecondary']}" padding="0">
          Your package has arrived
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Delivery details card -->
    <mj-section padding="0 24px 24px">
      <mj-column border="1px solid {skin['brandSecondary']}20" border-radius="12px">
        <mj-text font-size="14px" color="{skin['brandSecondary']}" font-weight="600" text-transform="uppercase" letter-spacing="0.5px" background-color="{skin['brandSecondary']}05" padding="16px 20px">
          Delivery Details
        </mj-text>
        <mj-text font-size="12px" color="{skin['brandSecondary']}" text-transform="uppercase" padding="20px 20px 4px">
          Delivered To
        </mj-text>
        <mj-text font-size="14px" color="{skin['brandPrimary']}" font-weight="500" padding="0 20px 16px">
          {{{{deliveryAddress}}}}
        </mj-text>
        <mj-text font-size="12px" color="{skin['brandSecondary']}" text-transform="uppercase" padding="0 20px 4px">
          Delivery Date &amp; Time
        </mj-text>
        <mj-text font-size="14px" color="{skin['brandPrimary']}" font-weight="500" padding="0 20px 16px">
          {{{{deliveryDateTime}}}}
        </mj-text>
        <mj-text font-size="12px" color="{skin['brandSecondary']}" text-transform="uppercase" padding="0 20px 4px">
          Signed By
        </mj-text>
        <mj-text font-size="14px" color="{skin['brandPrimary']}" font-weight="500" padding="0 20px 16px">
          {{{{deliverySignedBy}}}}
        </mj-text>
        <mj-text font-size="12px" color="{skin['brandSecondary']}" text-transform="uppercase" padding="0 20px 4px">
          Tracking Number
        </mj-text>
        <mj-text font-size="14px" color="{skin['brandAccent']}" font-weight="500" padding="0 20px 20px">
          {{{{deliveryTrackingNumber}}}}
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Delivery photo placeholder -->
    <mj-section padding="0 24px 24px">
      <mj-column>
        <mj-text font-size="14px" color="{skin['brandSecondary']}" font-weight="600" text-transform="uppercase" letter-spacing="0.5px" padding="0 0 12px">
          Proof of Delivery
        </mj-text>
        <mj-image src="{IMAGE_PLACEHOLDERS['product']}" alt="Delivery photo" width="300px" border-radius="8px" />
      </mj-column>
    </mj-section>

    <!-- Order summary -->
    <mj-section padding="0 24px 24px">
      <mj-column border="1px solid {skin['brandSecondary']}20" border-radius="8px">
        <mj-text font-size="14px" color="{skin['brandSecondary']}" font-weight="600" text-transform="uppercase" letter-spacing="0.5px" background-color="{skin['brandSecondary']}05" padding="12px 16px">
          Order Summary
        </mj-text>
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px">
          <span style="display: inline-block; width: 50%;">Order Number</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: {skin['brandPrimary']}; font-weight: 500;">{{{{deliveryOrderNumber}}}}</span>
        </mj-text>
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="0 16px 16px">
          <span style="display: inline-block; width: 50%;">Items Delivered</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: {skin['brandPrimary']}; font-weight: 500;">{{{{deliveryItemCount}}}} item(s)</span>
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_appointment_reminder(skin_name="apple_light"):
    """Convert appointment reminder to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <!-- Appointment reminder header -->
    <mj-section padding="24px" background-color="{skin['brandAccent']}10" border-radius="12px">
      <mj-column>
        <mj-image src="{IMAGE_PLACEHOLDERS['icon']}" alt="Calendar" width="64px" padding="0 0 16px" />
        <mj-text align="center" font-size="24px" color="{skin['brandPrimary']}" font-weight="700" padding="0 0 8px">
          {{{{appointmentTitle}}}}
        </mj-text>
        <mj-text align="center" font-size="16px" color="{skin['brandSecondary']}" padding="0 0 24px">
          {{{{appointmentMessage}}}}
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Appointment details card -->
    <mj-section padding="0 24px 24px">
      <mj-column background-color="#ffffff" border-radius="8px" padding="0">
        <mj-text font-size="12px" color="{skin['brandSecondary']}" text-transform="uppercase" letter-spacing="0.5px" padding="20px 20px 4px">
          📅 Date
        </mj-text>
        <mj-text font-size="18px" color="{skin['brandPrimary']}" font-weight="600" padding="0 20px 16px">
          {{{{appointmentDate}}}}
        </mj-text>
        <mj-divider border-color="{skin['brandSecondary']}15" padding="0 20px" />
        <mj-text font-size="12px" color="{skin['brandSecondary']}" text-transform="uppercase" letter-spacing="0.5px" padding="16px 20px 4px">
          ⏰ Time
        </mj-text>
        <mj-text font-size="18px" color="{skin['brandPrimary']}" font-weight="600" padding="0 20px 16px">
          {{{{appointmentTime}}}}
        </mj-text>
        <mj-divider border-color="{skin['brandSecondary']}15" padding="0 20px" />
        <mj-text font-size="12px" color="{skin['brandSecondary']}" text-transform="uppercase" letter-spacing="0.5px" padding="16px 20px 4px">
          📍 Location
        </mj-text>
        <mj-text font-size="16px" color="{skin['brandPrimary']}" padding="0 20px 20px">
          {{{{appointmentLocation}}}}
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Action buttons -->
    <mj-section padding="0 24px 24px">
      <mj-column>
        <mj-button href="{{{{addToCalendarUrl}}}}" background-color="{skin['brandAccent']}" color="#ffffff" font-size="14px" font-weight="600" border-radius="8px" inner-padding="14px 28px">
          Add to Calendar
        </mj-button>
        <mj-button href="{{{{rescheduleUrl}}}}" background-color="transparent" color="{skin['brandAccent']}" font-size="14px" font-weight="600" border-radius="8px" border="2px solid {skin['brandAccent']}" inner-padding="12px 26px">
          Reschedule
        </mj-button>
      </mj-column>
    </mj-section>'''


def section_to_mjml_two_factor_code(skin_name="apple_light"):
    """Convert two-factor authentication code to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <!-- 2FA header -->
    <mj-section padding="24px" background-color="{skin['brandSecondary']}05">
      <mj-column>
        <mj-image src="{IMAGE_PLACEHOLDERS['icon']}" alt="Security Shield" width="80px" padding="0 0 20px" css-class="security-badge" />
        <mj-text align="center" font-size="22px" color="{skin['brandPrimary']}" font-weight="700" padding="0 0 8px">
          Two-Factor Authentication
        </mj-text>
        <mj-text align="center" font-size="15px" color="{skin['brandSecondary']}" padding="0 0 24px">
          Enter this code to verify your identity
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- 2FA Code Display -->
    <mj-section padding="0 24px 24px">
      <mj-column>
        <mj-text align="center" background-color="#ffffff" border="2px solid {skin['brandPrimary']}" border-radius="12px" padding="24px 48px">
          <p style="font-family: 'SF Mono', 'Monaco', 'Consolas', monospace; font-size: 42px; color: {skin['brandPrimary']}; margin: 0; font-weight: 700; letter-spacing: 12px;">{{{{twoFactorCode}}}}</p>
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Expiry warning -->
    <mj-section padding="0 24px 24px">
      <mj-column>
        <mj-text align="center" background-color="#f59e0b15" border-radius="8px" padding="12px 20px" font-size="13px" color="#f59e0b" font-weight="600">
          ⏱ Code expires in {{{{twoFactorExpiry}}}}
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Security notice -->
    <mj-section padding="0 24px 24px">
      <mj-column>
        <mj-divider border-color="{skin['brandSecondary']}15" padding="0 0 24px" />
        <mj-text align="center" font-size="13px" color="{skin['brandSecondary']}" padding="0 0 4px">
          🔒 If you didn't request this code, please ignore this email.
        </mj-text>
        <mj-text align="center" font-size="13px" color="{skin['brandSecondary']}" padding="0">
          Never share this code with anyone.
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_account_suspended(skin_name="apple_light"):
    """Convert account suspended notification to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <!-- Account suspended header -->
    <mj-section padding="24px" background-color="#ef444415" border-radius="12px">
      <mj-column>
        <mj-text align="center" font-size="48px" padding="0 0 16px">
          ⚠️
        </mj-text>
        <mj-text align="center" font-size="24px" color="#ef4444" font-weight="700" padding="0 0 8px">
          Account Suspended
        </mj-text>
        <mj-text align="center" font-size="15px" color="{skin['brandSecondary']}" padding="0 0 24px">
          Your account has been temporarily suspended
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Reason box -->
    <mj-section padding="0 24px 16px">
      <mj-column background-color="#ffffff" border-radius="8px" padding="20px">
        <mj-text font-size="12px" color="{skin['brandSecondary']}" text-transform="uppercase" letter-spacing="0.5px" font-weight="600" padding="0 0 8px">
          Reason for Suspension
        </mj-text>
        <mj-text font-size="15px" color="{skin['brandPrimary']}" line-height="1.6" padding="0">
          {{{{suspensionReason}}}}
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Account details -->
    <mj-section padding="0 24px 24px">
      <mj-column background-color="#ffffff" border-radius="8px" padding="0">
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px 20px">
          <span style="display: inline-block; width: 50%;">Account</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: {skin['brandPrimary']}; font-weight: 500;">{{{{suspendedEmail}}}}</span>
        </mj-text>
        <mj-divider border-color="{skin['brandSecondary']}10" padding="0 20px" />
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px 20px">
          <span style="display: inline-block; width: 50%;">Suspended on</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: {skin['brandPrimary']}; font-weight: 500;">{{{{suspensionDate}}}}</span>
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Action buttons -->
    <mj-section padding="0 24px 24px">
      <mj-column>
        <mj-button href="{{{{appealUrl}}}}" background-color="{skin['brandPrimary']}" color="#ffffff" font-size="14px" font-weight="600" border-radius="8px" inner-padding="14px 32px">
          Appeal This Decision
        </mj-button>
        <mj-text align="center" padding="16px 0 0">
          <a href="{{{{policyUrl}}}}" style="font-family: {skin['brandFont']}; font-size: 13px; color: {skin['brandSecondary']}; text-decoration: underline;">Review our Terms of Service</a>
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_payment_failed(skin_name="apple_light"):
    """Convert payment failed notification to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <!-- Payment failed header -->
    <mj-section padding="24px" background-color="#f59e0b10" border-radius="12px">
      <mj-column>
        <mj-text align="center" font-size="48px" padding="0 0 16px">
          💳
        </mj-text>
        <mj-text align="center" font-size="24px" color="#f59e0b" font-weight="700" padding="0 0 8px">
          Payment Failed
        </mj-text>
        <mj-text align="center" font-size="15px" color="{skin['brandSecondary']}" padding="0 0 24px">
          We couldn't process your payment
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Payment details -->
    <mj-section padding="0 24px 16px">
      <mj-column background-color="#ffffff" border-radius="8px" padding="0">
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px 20px">
          <span style="display: inline-block; width: 50%;">Amount</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: {skin['brandPrimary']}; font-size: 16px; font-weight: 600;">{{{{failedAmount}}}}</span>
        </mj-text>
        <mj-divider border-color="{skin['brandSecondary']}10" padding="0 20px" />
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px 20px">
          <span style="display: inline-block; width: 50%;">Card ending in</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: {skin['brandPrimary']}; font-weight: 500;">•••• {{{{cardLastFour}}}}</span>
        </mj-text>
        <mj-divider border-color="{skin['brandSecondary']}10" padding="0 20px" />
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px 20px">
          <span style="display: inline-block; width: 50%;">Attempted on</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: {skin['brandPrimary']};">{{{{paymentDate}}}}</span>
        </mj-text>
        <mj-divider border-color="{skin['brandSecondary']}10" padding="0 20px" />
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px 20px">
          <span style="display: inline-block; width: 50%;">Reason</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: #ef4444; font-weight: 500;">{{{{failureReason}}}}</span>
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- What happens next -->
    <mj-section padding="0 24px 24px">
      <mj-column background-color="{skin['brandSecondary']}05" border-radius="8px" padding="16px 20px">
        <mj-text font-size="13px" color="{skin['brandSecondary']}" font-weight="600" padding="0 0 4px">
          What happens next?
        </mj-text>
        <mj-text font-size="13px" color="{skin['brandSecondary']}" line-height="1.5" padding="0">
          We'll automatically retry in {{{{retryDays}}}} days. To avoid service interruption, please update your payment method.
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Action buttons -->
    <mj-section padding="0 24px 24px">
      <mj-column>
        <mj-button href="{{{{updatePaymentUrl}}}}" background-color="{skin['brandAccent']}" color="#ffffff" font-size="14px" font-weight="600" border-radius="8px" inner-padding="14px 32px">
          Update Payment Method
        </mj-button>
        <mj-button href="{{{{retryPaymentUrl}}}}" background-color="transparent" color="{skin['brandAccent']}" font-size="14px" font-weight="600" border-radius="8px" border="2px solid {skin['brandAccent']}" inner-padding="12px 26px">
          Retry Payment
        </mj-button>
      </mj-column>
    </mj-section>'''


def section_to_mjml_order_hold(skin_name="apple_light"):
    """Convert order hold notification to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <!-- Order hold header -->
    <mj-section padding="24px" background-color="#fbbf2410" border-radius="12px">
      <mj-column>
        <mj-text align="center" font-size="48px" padding="0 0 16px">
          ⏸️
        </mj-text>
        <mj-text align="center" font-size="24px" color="#fbbf24" font-weight="700" padding="0 0 8px">
          Order On Hold
        </mj-text>
        <mj-text align="center" font-size="15px" color="{skin['brandSecondary']}" padding="0 0 24px">
          We need a bit more information to process your order
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Order details -->
    <mj-section padding="0 24px 16px">
      <mj-column background-color="#ffffff" border-radius="8px" padding="0">
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px 20px">
          <span style="display: inline-block; width: 50%;">Order Number</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: {skin['brandPrimary']}; font-weight: 600;">{{{{orderNumber}}}}</span>
        </mj-text>
        <mj-divider border-color="{skin['brandSecondary']}10" padding="0 20px" />
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px 20px">
          <span style="display: inline-block; width: 50%;">Order Date</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: {skin['brandPrimary']};">{{{{orderDate}}}}</span>
        </mj-text>
        <mj-divider border-color="{skin['brandSecondary']}10" padding="0 20px" />
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px 20px">
          <span style="display: inline-block; width: 50%;">Hold Reason</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: #fbbf24; font-weight: 500;">{{{{holdReason}}}}</span>
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Action required -->
    <mj-section padding="0 24px 16px">
      <mj-column background-color="{skin['brandSecondary']}05" border-radius="8px" padding="16px 20px">
        <mj-text font-size="13px" color="{skin['brandSecondary']}" font-weight="600" padding="0 0 8px">
          Action Required
        </mj-text>
        <mj-text font-size="13px" color="{skin['brandSecondary']}" line-height="1.5" padding="0">
          {{{{holdActionRequired}}}}
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Deadline warning -->
    <mj-section padding="0 24px 16px">
      <mj-column>
        <mj-text align="center" font-size="13px" color="#ef4444">
          ⚠️ Please respond by {{{{holdDeadline}}}} to avoid cancellation
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Action buttons -->
    <mj-section padding="0 24px 24px">
      <mj-column>
        <mj-button href="{{{{resolveHoldUrl}}}}" background-color="{skin['brandAccent']}" color="#ffffff" font-size="14px" font-weight="600" border-radius="8px" inner-padding="14px 32px">
          Resolve Now
        </mj-button>
        <mj-text align="center" padding="16px 0 0">
          <a href="{{{{cancelOrderUrl}}}}" style="font-family: {skin['brandFont']}; font-size: 13px; color: {skin['brandSecondary']}; text-decoration: underline;">Cancel this order</a>
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_subscription_paused(skin_name="apple_light"):
    """Convert subscription paused notification to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <!-- Subscription paused header -->
    <mj-section padding="24px" background-color="{skin['brandSecondary']}08" border-radius="12px">
      <mj-column>
        <mj-text align="center" font-size="48px" padding="0 0 16px">
          ⏸️
        </mj-text>
        <mj-text align="center" font-size="24px" color="{skin['brandPrimary']}" font-weight="700" padding="0 0 8px">
          Subscription Paused
        </mj-text>
        <mj-text align="center" font-size="15px" color="{skin['brandSecondary']}" padding="0 0 24px">
          Your subscription has been paused as requested
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Subscription details -->
    <mj-section padding="0 24px 16px">
      <mj-column background-color="#ffffff" border-radius="8px" padding="0">
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px 20px">
          <span style="display: inline-block; width: 50%;">Plan</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: {skin['brandPrimary']}; font-weight: 600;">{{{{subscriptionPlan}}}}</span>
        </mj-text>
        <mj-divider border-color="{skin['brandSecondary']}10" padding="0 20px" />
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px 20px">
          <span style="display: inline-block; width: 50%;">Paused on</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: {skin['brandPrimary']};">{{{{pauseDate}}}}</span>
        </mj-text>
        <mj-divider border-color="{skin['brandSecondary']}10" padding="0 20px" />
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px 20px">
          <span style="display: inline-block; width: 50%;">Resume date</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: {skin['brandPrimary']};">{{{{resumeDate}}}}</span>
        </mj-text>
        <mj-divider border-color="{skin['brandSecondary']}10" padding="0 20px" />
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px 20px">
          <span style="display: inline-block; width: 50%;">Status</span>
          <span style="display: inline-block; width: 50%; text-align: right;">
            <span style="padding: 4px 12px; background-color: {skin['brandSecondary']}15; border-radius: 12px; font-size: 12px; color: {skin['brandSecondary']}; font-weight: 600;">PAUSED</span>
          </span>
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- What you'll miss -->
    <mj-section padding="0 24px 24px">
      <mj-column background-color="#ffffff" border-radius="8px" border="1px dashed {skin['brandSecondary']}30" padding="16px 20px">
        <mj-text font-size="13px" color="{skin['brandSecondary']}" font-weight="600" padding="0 0 8px">
          While paused, you won't have access to:
        </mj-text>
        <mj-text font-size="13px" color="{skin['brandSecondary']}" line-height="1.8" padding="0">
          • {{{{pausedFeature1}}}}<br/>
          • {{{{pausedFeature2}}}}<br/>
          • {{{{pausedFeature3}}}}
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Action buttons -->
    <mj-section padding="0 24px 24px">
      <mj-column>
        <mj-button href="{{{{resumeNowUrl}}}}" background-color="{skin['brandAccent']}" color="#ffffff" font-size="14px" font-weight="600" border-radius="8px" inner-padding="14px 32px">
          Resume Subscription
        </mj-button>
        <mj-text align="center" padding="16px 0 0">
          <a href="{{{{manageSubscriptionUrl}}}}" style="font-family: {skin['brandFont']}; font-size: 13px; color: {skin['brandSecondary']}; text-decoration: underline;">Manage subscription settings</a>
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_referral_success(skin_name="apple_light"):
    """Convert referral success notification to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <!-- Referral success header -->
    <mj-section padding="24px" background-color="#10b98110" border-radius="12px">
      <mj-column>
        <mj-text align="center" font-size="56px" padding="0 0 16px">
          🎉
        </mj-text>
        <mj-text align="center" font-size="28px" color="#10b981" font-weight="700" padding="0 0 8px">
          Referral Successful!
        </mj-text>
        <mj-text align="center" font-size="16px" color="{skin['brandSecondary']}" padding="0 0 24px">
          {{{{referredFriendName}}}} has joined thanks to you
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Reward earned -->
    <mj-section padding="0 24px 16px">
      <mj-column background-color="#ffffff" border-radius="12px" padding="0">
        <mj-section padding="12px 20px" background-color="#10b981">
          <mj-column>
            <mj-text font-size="12px" color="#ffffff" text-transform="uppercase" letter-spacing="1px" font-weight="600">
              Your Reward
            </mj-text>
          </mj-column>
        </mj-section>
        <mj-section padding="24px">
          <mj-column>
            <mj-text align="center" font-size="48px" color="{skin['brandPrimary']}" font-weight="700" padding="0">
              {{{{referralReward}}}}
            </mj-text>
            <mj-text align="center" font-size="14px" color="{skin['brandSecondary']}" padding="8px 0 0">
              {{{{referralRewardType}}}}
            </mj-text>
          </mj-column>
        </mj-section>
      </mj-column>
    </mj-section>

    <!-- Stats -->
    <mj-section padding="0 24px 16px">
      <mj-column width="50%" background-color="#ffffff" border-radius="8px 0 0 8px" padding="20px">
        <mj-text align="center" font-size="32px" color="{skin['brandPrimary']}" font-weight="700" padding="0">
          {{{{totalReferrals}}}}
        </mj-text>
        <mj-text align="center" font-size="12px" color="{skin['brandSecondary']}" text-transform="uppercase" padding="4px 0 0">
          Total Referrals
        </mj-text>
      </mj-column>
      <mj-column width="50%" background-color="#ffffff" border-radius="0 8px 8px 0" padding="20px" border-left="1px solid {skin['brandSecondary']}10">
        <mj-text align="center" font-size="32px" color="#10b981" font-weight="700" padding="0">
          {{{{totalEarned}}}}
        </mj-text>
        <mj-text align="center" font-size="12px" color="{skin['brandSecondary']}" text-transform="uppercase" padding="4px 0 0">
          Total Earned
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Keep referring -->
    <mj-section padding="0 24px 16px">
      <mj-column background-color="{skin['brandSecondary']}05" border-radius="8px" padding="16px 20px">
        <mj-text font-size="14px" color="{skin['brandPrimary']}" font-weight="600" padding="0 0 4px">
          Keep the referrals coming!
        </mj-text>
        <mj-text font-size="13px" color="{skin['brandSecondary']}" line-height="1.5" padding="0">
          Share your unique link and earn {{{{referralRewardPerReferral}}}} for each friend who signs up.
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Share link -->
    <mj-section padding="0 24px 24px">
      <mj-column background-color="#ffffff" border-radius="8px" border="1px solid {skin['brandSecondary']}20" padding="12px 16px">
        <mj-text font-family="monospace" font-size="13px" color="{skin['brandAccent']}" word-break="break-all">
          {{{{referralLink}}}}
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Action buttons -->
    <mj-section padding="0 24px 24px">
      <mj-column>
        <mj-button href="{{{{shareReferralUrl}}}}" background-color="{skin['brandAccent']}" color="#ffffff" font-size="14px" font-weight="600" border-radius="8px" inner-padding="14px 32px">
          Share With More Friends
        </mj-button>
        <mj-text align="center" padding="16px 0 0">
          <a href="{{{{viewRewardsUrl}}}}" style="font-family: {skin['brandFont']}; font-size: 13px; color: {skin['brandSecondary']}; text-decoration: underline;">View all rewards</a>
        </mj-text>
      </mj-column>
    </mj-section>'''


def section_to_mjml_order_returned(skin_name="apple_light"):
    """Convert order returned notification to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <!-- Order returned header -->
    <mj-section padding="24px" background-color="#10b98110" border-radius="12px">
      <mj-column>
        <mj-text align="center" font-size="48px" padding="0 0 16px">
          📦
        </mj-text>
        <mj-text align="center" font-size="24px" color="#10b981" font-weight="700" padding="0 0 8px">
          Return Received
        </mj-text>
        <mj-text align="center" font-size="15px" color="{skin['brandSecondary']}" padding="0 0 24px">
          We've received your return and are processing your refund
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Return details -->
    <mj-section padding="0 24px 16px">
      <mj-column background-color="#ffffff" border-radius="8px" padding="0">
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px 20px">
          <span style="display: inline-block; width: 50%;">Order number</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: {skin['brandPrimary']}; font-weight: 600;">{{{{orderNumber}}}}</span>
        </mj-text>
        <mj-divider border-color="{skin['brandSecondary']}10" padding="0 20px" />
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px 20px">
          <span style="display: inline-block; width: 50%;">Return ID</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: {skin['brandPrimary']};">{{{{returnId}}}}</span>
        </mj-text>
        <mj-divider border-color="{skin['brandSecondary']}10" padding="0 20px" />
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px 20px">
          <span style="display: inline-block; width: 50%;">Item returned</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: {skin['brandPrimary']};">{{{{returnedItemName}}}}</span>
        </mj-text>
        <mj-divider border-color="{skin['brandSecondary']}10" padding="0 20px" />
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px 20px">
          <span style="display: inline-block; width: 50%;">Refund amount</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: #10b981; font-weight: 600;">{{{{refundAmount}}}}</span>
        </mj-text>
        <mj-divider border-color="{skin['brandSecondary']}10" padding="0 20px" />
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px 20px">
          <span style="display: inline-block; width: 50%;">Refund method</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: {skin['brandPrimary']};">{{{{refundMethod}}}}</span>
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Timeline info -->
    <mj-section padding="0 24px 16px">
      <mj-column background-color="{skin['brandSecondary']}05" border-radius="8px" padding="16px 20px">
        <mj-text font-size="13px" color="{skin['brandSecondary']}" font-weight="600" padding="0 0 4px">
          When will I get my refund?
        </mj-text>
        <mj-text font-size="13px" color="{skin['brandSecondary']}" line-height="1.5" padding="0">
          Your refund will be processed within {{{{refundDays}}}} business days. You'll receive a confirmation email once it's complete.
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Action button -->
    <mj-section padding="0 24px 24px">
      <mj-column>
        <mj-button href="{{{{returnDetailsUrl}}}}" background-color="{skin['brandAccent']}" color="#ffffff" font-size="14px" font-weight="600" border-radius="8px" inner-padding="14px 32px">
          View Return Details
        </mj-button>
      </mj-column>
    </mj-section>'''


def section_to_mjml_account_reactivated(skin_name="apple_light"):
    """Convert account reactivated notification to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <!-- Account reactivated header -->
    <mj-section padding="24px" background-color="#6366f110" border-radius="12px">
      <mj-column>
        <mj-text align="center" font-size="48px" padding="0 0 16px">
          🎉
        </mj-text>
        <mj-text align="center" font-size="24px" color="#6366f1" font-weight="700" padding="0 0 8px">
          Welcome Back!
        </mj-text>
        <mj-text align="center" font-size="15px" color="{skin['brandSecondary']}" padding="0 0 24px">
          Your account has been successfully reactivated
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Account details -->
    <mj-section padding="0 24px 16px">
      <mj-column background-color="#ffffff" border-radius="8px" padding="0">
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px 20px">
          <span style="display: inline-block; width: 50%;">Account</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: {skin['brandPrimary']}; font-weight: 600;">{{{{userEmail}}}}</span>
        </mj-text>
        <mj-divider border-color="{skin['brandSecondary']}10" padding="0 20px" />
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px 20px">
          <span style="display: inline-block; width: 50%;">Status</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: #10b981; font-weight: 600;">Active</span>
        </mj-text>
        <mj-divider border-color="{skin['brandSecondary']}10" padding="0 20px" />
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px 20px">
          <span style="display: inline-block; width: 50%;">Plan</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: {skin['brandPrimary']};">{{{{planName}}}}</span>
        </mj-text>
        <mj-divider border-color="{skin['brandSecondary']}10" padding="0 20px" />
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px 20px">
          <span style="display: inline-block; width: 50%;">Reactivated on</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: {skin['brandPrimary']};">{{{{reactivationDate}}}}</span>
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- What's new section -->
    <mj-section padding="0 24px 16px">
      <mj-column background-color="{skin['brandSecondary']}05" border-radius="8px" padding="16px 20px">
        <mj-text font-size="13px" color="{skin['brandSecondary']}" font-weight="600" padding="0 0 4px">
          While you were away
        </mj-text>
        <mj-text font-size="13px" color="{skin['brandSecondary']}" line-height="1.5" padding="0">
          {{{{whatsNewText}}}}
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Action button -->
    <mj-section padding="0 24px 24px">
      <mj-column>
        <mj-button href="{{{{dashboardUrl}}}}" background-color="{skin['brandAccent']}" color="#ffffff" font-size="14px" font-weight="600" border-radius="8px" inner-padding="14px 32px">
          Go to Dashboard
        </mj-button>
      </mj-column>
    </mj-section>'''


def section_to_mjml_loyalty_tier_upgrade(skin_name="apple_light"):
    """Convert loyalty tier upgrade notification to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <!-- Loyalty tier upgrade header -->
    <mj-section padding="24px" background-color="#fbbf2420" border-radius="12px">
      <mj-column>
        <mj-text align="center" font-size="48px" padding="0 0 16px">
          👑
        </mj-text>
        <mj-text align="center" font-size="24px" color="#f59e0b" font-weight="700" padding="0 0 8px">
          You've Been Upgraded!
        </mj-text>
        <mj-text align="center" font-size="15px" color="{skin['brandSecondary']}" padding="0 0 24px">
          Welcome to {{{{newTierName}}}} status
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Tier change display -->
    <mj-section padding="0 24px 16px">
      <mj-column>
        <mj-text align="center" font-size="14px" color="{skin['brandSecondary']}" padding="12px 24px">
          <span style="display: inline-block; padding: 12px 24px; background-color: {skin['brandSecondary']}10; border-radius: 8px; text-decoration: line-through;">{{{{previousTierName}}}}</span>
          <span style="display: inline-block; padding: 0 16px; font-size: 20px;">→</span>
          <span style="display: inline-block; padding: 12px 24px; background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%); border-radius: 8px; color: #ffffff; font-weight: 600;">{{{{newTierName}}}}</span>
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- New benefits -->
    <mj-section padding="0 24px 16px">
      <mj-column>
        <mj-text align="center" font-size="14px" color="{skin['brandPrimary']}" font-weight="600" padding="0 0 16px">
          Your New Benefits
        </mj-text>
      </mj-column>
    </mj-section>

    <mj-section padding="0 24px 16px">
      <mj-column background-color="#ffffff" border-radius="8px" padding="0">
        <mj-text font-size="14px" color="{skin['brandPrimary']}" padding="14px 20px">
          <span style="margin-right: 8px;">✨</span> {{{{benefit1}}}}
        </mj-text>
        <mj-divider border-color="{skin['brandSecondary']}10" padding="0 20px" />
        <mj-text font-size="14px" color="{skin['brandPrimary']}" padding="14px 20px">
          <span style="margin-right: 8px;">🎁</span> {{{{benefit2}}}}
        </mj-text>
        <mj-divider border-color="{skin['brandSecondary']}10" padding="0 20px" />
        <mj-text font-size="14px" color="{skin['brandPrimary']}" padding="14px 20px">
          <span style="margin-right: 8px;">🚀</span> {{{{benefit3}}}}
        </mj-text>
        <mj-divider border-color="{skin['brandSecondary']}10" padding="0 20px" />
        <mj-text font-size="14px" color="{skin['brandPrimary']}" padding="14px 20px">
          <span style="margin-right: 8px;">💎</span> {{{{benefit4}}}}
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Points info -->
    <mj-section padding="0 24px 16px">
      <mj-column background-color="{skin['brandSecondary']}05" border-radius="8px" padding="16px 20px">
        <mj-text font-size="13px" color="{skin['brandSecondary']}" padding="0">
          <span style="display: inline-block; width: 50%;">Current points balance</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: #f59e0b; font-weight: 600; font-size: 16px;">{{{{pointsBalance}}}} pts</span>
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Action button -->
    <mj-section padding="0 24px 24px">
      <mj-column>
        <mj-button href="{{{{rewardsUrl}}}}" background-color="{skin['brandAccent']}" color="#ffffff" font-size="14px" font-weight="600" border-radius="8px" inner-padding="14px 32px">
          Explore Your Rewards
        </mj-button>
      </mj-column>
    </mj-section>'''


def section_to_mjml_password_changed(skin_name="apple_light"):
    """Convert password changed notification to MJML."""
    skin = DESIGN_SKINS.get(skin_name, DESIGN_SKINS["apple_light"])

    return f'''    <!-- Password changed header -->
    <mj-section padding="24px" background-color="#10b98110" border-radius="12px">
      <mj-column>
        <mj-text align="center" font-size="48px" padding="0 0 16px">
          🔒
        </mj-text>
        <mj-text align="center" font-size="24px" color="#10b981" font-weight="700" padding="0 0 8px">
          Password Changed
        </mj-text>
        <mj-text align="center" font-size="15px" color="{skin['brandSecondary']}" padding="0 0 24px">
          Your password has been successfully updated
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Change details -->
    <mj-section padding="0 24px 16px">
      <mj-column background-color="#ffffff" border-radius="8px" padding="0">
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px 20px">
          <span style="display: inline-block; width: 50%;">Account</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: {skin['brandPrimary']}; font-weight: 600;">{{{{userEmail}}}}</span>
        </mj-text>
        <mj-divider border-color="{skin['brandSecondary']}10" padding="0 20px" />
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px 20px">
          <span style="display: inline-block; width: 50%;">Changed on</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: {skin['brandPrimary']};">{{{{changeDate}}}}</span>
        </mj-text>
        <mj-divider border-color="{skin['brandSecondary']}10" padding="0 20px" />
        <mj-text font-size="14px" color="{skin['brandSecondary']}" padding="16px 20px">
          <span style="display: inline-block; width: 50%;">IP Address</span>
          <span style="display: inline-block; width: 50%; text-align: right; color: {skin['brandPrimary']};">{{{{ipAddress}}}}</span>
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Security warning -->
    <mj-section padding="0 24px 16px">
      <mj-column background-color="#f59e0b10" border-radius="8px" border="1px solid #f59e0b25" padding="16px 20px">
        <mj-text font-size="13px" color="#b45309" padding="0">
          <span style="margin-right: 8px;">⚠️</span>
          <strong>Didn't make this change?</strong><br/>
          If you didn't change your password, your account may be compromised. Please secure your account immediately.
        </mj-text>
      </mj-column>
    </mj-section>

    <!-- Action buttons -->
    <mj-section padding="0 24px 24px">
      <mj-column width="50%">
        <mj-button href="{{{{secureAccountUrl}}}}" background-color="#f59e0b" color="#ffffff" font-size="14px" font-weight="600" border-radius="8px" inner-padding="14px 28px" width="100%">
          Secure My Account
        </mj-button>
      </mj-column>
      <mj-column width="50%">
        <mj-button href="{{{{accountSettingsUrl}}}}" background-color="transparent" color="{skin['brandAccent']}" font-size="14px" font-weight="600" border-radius="8px" border="2px solid {skin['brandAccent']}" inner-padding="12px 28px" width="100%">
          Account Settings
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
    "referral_program": section_to_mjml_referral_program,
    "loyalty_points": section_to_mjml_loyalty_points,
    "gift_card": section_to_mjml_gift_card,
    "subscription_renewal": section_to_mjml_subscription_renewal,
    "wishlist_item": section_to_mjml_wishlist_item,
    "price_alert": section_to_mjml_price_alert,
    "back_in_stock": section_to_mjml_back_in_stock,
    "invoice_details": section_to_mjml_invoice_details,
    "receipt_summary": section_to_mjml_receipt_summary,
    "delivery_confirmation": section_to_mjml_delivery_confirmation,
    "appointment_reminder": section_to_mjml_appointment_reminder,
    "two_factor_code": section_to_mjml_two_factor_code,
    "account_suspended": section_to_mjml_account_suspended,
    "payment_failed": section_to_mjml_payment_failed,
    "order_hold": section_to_mjml_order_hold,
    "subscription_paused": section_to_mjml_subscription_paused,
    "referral_success": section_to_mjml_referral_success,
    "order_returned": section_to_mjml_order_returned,
    "account_reactivated": section_to_mjml_account_reactivated,
    "loyalty_tier_upgrade": section_to_mjml_loyalty_tier_upgrade,
    "password_changed": section_to_mjml_password_changed,
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

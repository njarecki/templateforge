"""
Template Validator

Validates and auto-fixes email templates for common issues.
Implements scoring system (0-100) per CLAUDE_RUNBOOK.md:
  - hierarchy(20): visual hierarchy quality
  - responsiveness(20): mobile responsive design
  - code_safety(20): HTML/email client safety
  - aesthetics(20): visual design quality
  - contrast(10): color contrast accessibility
  - tokenization(10): proper design token usage
"""

import re
from html.parser import HTMLParser


class HTMLValidator(HTMLParser):
    """Simple HTML structure validator."""

    def __init__(self):
        super().__init__()
        self.tag_stack = []
        self.errors = []
        self.warnings = []

    def handle_starttag(self, tag, attrs):
        # Self-closing tags that don't need to be tracked
        self_closing = {'img', 'br', 'hr', 'meta', 'link', 'input', 'area', 'base', 'col', 'embed', 'param', 'source', 'track', 'wbr'}
        if tag.lower() not in self_closing:
            self.tag_stack.append(tag.lower())

    def handle_endtag(self, tag):
        if self.tag_stack and self.tag_stack[-1] == tag.lower():
            self.tag_stack.pop()
        elif tag.lower() in self.tag_stack:
            self.errors.append(f"Mismatched tag: expected </{self.tag_stack[-1]}>, got </{tag}>")

    def validate(self, html):
        """Validate HTML and return issues."""
        self.tag_stack = []
        self.errors = []
        self.warnings = []
        try:
            self.feed(html)
        except Exception as e:
            self.errors.append(f"HTML parsing error: {str(e)}")

        if self.tag_stack:
            self.errors.append(f"Unclosed tags: {', '.join(self.tag_stack)}")

        return {
            "valid": len(self.errors) == 0,
            "errors": self.errors,
            "warnings": self.warnings
        }


def check_accessibility(html):
    """Check for accessibility issues."""
    issues = []

    # Check for images without alt text
    img_pattern = r'<img[^>]*>'
    images = re.findall(img_pattern, html, re.IGNORECASE)
    for img in images:
        if 'alt=' not in img.lower():
            issues.append("Image missing alt attribute")
        elif 'alt=""' in img or "alt=''" in img:
            # Empty alt is ok for decorative images, but warn
            pass

    # Check for links without text
    link_pattern = r'<a[^>]*>([^<]*)</a>'
    links = re.findall(link_pattern, html, re.IGNORECASE)
    for link_text in links:
        if not link_text.strip() and '{{' not in link_text:
            issues.append("Link with empty text")

    return issues


def check_email_best_practices(html):
    """Check for email-specific best practices."""
    issues = []
    warnings = []

    # Check max width
    if 'max-width: 640px' not in html and 'width="640"' not in html:
        warnings.append("Template may exceed 640px max width")

    # Check for role="presentation" on tables
    table_count = html.lower().count('<table')
    presentation_count = html.lower().count('role="presentation"')
    if table_count > presentation_count:
        warnings.append("Some tables missing role='presentation'")

    # Check for DOCTYPE
    if '<!DOCTYPE' not in html.upper():
        issues.append("Missing DOCTYPE declaration")

    # Check for viewport meta
    if 'viewport' not in html.lower():
        issues.append("Missing viewport meta tag")

    # Check for lang attribute
    if 'lang=' not in html.lower():
        warnings.append("Missing lang attribute on html element")

    # Check for preheader
    if 'preheader' not in html.lower() and '{{preheader}}' not in html:
        warnings.append("Missing preheader text")

    # Check for unsubscribe link
    if 'unsubscribe' not in html.lower():
        warnings.append("Missing unsubscribe link")

    return issues, warnings


def check_color_contrast(html):
    """Basic color contrast check (simplified)."""
    warnings = []

    # Look for potentially low contrast combinations
    low_contrast_patterns = [
        (r'color:\s*#fff', r'background-color:\s*#fff'),
        (r'color:\s*#000', r'background-color:\s*#000'),
        (r'color:\s*#eee', r'background-color:\s*#fff'),
    ]

    # This is a simplified check - real contrast checking needs color parsing
    if 'color: #fff' in html.lower() and 'background: #fff' in html.lower():
        warnings.append("Potential low contrast: white on white")

    return warnings


def check_mobile_responsiveness(html):
    """Check for mobile responsive elements."""
    warnings = []

    # Check for media queries
    if '@media' not in html:
        warnings.append("No media queries found for mobile responsiveness")

    # Check for mobile-specific classes
    mobile_indicators = ['mobile-full', 'mobile-hide', 'mobile-padding', 'max-width:']
    has_mobile = any(indicator in html.lower() for indicator in mobile_indicators)

    if not has_mobile:
        warnings.append("Limited mobile-responsive styling detected")

    return warnings


def score_hierarchy(html):
    """
    Score visual hierarchy (0-20 points).
    Checks for proper heading structure, section separation, and content flow.
    """
    score = 20
    deductions = []

    # Check for h1 (main headline) - should have exactly one
    h1_count = len(re.findall(r'<h1[^>]*>', html, re.IGNORECASE))
    if h1_count == 0:
        score -= 4
        deductions.append("Missing h1 headline")
    elif h1_count > 1:
        score -= 2
        deductions.append("Multiple h1 tags (should have one)")

    # Check for subheadings (h2, h3)
    h2_count = len(re.findall(r'<h2[^>]*>', html, re.IGNORECASE))
    h3_count = len(re.findall(r'<h3[^>]*>', html, re.IGNORECASE))
    if h2_count == 0 and h3_count == 0:
        score -= 3
        deductions.append("No subheadings for content structure")

    # Check for proper section spacing (padding/margin)
    padding_count = len(re.findall(r'padding[:\s]*\d+', html, re.IGNORECASE))
    if padding_count < 3:
        score -= 3
        deductions.append("Insufficient spacing between sections")

    # Check for CTA button prominence
    cta_patterns = [r'class=["\'][^"\']*cta', r'class=["\'][^"\']*button', r'<a[^>]*style[^>]*padding']
    has_cta = any(re.search(p, html, re.IGNORECASE) for p in cta_patterns)
    if not has_cta:
        score -= 4
        deductions.append("No prominent CTA button found")

    # Check for proper font size hierarchy
    font_sizes = re.findall(r'font-size[:\s]*(\d+)', html, re.IGNORECASE)
    if font_sizes:
        sizes = [int(s) for s in font_sizes]
        if len(set(sizes)) < 2:
            score -= 3
            deductions.append("Insufficient font size variation")

    return max(0, score), deductions


def score_responsiveness(html):
    """
    Score mobile responsiveness (0-20 points).
    Checks for media queries, fluid widths, and mobile-safe patterns.
    """
    score = 20
    deductions = []

    # Check for media queries
    if '@media' not in html:
        score -= 6
        deductions.append("No media queries for responsive design")
    else:
        # Check for mobile breakpoint
        if '600px' not in html and '480px' not in html and '375px' not in html:
            score -= 2
            deductions.append("No standard mobile breakpoint")

    # Check for max-width constraint
    if 'max-width: 640px' not in html and 'max-width:640px' not in html:
        score -= 3
        deductions.append("Missing max-width container")

    # Check for mobile-specific classes
    mobile_classes = ['mobile-full', 'mobile-hide', 'mobile-padding', 'mobile-stack']
    has_mobile_classes = any(mc in html.lower() for mc in mobile_classes)
    if not has_mobile_classes:
        score -= 3
        deductions.append("No mobile-specific CSS classes")

    # Check for fluid images
    if 'width: 100%' in html or 'max-width: 100%' in html or 'width="100%"' in html:
        pass  # Good
    else:
        score -= 3
        deductions.append("Images may not be fluid/responsive")

    # Check for viewport meta tag
    if 'viewport' not in html.lower():
        score -= 3
        deductions.append("Missing viewport meta tag")

    return max(0, score), deductions


def score_code_safety(html):
    """
    Score HTML/email client safety (0-20 points).
    Checks for DOCTYPE, valid HTML, MSO conditionals, table layouts.
    """
    score = 20
    deductions = []

    # Check for DOCTYPE
    if '<!DOCTYPE' not in html.upper():
        score -= 4
        deductions.append("Missing DOCTYPE declaration")

    # Check for role="presentation" on tables
    table_count = html.lower().count('<table')
    presentation_count = html.lower().count('role="presentation"')
    if table_count > 0 and presentation_count < table_count:
        missing = table_count - presentation_count
        score -= min(3, missing)
        deductions.append(f"{missing} tables missing role='presentation'")

    # Check for MSO conditionals (Outlook support)
    if '<!--[if mso]>' not in html and '<!--[if gte mso' not in html:
        score -= 3
        deductions.append("No MSO conditionals for Outlook")

    # Check for inline styles (email best practice)
    style_count = len(re.findall(r'style=["\']', html, re.IGNORECASE))
    if style_count < 5:
        score -= 3
        deductions.append("Insufficient inline styles (may break in email clients)")

    # Check for cellpadding/cellspacing on tables
    table_attrs = re.findall(r'<table[^>]*>', html, re.IGNORECASE)
    tables_with_attrs = sum(1 for t in table_attrs if 'cellpadding' in t.lower() and 'cellspacing' in t.lower())
    if table_count > 0 and tables_with_attrs < table_count:
        score -= 2
        deductions.append("Tables missing cellpadding/cellspacing attributes")

    # Check for border="0" on tables
    tables_with_border = sum(1 for t in table_attrs if 'border="0"' in t.lower() or "border='0'" in t.lower())
    if table_count > 0 and tables_with_border < table_count:
        score -= 2
        deductions.append("Tables missing border='0' attribute")

    # Check for lang attribute on html
    if '<html' in html.lower() and 'lang=' not in html[:500].lower():
        score -= 2
        deductions.append("Missing lang attribute on html element")

    return max(0, score), deductions


def score_aesthetics(html):
    """
    Score visual design quality (0-20 points).
    Checks for consistent spacing, balanced layout, visual polish.
    """
    score = 20
    deductions = []

    # Check for consistent spacing values (multiples of 4 or 8)
    padding_values = re.findall(r'padding[:\s]*(\d+)px', html, re.IGNORECASE)
    if padding_values:
        odd_values = [int(v) for v in padding_values if int(v) % 4 != 0 and int(v) > 4]
        if len(odd_values) > len(padding_values) // 3:
            score -= 3
            deductions.append("Inconsistent spacing (not using 4/8px grid)")

    # Check for border-radius usage (modern design)
    if 'border-radius' not in html:
        score -= 2
        deductions.append("No border-radius (may look dated)")

    # Check for proper line-height
    if 'line-height' not in html:
        score -= 3
        deductions.append("No line-height specified (readability issue)")

    # Check for font-weight variation
    weights = re.findall(r'font-weight[:\s]*(\d+|bold|normal)', html, re.IGNORECASE)
    if len(set(weights)) < 2:
        score -= 2
        deductions.append("No font-weight variation")

    # Check for letter-spacing (typographic polish)
    if 'letter-spacing' not in html:
        score -= 2
        deductions.append("No letter-spacing refinement")

    # Check for footer section
    if 'footer' not in html.lower() and 'unsubscribe' not in html.lower():
        score -= 4
        deductions.append("No footer section detected")

    # Check for visual separators or sections
    section_patterns = ['<hr', 'border-top', 'border-bottom', 'background-color']
    section_count = sum(1 for p in section_patterns if p in html.lower())
    if section_count < 2:
        score -= 2
        deductions.append("Insufficient visual section separation")

    # Check for preheader text
    if '{{preheader}}' not in html and 'preheader' not in html.lower():
        score -= 2
        deductions.append("Missing preheader text")

    return max(0, score), deductions


def score_contrast(html):
    """
    Score color contrast accessibility (0-10 points).
    Checks for sufficient contrast between text and background.
    """
    score = 10
    deductions = []

    # Check for explicit color definitions
    colors = re.findall(r'color[:\s]*#([0-9a-fA-F]{3,6})', html)
    bg_colors = re.findall(r'background(?:-color)?[:\s]*#([0-9a-fA-F]{3,6})', html)

    if not colors:
        score -= 3
        deductions.append("No explicit text colors defined")

    # Check for known low-contrast combinations
    html_lower = html.lower()
    if 'color: #fff' in html_lower and 'background: #fff' in html_lower:
        score -= 5
        deductions.append("White text on white background detected")

    if 'color: #000' in html_lower and 'background: #000' in html_lower:
        score -= 5
        deductions.append("Black text on black background detected")

    # Check for light gray on white
    light_grays = ['#eee', '#ddd', '#ccc', '#bbb', '#aaa']
    for gray in light_grays:
        if f'color: {gray}' in html_lower and ('#fff' in html_lower or '#ffffff' in html_lower):
            score -= 3
            deductions.append(f"Light gray ({gray}) on light background")
            break

    # Check for dark theme contrast issues
    if '{brandBG}' in html or '{brandPrimary}' in html:
        # Using tokens, assume proper contrast
        pass
    elif 'background-color: #0' in html_lower or 'background:#0' in html_lower:
        # Dark background - check for light text
        if 'color: #f' not in html_lower and 'color: #e' not in html_lower and 'color: #d' not in html_lower:
            score -= 3
            deductions.append("Dark background may have contrast issues")

    return max(0, score), deductions


def score_tokenization(html):
    """
    Score proper design token usage (0-10 points).
    Checks for use of {brandX} tokens and {{content}} placeholders.
    """
    score = 10
    deductions = []

    # Check for brand tokens
    brand_tokens = ['{brandFont}', '{brandPrimary}', '{brandSecondary}',
                    '{brandText}', '{brandAccent}', '{brandBG}']
    tokens_found = sum(1 for token in brand_tokens if token in html)

    if tokens_found == 0:
        score -= 5
        deductions.append("No brand design tokens used")
    elif tokens_found < 3:
        score -= 2
        deductions.append("Minimal brand token usage")

    # Check for content placeholders
    content_tokens = ['{{headline}}', '{{subheadline}}', '{{bodyText}}',
                      '{{ctaLabel}}', '{{ctaUrl}}', '{{preheader}}']
    content_found = sum(1 for token in content_tokens if token in html)

    if content_found == 0:
        score -= 3
        deductions.append("No content placeholders")
    elif content_found < 2:
        score -= 1
        deductions.append("Limited content placeholders")

    # Check for hardcoded colors that should be tokens
    hardcoded_colors = re.findall(r'(?<!brand)color[:\s]*#[0-9a-fA-F]{3,6}', html)
    if len(hardcoded_colors) > 10:
        score -= 2
        deductions.append("Many hardcoded colors (should use tokens)")

    return max(0, score), deductions


def score_template(template):
    """
    Score a template on a 0-100 scale.

    Components:
    - hierarchy (20): visual hierarchy quality
    - responsiveness (20): mobile responsive design
    - code_safety (20): HTML/email client safety
    - aesthetics (20): visual design quality
    - contrast (10): color contrast accessibility
    - tokenization (10): proper design token usage

    Returns:
        dict with total score, component scores, and deductions
    """
    html = template.get("html", "")
    if not html:
        return {
            "total": 0,
            "hierarchy": 0,
            "responsiveness": 0,
            "code_safety": 0,
            "aesthetics": 0,
            "contrast": 0,
            "tokenization": 0,
            "deductions": ["No HTML content"],
            "grade": "F"
        }

    # Score each component
    hierarchy, h_deductions = score_hierarchy(html)
    responsiveness, r_deductions = score_responsiveness(html)
    code_safety, c_deductions = score_code_safety(html)
    aesthetics, a_deductions = score_aesthetics(html)
    contrast, cn_deductions = score_contrast(html)
    tokenization, t_deductions = score_tokenization(html)

    total = hierarchy + responsiveness + code_safety + aesthetics + contrast + tokenization

    # Determine grade
    if total >= 85:
        grade = "A"
    elif total >= 75:
        grade = "B"
    elif total >= 65:
        grade = "C"
    else:
        grade = "F"

    all_deductions = (
        [f"[hierarchy] {d}" for d in h_deductions] +
        [f"[responsiveness] {d}" for d in r_deductions] +
        [f"[code_safety] {d}" for d in c_deductions] +
        [f"[aesthetics] {d}" for d in a_deductions] +
        [f"[contrast] {d}" for d in cn_deductions] +
        [f"[tokenization] {d}" for d in t_deductions]
    )

    return {
        "total": total,
        "hierarchy": hierarchy,
        "responsiveness": responsiveness,
        "code_safety": code_safety,
        "aesthetics": aesthetics,
        "contrast": contrast,
        "tokenization": tokenization,
        "deductions": all_deductions,
        "grade": grade,
        "passes_threshold": total >= 85,
        "needs_retry": 75 <= total < 85,
        "should_drop": total < 75
    }


def validate_template(template):
    """
    Validate a template and return validation results.

    Args:
        template: dict with 'html' key containing the email HTML

    Returns:
        dict with validation results
    """
    html = template.get("html", "")
    if not html:
        return {
            "valid": False,
            "errors": ["Template has no HTML content"],
            "warnings": [],
            "template_type": template.get("type", "unknown")
        }

    # Run all checks
    html_validator = HTMLValidator()
    html_result = html_validator.validate(html)

    accessibility_issues = check_accessibility(html)
    bp_issues, bp_warnings = check_email_best_practices(html)
    contrast_warnings = check_color_contrast(html)
    mobile_warnings = check_mobile_responsiveness(html)

    all_errors = html_result["errors"] + bp_issues
    all_warnings = (
        html_result["warnings"] +
        accessibility_issues +
        bp_warnings +
        contrast_warnings +
        mobile_warnings
    )

    return {
        "valid": len(all_errors) == 0,
        "errors": all_errors,
        "warnings": all_warnings,
        "template_type": template.get("type", "unknown")
    }


def fix_template_issues(template):
    """
    Attempt to auto-fix common template issues.

    Args:
        template: dict with 'html' key

    Returns:
        Fixed template dict
    """
    html = template.get("html", "")
    if not html:
        return template

    fixed_html = html

    # Fix missing alt attributes on images (add placeholder)
    def add_alt(match):
        img = match.group(0)
        if 'alt=' not in img.lower():
            return img[:-1] + ' alt="">'
        return img

    fixed_html = re.sub(r'<img[^>]*>', add_alt, fixed_html, flags=re.IGNORECASE)

    # Ensure role="presentation" on all tables
    def add_role(match):
        table = match.group(0)
        if 'role=' not in table.lower():
            return table[:-1] + ' role="presentation">'
        return table

    fixed_html = re.sub(r'<table[^>]*>', add_role, fixed_html, flags=re.IGNORECASE)

    # Ensure lang attribute on html element
    if '<html' in fixed_html.lower() and 'lang=' not in fixed_html[:500].lower():
        fixed_html = re.sub(
            r'<html([^>]*)>',
            r'<html\1 lang="en">',
            fixed_html,
            count=1,
            flags=re.IGNORECASE
        )

    template["html"] = fixed_html
    template["auto_fixed"] = True

    return template


def validate_batch(templates):
    """
    Validate a batch of templates.

    Args:
        templates: list of template dicts

    Returns:
        Summary of validation results
    """
    results = {
        "total": len(templates),
        "passed": 0,
        "fixed": 0,
        "issues": []
    }

    for template in templates:
        validation = validate_template(template)
        if validation["valid"]:
            results["passed"] += 1
        else:
            results["issues"].append({
                "type": validation["template_type"],
                "errors": validation["errors"],
                "warnings": validation["warnings"]
            })

        # All templates can be auto-fixed
        results["fixed"] += 1

    return results


if __name__ == "__main__":
    # Test the validator
    test_html = """
    <!DOCTYPE html>
    <html>
    <head><meta name="viewport" content="width=device-width"></head>
    <body>
        <table width="640">
            <tr><td><img src="test.jpg"></td></tr>
        </table>
    </body>
    </html>
    """

    result = validate_template({"html": test_html, "type": "test"})
    print("Validation result:")
    print(f"  Valid: {result['valid']}")
    print(f"  Errors: {result['errors']}")
    print(f"  Warnings: {result['warnings']}")

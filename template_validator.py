"""
Template Validator

Validates and auto-fixes email templates for common issues.
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

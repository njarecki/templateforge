"""
TopMail Design System Configuration

Defines all tokens, spacing rules, and design constraints for email templates.
"""

# Layout Rules
MAX_WIDTH = 640
SPACING_INCREMENTS = [8, 12, 16, 24]

# Typography Tokens
TYPOGRAPHY_TOKENS = {
    "brandFont": "{brandFont}",
    "brandText": "{brandText}",
    "brandAccent": "{brandAccent}",
}

# Color Tokens
COLOR_TOKENS = {
    "brandBG": "{brandBG}",
    "brandPrimary": "{brandPrimary}",
    "brandSecondary": "{brandSecondary}",
    "brandText": "{brandText}",
    "brandAccent": "{brandAccent}",
}

# Image Placeholders
IMAGE_PLACEHOLDERS = {
    "hero": "https://via.placeholder.com/640x320",
    "product": "https://via.placeholder.com/300",
    "icon": "https://via.placeholder.com/64",
    "logo": "https://via.placeholder.com/150x50",
    "avatar": "https://via.placeholder.com/80",
}

# Copy Tokens
COPY_TOKENS = {
    "headline": "{{headline}}",
    "subheadline": "{{subheadline}}",
    "bodyText": "{{bodyText}}",
    "ctaLabel": "{{ctaLabel}}",
    "footerText": "{{footerText}}",
    "preheader": "{{preheader}}",
    "productName": "{{productName}}",
    "productPrice": "{{productPrice}}",
    "testimonialQuote": "{{testimonialQuote}}",
    "testimonialAuthor": "{{testimonialAuthor}}",
}

# Design Skin Definitions
DESIGN_SKINS = {
    "linear_dark": {
        "name": "Linear Dark",
        "brandBG": "#0a0a0a",
        "brandPrimary": "#ffffff",
        "brandSecondary": "#888888",
        "brandText": "#ffffff",
        "brandAccent": "#5c6bc0",
        "brandFont": "'Inter', 'Helvetica Neue', sans-serif",
        "borderRadius": "8px",
        "buttonStyle": "solid",
    },
    "apple_light": {
        "name": "Apple Light Minimal",
        "brandBG": "#ffffff",
        "brandPrimary": "#1d1d1f",
        "brandSecondary": "#86868b",
        "brandText": "#1d1d1f",
        "brandAccent": "#0071e3",
        "brandFont": "'SF Pro Display', -apple-system, BlinkMacSystemFont, sans-serif",
        "borderRadius": "12px",
        "buttonStyle": "solid",
    },
    "dtc_pastel": {
        "name": "DTC Pastel",
        "brandBG": "#fef6f0",
        "brandPrimary": "#2d2d2d",
        "brandSecondary": "#666666",
        "brandText": "#2d2d2d",
        "brandAccent": "#e07c5f",
        "brandFont": "'Poppins', 'Helvetica Neue', sans-serif",
        "borderRadius": "24px",
        "buttonStyle": "rounded",
    },
    "editorial_serif": {
        "name": "Editorial Serif",
        "brandBG": "#f8f5f0",
        "brandPrimary": "#1a1a1a",
        "brandSecondary": "#555555",
        "brandText": "#1a1a1a",
        "brandAccent": "#8b4513",
        "brandFont": "'Georgia', 'Times New Roman', serif",
        "borderRadius": "0px",
        "buttonStyle": "outline",
    },
    "brutalist_bold": {
        "name": "Brutalist Bold",
        "brandBG": "#ffff00",
        "brandPrimary": "#000000",
        "brandSecondary": "#333333",
        "brandText": "#000000",
        "brandAccent": "#ff0000",
        "brandFont": "'Impact', 'Arial Black', sans-serif",
        "borderRadius": "0px",
        "buttonStyle": "blocky",
    },
}


def get_base_styles():
    """Returns base CSS styles for email templates."""
    return """
    <style type="text/css">
        /* Reset styles */
        body, table, td, p, a, li { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; }
        table, td { mso-table-lspace: 0pt; mso-table-rspace: 0pt; }
        img { -ms-interpolation-mode: bicubic; border: 0; height: auto; line-height: 100%; outline: none; text-decoration: none; }

        /* Base styles */
        body { margin: 0; padding: 0; width: 100% !important; background-color: {brandBG}; }
        .wrapper { width: 100%; table-layout: fixed; background-color: {brandBG}; }
        .main { max-width: 640px; margin: 0 auto; background-color: {brandBG}; }

        /* Typography */
        .headline { font-family: {brandFont}; font-size: 32px; line-height: 1.2; color: {brandPrimary}; margin: 0; }
        .subheadline { font-family: {brandFont}; font-size: 18px; line-height: 1.4; color: {brandSecondary}; margin: 0; }
        .body-text { font-family: {brandFont}; font-size: 16px; line-height: 1.6; color: {brandText}; margin: 0; }

        /* Buttons */
        .cta-button {
            display: inline-block;
            padding: 16px 32px;
            background-color: {brandAccent};
            color: #ffffff;
            font-family: {brandFont};
            font-size: 16px;
            font-weight: 600;
            text-decoration: none;
            border-radius: 8px;
        }

        /* Mobile responsive */
        @media screen and (max-width: 600px) {
            .main { width: 100% !important; }
            .mobile-full { width: 100% !important; display: block !important; }
            .mobile-hide { display: none !important; }
            .mobile-padding { padding: 16px !important; }
            .headline { font-size: 24px !important; }
            .subheadline { font-size: 16px !important; }
        }
    </style>
    """


def get_outlook_conditionals():
    """Returns Outlook-specific conditional comments."""
    return """
    <!--[if mso]>
    <style type="text/css">
        body, table, td, p, a { font-family: Arial, Helvetica, sans-serif !important; }
    </style>
    <![endif]-->
    """

"""
Reusable Style Templates for Gemini Image Generation

Use these as prefixes or combine them with your content prompts to maintain
consistent style across generations.
"""

# =============================================================================
# STYLE: Hand-drawn Storybook / Educational Worksheet
# =============================================================================
# Extracted from the successful beijing_travel_story image

STORYBOOK_WORKSHEET = """
Hand-drawn storybook worksheet illustration style. Cute comic book aesthetic
with soft watercolor-like colors and slightly whimsical hand-drawn look.
Warm, inviting illustration like a children's travel book or comic.
Cute but not childish - appropriate for high school students.
Educational worksheet feel with clean readable elements.
"""

STORYBOOK_WORKSHEET_DETAILED = """
ARTISTIC STYLE:
- Hand-drawn storybook illustration aesthetic
- Cute comic book style with soft, gentle lines
- Soft watercolor-like colors (not harsh or saturated)
- Slightly whimsical, playful hand-drawn look
- Warm, inviting color palette
- Like a children's travel book or educational comic
- Cute but not childish - appropriate for teens/high schoolers

TECHNICAL STYLE:
- Clean, readable text labels
- Collage-style composition with multiple vignettes
- Small illustrated icons and scenes
- Soft pastel background colors
- Clear visual hierarchy
- Educational worksheet aesthetic
"""

# =============================================================================
# STYLE: Clean Educational Infographic
# =============================================================================

EDUCATIONAL_INFOGRAPHIC = """
Clean, modern educational infographic style. Professional classroom poster
aesthetic with organized sections. Soft pastel colors for visual organization.
Clear readable fonts with proper visual hierarchy. Small cute icons accompany
text elements. Suitable for educational materials and classroom use.
"""

# =============================================================================
# STYLE: Kawaii / Cute Japanese
# =============================================================================

KAWAII_CUTE = """
Kawaii cute Japanese illustration style. Rounded shapes, big expressive eyes,
soft pastel colors. Cheerful and adorable aesthetic. Simple clean lines with
minimal detail. Friendly and approachable character designs.
"""

# =============================================================================
# STYLE: Minimalist Line Art
# =============================================================================

MINIMALIST_LINE = """
Minimalist line art illustration style. Clean single-weight black lines on
white or light background. Simple geometric shapes. Elegant and modern.
Minimal color accents if any. Focus on essential forms only.
"""

# =============================================================================
# STYLE: Vintage Travel Poster
# =============================================================================

VINTAGE_TRAVEL = """
Vintage travel poster illustration style from the 1920s-1950s. Bold flat
colors, simplified shapes, art deco influences. Dramatic compositions with
strong silhouettes. Nostalgic and romantic aesthetic. Bold typography
integration.
"""

# =============================================================================
# STYLE: Watercolor Painting
# =============================================================================

WATERCOLOR_SOFT = """
Soft watercolor painting style. Transparent washes of color, visible paper
texture, organic bleeding edges where colors meet. Delicate and airy feel.
Light pastel palette. Hand-painted aesthetic with natural imperfections.
"""

# =============================================================================
# HELPER: Combine style with content
# =============================================================================

def apply_style(content_prompt: str, style: str = STORYBOOK_WORKSHEET) -> str:
    """
    Combine a style template with content to create a full prompt.

    Args:
        content_prompt: The specific content/subject matter
        style: Style template to apply (defaults to STORYBOOK_WORKSHEET)

    Returns:
        Combined prompt with style + content
    """
    return f"{style.strip()}\n\nCONTENT:\n{content_prompt.strip()}"


def style_match_instruction(reference_description: str = None) -> str:
    """
    Generate instruction text for matching a reference style.

    Args:
        reference_description: Optional description of the reference image

    Returns:
        Instruction text for style matching
    """
    base = """
CRITICAL STYLE CONSISTENCY REQUIREMENT:
Match the EXACT artistic style of the reference image provided. This includes:
- Same line weight and drawing style
- Same color palette and saturation levels
- Same level of detail and simplification
- Same character proportions if applicable
- Same background treatment
- Same overall mood and aesthetic

Do NOT deviate from the reference style. The new image should look like it
was created by the same artist in the same session as the reference.
"""
    if reference_description:
        base += f"\nReference style description: {reference_description}"

    return base

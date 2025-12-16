"""
Core Image Generation Module with Style Reference Support

Features:
- Basic text-to-image generation
- Style-referenced generation (use a reference image to maintain style)
- Image editing/refinement (make small changes to existing images)
"""

import os
import base64
from datetime import datetime
from pathlib import Path
from typing import Optional, Union

from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment")

# Initialize client
client = genai.Client(api_key=API_KEY)

# Default model for image generation
DEFAULT_MODEL = "gemini-2.0-flash-exp"  # Supports multimodal input
IMAGE_MODEL = "gemini-2.0-flash-exp"  # For style reference


def load_image_as_base64(image_path: Union[str, Path]) -> str:
    """Load an image file and return base64 encoded string."""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def load_image_for_api(image_path: Union[str, Path]) -> types.Part:
    """Load an image and prepare it for the Gemini API."""
    path = Path(image_path)

    # Determine mime type
    suffix = path.suffix.lower()
    mime_types = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
        ".gif": "image/gif",
    }
    mime_type = mime_types.get(suffix, "image/png")

    # Load and encode
    with open(path, "rb") as f:
        image_data = f.read()

    return types.Part.from_bytes(data=image_data, mime_type=mime_type)


def generate_image(
    prompt: str,
    output_dir: Union[str, Path] = "output",
    filename_prefix: str = "generated",
    model: str = "gemini-2.0-flash-exp"
) -> Optional[str]:
    """
    Generate an image from a text prompt.

    Args:
        prompt: Text description of the image to generate
        output_dir: Directory to save the output
        filename_prefix: Prefix for the output filename
        model: Model to use for generation

    Returns:
        Path to saved image, or None if generation failed
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    print(f"Generating image...")
    print(f"Model: {model}")

    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=['IMAGE', 'TEXT']
        )
    )

    return _save_response_image(response, output_path, filename_prefix)


def generate_with_style_reference(
    prompt: str,
    reference_image_path: Union[str, Path],
    output_dir: Union[str, Path] = "output",
    filename_prefix: str = "styled",
    model: str = "gemini-2.0-flash-exp"
) -> Optional[str]:
    """
    Generate an image using a reference image for style consistency.

    This sends the reference image along with the prompt, asking the model
    to generate new content in the same artistic style.

    Args:
        prompt: Text description of the NEW content to generate
        reference_image_path: Path to the style reference image
        output_dir: Directory to save the output
        filename_prefix: Prefix for the output filename
        model: Model to use

    Returns:
        Path to saved image, or None if generation failed
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    print(f"Generating with style reference...")
    print(f"Reference: {reference_image_path}")
    print(f"Model: {model}")

    # Load the reference image
    reference_image = load_image_for_api(reference_image_path)

    # Build the style-matching prompt
    style_prompt = f"""
Look at this reference image carefully. I want you to generate a NEW image
that matches the EXACT same artistic style, including:
- Same drawing/illustration style
- Same color palette and saturation
- Same line weights and detail level
- Same overall aesthetic and mood

Generate this new content IN THAT EXACT STYLE:
{prompt}

IMPORTANT: The output should look like it was drawn by the same artist.
Maintain perfect style consistency with the reference.
"""

    # Send both reference image and prompt
    response = client.models.generate_content(
        model=model,
        contents=[reference_image, style_prompt],
        config=types.GenerateContentConfig(
            response_modalities=['IMAGE', 'TEXT']
        )
    )

    return _save_response_image(response, output_path, filename_prefix)


def edit_image(
    image_path: Union[str, Path],
    edit_instructions: str,
    output_dir: Union[str, Path] = "output",
    filename_prefix: str = "edited",
    model: str = "gemini-2.0-flash-exp"
) -> Optional[str]:
    """
    Make edits to an existing image while preserving overall style.

    This is for making SMALL refinements - fixing details, adjusting elements,
    etc. The model will try to preserve the original image's style and most
    of its content.

    Args:
        image_path: Path to the image to edit
        edit_instructions: Description of what to change/fix
        output_dir: Directory to save the output
        filename_prefix: Prefix for the output filename
        model: Model to use

    Returns:
        Path to saved image, or None if generation failed
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    print(f"Editing image: {image_path}")
    print(f"Instructions: {edit_instructions}")
    print(f"Model: {model}")

    # Load the original image
    original_image = load_image_for_api(image_path)

    # Build the edit prompt
    edit_prompt = f"""
Look at this image carefully. I want you to create a MODIFIED version with
these specific changes:

{edit_instructions}

CRITICAL REQUIREMENTS:
1. Keep EVERYTHING ELSE exactly the same as the original
2. Maintain the exact same artistic style, colors, and aesthetic
3. Only change what was specifically requested
4. The edited image should look like a minor revision, not a completely new image
5. Preserve all other elements, layout, and composition

Generate the edited version now.
"""

    response = client.models.generate_content(
        model=model,
        contents=[original_image, edit_prompt],
        config=types.GenerateContentConfig(
            response_modalities=['IMAGE', 'TEXT']
        )
    )

    return _save_response_image(response, output_path, filename_prefix)


def regenerate_similar(
    image_path: Union[str, Path],
    variation_instructions: str = "Create a slight variation",
    output_dir: Union[str, Path] = "output",
    filename_prefix: str = "variation",
    model: str = "gemini-2.0-flash-exp"
) -> Optional[str]:
    """
    Generate a new image that's similar to the original but with variations.

    Use this when you want to try different versions while staying close
    to the original concept and style.

    Args:
        image_path: Path to the reference image
        variation_instructions: What kind of variation to make
        output_dir: Directory to save output
        filename_prefix: Prefix for output filename
        model: Model to use

    Returns:
        Path to saved image, or None if failed
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    print(f"Creating variation of: {image_path}")
    print(f"Instructions: {variation_instructions}")

    # Load the original
    original_image = load_image_for_api(image_path)

    variation_prompt = f"""
Study this image carefully - its style, composition, colors, and content.

Now generate a NEW image that is very similar but with this variation:
{variation_instructions}

Requirements:
- Keep the same artistic style exactly
- Keep the same color palette
- Keep the same general composition and layout
- Keep the same mood and aesthetic
- Make only the requested variation

The result should be recognizably similar to the original.
"""

    response = client.models.generate_content(
        model=model,
        contents=[original_image, variation_prompt],
        config=types.GenerateContentConfig(
            response_modalities=['IMAGE', 'TEXT']
        )
    )

    return _save_response_image(response, output_path, filename_prefix)


def _save_response_image(
    response,
    output_dir: Path,
    filename_prefix: str
) -> Optional[str]:
    """Extract and save image from API response."""
    image_path = None

    for part in response.candidates[0].content.parts:
        if part.text is not None:
            print(f"Model notes: {part.text}")
        elif part.inline_data is not None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{filename_prefix}_{timestamp}.png"
            image_path = output_dir / filename

            image = part.as_image()
            image.save(str(image_path))
            print(f"Image saved to: {image_path}")

    return str(image_path) if image_path else None

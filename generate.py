"""
Gemini Image Generator (Nano Banana Pro)
Generates images using Google's Gemini Image API
"""

import os
import sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables
load_dotenv()

# Configure the API
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    print("Error: GEMINI_API_KEY not found in .env file")
    sys.exit(1)

# Create client with API key
client = genai.Client(api_key=API_KEY)

# Output directory
OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


def generate_image(prompt: str, model_name: str = "gemini-2.5-flash-image") -> str:
    """
    Generate an image from a text prompt using Gemini.

    Args:
        prompt: Text description of the image to generate
        model_name: Model to use

    Returns:
        Path to the saved image file
    """
    print(f"Generating image with prompt: '{prompt}'")
    print(f"Using model: {model_name}")

    # Generate content
    response = client.models.generate_content(
        model=model_name,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=['IMAGE', 'TEXT']
        )
    )

    # Process the response
    image_path = None

    for part in response.candidates[0].content.parts:
        if part.text is not None:
            print(f"Model response: {part.text}")
        elif part.inline_data is not None:
            # Generate filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"generated_{timestamp}.png"
            image_path = OUTPUT_DIR / filename

            # Save using the built-in method
            image = part.as_image()
            image.save(str(image_path))

            print(f"Image saved to: {image_path}")

    return str(image_path) if image_path else None


def main():
    """Main entry point - interactive prompt mode"""
    print("=" * 50)
    print("Gemini Image Generator (Nano Banana)")
    print("=" * 50)
    print("\nModels available:")
    print("  1. gemini-2.5-flash-image (Nano Banana)")
    print("  2. gemini-3-pro-image-preview (Nano Banana Pro)")
    print("  3. imagen-4.0-generate-001 (Imagen 4)")
    print("\nType 'quit' to exit\n")

    # Default model
    current_model = "gemini-2.5-flash-image"

    while True:
        try:
            user_input = input("\nEnter prompt (or 'model' to switch): ").strip()

            if not user_input:
                continue

            if user_input.lower() == 'quit':
                print("Goodbye!")
                break

            if user_input.lower() == 'model':
                print("\nSelect model:")
                print("  1. gemini-2.5-flash-image (Nano Banana)")
                print("  2. gemini-3-pro-image-preview (Nano Banana Pro)")
                print("  3. imagen-4.0-generate-001 (Imagen 4)")
                choice = input("Enter 1, 2, or 3: ").strip()
                if choice == "2":
                    current_model = "gemini-3-pro-image-preview"
                elif choice == "3":
                    current_model = "imagen-4.0-generate-001"
                else:
                    current_model = "gemini-2.5-flash-image"
                print(f"Switched to: {current_model}")
                continue

            # Generate the image
            result = generate_image(user_input, current_model)

            if result:
                print(f"\nSuccess! Image saved to: {result}")
            else:
                print("\nNo image was generated. Try a different prompt.")

        except KeyboardInterrupt:
            print("\n\nInterrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")
            print("Try again with a different prompt.")


if __name__ == "__main__":
    # If command line argument provided, use it as prompt
    if len(sys.argv) > 1:
        prompt = " ".join(sys.argv[1:])
        generate_image(prompt)
    else:
        main()

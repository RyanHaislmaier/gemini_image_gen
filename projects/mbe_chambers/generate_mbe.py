"""
MBE Chamber Visualization Generator
Generates scientific illustrations of MBE growth processes
"""

import os
import sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables from parent gemini_image_gen folder
env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(env_path)

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    print(f"Error: GEMINI_API_KEY not found. Checked: {env_path}")
    sys.exit(1)

client = genai.Client(api_key=API_KEY)

OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


# ============================================================================
# BaTiO3 MBE GROWTH PROMPT
# ============================================================================

BATIO3_MBE_PROMPT = """
Scientific 3D cutaway illustration of a Molecular Beam Epitaxy (MBE) chamber
during BaTiO3 thin film growth. Cross-sectional view showing the interior.

GEOMETRY AND LAYOUT:
- Cylindrical stainless steel UHV chamber, polished interior walls
- At TOP CENTER: Silicon substrate (labeled "Si") mounted face-down on a
  circular heated substrate holder, glowing orange-red at 750°C
- At BOTTOM: Three effusion cells with conical pyrolytic boron nitride crucibles,
  angled 20-30 degrees toward the substrate center

MOLECULAR BEAMS (the key visual element):
- From the "Ba" effusion cell: a CONICAL molecular beam of barium atoms
  (shown as streams of green spheres) diverging upward in a cone shape,
  the cone expanding as it rises toward the substrate
- From the "Ti" effusion cell: a CONICAL molecular beam of titanium atoms
  (shown as streams of blue spheres) also diverging in a cone
- The two conical beams OVERLAP and MIX at the substrate surface
- Each beam shows LINEAR TRAJECTORIES of individual atoms - straight lines
  from source to substrate (no curved paths - this is ballistic transport in vacuum)

OXYGEN SOURCE:
- RF plasma source with glowing pale blue/violet plasma discharge tube
  (labeled "O2 plasma")
- Atomic oxygen stream (small red spheres) directed at substrate
- The oxygen mingles with the metal beams at the growth surface

CRYSTAL GROWTH AT SUBSTRATE (zoomed inset or detail):
- Show the BaTiO3 perovskite crystal lattice forming layer-by-layer
- Cubic unit cells: Ba atoms at corners (green), Ti atom at center (blue),
  O atoms at face centers (red)
- Multiple complete unit cell layers stacked on the Si substrate
- Atoms arriving and locking into lattice positions

RHEED SYSTEM:
- On LEFT SIDE: RHEED electron gun firing a thin bright electron beam at
  grazing incidence (2 degrees) toward the substrate surface
- On RIGHT SIDE: Phosphor RHEED screen (labeled "RHEED screen") displaying
  the diffraction pattern
- The pattern shows VERTICAL STREAKS arranged in a semicircular arc
  (Laue zone pattern) - streaks indicate flat layer-by-layer growth

LABELS (clear text labels with lines pointing to components):
- "Ba" on barium effusion cell
- "Ti" on titanium effusion cell
- "O2 plasma" on oxygen source
- "Si substrate" on the substrate
- "BaTiO3 film" on the growing crystal
- "RHEED gun" and "RHEED screen"

STYLE: Photorealistic scientific illustration, 3D render, dramatic lighting
from the glowing substrate and effusion cells, volumetric rendering of the
molecular beams showing individual atoms in flight, clean technical aesthetic
suitable for a scientific journal cover or textbook. No people, no cartoonish
elements - pure accurate physics visualization.
"""


def generate_image(prompt: str, model: str = "gemini-2.5-flash-image",
                   filename_prefix: str = "mbe") -> str:
    """Generate an image from a prompt."""
    print(f"Generating image...")
    print(f"Model: {model}")
    print(f"Prompt length: {len(prompt)} characters")

    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=['IMAGE', 'TEXT']
        )
    )

    image_path = None

    for part in response.candidates[0].content.parts:
        if part.text is not None:
            print(f"\nModel notes: {part.text}")
        elif part.inline_data is not None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{filename_prefix}_{timestamp}.png"
            image_path = OUTPUT_DIR / filename

            image = part.as_image()
            image.save(str(image_path))
            print(f"\nImage saved to: {image_path}")

    return str(image_path) if image_path else None


def main():
    print("=" * 60)
    print("MBE Chamber Visualization Generator")
    print("=" * 60)

    print("\nPrompt for BaTiO3 MBE Growth:")
    print("-" * 40)
    print(BATIO3_MBE_PROMPT[:500] + "...")
    print("-" * 40)

    print("\nOptions:")
    print("  1. Generate with Nano Banana (gemini-2.5-flash-image)")
    print("  2. Generate with Nano Banana Pro (gemini-3-pro-image-preview)")
    print("  3. Edit prompt first")
    print("  4. Quit")

    choice = input("\nSelect option (1-4): ").strip()

    if choice == "1":
        result = generate_image(BATIO3_MBE_PROMPT, "gemini-2.5-flash-image", "batio3_mbe")
    elif choice == "2":
        result = generate_image(BATIO3_MBE_PROMPT, "gemini-3-pro-image-preview", "batio3_mbe_pro")
    elif choice == "3":
        print("\nCurrent prompt saved in this file. Edit BATIO3_MBE_PROMPT and re-run.")
        return
    else:
        print("Goodbye!")
        return

    if result:
        print(f"\nSuccess! Open the image at: {result}")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--auto":
        # Auto-generate without prompts
        generate_image(BATIO3_MBE_PROMPT, "gemini-2.5-flash-image", "batio3_mbe")
    else:
        main()

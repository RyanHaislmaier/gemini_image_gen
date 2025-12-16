"""
Chinese Class - Beijing Travel Images Generator
Creates educational illustrations for high school Chinese language class
"""

import os
import sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables from gemini_image_gen root
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
# IMAGE 1: BEIJING TRAVEL STORY / CHRONICLE
# ============================================================================

BEIJING_TRAVEL_STORY_PROMPT = """
Hand-drawn storybook worksheet illustration showing an American high school
BOY student's travel chronicle to Beijing, China. Cute comic book style with
soft colors and slightly whimsical hand-drawn aesthetic.

PURPOSE: This is a WORKSHEET - labels are in ENGLISH with blank lines _____
so students can write in the Chinese characters themselves. Make blank lines
LONG and VISIBLE (enough space to write Chinese characters).

LAYOUT: Collage-style composition with multiple vignettes arranged creatively

CENTRAL CHARACTER:
- American teenage BOY (friendly, excited expression)
- Wearing winter clothes (puffy jacket, scarf, warm hat) - it's cold in Beijing!
- Holding a camera in one hand
- Near him: an open passport showing a Chinese visa stamp

MAP ELEMENT (top right corner - KEEP SEPARATE from travel items):
- Stylized hand-drawn map of Beijing
- Beijing is roughly rectangular/square shaped city with ring roads
- Mark these THREE locations with cute icons and PROMINENT ENGLISH labels WITH LONG BLANKS:
  * CENTER: "Forbidden City __________" - rectangular palace complex
  * NORTHWEST: "Summer Palace __________" - by a lake
  * FAR NORTHWEST: "Great Wall __________" - in mountains
- ALL THREE location names MUST have visible blank lines for students to write Chinese
- NO arrows, NO distance labels (like "20km") - just the location names with blanks

LANDMARK VIGNETTES (3 small illustrated scenes - use DIFFERENT vocabulary):
1. Great Wall scene - Boy climbing the steep stone steps, wall winding through
   snowy mountains, watchtowers visible. Label: "to climb __________"
2. Forbidden City scene - Red walls, golden roofs, grand gate with Chinese
   architectural details, boy taking photos. Label: "to take photos __________"
3. Summer Palace scene - Beautiful pavilions by Kunming Lake, Longevity Hill
   in background, traditional Chinese garden scenery. Label: "beautiful __________"

FOOD VIGNETTES (3 small illustrated dishes with ENGLISH labels and blanks):
1. "Peking Duck __________" - Whole roast duck, golden crispy skin, being sliced
2. "Mapo Tofu __________" - Spicy red tofu dish in a bowl with chopsticks
3. "Soup Dumplings __________" - Steamer basket with xiaolongbao dumplings

TRAVEL ITEMS (arrange in BOTTOM LEFT corner, AWAY from the map - NO DUPLICATES):
- Show a PASSPORT (blue book with globe emblem) with label "Passport __________" directly below it
- Show a CAMERA (black DSLR camera) with label "Camera __________" directly below it
- Show a PLANE TICKET (boarding pass with airplane icon) with label "Plane ticket __________" directly below it
- Show WINTER CLOTHES (jacket, scarf, hat, gloves stacked together) with label "Winter clothes __________" directly below it
- NO ARROWS - put each label DIRECTLY UNDERNEATH its item, not connected by arrows
- EVERY item above MUST show a long visible blank line for writing Chinese

TITLE at top: "Beijing Trip __________" (with blank for Chinese)

Speech bubble from boy: "So fun! __________" - position this bubble ABOVE the boy's head,
NOT overlapping any other labels or vignettes

STYLE: Warm, inviting, hand-drawn illustration like a children's travel book
or comic. Soft watercolor-like colors. Cute but not childish - appropriate
for high school students. Educational worksheet style with LONG VISIBLE blank
lines next to English words where students can write Chinese characters.

CRITICAL REQUIREMENT: EVERY English label in this image MUST have a VERY LONG
visible blank line next to it or underneath it. The blank lines must be long
enough to write 2-3 Chinese characters (approximately 3-4cm or 1.5 inches).
Use this length as reference: ______________________ (not short dashes).
This includes: Beijing Trip, So fun, all map locations, all landmark labels,
all food items, and ALL travel items. NO EXCEPTIONS.
"""


# ============================================================================
# IMAGE 2: CHINESE VOCABULARY LESSON - TRAVEL THEME
# ============================================================================

TRAVEL_VOCABULARY_LESSON_PROMPT = """
LANDSCAPE ORIENTATION educational vocabulary poster for high school Chinese
class (students with 2+ years of Chinese study). Travel theme. Wide format.

FORMAT: LANDSCAPE / HORIZONTAL layout (wider than tall, like 16:9 ratio)

STYLE: Clean, modern educational infographic with hand-drawn illustrations.
Sections arranged HORIZONTALLY across the wide page. Cute small icons.

TITLE at top center:
"旅行词汇" (Lǚxíng cíhuì) - Travel Vocabulary
With pinyin above characters

ARRANGE 5 SECTIONS AS COLUMNS ACROSS THE LANDSCAPE PAGE:

SECTION 1 - 交通 (Jiāotōng) TRANSPORTATION:
- 飞机 (fēijī) - airplane [plane icon]
- 高铁 (gāotiě) - high-speed train [train icon]
- 地铁 (dìtiě) - subway [metro icon]
- 出租车 (chūzūchē) - taxi [car icon]
- 公共汽车 (gōnggòng qìchē) - bus [bus icon]

SECTION 2 - 地方 (Dìfang) PLACES:
- 机场 (jīchǎng) - airport
- 火车站 (huǒchē zhàn) - train station
- 旅馆 (lǚguǎn) - hotel
- 景点 (jǐngdiǎn) - scenic spot
- 博物馆 (bówùguǎn) - museum

SECTION 3 - 旅行用品 (Lǚxíng yòngpǐn) TRAVEL ITEMS:
- 护照 (hùzhào) - passport
- 签证 (qiānzhèng) - visa
- 行李 (xíngli) - luggage
- 相机 (xiàngjī) - camera
- 地图 (dìtú) - map

SECTION 4 - 常用句子 (Chángyòng jùzi) USEFUL PHRASES:
- 我想去... (Wǒ xiǎng qù...) - I want to go to...
- ...在哪里? (...zài nǎlǐ?) - Where is...?
- 多少钱? (Duōshao qián?) - How much?
- 太贵了 (Tài guì le) - Too expensive
- 可以拍照吗? (Kěyǐ pāizhào ma?) - Can I take photos?

SECTION 5 - 北京景点 (Běijīng jǐngdiǎn) BEIJING:
- 长城 (Chángchéng) - Great Wall
- 故宫 (Gùgōng) - Forbidden City
- 颐和园 (Yíhéyuán) - Summer Palace
- 天安门 (Tiān'ānmén) - Tiananmen
- 天坛 (Tiāntán) - Temple of Heaven

DESIGN:
- WIDE LANDSCAPE format, sections as vertical columns side by side
- Soft pastel colors for each section column
- Chinese characters large and clear with pinyin
- Small cute icons next to vocabulary words
- Clean readable fonts
- Subtle Chinese cloud pattern border

Professional WIDE classroom poster style, visually engaging.
"""


def generate_image(prompt: str, model: str = "gemini-3-pro-image-preview",
                   filename_prefix: str = "chinese") -> str:
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
    print("Chinese Class - Beijing Travel Image Generator")
    print("=" * 60)

    print("\nAvailable prompts:")
    print("  1. Beijing Travel Story (storybook style)")
    print("  2. Travel Vocabulary Lesson (educational poster)")
    print("  3. Generate BOTH images")
    print("  4. Quit")

    choice = input("\nSelect option (1-4): ").strip()

    if choice == "1":
        result = generate_image(BEIJING_TRAVEL_STORY_PROMPT,
                               "gemini-3-pro-image-preview",
                               "beijing_travel_story")
        if result:
            print(f"\nSuccess! Open: {result}")

    elif choice == "2":
        result = generate_image(TRAVEL_VOCABULARY_LESSON_PROMPT,
                               "gemini-3-pro-image-preview",
                               "travel_vocabulary")
        if result:
            print(f"\nSuccess! Open: {result}")

    elif choice == "3":
        print("\n--- Generating Travel Story ---")
        result1 = generate_image(BEIJING_TRAVEL_STORY_PROMPT,
                                "gemini-3-pro-image-preview",
                                "beijing_travel_story")

        print("\n--- Generating Vocabulary Lesson ---")
        result2 = generate_image(TRAVEL_VOCABULARY_LESSON_PROMPT,
                                "gemini-3-pro-image-preview",
                                "travel_vocabulary")

        print("\n=== DONE ===")
        if result1:
            print(f"Travel Story: {result1}")
        if result2:
            print(f"Vocabulary: {result2}")
    else:
        print("Goodbye!")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--story":
            generate_image(BEIJING_TRAVEL_STORY_PROMPT,
                          "gemini-3-pro-image-preview",
                          "beijing_travel_story")
        elif sys.argv[1] == "--vocab":
            generate_image(TRAVEL_VOCABULARY_LESSON_PROMPT,
                          "gemini-3-pro-image-preview",
                          "travel_vocabulary")
        elif sys.argv[1] == "--both":
            generate_image(BEIJING_TRAVEL_STORY_PROMPT,
                          "gemini-3-pro-image-preview",
                          "beijing_travel_story")
            generate_image(TRAVEL_VOCABULARY_LESSON_PROMPT,
                          "gemini-3-pro-image-preview",
                          "travel_vocabulary")
    else:
        main()

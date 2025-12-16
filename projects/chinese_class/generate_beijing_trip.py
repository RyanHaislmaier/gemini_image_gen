"""
Chinese Class - Beijing Travel Images Generator
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
# IMAGE 1: BEIJING TRAVEL STORY WORKSHEET
# ============================================================================

BEIJING_TRAVEL_STORY_PROMPT = """
Create a hand-drawn storybook worksheet illustration about an American high
school BOY student's travel chronicle to Beijing, China.

PURPOSE: This is a WORKSHEET - all labels in ENGLISH with blank lines _____
where students can write Chinese characters. Blank lines must be LONG and VISIBLE.

LAYOUT: Collage-style composition with multiple vignettes arranged together

CENTRAL CHARACTER:
- American teenage BOY (brown hair, friendly, excited expression)
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
2. Forbidden City scene - Red walls, golden roofs, boy taking photos of the
   grand palace entrance. Label: "to take photos __________"
3. Summer Palace scene - Traditional pavilions by a frozen lake, beautiful
   garden scenery. Label: "beautiful __________"

FOOD VIGNETTES (3 Beijing dishes with English labels + blanks):
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
Create a LANDSCAPE (wide, horizontal) educational vocabulary poster for a
high school Chinese language class. Travel theme.

FORMAT: LANDSCAPE orientation (wider than tall), like a classroom poster
Aspect ratio approximately 16:9 or 3:2 (WIDE)

TITLE AT TOP: "旅行词汇" (Lǚxíng cíhuì) - Travel Vocabulary
Include pinyin pronunciation under the Chinese title

LAYOUT: 5 COLUMNS arranged horizontally across the wide format:

COLUMN 1 - 交通 (Jiāotōng) TRANSPORTATION:
- 飞机 (fēijī) - airplane [small airplane icon]
- 高铁 (gāotiě) - high-speed train [bullet train icon]
- 地铁 (dìtiě) - subway [metro icon]
- 出租车 (chūzūchē) - taxi [yellow taxi icon]
- 公共汽车 (gōnggòng qìchē) - bus [bus icon]

COLUMN 2 - 地方 (Dìfang) PLACES:
- 机场 (jīchǎng) - airport [airport icon]
- 火车站 (huǒchē zhàn) - train station [station icon]
- 旅馆 (lǚguǎn) - hotel [hotel building icon]
- 景点 (jǐngdiǎn) - scenic spot [camera/landmark icon]
- 博物馆 (bówùguǎn) - museum [museum building icon]

COLUMN 3 - 旅行用品 (Lǚxíng yòngpǐn) TRAVEL ITEMS:
- 护照 (hùzhào) - passport [passport icon]
- 签证 (qiānzhèng) - visa [visa stamp icon]
- 行李 (xíngli) - luggage [suitcase icon]
- 相机 (xiàngjī) - camera [camera icon]
- 地图 (dìtú) - map [folded map icon]

COLUMN 4 - 常用句子 (Chángyòng jùzi) USEFUL PHRASES:
- 我想去... (Wǒ xiǎng qù...) - I want to go to...
- ...在哪里? (...zài nǎlǐ?) - Where is...?
- 多少钱? (Duōshao qián?) - How much?
- 太贵了 (Tài guì le) - Too expensive
- 可以拍照吗? (Kěyǐ pāizhào ma?) - Can I take photos?

COLUMN 5 - 北京景点 (Běijīng jǐngdiǎn) BEIJING ATTRACTIONS:
- 长城 (Chángchéng) - Great Wall [wall icon]
- 故宫 (Gùgōng) - Forbidden City [palace icon]
- 颐和园 (Yíhéyuán) - Summer Palace [garden icon]
- 天安门 (Tiān'ānmén) - Tiananmen [gate icon]
- 天坛 (Tiāntán) - Temple of Heaven [temple icon]

DESIGN STYLE:
- Clean, organized educational poster layout
- Soft pastel colors for each section/column (different color per column)
- Small cute icons next to each vocabulary word
- Clear, readable fonts
- Chinese characters prominent, pinyin smaller below, English translation
- Appropriate for high school classroom display
- Modern, appealing design that students would find engaging
"""


def generate_image(prompt: str, filename_prefix: str = "image"):
    """Generate an image using Gemini API"""
    print("Generating image...")
    print(f"Model: gemini-3-pro-image-preview")
    print(f"Prompt length: {len(prompt)} characters")

    response = client.models.generate_content(
        model="gemini-3-pro-image-preview",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=['IMAGE', 'TEXT']
        )
    )

    # Save the generated image
    for part in response.candidates[0].content.parts:
        if part.text is not None:
            print(f"Model response: {part.text}")
        elif part.inline_data is not None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{filename_prefix}_{timestamp}.png"
            filepath = OUTPUT_DIR / filename

            image = part.as_image()
            image.save(str(filepath))
            print(f"\nImage saved to: {filepath}")
            return str(filepath)

    return None


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--story":
            generate_image(BEIJING_TRAVEL_STORY_PROMPT, "beijing_travel_story")
        elif sys.argv[1] == "--vocab":
            generate_image(TRAVEL_VOCABULARY_LESSON_PROMPT, "travel_vocabulary")
        else:
            print("Usage:")
            print("  python generate_beijing_trip.py --story  # Beijing travel worksheet")
            print("  python generate_beijing_trip.py --vocab  # Vocabulary poster")
    else:
        print("Usage:")
        print("  python generate_beijing_trip.py --story  # Beijing travel worksheet")
        print("  python generate_beijing_trip.py --vocab  # Vocabulary poster")

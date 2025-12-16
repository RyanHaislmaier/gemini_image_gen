# Gemini Image Generation Workspace

This workspace uses Google's Gemini API (Nano Banana / Nano Banana Pro) to generate images from text prompts.

## Setup

- **API Key**: Stored in `.env` as `GEMINI_API_KEY`
- **Virtual Environment**: `venv/` with `google-genai`, `Pillow`, `python-dotenv`

## Available Models

| Model ID | Name | Best For |
|----------|------|----------|
| `gemini-2.5-flash-image` | Nano Banana | Fast generation, iteration |
| `gemini-3-pro-image-preview` | Nano Banana Pro | Highest quality, final images |
| `imagen-4.0-generate-001` | Imagen 4 | Alternative high-quality |

## Usage

### Quick Generate (main script)
```bash
cd gemini_image_gen
venv/Scripts/python generate.py "your prompt here"
```

### Interactive Mode
```bash
venv/Scripts/python generate.py
```

## Projects

Each project lives in `projects/<project_name>/` with its own `generate_<name>.py` and `output/` folder.

### MBE Chambers (`projects/mbe_chambers/`)

Scientific visualization of Molecular Beam Epitaxy crystal growth.

```bash
cd projects/mbe_chambers
../../venv/Scripts/python generate_mbe.py
```

**Key prompt elements for MBE accuracy:**
- Conical molecular beams with LINEAR atom trajectories (ballistic transport)
- Effusion cells at bottom, substrate at top (face-down)
- RHEED: grazing incidence electron beam, vertical STREAKS on phosphor screen (not spots)
- RF oxygen plasma source (blue/violet glow)
- BaTiO3 perovskite: Ba at corners, Ti at center, O at face centers

## Prompt Engineering Tips

1. **Be specific about geometry** - describe spatial relationships clearly
2. **Use scientific terminology** - models understand technical terms
3. **Specify what NOT to include** - "no people", "no cartoonish elements"
4. **Include render style keywords** - "photorealistic", "Octane render", "volumetric lighting"
5. **Request labels** - models can add text labels to diagrams
6. **Describe physics accurately** - linear trajectories, conical beams, etc.

## IMPORTANT: Rules for Editing Prompts

When the user asks to FIX or ADJUST an existing prompt:

1. **MINIMAL CHANGES ONLY** - Only change what the user specifically asked for
2. **PRESERVE THE STYLE** - Keep the same artistic style, tone, and descriptions
3. **PRESERVE CHARACTER DETAILS** - If there's a boy, keep it a boy. If specific clothing, keep it.
4. **DON'T REMOVE CONTENT** - Unless explicitly asked, don't remove elements that were working
5. **ASK IF UNCLEAR** - If the fix could be interpreted multiple ways, ask before changing

### Common Fix Requests (do ONLY these):
- "Remove duplicates" → Remove only the duplicate, keep one instance
- "Add underlines/blanks" → Add _____ after words, don't change anything else
- "Change X to Y" → Only change that specific word/phrase
- "Use different vocab" → Change vocabulary in specified section only

### DON'T Do These Unless Asked:
- Don't simplify or shorten the prompt
- Don't change character gender, age, or appearance
- Don't remove descriptive details about style
- Don't restructure the layout

## Output

Generated images are saved to `output/` (main) or `projects/<name>/output/` with timestamps.

## Projects

### Chinese Class (`projects/chinese_class/`)

Educational illustrations for Chinese language class.

**Key rules for worksheet images:**
- Student character: American teenage BOY
- All English labels need blank lines _____ for students to write Chinese
- Blanks must be LONG ENOUGH for Chinese characters (visible space)
- Style: warm, hand-drawn, soft watercolors, cute comic book style
- Keep the collage layout with map, mini-pictures, food, travel items

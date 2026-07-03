# AI Short Drama & AI Comic Drama (漫剧) Screenplay Format

> **Important**: This file is an optional production-format reference. For normal short-drama script delivery, use `references/script-structure.md` first: plain-text Chinese delivery format (`角色：台词`, `△动作`, `角色VO：`, `角色（OS）：`). Do not use tables, quote boxes, code blocks, or separate dialogue/narration boxes for normal正文. Load this file only when the user explicitly requests American screenplay, panel tables, anime blocks, or AI prompt tables.

## Table of Contents

1. Format Type Selection (Choose Correct Format)
2. AI Live-Action Short Drama Format
3. AI Comic Drama (漫剧) Format
4. AI Anime Short Drama Format
5. Universal Standards (All Formats)
6. AI Image Prompt Standards
7. Character Consistency Bible
8. Shot Size Vocabulary
9. Camera Movement & Effect Notation
10. Common Format Mistakes

---

## 1. Format Type Selection

Choose the correct format based on your production type:

| Production Type | Visual Style | Format Section | AI Tool Chain |
|----------------|-------------|----------------|---------------|
| AI Live-Action | Photorealistic | Section 2 | MJ/SD/KL → Video AI |
| AI Comic Drama (漫剧) | Comic/illustration panels | Section 3 | MJ/SD/即梦 → Motion |
| AI Anime | Anime/cel-shaded | Section 4 | MJ/SD/即梦 → Seedance |
| AI Visual Novel | Static image + text | Section 3 | MJ/SD → Engine |

**Critical**: Never mix formats within one project. Pick one format type and use it consistently for all episodes.

---

## 2. AI Live-Action Short Drama Format (Optional American Screenplay)

Use this format only when the deliverable is an American screenplay-style draft or a production conversion for photorealistic imagery. It is not the default正文 format.

### Standard Scene Header

```
                         REELSHORT ORIGINAL

                    "THE CONTRACT WIFE"

                           EPISODE 7

FADE IN:

INT. MANHATTAN PENTHOUSE - NIGHT

SARAH (28, tailored burgundy dress, jaw set with determination)
slams the manila folder onto the marble counter. Her husband —
JACK (35, loosened tie, the guilt already pooling in his eyes) —
doesn't reach for it.

                    SARAH
          Sign it. Or I'll make sure the only 
          board you sit on is a park bench.

Jack's jaw tightens. He picks up the folder, flips it open — 
stops. His face drains.

                    JACK
          Where did you get this?

Sarah smiles. It's not kind.

                    SARAH
          I know people too, Jack.

She turns for the door. Jack's hand shoots out — grabs her wrist.

                    JACK
          (desperate)
          Sarah, wait—

The door OPENS before she touches the handle. A WOMAN (25, 
blonde, Chanel suit, frozen in the doorway) stares at them —
at Jack's hand on Sarah's wrist, at the folder, at the terror 
on Jack's face.

                    WOMAN
          ...Am I interrupting something?

Sarah looks from the woman to Jack. The realization hits her 
like a freight train. She doesn't blink. She doesn't cry.

                    SARAH
          (cold, to the woman)
          Take him. He's all yours.

She walks out. The door clicks shut behind her. The woman turns
to Jack, confused. Jack stares at the closed door, the folder 
still in his hand, his world collapsing in slow motion.

                    FADE OUT.
```

### Format Rules (Live-Action)

| Element | Rule | Example |
|---------|------|---------|
| **Slugline** | INT./EXT. + LOCATION + TIME | `INT. MANHATTAN PENTHOUSE - NIGHT` |
| **Character intro** | NAME (age, 2-3 descriptors) | `SARAH (28, burgundy dress, jaw set)` |
| **Dialogue** | NAME centered, ALL CAPS | `SARAH` (not `Sarah`) |
| **Parentheticals** | Delivery note, use sparingly | `(desperate)`, `(beat)` |
| **Action** | Present tense, visual, 3-4 lines max | `She slams the folder onto the counter.` |
| **V.O.** | Voiceover only when essential | `SARAH (V.O.)` |
| **O.S.** | Off-screen | `JACK (O.S.)` |
| **Transitions** | Use sparingly | `FADE IN:`, `CUT TO:`, `SMASH CUT TO:` |

---

## 3. AI Comic Drama (漫剧) Panel Production Format

Use this table format for AI-generated comic/illustration production only when the user asks for panels, image prompts, or a visual-novel implementation. Do not use it for ordinary Chinese short-drama script正文.

### Master Table Format (Per Episode)

Every episode must be presented as a structured table:

```
# "THE ALPHA'S REJECTED MATE"
## EPISODE 7

### EPISODE INFO
- Duration: 75 seconds
- Panels: 18-20
- Card: First Card (Ep 6-10 boundary)
- Emotional Tone: Betrayal → Shock → Resolve
- Style: Korean webtoon, painterly, dramatic lighting

---

| Panel | Shot | Visual Description | AI Prompt | Dialogue / Caption | SFX | BGM |
|-------|------|-------------------|-----------|-------------------|-----|-----|
| 1 | CU | ELARA (19, silver hair, teal eyes, torn dress) kneels in the rain. Mud on her cheek. Pack house behind her — warm light, she's outside it. | CU, 19yo woman kneeling in heavy rain, long silver hair plastered to face, teal eyes wide with shock, torn dark dress, mud on cheek, blurred warm-lit mansion behind, cold blue lighting, painterly webtoon style, dramatic chiaroscuro, rain droplets visible, heartbreak emotion, 8k --ar 9:16 | (Caption: The night I was rejected... everything changed.) | Rain, thunder crack | Piano, minor key |
| 2 | MCU | Close on ELARA's face. Eyes welling with tears she refuses to shed. Jaw clenched. | MCU, 19yo woman's face in rain, teal eyes filling with tears, jaw clenched defiantly, silver hair wet strands across forehead, torn dress visible at shoulders, cold blue and warm orange contrast lighting, painterly webtoon style, emotional intensity, 8k --ar 9:16 | ELARA (V.O.): He said I was worthless. | Rain continues | Piano swells |
| 3 | WS | KELLEN (28, dark hair, broad shoulders, Alpha's gold insignia on chest) stands on the porch above her. Looking down. No emotion. | WS, tall muscular man standing on mansion porch looking down, dark hair, broad shoulders, golden wolf insignia on black coat, cold expression looking downward, rain falling, warm amber light behind him contrasting with cold blue rain, painterly webtoon style, power dynamic, 8k --ar 9:16 | KELLEN: You are not my fated mate. Leave. | Thunder | Low bass drone |
| 4 | CU | ELARA's hands — clenched into fists in the mud. Knuckles white. | CU, woman's hands clenched into fists in muddy ground, knuckles white with tension, rain hitting mud, silver hair falling around shoulders, cold blue lighting, painterly webtoon style, determination, 8k --ar 9:16 | (Caption: But he forgot — I don't break.) | Rain | Beat drop |
| 5 | WS | ELARA stands up. Slow. Rain pouring off her. She's small but unbowed. | WS, young woman standing up from kneeling position in heavy rain, long silver hair flowing, torn dark dress, head lifted defiantly, rain pouring, dark forest behind, blue-purple lighting, painterly webtoon style, empowerment moment, 8k --ar 9:16 | ELARA: You'll regret this, Kellen. | Rain, thunder | Music builds |
| 6 | CU | KELLEN's eyes — a flicker of something. Doubt? Then it hardens. | CU, man's eyes close-up, dark intense eyes, brief flicker of doubt then cold resolve, golden light on face, painterly webtoon style, internal conflict, 8k --ar 9:16 | KELLEN: (cold) I doubt that very much. | --- | --- |
| 7 | WS | ELARA turns. Walks away into the dark forest. Alone. | WS, young woman walking away into dark forest, long silver hair flowing behind, torn dark dress, rain-soaked, solitary figure, trees closing around her, cold blue-purple lighting, painterly webtoon style, departure scene, 8k --ar 9:16 | (Caption: That was six months ago.) | Rain fading | Music shifts — time passage |
| 8 | CU | TITLE CARD: "Six Months Later" — elegant, gothic font over dark background. | Title card text "Six Months Later", elegant gothic calligraphy font, dark textured background with subtle wolf silhouette, gold and deep purple color scheme, painterly webtoon style, cinematic title, 8k --ar 9:16 | --- | Whoosh | Music transition |
| 9 | WS | ELARA — unrecognizable. White gown that flows like moonlight. Confident stance. Grand ballroom behind her. | WS, transformed young woman in flowing white gown, long silver hair styled elegantly, teal eyes confident and bright, standing in grand ballroom entrance, crystal chandeliers, golden warm lighting, painterly webtoon style, glow-up reveal, 8k --ar 9:16 | (Caption: Now? He doesn't even recognize me.) | Ballroom ambience | Upbeat, triumphant |
| 10 | MCU | ELARA enters the ballroom. Heads turn. Conversations stop. | MCU, elegant young woman walking into ballroom, white gown flowing, silver hair catching light, teal eyes scanning room confidently, guests in background turning heads, golden warm lighting, painterly webtoon style, entrance scene, 8k --ar 9:16 | GUEST (O.S.): Who is she? | Chatter stops | Music swells |
| 11 | CU | KELLEN — across the room. He freezes. His wine glass halfway to his lips. Recognition dawning. | CU, man's face across ballroom, wine glass paused at lips, dark eyes widening in recognition, shock expression, golden lighting, blurred ballroom behind, painterly webtoon style, dramatic realization, 8k --ar 9:16 | (Caption: But he will.) | --- | Tension chord |
| 12 | MCU | ELARA smiles at a GUEST (45, wealthy, dazzled). She touches his arm. Kellen watches from across the room. Jaw tight. | MCU, elegant young woman smiling at wealthy older gentleman, hand lightly on his arm, white gown elegant, in background tall dark-haired man watching with tightened jaw, grand ballroom setting, golden lighting, painterly webtoon style, jealousy setup, 8k --ar 9:16 | ELARA: (warm, to Guest) You're too kind. | Chatter resumes | Upbeat continues |
| 13 | CU | KELLEN's hand — crushing the wine glass stem. White knuckles. | CU, man's hand gripping wine glass stem tightly, white knuckles, golden light on hand, painterly webtoon style, suppressed rage, 8k --ar 9:16 | --- | Glass stress sound | Low rumble |
| 14 | WS | KELLEN starts across the ballroom. Determined. Guests part. | WS, tall muscular man striding across ballroom, black formal coat with gold insignia, determined expression, guests parting, grand ballroom with chandeliers, golden warm lighting, painterly webtoon style, purposeful walk, 8k --ar 9:16 | (Caption: The hunter just became the prey.) | Footsteps | Tension builds |
| 15 | MCU | KELLEN reaches Elara. She turns. Their eyes meet. Her smile doesn't waver — but it's ice now. | MCU, elegant woman turning to face approaching man, teal eyes meeting dark eyes, smile turning cold, white gown vs black coat, grand ballroom background blurred, golden lighting, painterly webtoon style, confrontation, 8k --ar 9:16 | KELLEN: (quiet, intense) Elara. | Music stops | Silence — then pulse |
| 16 | CU | ELARA's face. She tilts her head. Pretending to think. | CU, elegant woman's face with playful tilted head, teal eyes calculating, slight mocking smile, silver hair styled with crystal pins, golden lighting, painterly webtoon style, power shift, 8k --ar 9:16 | ELARA: (mocking) I'm sorry. Do I know you? | --- | Beat |
| 17 | CU | KELLEN's face. Struck. Then — something else. Something he didn't expect. Respect? Desire? | CU, man's face close-up, initial shock morphing into unexpected respect and attraction, dark eyes intense, golden lighting, painterly webtoon style, emotional reversal, 8k --ar 9:16 | --- | Heartbeat SFX | Swell |
| 18 | WS | ELARA turns away from him. Walks toward the terrace doors. Leaving him standing there. Kellen doesn't move — but his eyes follow. | WS, elegant woman in white gown walking away toward terrace doors, tall man in black coat standing frozen watching her, grand ballroom, golden lighting, painterly webtoon style, power reversal complete, 8k --ar 9:16 | (Caption: Let the games begin.) | Door opening | Music crescendo |

---

### END CARD: "To be continued... Episode 8"
```

### Format Rules (Comic Drama / 漫剧)

| Column | Required | Description |
|--------|----------|-------------|
| **Panel** | Yes | Sequential number within episode |
| **Shot** | Yes | Shot size code (see Section 8) |
| **Visual Description** | Yes | Detailed visual description for human artists OR AI reference |
| **AI Prompt** | Yes | Complete, production-ready prompt for image generation |
| **Dialogue/Caption** | Yes | Spoken lines OR narrative captions |
| **SFX** | Recommended | Sound effects |
| **BGM** | Recommended | Background music cue |

### AI Prompt Structure (Mandatory)

Every AI Prompt must follow this exact structure:

```
[SHOT SIZE], [SUBJECT], [AGE/GENDER], [CLOTHING], [ACTION], [FACIAL EXPRESSION], [ENVIRONMENT], [LIGHTING], [COLOR PALETTE], [ART STYLE], [MOOD/EMOTION], [QUALITY], --ar 9:16
```

**Example (full)**:
```
MCU, 19yo woman, long silver hair, teal eyes, torn dark dress, 
clenched jaw in rain, defiant expression, mansion porch in 
background, cold blue lighting with warm amber contrast, 
painterly webtoon style, heartbreak and determination, 
8k --ar 9:16
```

---

## 4. AI Anime Short Drama Format

Use this format for cel-shaded/anime-style content.

### Scene Block Format

```
# "NEON SHADOWS"
## EPISODE 7

SERIES DEFAULT:
- Protagonist: KIRARA (17, steel-gray eyes, rain-dark hair, red scarf)
- Grade: cool_blue_v2 (neon reflections)
- Locations: INT ALLEY NIGHT (primary), INT CAFE NIGHT, EXT ROOFTOP NIGHT
- Forbidden: No hairstyle changes. No day-for-night.

---

SCENE 1 — HOOK

SCENE HEADING: INT ALLEY - NIGHT

CHARACTER: KIRARA, guarded, rain on shoulders

ACTION: She lifts the torn letter from the puddle.

CAMERA: MCU, static, cool blue grade with magenta neon reflections

DIALOGUE: (none — physical beat only)

AI PROMPT: medium close-up, static camera, 17yo anime girl with steel 
gray eyes and rain-dark hair with red scarf, she lifts a torn letter 
from a neon alley puddle, INT alley night, cool blue grade with 
magenta neon reflections, cel-shaded anime style, 4k --ar 9:16

---

SCENE 2 — TURN

SCENE HEADING: INT ALLEY - NIGHT (CONTINUOUS)

CHARACTER: KIRARA, realizing, reading the letter

ACTION: Her hand tightens. The ink is his. She looks up — searching.

CAMERA: CU on eyes, slow push in, blue grade intensifies

DIALOGUE: (subtitled flashback) "The witness lied. Trust no one. —R"

AI PROMPT: extreme close-up anime girl eyes with steel gray irises, 
slow camera push in, eyes widening in realization, rain droplets on 
eyelashes, cool blue grade intensifying, cel-shaded anime style, 
4k --ar 9:16

---

SCENE 3 — LAND

SCENE HEADING: INT ALLEY - NIGHT

CHARACTER: KIRARA, resolved, pocketing the letter

ACTION: She stands. Doesn't look back. Walks into the neon.

CAMERA: WS from behind, tracking, neon colors bloom

DIALOGUE: KIRARA: (quiet, eight words max) "You picked the wrong girl."

AI PROMPT: wide shot from behind, tracking camera, 17yo anime girl 
with rain-dark hair and red scarf walking into neon-lit alley, 
neon signs reflecting on wet ground, confident stride, INT alley 
night, neon colors blooming, cel-shaded anime style, 4k --ar 9:16

---

### END CARD
```

### Anime Format Rules

| Field | Required | Notes |
|-------|----------|-------|
| **Scene Heading** | Yes | INT/EXT + LOCATION + TIME |
| **Purpose Tag** | Yes | HOOK / TURN / LAND per scene |
| **Character** | Yes | NAME + emotional state |
| **Action** | Yes | One physical verb per beat |
| **Camera** | Yes | Shot size + movement + color grade |
| **Dialogue** | If needed | Max 8 words per clip for lip-sync simplicity |
| **AI Prompt** | Yes | Complete generation prompt |

---

## 5. Universal Standards (All Formats)

### Character Introduction (First Appearance)

```
ELARA (19, silver hair, teal eyes, torn dress, mud on cheek)
```

Required elements:
- **NAME** (ALL CAPS)
- **Age** (number)
- **2-3 visual descriptors** (hair, clothing, distinguishing feature)

### Parenthetical Delivery Notes

Use sparingly — only when meaning changes:

| Note | Meaning | When to Use |
|------|---------|-------------|
| `(beat)` | Pause for processing | Emotional moment |
| `(cold)` | Intentionally emotionless | Hiding true feelings |
| `(desperate)` | Losing control | Crisis point |
| `(mocking)` | Sarcastic, superior | Power reversal |
| `(V.O.)` | Voiceover | Internal thought or narration |
| `(O.S.)` | Off-screen | Character not in frame |

### Transitions

| Transition | Usage |
|-----------|-------|
| `FADE IN:` | Episode start only |
| `FADE OUT.` | Episode end only |
| `CUT TO:` | Standard scene change (use sparingly, mostly implied) |
| `SMASH CUT TO:` | Dramatic/jarring shift |
| `MATCH CUT TO:` | Visual parallel between scenes |
| `DISSOLVE TO:` | Time passage, memory, dream |
| `TITLE CARD:` | Text overlay for time jumps, location labels |

---

## 6. AI Image Prompt Standards

### The Universal Prompt Formula

```
[SHOT SIZE], [SUBJECT DESCRIPTION], [CLOTHING], [ACTION/POSE], 
[FACIAL EXPRESSION], [ENVIRONMENT/LOCATION], [LIGHTING], 
[COLOR PALETTE], [ART STYLE], [MOOD/EMOTION], [QUALITY TAG], 
--ar 9:16
```

### Prompt Quality Checklist

- [ ] **Shot size specified** (WS, MCU, CU, etc.)
- [ ] **Subject fully described** (age, gender, hair, eyes, build)
- [ ] **Clothing detailed** (style, color, condition)
- [ ] **Action/pose clear** (what the body is doing)
- [ ] **Facial expression specified** (emotional state visible)
- [ ] **Environment described** (location, time, weather)
- [ ] **Lighting defined** (direction, color temperature, mood)
- [ ] **Art style locked** (painterly, cel-shaded, photorealistic, etc.)
- [ ] **Aspect ratio set** (--ar 9:16 for vertical/mobile)
- [ ] **Quality tag included** (8k, 4k, highly detailed)

### Subject Description Template

```
[AGE]yo [GENDER], [HAIR COLOR] [HAIR STYLE] hair, 
[EYE COLOR] eyes, [BUILD], [SKIN TONE], 
[DISTINGUISHING FEATURE]
```

Examples:
```
28yo woman, auburn wavy hair, green eyes, athletic build, 
freckles across nose

35yo man, dark slicked-back hair, gray eyes, tall broad-shouldered, 
small scar on jaw

19yo woman, long silver hair, teal eyes, slender, pointed ears, 
wolf mark on neck
```

### Art Style Lock (Consistency)

Every prompt in a series must include the SAME style tag:

| Style | Prompt Tag | Best For |
|-------|-----------|----------|
| Korean Webtoon | `painterly webtoon style, soft shading, dramatic lighting` | Romance, drama |
| Japanese Anime | `cel-shaded anime style, bold lines, vibrant colors` | Action, fantasy |
| Western Comic | `bold comic book style, high contrast, graphic lines` | Superhero, noir |
| Semi-Realistic | `semi-realistic illustration, detailed shading, cinematic` | Mature themes |
| Chibi/Cute | `chibi anime style, large heads, cute proportions, bright` | Comedy, light |
| Dark Fantasy | `dark fantasy illustration, moody lighting, gothic details` | Supernatural |

**Never change style tags mid-series. Character lock is maintained by style consistency.**

### Negative Prompts (When Needed)

```
--no blurry, deformed, bad anatomy, extra limbs, watermark, 
signature, text, low quality, worst quality
```

### Lighting Vocabulary

| Lighting Term | Effect | When to Use |
|--------------|--------|-------------|
| `dramatic chiaroscuro` | Strong light/dark contrast | Emotional intensity |
| `soft golden hour` | Warm, flattering | Romantic moments |
| `cold blue moonlight` | Cool, lonely | Sadness, isolation |
| `neon-lit` | Colorful artificial | Urban night scenes |
| `rim lighting` | Subject outlined in light | Heroic reveals |
| `under-lit` | Light from below | Horror, unease |
| `bloom/glow` | Soft light radiating | Magical, dreamlike |
| `high-key` | Bright, minimal shadows | Comedy, optimism |
| `low-key` | Dark, deep shadows | Drama, mystery |

---

## 7. Character Consistency Bible

### Character Master Sheet

Every character must have a locked master sheet used in ALL prompts:

```
=== ELARA (Protagonist) ===
BASE PROMPT: 19yo woman, long silver hair, teal eyes, slender 
build, pointed ears, wolf mark on neck

VARIANTS:
- Tattered: torn dark dress, mud on face and clothes, barefoot
- Transformed: flowing white gown with moon embroidery, crystal 
  hair pins, confident stance
- Battle: leather armor, silver claw gauntlets, blood on cheek
- Casual: cream sweater, dark jeans, hair in ponytail

NEVER CHANGE: Silver hair color, teal eye color, pointed ears, 
wolf mark location (left side of neck)

REFERENCE SEED: [Seed number for image gen consistency]
STYLE REFERENCE IMAGE: [URL or file path to style-locked reference]
```

### Consistency Rules

1. **Physical traits NEVER change** across episodes (hair color, eye color, height, distinguishing marks)
2. **Clothing changes ONLY at designated story beats** (glow-up, battle, formal event)
3. **Art style tag remains IDENTICAL** in every prompt
4. **Lighting color temperature** can vary by mood, but face rendering must be consistent
5. **Age does not change** unless explicitly part of the plot (time jump with explanation)

### Seed/Style Reference Method

For AI image generators that support it:

1. Generate a **master character reference image** first
2. Lock the **seed number** from that generation
3. Use the **same seed + character description** for all future panels
4. For Midjourney: use `--cref [URL]` (character reference)
5. For Stable Diffusion: use the same seed + consistent prompt structure

---

## 8. Shot Size Vocabulary

### Standard Film Shots (Use These Exact Terms)

| Abbreviation | Full Name | Frame Description | When to Use |
|-------------|-----------|-------------------|-------------|
| **EWS** | Extreme Wide Shot | Subject tiny, environment dominant | Establishing location |
| **WS** | Wide Shot | Subject full body, some environment | Action, movement, entrance |
| **MS** | Medium Shot | Subject waist up | Dialogue, standard interaction |
| **MCU** | Medium Close-Up | Subject chest up | Emotional dialogue, reaction |
| **CU** | Close-Up | Subject face fills frame | Intense emotion, revelation |
| **ECU** | Extreme Close-Up | Eyes, mouth, or detail only | Maximum intensity, secret reveal |
| **OTS** | Over-The-Shoulder | Looking past one subject to another | Two-person dialogue |
| **POV** | Point of View | What the character sees | Discovery, reaction setup |
| **TS** | Two-Shot | Two subjects in frame | Relationship dynamics |
| **INSERT** | Detail Shot | Object or detail only | Clue, prop, important item |
| **AERIAL** | Bird's Eye | Directly overhead | Power, scale, isolation |
| **LOW** | Low Angle | Camera below subject | Power, intimidation, heroism |
| **HIGH** | High Angle | Camera above subject | Vulnerability, defeat, surveillance |

### Shot Selection by Emotional Beat

| Beat Type | Recommended Shot | Why |
|-----------|-----------------|-----|
| Shock/reveal | CU or ECU | Maximum facial impact |
| Power moment | LOW angle WS | Subject dominates frame |
| Vulnerability | HIGH angle MCU | Subject looks small, exposed |
| Action sequence | WS or EWS | Space for movement |
| Romantic tension | MCU or OTS | Intimate but not invasive |
| Isolation | AERIAL or EWS | Subject alone in space |
| Secret/object | INSERT or ECU | Detail is the story |
| Entrance | WS or LOW | Subject arrives with impact |

---

## 9. Camera Movement & Effect Notation

### Movement Types

| Notation | Movement | Effect |
|----------|----------|--------|
| `static` | No movement | Stability, tension, intimacy |
| `push in` | Camera moves closer | Intensity increase, revelation |
| `pull out` | Camera moves away | Scale, isolation, context |
| `track left/right` | Camera follows subject | Movement, pursuit |
| `pan left/right` | Camera rotates horizontal | Discovery, scanning |
| `tilt up/down` | Camera rotates vertical | Reveal, scale |
| `dolly in` | Smooth approach | Emotional deepening |
| `handheld` | Slight shake | Urgency, documentary feel |
| `drift` | Slow float | Dreamlike, memory |

### Effect Notation (漫剧/Comic Specific)

| Effect | Notation | When to Use |
|--------|----------|-------------|
| **Speed lines** | `[EFFECT: speed lines]` | Action, impact, fast movement |
| **Impact frame** | `[EFFECT: impact flash]` | Punch, shock, sudden event |
| **Screen shake** | `[EFFECT: screen shake]` | Explosion, earthquake, power |
| **Black screen** | `[EFFECT: black panel]` | Dramatic pause, transition |
| **White flash** | `[EFFECT: white flash]` | Memory, time jump, power up |
| **Split screen** | `[EFFECT: split 2-way]` | Parallel action, comparison |
| **Panel border break** | `[EFFECT: border break]` | Character "escapes" the panel |
| **Motion blur** | `[EFFECT: motion blur]` | Fast movement, transition |
| **Focus pull** | `[EFFECT: focus shift]` | Attention shift, reveal |
| **Particle effect** | `[EFFECT: particles/sparkles]` | Magic, romance, atmosphere |

### Transition Effects Between Panels

| Transition | Notation | Effect |
|------------|----------|--------|
| Hard cut | `CUT` | Standard, time continuous |
| Fade | `FADE` | Time passage, dream |
| Dissolve | `DISSOLVE` | Memory, soft transition |
| Wipe | `WIPE [direction]` | Location change |
| Iris | `IRIS IN/OUT` | Focus point, romantic |
| Smash cut | `SMASH CUT` | Jarring shift, comedy |
| Match cut | `MATCH CUT` | Visual parallel |

---

## 10. Common Format Mistakes

### Critical Errors (Will Break Production)

| Mistake | Why It Breaks | Correct Approach |
|---------|--------------|-----------------|
| **Inconsistent character description** | AI generates different-looking character | Use Character Bible, lock all physical traits |
| **Missing shot size** | AI generates wrong framing | Always specify WS/MCU/CU/etc. |
| **Vague art style** | Every panel looks different | Lock ONE style tag for entire series |
| **No aspect ratio** | Wrong image dimensions | Always include `--ar 9:16` |
| **Dialogue too long** | Panel too text-heavy, unreadable on mobile | Max 2 lines per panel |
| **Missing facial expression** | Character looks blank/wrong emotion | Always specify expression in prompt |
| **Wrong lighting direction** | Flat, unprofessional images | Specify lighting type and direction |
| **Inconsistent environment** | Location changes without reason | Lock location descriptions |

### Format Inconsistency Checklist

Before finalizing any episode, verify:

- [ ] All characters use the same physical description as Character Bible
- [ ] All prompts include `--ar 9:16`
- [ ] All prompts include the series-locked art style tag
- [ ] Shot sizes vary (not all MCU, not all WS)
- [ ] Each panel has ONE clear action
- [ ] Dialogue max 2 lines per panel
- [ ] Captions (narration) are distinct from dialogue
- [ ] SFX and BGM columns are filled for key moments
- [ ] Panel count matches target duration (18-22 panels for 75-90s)
- [ ] Purpose tags (HOOK/TURN/LAND) are assigned for anime format

### Episode Duration Formula

```
EPISODE DURATION ≈ PANEL COUNT × 4 seconds

Target:
- 60 seconds = 15 panels
- 75 seconds = 18-20 panels
- 90 seconds = 22-24 panels
```

Adjust panel count by reducing motion panels or adding static panels as needed.

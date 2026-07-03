# Netflix-Level Cinematic Production Standard

## What This Means

Netflix dramas (Bridgerton, The Crown, You, The Witcher, Sex/Life) set the visual
standard that American female audiences expect. AI realistic human drama must
deliver comparable production values through Action Lines that direct AI generation
toward cinematic quality.

**This is NOT about changing the script format.** The format stays the same.
This is about what goes INTO the Action Lines — the visual direction that
determines whether the output looks like a $200M Netflix original or a cheap phone video.

## The Netflix Visual DNA

### 1. Color Grading (色调)

Netflix dramas use deliberate, emotionally-coded color palettes. Every scene has
a color temperature that communicates mood before a word is spoken.

| Mood | Temperature | Key Colors | Hex Reference |
|------|------------|-----------|---------------|
| **Cold power / Isolation** | Cool blue-teal | Steel blue, slate, ice | #2C3E50, #5D8AA8 |
| **Warm romance / Intimacy** | Golden amber | Honey, candlelight, blush | #D4A574, #F4A460 |
| **Danger / Tension** | Desaturated red | Deep crimson, burgundy, ash | #8B0000, #6B3A2A |
| **Mystery / Supernatural** | Purple-magenta | Violet, indigo, midnight | #6B4C7F, #191970 |
| **Hope / New beginning** | Soft morning light | Peach, cream, pale gold | #FFDAB9, #FFF8DC |
| **Wealth / Opulence** | Rich contrast | Deep emerald, gold, ivory | #006A4E, #C9B037 |

**In Action Lines**: Always specify the color temperature. This determines the AI's color grade.

```
GOOD: "The ballroom glows with honey-amber candlelight, warm gold 
reflecting off crystal."

BAD: "The ballroom is well-lit."
```

### 2. Lighting Design (灯光)

Netflix lighting is NEVER flat. Every scene has motivated, directional light
that sculpts the actor's face and creates depth.

| Lighting Style | Description | When to Use |
|---------------|-------------|-------------|
| **Rembrandt** | Single dominant light source at 45°, creating a triangle of light on the shadow-side cheek | Power scenes, emotional intensity |
| **Chiaroscuro** | Extreme light-dark contrast, deep shadows | Betrayal, secrets, noir moments |
| **Rim / Backlight** | Light from behind subject, creating a halo | Heroic reveals, dreamlike romance |
| **Practical-motivated** | Light appears to come from visible sources (lamps, candles, windows) | Realism, grounded scenes |
| **Neon accent** | Saturated color light mixed with neutral base | Modern urban, nightlife, tension |
| **Golden hour** | Warm, low-angle, soft shadows | Hope, romance, new beginnings |
| **Overcast soft** | Even, diffused light with no hard shadows | Sadness, vulnerability, truth-telling |

**In Action Lines**: Specify light source direction and quality:

```
GOOD: "Cold window light slices across her face, leaving half in 
shadow — the side with the bruise."

BAD: "She stands by the window." (light direction unknown)
```

### 3. Camera Work (镜头语言)

Netflix camera work is invisible but intentional. Every shot size and movement
is emotionally motivated.

#### Shot Size Rules

| Shot | Netflix Standard | When to Use |
|------|-----------------|-------------|
| **CU (Close-Up)** | Face fills frame, shallow depth of field (background creamy blur) | Emotional reveals, reactions, intimacy |
| **MCU (Medium Close-Up)** | Chest to head, most common dialogue shot | Standard dialogue, confrontation |
| **MS (Medium Shot)** | Waist up, character + immediate environment | Context + character |
| **WS (Wide Shot)** | Full body + environment, used sparingly | Entrances, power dynamics, isolation |
| **ECU (Extreme Close-Up)** | Eyes, lips, or object only | Maximum intensity, secrets, discovery |

**Netflix rule**: 70% of scenes are CU/MCU. WS is used deliberately — when the
environment matters as much as the character.

#### Camera Movement

| Movement | Effect | Action Line Example |
|----------|--------|-------------------|
| **Static hold** | Tension, forced attention | "The camera doesn't move. It watches." |
| **Slow push-in** | Intensity deepening | "Camera slowly pushes closer to her face as she reads." |
| **Slow pull-out** | Reveal, scale, loneliness | "Camera pulls back — she's alone in the empty ballroom." |
| **Subtle drift** | Unease, dreamlike | "Camera drifts left, as if we're circling the truth." |
| **Handheld shake** | Urgency, documentary realism | "Handheld camera — raw, immediate." |
| **Locked-off with subject movement** | Character controls the frame | "She crosses the room. The camera stays. She comes to us." |

**Netflix rule**: Camera moves slowly or not at all. Fast movement is reserved for
action sequences. Drama lives in the stillness.

#### Depth of Field (景深)

Netflix productions use shallow depth of field (background blur) to isolate
characters and create a three-dimensional, cinematic look.

```
GOOD: "Shallow depth of field — Sarah sharp in focus, the boardroom 
surrendered to creamy bokeh behind her."

BAD: "Sarah is in the boardroom." (no depth information)
```

### 4. Frame Composition (构图)

| Technique | Description | When to Use |
|-----------|-------------|-------------|
| **Center frame** | Subject dead center | Power, confrontation, direct address |
| **Rule of thirds** | Subject off-center | Naturalism, dialogue, observation |
| **Negative space** | Vast empty space around subject | Isolation, insignificance, loneliness |
| **Frame within frame** | Doorways, windows, mirrors contain the subject | Entrapment, surveillance, layers of truth |
| **Low angle** | Camera below subject | Power, intimidation, heroic moment |
| **High angle** | Camera above subject | Vulnerability, defeat, surveillance |
| **Symmetry** | Perfectly balanced frame | Order, control, artificial perfection (before chaos) |
| **Asymmetry** | Unbalanced frame | Tension, instability, unease |

```
GOOD: "Center frame. Sarah fills the middle third. The boardroom 
stretches empty on either side — a queen in a castle of her own making."

BAD: "Sarah stands in the boardroom."
```

### 5. Production Design (美术)

Netflix-level production design means every prop, every costume detail, every
set element tells a story.

#### Costume as Character

Every outfit must communicate status, personality, and emotional state:

```
GOOD: "She wears a charcoal Alexander McQueen blazer — the one 
with the structured shoulders that make her look like she could 
headbutt a skyscraper. No jewelry. She doesn't need decoration."

BAD: "She wears a business suit."
```

#### Environment as Emotion

```
GOOD: "The penthouse is all glass and steel — floor-to-ceiling 
windows framing the Manhattan skyline like a threat. One orchid 
on the table. Perfect. Dead."

BAD: "She is in a luxury apartment."
```

#### Props as Plot

```
GOOD: "She holds the envelope by its corner — two fingers, like 
it might bite. The seal is broken. It already has."

BAD: "She is holding a letter."
```

### 6. Pacing and Rhythm (剪辑节奏)

Netflix editing rhythm follows emotional beats, not just plot:

| Beat Type | Shot Duration | Transition | Example |
|-----------|--------------|------------|---------|
| **Shock / Reveal** | 2-3 seconds | Hard cut | Slap, discovery, entrance |
| **Tension building** | 5-8 seconds, static | Hold | Staring contest, decision moment |
| **Dialogue beat** | 3-5 seconds per line | Cut on reaction | Standard conversation |
| **Emotional peak** | 8-12 seconds, slow push | Dissolve | Kiss, confession, breakdown |
| **Breath / Transition** | 2-3 seconds | Fade / dissolve | Scene change, time passage |
| **Action** | 1-2 seconds | Rapid hard cuts | Chase, fight, destruction |

**Netflix rule**: The best drama lets moments BREATHE. A held close-up for
5 seconds can be more powerful than 5 rapid cuts.

### 7. The "Movie Moment" (Netflix Signature)

Every episode should have ONE "movie moment" — a shot so visually striking
that it could be a poster. This is what separates Netflix from television.

Examples:
- A woman in a red dress alone in a black-and-white room
- Two enemies inches apart, their reflections merging in a mirror
- A silhouette against a wall of windows at sunset
- Rain pouring over a face that's trying not to cry
- A crown placed on a head, shot from below with rim light

```
In Action Lines:

"THE MOVIE MOMENT: Sarah stands at the floor-to-ceiling window.
Manhattan sprawls below like a circuit board. She's backlit — 
a silhouette in a white dress that glows at the edges. She doesn't
turn. She doesn't need to. The city is already hers."
```

## Integrating Netflix Standard into Action Lines

### Before (Basic)

```
Sarah walks into the boardroom. Mark is at the head of the table.
She sits down. He gives her a promotion letter. She takes it.
```

### After (Netflix Cinematic Standard + 中英文混合格式)

```
3.1 企业董事会会议室 日 内
人物：Sarah、Mark

△冷钢蓝色调。落地玻璃窗将冬日光线倾泻进房间，蓝白色，不留情面。
△Sarah（32，炭灰色麦昆西装外套，没有任何首饰）从远端门进入。镜头停在她的脸上：半张脸被窗户照亮，半张隐没在阴影中。她没有眨眼。

△正中央构图。她沿着桌子走了全程。十把空皮椅。Mark（55，银发，一脸满足）坐在首位，一个能容纳二十人的房间里唯一的另一个人。
Mark：VP of Operations. You earned it.

△他把信推过桃花心木桌面。她接过，没有打开。浅景深：她的脸锐利清晰，Mark消融在柔焦模糊中。
▲一个微表情：她的下颌收紧了一毫米。
Sarah：Thank you, Mark. I won't let you down.

▲电影级画面：镜头缓缓推向她的眼睛，钢灰色，倒映着曼哈顿天际线。冰冷。算计。准备好了。
```

## The Cumulative Effect

When every Action Line carries Netflix-level visual direction:

| Element | Viewer Experience |
|---------|------------------|
| Color grading | "I feel the mood before anyone speaks" |
| Lighting | "Her face is beautiful AND dramatic" |
| Depth of field | "This looks like a real movie" |
| Frame composition | "Every frame could be a painting" |
| Production design | "I believe this world is real" |
| Pacing | "I can't look away — every second matters" |

**The result**: Viewer forgets this is AI-generated. They simply watch a story
that looks and feels as good as anything on Netflix.

## Quick Reference: Netflix Keywords for AI Prompts

Always include at least 3 of these in AI image generation prompts:

```
Core: cinematic, shallow depth of field, professional color grading
Lighting: Rembrandt lighting, golden hour, practical-motivated, rim light
Mood: atmospheric, moody, dramatic, intimate, tense
Quality: photorealistic, 8k, anamorphic lens, film grain, Netflix original quality
Composition: rule of thirds, center frame, negative space, frame within frame
```

Example complete prompt:
```
cinematic MCU, shallow depth of field, professional color grading,
cool steel-blue color temperature, Rembrandt lighting, a 32-year-old
woman in charcoal blazer, jaw set with determination, half her face
in shadow, modern corporate boardroom floor-to-ceiling windows behind,
Manhattan skyline visible through glass, photorealistic, 8k,
Netflix original quality, atmospheric, tense --ar 9:16
```

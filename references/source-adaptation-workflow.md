# Source Material Adaptation Workflow

Complete workflow for transforming ANY source material — Chinese or English novel chapters,
Chinese or English scripts, complete or partial — into a full American-market short drama script.

## The 4 Source Types x 3 Operation Modes Matrix

### Source Types

| Type | Code | Description |
|------|------|-------------|
| CN-Novel | Chinese novel chapter(s) | Web novel, romance, urban fiction, xianxia, etc. |
| EN-Novel | English novel chapter(s) | Romance, thriller, YA, fanfiction, etc. |
| CN-Script | Chinese short drama script | Existing domestic short drama, partial or full |
| EN-Script | English short drama script | Existing script needing rewrite or expansion |

### Operation Modes

| Mode | What Happens | When to Use |
|------|-------------|-------------|
| **Rewrite** | Keep core plot/characters, change cultural packaging, dialogue, setting for US audience | Source is culturally foreign (Chinese) or stylistically outdated |
| **Write-in-style** | Learn the structure, pacing, and technique from source; create NEW story with same emotional mechanics | Source demonstrates effective technique but content cannot be directly used |
| **Expand** | Take brief/outline/partial material and build full 60-80 episode series with complete arcs | Source is incomplete (outline, few chapters, partial script) |

### How to Auto-Select Operation Mode

```
IS the source culturally Chinese or heavily Chinese-context-dependent?
├── YES → Rewrite (文化改写)
│
NO → IS the source complete (has beginning, middle, end)?
    ├── YES → IS it already American-market-ready?
    │   ├── YES → Write-in-style (仿写 — learn technique, new story)
    │   └── NO → Rewrite (风格改写 for US market)
    │
    └── NO (incomplete) → Expand (扩写)
        ├── Has characters + some plot → Expand with full arcs
        ├── Has outline only → Expand from scratch
        └── Has only concept/genre → Expand with genre template
```

## Input Analysis Protocol

When user provides source material, execute this analysis automatically:

### Step 1: Source Classification

Analyze the input and classify:

```
SOURCE CLASSIFICATION:
- Language: [Chinese / English]
- Format: [Novel prose / Script / Outline / Mixed]
- Completeness: [Complete story / Partial chapters / Outline only / Fragments]
- Genre: [Romance / Urban / Fantasy / Revenge / Workplace / Mixed]
- Cultural origin: [Chinese-context / Western-context / Mixed / Universal]
- Word count (approx): [___]
```

### Step 2: Content Extraction

Extract from the source:

```
CORE ELEMENTS:
- Protagonist: [Name, age, defining trait, wound, want]
- Antagonist: [Name, relationship to protagonist, power, motivation]
- Love Interest (if any): [Name, relationship dynamic, secret/wound]
- Inciting Incident: [What disrupts the protagonist's world?]
- Central Conflict: [What drives the entire story?]
- Emotional Core: [What feeling should the audience have at the end?]
- Karma Moment: [How does the antagonist get their comeuppance?]
- Setting: [Location, time period, social world]
- Tone: [Dark / Comedic / Romantic / Thriller / Mixed]
```

### Step 3: Gap Analysis

Compare extracted elements against what a full 60-80 episode series needs:

| Element | Source Has? | Gap | Resolution |
|---------|------------|-----|------------|
| Clear protagonist arc | Y/N | [Describe gap] | [How to fill] |
| Strong antagonist presence | Y/N | [Describe gap] | [How to fill] |
| Romantic subplot (if genre needs it) | Y/N | [Describe gap] | [How to fill] |
| Episode 1 hook | Y/N | [Describe gap] | [How to fill] |
| Mid-season twist (Ep 30-40) | Y/N | [Describe gap] | [How to fill] |
| Finale resolution | Y/N | [Describe gap] | [How to fill] |
| Card boundary cliffhangers | Y/N | [Describe gap] | [How to fill] |
| Cultural compatibility (US market) | Y/N | [Describe gap] | [How to fill] |

### Step 4: Direction + Episode Count Determination

Based on gap analysis, auto-determine:

```
RECOMMENDED APPROACH:
- Operation Mode: [Rewrite / Write-in-style / Expand]
- Episode Count: [60-80, with justification]
- Primary Genre Template: [From genre-templates.md]
- Secondary Genre (if hybrid): [From genre-templates.md]
- Cultural Adaptation Level: [Heavy / Moderate / Light / None]

JUSTIFICATION:
[2-3 sentences explaining why this approach best serves the source material
and the US market target audience]
```

## Per-Source-Type Processing Guide

### Type A: Chinese Novel (CN-Novel) → American Short Drama

**Default mode**: Rewrite (50% rewrite rule applies)

**Processing steps**:

1. **Extract emotional spine** — What makes Chinese readers binge this? Find the "爽点" (cathartic beats)
2. **Map cultural mechanisms** — Use `references/cultural-adaptation.md` to translate every culturally-specific element
3. **Rebuild setting** — Replace all Chinese locations with American equivalents
4. **Restructure relationships** — Convert Chinese relationship dynamics to American equivalents
5. **Rewrite dialogue from scratch** — Never translate dialogue; write new dialogue that serves the same emotional function
6. **Add US-market requirements** — Consent markers, diverse casting, female friendship, mental health awareness
7. **Expand to 60-80 episodes** — Most novel chapters need significant expansion; each chapter may become 5-10 episodes

**Common CN-Novel patterns and their American versions**:

| Chinese Pattern | American Version | Notes |
|----------------|-----------------|-------|
| 霸道总裁 (Domineering CEO) | Alpha male with vulnerability + respect for her agency | Remove controlling behavior, add genuine respect |
| 先婚后爱 (Marriage first, love later) | Contract marriage / fake dating | Keep but frame with American legal/social logic |
| 重生复仇 (Rebirth revenge) | Glow-up comeback / second chance | Remove literal rebirth; use transformation instead |
| 穿越 (Time travel/isekai) | "Fish out of water" / identity swap | Keep culture clash, modernize mechanism |
| 宫斗 (Palace intrigue) | Boardroom politics / corporate warfare | Replace imperial hierarchy with corporate |
| 修仙 (Cultivation) | Career ladder / skill mastery | Remove mystical elements; keep progression fantasy |
| 打脸 (Face-slapping) | Public exposure / viral takedown | Same catharsis, different mechanism |
| 白莲花女主 (Pure/innocent heroine) | Competent woman who chooses kindness | American audiences reject pure innocence; add competence |
| 恶毒女配 (Evil female rival) | Rival with understandable motivation | Add depth; avoid cartoon villainy |

**Episode count guide for CN-Novels**:
- 1-3 chapters (brief setup) → Expand to 60-70 episodes using genre template
- 5-10 chapters (partial arc) → Expand to 70-80 episodes; fill gaps with original material
- 20+ chapters (substantial) → Rewrite and condense to 60-80 episodes; select strongest beats
- Complete novel (100+ chapters) → Heavy rewrite; extract 3-5 strongest arcs; condense to 60-80 episodes

---

### Type B: English Novel (EN-Novel) → American Short Drama

**Default mode**: Expand (most EN novels submitted are partials or need restructuring)

**Processing steps**:

1. **Analyze structure** — English novels often have slower pacing; identify where to accelerate
2. **Frontload conflict** — American short drama needs the inciting incident in Episode 1
3. **Condense subplots** — Keep only the subplot that directly supports the main arc
4. **Add card boundary cliffhangers** — Novels don't have payment points; design artificial but organic cliffhangers every 10 episodes
5. **Strengthen visual beats** — Novels rely on internal monologue; convert to visual action
6. **Americanize if needed** — Even English novels may need cultural tuning for the 25-50 female demo

**Episode count guide for EN-Novels**:
- Outline / synopsis only → Expand to 60-70 episodes using genre template
- 1-3 chapters → Expand to 60-70 episodes; build full arcs around existing material
- 5-10 chapters → Expand to 70-80 episodes; you have substantial material to work with
- Complete novel → Condense to 60-80 episodes; extract strongest emotional beats

---

### Type C: Chinese Script (CN-Script) → American Short Drama

**Default mode**: Rewrite (cultural translation required)

**Processing steps**:

1. **Preserve structure, rewrite content** — The episode-by-episode structure often works; the content needs 50% rewriting
2. **Scene-by-scene cultural audit** — Each scene: what is culturally Chinese? Replace with American equivalent
3. **Dialogue total replacement** — Never translate Chinese short drama dialogue; the rhythm and idioms don't transfer
4. **Setting replacement** — Every location, every prop, every social context
5. **Hook/cliffhanger audit** — Chinese hooks often rely on cultural shock (跪求, 打脸); replace with universal hooks
6. **Check against US red lines** — Forced contact, filial piety extremes, colorism, etc.

**Key differences between CN and US scripts**:

| Element | Chinese Script | American Script |
|---------|---------------|-----------------|
| Pacing | Faster, more reversals per minute | Slightly slower, more emotional beats |
| Dialogue style | More direct, 怼 (confrontational) | More subtext, sarcasm, wit |
| Romance | Faster confession, more physical | Slower burn, more verbal sparring |
| Antagonist | Often more cartoonishly evil | Needs understandable motivation |
| Social media | WeChat moments, livestreaming | Instagram, TikTok, viral tweets |
| Class dynamics | Very explicit (rich vs poor) | More coded, subtle |
| Resolution | Often family reconciliation | Often personal independence |

**Episode count guide for CN-Scripts**:
- Partial script (1-10 episodes) → Rewrite existing + expand to 60-80 episodes
- Partial script (11-30 episodes) → Rewrite existing + expand to 60-80 episodes
- Partial script (31-50 episodes) → Rewrite existing + add finale arcs to reach 60-80
- Complete script (60-80 episodes) → Full rewrite for cultural adaptation
- Complete script (80-100 episodes) → Condense to 60-80 strongest episodes + rewrite

---

### Type D: English Script (EN-Script) → American Short Drama

**Default mode**: Write-in-style (learn technique) or Expand (if partial)

**Processing steps**:

1. **Analyze what works** — Identify the techniques that make this script effective
2. **Analyze gaps** — What's missing for a complete 60-80 episode series?
3. **If partial**: Expand using the same voice, same character dynamics, same tone
4. **If complete but learning exercise**: Create NEW story using same structural techniques
5. **Ensure US-market fit** — Even English scripts may need demographic tuning

**Episode count guide for EN-Scripts**:
- Partial script (any length) → Write in same style, expand to 60-80 episodes
- Complete script (60-80 episodes) → Write-in-style: create new story using same techniques
- Complete script (under 60 episodes) → Expand to 60-80; add subplots and escalation

---

## The Complete Adaptation-to-Script Workflow

For ANY source material, follow this end-to-end process:

### Phase 1: Input Analysis (Automatic)

```
1. Classify source (Type A/B/C/D)
2. Determine completeness (full / partial / outline)
3. Auto-select operation mode (Rewrite / Write-in-style / Expand)
4. Determine episode count (60-80, with justification)
5. Select primary genre template
6. Extract core elements (protagonist, antagonist, conflict, karma moment)
7. Perform gap analysis
8. Report findings to user with recommendation
```

### Phase 2: Series Architecture

```
1. Write logline (one sentence)
2. Build character profiles + Character Consistency Bible
3. Create 60-80 episode master beat sheet
4. Design card boundary cliffhangers (Ep 10, 20, 30, 40, 50, 60)
5. Map emotional pacing chart
6. Plan set piece episodes (every 10 episodes)
7. Get user approval on architecture
```

### Phase 3: Cultural Adaptation (if Rewrite mode)

```
1. Translate all culturally-specific elements (see cultural-adaptation.md)
2. Americanize settings, relationships, social dynamics
3. Remove cultural red flags
4. Add US-market requirements
5. Verify Golden Triangle is present in Episode 1
```

### Phase 4: Script Writing

```
1. Select format (Live-Action / Comic Drama / Anime)
2. Write Episodes 1-5 (Setup phase)
3. User review and approval
4. Write Episodes 6-20 (First Card)
5. User review
6. Write Episodes 21-40 (Second Card)
7. User review
8. Write Episodes 41-60 (Third Card)
9. User review
10. Write Episodes 61-80 (Finale)
11. Final delivery
```

### Phase 5: Quality Validation

```
1. Run format consistency check (format reference)
2. Run hook/cliffhanger audit (viral-formula reference)
3. Run cultural sensitivity check (cultural-adaptation reference)
4. Run American sound check (screenplay-format reference)
5. Run audience fit validation (audience-insights reference)
6. Deliver final package
```

## Adaptation Quality Standards

### For Rewrite Mode:
- [ ] Source's emotional core preserved
- [ ] Every culturally-specific element replaced with American equivalent
- [ ] Dialogue sounds written by native English speaker (not translated)
- [ ] Setting fully Americanized
- [ ] Red lines removed, US expectations added
- [ ] Episode count justified by source material depth

### For Write-in-Style Mode:
- [ ] Source's structural techniques identified and documented
- [ ] New story is genuinely original (not plagiarism)
- [ ] Same emotional impact as source
- [ ] Same pacing density (hooks, cliffhangers, reversals)
- [ ] Character voices distinct from source

### For Expand Mode:
- [ ] Source material fully incorporated (nothing wasted)
- [ ] Added material matches source's tone and quality
- [ ] Character arcs complete and satisfying
- [ ] All 60-80 episodes earn their place
- [ ] No "filler" episodes — every one moves plot or deepens character
- [ ] Card boundary cliffhangers organic to the story

## Common Adaptation Scenarios

### Scenario 1: "I have a Chinese web novel chapter, make it American"
→ Type A + Rewrite mode → Full cultural translation + expansion

### Scenario 2: "I wrote 5 chapters of an English romance, make it a full series"
→ Type B + Expand mode → Keep characters/plot, build full 60-80 episode arcs

### Scenario 3: "Here's a hit Chinese short drama script, make it work for ReelShort"
→ Type C + Rewrite mode → Preserve structure, rewrite all content for US audience

### Scenario 4: "I love how this English short drama is written, write me something similar"
→ Type D + Write-in-style mode → Analyze technique, create new story

### Scenario 5: "I just have an idea: billionaire contract marriage"
→ No source + Original creation → Use genre template directly

### Scenario 6: "I have a Chinese novel outline, not the full chapters"
→ Type A + Expand mode → Use outline as spine, build all episodes from scratch

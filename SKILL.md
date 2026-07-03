---
name: ai-short-drama-writer
description: "Write and adapt AI short-drama scripts for Chinese production teams, especially AI仿真人剧 for US female audiences; uses plain-text 正文 format, narration/dialogue modes, cinematic visual notes, hooks, cliffhangers, and paid-card arcs."
version: 4.4
optimized_via: real-video reverse-engineering of netshort.com + shorttv.live (mlx-turbo ASR, netshort 44 集 + shorttv 93 集) + 数据源 #3 发行元数据反推 (85 海外本土AI仿真人剧 from /Users/mac/Documents/reso/剧单, pan.baidu 样片); pipeline skill化 in reverse-engineering-pipeline/; v4.2 视频级结构发现 (冷开场 in-media-res / 节拍密度量化 / 爽点簇射曲线 / 决策悬崖 / 中段禁零 / netshort-vs-shorttv 工艺分野) 见 references/research-evidence-video.md
---

# AI Short Drama Writer

> **v4.4 — 海外仿真人剧 4 簇交叉反推（n=1→4 剧 / 12→29 集）+ 证伪修正。** 在 v4.3 单簇（Persephone 神话降世）基础上扩样 3 簇：sorrow-sea（虐心被冤家庭伦理 7 集）/ wolf-vampire（超自然狼族×吸血鬼言情 5 集）/ mars-return（科幻火星归来×前夫悔 5 集），皆英文对白、北美市场、mlx-turbo ASR。**五处实质变化**：①**证伪并撤回** v4.3「付费墙集必为全弧 top-2」通用规则——mars-return 付费墙集恰是全弧最低谷（13.0 segs/min，靠一句"That villa is mine"身份揭底兑现，非密度峰）；改为**密度曲线 4 原型菜单**（A 后载爬坡 / B 平坦高位 / C 前载尖峰 / D 中峰+揭底谷，按题材选）；②**爽点元引擎 = 戏剧反讽/信息差**——4 簇证实关键词库对真实引擎漏判 50–100%（wolf 圣水道德绑架整场零分 / mars 身份揭晓零分），关键词降级为兑现手段 checklist，每集先填「观众知道___而___不知道」信息差结构；③**道德绑架虐心密度尖峰** 4 拍 beat（wolf ep3=26.0，紧急筹码→FL代价揭露→ML最小化→绝杀反问+苦涩回响）；④**跨时空戏剧反讽刺开场**（mars ep1 双线同屏：ML偷腥 vs 火星直播）；⑤**主角声口 4 变体**（冷峻尊严/受伤诘问/牺牲决绝/冷峻权威，全弧锁定不漂移）。v4.3 的密度校准/视觉承重豁免/神话spine/觉醒变身/儿童信使/信物三型经 4 簇验证**保留**。证据见 `reverse-engineering-pipeline/_local7..9_..` + `_local12/`。**诚实边界**：4 剧 29 集（仍小样本），4 原型与元引擎是"高质量海外格式的工艺指纹"非统计硬默认；扩样后曲线数字会收敛。

> **v4.3 — 海外本土仿真人剧首条视频级反推（补 v4.1 盲区）。** v4.1 只拿到 85 部海外仿真人剧的**发行元数据**（付费墙/集数/题材），无视频结构；v4.3 首次对一部海外本土 AI 仿真人剧做**全弧视频级反推**（古言网络英文生产，12 集免费 / 992s 音频（均 82.6s/集）/ mlx-turbo ASR 逐句 + 关键帧视觉，FL=Persephone 复仇女神 Nemesis 继承人 / ML=Julian Hart，神话堕神降世×背叛复仇）。**核心修正**：v4.2 的 18.5 segs·min⁻¹ / 169 wpm 基线**全部来自中文 netshort/shorttv**——直接套到海外英文仿真人剧会**误判高质量集为"密度不足"**并逼出填充对白。新增 `references/overseas-cinematic-craft.md`，七处工艺发现：①**格式校准**——海外英文格式实测 11.7 segs/min·97 wpm，逐集地板下调 ≥7/≥80（非 ≥8/≥15）；②**视觉承重集豁免**——低对白高视觉集（ep4=4.9/min 换药背叛靠演不靠说）过三问后豁免，不塞填充台词；③**密度双峰加速**——蓄(5–12)→放(16–21)，付费墙集必为全弧 top-2；④**神话堕神降世 spine**——双时间线序章冷开场/封印记忆/神具机制/12 集节拍表（netshort-arc §9 只一句"玄幻混合模型"）；⑤**第 8 类爽点「觉醒变身」**——主角态变时刻，区别于身份揭晓（信息揭 vs 状态复）；⑥**冷峻尊严台词群**——补主角声口规范（反派有羞辱词库、主角此前无 → 人物塑造弱的主因）；⑦**儿童信使无意识揭露装置** + 信物三型。证据见 `reverse-engineering-pipeline/_local12/`。**诚实边界**：本版基于 1 剧 12 集（样本量小），七处发现是"高质量海外格式的工艺指纹"非统计硬默认；扩样到同簇多剧后数字会收敛。

> **v4.2 — 视频级反推：netshort + shorttv 真实 ASR 全语料结构发现。** 把 netshort 44 集 + shorttv 87 集（共 131 集，mlx-turbo ASR 热池 7-27×，零错误）跑成可量化语料，得出**视频证据级硬默认**（非发行元数据、非记忆）：①**冷开场 in-media-res**——首句对白/旁白落 **0–1s**（均值 0.26s），必须是进行时冲突；ep1 ≤10s 点核心前提，25s 内建观众>主角的上帝反差信息差；②**节拍密度量化**——单集均值 1.9min / **18.5 段·min⁻¹** / **169 词·min⁻¹**（netshort ~14/100 长集 vs shorttv ~21/200 短集），hook 集节拍间隔 **≤30s**（<90 wpm 判密度不足）；③**爽点"簇射"曲线**——禁止均匀摊铺，免费弧 = ep1–3 高位 hook(≥3/集) → 中段复利升温(≥2/集 且不得为 0) → **最后 1–2 集付费墙簇射(≥5，多类型同场对撞)**；成功弧实证单调递增到付费墙峰值；④**付费墙悬崖双 flavor**——v3.0「生死危难」补全为：关系/背叛流派更常是**决策/宣告悬崖**（离婚/签约/揭身份/复仇启动，payoff 落墙后）；⑤**中段禁零**——任意连续 2 集爽点之和 <3 即判失败模式（实证：零爽点中段=观众流失点）；⑥**平台工艺分野**——netshort=对白对峙/当场兑现/≤30s beat/对白≥85%；shorttv=第一人称旁白内省（允许 30–40%）但**不得替代爽点兑现**。证据见 `references/research-evidence-video.md`。**诚实边界**：爽点类型排序基于关键词正则（本版虐心 46% 居首 vs v4.0 隐藏实力 43%），对 regex 敏感、两版均不足为据，真实类型混合须人工通读判定；但 §1–§6 结构性发现与正则无关、稳健。证据基线 **131 集/26 剧**（netshort 44 + shorttv 87，全量 ASR 零错误）。

> **v4.1 — 数据源 #3：海外本土 AI仿真人剧 剧单（85 部发行元数据反推）。** 新增 `/Users/mac/Documents/reso/剧单` 第三条数据线（制作方自报发行元数据，与 netshort/shorttv 的视频 ASR 反推互补）。85 部（海外首发 2026-05-27..06-13，74 女频/11 男频）给出三处**市场事实级硬默认**：①**付费墙聚类在卡点 10**（众数 44%、均值 10.4、卡点 9–12 占 75%）——长弧仿真人剧默认前 10 集免费、第 11 集起付费；②**长弧均值 71 集**（30–120，5–10× 于 netshort/shorttv 短弧）→ 梯次揭晓要扩成**多轮**（每 ~10 集一小揭晓峰 + 虐心谷，墙前放大）；③**霸总/护妻 61% + 虐心/背叛 57%** 是女频双基底，默认必含其一。证据见 `references/research-evidence-baidu.md` + `reverse-engineering-pipeline/baidu_judan.yaml`。视频 ASR 待 browser-harness 侧下载百度网盘样片后补（用户浏览器百度网盘已登录）。

> **v4.0 — mlx-turbo 重转写 + 流水线 skill化 + 机制纠错。** v3.0 用 faster-whisper small.en（244M）转写；v4.0 升级到 **mlx large-v3-turbo（809M）热池**（6.9-27× 实时 + 循环幻觉截断），密度数字整体刷新且更可信（见 `references/research-evidence-v4.md`）。三处实质变化：①**机制纠错**——v3.0 §1 工具链两处事实错误被真实抓取证伪（netshort 是 Aliyun WAF 非 og:video；shorttv 是明文 .ts 非 AES-CBC 加密）；②**流水线 skill化**——把"获取→ASR→分析→反推"固化成 `reverse-engineering-pipeline/`（README + 5 脚本 + dramas.yaml），加剧/换平台不再重新探索机制；③**爽点引擎量化重排**——跨 44 集实证：**隐藏实力被低估（43%）远超打脸**，应作为扮猪吃虎/隐藏身份型的贯穿主驱动。诚实边界：39 剧清单当前覆盖 13/39（33%），余 26 剧待 IP 冷却后用流水线续抓（可复用可续跑）。
>
> **v3.0 — netshort 全弧付费转化结构 + 工艺三件套。** v2.0 用 16 剧 ep1 横截面解决了"单集爽点密度按流派分层"；v3.0 首次拿到 **netshort 完整免费弧**（bankrupt ep1-8 / married-a-ceo ep1-12 / wolfless ep1-9，browser-harness 突破 Aliyun WAF 逐集抓 mp4 → ASR），闭合 v2.0 最大的盲区——"netshort 付费墙到底卡在哪"。新增 `references/netshort-arc-mechanics.md`，核心修正：①集时长 60-90s→**90-210s**；②**netshort 付费墙 = 主角最大生死危难**（≠ shorttv 的真相曝光），真相与清算全押墙后——三剧三流派全部坐实（bankrupt 扣药/铁链、maco 持枪「I'll blow your hand off」、wolfless 屠族「whole pack buried with you」）；③身份揭晓从"单点峰值"改为**梯次剥洋葱**；④**反派绝不认输的 6 阶升级阶梯**；⑤**美式阶级羞辱词库**；⑥**具象情感信物**作结构元件；⑦**背叛者平行视角**双线虐心。
>
> **v2.0 — 量化爽点密度增强。** 针对"单集爽点不足、信息密度不够"，基于 16 剧 ep1 横截面，新增 `references/scene-density-spec.md`（流派分层密度基线 / 7 类爽点引擎 / 单集时序硬钉 / 付费卡点密度公式）与 `references/research-evidence.md`。核心：抛弃"3-4 conflicts/集"一刀切，改按流派 × 集位给量化基线（密度跨流派差 3-4 倍），单集爽点时序、付费卡点、信息密度自检接成**硬门禁**。

Professional short drama scriptwriting system for American female audiences (25-50).

## The Core Insight

Short drama is "network literature visualized" — it takes the emotional mechanics of web novels
and compresses them into 60-90 second episodes optimized for mobile binge-watching. The #1 platform
ReelShort reports 70% of its users are women aged 25-45. The North American market has the highest
ARPU ($4.70) and the highest willingness to pay ($15.99-25/month).

**The 6-Second Law**: 80%+ of users decide whether to continue watching within the first 6 seconds.
Every episode hook must be unskippable.

## Reference Files

Load these files as needed during the workflow:

| File | When to Load |
|------|-------------|
| `references/source-adaptation-workflow.md` | **FIRST — when user provides ANY source material (novel/script/outline)** |
| `references/production-types.md` | **Before writing — determine Narration-Driven or Dialogue-Driven** |
| `references/script-structure.md` | **MANDATORY — 剧本前述（简介/看点/小传）+ 正文（分集）格式** |
| `references/bilingual-format-guide.md` | **所有剧本输出——中英文混合格式规范** |
| `references/netflix-cinematic-standard.md` | **Before writing — Netflix-level visual direction standards** |
| `references/audience-insights.md` | Before starting any project — understand who you're writing for |
| `references/cultural-adaptation.md` | When adapting Chinese content or uncertain about cultural elements |
| `references/drama-formats.md` | When outlining episodes or checking structural requirements |
| `references/genre-templates.md` | When selecting genre or building beat sheets |
| `references/screenplay-format.md` | Only when user explicitly requests American screenplay, panel tables, anime blocks, or production-prompt tables |
| `references/viral-formula.md` | When designing hooks, cliffhangers, or card boundaries |
| `references/ai-collaboration.md` | When determining AI vs human work split |
| `references/redfruit-methodology.md` | When seeking proven industry writing methodology from top creators |
| **`references/scene-density-spec.md`** | **MANDATORY — 写每集前定密度档 + 写完逐集自检（量化爽点密度）** |
| **`references/netshort-arc-mechanics.md`** | **MANDATORY（v3.0 新增）— 写复仇/隐藏身份/契约婚等 netshort 流派时，整弧付费转化结构：梯次身份揭晓 / 付费墙=生死危难 / 反派升级阶梯 / 阶级羞辱词库 / 具象信物 / 背叛者平行视角。写整条免费弧前必读。** |
| `references/research-evidence.md` | 25 剧真实视频反推证据（密度基线 + 全弧结构的数据来源，v3.0 含 3 条 netshort 全弧） |
| **`references/research-evidence-v4.md`** | **v4.0（密度基线）— mlx-turbo 重转写 13 剧/44 集的量化证据 + 机制纠错 + 爽点引擎重排（隐藏实力=43%居首）。引用密度数字以本文为准。** |
| **`references/research-evidence-baidu.md`** | **v4.1 新增 — 数据源 #3（85 部 AI仿真人剧发行元数据）证据：付费墙卡点 10 聚类 / 长弧 71 集 / 霸总+虐心双基底。写长弧仿真人剧前读。** |
| **`references/research-evidence-video.md`** | **v4.2 新增 — 视频级反推（netshort 44 + shorttv 87 = 131 集全量 ASR）证据：冷开场 0.26s / 节拍 18.5 segs·min⁻¹·169 wpm / 爽点簇射曲线（15 弧付费墙集爆 5–10）/ 决策悬崖（纯肉体危机仅 27%）/ 中段禁零 / netshort-vs-shorttv 工艺分野。写每集冷开场 + 付费墙集前读。** |
| **`references/overseas-cinematic-craft.md`** | **v4.4（MANDATORY for 海外英文仿真人剧）— 4 簇交叉电影感工艺：密度校准(≥7/≥80) / 视觉承重集豁免 / **密度曲线 4 原型(A后载/B平坦/C前载尖峰/D中峰+揭底谷，v4.4 证伪v4.3单一"付费墙=top-2")** / **爽点元引擎=戏剧反讽信息差(§9，关键词库漏判50-100%)** / 道德绑架虐心尖峰4拍beat(§10) / 跨时空冷开场(§11) / 神话堕神降世spine / 第8类爽点「觉醒变身」/ **主角声口4变体(§6.1)** / 儿童信使揭露。写海外本土仿真人剧(英文对白、北美市场)前必读——套中文 netshort 密度(18.5/169)会误判高质量集。** |
| **`reverse-engineering-pipeline/README.md`** | **v4.0 新增 — netshort+shorttv+百度 抓取/ASR/分析流水线（skill化）。加剧/换平台前读，机制不再重新探索。** |
| **`references/storyboard-reverse.md`** | **v4.5 新增 — 视频→15s 分镜→剧本 反推工艺（seedance 2.0 = 1 shot/15s）。拿到竞品 mp4 要拆分镜 / 要批量产 seedance T2V prompt 时读。含 7 字段 schema（已验证）/ 视觉连续性三重锚定 / 名字卡硬规范 / 成本模型 + 采样策略。** |

### Source Material Guide

When user provides source material, load `references/source-adaptation-workflow.md` FIRST and classify:

| Source Type | Operation Mode | See Workflow Section |
|-------------|---------------|---------------------|
| Chinese novel (complete chapters / partial) | Rewrite (文化改写) | Type A |
| English novel (complete / partial chapters) | Expand (扩写) | Type B |
| Chinese script (complete / partial) | Rewrite (文化改写) | Type C |
| English script (complete / partial) | Write-in-style (仿写) or Expand | Type D |
| Concept / idea only (no source) | Original creation | Scenario 5 |

The workflow auto-determines: operation mode, episode count, genre template, and cultural adaptation level.

### Production Type Selection

AI realistic human drama has two production modes. Load `references/production-types.md` to select:

| Type | Name | Best For |
|------|------|----------|
| **A** | Narration-Driven (旁白解说型) | Internal monologue, complex backstory, revenge/calculation |
| **B** | Dialogue-Driven (对白演绎型) | Sharp banter, multi-character conflict, subtext-heavy romance |
| **Hybrid** | Both | Setup uses more narration; climax shifts to pure dialogue |

> **密度档校准**：Type/B 流派决定密度基线，见 `references/scene-density-spec.md` §1。对白密集型（复仇/契约婚/宫斗/情感悬疑）segs/min 8-21、首对白 ≤10s；标准言情型（萌宝/霸总/抚养权）5-7；奇观慢热型（玄幻/狼人/吸血鬼/神话）4-7.6、首对白可达 27-81s（允许大段世界观镜头）。**切勿用统一密度要求套所有流派。** **海外英文仿真人剧（英文对白/北美市场，v4.3 新增）**密度更低（实测 11.7 segs/min·97 wpm），逐集地板下调至 ≥7/≥80，且低对白高视觉的"视觉承重集"过三问后豁免——见 `references/overseas-cinematic-craft.md` §1–§2。
>
> **集时长预算（v3.0 修正）**：每集 **90–150s 常规**（约 180–300 词），首集/揭晓峰/付费墙集 **160–215s**（约 320–430 词）。**不要再把剧本压进 60s**——netshort 全弧实测（3 剧 / 29 集）集均 156s，付费墙集普遍 200s+，硬压 60s 会迫使对白虚高或砍情绪铺垫。详见 `scene-density-spec.md` §1b。

> **整弧付费转化（v3.0 新增硬门禁）**：写复仇/隐藏身份/契约婚/玄幻等 netshort 主力流派时，**必读 `references/netshort-arc-mechanics.md`**。关键：netshort 付费墙卡在**主角最大生死危难**（≠ shorttv 的真相曝光），真相与清算全押墙后；身份/底牌**梯次揭晓**（每集一层）；反派**绝不认输**逐级升级；配 1 件**具象情感信物** + **美式阶级羞辱词** + **背叛者平行视角**。三剧三流派（bankrupt/maco/wolfless）全部坐实。
>
> **神话/堕神降世复仇 spine（v4.3 新增）**：神/神话存在为爱堕凡→失忆→遭背叛→觉醒→复仇是海外高频设定，netshort-arc §9 只给一句"玄幻混合模型"——完整工艺（双时间线序章冷开场 / 封印记忆上帝视角开关 / 神话工具 / 12 集可复用节拍表）见 `references/overseas-cinematic-craft.md` §4。

### Netflix Cinematic Standard

ALL scripts must meet `references/netflix-cinematic-standard.md`:
- Color-graded Action Lines (temperature, palette)
- Motivated lighting (Rembrandt, chiaroscuro, rim, practical)
- Professional camera work (shot sizes, depth of field, composition)
- Production design detail (costume, environment, props as storytelling)
- One "movie moment" per episode (poster-worthy frame)
- Pacing rhythm following emotional beats

## Workflow Overview

Creating a short drama script involves these steps:

1. **Intake & Analysis** — Determine input type and core story
2. **Genre Mapping** — Match story to proven genre template
3. **Cultural Adaptation** — Localize for American audience
4. **Episode Outlining** — Build 60-80 episode arc with beat sheet
5. **Script Writing** — Write episodes in Chinese short-drama delivery format, with optional AI-production visual notes
6. **Quality Check** — Validate against audience and format rules

## Step 1: Intake & Analysis

Read `references/source-adaptation-workflow.md` for the complete source material processing system.

### When User Provides Source Material (Novel / Script / Outline)

Execute the **Input Analysis Protocol** automatically:

**Step 1A — Source Classification:**
- Language: [Chinese / English]
- Format: [Novel prose / Script / Outline / Mixed]
- Completeness: [Complete story / Partial chapters / Outline only / Fragments]
- Word count: [Approximate]

**Step 1B — Auto-Select Operation Mode:**

```
Chinese source? → Rewrite (文化改写)
English source + incomplete? → Expand (扩写)
English source + complete? → Write-in-style (仿写)
```

**Step 1C — Content Extraction:**
- Protagonist (wound, want, defining trait)
- Antagonist (power, motivation, relationship)
- Love Interest (if applicable)
- Inciting Incident, Central Conflict, Emotional Core, Karma Moment
- Setting, Tone

**Step 1D — Gap Analysis:**
Compare against 60-80 episode series requirements. Identify what's missing.

**Step 1E — Direction + Episode Count Determination:**
Report to user: operation mode, episode count (60-80), primary genre template, cultural adaptation level, and justification.

### When User Has NO Source Material (Original Creation)

Skip source analysis. Proceed directly to:
- Genre template selection (see Step 2)
- Character creation
- Episode architecture

### Key Questions (All Projects)

- What is the protagonist's defining wound and want?
- Who is the antagonist and what power do they hold?
- What is the central romantic or empowerment fantasy?
- What public "karma moment" delivers catharsis?

### The Golden Triangle (from Hongguo/Redfruit methodology)

Every successful short drama must establish within Episode 1:
- **Identity**: Who is the protagonist? (Not backstory — current status)
- **Crisis**: What immediate threat or problem do they face?
- **Goal**: What do they want? (Clear, active, driving motivation)

If these three elements are not clear within the first episode, the opening needs rewriting.

## Step 2: Genre Mapping

Read `references/genre-templates.md` and select the closest match:

| User Request Pattern | Genre Template | US Market Performance |
|---------------------|----------------|----------------------|
| Marriage contract, fake relationship, billionaire husband | The Billionaire's Secret | #2 genre |
| Revenge after humiliation, transformation, former bully | The Return | Strong |
| Twin swap, lookalike, mistaken identity | Wrong Place, Right Person | Moderate |
| Office politics, passed over, proving worth | The Underdog's Rise | Growing |
| Widow/divorcée, finding love again, starting over | Love After Loss | Niche but loyal |
| Discovered inheritance, secret family, sudden wealth | The Hidden Heir | Moderate |
| Werewolf mate, alpha, fated bond, supernatural romance | Fated to the Alpha | **#1 genre** |
| Vampire romance, immortal love, blood bond | Immortal Desires | Classic |
| Mafia boss, forbidden love, dark romance | Dangerous Vows | Emerging |

**If uncertain which genre to choose for US market**: Start with werewolf/alpha or billionaire romance — these are the top two performers on ReelShort and DramaBox.

If the story blends genres, identify the primary genre for structural beats and secondary genre for flavor.

## Step 3: Cultural Adaptation

Read `references/cultural-adaptation.md` for detailed guidance. Core principles:

**The 50% Rewrite Rule**: Direct translation has a 50% failure rate. The most successful adaptations undergo 50% content rewriting — not just words, but cultural mechanisms, social logic, and emotional triggers.

**Key cultural replacements**:
- Face/mianzi → Social reputation / public image / "cancel culture"
- Filial piety → Family legacy / expectation / guilt trip
- Guanxi connections → Old boys' network / nepotism
- Imperial hierarchy → Corporate / social hierarchy
- Harem intrigue → Boardroom / office politics

**Americanize settings**: Manhattan penthouses, Hamptons estates, Silicon Valley startups, Ivy League campuses, LA mansions.

**Remove red flags**: Eliminate colorism, romanticized non-consent, underage romance, racial stereotypes, pure wealth worship without character growth, forced submission presented as romance.

**Add American expectations**: Diversity in casting descriptions, mental health awareness, female friendship (Bechdel test), clear romantic consent, professional competence as attractive trait.

**Never assume cultural context transfers**: Explain nothing, show everything.

## Step 4: Episode Outlining

Read `references/drama-formats.md` for structure specifications and `references/viral-formula.md` for hook/cliffhanger design.

### Mandatory Structure
- **60-80 episodes**, each 60-90 seconds when produced
- **Every episode** must have: Hook (0-3s), Setup, Confrontation, Twist, Cliffhanger (last 5-10s)
- **EP1 黄金三角（强制审核关，NG14）**：第 1 集开场 10s 内须清晰交付三问——**身份**（主角现在是谁，非过去）+ **危机**（即时、具体、有压迫感的威胁）+ **目标**（主动想要什么，具体可衡量）。三项任一模糊 → 直接重写（行业"淘汰第一关"）。通过动作展示，禁旁白解释。
- **Major escalation every 5 episodes**
- **Genre set piece every 10 episodes** (gala, trial, wedding, boardroom battle)

### The Card System (Paid Conversion Architecture)

```
First Card (Ep 1-10):    Free preview → STRONGEST cliffhanger at Ep 10
Second Card (Ep 11-20):  $X.99 → identity/relationship crisis
Third Card (Ep 21-30):   $X.99 → public showdown
Fourth Card (Ep 31-40):  $X.99 → betrayal/loss
Fifth Card (Ep 41-50):   $X.99 → transformation complete
Sixth Card (Ep 51-60):   $X.99 → reversal
Seventh Card (Ep 61-70): $X.99 → pre-finale
Eighth Card (Ep 71-80):  $X.99 → resolution
```

**Critical**: The episode immediately BEFORE each card boundary must have the STRONGEST cliffhanger in that arc. This is where payment conversion happens.

> **⚠️ 行业指南冲突裁定 B（卡点物理危险 vs 实证）**：ReelShort 指南主张"Ep10/20/30 强制 Type 1 物理危险 / Type 2 倒计时 / Type 3 背叛揭露"，但本 skill v4.2 的 15 弧实证——**决策/宣告悬崖**（离婚/签约/揭身份/复仇启动）占主流，**纯肉体危机仅 27%**；v4.5 243/mars 付费墙再证（悬念钩 / 揭底谷）。**采信实证，按流派分**（见下方 v3.0 分流）：物理危险仅 netshort 复仇弧适用，非通用硬规则。详见 `COMPARISON-FINDINGS.md` 附录 C.2。

> **⚠️ v3.0 付费墙分流（重要）**：cliffhanger 的**类型**因平台/流派而异——
> - **shorttv 模型**（宫斗/情感悬疑）：cliffhanger = **真相即将曝光**（"喝下毒杯的是你"）。观众付费为"看反应"。用本节三件套。
> - **netshort 模型**（复仇/隐藏身份/契约婚/玄幻）：cliffhanger = **主角最大生死危难**（bankrupt 扣药+铁链 / maco 持枪「I'll blow your hand off」/ wolfless 屠族「whole pack buried with you」）。**真相与清算全部押到墙后**，它们是奖励不是诱饵。观众付费为"看救赎+清算"双重奖励。**必读 `references/netshort-arc-mechanics.md` §2。**

### 付费卡点集密度公式（见 `references/scene-density-spec.md` §4）

真实爆款反推证明：付费墙前的卡点集**密度回升至中段集的 ~1.5–2×**，并叠加**虐点峰值 + 真相方蒙鼓 + 双层 cliffhanger**（ mommy ep6 主角死亡+"妈妈会后悔吗"灵魂拷问；crown ep6 渣男逼退位+"喝下毒杯的是你"真相揭穿即卡）。每张卡末集必须满足：
1. **虐点/冲突峰值** — 把主角推到该弧最痛的点
2. **真相方仍蒙在鼓里** — 施虐者/误解者继续冤枉，上帝视角虐心拉满
3. **双层 cliffhanger** — 动作层（真相方即将发现）+ 灵魂层（受害方画外音拷问）
4. **密度回升** — 卡点集 segs/min ≥ 该剧中段集均值的 1.5×，叠加 ≥2 类爽点引擎

### Create a master beat sheet before writing:

```
Ep 1-5:   [Setup phase - one sentence per episode]
Ep 6-10:  [Escalation phase - one sentence per episode, Ep 10 = CARD CLIFFHANGER]
... (continue through Ep 76-80)
```

For each episode, note:
- Location
- Characters present
- Central conflict
- Twist / new information
- Cliffhanger
- Card boundary (if applicable — must be DEVASTATING)

## Step 5: Script Writing

Read `references/script-structure.md` for 前述+正文格式要求,
`references/production-types.md` for Narration-Driven vs Dialogue-Driven guidance,
`references/netflix-cinematic-standard.md` for visual direction standards, and
**`references/bilingual-format-guide.md` for 中英文混合格式规范** (mandatory).
Load `references/screenplay-format.md` only when the user explicitly requests American screenplay,
panel tables, anime blocks, or production-prompt tables.

### CRITICAL: Two Decisions Before Writing Episode 1

**Decision 1: Production Type** (see `references/production-types.md`)

| Type | Name | Core Mechanic |
|------|------|--------------|
| **A** | Narration-Driven (旁白解说型) | `旁白：` / `角色VO：` drives story + character dialogue supplements |
| **B** | Dialogue-Driven (对白演绎型) | Pure dialogue + physical action, minimal/no narration |
| **Hybrid** | Both | More narration in setup (Ep 1-20), shifting to dialogue by climax (Ep 60+) |

**Decision 2: Netflix Cinematic Standard** (see `references/netflix-cinematic-standard.md`)

Key action lines should carry cinematic direction without bloating every beat:
- Color temperature and emotional palette
- Motivated lighting (direction, quality, source)
- Shot size with depth of field description
- Frame composition (rule of thirds, center frame, negative space)
- Camera movement (or intentional stillness)
- One "movie moment" per episode

### The Standard Format (Chinese Short-Drama Delivery Draft)

Default scripts use the same plain-text format as the reference sample scripts. Visual indentation or centering in Word/PDF is only screen layout, not a script grammar requirement:
- Episode marker: `第1集` / `第 1 集`
- Scene marker: `1.1 土路边 日 外`, `1-1 日，内，酒店`, or equivalent `1-1场景：酒店 / 时间：日 内`
- Characters: `人物：叶知秋，林玹` or `出场人物：...`
- Action/visuals: `△` for normal action, `▲` for flashback/key visual/special emphasis
- Dialogue: `角色名（语气/动作/状态）：台词`
- Narration/inner voice: `旁白：`、`画外音：`、`角色VO：`、`角色（OS）：`
- Optional screen text: `字幕：` or `【字幕：...】`

### Format Requirements
- **Language**: 默认动作描述/镜头指示/制作注释 = 中文；对白/旁白/屏幕文字按项目市场决定（美国项目用英文，中文内测/国内样稿可用中文）
- For US-market scripts, keep character/location names in English on first mention, with Chinese notes only where useful for production.
- Present tense only
- Visual, cinematic language — show don't tell — **with Netflix-level color/lighting/composition**
- Each episode is self-contained but ends unresolved
- Character physical traits remain IDENTICAL across all episodes (use Character Bible)
- Production type (A/B/Hybrid) established in Episode 1 and maintained throughout
- Do not put dialogue/narration into tables, quote boxes, code blocks, separate “dialogue/narration” boxes, or American screenplay indentation blocks unless explicitly requested.

### 前述 + 正文 结构 (MANDATORY)

每部剧本必须包含**前述**和**正文**两大部分。详见 `references/script-structure.md`。

**前述（前置内容）必须包含**：
1. **剧名** — 英文 + 中文
2. **简介** — 200-500字故事梗概（人物+冲突+走向）
3. **看点** — 3-5条创意亮点/卖点（供平台和投流使用）。**v4.5 G8 三层梗结构**：每条卖点拆三层——**核心梗**（题材类型，如"打小三/身份曝光"）+ **创新点**（本剧独有反转，如"女主=男主女儿"）+ **微创新点**（vs 同题材差异化，如"绝嗣设定"），逼出"与同题材比新在哪"
4. **人物小传** — 每个角色五维度：外在/内在/状态/行动/变化 + 记忆点标签。**v4.5 NG1**：①"外在"强制含**发色+瞳色 EN 双锚**（如 `冷调铂金色发（Platinum Blonde）/ 深邃冷灰眼（Grey eyes）`）——生物特征比服装色跨帧稳定，解决 image-gen 颜色漂移（pilot 实测服装色不可靠，见 storyboard-reverse §3.1）；②新增**声音**维度（音域 Alto/Baritone + 口音 + 语速 + 用词偏好），ASR/配音一致性硬约束

**正文（分集剧本）每集必须包含**：
- 集数标注
- 场景（地点+日/夜+内/外）
- 出场人物
- 画面（`△/▲`动作画面 + 对白/旁白/OS/VO）
- 本集反转
- 下集悬念
- 情绪标签（虐/甜/燃/泪/惊/气愤）

### The American Sound Checklist

Before finalizing dialogue, verify:
- Contractions used naturally ("I'm," "don't," "can't")
- American idioms present ("hit the ground running," "read the room")
- No translated-sounding lines ("You dare to...?" → "You think you can...?")
- Sentence fragments for tension ("You. Out. Now.")
- Regional flavor if setting is specific
- Profanity used sparingly for impact

### The Bullet Principle (from industry top creators)

Every line of dialogue must be a **bullet**, not cotton:
- Cut all redundant modifiers, unnecessary greetings, empty pleasantries
- Keep only what drives plot OR reveals character
- Test: cut 30% of the words — does the core message survive? If yes, keep the cut version
- Every line should simultaneously: advance plot + reveal relationship + hint at subtext
- **每集 ≥1 金句 + ≤15 句对白（NG15）**：每集至少一句"可截取传播"的高光台词（耳光台词 / 震撼宣告 / 反转金句，能独立截图传播）；单集对白总量 ≤15 句（60-90s 集长，配合 ≤8 词/句 + 150-210 词/集预算）。零闲聊零寒暄——删所有问候/天气/客套。

### 情绪弹簧 + 单集爽点时序（v2.0 硬钉 — 见 `references/scene-density-spec.md` §2 §3）

**情绪弹簧**：每一集要么**压**（虐/受辱/受挫/冤枉/低估）要么**放**（爽/甜/解气/震撼/真相），**禁止平推集**。连续 2 集压后第 3 集必须放。

**单集时序硬钉**（与集时长无关）：
```
0–6s    首钩子（核心前提 / 打脸开场 / 身份伏笔）
6–30s   铺垫升级（抛出本集核心冲突）
30–45s  中段反转【硬钉】（新信息改变方向 — 压或放）
末5–10s 结尾再钩子（比 6s 钩子更强的未竟爽点）
```
真实佐证：married-a-ceo 2.8s 婚姻宣布→76s 街边拉人结婚（放）→158s "Wait. What?"；adopted-baby 0s 喜剧打脸→54s 被骂 beggar（压）→77s "you just said no to a god"（放）。

**爽点引擎库（8 类）**：打脸反杀 / 身份揭晓 / 霸总护妻护崽 / 隐藏实力被低估（玄幻+逆袭+萌宝核心）/ 虐心-悔恨（情感悬疑付费主引擎）/ 契约婚反转 / 上帝视角反差 / **觉醒变身（v4.3 新增——主角态变时刻「她终于回来了」，区别于身份揭晓的"原来如此"；神话降世/重生/逆袭觉醒题材的第二高潮，落弧 60–75%）**。前 7 类例证见 `scene-density-spec.md` §3，第 8 类见 `overseas-cinematic-craft.md` §5。**每集至少落地 1 类**。**⚠️ v4.4 元引擎**：4 簇反推证实爽点真引擎 = **戏剧反讽 / 信息差**（观众 > 角色），关键词库对真实引擎漏判 50–100%——写每集**先填信息差结构**（「观众知道___，而___不知道，所以此幕爽/虐来自___」填不出 = 重写，见 `overseas-cinematic-craft.md` §9），关键词类型仅作**兑现手段 checklist**。

### Writing Quality Standards
- **Dialogue**: Sharp, subtext-rich, American idiom. Avoid translated-sounding dialogue.
- **Pacing**: No dead scenes. Every scene moves plot or deepens character.
- **Hooks**: Open with visual shock, provocative line, or dramatic reversal. See `references/viral-formula.md` for hook templates by genre.
- **⚠️ 行业指南冲突裁定 A（0-3s 纯视觉 vs 实证）**：ReelShort 指南主张"0-3s 纯视觉零对话"，但本 skill v4.2 的 131 集 ASR 实证——首句对白/旁白落 **0-1s（均值 0.26s）**，in-media-res 进行时冲突。**采信实证**：对白与画面冲击同步（非互斥），不强制"零对话"。详见 `reverse-engineering-pipeline/_pilot_243_qianjin/COMPARISON-FINDINGS.md` 附录 C.2。
- **Cliffhangers**: Unresolved tension — revelation interrupted, door opening, "You won't believe who I am," etc. See `references/viral-formula.md` for cliffhanger types.
- **Binge architecture**: Each episode makes the next one irresistible. Use the 3-second rule: viewer must click next within 3 seconds of episode end.
- **Conflict density**: Target 3-4 conflicts per episode (external plot, relationship, internal, social/time).

### Episode Delivery Pattern
When writing, produce episodes in batches of 5-10 for user review, or write full series if requested.

## Step 6: Quality Check

Read `references/audience-insights.md` for audience validation.

### Mandatory Checks

- [ ] Protagonist has clear agency in every episode
- [ ] Female friendship or mentorship exists (not just rivalries)
- [ ] Romantic interest shows genuine vulnerability, not just dominance
- [ ] Clear consent markers in all romantic scenes (non-negotiable for US market)
- [ ] "Karma moment" is earned and satisfying (not deus ex machina)
- [ ] No cultural red flags (stereotypes, colorism, non-consent, forced submission)
- [ ] Every episode has hook (first 3 seconds) and cliffhanger (last 5-10 seconds)
- [ ] Dialogue sounds authentically American (not translated)
- [ ] Setting and social dynamics reflect American reality
- [ ] Pacing matches **90-210 second** episode format (v3.0：60-90s 仅适用高密度省钱集；常规 90-150s，首集/付费墙集 160-215s)
- [ ] Total episode count falls within 60-80 range
- [ ] Card boundary cliffhangers are devastating enough to drive payment
- [ ] **前述部分完整**: 剧名 + 简介 + 看点 + 人物小传（五维度）
- [ ] **正文每集完整**: 集数 + 场景 + 人物 + 画面 + 本集反转 + 下集悬念 + 情绪标签
- [ ] **Golden Triangle established in Ep 1**: Identity + Crisis + Goal all clear
- [ ] **Bullet Principle applied**: Every dialogue line earns its place
- [ ] **密度档已定并达标（v2.0 硬门禁）**：按 `scene-density-spec.md` §1 确定本剧档位（对白密集/标准言情/奇观慢热），逐集过 §5 自检表（segs/min、words/min、首对白延迟、中段反转 30–45s 落点）。**海外英文仿真人剧改用 `overseas-cinematic-craft.md` §12 自检（地板 ≥7 segs/min·≥80 wpm）**，低对白集先过 §2 视觉承重豁免三问（沉默是否承载可命名视觉动作链 / 对白是否每句承重 / 是否有戏剧反讽信息差）
- [ ] **情绪弹簧无平推**：每集明确压或放，无连续 3 集同方向
- [ ] **爽点引擎落地**：每集 ≥1 类 §3 引擎；卡点集 ≥2 类叠加 + 付费三件套
- [ ] **付费卡点集密度回升**：每张卡末集 segs/min ≥ 中段均值 1.5×
- [ ] **整弧付费转化（v3.0 硬门禁，netshort 流派必过）**：过 `netshort-arc-mechanics.md` §10 自检——付费墙落点是主角生死危难（非真相曝光）、身份梯次揭晓（每集一层）、反派免费弧内零认输（≥4 阶升级）、1 件具象情感信物牵涉危难、阶级羞辱词与女主底牌一一对应、≥1 拍背叛者平行视角
- [ ] **海外英文仿真人剧追加（v4.4）**：①**先定密度原型**（A 后载爬坡/B 平坦高位/C 前载尖峰/D 中峰+揭底谷，按题材选，见 `overseas-cinematic-craft.md` §3）——**禁再用"付费墙集=top-2"通用规则**（v4.4 证伪：仅原型 A 适用；原型 D 付费墙故意落谷但须含揭底判词）；②**每集填信息差结构**（§9 元引擎：「观众知道___而___不知道」填不出=重写；关键词库仅作兑现 checklist，不靠计数判爽点足不足）；③**主角声口锁定 1 变体全弧不漂移**（§6.1：冷峻尊严/受伤诘问/牺牲决绝/冷峻权威），每集 ≥1 句标志判词；④密度尖峰非动作集时用 §10 道德绑架 4 拍 beat；归来/异地冷开场用 §11 跨时空双线同屏；⑤≥1 次真相揭露用无意识信使（孩子画作/童言/旧照/录音，非"撞破查手机"）；2–3 件不同型信物分三阶段登场
- [ ] **第 8 类爽点 + 神话 spine（v4.3，神话题材必过）**：神话降世/重生/逆袭觉醒题材——ep1 含神话序章冷开场(30–70s)+凡世背叛切入(≤70s)；弧 60–75% 处有觉醒变身爽点（态变宣告+复仇宣言+神具登场）；观众已知主角真身而主角失忆（上帝视角总开关）

### Audience Fit Validation
- [ ] Target demographic (women 25-50) would emotionally invest
- [ ] Fantasy element provides escapist satisfaction
- [ ] Relatable pain points addressed
- [ ] Catharsis arc delivers emotional payoff
- [ ] 6-second hook would stop a scroller

## Output Format

### Language Convention (语言规范)

**面向中国制作团队，按发行市场决定对白语言。**
- 美国市场项目：对白/旁白/屏幕文字 = **英文**；动作描述/镜头指示/制作注释 = **中文**
- 中文样稿、国内参考、未指定海外发行时：对白/旁白可用中文，仍保持短剧普通文本正文格式
- 人名/地名按项目设定；美国项目首次出现可附中文译名或制作备注
- 详见 `references/bilingual-format-guide.md`

### 完整剧本结构：前述 + 正文

详见 `references/script-structure.md`。正式交付时直接输出正文，不要用 Markdown 代码块、表格、引用框或“对白/旁白框”包住剧本。结构顺序如下：

═══════════════════════════════════════════════════
                        前述
═══════════════════════════════════════════════════

【剧名】
《英文剧名》
《中文译名》

【简介】
[200-500字故事梗概：主要人物 + 核心冲突 + 大致走向]

【看点】
1. [人设看点]
2. [关系看点]
3. [反转看点]
4. [爽点]
5. [质感看点]

【人物小传】

【女主】NAME / 译名（年龄）
[外在/内在/状态/行动/变化五维度，150-300字]
记忆点标签：#标签1 #标签2

【男主】NAME / 译名（年龄）
[外在/内在/状态/行动/变化五维度，150-300字]
记忆点标签：#标签1 #标签2

【反派】NAME / 译名（年龄）
[外在/内在/状态/行动/变化五维度，150-300字]
记忆点标签：#标签1 #标签2

═══════════════════════════════════════════════════
                        正文
═══════════════════════════════════════════════════

第 1 集

1.1 地点 日/夜 内/外
人物：角色A、角色B

字幕：（**人物首入强制**：`【字幕：身份-姓名】`，如 `【字幕：华尔街风投合伙人-Isabella】`；地点/时间提示可选。overseas 仿真人剧借名字卡埋伏笔——如父系标注 `THE SON OF LUKE MILLER` → 血缘反转种子。两源互证：视频反推 + 海外本子均硬命中此工艺，详见 `references/storyboard-reverse.md` §3.2）

△动作/画面描述（可含Netflix级视觉指导：色温、灯光、景别、景深、构图）。
角色A（语气/动作）：台词。
角色B：台词。

角色A（OS）：内心独白。
角色A VO：回忆/旁白式声音。
旁白：非角色叙述或补充信息。

▲闪回/特写/关键视觉：动作描述。

【本集反转】：[一句话描述本集核心反转]
【下集悬念】：[一句话钩子，引导点击下一集]
【情绪标签】：[虐/甜/燃/泪/惊/气愤，选1-2个]
【卡点】：（**付费墙集必填**，非墙集可省）该集付费悬崖的**特写道具锚点 + 具象画面 + 信息差判词**，如 `【卡点·付费卡】特写：掌心里静静躺着一根长发。Alexander 满脸红酒死死盯着 Isabella。`（参照海外本子 fuhun-ju 集末 `【卡点】` 标记）。**v4.5 G5 升级三元标注**：每个集末卡点须标类型——`【卡点·悬念钩】`（下集开头即揭，非墙集常用）/ `【卡点·假钩子】`（本集末制造悬念但下集转移焦点）/ `【卡点·付费卡】`（真付费墙集，仅墙集用）。卡点必含 1 个**特写道具锚**（信物/凶器/文件等具象物），是 image-to-video 的视觉抓手。

---

第 2 集
[同上格式]

**格式要点**：
- 场景标注：优先 `X.Y 地点 日/夜 内/外`，也兼容 `X-Y 日/夜，内/外，地点`（集-场号 + 地点 + 时间 + 内/外）
- 动作描述前加 `△` 或 `▲` 符号，与对话明确区分
- 对白使用 `角色名（语气/动作）：台词`，不要输出单独对白框、表格、引用块或 screenplay 缩进块
- 字幕用 `字幕：` 标注（人物介绍、地点、时间提示）
- OS/VO/旁白/画外音严格区分，但都使用行内冒号格式
- 每集末尾必须标注：本集反转、下集悬念、情绪标签（付费墙集另加 `【卡点】`）
- **overseas 双语输出（硬规则，v4.5 NG13 补全）**：英文仿真人剧**每句台词 + 每行场景/动作描述（△ 行）**都须 CH + EN 双写——非仅对白层（3 样本校准：sterling/fuqi/zhangfu 场景描述层普遍缺 EN 是共性 gap）。台词 `Alexander（暴怒）：别碰她！/ Don't touch her!`；动作 `△暖金光从落地窗倾泻 / warm golden light floods through floor-to-ceiling windows`。中文短剧单语即可。
- **音效层 `-VO-：`**：每场在动作/对白间穿插音效标注（如 `-VO-：玻璃碎裂声` / `-VO-：门锁转动声`），与 OS/VO/旁白同行内冒号格式。海外仿真人剧靠特写 + 音效承重，音效是必备层（见 `overseas-cinematic-craft.md` §1 信息载体三层的"演 + 看字幕 + 听音效"）。
- **名字卡强制**：人物首入必给 `【字幕：身份-姓名】`（非可选），overseas 剧常借此埋伏笔。
- **每集三标记（NG16，竖屏 + 传播 + AI 生产）**：每集正文至少嵌入 ① **【竖屏特写】** 1 个（CU/MCU，适配 ReelShort/TikTok 9:16）② **【可截取传播高光】** 1 个（耳光/震撼揭露/金句/反转瞬间，能独立成片）③ 关键画面附 **【AI 生成提示参考】**（`[景别], [主体], [动作], [表情], [灯光]`，可直接翻译为 image-to-video prompt）。参照 `references/screenplay-format.md` 的 `--ar 9:16` 表格范式。

### Series Bible:

前述部分：
- 剧名（英文 + 中文）
- 简介（200-500字故事梗概）
- 看点（3-5条创意亮点/卖点）
- 期待（**5 条观众爽点承诺**：本弧必须兑现的具体 payoff 场景，如"反派对峙下跪 / 真相揭开 / 苦肉计 / 病房极致对峙 / 复仇达成"。**与"看点"区分**：看点=卖点定位，期待=承诺契约，须在分集表中逐条标注兑现集。参照海外本子 fuhun-ju `三、期待`）
- 人物小传（每个角色五维度 + 记忆点标签 + 角色关系图）

正文部分：
- 60-80 episode master beat sheet
- 分集剧本（每集含：画面/对白/本集反转/下集悬念/情绪标签）

制作规格：
- Production Type declaration (Narration-Driven / Dialogue-Driven / Hybrid)
- Character Consistency Bible (locked physical traits, prompt seeds, style references)
- Netflix Color Palette lock (primary temperature, key color references)
- Lighting style lock (Rembrandt/chiaroscuro/practical/etc.)
- **拍摄质感参考（v4.5 G6）**：列 3–4 部具体 IP 锚定视觉 tone，逼出"vs 通用 AI 出片"差异化。格式 `拍摄质感参考：《IP1》(tone 关键词) / 《IP2》(tone 关键词) / 《IP3》(tone 关键词)`，例 `《Succession》(老钱冷峻+庭审光线) / 《Billions》(华尔街权力对峙+办公室冷调) / 《The Devil Wears Prada》(时尚圈压迫+奢侈品特写)`。**禁只用抽象色温描述**——sterling 反面教训：纯抽象 per-ep 色温（"暖金+冷蓝对比"）让 image-gen 出片飘忽，须参照剧锚定。
- Genre notes and adaptation rationale (if adapted)
- Pacing map (emotional intensity per episode)
- Card boundary cliffhanger specifications

## AI Collaboration Note

Read `references/ai-collaboration.md` for detailed guidance on human-AI workflow.

The 70/30 Rule: 70% of structural work can be AI-generated (outlines, format, consistency). 30% must be human-created (emotional beats, cultural nuance, voice). The 30% human input determines whether the script is competent or exceptional.

## Industry Data Backing

Key 2025 market data (DataEye / Guangdada sources):
- 2025 Q1 revenue: $24亿+, downloads: 259M
- Ad materials deployed: 1.27M sets (10x YoY growth)
- Female-oriented content: 77% of market heat value
- Top 3 sub-genres: Romance 34%, Urban 26%, Comeback 14%
- English content: 50%+ of all deployments
- North America: highest ARPU globally ($4.70)
- 2% of hit series generate ~80% of revenue
- Hit series definition: 3-day spend ≥$20K, CTR≥1.5%, 6s completion≥20%

## Real-Video Reverse-Engineering Evidence (v2.0 量化基线来源)

本版密度基线来自 **25 部爆款真实视频反推**（非拍脑袋）：netshort.com 23 部 + shorttv.live 2 部，覆盖复仇打脸 / 隐藏身份霸总 / 复仇契约婚 / 玄幻狼人 / 逆袭造神 / 玄幻吸血鬼 / 霸总萌宝 / 神话重生 / 契约婚抚养权 / 隐藏萌宝 / 逆袭厨神 / 狼人护崽 / 多男主玄幻 / 萌宝财神 / 情感悬疑 / 重生宫斗 / 现代虐心觉醒 / 玄幻龙族·蛇族 / 狼人寻妻。方法：下载真实视频 → ffmpeg 抽音（16kHz mono）→ faster-whisper ASR 逐句时间戳转写（**55+ 集**，含 3 条 netshort 完整免费弧 bankrupt ep1-8 / married-a-ceo ep1-12 / wolfless ep1-9）。完整数据表与每集转写见 `references/research-evidence.md`。

**核心数据**：密度跨流派差 3–4 倍（crown 宫斗 15–21 segs/min vs wolfless 玄幻 4.2 segs/min）；首对白延迟跨流派差 40 倍（adopted-baby 2s vs wolfless 81s）。这证明一刀切的"3-4 conflicts/集"会同时让复仇剧太疏、玄幻剧太密——故 v2.0 改为流派 × 集位分层基线。

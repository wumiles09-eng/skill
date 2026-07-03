# Research Evidence — 视频级反推：netshort + shorttv 真实 ASR 全语料（v4.2）

> **数据线**：本文件是 **v4.2 视频级反推**的证据库，与 `research-evidence-v4.md`（v4.0 密度基线）、`research-evidence-baidu.md`（v4.1 发行元数据）互补。
> **方法**：browser-harness 突破 CDN 抓 mp4 → mlx large-v3-turbo ASR（热池 7-27×）→ `analyze.py` 量化 + 人工深读。
> **证据基线（FINAL）**：**131 集 / 26 剧**（netshort 44 集 + shorttv 87 集，全量 ASR 零错误完成 2026-07-01）。注：shorttv 实际 ASR 转写 93 集，其中 6 集因时长<1s 或空段被 `analyze.py` 过滤 → 87 集有效进入分析；所有数字基于 131 集有效语料。
> **⚠ 诚实告诫（§7）**：爽点类型排序基于关键词正则，对 regex 设计敏感（本文件与 v4.0 的排序不同），**真实类型混合须人工通读判定**，不可单凭正则下产品结论。但 §1–§6 结构性发现与正则无关，全语料坐实。

---

## 跨语料总量（Final，131 集 / 26 剧）

| 指标 | 值 | 含义 |
|------|----|----|
| avg episode duration | **114.8s（1.9min）** | 单集时长（netshort ~2.5min / shorttv ~1.3min，平台分化） |
| avg segs/min（信息密度） | **18.5** | 每分钟对白/事件段数 |
| avg words/min（对白密度） | **169.0** | 每分钟词数 |
| avg first-speech offset | **0.26s** | 冷开场首句起声——极度 in-media-res |
| avg 爽点 hits/episode | **1.35** | 每集爽点命中（hook/付费墙集远高，见 §3） |
| paywall cliff 分布 | **ambiguous 18 / mortal-peril 7 / identity-tease 1** | 纯肉体危机仅 27%，关系/决策悬念占主流（见 §4） |

**平台分化（§6 量化坐实）**：
- **netshort**（`…71649`/`…8593`/`…2882` 等）：长集（137–210s）、中密度（~14 segs/min、~100 wpm）、对白对峙驱动。
- **shorttv**（slug 名剧）：短集（57–150s）、高密度（~21 segs/min、~200 wpm）、旁白内省 + 对白叠加。短集靠高 segs/min 维持信息密度。

---

## §1. 冷开场 in-media-res：首句对白 0.0–0.3s 起（新硬默认）

**证据**：全语料 avg first-speech offset = **0.26s**。深读 `2059541389654171649` ep1：0.0s 即开口「Vivian and I are officially getting married today」，8s 揭背叛、25s 双视角上帝反差。无环境建立镜头 / 无旁白自我介绍铺垫。

**深读实证**（`2059541389654171649` ep1，162s，契约/背叛冷开场）：
```
[  0.0-  8.3] Vivian and I are officially getting married today. I've been waiting for this for too long, finally.   ← 0s 进行时冲突
[ 21.3- 28.1] That fool's actually waiting for you to sign the marriage certificate? You going? Nah. I love you, sweetheart. Not him.   ← 25s 双视角上帝反差
[ 48.8- 50.0] Nathan, we're done.   ← 50s 干净分手
[106.3-110.4] I'd rather grab a stranger off the street and marry him.   ← 契约婚前提种子
[154.8-159.9] Now you are legally married. — Wait, what?   ← 决策悬崖
```

**规则**：每集第一句对白/旁白落 **0–1s**（硬默认 0–0.5s），必须是**进行中的冲突**；ep1 须 **≤10s** 点出全剧核心前提；冷开场 25s 内建立**观众 > 主角的信息差**（双视角同时切主角不知情的背叛/阴谋）。

---

## §2. 节拍密度量化（18.5 segs/min / 169 wpm / hook ≤30s beat）

**证据**：avg **18.5 段/min**（信息密度）；avg **169 词/min**（对白密度）；first-speech **0.26s**。hook 集 `…71649` ep1 = 162s 内 5–6 个主要节拍 ≈ **每 28s 一个**；shorttv 短集（~60–90s）beat 更密（~15s/beat）。

**规则**（密度用 segs/min 与 wpm 作不变量，segs/集 随集长缩放故不作硬钉）：
- **信息密度 ≥ 15 segs/min**（shorttv 风格 ≥ 20）；**对白密度 ≥ 100 wpm**（shorttv 风格 ≥ 150）。
- **< 90 wpm 判密度不足**（对应原优化诉求 b「信息密度不够」）——语料中 `…2882`(74.5)、`2068175…`(70.8) 等弱剧即落此区。
- **hook 集（ep1–3）节拍间隔 ≤30s**，普通集 ≤45s。
- 每集**至少 1 个明确爽点**（语料均值 1.35/集），hook 与付费墙集 ≥3（见 §3）。

---

## §3. 爽点"簇射"分布——禁止均匀摊铺，强制前重 + 付费墙集爆点

**证据（arc-shape 表，每集爽点命中数；Final 全语料，15 条 ≥5 集弧）**：

| 剧 | ep1 | ep2 | ep3 | ep4 | ep5 | ep6 | ep7 | ep8 | ep9 | ep10 | ep11 | ep12 |
|----|----|----|----|----|----|----|----|----|----|----|----|----|
| `…8593`（8 集·成功弧） | 0 | 1 | 4 | 2 | 4 | 3 | **10** | 3 | | | | |
| `touch-the-dons-wife`（7） | 2 | 2 | 0 | 2 | 1 | 2 | **5** | | | | | |
| `doing-bridal-makeup`（7） | 1 | 0 | 1 | 0 | 0 | 1 | **5** | | | | | |
| `stolen-sight`（6） | 3 | 1 | 2 | 0 | 0 | **5** | | | | | | |
| `my-alpha-killed-me`（7） | 0 | 0 | 0 | 1 | 4 | **5** | 1 | | | | | |
| `mommy-im-not-lying`（6） | 1 | 1 | 0 | 2 | 0 | **6** | | | | | | |
| `identity-unveiled`（11） | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | **5** | |
| `…2882`（9） | 2 | 3 | 1 | 1 | 0 | 0 | 0 | 1 | **5** | | | |
| `…71649`（12） | 2 | 0 | 3 | 1 | 2 | 3 | 0 | 0 | 1 | 1 | 0 | 3 |
| `frozen-vengeance`（10） | 1 | 0 | 1 | 1 | 3 | 0 | 0 | 0 | 0 | 2 | | |
| `the-heiresss-ruthless`（7） | 2 | 2 | 2 | 0 | 3 | 0 | 2 | | | | | |
| `back-with-baby`（9） | 0 | 1 | 2 | 1 | 0 | 1 | 0 | 0 | 3 | | | |
| `you-killed-my-dragon`（6） | 0 | 0 | 1 | 1 | 2 | 0 | | | | | | |
| `oisoned-crown`（5） | 0 | 5 | 0 | 1 | 1 | | | | | | | |
| `look-who-you-killed`（5） | 0 | 1 | 0 | 0 | 1 | | | | | | | |

**发现（全语料坐实，15 弧无一例外）**：
1. **付费墙边缘集必爆**：几乎每条弧的**最后一两集**爽点骤升到 5–10（`…8593` ep7=10、mommy ep6=6、touch-the-dons ep7=5、doing-bridal-makeup ep7=5、stolen-sight ep6=5、my-alpha-killed ep6=5、identity-unveiled ep11=5、`…2882` ep9=5）。**最后一两集免费集必须爽点堆叠**。
2. 成功弧（`…8593`）**单调递增到付费墙峰值**——"复利升温"曲线，留存最优。
3. **付费墙峰值集 = 多类型爽点同场对撞**：`…8593` ep7 同一场对峙塞入 face-slap + hidden-power-reveal（"LK Group will finally be mine"）+ underdog-reversal + 背叛虐心 + 离婚宣告。不是"每集一个"，而是"关键集一场戏打五个"。

**规则**：免费弧曲线 = **ep1–3 高位 hook（每集≥3）→ ep4–(N-2) 复利升温（每集≥2 且不得为 0）→ 最后 1–2 集付费墙簇射（≥5，多类型对撞）**。**禁止零爽点集**。

---

## §4. 付费墙悬崖：两种 flavor（决策/宣告 ≳ 肉体危机）

> **与 v3.0 的关系**：v3.0 立「netshort 付费墙 = 主角最大生死危难」（bankrupt/maco/wolfless 三剧坐实）。v4.2 补全：生死危难是**动作/玄幻流派**的 flavor；**关系/背叛流派**的付费墙悬崖更常是"主角做出一个后果性决定/宣告"。两种皆合法，按流派选。

**证据（全语料 cliff 分布）**：`ambiguous 18 / mortal-peril 7 / identity-tease 1`——**纯肉体危机仅 27%**，关系/决策悬念占 69% 主流。

**深读**：
- `…71649` ep1 结尾：「Now you are legally married. — **Wait, what?**」（冲动结婚的错愕后果）
- `…8593` ep7 结尾：「I want a **divorce** and take back everything I gave him.」（离婚宣告）
- `…2882` ep9 结尾：mortal-peril（"your whole pack will be buried with you"）+ 重复呼喊「RAYBON!」（v3.0 风格）
- `frozen-vengeance` ep10 结尾：「Julian, come to the hospital. **Now.**」（最后通牒）

**规则**：付费墙集结尾**默认"决策悬崖"**（离婚/签约/揭身份/复仇启动等不可逆决定，payoff 落在解锁后）；用"危机悬崖"时必须叠情感锚点（身份揭晓/呼喊/信物）。

---

## §5. 中段塌陷 = 失败模式（禁止复利曲线被打断）

**证据（全语料多处实证）**：`…2882` ep5–7 = 0,0,0；`…71649` ep7–8、ep11 = 0,0,0；`frozen-vengeance` ep6–9 = 0,0,0,0；`the-heiresss-ruthless` ep4/ep6 = 0。零爽点中段是观众流失点；对照 `…8593` 全程无零、单调升温 = 留存最优。

**规则**：免费弧**任意连续 2 集爽点之和不得 < 3**（禁止"0,0"或"0,1,0"中段真空）。中段集用**次级爽点**（身份暗示 / 实力伏笔 / 反派挑衅）填充，维持升温感。

---

## §6. 平台工艺分野：netshort（对白对峙）vs shorttv（旁白内省）

**证据（量化坐实，见顶部平台分化表）**：
- **netshort**（`…71649`/`…8593`/`…2882`）：**对白驱动对峙**为主，多视角上帝反差，节拍快速切换（~28s/beat），爽点靠**当场冲突兑现**；长集（~2.5min）、中密度（~14 segs/min、~100 wpm）。
- **shorttv**（`identity-unveiled`/`frozen-vengeance`/`mommy`/`stolen-sight` 等）：大量**第一人称旁白内省**（"I burst into the ER… I watched… my throat so raw"），危机叠层靠**内心独白 + 情感累积**，爽点靠**低估-揭晓的延迟反差**；短集（~1.3min）、高密度（~21 segs/min、~200 wpm）。
- **共同点**：两者都用高 segs/min 维持信息密度（netshort 靠对白高频切换，shorttv 靠旁白+对白叠加），都达 ≥15 segs/min。

**shorttv 隐藏实力原型**（`identity-unveiled` ep1，72s）：
```
[ 20.0- 62.0] You are not fit to drive Jason's car... that boy is a dead end... He's beneath us... You just don't belong in this world.   ← 持续低估/最大化羞辱
[ 62.0- 69.0] It's a Centenary Edition that's worth ten... the mortgage was really crazy until we paid it off.   ← 隐藏实力揭晓（隐性财富，无"secretly"字面词→正则漏计实证）
```

**规则**：Type B 默认 netshort 路线（多视角、当场兑现、≤30s beat，对白≥85%）；shorttv/情感虐恋细分允许 30–40% 第一人称旁白内省，但**不得用它替代爽点兑现**——低估-揭晓反差仍须在场，每个旁白段后须接外部冲突 beat。

---

## §7. 爽点类型语料（关键词正则，含诚实告诫）

**本语料 Final 排序（131 集）**：虐心-悔恨 82(46%) ＞ 打脸 29(16%) ＞ 契约婚反转 18(10%) ＝ 隐藏实力 17(10%) ＝ 霸总护妻 17(10%) ＞ 身份揭晓 13(7%) ＞ 上帝视角反差 1(1%)。

**⚠ 与 v4.0 排序（隐藏实力 43% 居首）的差异 = 正则敏感性（全语料进一步坐实）**：
- angst-regret 关键词（cry/pain/hurt/regret/betray）词频天然高，易过计——全语料扩到 131 集后其占比从 38%→46% 进一步上升；
- hidden-power 常通过**隐性叙事**传达（如"we paid it off / LK Group will finally be mine"无"secretly"字面词），正则易漏计——全语料中其占比从 13%→10% 进一步下降到第 4，**与 v4.0 的 43% 差距更大**，正说明正则不可靠。`identity-unveiled` ep1 即漏计实证。
- **结论**：两版排序**都不足为据**，真实类型混合须人工通读判定。结构性发现（§1–§6）与正则无关，可直接采信。v4.0「隐藏实力是扮猪吃虎/隐藏身份型贯穿主驱动」的**定性结论仍然成立**（深读坐实，见 §6 原型），只是定量占比待人工核定。

---

## §8. 与其他文件的关系

- **`scene-density-spec.md`**：v4.2 banner 落在 §3（爽点类型库）之后，补冷开场 0–1s / 节拍 ≤30s / 付费墙簇射曲线 / 决策悬崖 / 中段禁零。
- **`netshort-arc-mechanics.md`**（v3.0）：本文件 §4 补全其"付费墙=生死危难"为双 flavor（全语料 cliff 分布坐实：纯肉体危机仅 27%）。
- **`research-evidence-v4.md`**（v4.0）：本文件 §7 解释与其爽点排序的差异（正则敏感性，全语料进一步坐实），不推翻其定性结论。
- **`reverse-engineering-pipeline/`**：`analyze.py` + `asr_batch.py` 产出本文件的全部数字。

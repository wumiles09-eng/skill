# Storyboard-Reverse — 视频 → 15s 分镜 → 剧本 反推工艺

> **v1.0。** 配套工具链：`reverse-engineering-pipeline/`（README + capture / asr_mlx_warm / analyze / dramas.yaml）。
> 验证基线：243《千金归来》EP01 全 5 shot 实测（见 `_pilot_243_qianjin/storyboard/ep01.md`）。
> 消费目标：**seedance 2.0 文生视频**（1 shot = 15s = 1 次生成）。

## 0. 何时用本工艺

- 拿到竞品视频 mp4，要反推其分镜与底层剧本（拆解学习 / 再创作）。
- 要为 seedance 2.0 批量生产 T2V prompt（每个 15s shot 一条 prompt）。
- 要从视频证据量化某剧的密度 / 爽点 / 卡点（喂 `overseas-cinematic-craft.md` 的密度 4 原型判定）。

**不要用于**：只有剧本、无视频时（直接走 SKILL.md 正向生成）；中文 netshort（其密度基线见 `scene-density-spec.md`，本工艺专为海外英文仿真人剧 + seedance 而设，但 schema 通用）。

## 1. 流水线（5 步）

```
mp4 ──▶ [1] ASR 转写（mlx-turbo 热池）
   │           │
   │           ▼   asr/{ep}.txt  （带时间码 [start-end] line）
   │
   ├──▶ [2] 每 15s 抽 1 代表帧（ffmpeg -vf fps=1/15）
   │           │
   │           ▼   frames/ep{NN}_{ss}s.jpg
   │
   └──▶ [3] 逐帧视觉分析（多模态：SCENE/CHARACTERS/BLOCKING/CAMERA/LIGHTING/ON-SCREEN TEXT/KEY ACTION/STYLE）
                 │
                 ▼   结构化字段
            [4] 合成 seedance-T2V 分镜板（本文 §2 schema）
                 │
                 ▼   storyboard/ep{NN}.md
            [5] 分镜 → 底层剧本反推（节拍 / 功能 / 爽点 / hook）
```

### [1] ASR — 命令
```bash
# 热池已建（7-27× realtime），冷启会拉 ~800MB 模型一次性
/tmp/mlx-asr-venv/bin/python reverse-engineering-pipeline/asr_mlx_warm.py \
  --batch manifest.txt --out-dir "$TR"
# 输出格式：=== MODEL=... DUR=156.0s ===  +  [start-end] line
# 注意：condition_on_previous_text=False + 循环幻觉截断（见 pipeline README）
```

### [2] 抽帧 — 每 15s 一帧
```bash
ffmpeg -i ep01.mp4 -vf "fps=1/15" -frames:v 5 frames/ep01_%03ds.jpg
# seedance 粒度 = 15s/shot，故每 15s 取 1 帧代表该 shot
# 末段不足 15s 取整（70s 剧 → 第 5 帧 060-070s 仍取 063s 代表）
```

### [3] 视觉分析 — 多模态路径与降级

| 优先级 | 路径 | 状态 |
|--------|------|------|
| 1st | `mcp__image-analyzer__analyze_image`（本地 path） | **当前宕机**（Connection error） |
| 2nd | `mcp__4_5v_mcp__analyze_image`（**CDN URL** 模式） | ✅ 可用（pilot 验证） |
| 3rd | 人工看帧 | 兜底 |

**降级到 4.5v 的 double-hop**：`Read(frame.jpg)` 返回 CDN URL → 把 URL 喂 `mcp__4_5v_mcp__analyze_image`。token 偏重，但对小批量可用。

**统一分析 prompt**（每帧填这 8 字段，事实性、简短）：
```
SCENE/LOCATION | CHARACTERS(age/gender/attire-color/posture/expression)
| BLOCKING | CAMERA(size+angle+motion) | LIGHTING/COLOR
| ON-SCREEN TEXT(verbatim or none) | KEY ACTION | PRODUCTION STYLE
```

## 2. seedance-T2V 分镜 schema（7 字段，已验证）

每个 15s shot 一行块：

| 字段 | 内容 | 来源 |
|------|------|------|
| **SEEDANCE-T2V-PROMPT** | 一条完整 text-to-video prompt（英文），含风格前缀 + 人物 + 动作 + 字幕 overlay + 镜头 | 视觉帧 + ASR |
| **VISUAL-EVIDENCE** | 帧时间戳 + 内容摘要（ground truth 锚点） | [3] 视觉分析 |
| **DIALOGUE(ASR)** | 该 shot 时段内的台词逐句（带说话人，若可推断） | asr/{ep}.txt |
| **FUNCTION** | 该 shot 的剧作功能（建立场景 / 升级冲突 / 蓄力 / hook 兑现） | 综合 |
| **爽点+EMOTION** | 爽点类型（8 类之一，或"无"）+ 情绪标签 | ASR + 视觉 |
| **DENSITY** | segs/min / words/min（从 ASR 时间码算） | ASR |
| **TRANSITION** | 与下一 shot 的衔接（硬切 / 特效 / 匹配剪辑） | 视觉 |

**风格前缀（overseas 仿真人剧默认，pilot 实测）**：
```
Cinematic photoreal, [golden-hour warm light / soft natural], [pastel pink/neutral tones],
no grain, static mid-shot eye-level. Subtitle overlay: "..."
```
（如检测到运动，把 static 换成对应镜头运动。）

## 3. ⚠️ 关键操作约束（pilot 付费学到的坑）

### 3.1 视觉角色连续性不可靠 — 必须三重锚定
4.5v 对**同一角色跨帧的服装色判断不一致**（243 实测：Ella 在 008/023/038s 判"白衬衫"，053s 判"粉裙黑西装"；Leah 反之）。**禁止仅凭服装色判角色身份**。连续性须三重锚定：
1. **ASR 说话人**（谁在说 → 该 shot 的焦点角色）
2. **屏幕名字卡**（`【字幕：身份-姓名】`，见 §3.2）
3. **画面位置 / blocking**（前景/后景/左/右）

三者冲突时以 ASR + 名字卡为准，服装色仅作弱参考。

**v4.5 升级（NG1 联动）**：服装色不可靠的根因是 image-gen 对"非生物特征"颜色漂移严重。反推/正向生成时，角色连续性应优先锚定**生物特征**——发色 + 瞳色（EN 双锚，如 `Platinum Blonde + Grey eyes`），比服装色稳定得多。视觉分析 prompt 的 CHARACTERS 字段须显式记录发色/瞳色（而非只记 attire-color）。

### 3.2 角色入场名字卡 = overseas 硬规范（两源互证）
- **源 1（视频）**：243 EP01 SHOT1 屏幕字幕 `Leo Ella`(金) / `THE SON OF LUKE MILLER`(白)。
- **源 2（本子）**：fuhun-ju EP1 `【字幕：华尔街风投合伙人-Isabella】`、`【字幕：Alexander情妇-Mia】`。

→ overseas 剧的人物首入**强制**配名字卡，且常**借卡埋伏笔**（243 用 "THE SON OF LUKE MILLER" 强调父系 → 血缘反转种子）。反推时若检测到名字卡，必须在 SEEDANCE-T2V-PROMPT 显式写 `Subtitle title-card overlay: "Name" / "ROLE"`，并在 FUNCTION 标注其伏笔意图。

### 3.3 台词钩子 ≠ 视觉爽点
243 EP01 hook 纯靠一句台词（Leah: "That's what real love looks like"）制造信息差，**整集零视觉爽点**。反推时遇到"零爽点 shot 但有强信息差台词"，归为**台词重定义型信息差**（`overseas-cinematic-craft.md` §9 元引擎的子类），不要硬标爽点类型。

### 3.4 慢热 EP01 不必打脸开场（v4.5：先读 spec 期待值定原型）
243 EP01 全程憋屈蓄势，hook 在末句。这归 `overseas-cinematic-craft.md` §3 密度原型 B（平坦高位）的极端态。反推时不要因为"EP01 没爽点"就判失败——先定原型再判密度。

**v4.5 G7 升级**：定原型前**先读 spec 层"期待值"用词**。243 同家族 spec《千金归来不好惹》写"期待值：情绪逐步推进"→ 直接预测了 EP01 慢热零爽点（忠实于 spec，非偏差）。反推流程：① 读 spec 期待值 → ② 映射密度原型（见 overseas §3 期待映射表）→ ③ 再判逐集密度是否符形态。spec 若无期待值字段（如 sterling），从题材反推并在 Series Bible 补。

### 3.5 ASR 说话人标签缺失时的处理
mlx-turbo 输出**不带说话人**。推断规则（优先级）：
1. 名字卡出现 → 该 shot 焦点角色优先发言。
2. 台词含自称/称谓（"honey"/"sweetheart" → 母亲/情人；姓氏 → 下属）。
3. 上下文承接（上一 shot 已出场的角色延续）。
4. 无法判定时标 `角色(?)`，不臆断。

## 4. 成本模型 + 采样策略

| 单位 | 实测成本 |
|------|---------|
| 1 集 ASR（~70-90s 音） | < 5s（热池） |
| 1 集抽帧（5 帧） | 秒级 |
| 1 帧视觉分析（4.5v CDN） | ~5-10s + ~200 token |
| **1 集（5 shot）端到端** | ~3-5 min + ~1.5k token |

**外推**（1 shot = 15s，1 集 ≈ 5 shot）：
- 1 剧 15 集 ≈ 75 shot ≈ 45-75 min + ~25k token
- 8 剧全量 ≈ 600 shot ≈ 6-10 h + ~200k token

**采样推荐**（性价比最高）：每剧只反推 **EP01 + 付费墙集（2-3 集）**，覆盖冷开场工艺 + 卡点工艺两大信号源，成本降到 1/5。

**v4.5 P1c 工艺结论（ASR 为主、视觉定点为辅）**：243 全 15 集反推实测——当 ASR 质量高（mlx-turbo 海外英文对白 segs/words 密度可信）时，剧级反推应**以 ASR 为主还原剧作骨架，视觉只做关键帧定点**（反转/hook/新角帧，每剧 5-8 帧即可），不必逐帧视觉。243 实测：15 集 ASR 通读 + 6 关键帧视觉定点（非 70 帧全分析）即还原完整三幕骨架 + 密度原型 D 判定 + 付费墙双钩，成本远低于逐帧预估（见 `_pilot_243_qianjin/SERIES-REVERSE.md`）。

## 5. 从分镜反推底层剧本（步骤 [5]）

拿到全部分镜板后，聚合出：
1. **剧级元数据**：类型 / 核心人物 / 隐藏身份伏笔 / 视觉风格 token（见 ep01.md 顶部表）。
2. **主线节拍**：每集用 1 句话（功能 + 爽点 + hook 落点）。
3. **爽点曲线**：标到 `overseas-cinematic-craft.md` §3 的 4 原型上，定该剧属哪型。
4. **卡点位置**：付费墙落在哪个 shot、属"生死危难"还是"决策宣告"flavor。
5. **可复用元素**：名字卡设计 / 信物 / 声口 / 冷开场模式 → 回流到 SKILL.md 的 craft 库。

## 6. 自检清单（每集反推完过一遍）

- [ ] 每个 shot 的 SEEDANCE-T2V-PROMPT 可独立喂生成模型（含风格 + 人物 + 动作 + 字幕）
- [ ] DIALOGUE 与 ASR 时间码对齐（shot 时段内的台词全收入，不串集）
- [ ] 角色身份三重锚定（无"仅凭服装色"判断）
- [ ] 名字卡 shot 已在 prompt 写明 subtitle overlay
- [ ] 零爽点 shot 已核对是否为"台词重定义型信息差"
- [ ] 密度判定前已先定 4 原型之一
- [ ] 说话人不确定处标 `角色(?)` 而非臆断

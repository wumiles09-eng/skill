# Research Evidence — v4.0：mlx-turbo 重转写 + 流水线 skill化 + 机制纠错

> **本文是 v3.0 `research-evidence.md` 的增量证据层。** v3.0 的定性结构结论（netshort 全弧工艺、付费墙 = 生死危难、梯次揭晓、阶级羞辱词库等）全部仍然成立，**不重复**——本文只记录 v4.0 相对 v3.0 的**三处实质变化**：
>
> 1. **机制纠错**：v3.0 §1 工具链对两个平台的获取机制有**两处事实错误**，v4.0 用真实抓取证伪并改正。
> 2. **ASR 升级**：`faster-whisper small.en`（244M）→ **`mlx large-v3-turbo`（809M）+ 循环幻觉截断**。密度数字因此**整体刷新且更可信**（turbo 边界检测更准、幻觉被截断）。
> 3. **流水线 skill化**：把"获取→ASR→分析→反推"固化成可复用流水线（`reverse-engineering-pipeline/`），以后加剧/换平台不用重新探索机制。
>
> **v4.0 语料**：13 剧 / 44 集 = netshort 3 全弧（bankrupt/macoe/wolfless）+ netshort 9 ep1 横截面 + shorttv mommy 全 6 集。**全部用 mlx-turbo 重转写**。
>
> **诚实边界**：Obsidian 清单共 **39 剧**，当前语料覆盖 **13/39（33%）**；剩余 **26 剧**（13 netshort + 13 shorttv）因抓取期两平台视频 CDN 对当前 IP 联动软封，待 IP 冷却后用 `reverse-engineering-pipeline/batch_shorttv.sh` + `capture_netshort.py` 续抓（可复用、可续跑）。

---

## §1. 机制纠错（v3.0 §1 工具链两处事实错误）

v3.0 §1 写的是早期推测，v4.0 真实抓取后证伪：

| 平台 | v3.0 §1 的说法（**错误**） | v4.0 实测（**正确**） | 证据 |
|------|----------------------------|------------------------|------|
| **netshort** | `og:video` meta 标签暴露直链 mp4 → curl 下载 | **Aliyun WAF 拦所有非浏览器 HTTP**（curl/python/node 一律 `ERR_CONNECTION_CLOSED`）；mp4 走 cfcdn，URL 在 `<video>.currentSrc`，**`auth_key` 分钟级过期**，读到 src 必须同 session 立即下载 | 多次直连失败；browser-harness CDP 通过；存 URL 留待后下 = 0 字节 |
| **shorttv** | 自定义 AES-CBC 加密 HLS（IV=`shortmax00000000`，per-segment key） | **明文 .ts，无任何 DRM**。"hls-encrypted" 只是**路径名唬人**；m3u8+ts 可直接 curl/ffmpeg | segment 是标准 AAC-in-TS；`ffmpeg -c copy -bsf:a aac_adtstoasc` 直出可播 mp4，无需解密 |

**附带纠错**：shorttv 的 32-hex 视频 hash **不在静态 HTML 里**（Nuxt3 SPA，静态 curl 无 m3u8），只在页面 hydrate 后进 DOM → 必须用 browser-harness 渲染后从 DOM 收割 hash。v3.0 §1 假设"静态可拿"也是错的。

> 这两条纠错的意义不在写作工艺，而在**降低未来探索成本**——下游脚本不再走错路（不要再去破 shorttv 的"加密"，不要再用 curl 直连 netshort）。

---

## §2. ASR 升级：small.en → mlx large-v3-turbo

### 为什么换
v3.0 用 `faster-whisper small.en`（244M，CPU int8）转写，对密集对白有**两个已知问题**：
1. 边界检测粗，密集段会被合并 → segs/min 偏低。
2. 音频末尾/静音处会**循环幻觉**（一个 token 死循环重复数百次，如 "of you of you…"），撑爆词数。

v4.0 换 **`mlx-community/whisper-large-v3-turbo`**（809M，Apple Silicon GPU）：

| 模型 | 实时倍率 | 词数(209s 样本) | 结论 |
|------|---------|----------------|------|
| faster-whisper small.en（v3.0） | ~1× | — | ❌ 慢 + 边界粗 + 幻觉 |
| mlx large-v3-turbo 冷启动 | 1.2× | 403 | ❌ 含模型加载+Metal 编译税 |
| mlx distil-large-v3 | 1.5× | 400 | ❌ mlx 上反而更慢 |
| **mlx large-v3-turbo 热池** | **6.9–27×** | 456 | **✅ 采用** |

热池 = 启动加载一次、整批复用，只有第一个文件付冷启动税。整库 ~14h 音频 → **~1–2h 转写**（v3.0 small.en 要跑通宵）。

### 两个必做的后处理（`asr_mlx_warm.py` 内置）
1. **`dedupe_loop()`**：检测 n-gram（plen 1-5）从开头连续重复 ≥4 次即截断、保留前 2 次 + `[loop-truncated]`。
2. **空段过滤 + `condition_on_previous_text=False`**：消静音碎片、抑上下文传染式幻觉。

**修前/修后实证**（shorttv mommy ep03）：390 词/345w/m（幻觉）→ **170 词/150w/m（干净）**；71 段碎片 → 20 段。

### 密度数字整体刷新（v4.0 超越 v3.0）
因为 turbo 边界更准 + 幻觉被截断，**同一段视频的 s/m、w/m 与 v3.0 不完全一致，v4.0 更可信**。例：

| 剧·集 | v3.0 small.en | v4.0 turbo | 说明 |
|-------|---------------|------------|------|
| bankrupt ep5 | 13.0 s/m / 159 w/m | **20.9 s/m / 159 w/m** | w/m 接近（词数稳），s/m 涨（turbo 拆出更多边界）|
| mommy ep3 | 8.0 s/m / 117 w/m（含幻觉尾巴）| 15.9 s/m / 150 w/m | 幻觉截断后段数重整 |

**结论**：凡引用密度数字，以**本文 §3 / `research-evidence-v4.json`** 为准；v3.0 `research-evidence.md` §3 的表格保留作历史记录，不再作为基线源。

---

## §3. v4.0 量化语料（44 集，mlx-turbo 转写）

> 原始机器生成表（13 行 + 全语料聚合）见同目录 `research-evidence-v4.json`；本节为人工整理版（剧名替 ID + 曲线 + 结论）。

### 全弧剧密度（4 剧 / 35 集）—— v4.0 核心数据

| 剧 | 平台 | 流派 | 集 | 均dur | s/m | w/m | 付费墙 | 主爽点引擎 |
|----|------|------|----|-------|-----|-----|--------|-----------|
| **bankrupt** | netshort | 复仇打脸（隐藏实力）| 8 | 137s | **15.8** | **123** | mortal-peril | **打脸=9** / 隐藏实力=7 / 身份揭晓=6 |
| **married-a-ceo** | netshort | 复仇契约婚（隐藏身份）| 12 | 162s | 14.2 | 97 | **truth-reveal** | 隐藏实力=11 |
| **wolfless-carpenter** | netshort | 环境玄幻 | 9 | 167s | 11.3 | 74 | mortal-peril | 隐藏实力=5 |
| **mommy** | shorttv | 情感悬疑（家庭谎言）| 6 | **69s** | **16.0** | 109 | mortal-peril | **虐心=6** |

> mommy 全弧是 v4.0 **首次拿到的 shorttv 全弧 turbo 转写**（v3.0 mommy 是 small.en）。集长 57-85s 证实 shorttv"短集高密"分层独立于 netshort 的 90-210s。

#### 跨剧密度曲线（segs/min，逐集）

```
bankrupt       ep1:14.6 ep2:13.5 ep3:16.2 ep4:18.9 ep5:20.9 ep6:13.3 ep7:13.9 ep8:14.8
married-a-ceo  ep1:14.1 ep2:7.9  ep3:14.3 ep4:15.6 ep5:13.5 ep6:16.1 ep7:15.8 ep8:10.6 ep9:17.4 ep10:16.9 ep11:13.1 ep12:15.1
wolfless       ep1:7.8  ep2:18.1 ep3:9.7  ep4:13.6 ep5:13.0 ep6:10.5 ep7:9.4  ep8:8.4  ep9:11.2
mommy          ep1:16.8 ep2:14.7 ep3:15.9 ep4:16.6 ep5:16.2 ep6:15.5
```

**跨剧规律（turbo 数据强化 v3.0 结论）**：
- **bankrupt 密度峰在 ep5（20.9）= 最大真相曝光集**（v3.0 命中的"先甜"点，turbo 把峰测得更尖）。
- **macoe 在 ep7-8 有刻意谷（15.8/10.6）**——虐心沉淀集，v3.0 §4 的"虐心密度谷"用更准数据复现。
- **wolfless ep1 = 7.8（奇观慢热，前 81s 无对白），ep2 立即 18.1 揭晓峰补偿**——v3.0 §1/§4 的 C 档模式 turbo 复现。
- **mommy 全程高位平稳（14.7-16.8）**——情感悬疑型靠"持续中高密"而非"尖峰+深谷"，与复仇打脸型的 K 线形态**本质不同**。

### netshort 9 剧 ep1 横截面（turbo 重转写）

| codename | dur | s/m | w/m | 首白 | 流派（ep1 反推） | 主爽点 |
|----------|-----|-----|-----|------|------------------|--------|
| apollo | 260s | 12.5 | 81 | 0s | 神话重生 + 姐妹背叛 | — |
| suger-mommys | 301s | 14.8 | 98 | 0s | 现代背叛 + 复仇 | 隐藏实力=3 |
| lord-dragons | 218s | 7.7 | 50 | 0s | 玄幻龙族（驯龙） | — |
| ceos-forbidden-nanny | 149s | 16.1 | 87 | 0s | 霸总契约婚 + 萌宝认父 | — |
| doting-snake-lord | 232s | 14.5 | **128** | 0s | 玄幻重生 + 血脉羞辱 | — |
| mrs-hart | 287s | 14.2 | **139** | 0s | 现代虐心-悔恨 + 觉醒离婚 | 隐藏实力=1 / 虐心=1 |
| supreme-wastrel | 175s | 7.9 | 65 | 0s | 玄幻扮猪吃虎 | — |
| false-weakling | 286s | 13.2 | 73 | 0s | 玄幻竞技（斗兽场） | 打脸=1 |
| his-lost-lycan-luna | 299s | 11.2 | 71 | 0s | 狼人寻妻复仇 | — |

> 9 剧 ep1 dur 均值 **245s**（> 全弧均值 137-167s），再次坐实 v3.0 §1"**首集明显偏长吸冷启动**"。v3.0 这些是 small.en 转写，v4.0 全部用 turbo 重转。

### 全语料爽点引擎总量（44 集合并计次）

| 排名 | 爽点引擎 | 命中数 | 占比 |
|------|---------|--------|------|
| **1** | **隐藏实力被低估** | **28** | **43%** |
| 2 | 虐心-悔恨 | 12 | 18% |
| 3 | 打脸 | 11 | 17% |
| 4 | 身份揭晓 | 6 | 9% |
| 5 | 霸总护妻 | 2 | 3% |
| 6 | 契约婚反转 | 2 | 3% |
| 7 | 上帝视角反差 | 1 | 2% |

**这是 v4.0 最重要的量化结论（写作工艺直接可操作）**：
1. **"隐藏实力被低估"是跨语料第一大引擎（43%）**——远超直觉上以为的"打脸"。任何"扮猪吃虎/被看不起/底牌藏身份"型剧，必须把"被低估→底牌"做成**贯穿全弧的主驱动**，而非点缀。
2. **引擎按流派分化**：
   - 复仇打脸型（bankrupt）= 打脸(9) + 隐藏实力(7) + 身份揭晓(6) **三引擎堆叠**（所以密度最高 15.8 s/m）。
   - 隐藏身份型（macoe/wolfless）= 隐藏实力单引擎主导。
   - 情感悬疑型（mommy）= **虐心(6) 主导，打脸≈0**——shorttv 家庭谎言剧根本不打脸，靠虐心驱动。引擎选择与平台流派强绑定。
3. `scene-density-spec.md` §3 的 7 类引擎优先级，**应以这张量化表重排**：隐藏实力 > 虐心 ≈ 打脸 > 身份揭晓 > 其余。

### 付费墙落点分布（13 剧末集文本分类）

| 分类 | 剧数 | 剧 |
|------|------|----|
| mortal-peril（生死危难）| 8 | bankrupt / wolfless / mommy + 5 ep1 |
| truth-reveal（真相揭穿）| 1 | **married-a-ceo** |
| ambiguous | 4 | 其余 ep1（文本不足判定）|

**关键 nuance**：married-a-ceo 是**唯一被判 truth-reveal 的 netshort 剧**——它虽属 netshort，但末集（ep12）同时含身份揭晓（"He is Ms. Leech's husband"）与持枪生死威胁（"I'll blow your fucking hand off"），ASR 文本里真相词略多于危难词。这不推翻 `netshort-arc-mechanics.md` §2（付费墙=危难），而是说明：**当一集同时堆叠真相+危难时，cliffhanger 落点仍应是危难**（枪），写作时不要被文本计数误导把卡点放在揭晓上。

---

## §4. 流水线 skill化（v4.0 新增，对应"不用每次探索"）

完整流水线固化在 `../reverse-engineering-pipeline/`，详见该目录 `README.md`。要点：

| 产物 | 作用 |
|------|------|
| `README.md` | 机制总览 + 完整工作流 + 已知运维约束（skill化的核心文档）|
| `dramas.yaml` | 规范 39 剧清单（25 netshort + 14 shorttv，含 id/slug/codename）|
| `asr_mlx_warm.py` | mlx-turbo 热池 ASR + 循环幻觉截断 |
| `capture_shorttv.py` | shorttv 抓取（browser-harness 收 DOM hash → 去重分辨率 → curl/ffmpeg）|
| `capture_netshort.py` | netshort 抓取（browser-harness 破 WAF → 同 session 立即下 cfcdn mp4）|
| `batch_shorttv.sh` | shorttv 顺序批量（可续跑，≥3 集跳过）|
| `analyze.py` | 密度/爽点/付费墙/阶级羞辱词提炼（生成本文 §3 数据 + `.json`）|

**新增一剧/换平台的标准流程**：抓取（capture_*.py）→ ASR（asr_mlx_warm.py）→ 分析（analyze.py）→ 结论回写本文 + `scene-density-spec.md` + `netshort-arc-mechanics.md`。机制部分**不再需要重新探索**。

---

## §5. 局限与下一步

1. **覆盖 13/39（33%）**：剩余 26 剧（13 netshort + 13 shorttv）待 IP 冷却后续抓。两平台视频 CDN 在突发抓取后联动软封当前 IP（详见 `drama-cdn-ip-softban` 记忆 + pipeline README「已知运维约束」）。续抓命令已就绪、可复用：
   - shorttv：`bash reverse-engineering-pipeline/batch_shorttv.sh`
   - netshort：逐剧 `NS_URL=… NS_ID=… OUT_DIR=… browser-harness < capture_netshort.py`
2. **ASR 仍有盲区**：turbo 对**极快连读段 + 重背景音**偶有漏字；纯动作/画面段（无对白）的视觉信息仍需人工补（Type A 旁白剧影响大，Type B 对白剧影响小）。
3. **爽点词库是启发式初筛**：英文 ASR 关键词正则用于跨剧横向对比与导引人工精读，**不能替代逐句人工判定**；最终工艺结论须回原始转写复核。
4. **netshort 11 剧仍仅 ep1**：流派已被 3 全弧剧覆盖，但 mafia/workplace/second-chance 等流派样本偏少，后续补全弧。

---

## §6. 复现（v4.0）

```bash
PIPE="/Users/mac/Documents/project/专项skill/剧本创作skill/reverse-engineering-pipeline"
TR="/tmp/drama-re/tr"

# 抓取（见 README；当前 IP 软封，26 剧待冷却）
# ASR（热池批量）
ls /tmp/drama-re/{ns,stv}/*.mp4 > /tmp/all.manifest
/tmp/mlx-asr-venv/bin/python "$PIPE/asr_mlx_warm.py" --batch /tmp/all.manifest --out-dir "$TR"
# 分析（生成本文 §3 表 + research-evidence-v4.json）
python3 "$PIPE/analyze.py" "$TR" --out "$PIPE/../references/research-evidence-v4.md"
```

转写产物：`/tmp/drama-re/tr/*.txt`（44 集，mlx-turbo）。

---

## §7. 与其他文件的关系

- **`research-evidence.md`（v3.0）**：定性结构证据（netshort 全弧工艺、阶级词库、梯次揭晓等）仍然成立，本文不重复，只做机制纠错 + ASR 升级 + 数据刷新。
- **`netshort-arc-mechanics.md`**：整弧结构工艺——v4.0 数据强化其结论（密度峰/谷、付费墙=危难）。
- **`scene-density-spec.md`**：单集密度基线 + 7 类爽点引擎——**v4.0 §3 量化表应回写该文件的引擎优先级**。
- **`../reverse-engineering-pipeline/README.md`**：本文 §1 机制纠错 + §4 流水线的完整版。

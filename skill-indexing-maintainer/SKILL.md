---
name: skill-indexing-maintainer
description: 维护skill智能索引（补充典型问题/更新能力摘要/拆分子能力/检测覆盖度）。任务结束复盘、发现触发不准、创建新技能时使用。
---

# Skill Indexing Maintainer - 技能索引维护器

## 目标

让skills的索引变聪明，使用"智能索引"策略提升skill触发准确率。

## 智能索引策略

### 核心思想

> **索引 ≠ 检索**
> 索引是为"被找到"而设计的结构；检索只是用查询去触发这个结构。

### 4层混合索引

```
用户查询
    ↓
并行匹配:
  ├─ 查询索引 (typicalQueries)
  ├─ 摘要索引 (summaryIndex)
  └─ 子块索引 (subCapabilities)
    ↓
最佳匹配
    ↓
返回: 完整 SKILL.md + references
```

## 何时使用本技能？

1. **任务结束复盘时**: 把"用户实际说法"加入索引
2. **发现触发不准时**: 补充 typicalQueries 或调整 summaryIndex
3. **创建新 skill 时**: 同步在 SKILLS_REGISTRY.json 注册
4. **定期审计时**: 检查索引覆盖度，发现缺口

## 操作类型

### 1. 补充典型问题（查询索引维护）

**触发信号**: 用户说了某句话，但没触发对应 skill

**操作步骤**:
1. 读取 `_meta/SKILLS_REGISTRY.json`
2. 找到对应 skill
3. 在 `queryIndex.typicalQueries` 数组添加新问法
4. 写回文件

**示例**:
```json
// 用户说"目标不明确"但没触发 requirements-clarifier
// → 补充到 typicalQueries

{
  "id": "requirements-clarifier",
  "queryIndex": {
    "typicalQueries": [
      "需求不清晰怎么办",
      "目标不明确"  // ← 新增
    ]
  }
}
```

### 2. 更新能力摘要（摘要索引维护）

**触发信号**: skill 能力变更、说明不准确

**操作步骤**:
1. 读取 SKILL.md 确认最新能力
2. 更新 `summaryIndex` 字段：
   - `capability`（核心能力）
   - `input`（输入）
   - `output`（输出）
   - `keyPhrases`（关键短语）

### 3. 拆分子能力（子块索引维护）

**触发信号**:
- SKILL.md 超过 300 行
- 包含多个独立能力点
- 用户常常只需要其中一部分

**操作步骤**:
1. 识别可独立的能力点
2. 为每个能力点定义：
   - `id`（唯一标识）
   - `name`（能力名称）
   - `description`（做什么）
   - `triggers`（典型触发词）
3. 添加到 `subCapabilities` 数组
4. **注意**: 不动原 SKILL.md

**示例**:
```json
{
  "id": "optimize-iteration-spec",
  "subCapabilities": [
    {
      "id": "optimize-iteration-spec__scoring",
      "name": "迭代文档评分",
      "description": "按四层结构给需求文档打分",
      "triggers": ["检查文档质量", "评估完整性"]
    }
  ]
}
```

### 4. 注册新 skill

**触发信号**: 创建了新 SKILL.md

**操作步骤**:
1. 在 `SKILLS_REGISTRY.json` 添加新条目
2. 必填字段：
   - `id` / `name` / `path` / `type` / `layer`
3. 必填索引：
   - `queryIndex.typicalQueries`（至少 3-5 个）
   - `summaryIndex`（capability/input/output/keyPhrases）
4. 可选：
   - `subCapabilities`
   - `antiPatterns`
   - `dependencies`
   - `originRepo`

### 5. 索引覆盖度审计

**触发信号**: 定期检查（建议每月一次）

**检查项**:
- [ ] 所有 skills 都在 SKILLS_REGISTRY.json 注册了吗？
- [ ] 每个 skill 的 `typicalQueries` 至少有 3 个吗？
- [ ] 是否有用户常问的问题没有对应 skill？
- [ ] 长 skills（>300行）是否拆分了 subCapabilities？

**输出**:
- 缺失项清单
- 建议补充的 typicalQueries
- 建议拆分的 skills

## 维护频率建议

| 时机 | 动作 | 预计时间 |
|------|------|---------|
| 每次任务后 | 补充 1-2 个 typicalQueries | 1 分钟 |
| 创建新 skill | 注册到 SKILLS_REGISTRY.json | 3 分钟 |
| 每周一次 | 审计触发不准的 skills | 5 分钟 |
| 每月一次 | 完整覆盖度审计 + 清理冗余 | 15 分钟 |

## 输出格式

维护后输出：

```markdown
## 索引维护完成

### 本次更新
- ✅ 为 `xxx` skill 补充了 2 个 typicalQueries
- ✅ 更新了 `yyy` skill 的 summaryIndex
- ✅ 注册了新 skill `zzz`

### 索引统计
- 总 skills 数：40
- 有 queryIndex 的：40
- 有 subCapabilities 的：5
- 平均 typicalQueries 数：4.2

### 建议
- ⚠️ `aaa` skill 超过 300 行，建议拆分 subCapabilities
- ⚠️ `bbb` skill 只有 1 个 typicalQuery，建议补充
```

## 索引质量标准

### 优秀索引

```markdown
### 查询索引
- 典型问题 ≥5 个
- 覆盖多种表达方式
- 包含反模式

### 摘要索引
- capability 清晰准确
- input/output 明确
- keyPhrases 提取精准

### 子块索引
- 长 skill 已拆分
- 每个 sub-capability 有独立触发词
```

## 与其他技能的配合

- **在 `skill-lifecycle-and-evolution` 的复盘阶段**: 自动调用本技能更新索引
- **在 `workflow-orchestrator` 触发不准时**: 用本技能补充 typicalQueries
- **创建新 skill 时**: 用本技能同步注册索引

## 参考

- 4层智能索引策略：基于RAG最佳实践
- 注册表文件：`_meta/SKILLS_REGISTRY.json`
- 进化追踪：配合 evolution.json 使用

---

**维护**: 根据索引使用效果持续优化
**来源**: Cursor Hi Offer skill-indexing-maintainer
**相关**: skill-lifecycle-and-evolution, skill-creator

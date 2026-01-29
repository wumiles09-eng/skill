---
name: skill-lifecycle-and-evolution
description: 技能生命周期管理与演进（清单/更新/演进/闭环改进）。维护技能清单、记录触发失败、沉淀最佳实践、更新evolution.json。任务结束复盘、技能优化时使用。
---

# Skill Lifecycle and Evolution - 技能生命周期与演进

## 目标

建立技能的闭环改进机制，让技能系统随着使用不断进化。

## 技能生命周期

### 1. 创建阶段

```markdown
## Skill创建流程

### 需求识别
- [ ] 识别重复任务模式
- [ ] 发现技能缺口
- [ ] 评估技能价值

### 创建步骤
1. 使用 skill-creator 创建技能骨架
2. 编写 SKILL.md 核心内容
3. 在 SKILLS_REGISTRY.json 注册
4. 添加典型触发问题
5. 测试技能触发

### 创建检查清单
- [ ] skill名称唯一
- [ ] 描述清晰准确
- [ ] 至少3个typicalQueries
- [ ] 与现有技能无重叠
- [ ] 已在registry中注册
```

### 2. 使用阶段

```markdown
## Skill使用监控

### 正常使用
- 技能正确触发
- 内容满足需求
- 输出格式正确

### 异常情况
- ❌ 技能未触发（触发失败）
- ❌ 触发错误的技能
- ❌ 内容不满足需求
- ❌ 输出格式错误

### 记录格式
```json
{
  "timestamp": "2026-01-29T10:00:00Z",
  "userQuery": "用户原始问题",
  "expectedSkill": "应该触发的技能",
  "actualSkill": "实际触发的技能",
  "issue": "问题描述",
  "resolution": "解决方案"
}
```
```

### 3. 优化阶段

```markdown
## Skill优化类型

### 触发优化
- 补充 typicalQueries
- 调整 description
- 添加 antiPatterns

### 内容优化
- 更新技能内容
- 添加新功能
- 修复错误

### 性能优化
- 减少 token 使用
- 优化输出格式
- 简化流程
```

### 4. 废弃阶段

```markdown
## Skill废弃条件

- [ ] 功能被其他技能完全覆盖
- [ ] 长期未被使用（>6个月）
- [ ] 技术栈已过时
- [ ] 维护成本大于价值

### 废弃流程
1. 在registry中标记deprecated
2. 添加替代技能说明
3. 保留一个版本周期
4. 最后删除
```

## Evolution追踪

### evolution.json结构

```json
{
  "version": "1.0.0",
  "lastUpdated": "2026-01-29",
  "statistics": {
    "totalSkills": 40,
    "activeSkills": 38,
    "deprecatedSkills": 2
  },
  "triggerFixes": [
    {
      "skillId": "requirements-clarifier",
      "date": "2026-01-29",
      "originalQuery": "目标不明确",
      "fix": "添加到typicalQueries",
      "result": "触发成功"
    }
  ],
  "workflowFixes": [
    {
      "skillId": "workflow-orchestrator",
      "date": "2026-01-29",
      "issue": "阶段判定不准确",
      "fix": "增加决策树",
      "result": "准确率提升"
    }
  ],
  "templateAdditions": [
    {
      "skillId": "tech-proposal",
      "date": "2026-01-29",
      "template": "A/B方案对比表格",
      "reason": "用户反馈缺少对比格式"
    }
  ],
  "antiPatterns": [
    {
      "pattern": "在单个技能中实现过多功能",
      "consequence": "难以维护、触发不准确",
      "solution": "拆分为多个子技能"
    }
  ]
}
```

### 记录时机

```markdown
## 何时更新evolution.json

### 触发修复（trigger_fixes）
- 用户问题未触发技能
- 触发了错误的技能
- 触发了多个技能

### 工作流修复（workflow_fixes）
- 流程步骤遗漏
- 步骤顺序错误
- 输出格式不匹配

### 模板补充（template_additions）
- 发现常用模式
- 用户请求模板
- 提高输出一致性

### 反模式记录（anti_patterns）
- 重复出现的错误
- 低效模式
- 维护陷阱
```

## 复盘流程

### 任务结束复盘

```markdown
## 任务复盘模板

### 任务信息
- 任务名称: {名称}
- 完成时间: {日期}
- 使用的技能: {列表}

### 技能使用情况
| 技能 | 触发是否准确 | 内容是否满足 | 改进建议 |
|------|-------------|-------------|---------|
| skill1 | ✅/❌ | ✅/❌ | {建议} |

### 发现的问题
1. **触发失败**: {描述}
   - 用户问题: "{原话}"
   - 期望技能: {技能名}
   - 实际触发: {技能名或无}
   - 解决方案: {方案}

2. **内容不足**: {描述}
   - 缺失内容: {描述}
   - 补充方案: {方案}

### 改进行动
- [ ] 更新typicalQueries
- [ ] 补充技能内容
- [ ] 优化流程
- [ ] 记录到evolution.json
```

### 月度技能审计

```markdown
## 月度技能审计

### 审计项目
- [ ] 所有技能都在registry中注册
- [ ] 每个技能至少有3个typicalQueries
- [ ] 废弃技能已标记
- [ ] evolution.json已更新

### 统计分析
- 最常使用的5个技能
- 最少使用的5个技能
- 触发失败最多的3个技能
- 新增技能数量

### 优化计划
- [ ] 需要优化的技能列表
- [ ] 需要废弃的技能列表
- [ ] 需要创建的技能列表
```

## 闭环改进机制

```
用户使用
    ↓
记录问题
    ↓
分析根因
    ↓
实施改进
    ↓
验证效果
    ↓
更新evolution.json
    ↓
回到使用
```

## 技能质量标准

### 触发质量

```markdown
## 触发准确性指标

### 优秀 (≥90%)
- 绝大多数情况下正确触发
- typicalQueries覆盖全面
- antiPatterns清晰

### 良好 (70-89%)
- 大部分情况下正确触发
- 偶尔需要手动指定

### 需改进 (<70%)
- 经常触发失败
- 需要大量补充typicalQueries
```

### 内容质量

```markdown
## 内容完整性指标

### 优秀
- 结构清晰完整
- 有具体示例
- 有最佳实践
- 有检查清单

### 良好
- 结构基本完整
- 有部分示例
- 流程清晰

### 需改进
- 结构不完整
- 缺少示例
- 流程模糊
```

## 与其他技能的集成

### 配合技能
- `skill-indexing-maintainer` - 索引维护
- `workflow-orchestrator` - 工作流复盘
- `planning-with-files` - 持续改进记录

### 触发条件
- 任务结束复盘时
- 发现技能问题时
- 月度审计时

## 最佳实践

### 1. 持续改进
- 每次任务后记录
- 每周review evolution.json
- 每月全面审计

### 2. 数据驱动
- 记录真实使用情况
- 基于数据优化
- 验证优化效果

### 3. 社区贡献
- 分享改进经验
- 贡献最佳实践
- 参与技能review

---

**维护**: 根据技能使用经验持续优化
**来源**: Cursor Hi Offer skill-lifecycle-and-evolution
**相关**: skill-indexing-maintainer, skill-creator

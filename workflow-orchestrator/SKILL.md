---
name: workflow-orchestrator
description: 端到端工程流程编排与导航（想法→需求→设计→技术方案→开发→测试→部署→复盘→推广→知识管理→迭代→skill优化）。当用户提出较大的"要做什么/怎么做/怎么上线"请求，或任务跨多个阶段时使用；负责选择下一步、产出关键文档、串联其他技能并维护持久化文件。
---

# Workflow Orchestrator - 工程流程编排器

## 目标

把用户请求定位到当前阶段，生成/更新该阶段的产物文件，将工作拆成可执行的小任务，并在需要时切换到对应专项 skill。

## 完整研发流程

```
想法 → 需求 → 设计 → 技术方案 → 开发 → 测试 → 部署 → 推广 → 知识管理 → 迭代 → Skill优化
  ↓      ↓      ↓        ↓         ↓       ↓       ↓       ↓          ↓          ↓          ↓
Idea   PRD   Design  TechPlan   Code    Test    Deploy  Promo   Knowledge  Iterate  Evolution
```

## 阶段判定（快速分流）

用下面的信号判断你处于哪一步：

- **想法**: 用户有模糊想法，需要产品化
- **需求**: 目标/范围/约束/验收不清晰
- **设计**: 用户在谈"怎么交互/怎么组织信息/数据怎么流动"
- **技术方案**: 用户在谈"怎么拆任务/怎么实现/技术选型"
- **开发**: 已明确方案，开始改代码/写代码
- **测试**: 编写/运行/补齐测试，定位失败
- **部署**: 打包/发布/上线/迁移/回滚
- **推广**: 市场推广/用户增长/运营策略
- **知识管理**: 文档沉淀/知识库/最佳实践
- **迭代**: 功能迭代/优化/重构
- **Skill优化**: 反馈流程问题/优化技能/创建新技能

## 阶段产物（默认落到工作目录）

### 想法 → 需求
- **产物**: `prd.md` (产品需求文档)
- **触发**: requirements-clarifier, prd-generator
- **内容**: 目标用户、核心价值、功能清单、验收标准

### 设计
- **产物**: `design.md` + `adr/` (架构决策记录)
- **触发**: architecture-designer, ui-ux-design-system-generator
- **内容**: 信息架构、交互流程、数据流、技术边界

### 技术方案
- **产物**: `tech-plan.md` + `test-plan.md`
- **触发**: tech-proposal, implementation-plan-writer
- **内容**: A/B方案对比、成本/时间/风险评估、任务拆解

### 开发
- **产物**: `task-plan.md` + `progress.md`
- **触发**: coding-executor, react-performance-optimizer
- **内容**: 任务清单、代码实现、持续记录

### 测试
- **产物**: `test-report.md`
- **触发**: testing-orchestrator, visual-test, quality-gate
- **内容**: 单测/集成/E2E、覆盖率、失败分析

### 部署
- **产物**: `release-notes.md` + `runbook.md`
- **触发**: deployment-and-ops, versioning-and-release
- **内容**: 部署步骤、回滚方案、监控配置

### 推广
- **产物**: `promotion-plan.md`
- **触发**: (待添加 promotion skills)
- **内容**: 市场策略、用户增长、运营计划

### 知识管理
- **产物**: Obsidian vault / Wiki
- **触发**: obsidian-skills, docs-and-knowledge-management
- **内容**: 文档归档、知识图谱、最佳实践

### 迭代
- **产物**: `iteration-plan.md`
- **触发**: planning-with-files
- **内容**: 下一轮迭代计划、优化项、技术债

### Skill优化
- **产物**: `evolution.json`
- **触发**: skill-lifecycle-and-evolution, skill-indexing-maintainer
- **内容**: 触发修复、流程优化、新技能创建

## 持久化文件系统

### 必做：建立"文件即记忆"

创建工作目录（如 `.work/` 或 `project-work/`），并建立三文件：

- `task-plan.md`: 阶段与任务清单（checkbox）
- `findings.md`: 研究/发现/坑点/链接/命令输出摘要
- `progress.md`: 每次行动的时间线记录

### 写入规则

1. **2-Action Rule**: 每进行 1-2 次"阅读/检索/运行命令/观察输出"，就把要点写进 `findings.md` 或 `progress.md`

2. **决策记录**: 每做出决定（技术选型/接口/数据模型/质量门禁），写进 `task-plan.md` 或 ADR

3. **会话恢复**: 当对话重新开始时，先读取这三个文件恢复上下文

## 快速开始模板

### 初始化工作目录

```markdown
# task-plan.md

# 项目名称
## 当前阶段
- [ ] 当前任务1
- [ ] 当前任务2

## 阶段路线图
1. [ ] 需求澄清
2. [ ] 设计方案
3. [ ] 技术方案
4. [ ] 开发实现
5. [ ] 测试验证
6. [ ] 部署上线
```

```markdown
# findings.md

## 研究笔记

### 技术选型
- 决策: 使用 X 而非 Y
- 原因: ...

### 发现的问题
- 问题描述
- 解决方案

### 命令输出
```bash
# 关键命令记录
```

### 参考链接
- [文档标题](URL)
```

```markdown
# progress.md

## 时间线

### 2026-01-29 10:00
- 创建项目结构
- 配置开发环境

### 2026-01-29 11:30
- 完成 PRD 初稿
- 等待 PM 确认
```

## 技能串联示例

### 场景1：新功能开发

```
用户: "我想加一个用户登录功能"

↓ workflow-orchestrator 判定：需求阶段

↓ 调用 requirements-clarifier
→ 输出: prd.md

↓ 用户确认 PRD

↓ workflow-orchestrator 判定：进入设计阶段

↓ 调用 architecture-designer + ui-ux-design-system-generator
→ 输出: design.md + 设计系统

↓ workflow-orchestrator 判定：进入技术方案阶段

↓ 调用 tech-proposal
→ 输出: tech-plan.md (A/B方案对比)

↓ 用户确认技术方案

↓ workflow-orchestrator 判定：进入开发阶段

↓ 调用 coding-executor
→ 持续更新: task-plan.md + progress.md

↓ 开发完成

↓ workflow-orchestrator 判定：进入测试阶段

↓ 调用 testing-orchestrator + visual-test
→ 输出: test-report.md

↓ 测试通过

↓ workflow-orchestrator 判定：进入部署阶段

↓ 调用 deployment-and-ops
→ 输出: release-notes.md + runbook.md

↓ 部署成功

↓ workflow-orchestrator 判定：进入知识管理阶段

↓ 调用 obsidian-skills
→ 归档到 Obsidian vault
```

### 场景2：Bug修复

```
用户: "登录有问题，报错了"

↓ workflow-orchestrator 判定：测试/调试阶段

↓ 调用 systematic-debugging
→ 定位根因

↓ 调用 coding-executor
→ 修复代码

↓ 调用 quality-gate
→ 验证修复 + 回归测试

↓ 调用 deployment-and-ops
→ 热修复部署
```

### 场景3：性能优化

```
用户: "页面加载太慢了"

↓ workflow-orchestrator 判定：测试阶段（先诊断）

↓ 调用 audit-website
→ 性能分析报告

↓ 根据报告，调用 react-performance-optimizer
→ 优化建议

↓ 调用 coding-executor
→ 实施优化

↓ 调用 testing-orchestrator
→ 验证性能提升
```

## 输出格式偏好

- 默认在工作目录写文件，而不是把所有内容堆在对话里
- 面向执行：用 checklist、表格、明确的"下一步"
- 结构化：使用 Markdown 标题、列表、代码块

## 质量检查点

每个阶段结束时，检查：

- [ ] 产物文件已生成
- [ ] 产物文件已更新到工作目录
- [ ] findings.md 或 progress.md 已更新
- [ ] 下一阶段已明确
- [ ] 需要切换的 skill 已识别

## 相关技能

### 需求阶段
- requirements-clarifier
- prd-generator (VerveFlow)
- optimize-iteration-spec (Cursor)

### 设计阶段
- architecture-designer
- ui-ux-design-system-generator
- pencil-design-workflow
- stitch-design-workflow

### 技术方案阶段
- tech-proposal (VerveFlow)
- implementation-plan-writer

### 开发阶段
- coding-executor
- react-performance-optimizer
- systematic-debugging

### 测试阶段
- testing-orchestrator
- visual-test
- quality-gate

### 部署阶段
- deployment-and-ops
- versioning-and-release
- ios-simulator-deployment (VerveFlow)

### 知识管理阶段
- obsidian-skills
- docs-and-knowledge-management

### 优化阶段
- skill-lifecycle-and-evolution
- skill-indexing-maintainer

---

**维护**: 根据实际使用经验持续优化
**来源**: 基于 Cursor Hi Offer workflow-orchestrator，适配完整研发流程

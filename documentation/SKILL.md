---
name: docs-and-knowledge-management
description: 文档与知识管理（PRD/Design/ADR/Test/Runbook/Release文档治理+可选Obsidian）。管理项目文档、生成文档模板、维护知识库。当需要创建文档、组织知识、使用Obsidian时使用。
---

# Docs and Knowledge Management - 文档与知识管理

## 目标

建立和维护项目文档体系，确保知识有效沉淀和传承。

## 文档类型

### 1. PRD (产品需求文档)

**目的**: 描述产品要做什么、为什么做、为谁做

**内容结构**:
- 产品概述（目标/价值/用户）
- 功能需求（清单/详细说明）
- 验收标准（Given-When-Then）
- 业务规则（BR编号）

**模板**: 见 `prd-generator` 技能

### 2. Design (设计文档)

**目的**: 描述系统如何实现需求

**内容结构**:
- 系统架构（分层/模块）
- 接口设计（API规范）
- 数据模型（ER图）
- 技术选型（理由/权衡）

**模板**: 见 `architecture-designer` 技能

### 3. ADR (架构决策记录)

**目的**: 记录重要的技术决策及其原因

**内容结构**:
- 状态（提议/已接受/已弃用）
- 上下文（问题/背景）
- 决策（选择方案）
- 原因和后果（正面/负面）
- 替代方案

**模板**: 见 `architecture-designer` 技能

### 4. Test Plan (测试计划)

**目的**: 描述测试策略和范围

**内容结构**:
- 测试范围（单测/集成/E2E）
- 测试策略（覆盖率/优先级）
- 测试用例（场景/步骤）
- 通过标准

**模板**: 见 `testing-orchestrator` 技能

### 5. Runbook (运维手册)

**目的**: 指导运维操作和故障处理

**内容结构**:
- 服务概述（架构/组件）
- 常见操作（启动/停止/日志）
- 故障处理（诊断/解决）
- 紧急联系

**模板**: 见 `deployment-and-ops` 技能

### 6. Release Notes (发布说明)

**目的**: 向用户和团队说明版本变更

**内容结构**:
- 新功能
- Bug修复
- 性能优化
- 破坏性变更
- 升级指南

**模板**: 见 `versioning-and-release` 技能

## Obsidian集成（可选）

### 双链语法

```markdown
## 相关文档
- [[PRD-001]]: 用户认证功能
- [[ADR-002]]: 数据库选型
- [[API-001]]: 认证API规范
```

### 标签系统

```markdown
---
tags: [prd, v1.0, feature]
category: 需求文档
status: 草稿
---
```

### MOC (Map of Content)

```markdown
# 用户认证功能 MOC

## 概览
- [[PRD-001]]: 产品需求
- [[Design-001]]: 设计文档
- [[ADR-002]]: 架构决策
- [[API-001]]: API规范

## 相关
- [[项目索引]]
```

## 文档生命周期

```markdown
## 文档状态

### 草稿 (Draft)
- 正在编写中
- 内容不完整

### 评审中 (In Review)
- 待团队审查
- 待PM确认

### 已确认 (Confirmed)
- 可以基于此开发
- 后续变更需走流程

### 已废弃 (Deprecated)
- 不再使用
- 保留作为参考
```

## 文档质量标准

```markdown
## 质量检查清单

### 完整性
- [ ] 必要章节齐全
- [ ] 关键信息完整
- [ ] 示例充分

### 准确性
- [ ] 内容准确无误
- [ ] 技术细节正确
- [ ] 数据真实

### 可读性
- [ ] 结构清晰
- [ ] 语言简洁
- [ ] 格式规范

### 可维护性
- [ ] 版本控制
- [ ] 变更记录
- [ ] 定期更新
```

## 文档组织结构

```
docs/
├── prd/                    # 产品需求
│   ├── v1.0/
│   │   ├── PRD-001.md
│   │   └── PRD-002.md
│   └── v1.1/
├── design/                 # 设计文档
│   ├── architecture/
│   ├── api/
│   └── database/
├── adr/                    # 架构决策
│   ├── 001-db-selection.md
│   └── 002-cache-strategy.md
├── test/                   # 测试文档
│   ├── test-plan.md
│   └── test-report.md
├── runbook/                # 运维手册
│   └── runbook.md
└── release/                # 发布说明
    ├── v1.0.0.md
    └── v1.1.0.md
```

## 文档生成工具

### 自动生成

```bash
# 生成API文档
npm run docs:api

# 生成CHANGELOG
npm run changelog

# 生成架构图
npm run docs:arch
```

### 模板系统

```bash
# 使用文档模板
docs-template --type prd --name PRD-003

# 更新现有文档
docs-update --file PRD-001.md --section 功能清单
```

## 与其他技能的集成

### 配合技能
- `prd-generator` - 生成PRD
- `architecture-designer` - 生成设计文档
- `testing-orchestrator` - 生成测试计划
- `deployment-and-ops` - 生成Runbook
- `obsidian-skills` - Obsidian深度集成

### 触发条件
- 项目开始时
- 功能变更时
- 版本发布时
- 定期维护

## 最佳实践

### 1. 文档即代码
- Markdown格式
- Git版本控制
- Code Review

### 2. 文档驱动开发
- 先写文档
- 基于文档开发
- 更新文档

### 3. 持续更新
- 每次变更更新文档
- 定期review文档
- 废弃过时文档

---

**维护**: 根据文档管理经验持续优化
**来源**: Cursor Hi Offer docs-and-knowledge-management
**相关**: obsidian-skills, prd-generator, architecture-designer

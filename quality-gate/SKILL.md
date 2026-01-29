---
name: quality-gate
description: 质量门禁检查（TDD优先/回归测试/完成前验证）。确保代码在提交/合并/发布前满足质量标准。当代码完成、准备提交、准备发布时使用。
---

# Quality Gate - 质量门禁

## 目标

在代码提交、合并、发布前，确保满足预定义的质量标准。

## 质量门禁点

### Gate 1: 提交前 (Pre-commit)

**目的**: 确保提交的代码质量

**检查项**:
```bash
# 1. 代码格式化
npm run format

# 2. Lint检查
npm run lint

# 3. 类型检查
npm run typecheck

# 4. 单元测试
npm run test:unit

# 5. 覆盖率检查
npm run test:coverage
```

**通过标准**:
- [ ] 无lint错误
- [ ] 无类型错误
- [ ] 单元测试全部通过
- [ ] 覆盖率未下降

**失败处理**:
- Lint错误: 自动修复或手动修复
- 类型错误: 修复类型定义
- 测试失败: 修复代码或测试
- 覆盖率下降: 补充测试

### Gate 2: 合并前 (Pre-merge)

**目的**: 确保PR可以安全合并

**检查项**:
```markdown
## 代码审查
- [ ] 代码逻辑正确
- [ ] 代码可读性好
- [ ] 有适当注释
- [ ] 无安全漏洞
- [ ] 性能无明显退化

## 功能验证
- [ ] 功能符合需求
- [ ] 验收标准通过
- [ ] 边界条件处理
- [ ] 错误处理完善

## 测试覆盖
- [ ] 单元测试通过
- [ ] 集成测试通过
- [ ] E2E测试通过
- [ ] 回归测试通过
```

**通过标准**:
- [ ] 至少1人审查通过
- [ ] 所有测试通过
- [ ] 无P0/P1 issue
- [ ] 文档已更新

### Gate 3: 发布前 (Pre-release)

**目的**: 确保版本可以安全发布

**检查项**:
```markdown
## 功能完整性
- [ ] 所有计划功能已实现
- [ ] 所有P0 bug已修复
- [ ] 验收标准全部满足

## 质量指标
- [ ] 测试覆盖率达标
- [ ] 性能指标达标
- [ ] 安全扫描通过
- [ ] 依赖无已知漏洞

## 发布准备
- [ ] Release notes已完成
- [ ] Runbook已更新
- [ ] 回滚方案已准备
- [ ] 监控已配置
```

## TDD优先原则

### TDD流程

```
红 (Red) → 绿 (Green) → 重构 (Refactor)
    ↓           ↓            ↓
  写失败测试  写最少代码   改进代码
```

### TDD检查点

**Gate 1: 功能开发前**
```markdown
## TDD准备检查
- [ ] 是否有测试场景清单？
- [ ] 是否明确验收标准？
- [ ] 测试框架是否配置？

**如果答案都是YES → 开始TDD**
**如果任何NO → 先完成准备工作**
```

**Gate 2: 功能开发中**
```markdown
## TDD执行检查
- [ ] 是否先写测试？
- [ ] 测试是否失败了？（红）
- [ ] 是否写了最少代码让它通过？（绿）
- [ ] 是否重构了代码？

**任何NO → 回到TDD流程**
```

**Gate 3: 功能完成后**
```markdown
## TDD完成检查
- [ ] 所有测试通过？
- [ ] 代码是否重构过？
- [ ] 测试覆盖率是否达标？
- [ ] 是否有flaky test？
```

### 不适用TDD的场景

以下场景可以不使用TDD，但需要说明理由：

```markdown
## TDD豁免记录

**功能**: {功能名称}
**豁免原因**:
- [ ] UI原型探索（需求不明确）
- [ ] 技术预研（验证可行性）
- [ ] 紧急hotfix（时间紧迫）
- [ ] 其他: {说明}

**替代方案**: {如何保证质量}
**审批**: {负责人批准}
```

## 回归测试要求

### 触发条件

必须执行回归测试的情况：
- [ ] 修复了bug
- [ ] 重构了代码
- [ ] 添加了新功能
- [ ] 修改了公共模块

### 回归范围

```markdown
## 回归测试清单

### 核心功能 (必须)
- [ ] 功能1: {测试点}
- [ ] 功能2: {测试点}

### 影响范围 (根据改动)
- [ ] 模块A: {测试点}
- [ ] 接口B: {测试点}

### 高风险区域 (经验判断)
- [ ] {潜在影响点1}
- [ ] {潜在影响点2}
```

### 回归通过标准

- [ ] 所有核心功能正常
- [ ] 无新增P0/P1 bug
- [ ] 性能无明显退化
- [ ] 数据完整性验证

## 完成前验证 (DoD)

### Definition of Done (完成定义)

```markdown
## DoD Checklist

### 代码质量
- [ ] 代码已审查
- [ ] Lint检查通过
- [ ] 类型检查通过
- [ ] 代码已格式化

### 测试覆盖
- [ ] 单元测试通过
- [ ] 集成测试通过
- [ ] E2E测试通过
- [ ] 覆盖率达标

### 文档更新
- [ ] 代码已注释
- [ ] API文档已更新
- [ ] 用户文档已更新
- [ ] Changelog已更新

### 验收标准
- [ ] 功能符合需求
- [ ] 验收标准通过
- [ ] PM确认验收
- [ ] 无遗留P0/P1

### 部署准备
- [ ] 环境配置已更新
- [ ] 迁移脚本已准备
- [ ] 回滚方案已准备
- [ ] 监控已配置
```

### 不符合DoD的处理

```markdown
## DoD未通过处理

### 识别缺失项
- [ ] 缺失项1: {描述}
- [ ] 缺失项2: {描述}

### 处理方案
- [ ] 立即补充: {方案}
- [ ] 技术债记录: {内容}
- [ ] 风险评估: {描述}

### 决策
- [ ] 继续完成DoD
- [ ] 记录技术债，继续
- [ ] 需要讨论: {问题}
```

## 质量指标

### 代码质量

| 指标 | 目标 | 测量方法 |
|------|------|---------|
| 代码覆盖率 | ≥80% | jest --coverage |
| 复杂度 | ≤15 | eslint complexity |
| 重复代码 | ≤3% | jscpd |
| 代码行数/函数 | ≤50 | eslint max-lines-per-function |

### 测试质量

| 指标 | 目标 | 测量方法 |
|------|------|---------|
| 测试通过率 | 100% | npm test |
| Flaky test率 | 0% | 多次运行测试 |
| 测试执行时间 | ≤5min | time npm test |

### 性能质量

| 指标 | 目标 | 测量方法 |
|------|------|---------|
| 首屏加载 | ≤2s | Lighthouse |
| API响应 | ≤200ms | 性能监控 |
| 内存泄漏 | 无 | 性能分析 |

## 与其他技能的集成

### 前置技能
- `coding-executor` - 代码完成后触发质量检查
- `testing-orchestrator` - 执行测试计划
- `systematic-debugging` - Bug修复后验证

### 后置技能
- `deployment-and-ops` - 质量通过后部署
- `versioning-and-release` - 质量通过后发布

### 协作技能
- `code-review-checklist` - 代码审查清单
- `visual-test` - UI视觉质量检查
- `audit-website` - 网站质量审计

## 质量门禁配置

### 配置文件示例

```yaml
# quality-gate.yml
gates:
  pre-commit:
    - lint
    - typecheck
    - test:unit
    - coverage

  pre-merge:
    - test:integration
    - test:e2e
    - security-scan

  pre-release:
    - test:regression
    - performance-test
    - manual-qa

thresholds:
  coverage: 80
  complexity: 15
  duplication: 3

blocking:
  - lint
  - typecheck
  - test:unit

warnings:
  - coverage
  - complexity
```

---

**维护**: 根据项目质量标准调整
**来源**: Cursor Hi Offer quality-gate
**相关**: testing-orchestrator, coding-executor, deployment-and-ops

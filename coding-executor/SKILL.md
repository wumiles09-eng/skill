---
name: coding-executor
description: 按任务清单执行编码（小步骤+持久化记录+验证）。将实施计划转化为代码，每步验证并记录。当开始编码实现、按计划执行任务时使用。
---

# Coding Executor - 代码执行器

## 目标

按实施计划执行编码任务，确保每步可验证、可回滚。

## 执行流程

### Step 1: 读取任务

```markdown
## 当前任务

**任务ID**: T-1
**任务名称**: {名称}
**描述**: {描述}
**输入**: {需要的输入}
**输出**: {预期产出}
**验证**: {验证方式}
```

### Step 2: 执行编码

```markdown
## 编码步骤

### 2.1 理解需求
- [ ] 阅读相关文档
- [ ] 查看现有代码
- [ ] 确认技术方案

### 2.2 编写代码
- [ ] 创建/修改文件
- [ ] 实现核心逻辑
- [ ] 添加错误处理

### 2.3 本地验证
- [ ] 代码格式化
- [ ] Lint检查
- [ ] 类型检查
- [ ] 单元测试
```

### Step 3: 记录进度

```markdown
## 进度记录

### 完成内容
```typescript
// {文件路径}: {行号}
{代码片段}
```

### 遇到的问题
- **问题**: {描述}
- **解决**: {方案}

### 下一步
- [ ] {下个任务}
```

### Step 4: 更新状态

```bash
# 更新任务状态
task-update --id T-1 --status completed
```

## 执行原则

### 1. 小步快跑

```markdown
## 任务粒度

### 推荐（5-20分钟）
- ✅ 添加登录表单UI
- ✅ 实现表单验证
- ✅ 添加登录API

### 避免（太大）
- ❌ 实现用户认证系统
- ❌ 完成订单模块
```

### 2. 持续验证

```markdown
## 验证频率

### 每步验证
- 编写代码后立即测试
- 提交前运行所有测试
- 合并前code review

### 验证内容
- [ ] 代码格式化
- [ ] Lint检查
- [ ] 类型检查
- [ ] 单元测试
```

### 3. 持久化记录

```markdown
## 记录方式

### 进度文件
```markdown
# progress.md

## 2026-01-29 10:00
- [T-1] 开始实现登录表单

## 2026-01-29 10:30
- [T-1] 完成登录表单UI
- 遇到问题: 样式不生效
- 解决: 缺少className绑定
```

### Findings文件
```markdown
# findings.md

## 技术决策
- 使用Formik处理表单状态
- 使用Yup进行验证

## 问题记录
- {问题1}: {解决}
- {问题2}: {解决}
```
```

## 任务执行模板

```markdown
## 任务执行: {任务名称}

### 1. 准备
**文件**: {涉及的文件}
**依赖**: {前置条件}
**环境**: {需要的环境配置}

### 2. 执行
```typescript
// {文件路径}
// 变更: {变更描述}

{代码}
```

### 3. 验证
- [ ] 本地运行正常
- [ ] 测试通过
- [ ] 无lint错误

### 4. 记录
**完成时间**: {时间}
**变更文件**: {列表}
**测试结果**: {结果}
```

## 常见场景

### 场景1: 新增功能

```markdown
## 新增功能: {功能名}

### Step 1: 创建文件
```bash
touch src/features/{feature}.tsx
```

### Step 2: 实现逻辑
```typescript
// src/features/{feature}.tsx
export function {Feature}() {
  // 实现代码
}
```

### Step 3: 添加测试
```typescript
// src/features/{feature}.test.ts
describe('{Feature}', () => {
  it('should work', () => {
    // 测试代码
  });
});
```

### Step 4: 验证
```bash
npm test {feature}
npm run lint
```
```

### 场景2: 修复Bug

```markdown
## Bug修复: {Bug描述}

### Step 1: 定位问题
- 查看错误日志
- 复现问题
- 定位根因代码

### Step 2: 编写测试（先写失败的测试）
```typescript
it('should fix the bug', () => {
  // 测试用例
});
```

### Step 3: 修复代码
```typescript
// 修复代码
```

### Step 4: 验证
```bash
npm test # 测试应该通过
```
```

### 场景3: 重构代码

```markdown
## 重构: {重构目标}

### Step 1: 添加测试（如果没有）
```typescript
// 确保重构有测试保护
```

### Step 2: 小步重构
- 重命名变量/函数
- 提取函数
- 优化逻辑

### Step 3: 持续验证
```bash
npm test # 每次改动后运行
```
```

## 质量检查

```markdown
## 提交前检查

### 代码质量
- [ ] 代码格式化
- [ ] Lint无错误
- [ ] 类型检查通过
- [ ] 无console.log

### 测试覆盖
- [ ] 新增代码有测试
- [ ] 所有测试通过
- [ ] 覆盖率未下降

### 文档更新
- [ ] 更新相关文档
- [ ] 添加必要的注释
- [ ] 更新CHANGELOG
```

## 与其他技能的集成

### 前置技能
- `implementation-plan-writer` - 按实施计划执行
- `architecture-designer` - 按架构设计实现

### 后置技能
- `testing-orchestrator` - 完成后进行测试
- `quality-gate` - 通过质量门禁
- `code-review-checklist` - 代码审查

### 协作技能
- `systematic-debugging` - 调试问题
- `react-performance-optimizer` - 性能优化

## 最佳实践

### 1. 任务驱动
- 从任务列表中选取当前任务
- 完成后标记并记录
- 继续下一个任务

### 2. 小步提交
- 每个任务单独提交
- 提交信息清晰
- 便于回滚

### 3. 持续验证
- 每步都验证
- 问题早发现
- 避免累积

---

**维护**: 根据编码执行经验持续优化
**来源**: Cursor Hi Offer coding-executor
**相关**: implementation-plan-writer, testing-orchestrator, systematic-debugging

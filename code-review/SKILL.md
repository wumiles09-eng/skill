---
name: code-review-checklist
description: 代码审查清单（正确性/可维护性/安全性/性能/测试/文档）。系统化代码审查，确保代码质量。当代码审查、PR review、质量检查时使用。
---

# Code Review Checklist - 代码审查清单

## 目标

系统化地审查代码，确保代码质量、可维护性和团队标准一致性。

## 审查维度

### 1. 正确性 (Correctness)

```markdown
## 功能正确性

### 逻辑正确
- [ ] 代码实现了需求功能
- [ ] 边界条件处理正确
- [ ] 错误处理完善
- [ ] 无明显bug

### 边界条件
- [ ] 空值/undefined处理
- [ ] 数组边界检查
- [ ] 极值处理（最大/最小）
- [ ] 并发/竞态条件

### 错误处理
- [ ] try-catch覆盖必要场景
- [ ] 错误信息清晰
- [ ] 错误不会泄露敏感信息
- [ ] 有适当的日志记录
```

### 2. 可维护性 (Maintainability)

```markdown
## 代码可维护性

### 可读性
- [ ] 变量/函数命名清晰
- [ ] 代码结构清晰
- [ ] 复杂逻辑有注释
- [ ] 避免过度嵌套

### 模块化
- [ ] 函数职责单一
- [ ] 函数长度合理（<50行）
- [ ] 避免重复代码
- [ ] 合理的抽象层次

### 文档
- [ ] 复杂逻辑有注释
- [ ] 公共API有文档
- [ ] 示例代码正确
- [ ] README更新（如需要）
```

### 3. 安全性 (Security)

```markdown
## 安全检查

### 输入验证
- [ ] 用户输入已验证
- [ ] 防止SQL注入
- [ ] 防止XSS攻击
- [ ] 文件类型验证

### 数据安全
- [ ] 敏感数据加密
- [ ] 不泄露敏感信息
- [ ] 安全存储密码
- [ ] HTTPS通信

### 权限控制
- [ ] 访问权限检查
- [ ] 资源权限验证
- [ ] API鉴权
- [ ] 越权访问防护
```

### 4. 性能 (Performance)

```markdown
## 性能考虑

### 算法复杂度
- [ ] 时间复杂度合理
- [ ] 避免不必要的循环
- [ ] 使用合适的数据结构
- [ ] 避免深层嵌套

### 资源使用
- [ ] 避免内存泄漏
- [ ] 及时释放资源
- [ ] 避免频繁的DOM操作
- [ ] 使用缓存优化

### 异步处理
- [ ] 使用异步避免阻塞
- [ ] 正确处理Promise
- [ ] 避免回调地狱
- [ ] 错误处理完善
```

### 5. 测试 (Testing)

```markdown
## 测试覆盖

### 单元测试
- [ ] 核心逻辑有测试
- [ ] 边界条件有测试
- [ ] 错误路径有测试
- [ ] 测试有意义

### 测试质量
- [ ] 测试命名清晰
- [ ] 测试独立
- [ ] 断言准确
- [ ] 无flaky test

### 覆盖率
- [ ] 新代码覆盖率达标
- [ ] 关键路径覆盖
- [ ] 覆盖率未下降
```

### 6. 文档 (Documentation)

```markdown
## 文档完整性

### 代码注释
- [ ] 复杂逻辑有注释
- [ ] "为什么"而非"是什么"
- [ ] 注释与代码一致
- [ ] 无废弃注释

### API文档
- [ ] 公共API有文档
- [ ] 参数类型说明
- [ ] 返回值说明
- [ ] 使用示例

### 变更文档
- [ ] README更新（如需要）
- [ ] CHANGELOG更新
- [ ] 迁移指南（如需要）
```

## 审查流程

### Step 1: 快速扫描

```markdown
## 初步检查

### 基本信息
- PR标题清晰？
- 描述充分？
- 相关Issue链接？
- 变更范围合理？

### 自动化检查
- [ ] CI检查通过
- [ ] 测试全部通过
- [ ] 覆盖率达标
- [ ] 无新的warning
```

### Step 2: 深度审查

```markdown
## 详细审查

### 代码变更
```diff
# 查看diff
{diff内容}
```

### 关注点
- 核心逻辑变更
- 复杂算法
- 安全相关代码
- 性能敏感代码
```

### Step 3: 反馈

```markdown
## 反馈格式

### 问题报告
```markdown
### 问题: {简短描述}

**位置**: {文件}:{行号}

**问题**: {详细描述}

**建议**: {改进建议}

**优先级**: [必须修复/建议修复/可选]
```

### 正向反馈
```markdown
### 好的做法: {描述}

**位置**: {文件}:{行号}

**为什么好**: {理由}
```
```

## 常见问题

### 1. 正确性问题

```markdown
## 常见正确性错误

### 边界条件
```javascript
// ❌ 错误
function getFirst(arr) {
  return arr[0]; // 未检查空数组
}

// ✅ 正确
function getFirst(arr) {
  if (!arr || arr.length === 0) {
    return null;
  }
  return arr[0];
}
```

### 异步处理
```javascript
// ❌ 错误
async function fetchData() {
  const data = await fetch(url);
  return data.json(); // 未处理错误
}

// ✅ 正确
async function fetchData() {
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error('Fetch failed:', error);
    throw error;
  }
}
```
```

### 2. 性能问题

```markdown
## 常见性能问题

### 不必要的渲染
```javascript
// ❌ 错误: 每次渲染都创建新函数
function Component() {
  return <Button onClick={() => handleClick()} />;
}

// ✅ 正确: 使用useCallback
function Component() {
  const handleClick = useCallback(() => {
    // ...
  }, []);
  return <Button onClick={handleClick} />;
}
```

### 循环中的DOM操作
```javascript
// ❌ 错误
for (let i = 0; i < 1000; i++) {
  document.body.appendChild(createElement());
}

// ✅ 正确: 使用DocumentFragment
const fragment = document.createDocumentFragment();
for (let i = 0; i < 1000; i++) {
  fragment.appendChild(createElement());
}
document.body.appendChild(fragment);
```
```

## 审查检查清单

```markdown
## Code Review Checklist

### 快速检查（2分钟）
- [ ] CI通过
- [ ] 测试通过
- [ ] 描述清晰
- [ ] 变更合理

### 深度审查（10-15分钟）
- [ ] 功能正确性
- [ ] 代码可读性
- [ ] 安全性检查
- [ ] 性能考虑
- [ ] 测试覆盖
- [ ] 文档完整

### 反馈
- [ ] 问题报告清晰
- [ ] 建议可操作
- [ ] 优先级明确
- [ ] 语气友好
```

## 与其他技能的集成

### 前置技能
- `coding-executor` - 代码完成后审查
- `testing-orchestrator` - 测试通过后审查

### 后置技能
- `quality-gate` - 审查通过后进入质量门禁
- `deployment-and-ops` - 审查通过后可部署

### 协作技能
- `systematic-debugging` - 发现问题时调试
- `react-performance-optimizer` - 性能问题优化

## 最佳实践

### 1. 及时审查
- PR创建后24小时内审查
- 避免大量代码累积

### 2. 建设性反馈
- 指出问题的同时给出建议
- 解释为什么需要改进

### 3. 认可好代码
- 及时认可优秀实践
- 分享学习机会

---

**维护**: 根据代码审查经验持续优化
**来源**: Cursor Hi Offer code-review-checklist
**相关**: quality-gate, coding-executor, testing-orchestrator

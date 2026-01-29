---
name: pencil-design-workflow
description: Pencil MCP设计到代码工作流（像素级精度/组件库对齐）。使用Pencil MCP将Figma设计转换为代码，与组件库（Halo/shadcn）对齐。当需要从Figma导入设计、与组件库对齐时使用。
---

# Pencil Design Workflow - Pencil MCP工作流

## 目标

使用Pencil MCP实现像素级精度的设计到代码转换，与现有组件库对齐。

## 何时使用

- 从Figma/Sketch导入设计
- 需要像素级精度还原
- 与组件库（Halo/shadcn/Ant Design）对齐
- 长期维护的设计系统

## 核心理念

### Design as Code

```
传统: 设计 → 开发 → 调整 → 再调整
Pencil: 设计 = 代码 (单一真相源)
```

### 与Stitch对比

| 维度 | Pencil | Stitch |
|------|--------|--------|
| 精度 | 像素级 | 快速原型 |
| 速度 | 较慢 | 快速 |
| 适用场景 | 产品开发 | MVP验证 |
| 维护性 | 高（代码即设计） | 中 |
| 组件库 | 深度集成 | 独立 |

## 工作流程

### Phase 1: 设计准备

```markdown
## 设计准备清单

### 1.1 组件库确认
- [ ] 确认使用的组件库（Halo/shadcn/Ant Design等）
- [ ] 检查组件库版本
- [ ] 了解组件库API

### 1.2 设计规范
- [ ] 设计token（颜色/字体/间距）
- [ ] 组件变体规则
- [ ] 响应式断点

### 1.3 Pencil配置
- [ ] 安装Pencil MCP
- [ ] 配置设计源
- [ ] 设置导出选项
```

### Phase 2: 设计导入

```bash
# 使用Pencil MCP导入设计
pencil_import --source figma --file "design_url"

# 导出选项
pencil_import \
  --source figma \
  --format react \
  --component-library shadcn \
  --output src/components
```

### Phase 3: 组件映射

```markdown
## 组件映射策略

### 优先使用组件库组件
| 设计元素 | 组件库组件 | 配置 |
|---------|-----------|------|
| 按钮 | Button | variant/size |
| 输入框 | Input | placeholder/disabled |
| 卡片 | Card | 布局/样式 |

### 自定义组件
- 复杂交互：自定义组件
- 特殊样式：组件库组件 + 覆盖样式
- 动画：Framer Motion + 组件库组件
```

### Phase 4: 代码生成

```bash
# 生成React代码
pencil_generate \
  --input design.pencil \
  --output src \
  --format react \
  --typescript \
  --tailwind

# 与组件库对齐
pencil_generate \
  --component-library shadcn \
  --prefer-library-components \
  --custom-props "variant,size"
```

### Phase 5: 验证与调整

```markdown
## 验证检查清单

### 视觉验证
- [ ] 像素级精度对比
- [ ] 间距一致性
- [ ] 颜色准确性
- [ ] 字体渲染

### 功能验证
- [ ] 交互正常
- [ ] 响应式正常
- [ ] 可访问性
- [ ] 性能检查

### 组件对齐
- [ ] 优先使用组件库组件
- [ ] 自定义样式最小化
- [ ] 遵循组件库API
```

## Pencil MCP工具

### 核心命令

```javascript
// 读取Pencil文件
const design = await pencil.read('design.pencil');

// 导出组件
const components = await pencil.exportComponents(design, {
  format: 'react',
  typescript: true,
  componentLibrary: 'shadcn'
});

// 导出样式
const styles = await pencil.exportStyles(design, {
  format: 'tailwind',
  includeTokens: true
});

// 验证设计
const validation = await pencil.validate(design, {
  componentLibrary: 'shadcn',
  checkResponsive: true
});
```

## 组件库集成

### Shadcn UI

```typescript
// 组件映射示例
import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';
import { Input } from '@/components/ui/input';

// 使用组件库组件
function LoginForm() {
  return (
    <Card className="w-[400px]">
      <CardHeader>
        <Title>登录</Title>
      </CardHeader>
      <CardContent>
        <Input placeholder="邮箱" />
        <Button variant="default" size="lg">
          登录
        </Button>
      </CardContent>
    </Card>
  );
}
```

### Halo UI

```typescript
// Halo组件库集成
import { HaloButton, HaloCard, HaloInput } from '@halo/ui';

// 自定义主题
const theme = {
  colors: {
    primary: 'var(--primary)',
    // ... design tokens
  }
};
```

### Ant Design

```typescript
// Ant Design集成
import { Button, Card, Input } from 'antd';

// 配置主题
const theme = {
  token: {
    colorPrimary: '#1890ff',
    // ... design tokens
  }
};
```

## 最佳实践

### 1. 设计Token管理

```css
/* design-tokens.css */
:root {
  /* Colors */
  --color-primary: #1890ff;
  --color-secondary: #52c41a;

  /* Spacing */
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;

  /* Typography */
  --font-size-base: 14px;
  --font-size-lg: 16px;
}
```

### 2. 组件变体

```typescript
// 组件变体配置
const buttonVariants = {
  primary: {
    backgroundColor: 'var(--color-primary)',
    color: 'white'
  },
  secondary: {
    backgroundColor: 'var(--color-secondary)',
    color: 'white'
  }
};
```

### 3. 响应式设计

```css
/* 响应式断点 */
@media (max-width: 768px) {
  .container {
    padding: var(--spacing-md);
  }
}
```

## 与Stitch工作流配合

### Stitch用于快速原型，Pencil用于精修

```
1. Stitch快速生成页面原型
    ↓
2. 设计师在Figma中精修
    ↓
3. Pencil导入精修设计
    ↓
4. 与组件库对齐
    ↓
5. 生成生产代码
```

## 输出质量标准

### 代码质量

```markdown
## 代码标准

- [ ] TypeScript类型完整
- [ ] 组件可复用
- [ ] 样式模块化
- [ ] 性能优化（memo/lazy）
- [ ] 可访问性（ARIA）
```

### 设计还原

```markdown
## 设计还原标准

- [ ] 像素级精度（±1px）
- [ ] 颜色准确（ΔE<2）
- [ ] 字体渲染一致
- [ ] 间距准确
- [ ] 交互流畅
```

## 常见问题

### Q1: 组件库没有需要的组件怎么办？

**A**:
1. 使用组件库基础组件组合
2. 扩展现有组件
3. 自定义组件（遵循组件库规范）

### Q2: 设计与组件库风格不一致？

**A**:
1. 使用设计token覆盖组件库样式
2. 调整设计以符合组件库规范
3. 与设计团队协商统一

### Q3: 如何保持设计与代码同步？

**A**:
1. 代码作为设计的单一真相源
2. Pencil文件作为设计源
3. 自动化CI/CD同步

## 与其他技能的集成

### 前置技能
- `ui-ux-design-system-generator` - 生成设计系统
- `stitch-design-workflow` - 快速原型

### 后置技能
- `react-performance-optimizer` - 性能优化
- `web-design-guidelines` - 设计审查

### 协作技能
- `frontend-design` - 前端实现
- `vercel-react-best-practices` - React最佳实践

---

**维护**: 根据Pencil MCP更新和项目经验持续优化
**MCP**: user-pencil
**相关**: stitch-design-workflow, ui-ux-design-system-generator, frontend-design

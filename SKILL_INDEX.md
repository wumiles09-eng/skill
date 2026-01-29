# Claude Code Skills 智能索引系统

> 基于RAG智能索引理念的技能管理系统
>
> **核心原则**: 索引 ≠ 检索。索引是为了"更容易被找到"而设计的结构。

---

## 一、索引架构

### 四层索引结构

```
┌─────────────────────────────────────────────────────────────┐
│                    Layer 1: 场景索引 (查询索引)               │
│              "用户会问什么问题？" → 匹配场景                   │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                   Layer 2: 技能摘要 (摘要索引)                 │
│            "技能的核心能力是什么？" → 快速筛选                 │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                  Layer 3: 技能分类 (分块索引)                 │
│              "技能属于哪个类别？" → 分类浏览                   │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                 Layer 4: 完整技能 (子块索引)                  │
│           "技能的完整细节是什么？" → 深度查阅                 │
└─────────────────────────────────────────────────────────────┘
```

---

## 二、Layer 1: 场景索引 (查询索引)

> 用"用户问题"表征技能，解决"问法和技能描述不一致"的问题

### 按用户意图分类

#### 🎯 我想创建/构建 something

| 用户问题 | 匹配技能 | 优先级 |
|---------|---------|--------|
| "设计一个网站/页面/界面" | frontend-design + ui-ux-pro-max | ⭐⭐⭐ |
| "开发一个移动App" | building-native-ui + frontend-design | ⭐⭐⭐ |
| "创建一个React组件" | vercel-react-best-practices + frontend-design | ⭐⭐⭐ |
| "做一个PPT/文档/报告" | document-suite | ⭐⭐⭐ |
| "建立一个知识库" | obsidian-skills + planning-with-files | ⭐⭐ |
| "设计数据库" | supabase-postgres-best-practices | ⭐⭐ |

#### 🔍 我想检查/审查 something

| 用户问题 | 匹配技能 | 优先级 |
|---------|---------|--------|
| "审查我的代码" | vercel-react-best-practices + khazix-skills | ⭐⭐⭐ |
| "检查我的网站" | audit-website + seo-audit + web-design-guidelines | ⭐⭐⭐ |
| "评估设计质量" | web-design-guidelines + ui-ux-pro-max | ⭐⭐⭐ |
| "分析性能问题" | vercel-react-best-practices + supabase-postgres-best-practices | ⭐⭐ |
| "测试我的网站" | agent-browser + superpowers (TDD) | ⭐⭐ |

#### 🚀 我想优化/改进 something

| 用户问题 | 匹配技能 | 优先级 |
|---------|---------|--------|
| "优化React性能" | vercel-react-best-practices | ⭐⭐⭐ |
| "改进SEO" | seo-audit | ⭐⭐⭐ |
| "提升用户体验" | web-design-guidelines + ui-ux-pro-max | ⭐⭐⭐ |
| "重构代码" | khazix-skills + superpowers (systematic-debugging) | ⭐⭐ |
| "优化数据库" | supabase-postgres-best-practices | ⭐⭐ |

#### 📋 我想规划/管理 something

| 用户问题 | 匹配技能 | 优先级 |
|---------|---------|--------|
| "规划一个复杂项目" | planning-with-files + dev-workflow | ⭐⭐⭐ |
| "管理开发流程" | superpowers + dev-workflow | ⭐⭐⭐ |
| "组织团队协作" | superpowers (collaboration) | ⭐⭐ |
| "跟踪项目进度" | planning-with-files | ⭐⭐ |
| "创建工作流" | skill-creator + dev-workflow | ⭐⭐ |

#### 🎓 我想学习/提取 something

| 用户问题 | 匹配技能 | 优先级 |
|---------|---------|--------|
| "学习最佳实践" | skill-from-masters | ⭐⭐⭐ |
| "理解专家代码" | skill-from-masters + khazix-skills | ⭐⭐ |
| "创建自定义技能" | skill-creator | ⭐⭐⭐ |
| "提取代码模式" | skill-from-masters | ⭐⭐ |

#### 🤖 我想自动化 something

| 用户问题 | 匹配技能 | 优先级 |
|---------|---------|--------|
| "自动化测试" | agent-browser + superpowers (TDD) | ⭐⭐⭐ |
| "浏览器自动化" | agent-browser | ⭐⭐⭐ |
| "批量处理" | khazix-skills | ⭐⭐ |
| "更新技能" | skills-updater | ⭐⭐ |

---

## 三、Layer 2: 技能摘要 (摘要索引)

> 用"语义摘要"表征技能，解决复杂技能难以检索的问题

### 核心能力摘要

#### 🎨 设计类 (5个)

**frontend-design**
- 摘要: 生产级前端界面设计，避免AI通用审美，提供独特视觉风格
- 核心能力: 创意设计、美学选择、前端实现
- 典型输出: HTML/CSS/React代码，视觉惊艳

**ui-ux-pro-max**
- 摘要: 67种UI风格 + 96配色方案 + 57字体搭配 + 100+行业规则
- 核心能力: 行业设计系统、专业级UI/UX
- 典型输出: 完整设计系统、行业规范

**web-design-guidelines**
- 摘要: UI/UX审查和改进，WCAG可访问性标准
- 核心能力: 设计审查、可访问性、视觉层级
- 典型输出: 审查报告、改进建议

**building-native-ui**
- 摘要: Expo/React Native移动应用开发
- 核心能力: 移动端UI、平台特性、性能优化
- 典型输出: 移动应用代码

**vercel-react-best-practices**
- 摘要: React/Next.js性能优化，40+性能模式
- 核心能力: 代码审查、性能优化、最佳实践
- 典型输出: 优化的React代码

#### 💾 后端类 (1个)

**supabase-postgres-best-practices**
- 摘要: PostgreSQL优化，RLS策略、存储过程、实时订阅
- 核心能力: 数据库设计、查询优化、安全策略
- 典型输出: 优化的SQL、数据库架构

#### ✅ 质量保障类 (2个)

**audit-website**
- 摘要: 网站综合审计（性能、可访问性、SEO、安全、UX）
- 核心能力: 多维度审查、问题识别、优先级建议
- 典型输出: 审计报告、问题清单

**seo-audit**
- 摘要: SEO诊断，元标签、结构化数据、Core Web Vitals
- 核心能力: 技术SEO、搜索排名、内容优化
- 典型输出: SEO报告、优化建议

#### 📊 生产力类 (2个)

**planning-with-files**
- 摘要: 基于Manus AI的持久化规划系统，文件系统作为记忆
- 核心能力: 跨会话规划、进度跟踪、会话恢复
- 典型输出: task_plan.md, findings.md, progress.md

**superpowers**
- 摘要: TDD、系统化调试、协作模式、git worktree
- 核心能力: 测试驱动开发、调试流程、团队协作
- 典型输出: 测试代码、调试报告

#### 📝 文档类 (2个)

**obsidian-skills**
- 摘要: Obsidian笔记系统，wiki链接、Zettelkasten、知识图谱
- 核心能力: 知识管理、笔记组织、双链
- 典型输出: Obsidian笔记、知识库

**document-suite**
- 摘要: Word/PPT/Excel/PDF创建和编辑
- 核心能力: 专业文档、演示文稿、表格
- 典型输出: DOCX, PPTX, XLSX, PDF

#### 🛠️ 工具类 (3个)

**agent-browser**
- 摘要: 浏览器自动化，页面交互、截图、表单处理
- 核心能力: Web自动化、数据抓取、测试
- 典型输出: 自动化脚本、测试结果

**skill-creator**
- 摘要: 创建自定义技能，模板化技能生成
- 核心能力: 技能设计、结构规范、文档生成
- 典型输出: 新技能目录

**skills-updater**
- 摘要: 技能自动更新，版本管理、回滚
- 核心能力: 版本跟踪、依赖管理、备份恢复
- 典型输出: 更新的技能

#### 🧠 学习类 (2个)

**khazix-skills**
- 摘要: 代码分析、重构、文档生成
- 核心能力: 模式识别、复杂度评估、自动化
- 典型输出: 分析报告、重构代码

**skill-from-masters**
- 摘要: 从专家代码中提取模式和最佳实践
- 核心能力: 模式提取、最佳实践编码、技能生成
- 典型输出: 专家技能

#### 🎯 编排类 (1个)

**dev-workflow**
- 摘要: 协调多个技能的工作流编排器
- 核心能力: 工作流模板、技能协调、任务分配
- 典型输出: 完整项目交付

---

## 四、Layer 3: 技能分类 (分块索引)

> 按"技能类别"组织，支持分类浏览和组合使用

### 按开发阶段分类

```
📋 规划阶段
├── planning-with-files (项目规划)
└── dev-workflow (工作流设计)

🎨 设计阶段
├── ui-ux-pro-max (UI/UX设计系统)
├── frontend-design (前端设计)
└── web-design-guidelines (设计审查)

💻 开发阶段
├── building-native-ui (移动开发)
├── vercel-react-best-practices (React优化)
├── supabase-postgres-best-practices (数据库)
└── khazix-skills (代码分析)

🧪 测试阶段
├── superpowers (TDD)
└── agent-browser (浏览器测试)

✅ 审查阶段
├── audit-website (网站审计)
├── seo-audit (SEO审查)
└── web-design-guidelines (设计审查)

📚 文档阶段
├── obsidian-skills (知识管理)
└── document-suite (办公文档)

🔧 维护阶段
├── skills-updater (技能更新)
└── superpowers (调试)
```

### 按技术栈分类

```
React生态
├── vercel-react-best-practices
├── frontend-design
└── ui-ux-pro-max

移动开发
└── building-native-ui

后端/数据库
└── supabase-postgres-best-practices

Web自动化
└── agent-browser

知识管理
├── obsidian-skills
└── planning-with-files

办公软件
└── document-suite
```

---

## 五、Layer 4: 完整技能 (子块索引)

> 父块: 完整技能文件 (SKILL.md)
> 子块: 技能的各个章节（用于精确匹配）

### 技能细节快速定位

每个技能的子块结构：

```yaml
技能名称:
  子块1: 使用场景 (when to use)
  子块2: 核心功能 (key features)
  子块3: 输出格式 (output)
  子块4: 使用示例 (examples)
  子块5: 最佳实践 (best practices)
  子块6: 相关技能 (integration)
```

### 查询逻辑

1. **粗粒度检索**: 匹配技能摘要 → 返回完整技能
2. **细粒度检索**: 匹配技能子块 → 返回完整技能（父块）
3. **组合检索**: 匹配多个技能摘要 → 返回技能组合

---

## 六、混合索引策略

### 组合拳模式

#### 模式1: 摘要 + 子块
- 摘要负责"找得准"
- 子块负责"定位精"
- 返回父块保证上下文

**示例**: "审查React组件性能"
1. 摘要匹配: vercel-react-best-practices
2. 子块匹配: "performance optimization"
3. 返回: 完整的技能文件

#### 模式2: 查询 + 分类双路召回
- 查询索引对齐用户问法
- 分类索引兜底覆盖
- 相互补位

**示例**: "我想做一个移动App"
1. 查询匹配: "开发移动应用" → building-native-ui
2. 分类匹配: 移动开发类 → building-native-ui
3. 确认匹配: 返回技能

#### 模式3: 场景 → 技能 → 工作流
- 场景索引确定用户意图
- 技能摘要筛选相关技能
- 工作流编排组合使用

**示例**: "从零开始建立一个SaaS产品"
1. 场景: 创建 + 规划
2. 技能: planning-with-files + ui-ux-pro-max + frontend-design + supabase-postgres-best-practices
3. 工作流: dev-workflow 自动编排

---

## 七、使用指南

### 快速查找流程

```
用户提问
    ↓
1. 场景匹配 (我想要做什么？)
    ↓
2. 技能筛选 (哪些技能能帮到我？)
    ↓
3. 分类确认 (这些技能属于什么类别？)
    ↓
4. 深度查阅 (技能的完整细节是什么？)
    ↓
5. 工作流编排 (如何组合使用这些技能？)
```

### 查询示例

#### 示例1: "我要做一个 landing page"

```
场景匹配 → "设计一个网站/页面"
    ↓
技能筛选 → ui-ux-pro-max + frontend-design + web-design-guidelines
    ↓
分类确认 → 设计类技能
    ↓
深度查阅 → 查看各技能的完整细节
    ↓
工作流编排 → dev-workflow 自动协调
```

#### 示例2: "我的网站性能很差"

```
场景匹配 → "优化/改进"
    ↓
技能筛选 → vercel-react-best-practices + audit-website
    ↓
分类确认 → 开发类 + 质量保障类
    ↓
深度查阅 → 性能优化细节 + 审计清单
    ↓
工作流编排 → 先诊断(audit-website) 再优化(vercel-react-best-practices)
```

#### 示例3: "规划一个复杂项目"

```
场景匹配 → "规划/管理"
    ↓
技能筛选 → planning-with-files + dev-workflow
    ↓
分类确认 → 生产力类
    ↓
深度查阅 → Manus AI规划模式 + 工作流模板
    ↓
工作流编排 → planning-with-files 创建规划 → dev-workflow 执行
```

---

## 八、索引维护

### 更新策略

1. **场景索引**: 定期收集用户问题，更新问题-技能映射
2. **技能摘要**: 技能更新时同步更新摘要
3. **技能分类**: 新技能加入时更新分类体系
4. **子块索引**: 技能结构调整时更新子块

### 质量保证

- **召回率测试**: 覆盖常见用户问题
- **准确率验证**: 技能匹配是否准确
- **用户体验**: 查询路径是否直观
- **性能监控**: 查询响应时间

---

## 九、技能关系图谱

### 技能依赖关系

```
核心编排器
└── dev-workflow
    ├── 依赖所有技能
    └── 协调工作流执行

设计系统
├── ui-ux-pro-max (基础设计系统)
│   ├── frontend-design (实现)
│   └── web-design-guidelines (审查)
└── building-native-ui (移动适配)

质量保障
├── audit-website (综合审计)
│   ├── seo-audit (SEO专项)
│   └── web-design-guidelines (设计审查)

开发流程
├── planning-with-files (规划)
├── superpowers (TDD + 调试)
└── khazix-skills (分析)

知识管理
├── obsidian-skills (笔记)
└── document-suite (文档)
```

### 推荐组合

```
完整Web应用
= planning-with-files
+ ui-ux-pro-max
+ frontend-design
+ vercel-react-best-practices
+ supabase-postgres-best-practices
+ audit-website
+ seo-audit

移动应用
= planning-with-files
+ building-native-ui
+ ui-ux-pro-max
+ superpowers (TDD)

知识库系统
= planning-with-files
+ obsidian-skills
+ document-suite

代码质量提升
= khazix-skills
+ vercel-react-best-practices
+ superpowers (systematic-debugging)
+ audit-website
```

---

## 十、总结

### 索引哲学

> **索引不是"把技能直接列出来"，而是"为快速找到合适技能"而专门设计的结构。**

### 四层索引的价值

| 层级 | 索引方式 | 解决问题 |
|------|---------|---------|
| Layer 1 | 场景/查询索引 | "用户不知道如何描述需求" |
| Layer 2 | 技能摘要索引 | "复杂技能难以快速理解" |
| Layer 3 | 技能分类索引 | "不知道去哪里找技能" |
| Layer 4 | 完整技能索引 | "需要技能的完整细节" |

### 使用建议

1. **从场景开始**: 用 Layer 1 快速定位
2. **摘要做筛选**: 用 Layer 2 缩小范围
3. **分类来确认**: 用 Layer 3 验证匹配
4. **深度查阅细节**: 用 Layer 4 获取完整信息
5. **编排实现工作流**: 用 dev-workflow 组合使用

---

**最后更新**: 2026-01-29
**维护者**: Claude Code Skills System
**版本**: 2.0

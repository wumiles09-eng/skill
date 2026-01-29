# Skills Collection - 完整研发流程版

**完整覆盖：想法→需求→设计→技术方案→开发→测试→部署→推广→知识管理→迭代→Skill优化**

[![Skills](https://img.shields.io/badge/Skills-40+-blue)]()
[![Categories](https://img.shields.io/badge/Categories-10-green)]()
[![Phases](https://img.shields.io/badge/Phases-11-purple)]()
[![Stitch AI](https://img.shields.io/badge/Stitch_AI-3-purple)]()

---

## 新增：完整研发流程覆盖

本版本整合了三个优秀技能集合的优势，提供端到端的研发流程支持：

### 来源集合

1. **基础技能 (21 skills)** - 前端、后端、测试、工具
2. **Cursor Hi Offer** - 智能索引、工作流编排、设计系统生成器
3. **VerveFlow** - 7阶段严格SOP、渐进式交付、iOS部署

### 整合策略

- **去重**: 保留最优版本，避免重复
- **互补**: 每个阶段的最佳实践
- **增强**: 4层智能索引、进化追踪

---

## 完整研发流程 (11阶段)

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                         完整研发流程 (11 Stages)                                │
└─────────────────────────────────────────────────────────────────────────────────┘

  想法      →    需求     →    设计    →  技术方案  →   开发   →   测试
   ↓            ↓           ↓            ↓            ↓          ↓
 IdeaClarify  PRD      DesignSpec   TechProposal   Code    Test
   │            │           │            │            │          │
   │      requirements-clarifier        │            │          │
   │      prd-generator (VerveFlow)     │            │          │
   │                                    │            │          │
   │            │      architecture-designer         │          │
   │            │      ui-ux-design-system-gen      │          │
   │            │      pencil/stitch-workflows      │          │
   │            │                                react-perf  │
   │            │                                coding-exec  │
   │            │                                   │          │
   │            │                                   │          │
   │      tech-proposal (VerveFlow)                │          │
   │      implementation-plan-writer               │          │
   │                                                  │          │
   │                                                  │   testing-orchestrator
   │                                                  │   visual-test
   │                                                  │   quality-gate

   部署    →    推广    →  知识管理  →   迭代   →  Skill优化
    ↓          ↓            ↓           ↓            ↓
  Deploy   Promotion   Knowledge   Iterate   Evolution
    │          │            │           │            │
    │   (待添加)   obsidian-skills    planning     skill-indexing
    │              docs-knowledge      -with-files  skill-lifecycle
    │                                  │            │
 deployment-and-ops                      │            │
 versioning-and-release                 │            │
 ios-simulator-deploy (VerveFlow)       │            │
                                        │            │
                            ┌───────────┴────────────┴────────────┐
                            │                                     │
                      workflow-orchestrator (贯穿全流程)
```

---

## 新增核心技能

### 1. 工作流编排

**workflow-orchestrator**
- 自动判定当前阶段
- 生成对应产物文件
- 串联其他技能
- 维护持久化文件系统

### 2. 智能索引系统

**skill-indexing-maintainer** + **SKILLS_REGISTRY.json**
- 4层混合索引（查询+摘要+子块+块）
- 进化追踪（evolution.json）
- 自我改进能力

### 3. 设计系统生成器

**ui-ux-design-system-generator** (替换原 ui-ux-pro-max)
- 67种UI样式
- 96个调色板
- 57个字体配对
- 行业推理引擎
- 脚本化搜索（--persist）

### 4. 需求澄清与PRD

**requirements-clarifier** + **prd-generator**
- 结构化需求提取
- Given-When-Then格式
- 业务语言优先
- Mermaid流程图

### 5. 技术方案

**tech-proposal** (VerveFlow)
- A/B方案对比
- 量化评估（成本/时间/风险）
- 推荐方案+理由
- 风险缓解

### 6. 测试编排

**testing-orchestrator** + **quality-gate**
- 单测/集成/E2E策略
- TDD优先
- 质量门禁
- 回归测试

### 7. 部署运维

**deployment-and-ops** + **versioning-and-release**
- 部署/迁移/回滚
- Runbook生成
- SemVer管理
- 监控告警

**ios-simulator-deployment** (VerveFlow)
- 完整iOS构建/安装/启动
- 故障排查指南
- 最佳实践

---

## 技能清单 (40+)

### 🔵 Stitch AI (3)
- design-md - 设计系统文档生成
- stitch-loop - 批量UI生成
- react-components - 设计转React代码

### 🎯 编排器 (2)
- workflow-orchestrator - 端到端流程编排
- planning-with-files - 持久化规划

### 💡 想法→需求 (3)
- requirements-clarifier - 需求澄清
- prd-generator - PRD生成器 (VerveFlow)
- optimize-iteration-spec - 迭代文档优化

### 🎨 设计 (4)
- architecture-designer - 架构设计
- ui-ux-design-system-generator - 设计系统生成 (67/96/57)
- pencil-design-workflow - Pencil MCP工作流
- stitch-design-workflow - Stitch MCP工作流

### 🔧 技术方案 (2)
- tech-proposal - 技术方案评估 (VerveFlow)
- implementation-plan-writer - 实施计划

### 💻 开发 (6)
- frontend-design - 前端界面设计
- building-native-ui - 移动端UI
- coding-executor - 任务清单执行
- react-performance-optimizer - React性能优化
- vercel-react-best-practices - Vercel最佳实践
- systematic-debugging - 系统化调试

### ✅ 测试 (5)
- testing-orchestrator - 测试编排
- visual-test - 视觉测试
- quality-gate - 质量门禁
- audit-website - 网站审计
- seo-audit - SEO审计

### 🚀 部署 (3)
- deployment-and-ops - 部署运维
- versioning-and-release - 版本发布
- ios-simulator-deployment - iOS模拟器部署 (VerveFlow)

### 📚 知识管理 (3)
- obsidian-skills - Obsidian集成
- docs-and-knowledge-management - 文档治理
- document-suite - 办公文档

### 🔄 迭代 (2)
- planning-with-files - 持久化规划
- code-review-checklist - 代码审查

### 🛠️ 工具 (4)
- agent-browser - 浏览器自动化
- skill-creator - 技能创建
- skills-updater - 技能更新
- skill-indexing-maintainer - 索引维护

### 🌱 学习与进化 (3)
- skill-from-masters - 大师模式提取
- khazix-skills - 代码分析
- skill-lifecycle-and-evolution - 技能生命周期

### 🔧 后端 (1)
- supabase-postgres-best-practices - PostgreSQL优化

---

## 工作流示例

### 示例1: 新功能开发 (完整流程)

```
1. workflow-orchestrator → 判定：需求阶段
2. requirements-clarifier → 输出 prd.md
3. architecture-designer + ui-ux-design-system-generator → 输出 design.md
4. tech-proposal → 输出 tech-plan.md (A/B对比)
5. coding-executor + react-performance-optimizer → 实现
6. testing-orchestrator + visual-test → 测试
7. deployment-and-ops → 部署
8. obsidian-skills → 知识归档
9. skill-lifecycle-and-evolution → 复盘优化
```

### 示例2: 快速UI设计 (Stitch)

```
1. design-md → 生成 DESIGN.md
2. stitch-loop → 批量生成页面
3. react-components → 转换为React代码
4. vercel-react-best-practices → 性能优化
```

### 示例3: iOS应用 (VerveFlow)

```
1. prd-generator → 业务语言PRD
2. architecture-designer → 架构设计
3. tech-proposal → A/B方案对比
4. building-native-ui → SwiftUI实现
5. ios-simulator-deployment → 模拟器部署测试
```

---

## 智能索引系统

### 4层混合索引

```
用户查询
    ↓
并行匹配:
  ├─ 查询索引 (typicalQueries)
  ├─ 摘要索引 (capability/input/output)
  └─ 子块索引 (subCapabilities)
    ↓
最佳匹配
    ↓
返回: 完整 SKILL.md + references
```

### 进化追踪

- 每次任务后补充 typicalQueries
- 记录触发失败案例
- 更新 evolution.json
- 月度索引审计

---

## 文件结构

```
skill/
├── README.md (本文件)
├── INTEGRATION_ANALYSIS.md (整合分析)
├── skills-index.json (机器可读索引)
├── FIND_SKILL.md (快速查找)
├── _meta/
│   ├── SKILLS_REGISTRY.json (技能注册表)
│   ├── INDEXING_STRATEGY.md (索引策略)
│   └── evolution.json (进化追踪)
├── workflow-orchestrator/
├── ui-ux-design-system-generator/
│   ├── data/ (67样式/96配色/57字体)
│   └── scripts/ (search.py)
├── requirements-clarifier/
├── prd-generator/
├── architecture-designer/
├── tech-proposal/
├── testing-orchestrator/
├── quality-gate/
├── deployment-and-ops/
├── ios-simulator-deployment/
├── [其他39个技能目录...]
```

---

## 安装

```bash
# 克隆仓库
git clone https://github.com/wumiles09-eng/skill.git

# 复制到 Claude Code skills 目录
cp -r skill/* ~/.claude/skills/

# 完成！
```

---

## 贡献

欢迎贡献新技能或改进现有技能！

1. Fork 项目
2. 创建技能目录
3. 编写 SKILL.md
4. 更新 SKILLS_REGISTRY.json
5. 提交 Pull Request

---

## 致谢

- **Anthropic** - Claude Code 和 Agent Skills 平台
- **Google Labs** - Stitch AI 和官方 Stitch 技能
- **Cursor Hi Offer** - 智能索引系统和工作流编排
- **VerveFlow** - 7阶段SOP和渐进式交付方法论
- **社区贡献者** - 所有技能创作者

---

**Built with ❤️ by the Claude Code community**

[⬆ Back to Top](#skills-collection---完整研发流程版)

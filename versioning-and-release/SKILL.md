---
name: versioning-and-release
description: 版本管理（SemVer/Changelog/发布流程）。管理版本号、生成变更日志、执行发布流程。当准备发布新版本、需要管理版本号时使用。
---

# Versioning and Release - 版本管理

## 目标

规范版本号管理，自动化发布流程，生成清晰的变更日志。

## SemVer版本规范

### 版本号格式

```
MAJOR.MINOR.PATCH

示例: 1.2.3
- MAJOR: 1 - 主版本（不兼容的API变更）
- MINOR: 2 - 次版本（向后兼容的功能新增）
- PATCH: 3 - 补丁版本（向后兼容的bug修复）
```

### 版本号变更规则

| 变更类型 | 版本号变更 | 示例 |
|---------|-----------|------|
| 破坏性变更 | MAJOR+1, MINOR=0, PATCH=0 | 1.2.3 → 2.0.0 |
| 新功能（向后兼容） | MINOR+1, PATCH=0 | 1.2.3 → 1.3.0 |
| Bug修复 | PATCH+1 | 1.2.3 → 1.2.4 |

### 预发布版本

```
1.0.0-alpha.1  (内部测试版)
1.0.0-beta.1   (公开测试版)
1.0.0-rc.1     (候选发布版)
1.0.0          (正式发布版)
```

### 版本号判断流程

```markdown
## 版本号决策树

新功能
  ↓
是否破坏现有API？
  ├─ Yes → MAJOR版本升级
  └─ No → MINOR版本升级

Bug修复
  ↓
是否仅修复问题？
  ├─ Yes → PATCH版本升级
  └─ No → 评估是否为MINOR
```

## Changelog生成

### Changelog格式

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2026-01-29

### Added
- New feature: User authentication
- New endpoint: POST /api/users
- New dependency: passport.js

### Changed
- Updated React to 18.2.0
- Improved error messages

### Deprecated
- Old authentication endpoint (will be removed in v2.0.0)

### Removed
- Dropped support for Node.js 14

### Fixed
- Fixed login redirect loop
- Fixed memory leak in image processing

### Security
- Updated lodash to 4.17.21 (security fix)

## [1.1.0] - 2026-01-15
...

## [1.0.0] - 2026-01-01
...
```

### Changelog生成命令

```bash
# 自动生成（基于commit messages）
npm run changelog

# 或使用 conventional-changelog
npx conventional-changelog -p angular -i CHANGELOG.md -s

# 或使用 git-changelog
npx git-changelog -t v1.2.0
```

### Commit Message规范

```bash
# 格式
<type>(<scope>): <subject>

<body>

<footer>

# 类型
feat: 新功能
fix: Bug修复
docs: 文档更新
style: 代码格式（不影响功能）
refactor: 重构（不是新功能也不是修复）
perf: 性能优化
test: 测试相关
chore: 构建/工具相关

# 示例
feat(auth): add JWT authentication

- Add login endpoint
- Add token refresh logic
- Update documentation

Closes #123
```

## 发布流程

### 1. 发布前准备

```markdown
## Release Checklist

### 版本确定
- [ ] 确定版本号（MAJOR/MINOR/PATCH）
- [ ] 创建发布分支: release/v{version}

### 代码准备
- [ ] 合并所有功能分支
- [ ] 更新版本号
- [ ] 更新package.json/requirements.txt
- [ ] 更新依赖版本

### 测试验证
- [ ] 所有测试通过
- [ ] Staging环境验证
- [ ] 性能测试通过
- [ ] 安全扫描通过

### 文档准备
- [ ] 更新README
- [ ] 更新API文档
- [ ] 生成Changelog
- [ ] 准备Release Notes
```

### 2. 版本号更新

```bash
# Node.js项目
npm version major  # 1.0.0 → 2.0.0
npm version minor  # 1.0.0 → 1.1.0
npm version patch  # 1.0.0 → 1.0.1

# 或手动编辑
# package.json
{
  "version": "1.2.3"
}

# Git tag
git tag -a v1.2.3 -m "Release v1.2.3"
git push origin v1.2.3
```

### 3. 生成Changelog

```bash
# 自动生成
npm run changelog

# 或手动编辑 CHANGELOG.md
# 按照上面的格式填写变更内容
```

### 4. 构建发布

```bash
# 构建项目
npm run build

# 生成发布包
npm pack

# 或发布到npm
npm publish
```

### 5. 创建GitHub Release

```markdown
## GitHub Release模板

### 标题
Release v{version}

### 描述
## 🎉 新功能
- {新功能}

## 🐛 Bug修复
- {bug修复}

## 📝 升级指南
```bash
npm install {package}@{version}
```

## 📚 文档
- [文档链接]({url})

## ⚠️ 破坏性变更
- {破坏性变更说明}
```

### 6. 部署

```bash
# 部署到生产环境
# 参考 deployment-and-ops 技能

# 标记部署完成
# 在GitHub Release中添加部署备注
```

## 发布后工作

### 1. 通知

```markdown
## 发布通知

### 开发团队
- [ ] 发送团队通知
- [ ] 更新项目看板
- [ ] 标记相关issue已关闭

### 用户
- [ ] 发送Release Notes
- [ ] 更新应用商店（如适用）
- [ ] 发布到公告渠道

### 监控
- [ ] 设置监控告警
- [ ] 观察关键指标
- [ ] 准备快速响应
```

### 2. 清理

```markdown
## 发布后清理

### 代码清理
- [ ] 合并发布分支到main
- [ ] 删除发布分支
- [ ] 清理临时分支

### 工单清理
- [ ] 关闭已完成的issue
- [ ] 更新未完成issue的milestone
- [ ] 创建下一个版本的milestone

### 文档归档
- [ ] 归档发布记录
- [ ] 更新版本历史
- [ ] 记录经验教训
```

## 版本回退

### 回退场景

```markdown
## 需要回退的情况

### 立即回退
- [ ] 严重bug导致核心功能不可用
- [ ] 数据丢失或损坏
- [ ] 安全漏洞
- [ ] 性能严重退化

### 评估后回退
- [ ] 影响范围较小
- [ ] 有快速修复方案
- [ ] 回退风险可控
```

### 回退流程

```bash
# 1. 标记版本为deprecated
npm deprecate {package}@{version} "Critical bug, use {new-version}"

# 2. 发布新版本（可能是回退或修复）
npm version patch

# 3. 在Changelog中说明
## [1.2.1] - 2026-01-30

### Fixed
- Reverted broken feature from v1.2.0
- Addressed critical issue causing service outage

### Security
- Hotfix for critical security vulnerability
```

## 版本管理最佳实践

### 1. 自动化

```yaml
# .github/workflows/release.yml
name: Release

on:
  push:
    tags:
      - 'v*'

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Build
        run: npm run build
      - name: Test
        run: npm test
      - name: Release
        uses: softprops/action-gh-release@v1
```

### 2. 版本策略

| 策略 | 描述 | 适用场景 |
|------|------|---------|
| 时间基线 | 定期发布（如每月） | SaaS产品 |
| 功能基线 | 功能完成后发布 | MVP阶段 |
| 语义化版本 | 严格遵循SemVer | 库/SDK |
| 持续部署 | 每次提交自动发布 | Web应用 |

### 3. 分支策略

```
main (生产)
  ↑
  ├── release/v1.2 (发布分支)
  │     ↑
  │     ├── feature/a (功能分支)
  │     ├── feature/b
  │     └── hotfix/c (紧急修复)
  │
develop (开发)
```

---

**维护**: 根据发布经验持续优化
**来源**: Cursor Hi Offer versioning-and-release
**相关**: deployment-and-ops, changelog-generation

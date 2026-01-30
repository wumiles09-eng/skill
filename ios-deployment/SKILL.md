# iOS 模拟器部署技能

## 技能概述

本技能涵盖 iOS 应用在模拟器上的完整构建、安装、启动流程，以及常见问题的诊断和解决方案。

## 适用场景

- 开发阶段的快速迭代测试
- UI 界面验证
- 功能调试和问题排查
- 演示和验收

## 核心流程

### 1. 环境准备

#### 1.1 检查模拟器状态
```bash
# 列出所有可用模拟器
xcrun simctl list devices

# 检查特定模拟器状态
SIMULATOR_ID="72EF9E8B-194A-46DD-A6C4-4B41ECEE3B4A"
xcrun simctl list devices | grep "$SIMULATOR_ID"
```

#### 1.2 启动模拟器（如果未运行）
```bash
# 启动指定模拟器
xcrun simctl boot "$SIMULATOR_ID"

# 打开模拟器应用
open -a Simulator
```

### 2. 构建应用

#### 2.1 标准构建命令
```bash
cd /path/to/project
xcodebuild -project ProjectName.xcodeproj \
  -scheme SchemeName \
  -destination 'platform=iOS Simulator,id=SIMULATOR_ID' \
  -derivedDataPath build \
  build
```

**关键参数说明**：
- `-project`: 指定 .xcodeproj 文件
- `-scheme`: 指定构建方案（通常与项目名相同）
- `-destination`: 指定目标设备（模拟器 ID）
- `-derivedDataPath`: 指定构建输出目录（推荐使用相对路径 `build`）

#### 2.2 清理构建（遇到缓存问题时）
```bash
xcodebuild -project ProjectName.xcodeproj \
  -scheme SchemeName \
  -destination 'platform=iOS Simulator,id=SIMULATOR_ID' \
  -derivedDataPath build \
  clean build
```

#### 2.3 检查构建结果
```bash
# 构建成功会输出
** BUILD SUCCEEDED **

# 构建失败会输出
** BUILD FAILED **

# 查看具体错误
xcodebuild ... 2>&1 | grep "error:"
```

### 3. 安装应用

#### 3.1 完全卸载旧版本（推荐）
```bash
# 先终止运行中的应用
xcrun simctl terminate "$SIMULATOR_ID" com.company.appname

# 完全卸载应用（清除所有数据）
xcrun simctl uninstall "$SIMULATOR_ID" com.company.appname
```

**为什么要完全卸载？**
- 清除旧的 UserDefaults 数据
- 清除旧的缓存和状态
- 确保测试的是最新代码逻辑
- 避免"代码已更新但行为未变"的问题

#### 3.2 安装新版本
```bash
xcrun simctl install "$SIMULATOR_ID" build/Build/Products/Debug-iphonesimulator/AppName.app
```

### 4. 启动应用

```bash
xcrun simctl launch "$SIMULATOR_ID" com.company.appname
```

**成功输出示例**：
```
com.company.appname: 12345
```
（12345 是进程 ID）

### 5. 完整部署脚本示例

```bash
#!/bin/bash
set -e

# 配置
SIMULATOR_ID="72EF9E8B-194A-46DD-A6C4-4B41ECEE3B4A"
BUNDLE_ID="com.verveflow.app"
PROJECT_DIR="/Users/nancy/Documents/Projects/verveflow/ios/VerveFlowApp"
PROJECT_NAME="VerveFlowApp"

echo "🚀 开始部署 iOS 应用到模拟器..."

# 1. 检查并启动模拟器
echo "📱 检查模拟器状态..."
SIMULATOR_STATE=$(xcrun simctl list devices | grep "$SIMULATOR_ID" | grep -o "Booted\|Shutdown" || echo "Shutdown")
if [ "$SIMULATOR_STATE" != "Booted" ]; then
    echo "启动模拟器..."
    xcrun simctl boot "$SIMULATOR_ID"
    open -a Simulator
    sleep 3
fi

# 2. 构建应用
echo "🔨 构建应用..."
cd "$PROJECT_DIR"
xcodebuild -project "$PROJECT_NAME.xcodeproj" \
  -scheme "$PROJECT_NAME" \
  -destination "platform=iOS Simulator,id=$SIMULATOR_ID" \
  -derivedDataPath build \
  build

# 3. 完全卸载旧版本
echo "🗑️  卸载旧版本..."
xcrun simctl terminate "$SIMULATOR_ID" "$BUNDLE_ID" 2>/dev/null || true
xcrun simctl uninstall "$SIMULATOR_ID" "$BUNDLE_ID" 2>/dev/null || true

# 4. 安装新版本
echo "📦 安装新版本..."
xcrun simctl install "$SIMULATOR_ID" build/Build/Products/Debug-iphonesimulator/"$PROJECT_NAME.app"

# 5. 启动应用
echo "▶️  启动应用..."
xcrun simctl launch "$SIMULATOR_ID" "$BUNDLE_ID"

echo "✅ 部署完成！"
```

## 常见问题与解决方案

### 问题 1: 编译错误 - 缺失的设计系统定义

**症状**：
```
error: type 'Color' has no member 'bgSecondary'
error: type 'AppFont' has no member 'tabLabel'
```

**原因**：SwiftUI 代码引用了未定义的颜色或字体常量

**解决方案**：
1. 检查错误信息，识别缺失的定义
2. 在对应的设计系统文件中添加定义：
   - 颜色：`DesignSystem/Colors.swift`
   - 字体：`DesignSystem/Typography.swift`
   - 圆角：`DesignSystem/CornerRadius.swift`

**示例修复**：
```swift
// Colors.swift
static let bgSecondary = Color(hex: "F3F4F6")
static let textPrimary = Color(hex: "000000")

// Typography.swift
static let tabLabel = Font.system(size: 10, weight: .medium)
static let h2 = Font.system(size: 24, weight: .bold)
```

### 问题 2: API 端口不匹配

**症状**：
- 按钮点击无响应
- 显示 "Could not connect to the server"
- 网络请求超时

**原因**：iOS 应用配置的 API 端口与后端实际运行端口不一致

**诊断步骤**：
1. 检查后端服务器运行端口：
   ```bash
   lsof -ti:8080  # 检查 8080 端口是否被占用
   ```

2. 检查 iOS 应用配置：
   ```swift
   // AuthService.swift
   private let apiBaseURL = "http://localhost:8080/v1"  // 确认端口号
   ```

**解决方案**：
- 修改 iOS 应用的 `apiBaseURL` 匹配后端端口
- 或修改后端配置匹配 iOS 应用的端口

### 问题 3: JSON 解析失败 - 字段名不匹配

**症状**：
```
The data couldn't be read because it is missing.
```

**原因**：后端 API 返回 snake_case（如 `user_id`），iOS 期望 camelCase（如 `userId`）

**解决方案**：
在 Swift 模型中添加 `CodingKeys` 枚举：

```swift
struct AuthData: Codable {
    let userId: String
    let token: String
    let expiresAt: Int64
    
    enum CodingKeys: String, CodingKey {
        case userId = "user_id"
        case token
        case expiresAt = "expires_at"
    }
}
```

### 问题 4: 代码已更新但行为未变

**症状**：
- 修改了代码并重新构建
- 安装到模拟器后，应用行为仍然是旧的

**原因**：
- 应用的 UserDefaults 保留了旧状态
- 未完全卸载应用，只是覆盖安装

**解决方案**：
```bash
# 必须先完全卸载
xcrun simctl uninstall "$SIMULATOR_ID" "$BUNDLE_ID"

# 然后重新安装
xcrun simctl install "$SIMULATOR_ID" path/to/app
```

### 问题 5: 访客登录逻辑混乱

**症状**：
- 访客登录后被标记为"已登录用户"
- 访客和正式用户状态无法区分

**原因**：
- 只有一个 `isAuthenticated` 标志
- 访客和正式登录共用同一个 token 存储

**解决方案**：
引入独立的访客状态管理：

```swift
class AuthService: ObservableObject {
    @Published var isAuthenticated = false  // 正式登录
    @Published var isGuest = false          // 访客模式
    
    private let tokenKey = "verveflow_token"
    private let guestTokenKey = "verveflow_guest_token"
    
    func anonymousLogin() async {
        // 访客模式
        storeGuestToken(token)
        isGuest = true
        isAuthenticated = false
    }
    
    func emailLogin() async {
        // 正式登录
        storeToken(token)
        isAuthenticated = true
        isGuest = false
    }
}
```

界面判断逻辑：
```swift
if authService.isAuthenticated || authService.isGuest {
    MainTabView()  // 都可以进入主界面
} else {
    AuthView()     // 显示登录页
}
```

## 最佳实践

### 1. 迭代开发流程

**快速迭代**（代码小改动）：
```bash
# 只构建和安装，不卸载（保留状态）
xcodebuild ... build
xcrun simctl install "$SIMULATOR_ID" app.app
xcrun simctl launch "$SIMULATOR_ID" "$BUNDLE_ID"
```

**完整测试**（验证新功能或修复 bug）：
```bash
# 完全卸载后重新安装（清除状态）
xcrun simctl uninstall "$SIMULATOR_ID" "$BUNDLE_ID"
xcodebuild ... build
xcrun simctl install "$SIMULATOR_ID" app.app
xcrun simctl launch "$SIMULATOR_ID" "$BUNDLE_ID"
```

### 2. 构建优化

**使用 derivedDataPath**：
```bash
-derivedDataPath build  # 使用项目内的 build 目录
```

优点：
- 构建产物在项目目录下，易于查找
- 避免污染系统级 DerivedData 目录
- 便于清理和版本控制忽略

**并行构建**（加速）：
```bash
xcodebuild ... -jobs 8  # 使用 8 个并行任务
```

### 3. 错误诊断技巧

**查看详细构建日志**：
```bash
xcodebuild ... 2>&1 | tee build.log
```

**只看错误信息**：
```bash
xcodebuild ... 2>&1 | grep -E "(error:|warning:)"
```

**查看最后几行输出**：
```bash
xcodebuild ... 2>&1 | tail -20
```

### 4. 模拟器管理

**列出已安装的应用**：
```bash
xcrun simctl listapps "$SIMULATOR_ID"
```

**查看应用数据目录**：
```bash
xcrun simctl get_app_container "$SIMULATOR_ID" "$BUNDLE_ID" data
```

**重置模拟器**（清除所有数据）：
```bash
xcrun simctl erase "$SIMULATOR_ID"
```

## 集成到工作流

### Phase 3: 开发阶段

在 `skills/03-development/` 中调用本技能：

```markdown
## iOS 开发流程

1. 修改代码
2. 使用 `ios-simulator-deployment.md` 中的流程构建和部署
3. 在模拟器中测试
4. 如遇问题，参考"常见问题与解决方案"章节
```

### Phase 4: 测试阶段

在 `skills/04-testing/` 中调用本技能：

```markdown
## iOS 测试准备

1. 使用完全卸载流程清除旧状态
2. 安装最新构建版本
3. 执行测试用例
```

## 工具清单

| 工具 | 用途 | 示例 |
|------|------|------|
| `xcrun simctl list` | 列出设备和应用 | `xcrun simctl list devices` |
| `xcrun simctl boot` | 启动模拟器 | `xcrun simctl boot SIMULATOR_ID` |
| `xcodebuild` | 构建项目 | `xcodebuild -project ... build` |
| `xcrun simctl install` | 安装应用 | `xcrun simctl install SIMULATOR_ID app.app` |
| `xcrun simctl uninstall` | 卸载应用 | `xcrun simctl uninstall SIMULATOR_ID BUNDLE_ID` |
| `xcrun simctl launch` | 启动应用 | `xcrun simctl launch SIMULATOR_ID BUNDLE_ID` |
| `xcrun simctl terminate` | 终止应用 | `xcrun simctl terminate SIMULATOR_ID BUNDLE_ID` |
| `lsof` | 检查端口占用 | `lsof -ti:8080` |

## 检查清单

部署前检查：
- [ ] 模拟器已启动
- [ ] 后端服务器正在运行（如需要）
- [ ] API 端口配置正确
- [ ] 代码已保存并提交（可选）

部署后验证：
- [ ] 应用成功启动
- [ ] 界面显示正常
- [ ] 网络请求正常（无连接错误）
- [ ] 核心功能可用

问题排查：
- [ ] 检查构建日志中的错误
- [ ] 验证 API 端口是否匹配
- [ ] 确认是否完全卸载了旧版本
- [ ] 检查 JSON 字段名是否匹配

## 相关文档

- Apple 官方文档: [Simulator Help](https://developer.apple.com/documentation/xcode/running-your-app-in-simulator-or-on-a-device)
- Xcode Build Settings: [Build Settings Reference](https://developer.apple.com/documentation/xcode/build-settings-reference)
- 项目相关: `/ios/run-simulator.sh` - 项目专用启动脚本

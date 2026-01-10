---
name: visual-test
description: Visual testing workflow for frontend UI validation using Playwright MCP. Use when user requests to (1) Check UI appearance or visual rendering, (2) Verify responsive design across viewports, (3) Test layout and styling issues, (4) Capture screenshots for documentation, (5) Debug visual bugs, (6) Validate design implementation, or (7) Perform visual regression testing. Triggered by phrases like "check the UI", "how does it look", "test responsive design", "screenshot the page", "verify layout", "visual test", "check mobile view".
---

# Visual Test Workflow

Automated visual testing workflow for validating frontend UI using Playwright MCP. Provides a systematic approach to capture, analyze, and fix visual issues through an iterative feedback loop.

---

## Workflow Decision Tree

Follow this decision tree to determine the appropriate testing approach:

```
User requests visual testing
    │
    ├─→ Is dev server running? 
    │   ├─→ NO → Check with scripts/check_server.py
    │   │         └─→ If not found, prompt user to start server
    │   └─→ YES → Continue
    │
    ├─→ What type of test?
    │   │
    │   ├─→ "Check UI" / "How does it look"
    │   │   └─→ Basic Visual Test (Section 1)
    │   │
    │   ├─→ "Test responsive" / "Check mobile view"
    │   │   └─→ Responsive Test (Section 2)
    │   │
    │   ├─→ "Test interaction" / "Check form"
    │   │   └─→ Interaction Test (Section 3)
    │   │
    │   ├─→ "Check specific element" / "Debug layout issue"
    │   │   └─→ Targeted Test (Section 4)
    │   │
    │   └─→ "Full page test" / "Complete visual audit"
    │       └─→ Comprehensive Test (Section 5)
    │
    └─→ After capturing screenshots
        └─→ Analyze using references/visual-checklist.md
            └─→ Issues found?
                ├─→ YES → Report issues → Apply fixes → Re-test
                └─→ NO → Report success
```

---

## Section 1: Basic Visual Test

**When to use:** User wants a quick check of how a page looks.

**Steps:**

1. **Check environment**
```bash
python scripts/check_server.py
```

2. **Navigate to page**
```python
# Use Playwright MCP
playwright_navigate(url="http://localhost:3000/page-path")
```

3. **Capture screenshot (default desktop)**
```python
playwright_screenshot(name="page-desktop", width=1920, height=1080)
```

4. **Analyze screenshot** using `references/visual-checklist.md`
   - Check layout issues (alignment, spacing, overflow)
   - Check visual style (colors, typography, borders)
   - Check content (images, text, loading states)
   - Check interactive elements (buttons, forms, navigation)

5. **Report findings**
   - If issues found: Document with specific details (see Section 6)
   - If all good: Confirm "Visual test passed"

**Example:**
```
User: "Check how the homepage looks"

Actions:
1. python scripts/check_server.py
2. playwright_navigate(url="http://localhost:3000")
3. playwright_screenshot(name="homepage-desktop", width=1920, height=1080)
4. Analyze screenshot
5. Report: "Homepage looks good. Layout is clean, all elements visible, 
   no overflow issues. Navigation is properly aligned."
```

---

## Section 2: Responsive Test

**When to use:** User wants to verify responsive design across different devices.

**Critical viewports to test:**
- Mobile: 375x812 (iPhone 13 size)
- Tablet: 768x1024 (iPad size)
- Desktop: 1920x1080 (Full HD)

**Steps:**

1. **Check environment**
```bash
python scripts/check_server.py
```

2. **Navigate to page**
```python
playwright_navigate(url="http://localhost:3000/page-path")
```

3. **Capture multiple viewport sizes**
```python
# Mobile
playwright_screenshot(name="page-mobile", width=375, height=812)

# Tablet  
playwright_screenshot(name="page-tablet", width=768, height=1024)

# Desktop
playwright_screenshot(name="page-desktop", width=1920, height=1080)
```

4. **Analyze each screenshot** focusing on:
   - Content reflow and stacking
   - Navigation adaptation (hamburger menu on mobile)
   - Touch target sizes (minimum 44x44px on mobile)
   - Text readability without zooming
   - Image scaling
   - Spacing adjustments

5. **Compare across viewports** for consistency

6. **Report findings** by viewport

**Common responsive issues to check:**
- Horizontal scrollbar on mobile ❌
- Text too small to read on mobile (<14px) ❌
- Buttons too small to tap (<44x44px) ❌
- Images not scaling properly ❌
- Multi-column layout not collapsing on mobile ❌

**Example:**
```
User: "Test the login page on mobile and desktop"

Actions:
1. python scripts/check_server.py
2. playwright_navigate(url="http://localhost:3000/login")
3. playwright_screenshot(name="login-mobile", width=375, height=812)
4. playwright_screenshot(name="login-desktop", width=1920, height=1080)
5. Analyze both screenshots
6. Report:
   - Desktop: ✅ Clean layout, centered form, good spacing
   - Mobile: ❌ Issue found - "Remember me" checkbox too small (30x30px, 
     should be at least 44x44px for touch). Form inputs look good.
```

---

## Section 3: Interaction Test

**When to use:** User wants to test interactive elements, forms, or state changes.

**Steps:**

1. **Check environment**
```bash
python scripts/check_server.py
```

2. **Navigate to page**
```python
playwright_navigate(url="http://localhost:3000/page-path")
```

3. **Capture initial state**
```python
playwright_screenshot(name="initial-state")
```

4. **Perform interactions and capture each state**
```python
# Example: Form interaction
playwright_fill(selector="#email", value="test@example.com")
playwright_screenshot(name="email-filled")

playwright_fill(selector="#password", value="password123")
playwright_screenshot(name="form-complete")

playwright_click(selector="button[type='submit']")
playwright_screenshot(name="form-submitted")
```

5. **Analyze sequence** for:
   - Visual feedback on interactions
   - Error states (if applicable)
   - Success states
   - Loading states
   - Disabled states
   - Hover/focus states (if testable)

6. **Report findings** for each state

**Testing different states:**

```python
# Hover state (via JS)
playwright_evaluate(script="document.querySelector('.button').classList.add('hover')")
playwright_screenshot(name="button-hover")

# Focus state
playwright_click(selector="input#email")
playwright_screenshot(name="input-focused")

# Error state (trigger validation)
playwright_click(selector="button[type='submit']")  # Submit empty form
playwright_screenshot(name="form-errors")

# Disabled state
playwright_evaluate(script="document.querySelector('.submit-btn').disabled = true")
playwright_screenshot(name="button-disabled")
```

**Example:**
```
User: "Test the contact form interaction"

Actions:
1. python scripts/check_server.py
2. playwright_navigate(url="http://localhost:3000/contact")
3. playwright_screenshot(name="form-empty")
4. playwright_fill(selector="#name", value="John Doe")
5. playwright_screenshot(name="name-filled")
6. playwright_click(selector="button[type='submit']")
7. playwright_screenshot(name="validation-errors")
8. Report: "Form validation works - shows red border on required email 
   field. Error message 'Email is required' appears below field. Good UX."
```

---

## Section 4: Targeted Test

**When to use:** User wants to check a specific element or debug a known issue.

**Steps:**

1. **Identify target element**
   - Get specific selector from user
   - Determine which page contains the element

2. **Navigate and capture**
```python
playwright_navigate(url="http://localhost:3000/page-path")

# Option 1: Scroll to element first
playwright_evaluate(
    script="document.querySelector('.target-element').scrollIntoView()"
)
playwright_screenshot(name="element-view")

# Option 2: Get element dimensions for analysis
dimensions = playwright_evaluate(
    script="""
    const el = document.querySelector('.target-element');
    ({
        width: el.offsetWidth,
        height: el.offsetHeight,
        top: el.offsetTop,
        left: el.offsetLeft
    })
    """
)
```

3. **Analyze specific aspects**
   - Element positioning
   - Size and dimensions
   - Styling (colors, fonts, borders)
   - Visibility and z-index
   - Computed styles

4. **Report findings** with specific measurements

**Useful element analysis scripts:**

```python
# Get computed styles
playwright_evaluate(
    script="""
    const el = document.querySelector('.button');
    const styles = getComputedStyle(el);
    ({
        color: styles.color,
        backgroundColor: styles.backgroundColor,
        fontSize: styles.fontSize,
        padding: styles.padding,
        margin: styles.margin
    })
    """
)

# Check visibility
playwright_evaluate(
    script="document.querySelector('.element').offsetParent !== null"
)

# Get bounding box
playwright_evaluate(
    script="document.querySelector('.element').getBoundingClientRect()"
)
```

**Example:**
```
User: "The header logo looks weird, can you check it?"

Actions:
1. playwright_navigate(url="http://localhost:3000")
2. playwright_evaluate(script="document.querySelector('.logo').scrollIntoView()")
3. playwright_screenshot(name="header-logo")
4. dimensions = playwright_evaluate(
    script="document.querySelector('.logo').getBoundingClientRect()"
)
5. Analyze screenshot and dimensions
6. Report: "Logo is displaying at 250x80px but appears stretched. 
   Image aspect ratio should be 3:1 but it's showing as 3.125:1. 
   Recommend setting fixed dimensions or using object-fit: contain."
```

---

## Section 5: Comprehensive Test

**When to use:** User wants a full visual audit or regression test.

**Steps:**

1. **Define test scope**
   - List all critical pages
   - Determine viewport sizes
   - Identify key user flows

2. **Use test config template** from `assets/test-config-template.md`

3. **Execute systematic testing**

```python
# For each page
pages = ["/", "/login", "/dashboard", "/settings"]
viewports = [
    {"name": "mobile", "width": 375, "height": 812},
    {"name": "tablet", "width": 768, "height": 1024},
    {"name": "desktop", "width": 1920, "height": 1080}
]

for page in pages:
    playwright_navigate(url=f"http://localhost:3000{page}")
    
    for viewport in viewports:
        page_name = page.strip("/") or "homepage"
        screenshot_name = f"{page_name}-{viewport['name']}"
        
        playwright_screenshot(
            name=screenshot_name,
            width=viewport["width"],
            height=viewport["height"]
        )
```

4. **Analyze all screenshots** using `references/visual-checklist.md`

5. **Generate report** using template from `assets/test-config-template.md`

6. **Prioritize issues**
   - Critical: Broken layout, inaccessible features
   - High: Visual bugs on main pages, poor mobile UX
   - Medium: Minor spacing/alignment issues
   - Low: Nice-to-have improvements

**Example:**
```
User: "Run a full visual test on the app"

Actions:
1. Check server running
2. Test homepage (mobile, tablet, desktop)
3. Test login page (mobile, tablet, desktop)
4. Test dashboard (mobile, tablet, desktop)
5. Analyze all 9 screenshots
6. Generate report:
   - 3 critical issues (broken mobile nav, form overflow)
   - 2 high issues (image aspect ratios)
   - 5 medium issues (spacing inconsistencies)
   - Report detailed findings with screenshots
```

---

## Section 6: Analysis and Reporting

After capturing screenshots, perform thorough analysis:

### Analysis Process

1. **Load visual checklist** from `references/visual-checklist.md`

2. **Systematically review** each category:
   - Layout (positioning, spacing, overflow)
   - Visual style (colors, typography, shadows)
   - Responsive design (breakpoints, scaling)
   - Content (images, text, media)
   - Interactive elements (buttons, forms, links)

3. **Document issues** using this format:

```
Issue: [Brief description]
Location: [Page and element/coordinates]
Viewport: [Affected screen size(s)]
Severity: Critical | High | Medium | Low
Expected: [What should happen]
Actual: [What is happening]
Fix: [Suggested solution]
Screenshot: [Reference to specific screenshot]
```

### Reporting Guidelines

**When issues found:**
```markdown
## Visual Test Results

### Issues Identified

**Issue #1: Button text overflow**
- Location: Login page, "Sign Up" button in header
- Viewport: Mobile (375px)
- Severity: High
- Expected: Full text "Sign Up" visible
- Actual: Text shows "Sign U..."
- Fix: Reduce button font-size to 14px on mobile or increase padding
- Screenshot: login-mobile-375.png

**Issue #2: Image aspect ratio**
- Location: Homepage hero section
- Viewport: All
- Severity: Medium
- Expected: 16:9 aspect ratio maintained
- Actual: Image is stretched to 2:1
- Fix: Add `object-fit: cover` to hero image CSS
- Screenshot: homepage-desktop-1920.png
```

**When all tests pass:**
```markdown
## Visual Test Results ✅

All visual tests passed successfully.

### Tested
- Homepage: ✅ Desktop, Tablet, Mobile
- Login: ✅ Desktop, Tablet, Mobile
- Dashboard: ✅ Desktop, Tablet, Mobile

### Verified
- ✅ Layout consistent across viewports
- ✅ Responsive breakpoints working correctly
- ✅ All interactive elements functional
- ✅ Images loading and scaled properly
- ✅ Typography and colors consistent
- ✅ No overflow or alignment issues
```

---

## Fix and Verify Loop

After identifying issues, follow this loop:

1. **Document issue** (as shown above)

2. **Apply fix**
   - Modify CSS/HTML as needed
   - Test locally

3. **Re-capture screenshot**
```python
playwright_navigate(url="http://localhost:3000/page")
playwright_screenshot(name="page-after-fix", width=375, height=812)
```

4. **Compare before/after**
   - Verify issue is resolved
   - Check for regressions

5. **Update status**
   - Mark issue as FIXED
   - Document the fix applied

**Important:** Always re-test after applying fixes to ensure:
- The issue is actually resolved
- No new issues were introduced
- The fix works across all affected viewports

---

## Best Practices

### 1. Environment Setup
- Always verify dev server is running first
- Clear browser cache before testing if needed
- Ensure test data is loaded

### 2. Screenshot Naming
Use descriptive names:
```
{page}-{viewport}-{state}.png

Examples:
- homepage-desktop-default.png
- login-mobile-filled.png
- dashboard-tablet-loading.png
```

### 3. Viewport Selection
Focus on these critical breakpoints:
- **Mobile**: 375px (most common)
- **Tablet**: 768px (iPad portrait)
- **Desktop**: 1920px (Full HD)

Test additional sizes only if:
- Specific device targeting required
- Known issues at specific breakpoints
- Client requirements mandate it

### 4. Analysis Depth
Match analysis depth to user needs:
- Quick check: Layout + critical issues only
- Standard test: Full checklist
- Comprehensive audit: Multiple pages + all viewports + full checklist

### 5. Issue Prioritization
```
Critical: Blocks core functionality
  - Broken layout making content inaccessible
  - Form cannot be submitted
  - Navigation completely broken

High: Major UX problems
  - Poor mobile experience
  - Important text cut off
  - Images missing/broken

Medium: Noticeable but not blocking
  - Spacing inconsistencies
  - Minor alignment issues
  - Non-critical visual glitches

Low: Polish and improvements
  - Subtle color variations
  - Minor typography tweaks
  - Nice-to-have enhancements
```

---

## Bundled Resources

### Scripts (`scripts/`)

**`check_server.py`**
Environment checker that verifies development server is running.

**Usage:**
```bash
python scripts/check_server.py
```

**Output:**
- Lists all running dev servers on common ports (3000, 5173, 8080, etc.)
- Shows process names and URLs
- Exits with error if no server found

**When to use:**
- Before every visual test session
- When user reports "screenshots are blank"
- When debugging connection issues

### References (`references/`)

**`visual-checklist.md`**
Comprehensive checklist for analyzing UI screenshots.

**Read when:**
- Performing detailed visual analysis
- User asks "what to look for"
- Need to ensure thorough coverage
- Creating test reports

**Contains:**
- Layout issue checklist
- Visual style checklist
- Responsive design checklist
- Content validation checklist
- Accessibility visual checks
- Common bug patterns

**`playwright-mcp-guide.md`**
Complete reference for Playwright MCP tools and patterns.

**Read when:**
- Need specific tool syntax
- Planning test workflow
- Learning available capabilities
- Troubleshooting MCP issues

**Contains:**
- All available Playwright MCP tools
- Common viewport sizes
- Testing workflow patterns
- Best practices
- Common issues and solutions
- Quick reference commands

### Assets (`assets/`)

**`test-config-template.md`**
Templates for test configuration and reporting.

**Use when:**
- Setting up comprehensive test
- Creating test reports
- Need standardized documentation
- Planning test coverage

**Contains:**
- YAML test configuration template
- Custom checklist template
- Screenshot naming conventions
- Test report template
- Environment setup checklist

---

## Common Scenarios

### Scenario 1: Quick Homepage Check
```
User: "How does the homepage look?"

Response:
1. python scripts/check_server.py
2. playwright_navigate(url="http://localhost:3000")
3. playwright_screenshot(name="homepage", width=1920, height=1080)
4. Analyze using checklist
5. Report findings
```

### Scenario 2: Mobile Responsiveness
```
User: "Is the site mobile-friendly?"

Response:
1. Check server
2. Navigate to key pages
3. Screenshot at 375px width for each page
4. Analyze for mobile UX issues
5. Report mobile-specific findings
```

### Scenario 3: Form Validation
```
User: "Test the signup form validation"

Response:
1. Navigate to signup page
2. Screenshot empty state
3. Fill partial data
4. Click submit to trigger validation
5. Screenshot error states
6. Analyze error message visibility and clarity
7. Report findings
```

### Scenario 4: Debug Specific Issue
```
User: "The header is weird on tablet"

Response:
1. Navigate to page
2. Screenshot at 768px
3. Inspect header element dimensions
4. Compare with desktop/mobile
5. Identify specific issue
6. Suggest fix
7. Verify fix with new screenshot
```

---

## Troubleshooting

### Screenshots are blank/white
**Problem**: Page hasn't loaded
**Solution**: 
```python
playwright_navigate(url="http://localhost:3000")
playwright_evaluate(script="new Promise(r => setTimeout(r, 2000))")
playwright_screenshot()
```

### Element not visible in screenshot
**Problem**: Element is below fold
**Solution**:
```python
playwright_evaluate(
    script="document.querySelector('.element').scrollIntoView()"
)
playwright_screenshot()
```

### Can't interact with element
**Problem**: Element selector is wrong or element is hidden
**Solution**:
```python
# Check if element exists
exists = playwright_evaluate(
    script="document.querySelector('.element') !== null"
)
# Get all matching selectors
playwright_evaluate(
    script="document.querySelectorAll('.element').length"
)
```

### Hover states don't show
**Problem**: Playwright doesn't trigger CSS :hover
**Solution**:
```python
# Add hover class via JS
playwright_evaluate(
    script="document.querySelector('.button').classList.add('hover')"
)
playwright_screenshot()
```

---

## Success Criteria

A successful visual test session includes:

✅ Development server verified running
✅ Screenshots captured at appropriate viewports
✅ Systematic analysis using checklist
✅ Clear documentation of any issues found
✅ Specific, actionable fix suggestions
✅ Verification screenshots after fixes (if applicable)
✅ Final status report (PASS/FAIL with details)

---

## Quick Reference

```bash
# Check server
python scripts/check_server.py

# Basic test pattern
playwright_navigate → screenshot → analyze → report

# Responsive test pattern  
navigate → screenshot(mobile) → screenshot(tablet) → screenshot(desktop) → analyze

# Fix loop
screenshot(before) → apply fix → screenshot(after) → verify

# Common viewports
Mobile:  375 x 812
Tablet:  768 x 1024  
Desktop: 1920 x 1080
```

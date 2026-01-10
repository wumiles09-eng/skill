# Playwright MCP Reference

Quick reference for using Playwright MCP tools for visual testing.

---

## Available Tools

### 1. playwright_navigate
Navigate to a URL

```python
playwright_navigate(url="http://localhost:3000")
playwright_navigate(url="http://localhost:3000/login")
```

**Parameters:**
- `url` (required): The URL to navigate to

**Use when:**
- Starting a new test session
- Navigating to a different page
- Refreshing the current page

---

### 2. playwright_screenshot
Capture a screenshot of the current page

```python
# Full page screenshot
playwright_screenshot(name="homepage", width=1920, height=1080)

# Mobile viewport
playwright_screenshot(name="mobile-view", width=375, height=812)

# Tablet viewport
playwright_screenshot(name="tablet-view", width=768, height=1024)
```

**Parameters:**
- `name` (optional): Name for the screenshot file
- `width` (optional): Viewport width in pixels (default: 1280)
- `height` (optional): Viewport height in pixels (default: 720)

**Common Viewport Sizes:**

**Mobile:**
- iPhone SE: 375 x 667
- iPhone 12/13/14: 390 x 844
- iPhone 12/13/14 Pro Max: 428 x 926
- Android (typical): 360 x 740

**Tablet:**
- iPad: 768 x 1024
- iPad Pro 11": 834 x 1194
- iPad Pro 12.9": 1024 x 1366

**Desktop:**
- Laptop: 1366 x 768
- Desktop HD: 1920 x 1080
- Desktop 2K: 2560 x 1440
- Desktop 4K: 3840 x 2160

---

### 3. playwright_click
Click an element on the page

```python
playwright_click(selector="button.submit")
playwright_click(selector="#login-button")
playwright_click(selector="[data-testid='submit']")
```

**Parameters:**
- `selector` (required): CSS selector for the element to click

**Common Selectors:**
- By ID: `#element-id`
- By class: `.class-name`
- By attribute: `[data-testid='value']`
- By tag: `button`, `a`, `input`
- Complex: `nav > ul > li:first-child`

---

### 4. playwright_fill
Fill in a form field

```python
playwright_fill(selector="input[name='email']", value="user@example.com")
playwright_fill(selector="#password", value="secret123")
```

**Parameters:**
- `selector` (required): CSS selector for the input element
- `value` (required): Text to fill in

---

### 5. playwright_evaluate
Execute JavaScript in the page context

```python
# Get element dimensions
playwright_evaluate(script="document.querySelector('.header').offsetHeight")

# Scroll to bottom
playwright_evaluate(script="window.scrollTo(0, document.body.scrollHeight)")

# Get computed styles
playwright_evaluate(script="getComputedStyle(document.querySelector('.button')).backgroundColor")
```

**Parameters:**
- `script` (required): JavaScript code to execute

**Common Use Cases:**
- Get element dimensions
- Scroll page
- Check visibility
- Get computed styles
- Trigger custom events

---

## Testing Workflow Patterns

### Pattern 1: Basic Page Test

```
1. playwright_navigate(url="http://localhost:3000")
2. playwright_screenshot(name="initial", width=1920, height=1080)
3. Analyze screenshot
4. Report findings
```

### Pattern 2: Responsive Test

```
1. playwright_navigate(url="http://localhost:3000")

2. # Desktop
   playwright_screenshot(name="desktop", width=1920, height=1080)
   
3. # Tablet
   playwright_screenshot(name="tablet", width=768, height=1024)
   
4. # Mobile
   playwright_screenshot(name="mobile", width=375, height=812)
   
5. Analyze all screenshots for responsive issues
```

### Pattern 3: Interaction Test

```
1. playwright_navigate(url="http://localhost:3000/form")
2. playwright_screenshot(name="form-initial")
3. playwright_fill(selector="#email", value="test@example.com")
4. playwright_screenshot(name="form-filled")
5. playwright_click(selector="button[type='submit']")
6. playwright_screenshot(name="form-submitted")
7. Analyze sequence for interaction feedback
```

### Pattern 4: Scroll Test

```
1. playwright_navigate(url="http://localhost:3000")
2. playwright_screenshot(name="above-fold")
3. playwright_evaluate(script="window.scrollTo(0, 1000)")
4. playwright_screenshot(name="mid-page")
5. playwright_evaluate(script="window.scrollTo(0, document.body.scrollHeight)")
6. playwright_screenshot(name="bottom")
7. Analyze for sticky elements, lazy loading
```

### Pattern 5: State Test

```
1. playwright_navigate(url="http://localhost:3000")
2. playwright_screenshot(name="default-state")
3. # Hover state (trigger via JS)
   playwright_evaluate(script="document.querySelector('.button').classList.add('hover')")
4. playwright_screenshot(name="hover-state")
5. # Active/clicked state
   playwright_evaluate(script="document.querySelector('.button').classList.add('active')")
6. playwright_screenshot(name="active-state")
```

---

## Best Practices

### 1. Always Check Server First
Before any visual test, verify the development server is running:
```bash
python scripts/check_server.py
```

### 2. Use Consistent Naming
```python
# Good
playwright_screenshot(name="homepage-desktop-1920")
playwright_screenshot(name="login-mobile-375")

# Bad
playwright_screenshot(name="screenshot1")
playwright_screenshot(name="test")
```

### 3. Test Critical Breakpoints
Focus on these breakpoints for responsive tests:
- 375px (mobile)
- 768px (tablet)
- 1280px or 1920px (desktop)

### 4. Capture Before and After Changes
```python
# Before fix
playwright_screenshot(name="button-issue-before")
# Apply fix
# After fix
playwright_screenshot(name="button-issue-after")
```

### 5. Use Descriptive Analysis
When analyzing screenshots, be specific:
- ❌ "Button looks wrong"
- ✅ "Button text is cut off at 375px width, showing 'Sign U...' instead of 'Sign Up'"

---

## Common Issues and Solutions

### Issue: Screenshot is blank/white
**Cause**: Page hasn't fully loaded
**Solution**: 
```python
playwright_navigate(url="http://localhost:3000")
# Wait a moment before screenshot
playwright_evaluate(script="new Promise(r => setTimeout(r, 1000))")
playwright_screenshot()
```

### Issue: Elements not visible
**Cause**: Need to scroll to element
**Solution**:
```python
playwright_evaluate(script="document.querySelector('.footer').scrollIntoView()")
playwright_screenshot()
```

### Issue: Modal/dialog not captured
**Cause**: Modal opens on interaction
**Solution**:
```python
playwright_click(selector=".open-modal-button")
# Brief wait for animation
playwright_evaluate(script="new Promise(r => setTimeout(r, 300))")
playwright_screenshot(name="modal-open")
```

### Issue: Hover state not showing
**Cause**: Playwright doesn't automatically trigger CSS :hover
**Solution**:
```python
# Use JavaScript to add hover class
playwright_evaluate(script="document.querySelector('.button').classList.add('hover')")
playwright_screenshot()
```

---

## Testing Checklist

Before each visual test session:
- [ ] Development server is running
- [ ] Page loads without console errors
- [ ] Know which viewport sizes to test
- [ ] Have specific visual goals in mind

During testing:
- [ ] Start with default/desktop view
- [ ] Test responsive breakpoints
- [ ] Check interactive states
- [ ] Document all issues found

After testing:
- [ ] Screenshots are named clearly
- [ ] All issues are documented
- [ ] Fixes are verified with new screenshots

---

## Quick Reference Commands

```bash
# Check if server is running
python scripts/check_server.py

# Common viewport sizes
Mobile:  375 x 812
Tablet:  768 x 1024
Desktop: 1920 x 1080

# Common test pattern
1. Navigate
2. Screenshot (multiple viewports)
3. Analyze
4. Fix if needed
5. Re-screenshot to verify
```

# Visual Test Configuration Template

Use this template to configure your visual testing sessions.

---

## Test Configuration

```yaml
# visual-test-config.yaml

project_name: "My Project"
base_url: "http://localhost:3000"

# Viewports to test
viewports:
  mobile:
    - name: "iPhone 13"
      width: 390
      height: 844
    - name: "iPhone SE"
      width: 375
      height: 667
  tablet:
    - name: "iPad"
      width: 768
      height: 1024
    - name: "iPad Pro"
      width: 1024
      height: 1366
  desktop:
    - name: "Laptop"
      width: 1366
      height: 768
    - name: "Desktop HD"
      width: 1920
      height: 1080

# Pages to test
pages:
  - path: "/"
    name: "homepage"
    critical: true
  - path: "/login"
    name: "login"
    critical: true
  - path: "/dashboard"
    name: "dashboard"
    critical: false

# Visual checks to perform
checks:
  layout:
    - alignment
    - spacing
    - overflow
  style:
    - colors
    - typography
    - borders
  responsive:
    - breakpoints
    - touch_targets
    - media_queries
  content:
    - images
    - text
    - loading_states
  interactive:
    - buttons
    - forms
    - navigation

# Test scenarios
scenarios:
  - name: "Homepage load"
    steps:
      - navigate: "/"
      - screenshot: "homepage-default"
      - scroll_to: "footer"
      - screenshot: "homepage-footer"
  
  - name: "Login form"
    steps:
      - navigate: "/login"
      - screenshot: "login-empty"
      - fill: { selector: "#email", value: "test@example.com" }
      - fill: { selector: "#password", value: "password" }
      - screenshot: "login-filled"
      - click: "button[type='submit']"
      - screenshot: "login-submitted"
```

---

## Custom Test Checklist

Create a custom checklist for your project:

```markdown
# My Project Visual Test Checklist

## Critical Pages
- [ ] Homepage loads correctly on all viewports
- [ ] Login page is accessible and functional
- [ ] Dashboard displays user data properly

## Brand Consistency
- [ ] Primary color: #007bff
- [ ] Secondary color: #6c757d
- [ ] Font family: 'Inter', sans-serif
- [ ] Logo appears correctly
- [ ] Brand guidelines followed

## Responsive Breakpoints
- [ ] Mobile (375px): Navigation collapses, content stacks
- [ ] Tablet (768px): Sidebar visible, content flows
- [ ] Desktop (1920px): Full layout, all features visible

## Interactive Elements
- [ ] All buttons have hover states
- [ ] Form validation shows inline errors
- [ ] Modal dialogs center correctly
- [ ] Dropdowns open in right direction

## Performance Visual Checks
- [ ] Images load without layout shift
- [ ] Lazy loading works for below-fold images
- [ ] Loading spinners visible during data fetch
- [ ] Smooth transitions (no janky animations)
```

---

## Screenshot Naming Convention

Use this format for screenshot names:

```
{page}-{viewport}-{state}-{timestamp}.png

Examples:
- homepage-desktop-default.png
- login-mobile-filled.png
- dashboard-tablet-loading.png
- header-desktop-scrolled.png
```

---

## Test Report Template

```markdown
# Visual Test Report

**Date**: YYYY-MM-DD
**Tester**: [Name]
**Project**: [Project Name]
**URL**: http://localhost:3000

## Summary
- Pages Tested: X
- Issues Found: Y
- Critical Issues: Z
- Status: PASS / FAIL / NEEDS REVIEW

## Test Coverage

### Desktop (1920x1080)
- [x] Homepage
- [x] Login
- [ ] Dashboard
- [ ] Settings

### Tablet (768x1024)
- [x] Homepage
- [ ] Login
- [ ] Dashboard
- [ ] Settings

### Mobile (375x812)
- [x] Homepage
- [ ] Login
- [ ] Dashboard
- [ ] Settings

## Issues Found

### Issue #1: Button text overflow on mobile
- **Page**: Login
- **Viewport**: 375px
- **Severity**: High
- **Description**: "Sign Up" button text shows as "Sign U..."
- **Screenshot**: login-mobile-button-issue.png
- **Expected**: Full text visible
- **Fix**: Reduce padding or font size on mobile
- **Status**: FIXED

### Issue #2: Image aspect ratio incorrect
- **Page**: Homepage
- **Viewport**: All
- **Severity**: Medium
- **Description**: Hero image is stretched
- **Screenshot**: homepage-hero-stretched.png
- **Expected**: 16:9 aspect ratio maintained
- **Fix**: Add object-fit: cover to CSS
- **Status**: PENDING

## Passed Tests
- ✅ Navigation responsive on all viewports
- ✅ Form labels visible and aligned
- ✅ Footer content properly spaced
- ✅ Color contrast meets WCAG AA

## Recommendations
1. Add loading skeleton for slow image loads
2. Increase touch target size on mobile (min 44x44px)
3. Add focus indicators for keyboard navigation
4. Test dark mode (if applicable)

## Next Steps
1. Fix critical issues (#1)
2. Re-test on mobile after fixes
3. Test on real devices
4. Cross-browser testing (Safari, Firefox)
```

---

## Environment Setup Checklist

Before starting visual tests:

```markdown
## Environment Setup

- [ ] Node.js installed (v16+)
- [ ] Development server running
- [ ] Playwright MCP installed and configured
- [ ] Test data/fixtures ready
- [ ] Browser cache cleared (for clean test)
- [ ] All features deployed to test environment

## Testing Tools Ready

- [ ] Screen capture tool working
- [ ] Visual diff tool (if using)
- [ ] Annotation tool for marking issues
- [ ] Browser DevTools accessible

## Test Data

- [ ] Test user accounts created
- [ ] Sample content loaded
- [ ] Mock API responses configured
- [ ] Database seeded with test data
```

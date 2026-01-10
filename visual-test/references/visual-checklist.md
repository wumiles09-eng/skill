# Visual Testing Checklist

A comprehensive checklist for analyzing UI screenshots and identifying common visual issues.

---

## 📐 Layout Issues

### Positioning & Alignment
- [ ] Elements are properly aligned (left, center, right, justified)
- [ ] Vertical rhythm is consistent
- [ ] Grid alignment is maintained
- [ ] Absolute/fixed positioned elements don't overlap content
- [ ] Sticky headers/footers work correctly at different scroll positions

### Spacing & Margins
- [ ] Consistent spacing between elements (8px, 16px, 24px, 32px grid)
- [ ] Adequate padding around content
- [ ] No unexpected margins collapsing
- [ ] White space is balanced and intentional
- [ ] Negative space improves readability

### Overflow & Boundaries
- [ ] No horizontal scrollbar on desktop
- [ ] Content doesn't overflow containers
- [ ] Long text is properly truncated with ellipsis
- [ ] Images stay within bounds
- [ ] Modals/dialogs are properly centered and contained

---

## 🎨 Visual Style Issues

### Colors
- [ ] Color contrast meets WCAG AA standards (4.5:1 for normal text)
- [ ] Brand colors are applied consistently
- [ ] Hover/active states have visible color changes
- [ ] Error states use appropriate colors (red/orange)
- [ ] Success states use appropriate colors (green)
- [ ] No color clashing or poor combinations

### Typography
- [ ] Font family is applied correctly
- [ ] Font sizes follow a scale (12px, 14px, 16px, 18px, 24px, 32px, 48px)
- [ ] Line height is comfortable (1.5-1.6 for body text)
- [ ] Letter spacing is appropriate
- [ ] Font weights are used consistently (400, 500, 600, 700)
- [ ] No text is illegible or too small (<14px)
- [ ] Headings have proper hierarchy (h1 > h2 > h3)

### Borders & Shadows
- [ ] Border widths are consistent
- [ ] Border radius is uniform across similar elements
- [ ] Shadows are subtle and enhance depth
- [ ] No double borders or unexpected outlines
- [ ] Focus indicators are visible but not distracting

---

## 📱 Responsive Design

### Viewport Breakpoints (Common)
- **Mobile**: 375px, 414px (iPhone sizes)
- **Tablet**: 768px, 1024px (iPad sizes)
- **Desktop**: 1280px, 1440px, 1920px

### Mobile-Specific Checks
- [ ] Touch targets are at least 44x44px
- [ ] Text is readable without zooming
- [ ] Horizontal scroll is intentional or absent
- [ ] Navigation collapses to hamburger menu
- [ ] Images scale proportionally
- [ ] Spacing is adequate for finger taps
- [ ] Forms are easy to fill on mobile

### Tablet-Specific Checks
- [ ] Layout adapts between mobile and desktop
- [ ] Touch and mouse interactions both work
- [ ] Content utilizes available space effectively
- [ ] Navigation is accessible and clear

### Desktop-Specific Checks
- [ ] Content doesn't stretch too wide (max-width: 1200-1440px)
- [ ] Hover states are visible and smooth
- [ ] Multi-column layouts work properly
- [ ] Sidebar navigation is accessible
- [ ] Large screens don't have excessive white space

---

## 🖼️ Content & Media

### Images
- [ ] Images load successfully (no broken image icons)
- [ ] Images have appropriate alt text
- [ ] Aspect ratios are maintained
- [ ] Images are not pixelated or blurry
- [ ] Lazy loading works (for below-fold images)
- [ ] Background images are positioned correctly
- [ ] Icons are aligned with text

### Text Content
- [ ] No Lorem Ipsum placeholder text (unless intentional)
- [ ] Text is not cut off mid-sentence
- [ ] Line breaks are natural (no orphans or widows)
- [ ] List items are properly formatted
- [ ] Quotes and special characters render correctly
- [ ] Numbers and dates are formatted consistently

### Loading States
- [ ] Loading spinners are visible and centered
- [ ] Skeleton screens match final layout
- [ ] Progress bars update smoothly
- [ ] Error states provide helpful messages
- [ ] Empty states are friendly and actionable

---

## ⚡ Interactive Elements

### Buttons & Links
- [ ] Buttons have clear labels
- [ ] Primary vs secondary buttons are distinguishable
- [ ] Disabled buttons look disabled
- [ ] Button sizes are appropriate for their importance
- [ ] Links are underlined or clearly distinguishable
- [ ] Visited links have different styling

### Forms
- [ ] Input fields have clear labels
- [ ] Placeholder text is visible but distinct from input
- [ ] Required fields are marked
- [ ] Error messages appear near relevant fields
- [ ] Success states are visible
- [ ] Checkboxes and radios are properly sized
- [ ] Select dropdowns are styled consistently

### Navigation
- [ ] Current page is highlighted in navigation
- [ ] Breadcrumbs show correct path
- [ ] Dropdown menus open in the right direction
- [ ] Mobile menu opens and closes smoothly
- [ ] Navigation is accessible via keyboard

---

## 🌐 Cross-Browser Compatibility

Common issues to check:
- [ ] Flexbox/Grid layouts render correctly
- [ ] Custom fonts load properly
- [ ] CSS animations work smoothly
- [ ] Box shadows appear as expected
- [ ] Border radius renders consistently
- [ ] Transforms (rotate, scale) work
- [ ] Position: sticky is supported
- [ ] CSS variables are applied

---

## ♿ Accessibility (Visual Aspects)

### Visibility
- [ ] Focus indicators are visible
- [ ] Skip links are available
- [ ] Color is not the only indicator (use icons + color)
- [ ] Interactive elements are distinguishable

### Readability
- [ ] Text contrast meets WCAG standards
- [ ] Font size is at least 16px for body text
- [ ] Line length is comfortable (50-75 characters)
- [ ] Adequate line spacing (at least 1.5)

---

## 🎯 Common Visual Bugs

### Layout Bugs
- **Content jump**: Page jumps when lazy-loaded content appears
- **Z-index issues**: Elements overlap incorrectly
- **Flexbox wrapping**: Items wrap unexpectedly
- **Fixed positioning**: Fixed elements don't stay in place

### Styling Bugs
- **CSS not loading**: Unstyled content visible
- **Specificity issues**: Styles not applying due to CSS specificity
- **Font flash**: Flash of unstyled text (FOUT)
- **Color inconsistency**: Different shades of the same color

### Responsive Bugs
- **Media query gaps**: Styles break between breakpoints
- **Image stretching**: Images distort on resize
- **Horizontal scroll**: Unwanted horizontal scrollbar
- **Touch targets**: Elements too small on mobile

---

## 📏 Quick Visual Tests

### The Squint Test
Blur your eyes or zoom out. Can you still:
- Identify main sections?
- See visual hierarchy?
- Distinguish interactive elements?
- Follow the content flow?

### The 5-Second Test
In 5 seconds, can a user:
- Understand what the page is for?
- Find the main call-to-action?
- Identify where to start?

### The Resize Test
Resize the browser window from mobile to desktop:
- Does layout adapt smoothly?
- Are all breakpoints covered?
- Does content reflow naturally?

---

## 📝 Reporting Format

When reporting visual issues, use this format:

**Issue**: [Brief description]
**Location**: [Specific element or coordinates]
**Expected**: [What should happen]
**Actual**: [What is happening]
**Severity**: Critical | High | Medium | Low
**Screenshot**: [Annotated if possible]

**Example:**
- **Issue**: Button text is cut off on mobile
- **Location**: "Sign Up" button in header, 375px viewport
- **Expected**: Full text "Sign Up" visible
- **Actual**: Text shows "Sign U..."
- **Severity**: High
- **Fix**: Reduce font size or button padding on mobile

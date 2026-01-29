---
name: audit-website
description: Comprehensive website audit covering performance, accessibility, SEO, security, and user experience. Use when reviewing websites for overall quality, identifying issues, and providing actionable improvement recommendations.
---

# Website Audit Skill

This skill performs comprehensive website audits across multiple dimensions.

## Audit Dimensions

### 1. Performance Audit

#### Core Web Vitals
- [ ] LCP (Largest Contentful Paint) < 2.5s
- [ ] FID (First Input Delay) < 100ms
- [ ] CLS (Cumulative Layout Shift) < 0.1

#### Load Time Metrics
- [ ] Time to First Byte (TTFB) < 600ms
- [ ] First Contentful Paint (FCP) < 1.8s
- [ ] Time to Interactive (TTI) < 3.8s
- [ ] Total page load < 3 seconds

#### Optimization Checklist
- [ ] Images optimized and compressed
- [ ] Minified CSS and JavaScript
- [ ] Browser caching enabled
- [ ] CDN usage
- [ ] Lazy loading implemented
- [ ] Code splitting for JavaScript
- [ ] Critical CSS inlined
- [ ] Font loading optimized
- [ ] Reduced third-party scripts

### 2. Accessibility Audit (WCAG 2.1 AA)

#### Perceivable
- [ ] Alt text for all images
- [ ] Captions for video content
- [ ] Text contrast ratio ≥ 4.5:1
- [ ] Resizable text (200% zoom)
- [ ] Seizure-safe (no flashing content)

#### Operable
- [ ] Keyboard navigable
- [ ] Focus indicators visible
- [ ] Skip navigation links
- [ ] No keyboard traps
- [ ] Sufficient time limits

#### Understandable
- [ ] Page language declared
- [ ] Consistent navigation
- [ ] Error identification and suggestions
- [ ] Clear labels and instructions

#### Robust
- [ ] Valid HTML/CSS
- [ ] ARIA labels where needed
- [ ] Semantic HTML structure
- [ ] Screen reader compatible

### 3. SEO Audit

#### Technical SEO
- [ ] XML sitemap present
- [ ] Robots.txt configured
- [ ] Clean URL structure
- [ ] HTTPS enabled
- [ ] Canonical tags
- [ ] No broken links
- [ ] Fast page load speed

#### On-Page SEO
- [ ] Unique title tags (50-60 chars)
- [ ] Meta descriptions (150-160 chars)
- [ ] Proper heading hierarchy (H1-H6)
- [ ] Mobile-friendly
- [ ] Structured data
- [ ] Internal linking
- [ ] Image alt text

### 4. Security Audit

#### Essential Security
- [ ] HTTPS enabled
- [ ] SSL certificate valid
- [ ] Secure headers configured
  - X-Frame-Options
  - X-Content-Type-Options
  - Strict-Transport-Security
  - Content-Security-Policy
- [ ] No mixed content
- [ ] Input validation
- [ ] Output encoding
- [ ] Authentication secure
- [ ] Sensitive data encrypted

### 5. User Experience Audit

#### Design & Layout
- [ ] Consistent visual design
- [ ] Clear visual hierarchy
- [ ] Adequate whitespace
- [ ] Responsive on all devices
- [ ] Touch-friendly (44x44px min)
- [ ] Loading states visible
- [ ] Error messages helpful

#### Navigation & Flow
- [ ] Clear navigation menu
- [ ] Breadcrumbs (if deep site)
- [ ] Search functionality
- [ ] Logical page flow
- [ ] Clear CTAs
- [ ] Easy to find important info

#### Content Quality
- [ ] Grammar and spelling correct
- [ ] Content up-to-date
- [ ] Scannable formatting
- [ ] Multimedia works properly
- [ ] No broken links
- [ ] Contact info accessible

### 6. Code Quality Audit

#### HTML
- [ ] Valid HTML5
- [ ] Semantic elements
- [ ] Proper meta tags
- [ ] ARIA attributes where needed

#### CSS
- [ ] No inline styles (mostly)
- [ ] Organized structure
- [ ] Mobile-first responsive
- [ ] Consistent naming

#### JavaScript
- [ ] No console errors
- [ ] Progressive enhancement
- [ ] Error handling
- [ ] Performance optimized

## Scoring System

### Critical Issues (0-25 points)
- Security vulnerabilities
- Site completely broken
- No mobile version
- Extremely slow load times

### High Priority Issues (26-50 points)
- Poor Core Web Vitals
- Major accessibility failures
- Broken functionality
- SEO blocking issues

### Medium Priority Issues (51-75 points)
- Minor performance issues
- Some accessibility concerns
- Content quality issues
- UX friction points

### Low Priority Issues (76-100 points)
- Minor optimizations
- Enhancement opportunities
- Nice-to-have improvements

## Audit Report Template

```markdown
# Website Audit Report

## Executive Summary
**Overall Score**: X/100
**Critical Issues**: X
**High Priority**: X
**Medium Priority**: X
**Low Priority**: X

## Performance (Score: X/100)
- [Issue 1]
- [Issue 2]

## Accessibility (Score: X/100)
- [Issue 1]
- [Issue 2]

## SEO (Score: X/100)
- [Issue 1]
- [Issue 2]

## Security (Score: X/100)
- [Issue 1]
- [Issue 2]

## User Experience (Score: X/100)
- [Issue 1]
- [Issue 2]

## Recommendations
### Quick Wins (This Week)
1. [Action item]

### Short Term (This Month)
1. [Action item]

### Long Term (Next Quarter)
1. [Action item]
```

## Testing Tools

- **Performance**: PageSpeed Insights, WebPageTest, Lighthouse
- **Accessibility**: WAVE, axe DevTools, Lighthouse
- **SEO**: Google Search Console, Screaming Frog
- **Security**: SSL Labs, Security Headers
- **Mobile**: Mobile-Friendly Test, Responsive Design Checker

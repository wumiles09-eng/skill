---
name: seo-audit
description: Comprehensive SEO audit for websites and web applications. Use when reviewing websites for search engine optimization, analyzing meta tags, checking technical SEO, evaluating content structure, and identifying opportunities to improve search rankings.
---

# SEO Audit Skill

This skill performs comprehensive SEO audits to identify issues and opportunities for improving search engine rankings.

## Audit Checklist

### Technical SEO

#### Meta Tags
- [ ] Title tag (50-60 characters, unique per page)
- [ ] Meta description (150-160 characters, compelling)
- [ ] Canonical URL specified
- [ ] Open Graph tags for social sharing
- [ ] Twitter Card tags
- [ ] Robots meta tag (if needed)
- [ ] Viewport meta tag

```html
<title>Primary Keyword - Secondary Keyword | Brand Name</title>
<meta name="description" content="Compelling description with keywords">
<link rel="canonical" href="https://example.com/page">
<meta property="og:title" content="Title for social sharing">
<meta property="og:description" content="Description for social sharing">
<meta property="og:image" content="https://example.com/image.jpg">
```

#### Structured Data
- [ ] Schema.org markup implemented
- [ ] JSON-LD format preferred
- [ ] Rich snippets opportunities
- [ ] Local business schema (if applicable)
- [ ] Product/Review schema (if applicable)
- [ ] Article/Blog schema (if applicable)
- [ ] BreadcrumbList schema
- [ ] FAQPage schema for FAQs

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Article Title",
  "author": {
    "@type": "Person",
    "name": "Author Name"
  },
  "datePublished": "2024-01-01"
}
</script>
```

#### Site Performance
- [ ] Page load speed < 3 seconds
- [ ] Mobile-friendly (responsive design)
- [ ] HTTPS enabled
- [ ] No crawl errors (check Google Search Console)
- [ ] XML sitemap submitted
- [ ] Robots.txt configured
- [ ] Clean URL structure
- [ ] 404 page exists
- [ ] Redirect chains avoided

### On-Page SEO

#### Content Structure
- [ ] H1 tag (one per page, includes primary keyword)
- [ ] H2-H6 tags used hierarchically
- [ ] Keyword in first 100 words
- [ ] Content length adequate (300+ words minimum)
- [ ] Internal links to relevant content
- [ ] External links to authoritative sources
- [ ] Image alt text descriptive
- [ ] URL contains keyword
- [ ] Content addresses search intent

#### Content Quality
- [ ] Unique, original content
- [ ] Addresses user's query comprehensively
- [ ] Readable and well-formatted
- [ ] Updated regularly
- [ ] Multimedia content (images, videos)
- [ ] Clear call-to-action
- [ ] Social sharing buttons
- [ ] Comments/discussion enabled

### Off-Page SEO

- [ ] Backlink profile analysis
- [ ] Domain authority checked
- [ ] Social media presence
- [ ] Local citations (if local business)
- [ ] Brand mentions tracked
- [ ] Competitor backlink analysis

## Common SEO Issues

### Critical Issues (Fix Immediately)
1. **Duplicate Content**: Multiple URLs with same content
2. **Missing Meta Tags**: No title or description
3. **Broken Links**: 404 errors on internal/external links
4. **Slow Page Speed**: Load time > 5 seconds
5. **Not Mobile-Friendly**: Poor mobile experience
6. **Blocked Resources**: CSS/JS blocked by robots.txt

### Important Issues (Fix Soon)
1. **Thin Content**: Pages with less than 300 words
2. **Missing Alt Text**: Images without descriptions
3. **Poor URL Structure**: Long, messy URLs
4. **Low Word Count**: Insufficient content depth
5. **Keyword Cannibalization**: Multiple pages targeting same keyword

### Minor Issues (Fix When Possible)
1. **Missing Schema**: No structured data
2. **No Open Graph**: Poor social sharing previews
3. **Old Content**: Outdated information
4. **Low Readability**: Complex sentences, poor formatting

## SEO Audit Report Structure

### 1. Executive Summary
- Overall SEO score
- Critical issues found
- Quick wins identified

### 2. Technical Analysis
- Site performance metrics
- Crawlability issues
- Indexing status
- Mobile-friendliness

### 3. On-Page Analysis
- Content quality assessment
- Meta tags review
- Internal linking structure
- Keyword usage

### 4. Off-Page Analysis
- Backlink profile
- Domain authority
- Social signals

### 5. Recommendations
- Prioritized action items
- Quick wins (implement in 1 week)
- Medium-term improvements (implement in 1 month)
- Long-term strategy (3-6 months)

## Tools to Use

- Google Search Console
- Google PageSpeed Insights
- SEMrush / Ahrefs / Moz
- Screaming Frog SEO Spider
- Schema.org validator
- Rich Results Test
- Mobile-Friendly Test

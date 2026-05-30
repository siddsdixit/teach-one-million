# SEO Audit Skill

Audit a live URL for SEO fundamentals and generate recommendations.

## Quick Audit

```bash
# Check meta tags
curl -s "$URL" | grep -E '<title>|<meta name="description"|<meta property="og'

# Check robots.txt
curl -s "$URL/robots.txt"

# Check sitemap
curl -s "$URL/sitemap.xml" | head -20
```

## Audit Checklist

### Meta Tags
- [ ] `<title>` tag — 50-60 characters, includes primary keyword
- [ ] `<meta name="description">` — 150-160 characters, compelling, includes keyword
- [ ] `<meta property="og:title">` — matches or improves on title tag
- [ ] `<meta property="og:description">` — social sharing description
- [ ] `<meta property="og:image">` — 1200×630px image
- [ ] `<meta property="og:url">` — canonical URL
- [ ] `<link rel="canonical">` — prevents duplicate content

### Page Structure
- [ ] Single `<h1>` on each page — primary keyword
- [ ] `<h2>`-`<h6>` hierarchy logical
- [ ] All images have descriptive `alt` attributes
- [ ] Internal links use descriptive anchor text (not "click here")

### Technical
- [ ] `robots.txt` exists and doesn't block important pages
- [ ] `sitemap.xml` exists and submitted to Google Search Console
- [ ] Page loads under 3 seconds
- [ ] HTTPS enabled (Google ranking factor)
- [ ] Mobile-responsive (Core Web Vitals)

## Keyword Targeting

Select 3-5 primary keywords:
1. Match search intent (informational, transactional, navigational)
2. Realistic volume for a new site (< 10k/month to start)
3. Clear connection to product value proposition

## Output Format

```markdown
# SEO Audit: [product-name]

## Score: [X]/10

## Meta Tags
- Title: ✅/❌ "[current title]" — [recommendation]
- Description: ✅/❌ "[current]" — [recommendation]
- OG tags: ✅/❌

## Page Structure
[findings]

## Technical
[findings]

## Keyword Recommendations
1. [keyword] — [monthly searches est.] — [intent]
2. ...

## Priority Fixes (in order)
1. [fix] — [expected impact]
```

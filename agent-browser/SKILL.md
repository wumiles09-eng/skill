---
name: agent-browser
description: Browser automation and web interaction capabilities for testing websites, scraping data, and performing automated browser tasks. Use when needing to interact with web pages programmatically, take screenshots, fill forms, or validate web applications.
---

# Agent Browser

Browser automation capabilities for testing, scraping, and validating web applications.

## Core Capabilities

### 1. Page Navigation
```javascript
// Navigate to URL
await page.goto('https://example.com')

// Wait for navigation
await page.waitForNavigation()

// Wait for selector
await page.waitForSelector('.content')

// Wait for load state
await page.waitForLoadState('networkidle')
```

### 2. Element Interaction
```javascript
// Click element
await page.click('button.submit')

// Fill input
await page.fill('#email', 'user@example.com')

// Select dropdown
await page.selectOption('select.country', 'US')

// Upload file
await page.setInputFiles('input[type="file"]', 'path/to/file.pdf')

// Hover
await page.hover('.menu-item')
```

### 3. Information Extraction
```javascript
// Get text content
const text = await page.textContent('h1')

// Get attribute
const href = await page.getAttribute('a', 'href')

// Get multiple elements
const items = await page.locator('.item').allTextContents()

// Evaluate JavaScript
const title = await page.evaluate(() => document.title)

// Screenshot
await page.screenshot({ path: 'screenshot.png' })

// PDF
await page.pdf({ path: 'page.pdf' })
```

### 4. Form Handling
```javascript
// Fill complete form
await page.fill('#name', 'John Doe')
await page.fill('#email', 'john@example.com')
await page.check('#terms')
await page.click('button[type="submit"]')

// Wait for response
await page.waitForResponse('https://api.example.com/submit')
```

## Testing Patterns

### 1. Page Object Model
```javascript
class LoginPage {
  constructor(page) {
    this.page = page
    this.emailInput = page.locator('#email')
    this.passwordInput = page.locator('#password')
    this.loginButton = page.locator('button[type="submit"]')
  }

  async login(email, password) {
    await this.emailInput.fill(email)
    await this.passwordInput.fill(password)
    await this.loginButton.click()
    await this.page.waitForURL('**/dashboard')
  }
}

// Usage
const loginPage = new LoginPage(page)
await loginPage.login('user@example.com', 'password123')
```

### 2. Assertions
```javascript
// Wait for element to be visible
await expect(page.locator('.success')).toBeVisible()

// Check text content
await expect(page.locator('h1')).toHaveText('Welcome')

// Check URL
await expect(page).toHaveURL('**/dashboard')

// Check element count
await expect(page.locator('.item')).toHaveCount(3)
```

### 3. Network Monitoring
```javascript
// Monitor API requests
page.on('request', request => {
  console.log('Request:', request.url())
})

page.on('response', response => {
  console.log('Response:', response.status(), response.url())
})

// Wait for specific response
await page.waitForResponse(response =>
  response.url().includes('api') && response.status() === 200
)
```

## Web Scraping

### Data Extraction
```javascript
// Scrape product listings
const products = await page.locator('.product').all()

const data = await Promise.all(products.map(async product => {
  return {
    name: await product.locator('.name').textContent(),
    price: await product.locator('.price').textContent(),
    image: await product.locator('img').getAttribute('src')
  }
}))

// Handle pagination
const allData = []
while (true) {
  const pageData = await scrapePage()
  allData.push(...pageData)

  const nextButton = page.locator('.next-page:not(.disabled)')
  if (await nextButton.count() === 0) break

  await nextButton.click()
  await page.waitForLoadState('networkidle')
}
```

### Dynamic Content
```javascript
// Wait for lazy-loaded content
await page.waitForFunction(() => {
  return document.querySelectorAll('.item').length >= 10
})

// Scroll to load more
while (true) {
  await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight))
  await page.waitForTimeout(1000)

  const count = await page.locator('.item').count()
  if (count >= targetCount) break
}
```

## Screenshots & Visual Testing

### Screenshots
```javascript
// Full page
await page.screenshot({
  path: 'full-page.png',
  fullPage: true
})

// Element screenshot
await page.locator('.header').screenshot({
  path: 'header.png'
})

// Multiple viewports
const viewports = [
  { width: 1920, height: 1080 },
  { width: 768, height: 1024 },
  { width: 375, height: 667 }
]

for (const viewport of viewports) {
  await page.setViewportSize(viewport)
  await page.screenshot({
    path: `screenshot-${viewport.width}x${viewport.height}.png`
  })
}
```

### Visual Regression
```javascript
// Compare with baseline
await page.goto('https://example.com')
expect(await page.screenshot()).toMatchSnapshot('homepage.png')
```

## Performance Monitoring

```javascript
// Monitor metrics
page.on('metrics', data => {
  console.log('Metrics:', data)
})

// Get performance metrics
const metrics = await page.evaluate(() => {
  const navigation = performance.getEntriesByType('navigation')[0]
  return {
    loadTime: navigation.loadEventEnd - navigation.navigationStart,
    domContentLoaded: navigation.domContentLoadedEventEnd - navigation.navigationStart
  }
})

// Core Web Vitals
const vitals = await page.evaluate(() => {
  return new Promise(resolve => {
    new PerformanceObserver(list => {
      const entries = list.getEntries()
      resolve(entries)
    }).observe({ entryTypes: ['largest-contentful-paint'] })
  })
})
```

## Error Handling

```javascript
// Retry logic
async function clickWithRetry(selector, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      await page.click(selector, { timeout: 5000 })
      return true
    } catch (error) {
      if (i === maxRetries - 1) throw error
      await page.waitForTimeout(1000)
    }
  }
}

// Handle alerts
page.on('dialog', async dialog => {
  console.log('Dialog:', dialog.message())
  await dialog.accept()
})

// Handle errors gracefully
try {
  await page.goto('https://example.com')
} catch (error) {
  console.error('Navigation failed:', error)
  // Take screenshot for debugging
  await page.screenshot({ path: 'error.png' })
}
```

## Best Practices

1. **Use explicit waits**: Avoid arbitrary `sleep()` calls
2. **Retry network operations**: Handle flaky network conditions
3. **Clean up resources**: Close pages and contexts
4. **Use locators**: More robust than selectors
5. **Handle dynamic content**: Wait for elements properly
6. **Parallelize tests**: Run multiple browsers concurrently
7. **Mock external APIs**: Speed up tests and reduce flakiness
8. **Take screenshots on failure**: Debug failed tests easily

## Common Patterns

### Authentication
```javascript
// Save storage state
await page.goto('https://example.com/login')
await page.fill('#email', 'user@example.com')
await page.fill('#password', 'password')
await page.click('button[type="submit"]')
await page.waitForURL('**/dashboard')

await page.context().storageState({ path: 'auth.json' })

// Use saved state
const context = await browser.newContext({
  storageState: 'auth.json'
})
```

### Multi-Tab
```javascript
// Open new tab
const [popup] = await Promise.all([
  page.waitForEvent('popup'),
  page.click('a[target="_blank"]')
])

await popup.waitForLoadState()
console.log(await popup.title())
```

### Iframe Handling
```javascript
// Get iframe
const frame = page.frame('iframe-name')

// Interact with iframe
await frame.fill('#input', 'value')
await frame.click('button')
```

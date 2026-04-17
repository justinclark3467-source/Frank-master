# BrowserCat Integration

API Key: TKDoxTWWufHnPZRcIelcIVzSyfHaKsWz4Vat5DOFIN2yy046e56GxwKEkCTxtKDP

## Usage

BrowserCat provides headless browser automation via WebSocket + Playwright/Puppeteer.

### Quick Connect (Playwright)

```python
import playwright.async_api as pw

bcat_url = "wss://api.browsercat.com/connect?browser=chrome&headless=new"
browser = await pw.chromium.connect(bcat_url, headers={
    "api-key": "TKDoxTWWufHnPZRcIelcIVzSyfHaKsWz4Vat5DOFIN2yy046e56GxwKEkCTxtKDP"
})
```

### Free Tier
- 1,000 credits/month
- 1 credit = 30 sec websocket OR 1 utility API request

## Setup Required
- `pip install playwright`
- `playwright install chromium`

import asyncio
from playwright.async_api import async_playwright
import os

async def test():
    api_key = os.getenv("BROWSERCAT_API_KEY", "TKDoxTWWufHnPZRcIelcIVzSyfHaKsWz4Vat5DOFIN2yy046e56GxwKEkCTxtKDP")
    
    bcat_url = "wss://api.browsercat.com/connect?browser=chrome&headless=new"
    
    async with async_playwright() as p:
        try:
            browser = await p.chromium.connect(bcat_url, headers={
                "api-key": api_key
            })
            print("✅ Connected to BrowserCat!")
            
            page = await browser.new_page()
            await page.goto("https://httpbin.org/ip")
            content = await page.content()
            print(f"✅ Page loaded: {content[:200]}")
            
            await browser.close()
            print("✅ Test complete!")
        except Exception as e:
            print(f"❌ Error: {e}")

asyncio.run(test())

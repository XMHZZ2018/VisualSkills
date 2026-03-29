"""
web-screenshot MCP server

Takes screenshots of web pages using Playwright (headless Chromium).
"""

import json
from pathlib import Path

from mcp.server.fastmcp import FastMCP
from playwright.async_api import async_playwright

mcp = FastMCP("web-screenshot")


@mcp.tool()
async def screenshot_url(
    url: str,
    output_path: str,
    full_page: bool = True,
    width: int = 1440,
    height: int = 900,
) -> str:
    """Take a screenshot of a web page.

    Args:
        url: URL to screenshot (e.g., "https://example.github.io")
        output_path: Path to save the PNG screenshot
        full_page: Capture full scrollable page (default True)
        width: Viewport width in pixels (default 1440)
        height: Viewport height in pixels (default 900)

    Returns:
        JSON with path to screenshot and dimensions.
    """
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": width, "height": height})
        await page.goto(url, wait_until="networkidle", timeout=30000)
        await page.screenshot(path=str(out), full_page=full_page)
        actual_height = await page.evaluate("document.body.scrollHeight") if full_page else height
        await browser.close()

    size_kb = out.stat().st_size / 1024
    return json.dumps({
        "path": str(out.resolve()),
        "size_kb": round(size_kb, 1),
        "width": width,
        "height": actual_height,
        "full_page": full_page,
    })


@mcp.tool()
async def screenshot_urls(
    urls: list[str],
    output_dir: str,
    full_page: bool = True,
    width: int = 1440,
    height: int = 900,
) -> str:
    """Take screenshots of multiple web pages.

    Args:
        urls: List of URLs to screenshot
        output_dir: Directory to save PNG screenshots
        full_page: Capture full scrollable page (default True)
        width: Viewport width in pixels (default 1440)
        height: Viewport height in pixels (default 900)

    Returns:
        JSON with list of screenshot paths.
    """
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        for i, url in enumerate(urls):
            try:
                page = await browser.new_page(viewport={"width": width, "height": height})
                await page.goto(url, wait_until="networkidle", timeout=30000)
                filename = f"screenshot_{i+1}.png"
                filepath = out_dir / filename
                await page.screenshot(path=str(filepath), full_page=full_page)
                await page.close()

                results.append({
                    "url": url,
                    "path": str(filepath.resolve()),
                    "size_kb": round(filepath.stat().st_size / 1024, 1),
                })
            except Exception as e:
                results.append({
                    "url": url,
                    "error": str(e),
                })

        await browser.close()

    return json.dumps(results, indent=2)


if __name__ == "__main__":
    mcp.run()

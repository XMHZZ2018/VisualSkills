"""
image-search MCP server

Provides tools to search for images online and download them.
"""

import io
import json
import re
import urllib.parse
from pathlib import Path

import httpx
from mcp.server.fastmcp import FastMCP
from PIL import Image

mcp = FastMCP("image-search")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}


@mcp.tool()
async def search_images(
    query: str,
    max_results: int = 20,
) -> str:
    """Search for images using DuckDuckGo and return image URLs.

    Args:
        query: Search query (e.g., "minimalist tech startup logo blue")
        max_results: Maximum number of image URLs to return (default 20)

    Returns:
        JSON list of image results with title, url, and source.
    """
    # Use DuckDuckGo's image search API
    search_url = "https://duckduckgo.com/"
    async with httpx.AsyncClient(timeout=30, headers=HEADERS, follow_redirects=True) as client:
        # First get the vqd token
        resp = await client.get(search_url, params={"q": query})
        vqd_match = re.search(r"vqd=['\"]([^'\"]+)['\"]", resp.text)
        if not vqd_match:
            # Fallback: try extracting from different pattern
            vqd_match = re.search(r"vqd=([\d-]+)", resp.text)
        if not vqd_match:
            return json.dumps({"error": "Could not get search token", "results": []})

        vqd = vqd_match.group(1)

        # Now search images
        img_url = "https://duckduckgo.com/i.js"
        params = {
            "l": "us-en",
            "o": "json",
            "q": query,
            "vqd": vqd,
            "f": ",,,,,",
            "p": "1",
        }

        resp = await client.get(img_url, params=params)
        data = resp.json()

    results = []
    for item in data.get("results", [])[:max_results]:
        results.append({
            "title": item.get("title", ""),
            "image_url": item.get("image", ""),
            "thumbnail_url": item.get("thumbnail", ""),
            "source": item.get("source", ""),
            "width": item.get("width"),
            "height": item.get("height"),
        })

    return json.dumps(results, indent=2)


@mcp.tool()
async def download_image(
    image_url: str,
    save_dir: str,
    filename: str | None = None,
) -> str:
    """Download an image to a local directory.

    Args:
        image_url: URL of the image to download
        save_dir: Directory to save the image in
        filename: Optional filename (default: derived from URL)

    Returns:
        Absolute path to the downloaded image file.
    """
    save_path = Path(save_dir)
    save_path.mkdir(parents=True, exist_ok=True)

    if not filename:
        url_path = urllib.parse.urlparse(image_url).path
        filename = url_path.split("/")[-1]
        if not any(filename.lower().endswith(ext) for ext in [".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"]):
            filename += ".png"
        filename = re.sub(r"[^\w.\-]", "_", filename)

    async with httpx.AsyncClient(timeout=30, headers=HEADERS, follow_redirects=True) as client:
        resp = await client.get(image_url)
        resp.raise_for_status()
        raw_bytes = resp.content

    # Validate and convert to PNG, resize if too large
    try:
        img = Image.open(io.BytesIO(raw_bytes))
        img = img.convert("RGB")

        # Resize to max 1024px on longest side
        max_dim = 1024
        if img.width > max_dim or img.height > max_dim:
            img.thumbnail((max_dim, max_dim), Image.LANCZOS)

        # Always save as JPEG for smaller file size
        if not filename.lower().endswith(".jpg"):
            filename = filename.rsplit(".", 1)[0] + ".jpg"

        output_file = save_path / filename
        img.save(str(output_file), "JPEG", quality=85)
    except Exception as e:
        return json.dumps({"error": f"Could not process image: {e}", "url": image_url})

    size_kb = output_file.stat().st_size / 1024
    return json.dumps({
        "path": str(output_file.resolve()),
        "size_kb": round(size_kb, 1),
        "filename": filename,
        "width": img.width,
        "height": img.height,
    })


if __name__ == "__main__":
    mcp.run()

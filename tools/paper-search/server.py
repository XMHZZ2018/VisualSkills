"""
paper-search MCP server

Provides tools to search for academic papers and download their PDFs.
Designed to be composed by skills like paper-beautify.
"""

import json
import os
import re
import urllib.parse
from pathlib import Path

import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("paper-search")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}


@mcp.tool()
async def search_papers(
    query: str,
    max_results: int = 20,
) -> str:
    """Search for academic papers using the Semantic Scholar API.

    Args:
        query: Search query (e.g., "object detection CVPR 2024")
        max_results: Maximum number of results to return (default 20)

    Returns:
        JSON list of papers with title, authors, year, venue, abstract, and PDF URLs.
    """
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        "query": query,
        "limit": min(max_results, 100),
        "fields": "title,authors,year,venue,abstract,externalIds,openAccessPdf,url",
    }

    async with httpx.AsyncClient(timeout=30, headers=HEADERS) as client:
        resp = await client.get(url, params=params)
        resp.raise_for_status()
        data = resp.json()

    papers = []
    for paper in data.get("data", []):
        pdf_url = None
        if paper.get("openAccessPdf"):
            pdf_url = paper["openAccessPdf"].get("url")

        # Fallback: try arxiv
        if not pdf_url and paper.get("externalIds", {}).get("ArXiv"):
            arxiv_id = paper["externalIds"]["ArXiv"]
            pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"

        authors = [a.get("name", "") for a in paper.get("authors", [])]

        papers.append({
            "title": paper.get("title"),
            "authors": authors[:5],  # Limit to first 5
            "year": paper.get("year"),
            "venue": paper.get("venue"),
            "abstract": (paper.get("abstract") or "")[:300],
            "pdf_url": pdf_url,
            "semantic_scholar_url": paper.get("url"),
        })

    return json.dumps(papers, indent=2)


@mcp.tool()
async def search_arxiv(
    query: str,
    max_results: int = 10,
) -> str:
    """Search for papers on arXiv.

    Args:
        query: Search query (e.g., "transformer object detection")
        max_results: Maximum number of results (default 10)

    Returns:
        JSON list of papers with title, authors, abstract, arxiv_id, and pdf_url.
    """
    search_query = urllib.parse.quote(query)
    url = (
        f"https://export.arxiv.org/api/query?"
        f"search_query=all:{search_query}&start=0&max_results={max_results}"
        f"&sortBy=relevance&sortOrder=descending"
    )

    async with httpx.AsyncClient(timeout=30, headers=HEADERS, follow_redirects=True) as client:
        resp = await client.get(url)
        resp.raise_for_status()
        text = resp.text

    papers = []
    # Simple XML parsing for arxiv atom feed
    entries = re.findall(r"<entry>(.*?)</entry>", text, re.DOTALL)
    for entry in entries:
        title = _extract_tag(entry, "title").strip().replace("\n", " ")
        abstract = _extract_tag(entry, "summary").strip().replace("\n", " ")[:300]
        authors = re.findall(r"<name>(.*?)</name>", entry)

        # Extract arxiv ID from the id URL
        id_url = _extract_tag(entry, "id")
        arxiv_id = id_url.split("/abs/")[-1] if "/abs/" in id_url else ""

        pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf" if arxiv_id else None

        # Extract categories
        categories = re.findall(r'<category[^>]*term="([^"]*)"', entry)

        papers.append({
            "title": title,
            "authors": authors[:5],
            "abstract": abstract,
            "arxiv_id": arxiv_id,
            "pdf_url": pdf_url,
            "categories": categories[:5],
        })

    return json.dumps(papers, indent=2)


@mcp.tool()
async def download_paper(
    pdf_url: str,
    save_dir: str,
    filename: str | None = None,
) -> str:
    """Download a paper PDF to a local directory.

    Args:
        pdf_url: URL of the PDF to download
        save_dir: Directory to save the PDF in
        filename: Optional filename (default: derived from URL)

    Returns:
        Absolute path to the downloaded PDF file.
    """
    save_path = Path(save_dir)
    save_path.mkdir(parents=True, exist_ok=True)

    if not filename:
        # Derive filename from URL
        url_path = urllib.parse.urlparse(pdf_url).path
        filename = url_path.split("/")[-1]
        if not filename.endswith(".pdf"):
            filename += ".pdf"
        # Sanitize
        filename = re.sub(r"[^\w.\-]", "_", filename)

    output_file = save_path / filename

    async with httpx.AsyncClient(timeout=60, headers=HEADERS, follow_redirects=True) as client:
        resp = await client.get(pdf_url)
        resp.raise_for_status()
        output_file.write_bytes(resp.content)

    size_kb = output_file.stat().st_size / 1024
    return json.dumps({
        "path": str(output_file.resolve()),
        "size_kb": round(size_kb, 1),
        "filename": filename,
    })


def _extract_tag(xml: str, tag: str) -> str:
    match = re.search(rf"<{tag}[^>]*>(.*?)</{tag}>", xml, re.DOTALL)
    return match.group(1) if match else ""


if __name__ == "__main__":
    mcp.run()

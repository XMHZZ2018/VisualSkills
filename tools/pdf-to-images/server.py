"""
pdf-to-images MCP server

Provides tools to convert PDF pages to PNG images for multimodal analysis.
Uses PyMuPDF (fitz) — no external dependencies like poppler or ImageMagick needed.
"""

import json
import os
from pathlib import Path

import fitz  # PyMuPDF
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("pdf-to-images")


@mcp.tool()
def pdf_to_images(
    pdf_path: str,
    output_dir: str | None = None,
    pages: str = "1-4",
    dpi: int = 150,
) -> str:
    """Convert PDF pages to PNG images for visual analysis.

    Args:
        pdf_path: Path to the PDF file
        output_dir: Directory to save images (default: same dir as PDF)
        pages: Page range to convert, e.g. "1-4", "1,3,5", or "all" (default "1-4")
        dpi: Resolution in DPI (default 150)

    Returns:
        JSON with list of image paths and page count.
    """
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        return json.dumps({"error": f"PDF not found: {pdf_path}"})

    if output_dir:
        out = Path(output_dir)
    else:
        out = pdf_path.parent
    out.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(str(pdf_path))
    total_pages = len(doc)

    # Parse page range
    page_indices = _parse_pages(pages, total_pages)

    zoom = dpi / 72.0
    matrix = fitz.Matrix(zoom, zoom)

    image_paths = []
    stem = pdf_path.stem

    for idx in page_indices:
        page = doc[idx]
        pix = page.get_pixmap(matrix=matrix)
        img_name = f"{stem}_page_{idx + 1}.png"
        img_path = out / img_name
        pix.save(str(img_path))
        image_paths.append(str(img_path.resolve()))

    doc.close()

    return json.dumps({
        "images": image_paths,
        "total_pages": total_pages,
        "pages_converted": len(image_paths),
        "dpi": dpi,
    }, indent=2)


@mcp.tool()
def pdf_page_count(pdf_path: str) -> str:
    """Get the number of pages in a PDF.

    Args:
        pdf_path: Path to the PDF file

    Returns:
        JSON with page count.
    """
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        return json.dumps({"error": f"PDF not found: {pdf_path}"})

    doc = fitz.open(str(pdf_path))
    count = len(doc)
    doc.close()

    return json.dumps({"path": str(pdf_path), "page_count": count})


def _parse_pages(pages_str: str, total: int) -> list[int]:
    """Parse page range string into 0-based indices."""
    if pages_str.strip().lower() == "all":
        return list(range(total))

    indices = set()
    for part in pages_str.split(","):
        part = part.strip()
        if "-" in part:
            start, end = part.split("-", 1)
            start = max(1, int(start))
            end = min(total, int(end))
            indices.update(range(start - 1, end))
        else:
            idx = int(part) - 1
            if 0 <= idx < total:
                indices.add(idx)

    return sorted(indices)


if __name__ == "__main__":
    mcp.run()

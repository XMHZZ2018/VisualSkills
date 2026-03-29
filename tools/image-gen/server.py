"""
image-gen MCP server

Generates images using Google Gemini (Nano Banana) API.
Requires GEMINI_API_KEY environment variable.
"""

import base64
import json
import os
from pathlib import Path

import google.genai as genai
from google.genai import types
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("image-gen")


def _get_client():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable is required")
    return genai.Client(api_key=api_key)


@mcp.tool()
def generate_image(
    prompt: str,
    output_path: str,
    aspect_ratio: str = "1:1",
    reference_images: list[str] | None = None,
) -> str:
    """Generate an image using Gemini (Nano Banana).

    Args:
        prompt: Text description of the image to generate
        output_path: Path to save the generated image (e.g., "output/logo.png")
        aspect_ratio: Aspect ratio - "1:1", "3:4", "4:3", "9:16", "16:9" (default "1:1")
        reference_images: Optional list of file paths to reference images for style guidance

    Returns:
        JSON with path to generated image and metadata.
    """
    client = _get_client()

    # Build contents
    contents = []

    # Add reference images if provided
    if reference_images:
        for img_path in reference_images:
            img_path = Path(img_path)
            if img_path.exists():
                img_data = base64.standard_b64encode(img_path.read_bytes()).decode("utf-8")
                mime = "image/png" if img_path.suffix == ".png" else "image/jpeg"
                contents.append(
                    types.Part(inline_data=types.Blob(mime_type=mime, data=img_data))
                )

    contents.append(prompt)

    response = client.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=contents,
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE"],
            image_config=types.ImageConfig(
                aspect_ratio=aspect_ratio,
            ),
        ),
    )

    # Extract and save image
    return _save_response_image(response, output_path)


@mcp.tool()
def edit_image(
    prompt: str,
    input_image: str,
    output_path: str,
) -> str:
    """Edit an existing image using Gemini (Nano Banana).

    Args:
        prompt: Description of the edit to make
        input_image: Path to the image to edit
        output_path: Path to save the edited image

    Returns:
        JSON with path to edited image.
    """
    client = _get_client()

    img_path = Path(input_image)
    if not img_path.exists():
        return json.dumps({"error": f"Image not found: {input_image}"})

    img_data = base64.standard_b64encode(img_path.read_bytes()).decode("utf-8")
    mime = "image/png" if img_path.suffix == ".png" else "image/jpeg"

    response = client.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=[
            types.Part(inline_data=types.Blob(mime_type=mime, data=img_data)),
            prompt,
        ],
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE"],
        ),
    )

    return _save_response_image(response, output_path)


def _save_response_image(response, output_path: str) -> str:
    """Extract image from Gemini response and save as PNG."""
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)

    for part in response.parts:
        if part.inline_data:
            data = part.inline_data.data

            # Handle both raw bytes and base64-encoded strings
            if isinstance(data, str):
                image_bytes = base64.b64decode(data)
            elif isinstance(data, bytes):
                # Check if it looks like base64 text
                try:
                    decoded = base64.b64decode(data)
                    # Verify it's a valid image by checking magic bytes
                    if decoded[:4] in [b'\x89PNG', b'\xff\xd8\xff\xe0', b'\xff\xd8\xff\xe1']:
                        image_bytes = decoded
                    else:
                        image_bytes = data
                except Exception:
                    image_bytes = data
            else:
                image_bytes = bytes(data)

            out.write_bytes(image_bytes)

            # Verify the saved file is a valid image
            try:
                from PIL import Image
                import io
                img = Image.open(io.BytesIO(image_bytes))
                # Re-save as proper PNG to ensure compatibility
                img.save(str(out), "PNG")
                return json.dumps({
                    "path": str(out.resolve()),
                    "size_kb": round(out.stat().st_size / 1024, 1),
                    "width": img.width,
                    "height": img.height,
                })
            except Exception as e:
                return json.dumps({
                    "path": str(out.resolve()),
                    "size_kb": round(len(image_bytes) / 1024, 1),
                    "warning": f"Saved but could not verify image: {e}",
                })

    return json.dumps({"error": "No image generated in response"})


if __name__ == "__main__":
    mcp.run()

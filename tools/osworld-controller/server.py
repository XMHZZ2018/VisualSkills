"""
osworld-controller MCP server

Bridges Claude to an OSWorld VM desktop via an HTTP bridge running in the
host Python process. Each action tool executes a pyautogui command, waits
for the UI to settle (2s, matching OSWorld's default pause), then returns
a screenshot — mirroring the original OSWorld action-observation loop.

Requires env var:
    OSWORLD_BRIDGE_URL  e.g. http://127.0.0.1:18765
"""

import base64
import io
import json
import os
import time

import httpx
from PIL import Image as PILImage
from mcp.server.fastmcp import FastMCP, Image

BRIDGE_URL = os.environ.get("OSWORLD_BRIDGE_URL", "http://127.0.0.1:18765")

# The VM runs at native resolution (e.g. 1920x1080) but we present
# screenshots to the model at this target size so it generates coordinates
# in a resolution matching the original OSWorld anthropic agent (1280x720).
TARGET_WIDTH = int(os.environ.get("OSWORLD_TARGET_WIDTH", "1280"))
TARGET_HEIGHT = int(os.environ.get("OSWORLD_TARGET_HEIGHT", "720"))
_native_width: int | None = None  # detected from first screenshot
_native_height: int | None = None

mcp = FastMCP("osworld-controller")
_client = httpx.Client(timeout=120.0)


# ── internal helpers ──────────────────────────────────────────────────────────

def _get(path: str) -> dict:
    r = _client.get(f"{BRIDGE_URL}{path}")
    r.raise_for_status()
    return r.json()


def _post(path: str, data: dict) -> dict:
    r = _client.post(f"{BRIDGE_URL}{path}", json=data)
    r.raise_for_status()
    return r.json()


def _screenshot() -> Image:
    """Capture a screenshot, resize to target resolution, return as Image."""
    global _native_width, _native_height
    data = _get("/screenshot")
    png_bytes = base64.b64decode(data["data"])
    img = PILImage.open(io.BytesIO(png_bytes))
    # Detect native resolution on first call
    if _native_width is None:
        _native_width, _native_height = img.size
    # Resize if needed
    if img.size != (TARGET_WIDTH, TARGET_HEIGHT):
        img = img.resize((TARGET_WIDTH, TARGET_HEIGHT), PILImage.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return Image(data=buf.getvalue(), format="png")


def _scale_coords(x: int, y: int) -> tuple[int, int]:
    """Scale coordinates from target (model) space to native (VM) space."""
    if _native_width is None or _native_width == TARGET_WIDTH:
        return x, y
    sx = _native_width / TARGET_WIDTH
    sy = _native_height / TARGET_HEIGHT
    return int(x * sx), int(y * sy)


def _exec_and_screenshot(command: str) -> list:
    """Execute a pyautogui command, wait for UI to settle, return screenshot."""
    _post("/execute_python", {"command": command})
    time.sleep(2)  # match OSWorld's default pause for UI to update
    img = _screenshot()
    return [json.dumps({"ok": True}), img]


# ── observation ───────────────────────────────────────────────────────────────

@mcp.tool()
def screenshot() -> Image:
    """Take a screenshot of the VM desktop.

    Returns:
        Current screenshot of the VM desktop as an image.
    """
    return _screenshot()


# ── mouse tools ───────────────────────────────────────────────────────────────

@mcp.tool()
def click(x: int, y: int, button: str = "left") -> list:
    """Click the mouse at (x, y) on the VM desktop.

    Args:
        x: X coordinate in pixels (0 = left edge).
        y: Y coordinate in pixels (0 = top edge).
        button: "left" (default), "right", or "middle".

    Returns:
        Confirmation message and a screenshot.
    """
    nx, ny = _scale_coords(x, y)
    if button == "right":
        cmd = f"pyautogui.rightClick({nx}, {ny})"
    elif button == "middle":
        cmd = f"pyautogui.click({nx}, {ny}, button='middle')"
    else:
        cmd = f"pyautogui.click({nx}, {ny})"
    return _exec_and_screenshot(cmd)


@mcp.tool()
def double_click(x: int, y: int) -> list:
    """Double-click at (x, y) on the VM desktop.

    Args:
        x: X coordinate in pixels.
        y: Y coordinate in pixels.

    Returns:
        Confirmation message and a screenshot.
    """
    nx, ny = _scale_coords(x, y)
    return _exec_and_screenshot(f"pyautogui.doubleClick({nx}, {ny})")


@mcp.tool()
def move_to(x: int, y: int) -> list:
    """Move the mouse cursor to (x, y) without clicking.

    Args:
        x: X coordinate in pixels.
        y: Y coordinate in pixels.

    Returns:
        Confirmation message and a screenshot.
    """
    nx, ny = _scale_coords(x, y)
    return _exec_and_screenshot(f"pyautogui.moveTo({nx}, {ny})")


@mcp.tool()
def drag_to(start_x: int, start_y: int, end_x: int, end_y: int, duration: float = 0.5) -> list:
    """Click and drag from one point to another on the VM desktop.

    Args:
        start_x: Starting X coordinate.
        start_y: Starting Y coordinate.
        end_x: Ending X coordinate.
        end_y: Ending Y coordinate.
        duration: Duration of the drag in seconds (default 0.5).

    Returns:
        Confirmation message and a screenshot.
    """
    nsx, nsy = _scale_coords(start_x, start_y)
    nex, ney = _scale_coords(end_x, end_y)
    cmd = f"pyautogui.moveTo({nsx}, {nsy}); pyautogui.dragTo({nex}, {ney}, duration={duration})"
    return _exec_and_screenshot(cmd)


@mcp.tool()
def scroll(x: int, y: int, clicks: int) -> list:
    """Scroll the mouse wheel at (x, y).

    Args:
        x: X coordinate in pixels.
        y: Y coordinate in pixels.
        clicks: Number of scroll clicks. Positive = up, negative = down.

    Returns:
        Confirmation message and a screenshot.
    """
    nx, ny = _scale_coords(x, y)
    return _exec_and_screenshot(f"pyautogui.scroll({clicks}, x={nx}, y={ny})")


# ── keyboard tools ────────────────────────────────────────────────────────────

@mcp.tool()
def type_text(text: str, interval: float = 0.02) -> list:
    """Type text on the VM desktop. Handles newlines by pressing Enter.

    Args:
        text: Text to type. Newlines are converted to Enter key presses.
        interval: Seconds between each keypress (default 0.02).

    Returns:
        Confirmation message and a screenshot.
    """
    lines = text.split("\n")
    parts = []
    for i, line in enumerate(lines):
        if line:
            parts.append(f"pyautogui.write({json.dumps(line)}, interval={interval})")
        if i < len(lines) - 1:
            parts.append("pyautogui.press('enter')")
    cmd = "; ".join(parts) if parts else "pass"
    return _exec_and_screenshot(cmd)


@mcp.tool()
def key_press(key: str) -> list:
    """Press a single keyboard key on the VM desktop.

    Args:
        key: Key name, e.g. 'enter', 'tab', 'escape', 'backspace', 'delete',
             'up', 'down', 'left', 'right', 'home', 'end', 'pageup', 'pagedown',
             'f1'–'f12', 'space', 'ctrl', 'alt', 'shift', 'super'.

    Returns:
        Confirmation message and a screenshot.
    """
    return _exec_and_screenshot(f"pyautogui.press({json.dumps(key)})")


@mcp.tool()
def hotkey(keys: list[str]) -> list:
    """Press a keyboard shortcut (keys held simultaneously) on the VM desktop.

    Args:
        keys: Keys to press together, e.g. ["ctrl", "c"], ["ctrl", "shift", "t"],
              ["alt", "f4"], ["super"].

    Returns:
        Confirmation message and a screenshot.
    """
    keys_str = ", ".join(json.dumps(k) for k in keys)
    return _exec_and_screenshot(f"pyautogui.hotkey({keys_str})")


if __name__ == "__main__":
    mcp.run()

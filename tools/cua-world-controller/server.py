"""
cua-world-controller MCP server

Bridges Claude CLI to a cua-world environment via the HTTP bridge.
Matches the exact same computer_use tool interface that CUA-World's
own ClaudeAgent uses, so the action format is 1:1 compatible.

The model sees screenshots at 1280x720. Coordinates are scaled to
1920x1080 (CUA-World's native resolution) before sending to the bridge.

Requires env var:
    CW_BRIDGE_URL  e.g. http://127.0.0.1:8766
"""

import base64
import io
import json
import os
import time

import httpx
from PIL import Image as PILImage
from mcp.server.fastmcp import FastMCP, Image

BRIDGE_URL = os.environ.get("CW_BRIDGE_URL", "http://127.0.0.1:8766")

# cua-world native resolution (all envs use 1920x1080)
NATIVE_WIDTH = 1920
NATIVE_HEIGHT = 1080

# Model sees screenshots at this resolution (matches CUA-World's ClaudeAgent)
MODEL_WIDTH = 1280
MODEL_HEIGHT = 720

mcp = FastMCP("cua-world-controller")
_client = httpx.Client(timeout=120.0)


# ── internal helpers ──────────────────────────────────────────────────────────

def _get(path: str) -> dict:
    r = _client.get(f"{BRIDGE_URL}{path}")
    r.raise_for_status()
    return r.json()


def _post(path: str, data: dict) -> dict:
    """POST to the bridge. Returns parsed JSON for both 2xx and 409 (episode
    already ended) so callers can branch on the `done` field. Other errors
    still raise."""
    r = _client.post(f"{BRIDGE_URL}{path}", json=data)
    if r.status_code == 409:
        return r.json()
    r.raise_for_status()
    return r.json()


def _screenshot() -> Image:
    """Capture a screenshot, resize to model resolution, return as Image."""
    data = _get("/screenshot")
    png_bytes = base64.b64decode(data["data"])
    img = PILImage.open(io.BytesIO(png_bytes))
    # Resize to model resolution (1280x720)
    if img.size != (MODEL_WIDTH, MODEL_HEIGHT):
        img = img.resize((MODEL_WIDTH, MODEL_HEIGHT), PILImage.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return Image(data=buf.getvalue(), format="png")


def _scale_coords(x: int, y: int) -> list[int]:
    """Scale from model space (1280x720) to native space (1920x1080).

    This matches CUA-World's convert_point_format_claude():
        int(x * 1920 / 1280), int(y * 1080 / 720)
    """
    return [int(x * NATIVE_WIDTH / MODEL_WIDTH),
            int(y * NATIVE_HEIGHT / MODEL_HEIGHT)]


def _action_and_screenshot(action: dict, pause: float = 2.0) -> list:
    """Execute an action via bridge, wait for UI to settle, return screenshot.

    The action dict uses the MCP-level format; the bridge translates it to
    CUA-World's internal {"mouse": {...}} / {"keyboard": {...}} format.

    If the bridge reports `done=True` (e.g. the env hit its max_steps cap),
    we DO NOT execute another screenshot/action — we return a clear stop
    message so the agent terminates instead of burning budget on no-ops.
    """
    resp = _post("/execute_action", action)
    if resp.get("done"):
        reason = resp.get("reason") or "done"
        msg = (
            f"EPISODE ENDED ({reason}). The environment will not accept any "
            "further actions. Stop calling tools and end your turn now."
        )
        return [json.dumps({"ok": False, "done": True, "reason": reason, "message": msg})]
    time.sleep(pause)
    img = _screenshot()
    return [json.dumps({"ok": True}), img]


# ── observation ───────────────────────────────────────────────────────────────

@mcp.tool()
def screenshot() -> Image:
    """Take a screenshot of the desktop.

    Returns:
        Current screenshot of the desktop as an image.
    """
    return _screenshot()


# ── mouse tools ───────────────────────────────────────────────────────────────

@mcp.tool()
def click(x: int, y: int, button: str = "left") -> list:
    """Click the mouse at (x, y) on the desktop.

    Args:
        x: X coordinate in pixels (0 = left edge).
        y: Y coordinate in pixels (0 = top edge).
        button: "left" (default), "right", or "middle".

    Returns:
        Confirmation message and a screenshot.
    """
    coord = _scale_coords(x, y)
    action_type = {"left": "left_click", "right": "right_click", "middle": "middle_click"}.get(button, "left_click")
    return _action_and_screenshot({"action": action_type, "coordinate": coord})


@mcp.tool()
def double_click(x: int, y: int) -> list:
    """Double-click at (x, y) on the desktop.

    Args:
        x: X coordinate in pixels.
        y: Y coordinate in pixels.

    Returns:
        Confirmation message and a screenshot.
    """
    coord = _scale_coords(x, y)
    return _action_and_screenshot({"action": "double_click", "coordinate": coord})


@mcp.tool()
def move_to(x: int, y: int) -> list:
    """Move the mouse cursor to (x, y) without clicking.

    Args:
        x: X coordinate in pixels.
        y: Y coordinate in pixels.

    Returns:
        Confirmation message and a screenshot.
    """
    coord = _scale_coords(x, y)
    return _action_and_screenshot({"action": "mouse_move", "coordinate": coord})


@mcp.tool()
def drag_to(start_x: int, start_y: int, end_x: int, end_y: int) -> list:
    """Click and drag from one point to another on the desktop.

    Args:
        start_x: Starting X coordinate.
        start_y: Starting Y coordinate.
        end_x: Ending X coordinate.
        end_y: Ending Y coordinate.

    Returns:
        Confirmation message and a screenshot.
    """
    start = _scale_coords(start_x, start_y)
    end = _scale_coords(end_x, end_y)
    return _action_and_screenshot({
        "action": "drag",
        "startCoordinate": start,
        "endCoordinate": end,
    })


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
    coord = _scale_coords(x, y)
    direction = "up" if clicks > 0 else "down"
    return _action_and_screenshot({
        "action": "scroll",
        "coordinate": coord,
        "direction": direction,
        "amount": abs(clicks),
    })


# ── keyboard tools ────────────────────────────────────────────────────────────

@mcp.tool()
def type_text(text: str) -> list:
    """Type text on the desktop.

    Args:
        text: Text to type.

    Returns:
        Confirmation message and a screenshot.
    """
    return _action_and_screenshot({"action": "type", "text": text})


@mcp.tool()
def key_press(key: str) -> list:
    """Press a single keyboard key on the desktop.

    Args:
        key: Key name, e.g. 'Return', 'Tab', 'Escape', 'BackSpace', 'Delete',
             'Up', 'Down', 'Left', 'Right', 'Home', 'End', 'Page_Up', 'Page_Down',
             'F1'-'F12', 'space'.

    Returns:
        Confirmation message and a screenshot.
    """
    return _action_and_screenshot({"action": "key", "keys": key})


@mcp.tool()
def hotkey(keys: list[str]) -> list:
    """Press a keyboard shortcut (keys held simultaneously) on the desktop.

    Args:
        keys: Keys to press together, e.g. ["ctrl", "c"], ["ctrl", "shift", "t"],
              ["alt", "F4"], ["super"].

    Returns:
        Confirmation message and a screenshot.
    """
    return _action_and_screenshot({"action": "key", "keys": "+".join(keys)})


if __name__ == "__main__":
    mcp.run()

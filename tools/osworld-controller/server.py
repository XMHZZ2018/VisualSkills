"""
osworld-controller MCP server

Bridges Claude to an OSWorld VM desktop via an HTTP bridge running in the
host Python process. The bridge exposes env.controller methods over a local
HTTP server, and this MCP server translates Claude's tool calls into HTTP
requests to that bridge.

Requires env var:
    OSWORLD_BRIDGE_URL  e.g. http://127.0.0.1:18765
"""

import json
import os

import httpx
from mcp.server.fastmcp import FastMCP, Image

BRIDGE_URL = os.environ.get("OSWORLD_BRIDGE_URL", "http://127.0.0.1:18765")

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


def _exec(command: str) -> str:
    """Send a pyautogui command to the VM and return a confirmation string."""
    _post("/execute_python", {"command": command})
    return json.dumps({"ok": True, "command": command})


# ── observation tools ─────────────────────────────────────────────────────────

@mcp.tool()
def screenshot() -> Image:
    """Take a screenshot of the VM desktop.

    Returns:
        Current screenshot of the VM desktop as an image.
    """
    import base64
    data = _get("/screenshot")
    png_bytes = base64.b64decode(data["data"])
    return Image(data=png_bytes, format="png")


@mcp.tool()
def get_accessibility_tree() -> str:
    """Get the accessibility tree of the current VM desktop.

    Returns:
        JSON string of all visible UI elements and their properties.
        Use this to identify button labels, text fields, and coordinates.
    """
    data = _get("/accessibility_tree")
    return data.get("tree", "")


# ── mouse tools ───────────────────────────────────────────────────────────────

@mcp.tool()
def click(x: int, y: int, button: str = "left") -> str:
    """Click the mouse at (x, y) on the VM desktop.

    Args:
        x: X coordinate in pixels (0 = left edge).
        y: Y coordinate in pixels (0 = top edge).
        button: "left" (default), "right", or "middle".

    Returns:
        Confirmation message.
    """
    if button == "right":
        cmd = f"pyautogui.rightClick({x}, {y})"
    elif button == "middle":
        cmd = f"pyautogui.click({x}, {y}, button='middle')"
    else:
        cmd = f"pyautogui.click({x}, {y})"
    return _exec(cmd)


@mcp.tool()
def double_click(x: int, y: int) -> str:
    """Double-click at (x, y) on the VM desktop.

    Args:
        x: X coordinate in pixels.
        y: Y coordinate in pixels.

    Returns:
        Confirmation message.
    """
    return _exec(f"pyautogui.doubleClick({x}, {y})")


@mcp.tool()
def move_to(x: int, y: int) -> str:
    """Move the mouse cursor to (x, y) without clicking.

    Args:
        x: X coordinate in pixels.
        y: Y coordinate in pixels.

    Returns:
        Confirmation message.
    """
    return _exec(f"pyautogui.moveTo({x}, {y})")


@mcp.tool()
def drag_to(start_x: int, start_y: int, end_x: int, end_y: int, duration: float = 0.5) -> str:
    """Click and drag from one point to another on the VM desktop.

    Args:
        start_x: Starting X coordinate.
        start_y: Starting Y coordinate.
        end_x: Ending X coordinate.
        end_y: Ending Y coordinate.
        duration: Duration of the drag in seconds (default 0.5).

    Returns:
        Confirmation message.
    """
    cmd = f"pyautogui.moveTo({start_x}, {start_y}); pyautogui.dragTo({end_x}, {end_y}, duration={duration})"
    return _exec(cmd)


@mcp.tool()
def scroll(x: int, y: int, clicks: int) -> str:
    """Scroll the mouse wheel at (x, y).

    Args:
        x: X coordinate in pixels.
        y: Y coordinate in pixels.
        clicks: Number of scroll clicks. Positive = up, negative = down.

    Returns:
        Confirmation message.
    """
    return _exec(f"pyautogui.scroll({clicks}, x={x}, y={y})")


# ── keyboard tools ────────────────────────────────────────────────────────────

@mcp.tool()
def type_text(text: str, interval: float = 0.02) -> str:
    """Type text on the VM desktop. Handles newlines by pressing Enter.

    Args:
        text: Text to type. Newlines are converted to Enter key presses.
        interval: Seconds between each keypress (default 0.02).

    Returns:
        Confirmation message.
    """
    lines = text.split("\n")
    parts = []
    for i, line in enumerate(lines):
        if line:
            parts.append(f"pyautogui.write({json.dumps(line)}, interval={interval})")
        if i < len(lines) - 1:
            parts.append("pyautogui.press('enter')")
    cmd = "; ".join(parts) if parts else "pass"
    return _exec(cmd)


@mcp.tool()
def key_press(key: str) -> str:
    """Press a single keyboard key on the VM desktop.

    Args:
        key: Key name, e.g. 'enter', 'tab', 'escape', 'backspace', 'delete',
             'up', 'down', 'left', 'right', 'home', 'end', 'pageup', 'pagedown',
             'f1'–'f12', 'space', 'ctrl', 'alt', 'shift', 'super'.

    Returns:
        Confirmation message.
    """
    return _exec(f"pyautogui.press({json.dumps(key)})")


@mcp.tool()
def hotkey(keys: list[str]) -> str:
    """Press a keyboard shortcut (keys held simultaneously) on the VM desktop.

    Args:
        keys: Keys to press together, e.g. ["ctrl", "c"], ["ctrl", "shift", "t"],
              ["alt", "f4"], ["super"].

    Returns:
        Confirmation message.
    """
    keys_str = ", ".join(json.dumps(k) for k in keys)
    return _exec(f"pyautogui.hotkey({keys_str})")


# ── shell tool ────────────────────────────────────────────────────────────────

@mcp.tool()
def run_bash(script: str) -> str:
    """Run a bash script inside the VM.

    Use this for file operations, checking application state, or any task
    that is easier via the command line than via the GUI.

    Args:
        script: Bash script to execute inside the VM.

    Returns:
        JSON with 'output' (stdout+stderr) and 'returncode'.
    """
    data = _post("/run_bash", {"script": script})
    return json.dumps(data, ensure_ascii=False)


# ── task completion signals ───────────────────────────────────────────────────

@mcp.tool()
def task_done() -> str:
    """Signal that the task has been successfully completed.

    Call this ONLY after you have verified (via screenshot or accessibility tree)
    that the task goal has been achieved. The evaluation will run immediately
    after this call.

    Returns:
        Confirmation that the done signal was received.
    """
    _post("/signal", {"signal": "DONE"})
    return "Task marked as DONE. Evaluation will now run."


@mcp.tool()
def task_fail() -> str:
    """Signal that the task cannot be completed.

    Call this if the task is impossible, the required application is missing,
    or you have encountered an unrecoverable error after exhausting retries.

    Returns:
        Confirmation that the fail signal was received.
    """
    _post("/signal", {"signal": "FAIL"})
    return "Task marked as FAIL."


if __name__ == "__main__":
    mcp.run()

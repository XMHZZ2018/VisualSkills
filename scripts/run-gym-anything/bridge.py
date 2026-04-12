"""
HTTP bridge that sits between our MCP server and gym-anything's env API.

The main runner (run.py) starts this bridge in a thread. It holds a
reference to the live GymAnythingEnv object and exposes HTTP endpoints
that the gym-anything-controller MCP server calls.

Action format translation:
    MCP server sends high-level actions → bridge translates to gym-anything's
    internal format:
        {"mouse": {"left_click": [x, y]}}
        {"mouse": {"right_click": [x, y]}}
        {"mouse": {"double_click": [x, y]}}
        {"mouse": {"move": [x, y]}}
        {"mouse": {"scroll": <pixels>}}
        {"mouse": {"left_click_drag": [[x1, y1], [x2, y2]]}}
        {"keyboard": {"text": "hello"}}
        {"keyboard": {"keys": ["ctrl", "a"]}}

Endpoints:
    GET  /screenshot        → base64-wrapped PNG
    POST /execute_action    → translate + env.step()
    GET  /health            → liveness check
"""

from __future__ import annotations

import base64
import json
import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

LISTEN_PORT = int(os.environ.get("BRIDGE_PORT", "8766"))
WORKSPACE = Path(os.environ.get("WORKSPACE", "/workspace"))

_step_counter = 0
_env = None          # set by run.py before starting the server
_env_lock = threading.Lock()


def set_env(env):
    """Called by run.py to inject the live gym-anything env."""
    global _env
    _env = env


def _translate_action(body: dict) -> list[dict]:
    """Translate MCP-level action dict into gym-anything internal format.

    gym-anything env.step() expects a list of dicts in the format:
        {"mouse": {"left_click": [x, y]}}
        {"keyboard": {"text": "hello"}}
        {"keyboard": {"keys": ["ctrl", "a"]}}
    etc.
    """
    action_type = body.get("action", "")
    coord = body.get("coordinate")

    if action_type == "left_click":
        return [{"mouse": {"left_click": coord}}]

    elif action_type == "right_click":
        return [{"mouse": {"right_click": coord}}]

    elif action_type == "middle_click":
        return [{"mouse": {"middle_click": coord}}]

    elif action_type == "double_click":
        return [{"mouse": {"double_click": coord}}]

    elif action_type == "triple_click":
        return [{"mouse": {"triple_click": coord}}]

    elif action_type == "mouse_move":
        return [{"mouse": {"move": coord}}]

    elif action_type == "drag":
        start = body.get("startCoordinate")
        end = body.get("endCoordinate")
        return [{"mouse": {"left_click_drag": [start, end]}}]

    elif action_type == "scroll":
        direction = body.get("direction", "down")
        amount = body.get("amount", 3)
        # gym-anything: positive = down, negative = up
        pixels = amount if direction == "down" else -amount
        actions = []
        if coord:
            actions.append({"mouse": {"move": coord}})
        actions.append({"mouse": {"scroll": pixels}})
        return actions

    elif action_type == "type":
        return [{"keyboard": {"text": body.get("text", "")}}]

    elif action_type == "key":
        keys_str = body.get("keys", "")
        # gym-anything expects keys as a list: ["ctrl", "a"]
        # We receive them as "ctrl+a" or just "Return"
        keys_list = keys_str.split("+") if "+" in keys_str else [keys_str]
        return [{"keyboard": {"keys": keys_list}}]

    elif action_type == "screenshot":
        return [{"action": "screenshot"}]

    elif action_type == "wait":
        return [{"action": "wait", "time": body.get("time", 1.0)}]

    elif action_type == "terminate":
        return [{"action": "terminate", "status": body.get("status", "success")}]

    else:
        # Pass through unknown actions
        return [body]


class BridgeHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == "/screenshot":
            self._handle_screenshot()
        elif self.path == "/health":
            self._json({"ok": True})
        else:
            self.send_error(404)

    def do_POST(self) -> None:
        length = int(self.headers.get("Content-Length", 0))
        body: dict = json.loads(self.rfile.read(length)) if length else {}

        if self.path == "/execute_action":
            self._handle_execute_action(body)
        else:
            self.send_error(404)

    # ── handlers ──────────────────────────────────────────────────────────

    def _handle_screenshot(self) -> None:
        global _step_counter
        with _env_lock:
            try:
                obs = _env.capture_observation()
                screen = obs.get("screen") or obs.get("screenshot") or obs.get("image")
                if screen is None:
                    self._json({"error": "no screen in observation"}, status=500)
                    return

                if isinstance(screen, (bytes, bytearray)):
                    png = bytes(screen)
                elif isinstance(screen, str):
                    png = Path(screen).read_bytes()
                else:
                    # numpy array → encode to PNG
                    import io
                    from PIL import Image as PILImage
                    img = PILImage.fromarray(screen)
                    buf = io.BytesIO()
                    img.save(buf, format="PNG")
                    png = buf.getvalue()
            except Exception as exc:
                self._json({"error": str(exc)}, status=500)
                return

        b64 = base64.b64encode(png).decode()

        # Save step screenshot
        _step_counter += 1
        try:
            screenshots_dir = WORKSPACE / "screenshots"
            screenshots_dir.mkdir(parents=True, exist_ok=True)
            (screenshots_dir / f"step_{_step_counter:03d}.png").write_bytes(png)
        except Exception:
            pass

        self._json({"data": b64, "mime": "image/png"})

    def _handle_execute_action(self, body: dict) -> None:
        """Translate MCP action and execute on gym-anything env."""
        with _env_lock:
            try:
                ga_actions = _translate_action(body)
                obs, reward, done, info = _env.step(ga_actions)
                action_result = info.get("action_result", {
                    "action": body.get("action", "unknown"),
                    "output": "Executed",
                })
                self._json({"ok": True, "result": action_result, "done": done})
            except Exception as exc:
                self._json({"ok": False, "error": str(exc)}, status=500)

    # ── helpers ───────────────────────────────────────────────────────────

    def _json(self, data: dict, status: int = 200) -> None:
        body = json.dumps(data, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args) -> None:
        pass


def start_bridge_server(env, port: int = LISTEN_PORT, workspace: str | Path | None = None) -> HTTPServer:
    """Start the bridge in a daemon thread. Returns the server instance."""
    global _step_counter, WORKSPACE
    _step_counter = 0
    if workspace is not None:
        WORKSPACE = Path(workspace)
    set_env(env)
    server = HTTPServer(("0.0.0.0", port), BridgeHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    print(f"Bridge listening on :{port}", flush=True)
    return server

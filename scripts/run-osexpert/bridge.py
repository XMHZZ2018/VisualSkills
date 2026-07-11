"""
HTTP bridge running inside the Claude CLI container.

Translates between MCP server protocol and the OSExpert-Eval VM's raw HTTP API.
The VM is reachable at http://osexpert-vm:5000 via Docker network alias.

Endpoints:
    GET  /screenshot        → base64-wrapped PNG
    POST /execute_python    → wraps command with pyautogui preamble, sends to VM
    GET  /accessibility_tree → accessibility tree string
    POST /signal            → writes signal to /workspace/signal.txt

Saves step screenshots to /workspace/screenshots/.
"""

from __future__ import annotations

import base64
import json
import os
import urllib.request
import urllib.error
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

VM_URL = os.environ.get("OSEXPERT_VM_URL", "http://osexpert-vm:5000")
LISTEN_PORT = int(os.environ.get("BRIDGE_PORT", "8765"))
WORKSPACE = Path("/workspace")

_step_counter = 0


class BridgeHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        if self.path == "/screenshot":
            self._handle_screenshot()
        elif self.path == "/accessibility_tree":
            self._handle_accessibility_tree()
        else:
            self.send_error(404)

    def do_POST(self) -> None:  # noqa: N802
        length = int(self.headers.get("Content-Length", 0))
        body: dict = json.loads(self.rfile.read(length)) if length else {}

        if self.path == "/execute_python":
            self._handle_execute_python(body)
        elif self.path == "/signal":
            self._handle_signal(body)
        else:
            self.send_error(404)

    # ── handlers ──────────────────────────────────────────────────────────

    def _handle_screenshot(self) -> None:
        global _step_counter
        try:
            req = urllib.request.Request(f"{VM_URL}/screenshot")
            with urllib.request.urlopen(req, timeout=30) as resp:
                png = resp.read()
        except Exception as exc:
            self._json({"error": str(exc)}, status=502)
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

    def _handle_accessibility_tree(self) -> None:
        try:
            req = urllib.request.Request(f"{VM_URL}/accessibility")
            with urllib.request.urlopen(req, timeout=30) as resp:
                tree = resp.read().decode()
        except Exception as exc:
            self._json({"error": str(exc)}, status=502)
            return
        self._json({"tree": tree})

    def _handle_execute_python(self, body: dict) -> None:
        command = body.get("command", "")
        # Wrap with pyautogui preamble
        wrapped = (
            "import pyautogui; import time; "
            f"pyautogui.FAILSAFE = False; {command}"
        )
        payload = json.dumps({
            "command": ["python3", "-c", wrapped],
            "shell": False,
        }).encode()

        try:
            req = urllib.request.Request(
                f"{VM_URL}/execute",
                data=payload,
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=60) as resp:
                result = resp.read().decode()
            self._json({"ok": True, "result": result})
        except Exception as exc:
            self._json({"ok": False, "error": str(exc)}, status=500)

    def _handle_signal(self, body: dict) -> None:
        signal = body.get("signal", "DONE")
        try:
            (WORKSPACE / "signal.txt").write_text(signal, encoding="utf-8")
        except Exception as exc:
            self._json({"ok": False, "error": str(exc)}, status=500)
            return
        self._json({"ok": True})

    # ── helpers ───────────────────────────────────────────────────────────

    def _json(self, data: dict, status: int = 200) -> None:
        body = json.dumps(data, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args) -> None:
        # Suppress default HTTP request logging
        pass


def main() -> None:
    server = HTTPServer(("0.0.0.0", LISTEN_PORT), BridgeHandler)
    print(f"Bridge listening on :{LISTEN_PORT}, VM at {VM_URL}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()

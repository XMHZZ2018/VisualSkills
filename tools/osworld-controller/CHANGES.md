# OSWorld Controller: Changes and Rationale

This document explains all the changes made to the OSWorld MCP controller and evaluation harness, and the reasoning behind each one.

## Context

We use Claude CLI + MCP as a replacement for the original OSWorld Anthropic API + loop approach. The MCP server (`tools/osworld-controller/server.py`) bridges Claude to the OSWorld VM desktop, and the evaluation harness (`scripts/run-osworld/run.py`) orchestrates task execution and scoring.

The original setup had low success rates (~19% on Chrome tasks with Sonnet, ~40% with Opus). After the changes below, we achieved **90% with Sonnet and 80% with Opus** on a 10-task Chrome subset.

---

## Change 1: Remove `screenshot()` as a standalone tool, auto-return screenshots from every action

**What changed:** In the original MCP server, `screenshot()` was a separate tool that the model had to call explicitly after each action to see the result. Now, every action tool (click, type_text, hotkey, etc.) automatically returns a screenshot along with its confirmation message.

A lightweight `screenshot()` tool is still available for the initial observation (before any action is taken).

**Why:** In the original OSWorld anthropic agent, the action-observation loop is built into the framework: after every action, the framework automatically captures a screenshot and feeds it back to the model as the next observation. The model never has to explicitly request a screenshot — it just gets one. By auto-returning screenshots from every action tool, we replicate this same loop within MCP.

**Impact:** The model always has up-to-date visual feedback after every action, matching the original OSWorld behavior.

---

## Change 2: Add 2-second pause before screenshot capture

**What changed:** After executing a pyautogui command, the MCP server now waits 2 seconds (`time.sleep(2)`) before capturing the screenshot.

**Why:** The original OSWorld `desktop_env` uses `pause=2` in its `step()` function — a 2-second delay between executing an action and capturing the observation screenshot. This gives the UI time to settle (e.g., menus to open, pages to load, dialogs to appear). Without this pause, screenshots were captured before the UI updated, so the model saw stale state and made incorrect decisions.

---

## Change 3: Remove `get_accessibility_tree()` from MCP tools

**What changed:** The `get_accessibility_tree()` tool was removed from the MCP server.

**Why:** The original OSWorld anthropic agent does not use accessibility tree information. It relies entirely on screenshots (visual observations) for decision-making. Removing this tool aligns our setup with the original and avoids giving the model a tool it wasn't designed to use in this context.

---

## Change 4: Remove `run_bash()` from MCP tools

**What changed:** The `run_bash()` tool, which allowed executing arbitrary shell commands inside the VM, was removed from the MCP server.

**Why:** The goal is to evaluate GUI interaction ability. `run_bash()` provided a shortcut that let the model bypass the GUI entirely — for example, running `pkill -f google-chrome` instead of clicking the close button. We observed the model using this escape hatch to run shell commands when it got stuck on GUI tasks, which defeats the purpose of the benchmark. Removing it forces the model to solve tasks through the GUI only.

---

## Change 5: Remove `task_done()` and `task_fail()` signal tools

**What changed:** The `task_done()` and `task_fail()` tools were removed. The system prompt now says: "When you believe the task is complete, simply stop — do not call any signal tool."

**Why:** In the original OSWorld anthropic agent, the agent simply stops generating actions when it believes the task is complete. There is no explicit "done" signal — the evaluation runs automatically after the agent exits. Our `task_done()`/`task_fail()` tools were non-standard additions that don't match the original behavior.

---

## Change 6: Disable Claude CLI built-in tools

**What changed:** Added `--disallowed-tools Bash,Read,Write,Edit,Glob,Grep,Agent,NotebookEdit` to the Claude CLI invocation.

**Why:** Claude CLI comes with built-in tools (Bash, file Read/Write/Edit, etc.) that are designed for software engineering tasks. In the OSWorld evaluation context, these tools are irrelevant and harmful — the model should only use the MCP desktop interaction tools. Without disabling them, the model could use the built-in `Bash` tool to run commands on the host machine (not the VM), or attempt file operations that don't make sense in this context. The system prompt also includes: "You MUST interact with applications through their graphical user interface (GUI) only."

---

## Change 7: Screenshot resolution scaling (1920x1080 → 1280x720)

**What changed:** The MCP server now resizes screenshots from the VM's native resolution (1920x1080) to 1280x720 before sending them to the model. Coordinates from the model (in 1280x720 space) are scaled back to native resolution before executing pyautogui commands.

**Why:** This was the single most impactful fix. The Docker provider in OSWorld ignores the `screen_size` parameter and always runs at 1920x1080. However, the original OSWorld anthropic agent is configured to work at 1280x720 (`screen_width=1280, screen_height=720`). At 1920x1080:
- UI elements are smaller and harder for the model to locate precisely
- The model generates coordinates that miss targets (e.g., clicking at 1438,68 for a button that's actually at a different position at this resolution)
- Screenshots consume more tokens per image

We observed the model repeatedly clicking the same wrong coordinates 5-6 times, unable to hit small UI targets. After adding the resize, the same tasks were solved in clean, deliberate actions — e.g., the bookmarks folder task went from failing in 40+ steps to succeeding in 9 steps.

**Implementation:** On the first screenshot, the native resolution is detected. All subsequent screenshots are resized to 1280x720 using PIL LANCZOS resampling. All incoming coordinates are scaled by `(native_width/1280, native_height/720)` before being passed to pyautogui.

---

## Change 8: Fix Python path in MCP config

**What changed:** Changed MCP server config from `"command": "python3"` to `"command": sys.executable`.

**Why:** The system `python3` didn't have the `mcp` package installed. Using `sys.executable` ensures the MCP server runs with the same Python interpreter (from the virtualenv) as the evaluation harness, where all dependencies are installed.

---

## Summary of final MCP tools (9 total)

| Tool | Purpose |
|------|---------|
| `screenshot()` | Take a screenshot (for initial observation) |
| `click(x, y, button)` | Click at coordinates + auto screenshot |
| `double_click(x, y)` | Double-click + auto screenshot |
| `move_to(x, y)` | Move cursor + auto screenshot |
| `drag_to(start_x, start_y, end_x, end_y)` | Drag + auto screenshot |
| `scroll(x, y, clicks)` | Scroll + auto screenshot |
| `type_text(text)` | Type text + auto screenshot |
| `key_press(key)` | Press key + auto screenshot |
| `hotkey(keys)` | Press key combo + auto screenshot |

## Results comparison (10 Chrome tasks)

| Setup | Success Rate |
|-------|-------------|
| Before fixes (Sonnet, 1920x1080, old tools) | 19.6% (9/46) |
| Before resolution fix (Opus, 1920x1080, new tools) | 40% (4/10) |
| After all fixes (Opus, 1280x720) | **80%** (8/10) |
| After all fixes (Sonnet, 1280x720) | **90%** (9/10) |
| Original OSWorld anthropic agent (Sonnet 4.5, reference) | ~65% (30/46 on full Chrome set) |

# run-osworld

Run OSWorld desktop evaluation tasks using **Claude CLI + computer-use MCP**.

## Architecture

```
run.py  (host process)
├── DesktopEnv ──────────────────────────────► VM (Ubuntu desktop)
├── HTTP bridge  (localhost thread)                 ▲
│   ├── GET /screenshot → env.controller            │
│   ├── GET /accessibility_tree → env.controller    │  VMware/VBox bridge
│   ├── POST /execute_python → env.controller       │
│   ├── POST /run_bash → env.controller             │
│   └── POST /signal → sets completion signal       │
└── subprocess: claude -p "<task>" ─────────────────┘
                  └── MCP server: osworld-controller
                        └── HTTP → bridge → VM
```

Claude sees the VM screen via `screenshot()`, controls it via `click()` /
`type_text()` / etc., and signals completion via `task_done()` or `task_fail()`.
The host evaluates the result with OSWorld's standard `env.evaluate()`.

## Requirements

- [OSWorld](https://github.com/xlang-ai/OSWorld) installed and a VM image ready
- Claude CLI (`claude`) installed and authenticated
- Python dependencies: `mcp`, `httpx` (already in MMSkills requirements)

## Usage

### Single task

```bash
python scripts/run-osworld/run.py \
    --osworld_root ~/Documents/OSWorld \
    --path_to_vm /path/to/ubuntu.vmx \
    --specific_task_id <task_id>
```

### Full domain

```bash
python scripts/run-osworld/run.py \
    --osworld_root ~/Documents/OSWorld \
    --path_to_vm /path/to/ubuntu.vmx \
    --domain calc
```

### All tasks

```bash
python scripts/run-osworld/run.py \
    --osworld_root ~/Documents/OSWorld \
    --path_to_vm /path/to/ubuntu.vmx
```

## Key arguments

| Argument | Default | Description |
|---|---|---|
| `--osworld_root` | `~/Documents/OSWorld` or `$OSWORLD_ROOT` | OSWorld repo path |
| `--path_to_vm` | *(required)* | Path to `.vmx` / `.vbox` VM file |
| `--provider_name` | `vmware` | `vmware`, `virtualbox`, or `docker` |
| `--model` | `claude-sonnet-4-5` | Claude model to use |
| `--task_timeout` | `600` | Max seconds per task |
| `--domain` | `all` | Restrict to a single domain |
| `--specific_task_id` | – | Run one task by ID |
| `--result_dir` | `./results_claude_mcp` | Where to write results |
| `--cli_path` | `claude` | Path to Claude CLI binary |
| `--headless` | off | Run VM headless |

## Output structure

```
results_claude_mcp/
└── <model>/
    └── <domain>/
        └── <task_id>/
            ├── result.txt          # score (0.0–1.0)
            ├── meta.json           # task metadata + timing
            ├── claude_output.txt   # Claude's text response
            ├── final_screenshot.png
            ├── recording.mp4
            └── runtime.log
```

## MCP tools available to Claude

| Tool | Description |
|---|---|
| `screenshot()` | Take a screenshot of the VM desktop |
| `get_accessibility_tree()` | Get all visible UI elements + coordinates |
| `click(x, y, button)` | Click at pixel coordinates |
| `double_click(x, y)` | Double-click |
| `move_to(x, y)` | Move mouse without clicking |
| `drag_to(sx, sy, ex, ey)` | Click and drag |
| `scroll(x, y, clicks)` | Scroll up/down |
| `type_text(text)` | Type text (newlines → Enter) |
| `key_press(key)` | Press a single key |
| `hotkey(keys)` | Press a keyboard shortcut |
| `run_bash(script)` | Run bash inside the VM |
| `task_done()` | Signal successful completion |
| `task_fail()` | Signal task is impossible |

## Note on `--mcp-config`

This script passes `--mcp-config <path>` to the Claude CLI so it picks up the
`osworld-controller` MCP server with the correct bridge URL. If your Claude CLI
version does not support this flag, you can work around it by copying the
generated temp JSON to `.mcp.json` in the directory you run `claude` from.

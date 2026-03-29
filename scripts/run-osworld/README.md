# run-osworld

Run OSWorld desktop evaluation tasks using **Claude CLI + computer-use MCP**.

## Setup

```bash
# Initialize OSWorld submodule and install dependencies
bash scripts/run-osworld/setup.sh
```

This initializes the `vendor/OSWorld` git submodule (pinned to a specific commit) and installs its Python dependencies. No separate clone needed.

## Architecture

```
run.py  (host process)
├── DesktopEnv ──────────────────────────────► VM (Ubuntu desktop)
├── HTTP bridge  (localhost thread)                 ▲
│   ├── GET /screenshot → env.controller            │
│   ├── GET /accessibility_tree → env.controller    │  Docker / VMware
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

- Claude CLI (`claude`) installed and authenticated (`claude login`)
- Docker with KVM support (for Docker provider), or VMware/VirtualBox
- Python dependencies installed via `setup.sh`

## Usage

### Docker provider (recommended for GCP)

```bash
# Baseline (no skills)
python3 scripts/run-osworld/run.py \
    --provider_name docker \
    --domain chrome --skill_mode none

# With text skills
python3 scripts/run-osworld/run.py \
    --provider_name docker \
    --domain chrome --skill_mode text

# With multimodal skills
python3 scripts/run-osworld/run.py \
    --provider_name docker \
    --domain chrome --skill_mode multimodal

# Parallel (2 containers)
python3 scripts/run-osworld/run.py \
    --provider_name docker \
    --domain chrome --skill_mode none --parallel 2
```

### VMware provider

```bash
python3 scripts/run-osworld/run.py \
    --provider_name vmware \
    --path_to_vm /path/to/Ubuntu0.vmx \
    --domain chrome --skill_mode none
```

### Single task

```bash
python3 scripts/run-osworld/run.py \
    --provider_name docker \
    --specific_task_id <task_id>
```

## Key arguments

| Argument | Default | Description |
|---|---|---|
| `--osworld_root` | `vendor/OSWorld` | OSWorld repo path (submodule) |
| `--path_to_vm` | – | Path to `.vmx` file (required for VMware/VirtualBox) |
| `--provider_name` | `vmware` | `vmware`, `virtualbox`, or `docker` |
| `--model` | `claude-opus-4-6` | Claude model to use |
| `--skill_mode` | `none` | `none` (baseline), `text`, or `multimodal` |
| `--task_timeout` | `600` | Max seconds per task |
| `--domain` | `all` | Restrict to a single domain (e.g., `chrome`) |
| `--max_tasks` | `0` | Limit number of tasks (0 = all) |
| `--parallel` | `1` | Number of parallel workers |
| `--specific_task_id` | – | Run one task by ID |
| `--headless` | off | Run VM headless |

## Output structure

```
workspaces/
└── <model>/
    └── skill-<mode>/
        ├── summary.json
        └── <domain>/
            └── <task_id>/
                ├── result.txt
                ├── meta.json
                ├── claude_output.txt
                ├── final_screenshot.png
                ├── recording.mp4
                ├── screenshots/
                └── runtime.log
```

## Skill injection

Skills are loaded automatically by Claude CLI via `--plugin-dir`:
- `--skill_mode none` → no plugin directory (baseline)
- `--skill_mode text` → `plugins/osworld-text/` (text-only instructions)
- `--skill_mode multimodal` → `plugins/osworld-multimodal/` (instructions + screenshots)

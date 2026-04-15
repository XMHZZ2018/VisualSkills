# gym-anything Evaluation Runner

Run Claude on desktop GUI automation tasks using [gym-anything](../../vendor/gym-anything/) environments. Each task spins up a Docker container with a real desktop (Ubuntu + app), then launches Claude with only GUI tools (screenshot, click, type, etc.) to complete the task autonomously.

## Architecture

```
┌──────────────────────┐     HTTP      ┌──────────────────────┐
│  Docker 1 (Desktop)  │◄────────────►│     Bridge (host)     │
│  Ubuntu + GIMP/QGIS  │  screenshot  │  bridge.py :8766+     │
│  VNC + systemd       │  /actions    │                       │
└──────────────────────┘              └───────────▲───────────┘
                                                  │ MCP
                                      ┌───────────┴───────────┐
                                      │  Docker 2 (Claude CLI) │
                                      │  MCP server only       │
                                      │  No bash/file access   │
                                      └────────────────────────┘
```

- **Docker 1**: The desktop environment (e.g., Ubuntu + GIMP). Created by gym-anything.
- **Bridge**: Runs on the host, translates HTTP requests to gym-anything env API calls.
- **Docker 2**: Claude CLI with an MCP server that connects to the bridge. Claude can only use GUI tools — no Bash, Edit, Write, etc.

## Prerequisites

On the VM (GCP):

```bash
# Python dependencies
pip3 install --break-system-packages numpy Pillow jsonschema paramiko pycryptodome PyYAML requests docker anthropic

# Docker with sysbox runtime (for systemd-based environments)
# sysbox must be installed: https://github.com/nestybox/sysbox
docker info | grep -i runtime  # should show sysbox-runc

# Claude CLI Docker image
docker build -t ga-claude-cli -f scripts/run-gym-anything/Dockerfile.claude-cli scripts/run-gym-anything/

# Claude CLI authentication (OAuth — NOT an API key)
# Run `claude login` on the host first, then the credentials file
# (~/.claude/.credentials.json) is mounted into the Claude container.
```

## Quick Start

### Run a single task

```bash
cd /home/ziyan/MMSkills

python3 scripts/run-gym-anything/run.py \
    --env_dir vendor/gym-anything/benchmarks/cua_world/environments/gimp_env_all_fast \
    --task add_border \
    --model claude-opus-4-6 \
    --task_timeout 600 \
    --log_level INFO
```

### Run a split (train or test)

```bash
python3 scripts/run-gym-anything/run.py \
    --env_dir vendor/gym-anything/benchmarks/cua_world/environments/qgis_env \
    --split test \
    --model claude-opus-4-6 \
    --task_timeout 600 \
    --parallel 4 \
    --log_level INFO
```

### Run with a skill guide

```bash
# Text skill (text-only guide)
python3 scripts/run-gym-anything/run.py \
    --env_dir vendor/gym-anything/benchmarks/cua_world/environments/qgis_env \
    --task create_new_project \
    --skill_mode text \
    --model claude-opus-4-6

# Multimodal skill (guide + screenshots)
python3 scripts/run-gym-anything/run.py \
    --env_dir vendor/gym-anything/benchmarks/cua_world/environments/qgis_env \
    --task create_new_project \
    --skill_mode multimodal \
    --model claude-opus-4-6
```

### Run with a YAML config

```bash
bash scripts/run-gym-anything/run.sh --config scripts/run-gym-anything/configs/impress_baseline.yaml
```

Config format:

```yaml
model: claude-opus-4-6
skill_mode: none            # none | text | multimodal
env_dir: vendor/gym-anything/benchmarks/cua_world/environments/gimp_env_all_fast
result_dir: scripts/run-gym-anything/workspaces
task_timeout: 900
task_list:                  # optional — omit to run all tasks
  - add_border
  - brightness_contrast
num_parallel: 4
rerun: true                 # re-run even if results exist
log_level: INFO
```

## CLI Reference

```
python3 scripts/run-gym-anything/run.py [OPTIONS]

Required:
  --env_dir PATH          Path to gym-anything environment (contains env.json)

Task selection (pick one):
  --task TASK_ID          Run a single task
  --split {train,test,all}  Run all tasks in a split
  (neither)               Run all tasks in the environment

Options:
  --model MODEL           Claude model (default: claude-opus-4-6)
  --skill_mode MODE       none | text | multimodal (default: none)
  --task_timeout SECS     Max seconds per task (default: 1800)
  --result_dir DIR        Output directory (default: scripts/run-gym-anything/workspaces)
  --max_tasks N           Limit number of tasks (0 = all)
  --parallel N            Parallel workers, each gets its own env + bridge port (default: 1)
  --rerun                 Re-run tasks even if results exist
  --use_cache             Use Docker checkpoint cache for faster env init
  --log_level LEVEL       DEBUG | INFO | WARNING | ERROR
```

## Available Environments

| Environment | Tasks | Base Image | Notes |
|---|---|---|---|
| `gimp_env` | 7 | `ubuntu-gnome-systemd` | Dev/debug, VNC enabled |
| `gimp_env_all_fast` | 145 | `ubuntu-gnome-systemd_highres_gimp` | Pre-baked GIMP, 80/20 split |
| `gimp_env_osw` | 17 | `ubuntu-gnome-systemd_highres_gimp` | OSWorld-ported tasks |
| `qgis_env` | 79 | `ubuntu-gnome-systemd_highres` | 80/20 split |
| `libreoffice_impress_env` | varies | `ubuntu-gnome-systemd_highres` | Presentation tasks |
| `chrome_env` | varies | `ubuntu-gnome-systemd` | Browser tasks |

See all environments: `ls vendor/gym-anything/benchmarks/cua_world/environments/`
See all splits: `ls vendor/gym-anything/benchmarks/cua_world/splits/`

## Existing Run Scripts

Pre-configured shell scripts for common runs:

```bash
bash scripts/run-gym-anything/run_gimp_dev.sh           # 7 GIMP tasks, sanity check
bash scripts/run-gym-anything/run_qgis_test.sh           # QGIS test split, 4 parallel
bash scripts/run-gym-anything/run_qgis_test_multimodal.sh # QGIS test split with multimodal skill
bash scripts/run-gym-anything/run_qgis_official.sh       # QGIS via official gym-anything harness
```

## Result Structure

Results are saved to `workspaces/{model}/skill-{mode}/{env_name}/{task_id}/`:

```
workspaces/
  claude-opus-4-6/
    skill-none/
      gimp_env_all_fast/
        add_border/
          result.json          # score, elapsed time, verifier feedback
          score.txt            # just the score (0.0 to 1.0)
          prompt.txt           # full prompt sent to Claude
          screenshots/         # step-by-step screenshots (step_001.png, ...)
          claude_output.txt    # Claude's stream-JSON event log
          container_stdout.txt # Docker container logs
    skill-multimodal/
      ...
```

**result.json** example:
```json
{
  "task_id": "add_border",
  "score": 0.25,
  "elapsed_seconds": 118.5,
  "model": "claude-opus-4-6",
  "skill_mode": "none",
  "verifier_result": {
    "passed": false,
    "score": 25,
    "feedback": "Border distinct: ✅ | Content preserved: ✅ | Dimensions increased: ❌"
  }
}
```

## Trajectory Viewer

A Streamlit app for visually inspecting agent runs — view screenshots, action traces, skill loading, and scores across skill modes.

### Setup

```bash
pip install streamlit
```

### Launch

```bash
streamlit run scripts/trajectory_viewer.py
```

The viewer reads data from the VM via `gcloud compute ssh`. Configure with environment variables:

```bash
VM_NAME=osworld VM_ZONE=us-west1-c streamlit run scripts/trajectory_viewer.py
```

### Features

- **Task browser**: Select experiment (model), environment, task, and skill mode from the sidebar
- **Task description**: Shows the task prompt and evaluation criteria
- **Score summary**: Score, number of GUI steps, skill loads, and elapsed time
- **Verifier feedback**: Detailed breakdown of what passed/failed
- **Trajectory timeline**: Step-by-step replay of Claude's actions
  - GUI actions (click, type, scroll) with coordinates
  - Skill loading blocks (guide reading, image viewing) collapsed together
  - Screenshots after each GUI action (toggleable)
- **Prompt viewer**: Full prompt including system instructions and skill guide
- **Side-by-side comparison**: Compare runs across skill modes (none vs text vs multimodal)

### Color coding

| Mode | Color |
|---|---|
| No Skill | Red |
| Text Skill | Teal |
| Multimodal Skill | Blue |

## Troubleshooting

### Hooks fail immediately (`pre_start hook failed`)

The Docker image tag is shared across environments with the same `id` in env.json. If you switch between environments (e.g., `gimp_env` → `gimp_env_all_fast`), the cached image may be wrong. Fix:

```bash
docker rmi ga/example.gimp_env:0.1   # remove cached image
# then re-run — it will rebuild with the correct Dockerfile
```

### Screen resolution mismatch (`Capture area 1920x1080 outside 1024x768`)

The base image doesn't support the requested resolution. Use `_highres` variants or ensure VNC/Xvfb is configured for the correct resolution.

### Container not found during verification

The container was already stopped/removed before the verifier ran. This can happen if the env closes prematurely. Check the container logs in `workspaces/.../container_stdout.txt`.

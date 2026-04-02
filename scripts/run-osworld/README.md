# OSWorld Evaluation with Claude CLI

Run OSWorld desktop evaluation tasks using **Claude CLI** with an **MCP-based action loop** that mirrors OSWorld's original API-based agent, while using Docker isolation to enforce GUI-only interaction.

## Table of Contents

- [Why Claude CLI?](#why-claude-cli)
- [Architecture](#architecture)
- [MCP Tool Design](#mcp-tool-design)
- [Docker Isolation](#docker-isolation)
- [Setup](#setup)
- [Usage](#usage)
- [Output Structure](#output-structure)
- [Skill Injection](#skill-injection)
- [Arguments Reference](#arguments-reference)
- [GCP VM Setup](#gcp-vm-setup)
- [Troubleshooting](#troubleshooting)

## Why Claude CLI?

OSWorld's standard evaluation uses the Claude API with a custom Python action loop. We use **Claude CLI** instead because it supports **plugins/skills** — domain knowledge files that Claude reads at task time. This lets us inject per-domain guidance (e.g., "how to navigate Chrome settings") and measure whether skills improve task success rates.

The challenge: Claude CLI has built-in tools (Bash, Read, Write, etc.) that could bypass the GUI constraint. If Claude runs on the host, it could `docker exec` into the VM or run shell commands directly. We solve this with **Docker isolation** — Claude CLI runs in its own container with no Docker socket and no host network access, so built-in tools are sandboxed while skills still load normally.

## Architecture

```
Host (run.py — orchestrates everything)
  │
  ├── DesktopEnv ──────────────────────────────► VM container (QEMU guest)
  │                                                port 5000 → host:<mapped_port>
  │
  └── Docker: osworld-claude-cli container               ▲
        ├── bridge.py (:8765)                            │
        │     └── HTTP → host.docker.internal:<port> ────┘
        ├── MCP server: osworld-controller
        │     └── HTTP → bridge (:8765)
        └── claude -p "<task>" --mcp-config ...
              └── MCP tools → MCP server → bridge → VM
```

**Data flow for each action:**
1. Claude calls an MCP tool (e.g., `click(500, 300)`)
2. The `osworld-controller` MCP server scales coordinates from 1280×720 → native resolution
3. MCP server sends HTTP request to `bridge.py` at `localhost:8765`
4. Bridge wraps the command with pyautogui preamble and forwards to VM at `host.docker.internal:<port>`
5. VM executes the pyautogui command inside the QEMU guest
6. After 2s UI settle delay, MCP server captures a screenshot, resizes to 1280×720, and returns it to Claude

**Host-side evaluation:** After Claude exits, `run.py` calls `env.evaluate()` on the host using OSWorld's standard scoring via the VM's published ports. Claude never sees or influences the scoring.

## MCP Tool Design

The `osworld-controller` MCP server (`tools/osworld-controller/server.py`) provides the same action space as OSWorld's original `pyautogui`-based agent, ensuring evaluation comparability.

### Action Space Alignment

| OSWorld Original (API agent) | MCP Tool | pyautogui Command |
|---|---|---|
| `click(x, y, button)` | `click(x, y, button)` | `pyautogui.click(x, y)` / `rightClick` / `middle` |
| `double_click(x, y)` | `double_click(x, y)` | `pyautogui.doubleClick(x, y)` |
| `move_to(x, y)` | `move_to(x, y)` | `pyautogui.moveTo(x, y)` |
| `drag_to(sx, sy, ex, ey)` | `drag_to(sx, sy, ex, ey, duration)` | `pyautogui.moveTo(); pyautogui.dragTo()` |
| `scroll(x, y, clicks)` | `scroll(x, y, clicks)` | `pyautogui.scroll(clicks, x, y)` |
| `type(text)` | `type_text(text, interval)` | `pyautogui.write(text)` + `press('enter')` for newlines |
| `press(key)` | `key_press(key)` | `pyautogui.press(key)` |
| `hotkey(keys)` | `hotkey(keys)` | `pyautogui.hotkey(k1, k2, ...)` |
| `screenshot()` | `screenshot()` | GET /screenshot from VM |

### Observation Loop

The original OSWorld agent follows an **action → wait → screenshot** loop:
1. Execute a pyautogui action
2. Wait for UI to settle (default 2 seconds)
3. Capture a screenshot and return it as the observation

The MCP server replicates this exactly: every action tool calls `_exec_and_screenshot()`, which executes the command, sleeps 2 seconds, then captures and returns a screenshot. The `screenshot()` tool is also available standalone for observation-only steps.

### Coordinate Scaling

The VM runs at native resolution (default 1920×1080), but screenshots are resized to **1280×720** before being sent to Claude. This matches the resolution used by OSWorld's original Anthropic agent. When Claude generates coordinates (in 1280×720 space), the MCP server scales them back to native resolution before executing:

```
Model coordinates (1280×720) → scale by (native_w/1280, native_h/720) → VM coordinates (1920×1080)
```

### Command Execution

All actions are executed as pyautogui commands inside the VM's QEMU guest. The bridge prepends:
```python
import pyautogui; import time; pyautogui.FAILSAFE = False; <command>
```

This matches OSWorld's `PythonController`, which wraps commands the same way and sends them to the VM's `/execute` endpoint.

## Docker Isolation

### Problem

Claude CLI's built-in tools (Bash, Read, Write, etc.) could bypass the GUI-only evaluation constraint. Disabling them with `--disallowed-tools` breaks skill/plugin loading since Claude can't read SKILL.md files.

### Solution

Run Claude CLI in its own Docker container:
- **No Docker socket** — can't `docker exec` into the VM
- **No host network** — can't SSH to the VM
- **Read-only repo mount** — can read skills but can't modify the host
- **Built-in tools enabled** — Bash/Read/Write work inside the container but are sandboxed

### Why `host.docker.internal`?

The OSWorld VM container runs QEMU inside Docker. Port 5000 is inside the **QEMU guest OS**, not the Docker container. Docker's port mapping (iptables) makes it accessible from the host via `localhost:<mapped_port>`, but it is **not accessible** from other containers on the same Docker network — the container only has QEMU/nginx processes listening, not the guest's Python server.

The bridge connects to the VM via `host.docker.internal:<host_mapped_port>`, which routes through the Docker host gateway to the iptables-mapped port.

### Security Properties

| Threat | Mitigation |
|---|---|
| `docker exec` into VM | No Docker socket mounted |
| SSH/network to VM | No direct network path; bridge is the only proxy |
| Modify host files | Repo mounted read-only |
| Modify evaluation code | `run.py` runs on host, not in container |
| Persist state across tasks | Each task gets a fresh container |
| Read other tasks' data | Each container only sees its own `/workspace` |

### Mount Strategy

| Host Path | Container Path | Mode | Purpose |
|---|---|---|---|
| `<output_dir>` | `/workspace` | rw | Prompt, output, screenshots, signal |
| `MMSKILLS_ROOT` | `/opt/mmskills` | ro | Repo with skills, plugins, MCP server |
| `~/.claude/.credentials.json` | `/home/node/.claude/.credentials.json` | ro | OAuth credentials for Claude API |

The entire `MMSKILLS_ROOT` is mounted (not just the plugin dir) so that plugin symlinks resolve correctly. For example, `plugins/osworld-multimodal/skills → ../../skills` resolves to `/opt/mmskills/skills/` inside the container.

Only `.credentials.json` is mounted from `~/.claude/` (not the entire directory) to avoid config file restore loops that cause Claude CLI to hang.

## Setup

### 1. Initialize OSWorld submodule

```bash
bash scripts/run-osworld/setup.sh
```

This initializes the `vendor/OSWorld` git submodule and installs its Python dependencies.

### 2. Build the Claude CLI Docker image

```bash
docker build -t osworld-claude-cli \
  -f scripts/run-osworld/Dockerfile.claude-cli \
  scripts/run-osworld/
```

### 3. Install host dependencies

```bash
pip install docker
```

### 4. Authenticate Claude CLI

```bash
claude login
```

This creates `~/.claude/.credentials.json`, which is mounted into the container.

## Usage

### Docker provider (recommended)

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

# Parallel (4 workers, each gets its own VM + Claude container)
python3 scripts/run-osworld/run.py \
    --provider_name docker \
    --domain chrome --skill_mode none --parallel 4
```

### Single task

```bash
python3 scripts/run-osworld/run.py \
    --provider_name docker \
    --specific_task_id <task_id>
```

### VMware provider

```bash
python3 scripts/run-osworld/run.py \
    --provider_name vmware \
    --path_to_vm /path/to/Ubuntu0.vmx \
    --domain chrome --skill_mode none
```

## Output Structure

```
workspaces/
└── <model>/
    └── skill-<mode>/
        ├── summary.json
        └── <domain>/
            └── <task_id>/
                ├── result.txt          # Score (0.0 or 1.0)
                ├── meta.json           # Task metadata + timing
                ├── claude_output.txt   # Claude's full output
                ├── prompt.txt          # System prompt + task instruction
                ├── mcp_config.json     # MCP server config used
                ├── final_screenshot.png
                ├── recording.mp4       # Replay video from step screenshots
                ├── screenshots/        # Per-step screenshots (step_001.png, ...)
                └── runtime.log
```

## Skill Injection

Skills are loaded by Claude CLI via `--plugin-dir`:
- `--skill_mode none` → no plugin directory (baseline)
- `--skill_mode text` → `plugins/osworld-text/` (text-only instructions)
- `--skill_mode multimodal` → `plugins/osworld-multimodal/` (instructions + screenshots)

Inside the container, plugin paths resolve via the read-only mount at `/opt/mmskills/`.

## Arguments Reference

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
| `--rerun` | off | Re-run tasks even if results exist |
| `--result_dir` | `workspaces/` | Output directory |

## GCP VM Setup

For running evaluations on Google Cloud with Docker + KVM.

### 1. Create the VM

```bash
# Create a boot disk with nested virtualization
gcloud compute disks create osworld-disk \
    --zone=us-west1-b \
    --size=200GB \
    --type=pd-ssd \
    --image-family=debian-12 \
    --image-project=debian-cloud

# Create the VM with nested virtualization
gcloud compute instances create osworld \
    --zone=us-west1-b \
    --machine-type=n2-standard-16 \
    --boot-disk-name=osworld-disk \
    --enable-nested-virtualization
```

Key specs:
- **Machine type**: `n2-standard-16` (16 vCPUs, 64GB RAM) — needed for KVM + Docker overhead
- **Disk**: 200GB SSD — OS World qcow2 image is ~20GB, plus Docker layers
- **Nested virtualization**: required for KVM inside Docker containers

### 2. SSH config

Add to `~/.ssh/config` on your local machine:

```
Host osworld
    HostName <EXTERNAL_IP>
    User <USERNAME>
    IdentityFile ~/.ssh/google_compute_engine
```

### 3. Install dependencies on the VM

```bash
ssh osworld

# Install system packages
sudo apt-get update
sudo apt-get install -y docker.io qemu-kvm python3-pip python3-venv git rsync

# Add user to docker and kvm groups
sudo usermod -aG docker $USER
sudo usermod -aG kvm $USER

# Re-login for group changes
exit
ssh osworld

# Verify KVM and Docker
ls /dev/kvm
docker run hello-world
```

### 4. Install Claude CLI and authenticate

```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs
npm install -g @anthropic-ai/claude-code
claude login
```

### 5. Clone and set up

```bash
git clone --recurse-submodules https://github.com/XMHZZ2018/MMSkills.git
cd MMSkills
python3 -m venv venv
source venv/bin/activate
bash scripts/run-osworld/setup.sh
```

### 6. Prepare the OS World Docker image

```bash
cd ~/MMSkills
mkdir -p docker_vm_data && cd docker_vm_data
# Download qcow2 image from OSWorld's official source (see OSWorld README)
cd ..
# Place in vendor/OSWorld/docker_vm_data/ or symlink there
```

### 7. Build Claude CLI image and run

```bash
docker build -t osworld-claude-cli \
  -f scripts/run-osworld/Dockerfile.claude-cli scripts/run-osworld/

# Run evaluation
source venv/bin/activate
python3 scripts/run-osworld/run.py \
    --provider_name docker \
    --domain chrome --skill_mode none --parallel 4
```

### 8. Sync results back

```bash
# From local machine
rsync -avz osworld:~/MMSkills/scripts/run-osworld/workspaces/ scripts/run-osworld/workspaces/
```

## Troubleshooting

### Claude container not visible in `docker ps`

The Claude CLI container runs only for the duration of a single task (typically 1-10 minutes), then is removed. You'll only see it during active task execution. The OS World VM container persists across tasks within a worker.

### KVM not available

```bash
grep -c vmx /proc/cpuinfo   # should be > 0
# If 0, recreate the VM with --enable-nested-virtualization
```

### Disk full

```bash
# Resize disk (from local machine)
gcloud compute disks resize osworld-disk --zone=us-west1-b --size=300GB

# Expand filesystem (on VM)
sudo growpart /dev/sda 1
sudo resize2fs /dev/sda1
```

### Docker container stuck booting

```bash
docker kill $(docker ps -q)
docker rm $(docker ps -aq)
```

### growpart not found

```bash
sudo apt-get install cloud-guest-utils
```

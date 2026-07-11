# OSExpert-Eval Evaluation: Docker Isolation Design

## Problem

OSExpert-Eval evaluation requires Claude to interact with a virtual machine desktop through GUI actions (click, type, screenshot). The standard approach uses the Claude API with a custom action loop — but we want to use **Claude CLI** so we can leverage its plugin/skill system for injecting domain knowledge.

The challenge: Claude CLI has built-in tools (Bash, Read, Write, etc.) that could bypass the GUI constraint. If Claude runs on the same host as the VM containers, it could `docker exec` into the VM, run shell commands directly, or read files — violating the GUI-only evaluation protocol.

### Failed approach: disabling built-in tools

We first tried `--disallowed-tools Bash,Read,Write,Edit,Glob,Grep,Agent,NotebookEdit` to block all built-in tools. This prevents cheating but also **breaks skill/plugin loading** — Claude can't read SKILL.md files from the plugin directory.

### Solution: Docker isolation

Run Claude CLI inside its own Docker container with:
- **No Docker socket** — can't `docker exec` into VM containers
- **No host network** — can't SSH to the VM
- **Read-only repo mount** — can read skills but can't modify the host
- **Built-in tools enabled** — Bash/Read/Write work inside the container but are sandboxed

## Architecture

```
Host (run.py)
  │
  ├── Worker 0
  │   ├── OSExpert-Eval VM container (QEMU guest, managed by DesktopEnv)
  │   │     port 5000 (guest) → host-mapped port (e.g. 5001)
  │   │
  │   └── Claude CLI container (osexpert-claude-cli)
  │         bridge.py :8765 → host.docker.internal:<host_port> → VM:5000
  │         claude CLI → MCP server → bridge → VM
  │         /opt/mmskills (read-only mount of repo)
  │         /workspace (read-write mount of output dir)
  │         NO docker socket
  │
  ├── Worker 1 (same pattern, different VM + Claude container)
  ├── Worker 2 ...
  └── Worker 3 ...
```

### Why host.docker.internal instead of container-to-container?

The OSExpert-Eval VM container runs QEMU inside Docker. Port 5000 is inside the **QEMU guest OS**, not the Docker container itself. Docker's port mapping (iptables) makes it accessible from the host via `localhost:<mapped_port>`, but it's **not accessible** from other containers on the same Docker network — because the container only has QEMU/nginx processes listening, not the guest's Python server.

Solution: the bridge inside the Claude container connects to the VM via `host.docker.internal:<host_mapped_port>`, which routes through the Docker host gateway to the iptables-mapped port.

## Components

### 1. `Dockerfile.claude-cli`

Builds the Claude CLI container image:
- Base: `node:20-slim`
- Installs: Python 3, Claude CLI (`@anthropic-ai/claude-code`)
- Python venv at `/opt/mcp-venv` with `mcp`, `httpx`, `Pillow` (for MCP server)
- Runs as `node` user (uid 1000) — Claude CLI refuses `--dangerously-skip-permissions` as root
- uid 1000 matches the typical host user, so bind-mounted files have correct permissions

```bash
docker build -t osexpert-claude-cli -f scripts/run-osexpert/Dockerfile.claude-cli scripts/run-osexpert/
```

### 2. `bridge.py`

Standalone HTTP bridge running inside the Claude CLI container. Translates between the MCP server's expected API and the VM's raw HTTP API:

| Bridge endpoint | VM endpoint | Notes |
|---|---|---|
| `GET /screenshot` | `GET http://<vm>/screenshot` | Returns base64-wrapped PNG, saves step screenshots |
| `POST /execute_python` | `POST http://<vm>/execute` | Wraps command with pyautogui preamble |
| `GET /accessibility_tree` | `GET http://<vm>/accessibility` | Returns AT string |
| `POST /signal` | (writes file) | Writes signal to `/workspace/signal.txt` |

The bridge reads `OSEXPERT_VM_URL` from environment (set by `run.py` to `http://host.docker.internal:<port>`).

### 3. `entrypoint.sh`

Container entrypoint:
1. Starts `bridge.py` in background
2. Polls `localhost:8765/screenshot` until bridge is ready (up to 30s)
3. Reads prompt from `/workspace/prompt.txt`
4. Runs `claude -p "$PROMPT" "$@"` — CLI args passed as CMD
5. Writes output to `/workspace/claude_output.txt` and exit code to `/workspace/exit_code.txt`

### 4. `run.py` (modified)

Host-side orchestrator. Key changes from the original single-process design:

**Removed:**
- `_BridgeState`, `_make_handler`, `_BridgeHandler` — no more in-process HTTP bridge
- `_free_port()` — no more host-side bridge ports
- Direct `subprocess.run(claude ...)` — replaced with Docker container
- `--disallowed-tools` — no longer needed, container provides isolation

**Added:**
- `_get_vm_host_port(env)` — reads the host-mapped port from the Docker provider
- `_run_claude_in_docker(...)` — creates and runs Claude CLI container with bind mounts, waits for completion

**Task flow:**
```
run_task():
  1. env.reset(task_config=example)     # Creates/resets VM container
  2. vm_port = _get_vm_host_port(env)   # Get host-mapped port for VM:5000
  3. Write prompt.txt + mcp_config.json to output_dir
  4. _run_claude_in_docker(...)          # Run Claude in container
  5. Read signal from output_dir/signal.txt
  6. env.step(signal) + env.evaluate()  # Score on host via published ports
```

**Container configuration:**
```python
docker_client.containers.run(
    "osexpert-claude-cli",
    command=cli_args,              # --mcp-config, --model, etc.
    environment={
        "CLAUDE_CODE_DISABLE_AUTO_MEMORY": "1",
        "OSEXPERT_VM_URL": f"http://host.docker.internal:{vm_port}",
    },
    extra_hosts={"host.docker.internal": "host-gateway"},
    volumes={
        output_dir: "/workspace:rw",
        MMSKILLS_ROOT: "/opt/mmskills:ro",
        "~/.claude/.credentials.json": "/home/node/.claude/.credentials.json:ro",
    },
    # No docker socket mounted
)
```

### 5. `tools/osexpert-controller/server.py` (unchanged)

MCP server that runs inside the Claude container. Connects to the bridge at `http://127.0.0.1:8765` (both in the same container). Provides screenshot/click/type/hotkey/scroll tools to Claude.

## Mount Strategy

| Host path | Container path | Mode | Purpose |
|---|---|---|---|
| `output_dir` | `/workspace` | rw | Prompt, output, screenshots, signal |
| `MMSKILLS_ROOT` | `/opt/mmskills` | ro | Repo with skills, plugins, MCP server |
| `~/.claude/.credentials.json` | `/home/node/.claude/.credentials.json` | ro | OAuth credentials for Claude API |

The entire `MMSKILLS_ROOT` is mounted (not just the plugin dir) so that plugin symlinks resolve correctly. For example, `plugins/osexpert-multimodal/skills → ../../skills` resolves to `/opt/mmskills/skills/` inside the container.

Only `.credentials.json` is mounted from `~/.claude/` (not the entire directory) to avoid config file restore loops that cause Claude CLI to hang.

## Security Properties

| Threat | Mitigation |
|---|---|
| `docker exec` into VM | No Docker socket mounted |
| SSH/network to VM | No direct network path; bridge is the only proxy |
| Modify host files | Repo mounted read-only |
| Modify evaluation code | `run.py` runs on host, not in container |
| Persist state across tasks | Each task gets a fresh container |
| Read other tasks' data | Each container only sees its own `/workspace` |

Note: The Claude container can reach `host.docker.internal` (needed for the bridge→VM path). This means it could theoretically access other host services. Full network isolation (internal Docker network) is not possible due to the QEMU port forwarding limitation. The primary isolation goal — preventing Claude from directly manipulating the VM outside the GUI — is achieved.

## Comparison with Original API-Based Approach

| Aspect | Claude API + Loop | Claude CLI (old) | Claude CLI + Docker (current) |
|---|---|---|---|
| Action loop | Custom Python loop | Claude CLI built-in | Claude CLI built-in |
| Tool definition | API tool schema | MCP server | MCP server |
| Skill injection | N/A | `--plugin-dir` | `--plugin-dir` (inside container) |
| GUI enforcement | Only GUI tools defined | `--disallowed-tools` (breaks skills) | Docker isolation (skills work) |
| Built-in tools | N/A | Disabled | Enabled but sandboxed |
| Parallelism | Custom threading | `--parallel` workers | `--parallel` workers |

## Verification

```bash
# 1. Build image
docker build -t osexpert-claude-cli \
  -f scripts/run-osexpert/Dockerfile.claude-cli scripts/run-osexpert/

# 2. Run single task
python3 scripts/run-osexpert/run.py \
  --provider_name docker \
  --specific_task_id 06fe7178-4491-4589-810f-2e2bc9502122 \
  --skill_mode none --model claude-sonnet-4-6

# 3. Run with skills
python3 scripts/run-osexpert/run.py \
  --provider_name docker \
  --domain chrome --skill_mode multimodal \
  --model claude-sonnet-4-6

# 4. Run parallel
python3 scripts/run-osexpert/run.py \
  --provider_name docker \
  --domain libreoffice_impress --parallel 4 \
  --skill_mode none --model claude-sonnet-4-6

# 5. Verify: check screenshots saved, scores match baseline
ls workspaces/<model>/skill-none/<domain>/<task_id>/screenshots/
cat workspaces/<model>/skill-none/<domain>/<task_id>/result.txt
```

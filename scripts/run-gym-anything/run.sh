#!/usr/bin/env bash
set -euo pipefail

# ── gym-anything evaluation runner ──────────────────────────────────────────
# Usage: bash run.sh --config configs/impress_baseline.yaml [--rebuild]
#
# Reads a YAML config, discovers tasks, builds Docker images if needed,
# then runs tasks in parallel with unique bridge ports per task.
# ────────────────────────────────────────────────────────────────────────────

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
MMSKILLS_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# ── parse args ──────────────────────────────────────────────────────────────

CONFIG=""
REBUILD=false

while [[ $# -gt 0 ]]; do
    case "$1" in
        --config)  CONFIG="$2"; shift 2 ;;
        --rebuild) REBUILD=true; shift ;;
        -h|--help)
            echo "Usage: $0 --config <config.yaml> [--rebuild]"
            echo "  --config   Path to YAML config file"
            echo "  --rebuild  Force rebuild of Claude CLI Docker image"
            exit 0
            ;;
        *) echo "Unknown argument: $1"; exit 1 ;;
    esac
done

if [[ -z "$CONFIG" ]]; then
    echo "ERROR: --config is required"
    echo "Usage: $0 --config <config.yaml> [--rebuild]"
    exit 1
fi

if [[ ! -f "$CONFIG" ]]; then
    echo "ERROR: Config file not found: $CONFIG"
    exit 1
fi

# ── read config ─────────────────────────────────────────────────────────────

read_cfg() {
    python3 -c "
import yaml, sys
cfg = yaml.safe_load(open(sys.argv[1]))
print(cfg.get(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else ''))
" "$CONFIG" "$1" "${2:-}"
}

NUM_PARALLEL=$(read_cfg num_parallel 1)
PORT_BASE=$(read_cfg bridge_port_base 8766)
IMAGE=$(read_cfg claude_cli_image ga-claude-cli)
RERUN=$(read_cfg rerun false)

echo "════════════════════════════════════════════════════════════"
echo "  gym-anything evaluation runner"
echo "  Config: $CONFIG"
echo "  Parallel: $NUM_PARALLEL"
echo "════════════════════════════════════════════════════════════"

# ── cleanup stale containers ────────────────────────────────────────────────

echo "Cleaning up stale containers..."
docker ps -a --filter "name=ga_" --filter "status=exited" -q 2>/dev/null | xargs -r docker rm -f 2>/dev/null || true
docker ps -a --filter "name=ga-claude-" --filter "status=exited" -q 2>/dev/null | xargs -r docker rm -f 2>/dev/null || true

# ── build Claude CLI image ──────────────────────────────────────────────────

if $REBUILD || ! docker image inspect "$IMAGE" > /dev/null 2>&1; then
    echo "Building Docker image: $IMAGE ..."
    docker build -t "$IMAGE" -f "$SCRIPT_DIR/Dockerfile.claude-cli" "$SCRIPT_DIR"
else
    echo "Docker image '$IMAGE' exists (use --rebuild to force)"
fi

# ── discover tasks ──────────────────────────────────────────────────────────

TASKS=$(python3 "$SCRIPT_DIR/run_task.py" --config "$CONFIG" --discover-tasks)
NUM_TASKS=$(echo "$TASKS" | wc -l | tr -d ' ')

if [[ -z "$TASKS" || "$NUM_TASKS" -eq 0 ]]; then
    echo "ERROR: No tasks found"
    exit 1
fi

# Filter out already-completed tasks (unless rerun=true)
if [[ "$RERUN" != "true" && "$RERUN" != "True" ]]; then
    RESULT_DIR=$(read_cfg result_dir scripts/run-gym-anything/workspaces)
    MODEL=$(read_cfg model claude-opus-4-6)
    SKILL=$(read_cfg skill_mode none)
    ENV_NAME=$(python3 -c "
import yaml, sys, os
cfg = yaml.safe_load(open(sys.argv[1]))
print(os.path.basename(cfg.get('env_dir', '')))
" "$CONFIG")

    PENDING=""
    SKIPPED=0
    while IFS= read -r task_id; do
        # Resolve result_dir the same way run_task.py does
        SCORE_FILE=$(python3 -c "
import yaml, sys, os
cfg = yaml.safe_load(open(sys.argv[1]))
rd = cfg.get('result_dir', 'scripts/run-gym-anything/workspaces')
if not os.path.isabs(rd):
    rd = os.path.join(sys.argv[2], rd)
print(os.path.join(rd, sys.argv[3], f'skill-{sys.argv[4]}', sys.argv[5], sys.argv[6], 'score.txt'))
" "$CONFIG" "$MMSKILLS_ROOT" "$MODEL" "$SKILL" "$ENV_NAME" "$task_id")

        if [[ -f "$SCORE_FILE" ]]; then
            SKIPPED=$((SKIPPED + 1))
        else
            PENDING="${PENDING}${task_id}"$'\n'
        fi
    done <<< "$TASKS"

    if [[ $SKIPPED -gt 0 ]]; then
        echo "Skipping $SKIPPED tasks with existing results (use rerun: true to override)"
    fi

    TASKS="${PENDING%$'\n'}"  # trim trailing newline
    NUM_TASKS=$(echo "$TASKS" | grep -c . || true)

    if [[ "$NUM_TASKS" -eq 0 ]]; then
        echo "All tasks already completed."
        python3 "$SCRIPT_DIR/run_task.py" --config "$CONFIG" --summarize
        exit 0
    fi
fi

echo "Running $NUM_TASKS task(s) with $NUM_PARALLEL parallel worker(s)"
echo ""

# Save config to result dir for reproducibility
RESULT_BASE=$(python3 -c "
import yaml, sys, os
cfg = yaml.safe_load(open(sys.argv[1]))
rd = cfg.get('result_dir', 'scripts/run-gym-anything/workspaces')
if not os.path.isabs(rd):
    rd = os.path.join(sys.argv[2], rd)
print(rd)
" "$CONFIG" "$MMSKILLS_ROOT")
mkdir -p "$RESULT_BASE"
cp "$CONFIG" "$RESULT_BASE/last_run_config.yaml"

# ── run tasks ───────────────────────────────────────────────────────────────
# Each task gets a unique bridge port: PORT_BASE + task_index.
# xargs -P runs up to NUM_PARALLEL tasks concurrently.

IDX=0
while IFS= read -r task_id; do
    PORT=$((PORT_BASE + IDX))
    echo "$task_id $PORT"
    IDX=$((IDX + 1))
done <<< "$TASKS" | xargs -P "$NUM_PARALLEL" -L 1 bash -c '
    TASK_ID="$0"
    PORT="$1"
    echo "[START] $TASK_ID (port $PORT)"
    python3 "'"$SCRIPT_DIR"'/run_task.py" \
        --config "'"$CONFIG"'" \
        --task "$TASK_ID" \
        --bridge_port "$PORT"
    EXIT=$?
    if [[ $EXIT -eq 0 ]]; then
        echo "[DONE]  $TASK_ID (port $PORT) - success"
    else
        echo "[DONE]  $TASK_ID (port $PORT) - exit code $EXIT"
    fi
'

# ── summary ─────────────────────────────────────────────────────────────────

echo ""
python3 "$SCRIPT_DIR/run_task.py" --config "$CONFIG" --summarize

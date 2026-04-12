#!/bin/bash
# Run QGIS test split using the OFFICIAL gym-anything harness (ClaudeAgent).
# Usage: bash scripts/run-gym-anything/run_qgis_official.sh
set -euo pipefail

cd /home/ziyan/MMSkills/vendor/gym-anything

# Pull latest code
git -C /home/ziyan/MMSkills pull origin main

# Ensure dependencies
pip3 install --break-system-packages -q anthropic litellm openai python-dotenv tqdm pillow numpy jsonschema paramiko pycryptodome PyYAML requests docker 2>/dev/null

# Clean up any leftover containers
pkill -f 'run_single' 2>/dev/null || true
pkill -f 'run_batch' 2>/dev/null || true
sleep 2
docker rm -f $(docker ps -aq) 2>/dev/null || true

export ANTHROPIC_API_KEY="${ANTHROPIC_API_KEY}"
export PYTHONPATH="/home/ziyan/MMSkills/vendor/gym-anything/src:${PYTHONPATH:-}"

MODEL="claude-opus-4-6"
EXP_NAME="official-baseline"
ENV_DIR="benchmarks/cua_world/environments/qgis_env"
MAX_STEPS=50
LOG="/tmp/ga_qgis_official.log"

echo "Starting QGIS official harness run at $(date)"
echo "Log: $LOG"

python3 -m agents.evaluation.run_batch \
    --env_dir "$ENV_DIR" \
    --split test \
    --agent ClaudeAgent \
    --model "$MODEL" \
    --exp_name "$EXP_NAME" \
    --max_steps "$MAX_STEPS" \
    --use_cache \
    2>&1 | tee "$LOG"

echo "Finished at $(date)"

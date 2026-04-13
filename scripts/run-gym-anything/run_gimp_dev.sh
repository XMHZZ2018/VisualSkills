#!/bin/bash
# Run GIMP dev environment (7 tasks) as a sanity check.
# Usage: bash scripts/run-gym-anything/run_gimp_dev.sh
set -euo pipefail

cd /home/ziyan/MMSkills

# Pull latest code
git pull origin main

# Ensure dependencies
pip3 install --break-system-packages -q numpy Pillow jsonschema paramiko pycryptodome PyYAML requests docker 2>/dev/null

# Clean up any leftover containers
pkill -f 'run.py' 2>/dev/null || true
sleep 2
docker rm -f $(docker ps -aq) 2>/dev/null || true

ENV_DIR="vendor/gym-anything/benchmarks/cua_world/environments/gimp_env"
LOG="/tmp/ga_gimp_dev.log"

echo "Starting GIMP dev run (7 tasks) at $(date)"
echo "Log: $LOG"

python3 scripts/run-gym-anything/run.py \
    --env_dir "$ENV_DIR" \
    --split train \
    --model claude-opus-4-6 \
    --task_timeout 600 \
    --parallel 4 \
    --log_level INFO \
    2>&1 | tee "$LOG"

echo "Finished at $(date)"

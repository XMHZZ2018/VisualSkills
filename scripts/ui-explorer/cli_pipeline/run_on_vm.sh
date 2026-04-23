#!/usr/bin/env bash
# Rsync the cli_pipeline scripts to the osworld GCP VM and kick off a run.
#
# Usage:  ./run_on_vm.sh [impress]   # impress is default
#
# Requires:  gcloud auth, rsync, and VM already provisioned with
#            ~/MMSkills cloned + ga-claude-cli docker image built +
#            claude CLI logged in.

set -euo pipefail

CONFIG="${1:-impress}"
VM="osworld"
ZONE="us-west1-c"
REMOTE_ROOT='~/MMSkills'

HERE="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$HERE/../../.." && pwd)"

echo "[sync] cli_pipeline/ -> VM:${REMOTE_ROOT}/scripts/ui-explorer/cli_pipeline/"
gcloud compute scp --zone="$ZONE" --recurse \
    "$HERE" \
    "${VM}:~/MMSkills/scripts/ui-explorer/" >/dev/null

echo "[sync] Ensure entrypoint.sh / bridge.py already present (part of existing repo)"

LOG_TAG="$(date +%Y%m%d_%H%M%S)"
REMOTE_LOG="/tmp/ui_explore_${LOG_TAG}.log"

echo "[launch] running orchestrator on VM, log -> ${REMOTE_LOG}"
gcloud compute ssh "$VM" --zone="$ZONE" --command "bash -lc '
set -e
cd ~/MMSkills
source ~/osworld-env/bin/activate
cd scripts/ui-explorer/cli_pipeline
# Run in background, detach from SSH session.
nohup python orchestrator.py --config configs/${CONFIG}.yaml \
    > ${REMOTE_LOG} 2>&1 &
echo \"PID=\$!\"
sleep 3
tail -n 40 ${REMOTE_LOG}
'"

echo ""
echo "▶ Tail remote log:"
echo "   gcloud compute ssh ${VM} --zone=${ZONE} --command 'tail -f ${REMOTE_LOG}'"

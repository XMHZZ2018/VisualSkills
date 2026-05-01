#!/usr/bin/env bash
# UI-explorer skill generation pipeline (v3).
#
# v3 always runs on the GCP osworld VM, since phases 1-3 spin up gym-anything
# Docker containers (sysbox runtime) and phases 4-5 read/write the same
# repo-relative output_dir.  This script:
#
#   1. rsyncs preprocess/skill-pipeline/v3/ from local → VM
#      (so unsynced local edits to scripts/configs/mapping take effect),
#   2. SSHs into the VM and runs the requested phase(s) under
#      ~/MMSkills/preprocess/skill-pipeline/v3/,
#   3. (after phase 4 / 5) rsyncs the resulting skills/ directories back
#      so the local tree stays in sync.
#
# Usage:
#   ./run.sh --config configs/impress.yaml                # phases 1-3
#   ./run.sh --config configs/impress.yaml --phase 4      # inline
#   ./run.sh --config configs/impress.yaml --phase 5      # text-v3
#   ./run.sh --config configs/impress.yaml --force        # wipe output_dir first
#   ./run.sh --config configs/impress.yaml --foreground   # don't nohup
#
# Requires:  gcloud auth, and VM already provisioned with
#            ~/MMSkills cloned + ga-claude-cli docker image built +
#            claude CLI logged in + python venv at ~/osworld-env.

set -euo pipefail

CONFIG=""
PHASE=""
FORCE=""
FOREGROUND=0
EXTRA=()

while [[ $# -gt 0 ]]; do
    case "$1" in
        --config)      CONFIG="$2"; shift 2 ;;
        --phase)       PHASE="$2"; shift 2 ;;
        --force)       FORCE="--force"; shift ;;
        --foreground)  FOREGROUND=1; shift ;;
        -h|--help)
            cat <<EOF
Usage: $0 --config <path> [options]

Options:
  --phase N      Run only phase N (1..5).  Default: phases 1-3.
                 Phases 4 and 5 are opt-in.
  --force        Wipe output_dir on the VM before phase 1.
  --foreground   Stream the remote log instead of nohup-ing.

Phases:
  1-3 plan/workers/assemble  (orchestrator.py — spins up Docker)
  4   inline regions+images into mm-v1 → mm-v3   (deterministic)
  5   derive text-v3 from mm-v3                  (Claude API, parallel)

Examples:
  $0 --config configs/impress.yaml
  $0 --config configs/impress.yaml --phase 4
  $0 --config configs/impress.yaml --phase 5
EOF
            exit 0
            ;;
        *)             EXTRA+=("$1"); shift ;;
    esac
done

if [[ -z "$CONFIG" ]]; then
    echo "Error: --config is required (run '$0 --help')" >&2
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Resolve config path locally (config may live in v3/configs/ or be absolute)
if [[ ! -f "$CONFIG" ]]; then
    if [[ -f "$SCRIPT_DIR/$CONFIG" ]]; then
        CONFIG="$SCRIPT_DIR/$CONFIG"
    else
        echo "Error: config not found: $CONFIG" >&2
        exit 1
    fi
fi

# Domain (for selective rsync-back) and output_dir (relative to repo root).
DOMAIN=$(python3 -c "
import yaml
c = yaml.safe_load(open('$CONFIG'))
d = c.get('domain') or c['env_dir'].rstrip('/').split('/')[-1].removesuffix('_env')
print(d)
")
OUTPUT_DIR_REL=$(python3 -c "
import yaml
c = yaml.safe_load(open('$CONFIG'))
print(c['output_dir'])
")
APP_NAME=$(python3 -c "import yaml; c=yaml.safe_load(open('$CONFIG')); print(c.get('app_name', ''))")
APP_VERSION=$(python3 -c "import yaml; c=yaml.safe_load(open('$CONFIG')); print(c.get('app_version', ''))")
PARALLEL=$(python3 -c "import yaml; c=yaml.safe_load(open('$CONFIG')); print(c.get('text_v3_parallel', 4))")

# Convert local config path to VM-side path (must live under v3/configs/).
CONFIG_REL="${CONFIG#$SCRIPT_DIR/}"
if [[ "$CONFIG_REL" == /* ]]; then
    echo "Error: --config must live under $SCRIPT_DIR (got absolute path: $CONFIG)" >&2
    exit 1
fi

VM="osworld"
ZONE="us-west1-c"
REMOTE_REPO="\$HOME/MMSkills"
REMOTE_PIPELINE="${REMOTE_REPO}/preprocess/skill-pipeline/v3"

echo "[v3] domain=$DOMAIN  config=$CONFIG_REL  phase=${PHASE:-1-3}"

# ── 1. Sync local v3/ scripts+configs (and the curated mapping) to the VM ──
echo "[sync] -> ${VM}:${REMOTE_PIPELINE}/"
gcloud compute scp --zone="$ZONE" --recurse \
    "$SCRIPT_DIR/" \
    "${VM}:~/MMSkills/preprocess/skill-pipeline/" >/dev/null

# ── 2. Build remote command for the requested phase ──
EXTRA_STR=""
for a in "${EXTRA[@]:-}"; do
    EXTRA_STR="${EXTRA_STR} ${a}"
done

case "${PHASE:-}" in
    "" | 1 | 2 | 3)
        REMOTE_CMD="cd ${REMOTE_PIPELINE} && \
python -c 'import PIL' 2>/dev/null || pip install --quiet Pillow ; \
python -u orchestrator.py --config ${CONFIG_REL} ${FORCE} ${EXTRA_STR}"
        ;;
    4)
        REMOTE_CMD="cd ${REMOTE_PIPELINE} && \
python -u inline_into_mm_v1.py --pipeline-dir ${REMOTE_REPO}/${OUTPUT_DIR_REL} ${EXTRA_STR}"
        ;;
    5)
        REMOTE_CMD="cd ${REMOTE_PIPELINE} && \
python -u derive_text_v3.py \
    --domain ${DOMAIN} \
    --app-name '${APP_NAME}' \
    --app-version '${APP_VERSION}' \
    --parallel ${PARALLEL} ${EXTRA_STR}"
        ;;
    *)
        echo "Error: --phase must be 1, 2, 3, 4, or 5 (got: $PHASE)" >&2
        exit 1
        ;;
esac

LOG_TAG="$(date +%Y%m%d_%H%M%S)"
REMOTE_LOG="/tmp/v3_${DOMAIN}_p${PHASE:-123}_${LOG_TAG}.log"

# ── 3. Run on VM ──
if [[ "$FOREGROUND" -eq 1 ]]; then
    echo "[run] foreground on ${VM}: ${REMOTE_CMD}"
    gcloud compute ssh "$VM" --zone="$ZONE" --command "bash -lc '
set -e
source ~/osworld-env/bin/activate
${REMOTE_CMD} 2>&1 | tee ${REMOTE_LOG}
'"
else
    echo "[run] background on ${VM}: log=${REMOTE_LOG}"
    gcloud compute ssh "$VM" --zone="$ZONE" --command "bash -lc '
set -e
source ~/osworld-env/bin/activate
nohup bash -c \"${REMOTE_CMD}\" > ${REMOTE_LOG} 2>&1 &
echo \"PID=\$!\"
sleep 3
tail -n 40 ${REMOTE_LOG} 2>/dev/null || true
'"
fi

echo ""
echo "▶ Tail remote log:"
echo "   gcloud compute ssh ${VM} --zone=${ZONE} --command 'tail -f ${REMOTE_LOG}'"

# ── 4. Pull skill outputs back after phases 4 / 5 ──
if [[ "${PHASE:-}" == "4" || "${PHASE:-}" == "5" ]]; then
    if [[ "$FOREGROUND" -eq 1 ]]; then
        echo "[sync-back] skills/${DOMAIN}-knowledge-{multimodal,text}-v3/ <- VM"
        for variant in multimodal text; do
            REMOTE_SKILL="~/MMSkills/skills/${DOMAIN}-knowledge-${variant}-v3"
            gcloud compute scp --zone="$ZONE" --recurse \
                "${VM}:${REMOTE_SKILL}" \
                "$SCRIPT_DIR/../../../skills/" 2>/dev/null || \
                echo "  (skipped ${variant}: not present on VM yet)"
        done
    else
        echo "(background mode — re-run with --phase ${PHASE} --foreground, or rsync skills/ back manually after the job finishes)"
    fi
fi

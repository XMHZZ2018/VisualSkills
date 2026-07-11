#!/usr/bin/env bash
# UI-explorer skill generation pipeline (Stage 2).
#
# Stage 2 always runs on the GCP osworld VM, since phases 1-3 spin up CUA-World
# Docker containers (sysbox runtime) and phases 4-5 read/write the same
# repo-relative output_dir.  This script:
#
#   1. rsyncs preprocess/skill-pipeline/stage2/ from local → VM
#      (so unsynced local edits to scripts/configs/mapping take effect),
#   2. SSHs into the VM and runs the requested phase(s) under
#      ~/MMSkills/preprocess/skill-pipeline/stage2/,
#   3. (after phases that touch skills/) rsyncs the resulting
#      skills/ directories back so the local tree stays in sync.
#
# Usage:
#   ./run.sh --config configs/impress.yaml                        # phases 1-3
#   ./run.sh --config configs/impress.yaml --phase 4              # inline (mm)
#   ./run.sh --config configs/impress.yaml --phase 5              # derive text
#   ./run.sh --config configs/impress.yaml --phase all            # full chain
#   ./run.sh --config configs/impress.yaml --mode both --text-source independent
#   ./run.sh --config configs/impress.yaml --force                # wipe first
#   ./run.sh --config configs/impress.yaml --foreground           # no nohup
#
# Requires:  gcloud auth, and VM already provisioned with
#            ~/MMSkills cloned + cw-claude-cli docker image built +
#            claude CLI logged in + python venv at ~/osworld-env.

set -euo pipefail

CONFIG=""
PHASE=""
MODE="both"
TEXT_SOURCE="derived"
FORCE=""
FOREGROUND=0
EXTRA=()

while [[ $# -gt 0 ]]; do
    case "$1" in
        --config)       CONFIG="$2"; shift 2 ;;
        --phase)        PHASE="$2"; shift 2 ;;
        --mode)         MODE="$2"; shift 2 ;;
        --text-source)  TEXT_SOURCE="$2"; shift 2 ;;
        --force)        FORCE="--force"; shift ;;
        --foreground)   FOREGROUND=1; shift ;;
        -h|--help)
            cat <<EOF
Usage: $0 --config <path> [options]

Options:
  --mode {multimodal,text,both}         default: both
      Which artifacts to produce.
  --text-source {independent,derived}   default: derived (matches paper)
      How the text-stage2 artifact is produced:
        derived     — verbalize figure refs in the multimodal guide
                      (Phase 5, derive_text.py). Prose is identical to
                      mm-stage2 up to those refs. Isolates the modality
                      contribution for the ablation.
        independent — text-only assembler pass over the same worker notes
                      (Phase 4t). Text prose is genuinely independent of
                      the multimodal prose. Runs alongside the mm chain
                      when --mode both.
  --phase N      Run only phase N.  Values:
                   1..3   plan / workers / assemble+map (orchestrator.py)
                   3b     re-run region→guide mapper (Opus)
                   4      inline mm regions   →  mm-stage2
                   4t     inline text regions →  text-stage2 (Option 1)
                   5      derive text-stage2 from mm-stage2 (Option 3)
                   all    chain the appropriate phases based on --mode
                          and --text-source.
                 Default (no --phase): equivalent to phases 1-3 only.
  --force        Wipe output_dir on the VM before phase 1.
  --foreground   Stream the remote log instead of nohup-ing.

Examples:
  # Default: mm + text-via-derive (Option 3), full chain via --phase all.
  $0 --config configs/impress.yaml --phase all

  # Independent text prose (Option 1) alongside mm.
  $0 --config configs/impress.yaml --phase all \\
     --mode both --text-source independent

  # Just re-do the inline step.
  $0 --config configs/impress.yaml --phase 4
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

case "$MODE" in
    multimodal|text|both) ;;
    *) echo "Error: --mode must be multimodal|text|both (got: $MODE)" >&2; exit 1 ;;
esac
case "$TEXT_SOURCE" in
    independent|derived) ;;
    *) echo "Error: --text-source must be independent|derived (got: $TEXT_SOURCE)" >&2; exit 1 ;;
esac

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Resolve config path locally (config may live in stage2/configs/ or be absolute)
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

# Convert local config path to VM-side path (must live under stage2/configs/).
CONFIG_REL="${CONFIG#$SCRIPT_DIR/}"
if [[ "$CONFIG_REL" == /* ]]; then
    echo "Error: --config must live under $SCRIPT_DIR (got absolute path: $CONFIG)" >&2
    exit 1
fi

VM="osworld"
ZONE="us-west1-c"
REMOTE_REPO="\$HOME/MMSkills"
REMOTE_PIPELINE="${REMOTE_REPO}/preprocess/skill-pipeline/stage2"

# ── Determine which assemble mode to pass to the orchestrator ────────────
# Independent text needs both mm regions (so the mapper can produce one
# mapping that both artefacts share) AND text regions from an independent
# Claude pass. Derived text only needs mm regions.
if [[ "$MODE" == "multimodal" ]]; then
    ASSEMBLE_MODE="multimodal"
elif [[ "$MODE" == "text" && "$TEXT_SOURCE" == "independent" ]]; then
    # Still need mm regions for the mapper; text-assembler will mirror the slugs.
    ASSEMBLE_MODE="both"
elif [[ "$MODE" == "text" && "$TEXT_SOURCE" == "derived" ]]; then
    ASSEMBLE_MODE="multimodal"  # derive_text.py reads mm-stage2
elif [[ "$MODE" == "both" && "$TEXT_SOURCE" == "independent" ]]; then
    ASSEMBLE_MODE="both"
else  # both + derived
    ASSEMBLE_MODE="multimodal"
fi

echo "[stage2] domain=$DOMAIN  config=$CONFIG_REL  phase=${PHASE:-1-3}  mode=$MODE  text-source=$TEXT_SOURCE  (assemble_mode=$ASSEMBLE_MODE)"

# ── 1. Sync local stage2/ scripts+configs (and the curated mapping) to the VM ──
echo "[sync] -> ${VM}:${REMOTE_PIPELINE}/"
gcloud compute scp --zone="$ZONE" --recurse \
    "$SCRIPT_DIR/" \
    "${VM}:~/MMSkills/preprocess/skill-pipeline/" >/dev/null

# ── 2. Build remote command for the requested phase ──
EXTRA_STR=""
for a in "${EXTRA[@]:-}"; do
    EXTRA_STR="${EXTRA_STR} ${a}"
done

# Common command fragments for each phase step.
CMD_ORCH="python -c 'import PIL' 2>/dev/null || pip install --quiet Pillow ; \
python -u orchestrator.py --config ${CONFIG_REL} --assemble-mode ${ASSEMBLE_MODE} ${FORCE}"

CMD_MAPPER="python -u map_regions.py --pipeline-dir ${REMOTE_REPO}/${OUTPUT_DIR_REL} --domain ${DOMAIN}"

CMD_INLINE_MM="python -u inline_into_stage1.py --pipeline-dir ${REMOTE_REPO}/${OUTPUT_DIR_REL} --mode multimodal"

CMD_INLINE_TEXT="python -u inline_into_stage1.py --pipeline-dir ${REMOTE_REPO}/${OUTPUT_DIR_REL} --mode text"

CMD_DERIVE_TEXT="python -u derive_text.py \
    --domain ${DOMAIN} \
    --app-name '${APP_NAME}' \
    --app-version '${APP_VERSION}' \
    --parallel ${PARALLEL}"

case "${PHASE:-}" in
    "" | 1 | 2 | 3)
        REMOTE_CMD="cd ${REMOTE_PIPELINE} && ${CMD_ORCH} ${EXTRA_STR}"
        ;;
    3b)
        REMOTE_CMD="cd ${REMOTE_PIPELINE} && ${CMD_MAPPER} ${EXTRA_STR}"
        ;;
    4)
        REMOTE_CMD="cd ${REMOTE_PIPELINE} && ${CMD_INLINE_MM} ${EXTRA_STR}"
        ;;
    4t)
        REMOTE_CMD="cd ${REMOTE_PIPELINE} && ${CMD_INLINE_TEXT} ${EXTRA_STR}"
        ;;
    5)
        REMOTE_CMD="cd ${REMOTE_PIPELINE} && ${CMD_DERIVE_TEXT} ${EXTRA_STR}"
        ;;
    all)
        # Chain: orchestrator (phases 1-3, assemble mode already set) → then
        # inline mm / inline text / derive text as appropriate for MODE +
        # TEXT_SOURCE.  Steps run sequentially; `set -e` aborts on failure.
        CHAIN=("cd ${REMOTE_PIPELINE}" "${CMD_ORCH}")
        if [[ "$MODE" != "text" ]]; then
            # multimodal or both → produce mm-stage2
            CHAIN+=("${CMD_INLINE_MM}")
        fi
        if [[ "$MODE" == "text" || "$MODE" == "both" ]]; then
            if [[ "$TEXT_SOURCE" == "independent" ]]; then
                CHAIN+=("${CMD_INLINE_TEXT}")
            else  # derived
                # derive_text.py requires mm-stage2 on disk, so ensure inline mm
                # ran even when MODE=text.
                if [[ "$MODE" == "text" ]]; then
                    CHAIN+=("${CMD_INLINE_MM}")
                fi
                CHAIN+=("${CMD_DERIVE_TEXT}")
            fi
        fi
        REMOTE_CMD=""
        for step in "${CHAIN[@]}"; do
            if [[ -z "$REMOTE_CMD" ]]; then
                REMOTE_CMD="$step"
            else
                REMOTE_CMD="${REMOTE_CMD} && ${step}"
            fi
        done
        REMOTE_CMD="${REMOTE_CMD} ${EXTRA_STR}"
        ;;
    *)
        echo "Error: --phase must be 1, 2, 3, 3b, 4, 4t, 5, or all (got: $PHASE)" >&2
        exit 1
        ;;
esac

LOG_TAG="$(date +%Y%m%d_%H%M%S)"
REMOTE_LOG="/tmp/stage2_${DOMAIN}_p${PHASE:-123}_${LOG_TAG}.log"

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

# ── 4. Pull skill outputs back after phases that touch skills/ ──
if [[ "${PHASE:-}" == "4" || "${PHASE:-}" == "4t" || "${PHASE:-}" == "5" || "${PHASE:-}" == "all" ]]; then
    if [[ "$FOREGROUND" -eq 1 ]]; then
        echo "[sync-back] skills/${DOMAIN}-{multimodal,text}-stage2/ <- VM"
        for variant in multimodal text; do
            REMOTE_SKILL="~/MMSkills/skills/${DOMAIN}-${variant}-stage2"
            gcloud compute scp --zone="$ZONE" --recurse \
                "${VM}:${REMOTE_SKILL}" \
                "$SCRIPT_DIR/../../../skills/" 2>/dev/null || \
                echo "  (skipped ${variant}: not present on VM yet)"
        done
    else
        echo "(background mode — re-run with --phase ${PHASE} --foreground, or rsync skills/ back manually after the job finishes)"
    fi
fi

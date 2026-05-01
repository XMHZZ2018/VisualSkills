#!/usr/bin/env bash
# Skill generation pipeline entry point.
#
# Usage:
#   ./run.sh --config configs/libreoffice_writer.yaml
#   ./run.sh --config configs/libreoffice_writer.yaml --mode multimodal
#   ./run.sh --config configs/libreoffice_writer.yaml --phase 4
#
# Per-phase parallelism is configured in the YAML config under `parallel:`.
# See README for defaults and overrides.
#
# Produces:
#   skills/<domain>-knowledge-text-v1/
#   skills/<domain>-knowledge-multimodal-v1/

set -euo pipefail

CONFIG=""
MODE="both"
EXTRA=()

while [[ $# -gt 0 ]]; do
    case "$1" in
        --config)
            CONFIG="$2"
            shift 2
            ;;
        --mode)
            MODE="$2"
            shift 2
            ;;
        -h|--help)
            cat <<EOF
Usage: $0 --config <path.yaml> [options]

Options:
  --mode {both,text,multimodal}    default: both
  --phase N                        run only phase N (1..6); default flow is 1-5.
                                   Phase 6 (text-v1 from multimodal-v1) is
                                   optional and only runs with --phase 6.
  --task_ids ID [ID ...]           (task-driven configs only) filter to these task ids

Per-phase parallelism is configured in the YAML config:

  parallel:
    phase_2: 8     # page rendering (local I/O)
    phase_3: 8     # figure extraction (pure bitmap-xref, deterministic)
    phase_4: 4     # guide generation (Claude calls — rate-limit bound)
    phase_5: 4     # use-when routing hints (Claude calls — rate-limit bound)
    phase_6: 4     # text-v1 from multimodal-v1 (Claude calls — optional phase)

Defaults are applied when keys are missing.

Examples:
  $0 --config configs/libreoffice_writer.yaml
  $0 --config configs/libreoffice_writer.yaml --mode multimodal --phase 4
  $0 --config configs/libreoffice_writer.yaml --phase 6   # derive text-v1
EOF
            exit 0
            ;;
        *)
            EXTRA+=("$1")
            shift
            ;;
    esac
done

if [[ -z "$CONFIG" ]]; then
    echo "Error: --config is required" >&2
    echo "Run '$0 --help' for usage." >&2
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Resolve config path relative to either CWD or the script dir.
if [[ ! -f "$CONFIG" ]]; then
    if [[ -f "$SCRIPT_DIR/$CONFIG" ]]; then
        CONFIG="$SCRIPT_DIR/$CONFIG"
    else
        echo "Error: config not found: $CONFIG" >&2
        exit 1
    fi
fi

cd "$SCRIPT_DIR"

export PYTHONUNBUFFERED=1

exec python3 -u generate_skill_from_knowledge_source.py \
    --config "$CONFIG" \
    --mode "$MODE" \
    ${EXTRA[@]+"${EXTRA[@]}"}

#!/usr/bin/env bash
# Skill generation pipeline entry point.
#
# Usage:
#   ./run.sh --config configs/libreoffice_writer.yaml
#   ./run.sh --config configs/libreoffice_writer.yaml --mode multimodal
#   ./run.sh --config configs/libreoffice_writer.yaml --parallel-pages 8 --parallel-guides 4
#
# Defaults:
#   --parallel-pages  8   (phases 2/3, mostly local IO + cheap PyMuPDF)
#   --parallel-guides 4   (phase 4, Claude calls — keep modest to avoid rate limits)
#
# Produces:
#   skills/<domain>-knowledge-text-v1/
#   skills/<domain>-knowledge-multimodal-v1/

set -euo pipefail

CONFIG=""
MODE="both"
PARALLEL_PAGES="8"
PARALLEL_GUIDES="4"
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
        --parallel-pages)
            PARALLEL_PAGES="$2"
            shift 2
            ;;
        --parallel-guides)
            PARALLEL_GUIDES="$2"
            shift 2
            ;;
        -h|--help)
            cat <<EOF
Usage: $0 --config <path.yaml> [options]

Options:
  --mode {both,text,multimodal}    default: both
  --parallel-pages N               phases 2/3 parallelism, default: 8
  --parallel-guides N              phase 4 parallelism, default: 4
  --phase N                        run only phase N (1..5), default: all
  --task_ids ID [ID ...]           (task-driven configs only) filter to these task ids

Examples:
  $0 --config configs/libreoffice_writer.yaml
  $0 --config configs/libreoffice_writer.yaml --mode multimodal --phase 4
  $0 --config configs/libreoffice_writer.yaml --parallel-guides 2
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
    --parallel-pages "$PARALLEL_PAGES" \
    --parallel-guides "$PARALLEL_GUIDES" \
    ${EXTRA[@]+"${EXTRA[@]}"}

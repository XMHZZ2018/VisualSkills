#!/usr/bin/env bash
# Skill generation pipeline entry point.
#
# Usage:
#   ./run.sh --config configs/libreoffice_writer.yaml
#   ./run.sh --config configs/libreoffice_writer.yaml --mode multimodal
#   ./run.sh --config configs/libreoffice_writer.yaml --mode both --text-source derived
#   ./run.sh --config configs/libreoffice_writer.yaml --phase 4
#
# Per-phase parallelism is configured in the YAML config under `parallel:`.
# See README for defaults and overrides.
#
# Produces:
#   skills/<domain>-text-stage1/
#   skills/<domain>-multimodal-stage1/

set -euo pipefail

CONFIG=""
MODE="both"
TEXT_SOURCE="derived"
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
        --text-source)
            TEXT_SOURCE="$2"
            shift 2
            ;;
        -h|--help)
            cat <<EOF
Usage: $0 --config <path.yaml> [options]

Options:
  --mode {both,text,multimodal}         default: both
  --text-source {independent,derived}   default: derived (matches paper)
      How the text-stage1 artifact is produced when --mode covers text:
        derived     — verbalize figure refs in the multimodal guide (Phase 6).
                      Prose is identical up to those refs; isolates the
                      contribution of visual evidence.
        independent — text is written by its own Claude pass over the source
                      pages, in parallel with the multimodal pass. Prose can
                      diverge between the two artifacts.
  --phase N                             run only phase N (1..6); default flow
                                        is 1-5 (+6 if --text-source derived).
  --task_ids ID [ID ...]                (task-driven configs only) filter to
                                        these task ids.

Per-phase parallelism is configured in the YAML config:

  parallel:
    phase_2: 8     # page rendering (local I/O)
    phase_3: 8     # figure extraction (pure bitmap-xref, deterministic)
    phase_4: 4     # guide generation (Claude calls — rate-limit bound)
    phase_5: 4     # use-when routing hints (Claude calls — rate-limit bound)
    phase_6: 4     # text-stage1 from multimodal-stage1 (Claude calls)

Defaults are applied when keys are missing.

Examples:
  $0 --config configs/libreoffice_writer.yaml
  $0 --config configs/libreoffice_writer.yaml --mode both --text-source independent
  $0 --config configs/libreoffice_writer.yaml --mode multimodal --phase 4
  $0 --config configs/libreoffice_writer.yaml --phase 6   # derive text-stage1
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
    --text-source "$TEXT_SOURCE" \
    ${EXTRA[@]+"${EXTRA[@]}"}

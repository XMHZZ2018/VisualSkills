#!/usr/bin/env bash
# Run Phase 3 chain for Writer to incorporate Phase 2b worker output into Stage 2 skill.
set -euo pipefail
cd /home/ziyan/MMSkills

PIPE=preprocess/skill-pipeline/v3/outputs/writer
MM1=skills/libreoffice_writer-knowledge-multimodal-stage1
MM2=skills/libreoffice_writer-knowledge-multimodal-stage2
TX2=skills/libreoffice_writer-knowledge-text-stage2

echo "=== [1/4] assembler — incorporating 21 worker dirs (8 free + 13 targeted) ==="
python3 preprocess/skill-pipeline/v3/assemble.py \
  --pipeline-dir "$PIPE" \
  --model claude-opus-4-6 \
  --timeout 2400

echo
echo "=== [2/4] map_regions — mapping new regions to Stage 1 topics ==="
python3 preprocess/skill-pipeline/v3/map_regions.py \
  --pipeline-dir "$PIPE" \
  --mm-v1-dir "$MM1" \
  --domain libreoffice_writer \
  --model claude-opus-4-6

echo
echo "=== [3/4] inline_into_mm_v1 — writing Stage 2 mm skill at $MM2 ==="
python3 preprocess/skill-pipeline/v3/inline_into_mm_v1.py \
  --pipeline-dir "$PIPE" \
  --mm-v1 "$MM1" \
  --out "$MM2"

echo
echo "=== [4/4] derive_text — producing Stage 2 text skill at $TX2 ==="
python3 preprocess/skill-pipeline/v3/derive_text_v3.py \
  --domain libreoffice_writer \
  --app-name "LibreOffice Writer" \
  --app-version 7.3.7 \
  --mm-dir "$MM2" \
  --text-dir "$TX2" \
  --parallel 4

echo
echo "=== Writer Stage 2 chain complete ==="

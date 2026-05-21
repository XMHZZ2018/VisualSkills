#!/usr/bin/env bash
# Re-run Phase 3 chain for Impress to fold Phase 2b worker output into Stage 2 skill.
set -euo pipefail
cd /home/ziyan/MMSkills

PIPE=preprocess/skill-pipeline/v3/outputs/impress
MM1=skills/libreoffice_impress-knowledge-multimodal-stage1
MM2=skills/libreoffice_impress-knowledge-multimodal-stage2
TX2=skills/libreoffice_impress-knowledge-text-stage2

echo "=== [1/4] assembler — incorporating 20 worker dirs (8 free + 12 targeted) ==="
python3 preprocess/skill-pipeline/v3/assemble.py \
  --pipeline-dir "$PIPE" \
  --model claude-opus-4-6 \
  --timeout 2400

echo
echo "=== [2/4] map_regions ==="
python3 preprocess/skill-pipeline/v3/map_regions.py \
  --pipeline-dir "$PIPE" \
  --mm-v1-dir "$MM1" \
  --domain libreoffice_impress \
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
  --domain libreoffice_impress \
  --app-name "LibreOffice Impress" \
  --app-version 7.3.7 \
  --mm-dir "$MM2" \
  --text-dir "$TX2" \
  --parallel 4

echo
echo "=== Impress Stage 2 chain (with Phase 2b) complete ==="

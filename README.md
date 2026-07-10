# VisualSkills

Code and skills for the paper **[VisualSkill: Multimodal Skills for Computer-Use Agents](https://arxiv.org/abs/2606.18448)**.

VisualSkill packages application knowledge (LibreOffice Writer / Calc / Impress, GIMP, QGIS, Zotero, Chrome, ...) as a topic-indexed hierarchy of markdown guides with cropped UI screenshots, and exposes it to a Claude Code agent through a `load_topic` MCP tool. Skills are built with a two-stage pipeline (Stage 1 from official docs, Stage 2 from live UI exploration) and evaluated end-to-end on [gym-anything](https://github.com/cmu-l3/gym-anything) and [OSWorld](https://os-world.github.io/).

## Repository layout

```
visualskills/
├── skills/                       # Generated skills (Stage 1 + Stage 2, text + multimodal)
├── plugins/                      # Claude Code --plugin-dir bundles
│   ├── gym-anything-text/
│   ├── gym-anything-multimodal/
│   ├── osworld-text/
│   └── osworld-multimodal/
├── tools/
│   ├── gym-anything-controller/  # GUI action MCP (screenshot / click / type / hotkey)
│   ├── osworld-controller/       # Same, targeting the OSWorld VM
│   └── skill_server.py           # load_topic / list_topics MCP (atomic prose+figures load)
├── preprocess/skill-pipeline/
│   ├── stage1/                   # Stage 1: docs-driven skill generation
│   └── stage2/                   # Stage 2: live UI explorer
├── scripts/
│   ├── run-gym-anything/         # Inference on gym-anything envs
│   └── run-osworld/              # Inference on OSWorld
└── vendor/
    ├── gym-anything/             # Benchmark envs (submodule)
    └── OSWorld/                  # OSWorld benchmark (submodule)
```

## 1. Environment setup

Both inference and Stage 2 skill construction depend on the two benchmark submodules under `vendor/` and on a Docker host with KVM + sysbox for live Ubuntu desktop containers.

### 1.1 Clone with submodules

```bash
git clone --recurse-submodules https://github.com/XMHZZ2018/VisualSkills.git
cd VisualSkills
# or, if already cloned:
git submodule update --init --recursive
```

`vendor/gym-anything` and `vendor/OSWorld` are pinned to specific commits.

### 1.2 Host dependencies

```bash
# Python packages (host)
pip install --break-system-packages \
    mcp httpx pymupdf Pillow PyYAML \
    numpy jsonschema paramiko pycryptodome requests docker anthropic \
    beautifulsoup4 markdownify

# OSWorld's own deps
bash scripts/run-osworld/setup.sh
```

### 1.3 Docker + sysbox

The benchmarks run each task in a fresh Ubuntu + GNOME + systemd container. Docker must be configured with the **sysbox runtime** so systemd works inside containers:

```bash
docker info | grep -i runtime   # must list sysbox-runc
```

Install sysbox from <https://github.com/nestybox/sysbox>. On GCP, use an `n2-standard-16` VM (or larger) with `--enable-nested-virtualization` for OSWorld's KVM guest.

### 1.4 Claude CLI

Both runners drive the agent through the Claude Code CLI (not the raw API), because plugins/skills are only surfaced through `--plugin-dir`:

```bash
npm install -g @anthropic-ai/claude-code
claude login          # writes ~/.claude/.credentials.json
```

`~/.claude/.credentials.json` is mounted read-only into every Claude container, so this only needs to be done once per host.

### 1.5 Claude CLI Docker images

Each runner has its own thin image that pins the CLI + the corresponding MCP server:

```bash
# gym-anything
docker build -t ga-claude-cli \
    -f scripts/run-gym-anything/Dockerfile.claude-cli scripts/run-gym-anything/

# OSWorld
docker build -t osworld-claude-cli \
    -f scripts/run-osworld/Dockerfile.claude-cli scripts/run-osworld/
```

## 2. Running inference

Both runners share the same three skill modes:

| Mode | Plugin dir | What Claude sees |
|------|------------|------------------|
| `none` | – | Baseline: no skill injected |
| `text` | `plugins/*-text/` | Topic guides as prose only (figures verbalized) |
| `multimodal` | `plugins/*-multimodal/` | Same prose + cropped UI screenshots, loaded via `load_topic` |

### 2.1 gym-anything

```bash
bash scripts/run-gym-anything/run.sh \
    --config scripts/run-gym-anything/experiments/configs/impress_mm_stage1.yaml
```

A minimal config:

```yaml
model: claude-opus-4-6
skill_mode: multimodal                     # none | text | multimodal
env_dir: vendor/gym-anything/benchmarks/cua_world/environments/libreoffice_impress_env
result_dir: scripts/run-gym-anything/workspaces
task_timeout: 1800
num_parallel: 4
```

Per-task outputs land under `workspaces/{model}/skill-{mode}/{env}/{task_id}/` with `result.json`, `score.txt`, `screenshots/`, and the full Claude event log. See [`scripts/run-gym-anything/README.md`](scripts/run-gym-anything/README.md) for the full config schema, parallel-worker layout, and the trajectory viewer.

### 2.2 OSWorld

```bash
# Baseline
python3 scripts/run-osworld/run.py \
    --provider_name docker --domain chrome --skill_mode none

# Multimodal skill (4 parallel workers, each with its own VM + Claude container)
python3 scripts/run-osworld/run.py \
    --provider_name docker --domain chrome --skill_mode multimodal --parallel 4
```

Claude Code runs inside `osworld-claude-cli` with **no Docker socket and no direct network path to the VM** — the only channel is a bridge that forwards actions to the QEMU guest at 1280×720 (matching OSWorld's original Anthropic agent). See [`scripts/run-osworld/README.md`](scripts/run-osworld/README.md) for provider options (`docker`, `vmware`, `virtualbox`), GCP VM setup, and the full argument reference.

## 3. Constructing skills

Every domain skill in `skills/<domain>-{text,multimodal}-stage{1,2}/` is produced by the same two-stage pipeline. Each stage emits a **matched pair** of artifacts — a multimodal form with cropped UI figures, and a text-only form in which each figure has been replaced by a verbal description of the same image — so any inference-score gap between them isolates the contribution of visual evidence.

At inference the multimodal artifact is loaded through `tools/skill_server.py`, which exposes `load_topic(topic)` and `list_topics()`. The agent gets a topic's prose and figures atomically in one MCP call instead of issuing separate `Read`s.

### 3.1 Stage 1 — from official documentation

Mines a skill from authored sources (a PDF user guide, a docs website, or a clustered list of gym-anything task descriptions). Runs entirely on the host. Lives at [`preprocess/skill-pipeline/stage1/`](preprocess/skill-pipeline/stage1/README.md).

Five phases, per YAML config:

1. **Taxonomy** — build a `category → topic` tree from the PDF ToC, HTML headings, or task clustering.
2. **Pages** — render (PDF) or fetch (HTML) each topic's source pages.
3. **Figures** — extract per-topic UI figures using PyMuPDF's embedded image rects (PDF) or inline `<img>` tags (HTML).
4. **Guides** — one Claude call per topic to write the prose; a second call anchors each figure back into the prose.
5. **Use-when + Index** — one keyword line per topic, then write `SKILL.md`.

An optional Phase 6 derives the matched text-Stage-1 artifact by verbalizing every `figNN.png` reference in the multimodal guides.

```bash
# Full pipeline, both modalities
./preprocess/skill-pipeline/stage1/run.sh \
    --config preprocess/skill-pipeline/stage1/configs/libreoffice_writer.yaml \
    --mode both

# Derive text-Stage-1 from multimodal-Stage-1
./preprocess/skill-pipeline/stage1/run.sh \
    --config preprocess/skill-pipeline/stage1/configs/libreoffice_writer.yaml \
    --phase 6
```

Configs for LibreOffice Writer / Calc / Impress, GIMP, QGIS, and Zotero live under `preprocess/skill-pipeline/stage1/configs/`.

### 3.2 Stage 2 — from live UI exploration

Augments the Stage 1 skill with knowledge that only exists in the running application. Runs on the GCP `osworld` VM because phases 1–2 spin up gym-anything Docker containers. Lives at [`preprocess/skill-pipeline/stage2/`](preprocess/skill-pipeline/stage2/README.md).

Two exploration sub-passes:

- **Free UI explorer.** An Opus planner inspects the idle app and proposes ~8 UI regions ("drawing toolbar", "properties sidebar", ...). ~8 Sonnet workers each drive the live app in parallel, scoped to one region, capturing screenshots and per-control notes.
- **Training-task-targeted explorer.** Failed train-task trajectories are reviewed to surface UI regions the agent measurably struggled with; additional workers are dispatched against those targets. Targets are scoped to *UI regions*, not specific tasks, so patches transfer to any test task touching the same UI surface.

Assembly is deterministic: an Opus assembler reconciles worker notes into per-region reference sections, an Opus mapper decides which Stage 1 guide each region belongs to, and the sections are inlined into a fresh copy of multimodal-Stage-1 with `ui-*.png` crops.

The matched text-Stage-2 artifact can be produced two ways, controlled by `--text-source`:

- `derived` (default, matches paper): verbalize each figure ref in the multimodal-Stage-2 guide (same mechanic as Stage 1 Phase 6). Prose is identical to multimodal-Stage-2 up to those refs, giving a tight ablation of what the visual modality contributes.
- `independent`: a separate text-only Claude pass over the same worker notes + screenshots, mirroring the mm region set. Prose is genuinely independent between the two artefacts.

```bash
# Stage 2 free explorer — full chain (paper default: mm-stage2 + derived text)
./preprocess/skill-pipeline/stage2/run.sh \
    --config preprocess/skill-pipeline/stage2/configs/writer.yaml --phase all

# Independent text prose (Option 1) alongside mm
./preprocess/skill-pipeline/stage2/run.sh \
    --config preprocess/skill-pipeline/stage2/configs/writer.yaml --phase all \
    --mode both --text-source independent

# Training-task-targeted explorer (after Stage 2a workers finish),
# chained straight into assembler + mapper + inline(s) so the augmented
# 2a+2b worker set produces the final skill pair in one command.
python3 preprocess/skill-pipeline/stage2/run_phase_2b.py \
    --v3-config preprocess/skill-pipeline/stage2/configs/writer.yaml \
    --rollouts-config scripts/run-gym-anything/experiments/configs/writer_train16_mm_skill.yaml \
    --app-name "LibreOffice Writer" \
    --then-inline --mode both --text-source derived
```

## 4. Citation

```bibtex
@article{jiang2026visualskill,
  title   = {VisualSkill: Multimodal Skills for Computer-Use Agents},
  author  = {Jiang, Ziyan and An, Li and Liu, Yujian and Ji, Jiabao and
             Wu, Qiucheng and Andreas, Jacob and Zhang, Yang and Chang, Shiyu},
  journal = {arXiv preprint arXiv:2606.18448},
  year    = {2026}
}
```

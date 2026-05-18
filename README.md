# MMSkills

Multimodal skills for [Claude Code](https://claude.ai/claude-code) — learning from visual references (papers, logos, websites, video tutorials) to improve agent performance.

Includes an evaluation framework for measuring skill impact on [OS World](https://os-world.github.io/) benchmarks.

## Quick Start

```bash
git clone --recurse-submodules https://github.com/XMHZZ2018/MMSkills.git
cd MMSkills
pip install mcp httpx pymupdf google-genai Pillow playwright yt-dlp opencv-python
```

## Repository Structure

```
MMSkills/
├── skills/                         # Skill definitions
│   ├── os-world/
│   │   ├── text/chrome-knowledge/  # Text-only Chrome skill
│   │   │   ├── SKILL.md            # Index → sub-guides
│   │   │   ├── settings/guide.md
│   │   │   ├── bookmarks-tabs/guide.md
│   │   │   ├── privacy/guide.md
│   │   │   └── ...
│   │   └── multimodal/chrome-knowledge/  # Multimodal Chrome skill
│   │       ├── SKILL.md            # Index → sub-guides
│   │       ├── settings/
│   │       │   ├── guide.md
│   │       │   └── *.png           # Reference screenshots
│   │       ├── bookmarks-tabs/
│   │       └── ...
│   ├── paper-beautify/
│   ├── logo-design/
│   └── website-beautify/
│
├── plugins/                        # Plugin groups for Claude CLI --plugin-dir
│   ├── osworld-text/               # Text-only OS World skills
│   ├── osworld-multimodal/         # Multimodal OS World skills
│   └── design/                     # Design skills (logo, paper, website)
│
├── preprocess/                     # Preprocessing pipelines
│   └── skill-from-tutorial/        # Generate skills from YouTube tutorials
│       ├── search-and-download.md  # Step 1: search & download
│       ├── extract-and-summarize.md # Step 2: frames & transcript
│       ├── generate-skills.md      # Step 3: synthesize into skills
│       ├── batch_search.py         # Batch search script
│       ├── batch_download.py       # Batch download script
│       ├── batch_extract.py        # Batch frame extraction
│       └── assets/searched/        # Per-query tutorial data
│
├── scripts/                        # Evaluation & use case scripts
│   └── run-osworld/
│       ├── run.py                  # Main evaluation script
│       ├── run.sh                  # Example commands
│       └── setup.sh                # One-time setup
│
├── tools/                          # MCP servers
│   ├── osworld-controller/         # VM control (screenshot, click, type)
│   ├── youtube-tutorial/           # YouTube search, download, frame extraction
│   ├── paper-search/               # Semantic Scholar + arXiv
│   ├── pdf-to-images/              # PDF → PNG conversion
│   ├── image-search/               # Image search + download
│   ├── image-gen/                  # Image generation (Gemini)
│   └── web-screenshot/             # Web page screenshots
│
└── vendor/                         # Git submodules
    └── OSWorld/                    # OS World benchmark (pinned commit)
```

## OS World Evaluation

Evaluate whether multimodal skills improve Claude's performance on OS World desktop tasks.

### Setup

```bash
# Initialize OSWorld submodule and install dependencies
bash scripts/run-osworld/setup.sh
```

Requires Docker with KVM support (e.g., GCP n2-standard-16 with nested virtualization).

### Run evaluation

```bash
# Baseline (no skills)
python3 scripts/run-osworld/run.py \
    --provider_name docker --domain chrome --skill_mode none

# Text skills
python3 scripts/run-osworld/run.py \
    --provider_name docker --domain chrome --skill_mode text

# Multimodal skills
python3 scripts/run-osworld/run.py \
    --provider_name docker --domain chrome --skill_mode multimodal
```

### Skill modes

| Mode | Plugin | Description |
|------|--------|-------------|
| `none` | – | Baseline, no skills injected |
| `text` | `plugins/osworld-text/` | Text-only step-by-step instructions |
| `multimodal` | `plugins/osworld-multimodal/` | Instructions + reference screenshots |

Skills are loaded automatically by Claude CLI via `--plugin-dir`. See [run-osworld/README.md](scripts/run-osworld/README.md) for details.

## Skill Generation

Every domain-specific skill in `skills/<env>-knowledge-{text,multimodal}-v1/`
is built through a two-stage pipeline. Each stage produces a **matched pair**
of artifacts: a `multimodal` form with cropped UI screenshots and a
`text-only` form in which every figure has been replaced by a verbal
description of the same image. The two artifacts share sub-guide structure
and prose verbatim, so any score gap between them isolates the contribution
of visual evidence.

Both stages also auto-install a `tools/skill_server.py` MCP server that
exposes `load_topic(topic)` and `list_topics()`. At inference the agent
loads a topic's prose + figures atomically in one tool call, instead of
issuing separate `Read`s for each figure.

### Stage 1 — from official documentation

Mines a skill from authored sources (HTML manuals, PDF guides, tutorial
videos). The 5-phase pipeline lives at
[`preprocess/skill-pipeline/v1/`](preprocess/skill-pipeline/v1/README.md).
The taxonomy is derived from the docs' own structure; per-topic guides are
synthesised from rendered pages or fetched HTML. Best when the target
application has mature, well-maintained documentation.

```bash
./preprocess/skill-pipeline/v1/run.sh \
    --config preprocess/skill-pipeline/v1/configs/libreoffice_writer.yaml \
    --mode both    # builds both text and multimodal artifacts
```

### Stage 2 — from UI exploration + training tasks

Augments the Stage 1 skill with knowledge that only exists in the running
application. Implemented at
[`preprocess/skill-pipeline/v3/`](preprocess/skill-pipeline/v3/README.md)
and runs in two sub-passes:

- **Free UI explorer.** An Opus planner inspects the idle app and proposes
  ~8 UI regions; ~8 Sonnet workers drive the live application in parallel,
  each scoped to one region, capturing screenshots and per-control notes.
- **Training-task-targeted explorer.** Failed train-task trajectories are
  reviewed (`review.py`) to surface UI regions the agent measurably
  struggled with; additional Sonnet workers are dispatched against those
  targets via `run_phase_2b.py`. Crucially the targets are scoped to *UI
  regions*, not specific tasks, so the patch transfers to any test task
  that touches the same UI surface.

An assembler reconciles all worker notes into per-region reference
sections, an LLM mapper merges them into the existing Stage 1 sub-guides,
and the matched text artifact is derived from the new multimodal one.

```bash
# Stage 2 free explorer (Phase 0–3)
./preprocess/skill-pipeline/v3/run.sh --config preprocess/skill-pipeline/v3/configs/writer.yaml

# Stage 2 training-task-targeted explorer (after Phase 1 workers finish)
python3 preprocess/skill-pipeline/v3/run_phase_2b.py \
    --v3-config preprocess/skill-pipeline/v3/configs/writer.yaml \
    --rollouts-config scripts/run-gym-anything/experiments/configs/writer_train16_mm_skill.yaml \
    --app-name "LibreOffice Writer"
```

### Other preprocessing utilities

For YouTube-tutorial-driven design skills (paper/logo/website), see
`preprocess/skill-from-tutorial/`:

```bash
# 1. Search and download videos
python3 preprocess/skill-from-tutorial/batch_search.py
python3 preprocess/skill-from-tutorial/batch_download.py

# 2. Extract frames and transcripts
python3 preprocess/skill-from-tutorial/batch_extract.py

# 3. Summarize and generate skills (interactive, uses Claude)
# Follow preprocess/skill-from-tutorial/generate-skills.md
```

## Design Skills

| Skill | What it does |
|-------|-------------|
| **paper-beautify** | Format a LaTeX paper by learning from published papers |
| **logo-design** | Design a logo using reference logos + image generation |
| **website-beautify** | Improve a personal website by learning from top academic sites |

## MCP Tools

| Server | Tools | Used by |
|--------|-------|---------|
| `osworld-controller` | `screenshot`, `click`, `type_text`, `key_press`, ... | OS World evaluation |
| `youtube-tutorial` | `search_youtube`, `download_youtube`, `extract_frames`, `extract_frame_at` | Skill preprocessing |
| `paper-search` | `search_papers`, `search_arxiv`, `download_paper` | paper-beautify |
| `pdf-to-images` | `pdf_to_images`, `pdf_page_count` | paper-beautify |
| `image-search` | `search_images`, `download_image` | logo-design |
| `image-gen` | `generate_image`, `edit_image` | logo-design |
| `web-screenshot` | `screenshot_url`, `screenshot_urls` | website-beautify |

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

### Preprocessing pipeline

Generate skills from YouTube tutorials:

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

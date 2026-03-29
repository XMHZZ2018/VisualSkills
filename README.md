# MMSkills

A collection of multimodal skills for [Claude Code](https://claude.ai/claude-code). Each skill uses Claude's vision capabilities to learn from real-world visual references — published papers, logos, websites, video tutorials — and applies those insights to improve your work.

## How It Works

Every skill follows a two-stage pattern:

1. **Setup** — Search online, download references, convert to images, annotate with descriptions, save to `assets/`
2. **Execute** — Read annotations + images as multimodal context, then do the actual work (format, generate, edit)

References are stored in two folders:
- `assets/curated/` — your hand-picked references with personal annotations (never auto-deleted)
- `assets/searched/` — auto-populated by the setup step, cleaned each run

An `index.md` in each folder lets Claude quickly understand what's available before selectively reading images.

## Skills

| Skill | Setup | Execute | What it does |
|-------|-------|---------|-------------|
| **paper-beautify** | `/setup-paper-refs` | `/format-paper` | Format a LaTeX paper by learning from published papers in the same venue |
| **logo-design** | `/setup-logo-refs <desc>` | `/logo-design <desc>` | Design a logo using reference logos + Nano Banana (Gemini) image generation |
| **website-beautify** | `/setup-website-refs <url>` | `/website-beautify <repo>` | Improve a personal website by learning from the best academic sites |
| **skill-from-tutorial** | `/setup-tutorial-refs <topic>` | `/skill-from-tutorial <topic>` | Create a Claude Code skill by watching a YouTube tutorial |

## Architecture

```
MMSkills/
├── .claude/commands/        # Slash command definitions (the skill prompts)
├── .mcp.json                # MCP server registration
│
├── skills/                  # Skill metadata + assets
│   └── <skill-name>/
│       ├── skill.md         # Skill overview, workflow, tool mapping
│       └── assets/
│           ├── curated/     # Human-maintained references
│           │   ├── index.md # Lists images + why you picked them
│           │   └── *.jpg/md # Image + annotation pairs
│           └── searched/    # Auto-populated by /setup-*
│               ├── index.md # Auto-generated index + annotations
│               └── *.jpg/md # Image + annotation pairs
│
├── tools/                   # MCP servers (reusable building blocks)
│   ├── paper-search/        # Search Semantic Scholar + arXiv, download PDFs
│   ├── pdf-to-images/       # Convert PDF pages to PNGs (PyMuPDF)
│   ├── image-search/        # Search + download images (DuckDuckGo)
│   ├── image-gen/           # Generate images via Gemini Nano Banana
│   ├── web-screenshot/      # Screenshot web pages (Playwright)
│   └── youtube-tutorial/    # Search YouTube, download, extract frames
│
└── scripts/                 # Use case entry points + examples
    └── <skill-name>/
        ├── README.md        # Commands + usage examples
        └── workspace/       # Working files for each run
```

### Layer separation

- **Tools** (MCP servers) are single-purpose and reusable. They don't know *why* they're called.
- **Skills** (slash commands) are orchestration prompts. They compose tools and tell Claude the goal.
- **Assets** are the multimodal knowledge base. Images + text annotations that inform Claude's decisions.
- **Scripts** are user-facing entry points with examples and workspace directories.

## MCP Tools

| Server | Tools | Used by |
|--------|-------|---------|
| `paper-search` | `search_papers`, `search_arxiv`, `download_paper` | paper-beautify |
| `pdf-to-images` | `pdf_to_images`, `pdf_page_count` | paper-beautify |
| `image-search` | `search_images`, `download_image` | logo-design |
| `image-gen` | `generate_image`, `edit_image` | logo-design |
| `web-screenshot` | `screenshot_url`, `screenshot_urls` | website-beautify |
| `youtube-tutorial` | `search_youtube`, `download_youtube`, `extract_frames` | skill-from-tutorial |

## Setup

### Prerequisites

- [Claude Code](https://claude.ai/claude-code) CLI
- Python 3.12+
- `GEMINI_API_KEY` environment variable (for logo generation)

### Install dependencies

```bash
pip install mcp httpx pymupdf google-genai Pillow playwright yt-dlp opencv-python
python -m playwright install chromium
```

### Start using

```bash
cd MMSkills

# Example: beautify a paper
./scripts/paper-beautify/run.sh ~/Downloads/my_paper.zip
/setup-paper-refs
/format-paper

# Example: design a logo
/setup-logo-refs a logo for my AI startup
/logo-design a logo for my AI startup
```

## Contributing

### Adding a new skill

1. **Create the tool** (if needed) — add a new MCP server in `tools/<name>/server.py`
2. **Register it** — add to `.mcp.json`
3. **Create the skill** — add `skills/<name>/skill.md` and `assets/{curated,searched}/`
4. **Write the commands** — add setup + execute `.md` files in `.claude/commands/`
5. **Add a script** — create `scripts/<name>/README.md` with examples and a `workspace/` dir

### Design principles

- **Two-stage pattern**: always separate asset preparation (setup) from execution
- **Curated + searched**: let the user inject their taste via `curated/`, auto-populate via `searched/`
- **Annotate everything**: every image gets a companion `.md` with 1–3 sentences explaining *why* it's useful
- **Index files**: each assets folder gets an `index.md` so Claude can decide which images to read
- **Tools are reusable**: a tool should work for multiple skills (e.g., `image-search` serves both logo-design and future skills)
- **Keep user input minimal**: infer venue, topic, style, etc. from the input files whenever possible

# Skill Pipeline (v1)

Generate domain-specific skills (text and/or multimodal) for a desktop
application from one of three knowledge sources, all driven by a single YAML
config and one Python entry point.

```bash
./run.sh --config configs/<domain>.yaml --mode multimodal --parallel 4
```

## Three modes

The pipeline auto-detects which mode to run based on what's in the YAML:

| Mode | Trigger | Taxonomy comes from | Per-topic content |
|------|---------|--------------------|-------------------|
| **Full-PDF** | `sources.pdf_guide.url` | The PDF's printed Table of Contents | Page renders cropped from the PDF |
| **HTML docs** | `sources.html_guide.root_url` | Crawl from a root page (acts as the ToC) | Full-page playwright screenshots + `<img>` tags |
| **Task-filtered** | A `tasks:` block | Cluster gym-anything tasks into topics | Pages of a PDF mapped to each topic via Claude |

All three converge on the same downstream pipeline.

## Pipeline phases

| Phase | What it does | Output |
|-------|--------------|--------|
| 1 — Taxonomy | Build a 2-layer category → topic structure | `workspace/<domain>/taxonomy.json` |
| 2 — Per-topic pages | Render the source pages for each topic (PDF crop @ 300 DPI, or playwright full-page PNG) | `workspace/<domain>/{pdf,html}_pages/<topic>/page_NNNN.png` |
| 3 — Figures | PDF: extract bitmap xrefs, fall back to LLM-bbox detection. HTML: download `<img>` tags. | `workspace/<domain>/{pdf,html}_figures/<topic>/fig_NNN.png` |
| 4 — Text guide | Concise prose `guide.md` per topic from page images | `skills/<domain>-knowledge-text-v1/<cat>/<topic>/guide.md` |
| 5 — Multimodal guide | Same prose with `Read the screenshot figNN.png` paragraphs spliced in + figure files copied | `skills/<domain>-knowledge-multimodal-v1/<cat>/<topic>/{guide.md,figNN.png}` |
| 6 — Index | Per-modality `SKILL.md` listing all topics | `skills/<domain>-knowledge-{text,multimodal}-v1/SKILL.md` |

Every phase caches its output. Re-running skips completed work; delete the
relevant cache file to force regeneration.

## Config examples

**Full-PDF mode** (`configs/libreoffice_writer.yaml`):
```yaml
app_name: "LibreOffice Writer"
app_version: "7.3.7"
domain: "libreoffice_writer"
sources:
  pdf_guide:
    url: "https://documentation.libreoffice.org/.../WG73-WriterGuide.pdf"
```

**HTML-docs mode** (`configs/zotero.yaml`):
```yaml
app_name: "Zotero"
app_version: "7"
domain: "zotero"
sources:
  html_guide:
    root_url: "https://www.zotero.org/support/start"
    crawl_depth: 2
```

`crawl_depth` controls how many link-hops we follow from the root when
harvesting structure. Depth 1 = the root page only (its links become topics).
Depth 2 = also walk each linked page's headings to discover sub-topics.
Content for each topic is always fetched in Phase 2 regardless of depth.

**Task-filtered mode** (`configs/libreoffice_impress.yaml`):
```yaml
app_name: "LibreOffice Impress"
app_version: "7.3.7"
domain: "libreoffice_impress"
sources:
  pdf_guide:
    url: "https://documentation.libreoffice.org/.../IG73-ImpressGuide.pdf"
tasks:
  env_dir: "vendor/gym-anything/.../libreoffice_impress_env"
  # Optional: restrict to a split subset
  # split: "vendor/gym-anything/.../libreoffice_impress_split.json"
  # use:   "test_tasks"
  # Optional: exact override list of task ids
  # task_list: ["create_flowchart", ...]
```

## Usage

```bash
# Full pipeline, both modalities, 4 topics in parallel
./run.sh --config configs/libreoffice_writer.yaml --mode both --parallel 4

# Multimodal only — drafts the prose internally, only writes multimodal-v1
./run.sh --config configs/zotero.yaml --mode multimodal --parallel 4

# Text only
./run.sh --config configs/libreoffice_impress.yaml --mode text

# Task mode with a specific subset
./run.sh --config configs/libreoffice_impress.yaml --task_ids create_flowchart
```

`--mode multimodal` does **not** require `text-v1` to exist — it drafts the
prose internally and caches it at `workspace/<domain>/text_drafts/<cat>/<topic>.md`,
so a later `--mode both` reuses that draft for free.

## Output layout

```
skills/
├── <domain>-knowledge-text-v1/
│   ├── SKILL.md
│   └── <category>/<topic>/guide.md
└── <domain>-knowledge-multimodal-v1/
    ├── SKILL.md
    └── <category>/<topic>/
        ├── guide.md          # same prose, with figure-reference paragraphs
        ├── fig01.png         # selected figures, renumbered in insertion order
        ├── fig02.png
        └── ...
```

The multimodal `guide.md` is the text guide byte-for-byte, plus paragraphs of
the form *"Read the screenshot `figNN.png` in this directory — you will see
&lt;short description&gt;."* spliced in at the spots Claude judged most useful.

## Workspace cache

```
workspace/<domain>/
├── official-guide.pdf          # PDF mode: downloaded once
├── html_cache/                 # HTML mode: per-URL HTML cache
├── toc_raw.json                # PDF mode: raw outline from PyMuPDF
├── toc_pages/                  # PDF mode: rendered ToC pages + per-page OCR JSON
├── html_outline_raw.json       # HTML mode: harvested headings + links
├── taxonomy.json               # Phase 1 output (delete to regenerate)
├── pdf_pages/<topic>/          # PDF mode: 300-DPI page renders
├── html_pages/<topic>/         # HTML mode: playwright full-page screenshots
├── pdf_figures/<topic>/        # PDF mode: cropped figures + figures.json
├── html_figures/<topic>/       # HTML mode: downloaded <img> + figures.json
└── text_drafts/<cat>/<topic>.md # In-memory prose cache (shared by both modalities)
```

## Requirements

- Python 3.10+ (uses `X | Y` type unions)
- `claude` CLI authenticated (model: `claude-opus-4-6`)
- `PyMuPDF`, `Pillow`, `PyYAML` — for PDFs
- `requests`, `beautifulsoup4`, `playwright` (with `chromium` installed) — for HTML mode

## Architecture notes

- **Single script**: `generate_skill_from_knowledge_source.py`. The runner
  dispatches on the YAML config. There used to be `generate_from_docs.py` and
  `generate_from_tasks.py`; they're unified.
- **All LLM calls** route through a thin `call_claude()` wrapper that shells
  out to the `claude` CLI. The CLI is run from `cwd=/tmp` because the project
  directory's `.claude/`/`.mcp.json` configuration confuses non-interactive
  invocations.
- **Parallelism** is at the topic level in Phases 4/5 (`--parallel N`). Phase 1
  ToC OCR is intentionally serial — parallel cold-start of `claude -p` can
  trip the OAuth `client_data` rate limit.
- **Caching is aggressive**: every phase keys its outputs into `workspace/`
  and skips on hit. Delete a specific cache file to force that phase only.

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

The pipeline has 5 phases. Use `--phase N` to run only one phase (assumes
earlier phases' outputs are cached). Default: run all phases end-to-end.

### Phase 1 — Taxonomy
Build a 2-layer `category → topic` structure with page ranges.
**Output:** `workspace/<domain>/taxonomy.json`

- **PDF mode** — three steps:
  1. Locate the *printed* Table-of-Contents pages in the PDF (using the
     embedded outline as a hint, plus a heuristic that scans front-matter
     pages for lines ending in a page number).
  2. Render those ToC pages as PNGs and send each one to Claude with a
     transcription prompt — Claude acts as a structure-aware OCR and returns
     `{level, title, page}` entries (one Claude call per ToC page, cached as
     `toc_NNNN.json`). Merged into `toc_transcribed.json`.
  3. Send the merged entry list to Claude with the synthesis prompt. Claude
     promotes L1 entries to categories, L2s to topics, drops front/back
     matter, merges over-fragmented sub-sections, and computes each topic's
     `pdf_pages` range. Result is `taxonomy.json`.
- **HTML mode** — fetch the root page, recursively harvest headings and
  in-scope links up to `crawl_depth`, then ask Claude to collapse them into
  a category → topic taxonomy.
- **Task mode** — cluster the gym-anything task descriptions with Claude
  into topics, then ask Claude to map each topic onto a page range of the
  PDF guide.

### Phase 2 — Per-topic pages
Render the source pages for every topic so phase 4 has visual context.
**Output:** `workspace/<domain>/{pdf,html}_pages/<topic>/page_NNNN.png`

- **PDF/Task:** for each topic, render its `pdf_pages` from the PDF at
  300 DPI using PyMuPDF. Skips pages already on disk.
- **HTML:** for each topic's URL, take a full-page screenshot via
  Playwright (chromium). Skips topics already screenshotted.

### Phase 3 — Figures
Collect figures used in phase 5 (multimodal). Skipped for `--mode text`.
**Output:** `workspace/<domain>/{pdf,html}_figures/<topic>/fig_NNN.png`

- **PDF:** first try PyMuPDF's bitmap-xref extraction (cheap and exact);
  for topics where xrefs miss, fall back to a Claude bounding-box pass that
  proposes figure regions on each page and crops them.
- **HTML:** download every `<img>` from the page (deduplicated by URL),
  resolving relative URLs and respecting the page's content scope.

### Phase 4 — Per-topic guides
Generate a `guide.md` per topic. Both modalities are produced here.
**Output:**
- `skills/<domain>-knowledge-text-v1/<cat>/<topic>/guide.md`
- `skills/<domain>-knowledge-multimodal-v1/<cat>/<topic>/{guide.md, figNN.png}`

- **Text:** ask Claude to read all of a topic's page images and write
  concise prose. Cached at `workspace/<domain>/text_drafts/<cat>/<topic>.md`.
- **Multimodal:** start from the text draft, then ask Claude to splice in
  *"Read the screenshot `figNN.png` in this directory — you will see &lt;short
  description&gt;."* paragraphs at the most useful spots and copy the chosen
  figures into the topic directory, renumbered in insertion order.
- Topics run in parallel with `--parallel N` (thread pool over topics).
  `--mode multimodal` does **not** require the text-v1 directory to exist —
  it drafts the prose internally on the fly and reuses the draft cache.

### Phase 5 — Index
Write the per-modality `SKILL.md` summary that lists every topic.
**Output:** `skills/<domain>-knowledge-{text,multimodal}-v1/SKILL.md`

---

Every phase caches its outputs aggressively. Re-running skips completed
work; delete the relevant cache file or directory to force regeneration of
just that step.

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

# Run a single phase (earlier phases must already be cached, later phases skipped)
./run.sh --config configs/libreoffice_writer.yaml --phase 1   # just (re)build taxonomy
./run.sh --config configs/libreoffice_writer.yaml --phase 4 --mode multimodal --parallel 4
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

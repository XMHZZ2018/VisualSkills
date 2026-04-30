# Skill Pipeline (v1)

Generate domain-specific skills (text and/or multimodal) for a desktop
application from one of three knowledge sources, all driven by a single YAML
config and one Python entry point.

```bash
./run.sh --config configs/<domain>.yaml --mode multimodal
```

Per-phase parallelism is set in the YAML config (defaults shown):
```yaml
parallel:
  phase_2: 8     # page rendering — local I/O, safe to run high
  phase_3: 8     # figure extraction — pure bitmap-xref, deterministic (local I/O)
  phase_4: 4     # guide generation — Claude calls per topic, rate-limit bound
```
Any key that's omitted falls back to the default. Phases 1 and 5 are serial.

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
  300 DPI using PyMuPDF. Skips pages already on disk. Topics are rendered
  in parallel (config `parallel.phase_2`, default 8); each worker opens its own `fitz.Document`
  so PyMuPDF's thread restrictions are respected.
- **HTML:** for each topic's URL, take a full-page screenshot via
  Playwright (chromium). Skips topics already screenshotted.

### Phase 3 — Figures
Collect figures used in phase 4 (multimodal). Skipped for `--mode text`.
**Output:** `workspace/<domain>/{pdf,html}_figures/<topic>/raw_NNN.png`
plus `figures.json` describing each crop.

- **PDF:** for each rendered page, use PyMuPDF
  `page.get_images(full=True)` + `get_image_rects(xref)` to locate every
  embedded bitmap rectangle (in PDF points). When one logical figure is
  stored as multiple adjacent strips, those rects are clustered (via
  union-find on a "close together on one axis, overlapping on the other"
  adjacency) into one union bbox per figure. For each cluster, search the
  page's text blocks for a matching `Figure N: ...` caption (strict regex
  so body prose can't match), extend the crop bottom to the caption
  block, and widen the X range to encompass any text blocks (legends/keys)
  sitting between the bitmap and the caption. Python crops the result
  from the rendered 300-DPI page PNG and writes `raw_NNN.png` plus a
  `figures.json` carrying `{path, page, figure_number, caption}`. Pages
  with no embedded bitmaps contribute no figures — Phase 3 never calls
  Claude, so coordinates come straight from the PDF's own image-object
  rects and body-text bleed is structurally impossible. Topics run in
  parallel (config `parallel.phase_3`, default 8 — purely local I/O).
- **HTML:** download every `<img>` from the page (deduplicated by URL),
  resolving relative URLs and respecting the page's content scope.

### Phase 4 — Per-topic guides
Generate a `guide.md` per topic. Text and multimodal are independent code
paths with their own Claude calls and caches — multimodal does not derive
from the text draft. **Output:**
- `skills/<domain>-knowledge-text-v1/<cat>/<topic>/guide.md`
- `skills/<domain>-knowledge-multimodal-v1/<cat>/<topic>/{guide.md, figNN.png}`

- **Text:** ask Claude to read all of a topic's page images and write
  concise prose (no figure references). Cached at
  `workspace/<domain>/text_drafts/<cat>/<topic>.md`.
- **Multimodal:** two Claude calls per topic:
  1. **Prose call** — pages → markdown body. Where a figure would help,
     Claude inserts a placeholder line `<!-- figure: <short description> -->`
     immediately after the relevant sentence. No filenames at this stage.
     Cached at `workspace/<domain>/multimodal_drafts/<cat>/<topic>.prose.md`.
  2. **Anchor call** — placeholder-marked prose + a small (~256px JPEG)
     thumbnail per candidate figure (filename + caption attached, in the
     same order). For each placeholder, Claude either replaces it with
     `See \`raw_NNN.png\`.` (or `(see \`raw_NNN.png\`)`) using a candidate
     filename, or deletes the placeholder line if no thumbnail clearly
     matches. The image carries the content; the pointer does not verbalize
     what's in it. Cached at
     `workspace/<domain>/multimodal_drafts/<cat>/<topic>.md`.

  After the anchor call returns, we extract the filenames it actually
  referenced (in order of first appearance), copy those crops into the
  topic dir as `fig01.png`, `fig02.png`, ..., and rewrite the markdown to
  use the renumbered names. Any leftover unresolved placeholders are
  stripped as a safety net.
- Topics run in parallel with the config value `parallel.phase_4` (thread
  pool over topics). Each topic issues 1 Claude call for text and up to 2
  for multimodal (prose + anchor); the anchor call is skipped if the prose
  has no placeholders or the topic has no candidate figures. Keep
  `phase_4` modest because of Claude rate limits — default is 4. The text
  and multimodal paths share neither prompts nor caches.

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
# Full pipeline, both modalities (parallelism set in the YAML config)
./run.sh --config configs/libreoffice_writer.yaml --mode both

# Multimodal only
./run.sh --config configs/zotero.yaml --mode multimodal

# Text only
./run.sh --config configs/libreoffice_impress.yaml --mode text

# Override parallelism for one run: edit the `parallel:` block in the YAML config.

# Task mode with a specific subset
./run.sh --config configs/libreoffice_impress.yaml --task_ids create_flowchart

# Run a single phase (earlier phases must already be cached, later phases skipped)
./run.sh --config configs/libreoffice_writer.yaml --phase 1   # just (re)build taxonomy
./run.sh --config configs/libreoffice_writer.yaml --phase 4 --mode multimodal
```

`--mode multimodal` and `--mode text` are fully independent — each runs its
own Claude call(s) and writes to its own draft cache
(`text_drafts/` vs. `multimodal_drafts/`). `--mode both` simply runs both
paths back-to-back; neither modality reuses the other's prose.

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
├── text_drafts/<cat>/<topic>.md       # text-mode prose draft cache
└── multimodal_drafts/<cat>/<topic>.md # multimodal-mode draft cache (with raw_NNN.png refs)
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
- **Parallelism** is set per-phase in the YAML config under a `parallel:` block:
  `phase_2` (page rendering, default 8), `phase_3` (figure extraction, default 4),
  `phase_4` (guide generation, default 4 — Claude rate-limit bound). Phase 1
  ToC OCR is intentionally serial — parallel cold-start of `claude -p` can
  trip the OAuth `client_data` rate limit.
- **Caching is aggressive**: every phase keys its outputs into `workspace/`
  and skips on hit. Delete a specific cache file to force that phase only.

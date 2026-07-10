# Skill Pipeline (Stage 1)

Generate domain-specific skills (text and/or multimodal) for a desktop
application from one of three knowledge sources, all driven by a single YAML
config and one Python entry point.

> Looking for the **UI-explorer** pipeline (mm-stage2 / text-stage2 from live app
> exploration)? See [`../stage2/README.md`](../stage2/README.md). Stage 2's Phase 5 reuses
> Stage 1's Phase 6 derivation core (`derive_text_from_multimodal_dir`).

```bash
./run.sh --config configs/<domain>.yaml --mode multimodal
```

Per-phase parallelism is set in the YAML config (defaults shown):
```yaml
parallel:
  phase_2: 8     # page rendering — local I/O, safe to run high
  phase_3: 8     # figure extraction — pure bitmap-xref, deterministic (local I/O)
  phase_4: 4     # guide generation — Claude calls per topic, rate-limit bound
  phase_5: 4     # use-when routing hints — Claude calls per guide, rate-limit bound
  phase_6: 4     # text-stage1 from multimodal-stage1 — optional, Claude calls per guide
```
Any key that's omitted falls back to the default. Phase 1 is serial; the
SKILL.md write at the end of phase 5 is also serial (the use-when calls
that precede it use `phase_5` parallelism). Phase 6 is optional and
only runs when explicitly requested via `--phase 6`.

## Three modes

The pipeline auto-detects which mode to run based on what's in the YAML:

| Mode | Trigger | Taxonomy comes from | Per-topic content |
|------|---------|--------------------|-------------------|
| **Full-PDF** | `sources.pdf_guide.url` | The PDF's printed Table of Contents | Page renders cropped from the PDF |
| **HTML docs** | `sources.html_guide.root_url` | Crawl from a root page (acts as the ToC) | Markdown extracted via plain-HTTP fetch + every inline `<img>` downloaded locally |
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
Produce the source pages for every topic so phase 4 has the content to
work from.

- **PDF/Task:** for each topic, render its `pdf_pages` from the PDF at
  300 DPI using PyMuPDF. Skips pages already on disk. Topics are rendered
  in parallel (config `parallel.phase_2`, default 8); each worker opens its own `fitz.Document`
  so PyMuPDF's thread restrictions are respected.
  **Output:** `workspace/<domain>/pdf_pages/<topic>/page_NNNN.png`
- **HTML:** for each topic's URL, fetch the HTML via `requests`, extract
  the main content (`<main>`, `<article>`, `[role="main"]`, then id-based
  fallbacks), download every inline `<img>` to a sibling `images/` dir,
  rewrite the markdown's `![]()` references to absolute local paths, and
  convert the result to markdown via `markdownify`. Phase 4 receives the
  markdown via Claude's Read tool, which transparently follows the
  embedded image refs. The inline-image download here is scoped to the
  markdown — Phase 3 (`phase_html_figures`) does an independent pass that
  builds the canonical `html_figures/<topic>/` figure list for Phase 4
  multimodal Call B.
  **Output:** `workspace/<domain>/html_pages/<topic>/page_NNNN.md` and
  `workspace/<domain>/html_pages/<topic>/images/img_NNN.<ext>`.

### Phase 3 — Figures
Collect figures used in phase 4 (multimodal). Skipped for `--mode text`.

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
  **Output:** `workspace/<domain>/pdf_figures/<topic>/raw_NNN.png` plus
  `figures.json`.
- **HTML:** independent pass. For each topic URL, re-parse the cached HTML,
  extract main content, and download every `<img>` (with `alt` text used
  as `description`) into `workspace/<domain>/html_figures/<topic>/`,
  writing a `figures.json` keyed by topic. This is the canonical figure
  list Phase 4 multimodal Call B picks from. The Phase 2 inline-image
  download under `html_pages/<topic>/images/` is a separate copy that
  exists only to back the markdown's `![]()` refs.

### Phase 4 — Per-topic guides
Generate a `guide.md` per topic. Text and multimodal are independent code
paths with their own Claude calls and caches — multimodal does not derive
from the text draft. **Output:**
- `skills/<domain>-text-stage1/<cat>/<topic>/guide.md`
- `skills/<domain>-multimodal-stage1/<cat>/<topic>/{guide.md, figNN.png}`

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

### Phase 5 — Routing hints + Index

Phase 5 runs in two sub-steps:

**Phase 5a — Use-when routing hints.** For every existing `guide.md` we
make one Claude call (text-only, the guide's own markdown is the input)
asking for a single comma-separated line of concrete user-task keywords —
dialog names, formats, settings, action verbs. The line is cached and
NEVER mutates the guide itself. A downstream agent uses these phrases to
pick the right topic guide for a given task description, without having
to scan all 100+ guides.

- **Output:** `workspace/<domain>/use_when/<modality>/<cat>/<topic>.txt`
- **Idempotent:** topics with a non-empty cache file are skipped, so
  partial / failed runs resume cleanly.
- **Parallelism:** `phase_5` (default 4 — same Claude rate-limit constraint
  as phase 4).

**Phase 5b — Index.** Walk the taxonomy and write the per-modality
`SKILL.md`. Each generated topic gets its taxonomy description plus a
`**Use when:** ...` sub-bullet read from the Phase 5a cache:

```markdown
- [Saving and Protecting Documents](.../guide.md) — Saving in various formats, password protection, ...
  - **Use when:** saving with a password, encrypting with GPG key, saving to .docx, configuring AutoRecovery, ...
```

Topics whose guides aren't generated yet appear as
`*(not yet generated)*` and have no use-when bullet.

**Output:** `skills/<domain>-{text,multimodal}-stage1/SKILL.md`

### Phase 6 (optional) — Text-stage1 derived from multimodal-stage1

Phase 6 is opt-in (run with `--phase 6`) and **not part of the default
flow**. It walks every generated multimodal-stage1 guide and rewrites the
inline figure references — lines like ``See `fig01.png`.`` — into 1-3
sentences of verbal description grounded in what the screenshot actually
shows. The result is markdown-only: no images are copied into the text-stage1
tree.

For each topic:
- Read the multimodal `guide.md`, find every ``See `figXX.png``` reference
  (deduped, in first-appearance order).
- Attach the corresponding `figXX.png` files to a Claude call in the same
  order, with a strict prompt: replace each ref with a verbal description,
  do not modify any other text, do not include any image syntax or
  filenames in the output.
- Write the rewritten markdown to
  `skills/<domain>-text-stage1/<cat>/<topic>/guide.md`.
- Topics whose multimodal guide had no figure refs are copied verbatim
  with no Claude call.

After all topics are processed, the multimodal use-when cache is mirrored
to the text-stage1 cache (the topic semantics are unchanged, so the routing
keywords apply equally), and `phase_index` runs for `text` mode to write
`skills/<domain>-text-stage1/SKILL.md`.

- **Workspace cache:** `workspace/<domain>/text_stage1_drafts/<cat>/<topic>.md`
- **Final output:** `skills/<domain>-text-stage1/<cat>/<topic>/guide.md`
  and `skills/<domain>-text-stage1/SKILL.md`
- **Parallelism:** `phase_6` (default 4 — Claude rate-limit bound).
- **Idempotent:** topics whose final `guide.md` already exists are skipped.

Run with:
```bash
./run.sh --config configs/libreoffice_writer.yaml --phase 6
```

(Mode flag is ignored for phase 6 — it always reads multimodal-stage1 and
writes text-stage1.)

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
    # Optional: restrict the crawl to a sub-section of the docs site.
    # Useful when the root page is a top-level index that mixes target
    # docs with out-of-scope siblings (e.g. a docs home that lists both
    # User Guide and Developer Guide).
    # path_prefix: "/support/"
```

`crawl_depth` controls how many link-hops we follow from the root when
harvesting structure. Depth 1 = the root page only (its links become topics).
Depth 2 = also walk each linked page's headings to discover sub-topics.
Content for each topic is always fetched in Phase 2 regardless of depth.

`path_prefix` (optional) restricts which links are followed AND which
outline entries are kept. The root URL itself is exempt so the entry-point
page always loads. Use it when the docs root mixes in unrelated sections
you don't want to taxonomize.

**Single tutorial page.** `root_url` doesn't have to be a documentation hub
— it can be one tutorial URL like
`https://www.zotero.org/support/quick_start_guide`. Set `crawl_depth: 1` and
Phase 1 will parse only that page's headings. Phase 2 then fetches that one
page's HTML, converts it to markdown, and downloads its inline `<img>`s.
The taxonomy will naturally collapse to a small (1-3 category) shape —
`TAXONOMY_FROM_HTML_PROMPT` allows this when the source warrants it. No
code changes needed across modes.

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
├── <domain>-text-stage1/
│   ├── SKILL.md
│   └── <category>/<topic>/guide.md
└── <domain>-multimodal-stage1/
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
├── html_pages/<topic>/         # HTML mode: page_NNNN.md + images/img_NNN.<ext>
├── pdf_figures/<topic>/        # PDF mode: cropped figures + figures.json
├── html_figures/<topic>/       # HTML mode: downloaded <img>s + figures.json
├── text_drafts/<cat>/<topic>.md       # text-mode prose draft cache
└── multimodal_drafts/<cat>/<topic>.md # multimodal-mode draft cache (with raw_NNN.png refs)
```

## Requirements

- Python 3.10+ (uses `X | Y` type unions)
- `claude` CLI authenticated (model: `claude-opus-4-6`)
- `PyMuPDF`, `Pillow`, `PyYAML` — for PDFs
- `requests`, `beautifulsoup4`, `markdownify` — for HTML mode

## Architecture notes

- **Single script**: `generate_skill_from_knowledge_source.py`. The runner
  dispatches on the YAML config. There used to be `generate_from_docs.py` and
  `generate_from_tasks.py`; they're unified.
- **All LLM calls** route through a thin `call_claude()` wrapper that shells
  out to the `claude` CLI. The CLI is run from `cwd=/tmp` because the project
  directory's `.claude/`/`.mcp.json` configuration confuses non-interactive
  invocations.
- **Parallelism** is set per-phase in the YAML config under a `parallel:` block:
  `phase_2` (page rendering, default 8), `phase_3` (figure extraction,
  default 8), `phase_4` (guide generation, default 4 — Claude rate-limit
  bound), `phase_5` (use-when routing hints, default 4 — same constraint
  as phase 4), `phase_6` (text-stage1 derivation, default 4 — optional phase,
  same constraint). Phase 1 ToC OCR is intentionally serial — parallel
  cold-start of `claude -p` can trip the OAuth `client_data` rate limit.
- **Caching is aggressive**: every phase keys its outputs into `workspace/`
  and skips on hit. Delete a specific cache file to force that phase only.

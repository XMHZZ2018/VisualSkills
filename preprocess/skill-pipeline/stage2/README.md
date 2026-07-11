# Skill Pipeline (Stage 2) — UI-explorer

Generate domain-specific skills (text and multimodal) by **driving the live
application** in a Docker container. An Opus planner inspects screenshots and
proposes ~8 UI exploration regions; ~8 Sonnet workers explore those regions in
parallel; an Opus assembler synthesizes their notes into per-region UI
Reference markdown + cropped screenshots; the result is then *inlined* into
the existing Stage 1 skill to produce **multimodal-skill-stage2**, and finally a
text-only twin **text-skill-stage2** is derived from mm-stage2.

> **Stage 2 always runs on the GCP `osworld` VM**, since phases 1-3 spin up
> CUA-World Docker containers (sysbox runtime).  `run.sh` rsyncs this
> directory to the VM and SSHs in to launch the requested phase.

```bash
# Full chain end-to-end (paper default: mm-stage2 + text-stage2 via derive).
./run.sh --config configs/impress.yaml --phase all

# Independent text prose (Option 1) — text-stage2 written from scratch by
# a separate Claude pass over the same worker notes, in parallel with mm-stage2.
./run.sh --config configs/impress.yaml --phase all \
    --mode both --text-source independent

# One-step invocations (backward compat):
./run.sh --config configs/impress.yaml             # phases 1, 2, 3a + 3b (on VM)
./run.sh --config configs/impress.yaml --phase 3b  # re-run mapper only
./run.sh --config configs/impress.yaml --phase 4   # inline mm regions → mm-stage2
./run.sh --config configs/impress.yaml --phase 4t  # inline text regions → text-stage2 (Option 1)
./run.sh --config configs/impress.yaml --phase 5   # derive text-stage2 from mm-stage2 (Option 3)
```

Two axes control what gets built:

- `--mode text | multimodal | both` — which artifacts to produce (default `both`).
- `--text-source independent | derived` — how the text-stage2 artifact is produced
  (default `derived`, matches paper):
  - **derived** (Option 3) — Phase 5 verbalizes the mm-stage2 figure refs. Text and
    mm prose are identical up to those refs; isolates the modality contribution.
  - **independent** (Option 1) — Phase 4t runs a separate text-only Claude assembler
    pass over the same worker notes + screenshots. Text prose is genuinely
    independent of mm prose but the region set is mirrored so a single
    region→guide mapping serves both artefacts.

The two "generate both" ergonomics mirror Stage 1's `--mode both --text-source X`.

## How Stage 2 differs from Stage 1

| | Stage 1 (`../stage1/`) | Stage 2 (this dir) |
|---|---|---|
| **Knowledge source** | Existing PDF / HTML docs | Live app screenshots from a running container |
| **Topic taxonomy** | Mined from PDF ToC, HTML headings, or task clustering | Opus planner proposes regions ad-hoc from a single screenshot |
| **Per-topic content** | One Claude call per topic over rendered page images | One Sonnet *worker* per region, autonomously clicking through the UI for up to N actions |
| **Output structure** | Flat `<cat>/<topic>/guide.md` + `figNN.png` | Same as Stage 1 (mm-stage2 is mm-stage1 with appended `## UI Reference — <region>` sections + `ui-*.png` crops) |
| **Where mm-stage2 plugs in** | n/a | `inline_into_stage1.py` merges into a fresh copy of mm-stage1; SKILL.md is unchanged |

Stage 2 is meant to *augment* Stage 1, not replace it: the regions discovered by live
exploration become per-topic UI Reference appendices in mm-stage1's existing
skill tree.

## Pipeline phases

### Phase 1 — Plan (Opus)
`plan.py` runs the Opus planner: it boots the env via CUA-World using the
synthetic **`_warmup`** task (see "Per-env `_warmup` task" below), takes a
single screenshot of the idle app window, and asks Claude to enumerate ~8
UI regions worth exploring (e.g., "drawing toolbar", "properties sidebar").
The planner emits `plan/plan.json` with one entry per `target_id`.

- **Model:** `planner_model` (default `claude-opus-4-6`)
- **Output:** `<output_dir>/plan/plan.json`
- **Wall clock:** `planner_timeout` (default 600s)

### Phase 2 — Workers (N × Sonnet, parallel)
For each target in `plan.json`, `worker.py` spawns a separate Python
subprocess with its own cua-world env (own Docker container, own bridge
port). Each worker boots a Sonnet Claude CLI inside `claude_cli_image`,
gives it the target's name + scope, and lets it click through the relevant
region of the UI. The worker writes:

- `worker_NN_<target_id>/notes.md`     — narrative observations
- `worker_NN_<target_id>/notes.json`   — structured records (each click + observed state)
- `worker_NN_<target_id>/screenshots/` — captured PNGs

- **Model:** `worker_model` (default `claude-sonnet-4-6`)
- **Parallelism:** `n_workers` (default 8) — each in its own subprocess, no shared state
- **Per-worker budget:** `task_timeout` (default 1800s wall) and `max_actions` (default 80)
- **Bridge ports:** `bridge_port_base + i + 1` for worker *i*

### Phase 3 — Assemble → mm-stage2
Phase 3 turns the raw worker notes into the finished `mm-stage2` skill. It
has three sub-steps; the orchestrator runs 3a + 3b automatically, and 3c
is invoked via `run.sh --phase 4` once mm-stage2 is ready to be merged.

**3a. Assembler (Opus, `assemble.py`).** Runs Opus on the host with
`cwd = <output_dir>`. Reads every worker's `notes.md` + `notes.json`,
selectively opens screenshots via the local `img_tool.py` helper
(Bash-callable crop/inspect utility), and writes the per-region skill
folder:

- `skill/regions/<region_id>.md` — one markdown file per region with H1, scope, screenshot block, and a per-element table
- `skill/images/*.png`           — cropped screenshots referenced by the regions

- **Model:** `assembler_model` (default `claude-opus-4-6`)
- **Wall clock:** `assembler_timeout` (default 2400s)

**3b. Region → guide mapper (Opus, `map_regions.py`).** Reads
`skill/regions/*.md` plus the mm-stage1 `SKILL.md` and the first ~40 lines of
each `guide.md`, then asks Opus to emit
`<output_dir>/region_to_guides.json` consumed by 3c. Each region is
annotated with one or more owners (`{guide, confidence, scope}`) using
these confidence levels:

- `primary`  — the region directly documents UI for that guide's task.
- `relevant` — the region overlaps with the guide but is not its main subject.
- `weak`     — only tangentially related; would bloat the guide if inlined.

Regions whose owners are all weak, or that are app-wide with no real
owner, are marked `drop_recommended: true` and skipped by 3c. This step
replaces the previously hand-curated mapping file.

- **Model:** `mapper_model` (default `claude-opus-4-6`)
- **Wall clock:** `mapper_timeout` (default 900s)
- **Re-run only this step:** `./run.sh --config configs/<d>.yaml --phase 3b`

**3c. Inline (deterministic, `inline_into_stage1.py`).** Reads the
auto-generated mapping at `<output_dir>/region_to_guides.json` and, for
each owning Stage 1 guide, does:

1. Strips the region.md's frontmatter and screenshot block.
2. Rewrites image references from markdown `![]()` syntax to mm-stage1's
   `Read the screenshot \`name.png\` in this directory` convention (the
   CUA-World agent does not auto-fetch `![]()` — it only reads files
   it's explicitly told to read).
3. Copies the region's PNGs next to the Stage 1 guide with a `ui-` prefix.
4. Appends a `## UI Reference — <region_name>` section to the guide.

The output is a fresh copy of mm-stage1 sitting at
`skills/<domain>-multimodal-stage2/`. **SKILL.md is unchanged** —
the Stage 2 augmentation is purely additive at the per-guide level.

- No Claude calls (deterministic merge).
- Owner confidence policy: `primary` and `relevant` are appended; `weak`
  is skipped. Regions marked `drop_recommended` or `orphan` are skipped.
- **Invoked as:** `./run.sh --config configs/<d>.yaml --phase 4`
  (kept as numeric flag `4` for backward compat; conceptually this is
  sub-step 3c).

### Phase 4 — Text-stage2 (Claude, mirrors Stage 1 Phase 6)
`derive_text.py` walks every `guide.md` under
`skills/<domain>-multimodal-stage2/` and replaces inline image
references — both the mm-stage1 ``See `figXX.png``` style and the stage2-appended
``Read the screenshot `ui-foo.png` in this directory`` style — with 1-3
sentences of verbal description grounded in what the screenshot actually
shows. The result is markdown-only at
`skills/<domain>-text-stage2/<cat>/<topic>/guide.md` plus a verbatim
copy of mm-stage2's `SKILL.md`.

This phase **delegates to Stage 1's `derive_text_from_multimodal_dir`** (in
`../stage1/generate_skill_from_knowledge_source.py`) so the prompt, caching,
and idempotent semantics are shared. The only Stage 2-specific bit is an
extended regex (`FIG_REF_PATTERN` in `derive_text.py`) that catches
both reference styles.

- **Workspace cache:** `workspace/<domain>/text_stage2_drafts/<cat>/<topic>.md`
- **Idempotent:** topics whose final `guide.md` already exists are skipped.
- **Parallelism:** `text_v3_parallel` (default 4 — Claude rate-limit bound).

## Config schema

```yaml
# Skill identity (used by phases 3c & 4)
domain: libreoffice_impress

app_name: "LibreOffice Impress"
app_version: "7.3.7"

# cua-world environment to drive
env_dir: vendor/gym-anything/.../libreoffice_impress_env
planner_task_id: _warmup                 # synthetic task: bare app + maximize, no fixture

# Where pipeline artefacts (plan/, workers/, skill/, region_to_guides.json) land.
# Persistent (committed to repo).
output_dir: preprocess/skill-pipeline/stage2/outputs/impress

# Phase 1-3 fan-out + budgets
n_workers: 8
bridge_port_base: 9100
planner_model: claude-opus-4-6
worker_model: claude-sonnet-4-6
assembler_model: claude-opus-4-6
mapper_model: claude-opus-4-6
claude_cli_image: cw-claude-cli
task_timeout: 1800
max_actions: 80
action_wait: 1.0
planner_timeout: 600
assembler_timeout: 2400
mapper_timeout: 900

# Phase 5 parallelism
text_v3_parallel: 4
```

## File layout

```
stage2/
├── README.md                          (this file)
├── run.sh                             # rsync to VM + launch phase (always remote)
├── orchestrator.py                    # phases 1 → 2 → 3a → 3b driver
├── plan.py / worker.py / assemble.py  # phase 1 / 2 / 3a implementations
├── map_regions.py                     # phase 3b: auto-map regions → mm-stage1 guides (Opus)
├── prompts.py                         # planner / worker / assembler / mapper prompts
├── img_tool.py                        # Bash-callable crop/inspect helper used by assembler
├── inline_into_stage1.py              # phase 3c: deterministic mm-stage2 merge
├── derive_text.py                     # phase 4: text-stage2 from mm-stage2 (reuses Stage 1 phase 6 core)
├── configs/
│   └── <domain>.yaml
└── outputs/<domain>/                  # per-domain pipeline artefacts (the config's output_dir)
    ├── region_to_guides.json          # phase 3b auto-generated mapping
    ├── plan/plan.json                 # phase 1
    ├── workers/worker_NN_*/           # phase 2
    └── skill/{regions,images}/        # phase 3a
```

## Output layout

```
skills/
├── <domain>-multimodal-stage2/  # mm-stage1 + appended UI Reference sections
│   ├── SKILL.md                       # copied verbatim from mm-stage1
│   └── <category>/<topic>/
│       ├── guide.md                   # mm-stage1 guide with `## UI Reference — <region>` appended
│       ├── fig01.png ...              # original mm-stage1 figures (untouched)
│       └── ui-<region>-*.png          # new screenshots from Stage 2
└── <domain>-text-stage2/        # text twin of mm-stage2 — image refs verbalized
    ├── SKILL.md                       # copied verbatim from mm-stage2
    └── <category>/<topic>/guide.md
```

## Per-env `_warmup` task

Phase 1's planner needs an *idle* app window — no fixture, no test-case
state.  Rather than reuse a real task (which would couple the planner to a
specific scenario), each cua-world env we explore must provide a
synthetic `_warmup` task at:

```
vendor/gym-anything/.../<env>/tasks/_warmup/
├── task.json          # references setup_task.sh + a no-op verifier
├── setup_task.sh      # launches the bare app, maximizes; no fixture
└── verifier.py        # always returns {"passed": True, ...}
```

The config sets `planner_task_id: _warmup` and the planner spins up the env
through the standard CUA-World lifecycle, takes one screenshot, then tears
down.  See `vendor/gym-anything/.../libreoffice_impress_env/tasks/_warmup/`
for the reference implementation.

## Running on the GCP VM

`run.sh` always runs on the `osworld` VM.  It rsyncs this directory (so any
local edits to scripts or configs take effect) and then SSHs in to launch
the requested phase.  After phases 4 and 5 (foreground mode), it rsyncs
the produced `skills/<domain>-{multimodal,text}-stage2/` directories
back to the local tree.

```bash
./run.sh --config configs/impress.yaml             # phases 1-3, nohup'd on VM
./run.sh --config configs/impress.yaml --force     # wipe output_dir first
./run.sh --config configs/impress.yaml --phase 4 --foreground
./run.sh --config configs/impress.yaml --phase 5 --foreground
```

## Requirements

- Python 3.10+
- `claude` CLI authenticated (Opus + Sonnet)
- `PyYAML`, `Pillow`
- CUA-World (`vendor/gym-anything/`) with the target env's Docker image built
- `cw-claude-cli` Docker image (the same one used by `scripts/run-cua-world/`)

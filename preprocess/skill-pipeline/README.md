# Skill Pipelines

Two parallel pipelines that produce Claude Code-style skills (SKILL.md +
per-topic guide.md + figures) for desktop applications.

| | [`stage1/`](stage1/README.md) | [`stage2/`](stage2/README.md) |
|---|---|---|
| **What** | text-skill-stage1 + multimodal-skill-stage1 | text-skill-stage2 + multimodal-skill-stage2 |
| **Source of knowledge** | PDF user guide / HTML docs / gym-anything task list | Live app screenshots from a Docker container |
| **How taxonomy is built** | Mined from PDF ToC / HTML headings / clustered task descriptions | Opus planner inspects one screenshot, proposes ~8 UI regions |
| **How content is generated** | One Claude call per topic over rendered page images | ~8 Sonnet workers in parallel autonomously click through the UI; an Opus assembler synthesizes their notes |
| **Where the output goes** | `skills/<domain>-{text,multimodal}-stage1/` | `skills/<domain>-{text,multimodal}-stage2/` (mm-stage2 = mm-stage1 + appended `## UI Reference` sections) |
| **Phases** | 1 Taxonomy → 2 Pages → 3 Figures → 4 Guides → 5 Use-when + Index → (6 optional: text-stage1 from mm-stage1) | 1 Plan → 2 Workers → 3 Assemble → 4 Inline → 5 Text-stage2 |

**Code reuse:** Stage 2 Phase 5 (text-stage2 from mm-stage2) imports
`derive_text_from_multimodal_dir` from Stage 1's
`generate_skill_from_knowledge_source.py`, with an extended regex that catches
both `See \`figXX.png\`` and `Read the screenshot \`X.png\`` reference styles.

See each subdir's README for full phase details, configs, and run commands.

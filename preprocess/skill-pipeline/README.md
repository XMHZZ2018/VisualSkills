# Skill Pipelines

Two parallel pipelines that produce Claude Code-style skills (SKILL.md +
per-topic guide.md + figures) for desktop applications.

| | [`v1/`](v1/README.md) | [`v3/`](v3/README.md) |
|---|---|---|
| **What** | text-skill-v1 + multimodal-skill-v1 | text-skill-v3 + multimodal-skill-v3 |
| **Source of knowledge** | PDF user guide / HTML docs / gym-anything task list | Live app screenshots from a Docker container |
| **How taxonomy is built** | Mined from PDF ToC / HTML headings / clustered task descriptions | Opus planner inspects one screenshot, proposes ~8 UI regions |
| **How content is generated** | One Claude call per topic over rendered page images | ~8 Sonnet workers in parallel autonomously click through the UI; an Opus assembler synthesizes their notes |
| **Where the output goes** | `skills/<domain>-knowledge-{text,multimodal}-v1/` | `skills/<domain>-knowledge-{text,multimodal}-v3/` (mm-v3 = mm-v1 + appended `## UI Reference` sections) |
| **Phases** | 1 Taxonomy → 2 Pages → 3 Figures → 4 Guides → 5 Use-when + Index → (6 optional: text-v1 from mm-v1) | 1 Plan → 2 Workers → 3 Assemble → 4 Inline → 5 Text-v3 |

**Code reuse:** v3 Phase 5 (text-v3 from mm-v3) imports
`derive_text_from_multimodal_dir` from v1's
`generate_skill_from_knowledge_source.py`, with an extended regex that catches
both `See \`figXX.png\`` and `Read the screenshot \`X.png\`` reference styles.

See each subdir's README for full phase details, configs, and run commands.

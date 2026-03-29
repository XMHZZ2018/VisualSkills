# Skill from Tutorial

Generate OS World skills (text + multimodal) by analyzing YouTube tutorial videos.

## Pipeline

For each query:

1. **Search & Download** (`search-and-download.md`): Search YouTube → pick best video → download
2. **Extract & Summarize** (`extract-and-summarize.md`): Sparse frames → transcript → summary → precise frames
3. **Generate Skills** (`generate-skills.md`): Synthesize across all queries → create skills with sub-guide structure

Batch scripts are also available for steps 1-2:
- `batch_search.py` — search YouTube for all queries and log results
- `batch_download.py` — download selected videos for all queries
- `batch_extract.py` — extract sparse frames and convert VTT transcripts

## Assets structure

```
assets/searched/
├── index.md                    ← overview of all queries
├── change-default-search/      ← one dir per query (slug from instruction)
│   ├── search_results.md
│   ├── video.mp4               ← (gitignored)
│   ├── video.en.vtt            ← (gitignored)
│   ├── transcript.md
│   ├── summary.md
│   └── frames/                 ← (gitignored)
│       ├── frame_0001_t0s.png
│       ├── frame_0002_t10s.png
│       └── keyframe_t25s.png
├── clear-cookies/
│   └── ...
└── ...
```

## Output

Two skills created from all queries combined, both with sub-guide structure:

```
skills/os-world/text/chrome-knowledge/
├── SKILL.md                     ← index (frontmatter + sub-guide table)
├── settings/guide.md
├── bookmarks-tabs/guide.md
├── privacy/guide.md
├── extensions/guide.md
├── downloads-shortcuts/guide.md
├── passwords/guide.md
└── google-services/guide.md

skills/os-world/multimodal/chrome-knowledge/
├── SKILL.md                     ← index (frontmatter + sub-guide table)
├── settings/
│   ├── guide.md
│   └── *.png                   ← selected frames for this topic
├── bookmarks-tabs/
│   ├── guide.md
│   └── *.png
└── ...
```

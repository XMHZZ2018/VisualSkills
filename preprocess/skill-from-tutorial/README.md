# Skill from Tutorial

Generate OS World skills (text + multimodal) by analyzing YouTube tutorial videos.

## Pipeline

For each query:

1. **Search & Download** (`search-and-download.md`): Search YouTube → pick best video → download
2. **Extract & Summarize** (`extract-and-summarize.md`): Sparse frames → transcript → summary → precise frames
3. **Generate Skills** (`generate-skills.md`): Synthesize across all queries → create one Chrome knowledge skill

## Assets structure

```
assets/searched/
├── index.md                    ← overview of all queries
├── change-default-search/      ← one dir per query (slug from instruction)
│   ├── search_results.md
│   ├── video.mp4
│   ├── transcript.md
│   ├── summary.md
│   └── frames/
│       ├── frame_0001_t0s.png      ← sparse frames (first pass)
│       ├── frame_0002_t10s.png
│       └── keyframe_t25s.png       ← precise frames (second pass)
├── clear-cookies/
│   └── ...
└── ...
```

## Output

Two skills created from all queries combined:
- `skills/os-world/text/chrome-knowledge/SKILL.md`
- `skills/os-world/multimodal/chrome-knowledge/SKILL.md` (with sub-guides + embedded screenshots)

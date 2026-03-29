# paper-beautify

Beautifies LaTeX paper formatting by learning from real published papers in the same venue.

## Two-step workflow

1. **`/setup-paper-refs`** — Search, download, convert to PNGs with annotations → `assets/searched/`
2. **`/format-paper`** — Read `index.md` + images from both `curated/` and `searched/`, apply formatting

## Assets

```
assets/
├── curated/              # Your hand-picked references (never auto-deleted)
│   ├── index.md          # Human-maintained: lists images + why you picked them
│   ├── example_page.png
│   └── example_page.md   # 1-3 sentences on what you like about it
└── searched/             # Auto-populated by /setup-paper-refs
    ├── index.md          # Auto-generated: lists all papers + annotations
    ├── paper_page_1.png
    └── paper.md          # Auto-generated: title, venue, notable formatting
```

## MCP tools used

| Tool | Server | Used by |
|------|--------|---------|
| `search_papers` | paper-search | setup-paper-refs |
| `search_arxiv` | paper-search | setup-paper-refs |
| `download_paper` | paper-search | setup-paper-refs |
| `pdf_to_images` | pdf-to-images | setup-paper-refs, format-paper |

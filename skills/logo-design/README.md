# logo-design

Design a logo by learning from reference logos online and your curated favorites.

## Two-step workflow

1. **`/setup-logo-refs`** — Search, download, judge, annotate reference logos → `assets/searched/`
2. **`/logo-design`** — Read `index.md` + images from both `curated/` and `searched/`, generate logo

## Assets

```
assets/
├── curated/              # Your hand-picked logos (never auto-deleted)
│   ├── index.md          # Human-maintained: lists images + why you like them
│   ├── stripe_logo.jpg
│   └── stripe_logo.md   # "Clean wordmark, simple gradient. Love the minimalism."
└── searched/             # Auto-populated by /setup-logo-refs
    ├── index.md          # Auto-generated: lists all logos + annotations
    ├── openai_avatar.jpg
    └── openai_avatar.md  # Auto-generated: what it depicts, what works
```

## MCP tools used

| Tool | Server | Used by |
|------|--------|---------|
| `search_images` | image-search | setup-logo-refs |
| `download_image` | image-search | setup-logo-refs |
| `generate_image` | image-gen | logo-design |
| `edit_image` | image-gen | logo-design |

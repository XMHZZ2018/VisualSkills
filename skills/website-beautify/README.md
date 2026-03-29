# website-beautify

Improve a personal academic website by learning from the best websites in your field.

## Two-step workflow

1. **`/setup-website-refs`** — Screenshot your site + similar ones, judge, annotate → `assets/searched/`
2. **`/website-beautify`** — Read `index.md` + screenshots from both `curated/` and `searched/`, apply improvements

## Assets

```
assets/
├── curated/              # Your hand-picked website screenshots (never auto-deleted)
│   ├── index.md          # Human-maintained: lists screenshots + what you like
│   ├── favorite_site.png
│   └── favorite_site.md  # "Love the dark theme and pub layout with thumbnails."
└── searched/             # Auto-populated by /setup-website-refs
    ├── index.md          # Auto-generated: lists all screenshots + annotations
    ├── screenshot_1.png
    └── screenshot_1.md   # Auto-generated: URL, researcher, what's good about it
```

## MCP tools used

| Tool | Server | Used by |
|------|--------|---------|
| `screenshot_url` | web-screenshot | setup-website-refs, website-beautify |
| `screenshot_urls` | web-screenshot | setup-website-refs |

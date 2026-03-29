# Generate Skills

## Step 5: Generate both text and multimodal skills

### 5a: Synthesize across all queries

Read all query summaries and transcripts from `preprocess/skill-from-tutorial/assets/searched/<query-slug>/`:
- `summary.md` — key moments with visual descriptions and timestamps
- `transcript.md` — full spoken transcript

Cross-reference across all queries to:
- Group queries by **topic area** (e.g., settings, bookmarks, extensions, privacy)
- Identify **shared navigation patterns** (e.g., opening Settings, accessing chrome://flags)
- Pick the **clearest explanation** of each procedure from its tutorial
- Identify **common pitfalls** mentioned across tutorials

Decide the topic grouping. Each topic becomes a sub-directory with its own `guide.md`. Typical groupings:
- `settings/` — search engine, homepage, startup, font size, language, profile, dark mode, UI flags
- `bookmarks-tabs/` — bookmark a page, create folder, restore tabs
- `privacy/` — cookies, browsing data, Do Not Track, Safe Browsing
- `extensions/` — install unpacked extension
- `downloads-shortcuts/` — save as PDF, desktop shortcuts
- `passwords/` — view saved passwords
- `google-services/` — Google Flights

### 5b: Generate text-only skill

The text skill uses the same sub-guide structure as multimodal, just without images.

#### Directory structure

```
skills/os-world/text/chrome-knowledge/
├── SKILL.md                     ← index only
├── settings/
│   └── guide.md
├── bookmarks-tabs/
│   └── guide.md
├── privacy/
│   └── guide.md
├── extensions/
│   └── guide.md
├── downloads-shortcuts/
│   └── guide.md
├── passwords/
│   └── guide.md
└── google-services/
    └── guide.md
```

#### SKILL.md (index)

```markdown
---
name: chrome-knowledge
description: Comprehensive guide for Chrome browser tasks — settings, bookmarks, extensions, privacy, downloads, and more
---

# Chrome Knowledge

Reference guide for performing common Chrome browser tasks.

## Sub-Guides

| Topic | Guide | Description |
|-------|-------|-------------|
| Settings | [settings/guide.md](./settings/guide.md) | Default search engine, homepage, startup, appearance, language, font size |
| Bookmarks & Tabs | [bookmarks-tabs/guide.md](./bookmarks-tabs/guide.md) | Bookmark management, tab restore |
| Privacy & Security | [privacy/guide.md](./privacy/guide.md) | Cookies, browsing data, Do Not Track, Safe Browsing |
| Extensions | [extensions/guide.md](./extensions/guide.md) | Install unpacked extensions |
| Downloads & Shortcuts | [downloads-shortcuts/guide.md](./downloads-shortcuts/guide.md) | Save as PDF, desktop shortcuts |
| Passwords | [passwords/guide.md](./passwords/guide.md) | View saved passwords |
| Google Services | [google-services/guide.md](./google-services/guide.md) | Google Flights |
```

#### Each guide.md

```markdown
# <Topic> Guide

## <Task Name>

### Steps
1. ...
2. ...

### Verification
...

---

## <Task Name 2>
...
```

**Text-only guidelines:**
- Translate visual demonstrations into concrete text instructions
- Include specific UI element names, menu paths, button labels
- Include specific URLs (e.g., `chrome://settings/searchEngines`) where known from transcripts
- Include keyboard shortcuts where mentioned (e.g., Ctrl+Shift+T)
- Must be **self-contained** — no references to videos or external resources

### 5c: Generate multimodal skill

Same structure as text, but each topic sub-directory also contains selected screenshot frames.

#### Directory structure

```
skills/os-world/multimodal/chrome-knowledge/
├── SKILL.md                     ← index only
├── settings/
│   ├── guide.md
│   ├── search-engine-menu.png
│   ├── font-size-dropdown.png
│   └── ...
├── bookmarks-tabs/
│   ├── guide.md
│   ├── bookmark-added-dialog.png
│   └── ...
├── privacy/
│   ├── guide.md
│   ├── do-not-track-toggle.png
│   └── ...
└── ...
```

#### SKILL.md (index)

Same as text version but with description mentioning "visual references":

```markdown
---
name: chrome-knowledge
description: Comprehensive guide for Chrome browser tasks with visual references — settings, bookmarks, extensions, privacy, downloads, and more
---

# Chrome Knowledge

Visual reference guide for performing common Chrome browser tasks.

## Sub-Guides

| Topic | Guide | Description |
|-------|-------|-------------|
| Settings | [settings/guide.md](./settings/guide.md) | ... |
| ... | ... | ... |
```

#### Each guide.md

Same step-by-step content as the text version, but with embedded screenshots at key checkpoints:

```markdown
# Settings Guide

## Change Default Search Engine

### Steps

1. Open Chrome Settings (⋮ → Settings, or `chrome://settings`)

2. Click "Search engine" in the left sidebar. The page should look like this:

![Search engine settings page](./search-engine-menu.png)

3. Click the dropdown next to "Search engine used in the address bar"
4. Select the desired search engine

### Verification

The selected search engine now appears in the dropdown.
```

#### Frame selection and placement

- Read the `summary.md` for each query to identify which frames show key UI states
- Copy selected frames from `preprocess/skill-from-tutorial/assets/searched/<query-slug>/frames/` into the appropriate topic sub-directory
- Rename frames descriptively (e.g., `search-engine-menu.png`, `clear-cookies-dialog.png`)
- Reference with relative paths: `![description](./filename.png)`
- Typically 1-3 frames per task (navigation target, setting to change, verification)

**Frame selection criteria:**
- Shows the exact UI state the user should see at that step
- Text is legible
- No overlapping dialogs or irrelevant popups

### 5d: Register in marketplace.json

Update both plugin marketplace files to include the new skill:
- `plugins/osworld-text/.claude-plugin/marketplace.json` → `"./skills/os-world/text/chrome-knowledge"` in the skills array
- `plugins/osworld-multimodal/.claude-plugin/marketplace.json` → `"./skills/os-world/multimodal/chrome-knowledge"` in the skills array

### 5e: Report

Output:
- Paths to both generated skill directories
- Summary of what the skill covers (grouped by topic area)
- Number of queries synthesized and frames selected
- List of sub-guides created with task counts

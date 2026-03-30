# Skill Pipeline

Generate domain-specific skills from YouTube tutorials using a taxonomy-driven approach.

## Pipeline Overview

```
discover.py → taxonomy.json → generate.py → skills/
                                   ↓
                              evolve.py (future)
```

## Quick Start

```bash
cd preprocess/skill-pipeline

# 1. Build taxonomy for a domain
python3 discover.py --domain chrome

# 2. Generate skills (text + multimodal)
python3 generate.py --domain chrome --mode both
```

## Phase 1+2: Discover & Organize (`discover.py`)

Builds a hierarchical taxonomy for a domain using two sources:

1. **Claude's knowledge** — drafts an initial taxonomy with 20-40 leaf topics
2. **YouTube validation** — searches multiple query variants per topic, attaches best video

Each leaf gets 2-3 `search_queries` (different phrasings users would type). All variants are searched, results deduplicated, and the best video is selected by view count (preferring ≤10 min).

A broad YouTube search also catches topics Claude may have missed.

```bash
python3 discover.py --domain chrome
python3 discover.py --domain chrome --skip-youtube  # Claude-only, no validation
```

Output: `data/<domain>/taxonomy.json`

### Taxonomy structure

Max depth = 3 (root → category → leaf topic):

```
Chrome (depth 0)
├── Privacy & Security (depth 1)
│   ├── safe-browsing (depth 2, leaf)
│   ├── clear-cache-cookies (leaf)
│   └── ...
├── Tabs & Windows (depth 1)
│   └── ...
└── ...
```

## Phase 3: Generate Skills (`generate.py`)

For each leaf topic in the taxonomy:

### Text skills
1. Download video + transcript (via yt-dlp)
2. Claude generates a step-by-step `guide.md` from the transcript

### Multimodal skills (coarse-to-fine frame selection)

```
Pass 1 (coarse):
  Extract frames at adaptive interval → Claude sees transcript + coarse frames
  Claude outputs: guide steps + "step 3 needs screenshot at ~45s"

Pass 2 (fine):
  Extract frames every 1s within ±3s of each key timestamp
  Claude picks the best frame per step

Pass 3 (assemble):
  guide.md with step text + embedded PNGs
```

Adaptive coarse interval based on video duration:

| Duration | Interval | ~Frames |
|----------|----------|---------|
| <1 min | 2s | ~30 |
| 1-2 min | 3s | ~40 |
| 2-5 min | 5s | ~60 |
| 5-10 min | 10s | ~60 |
| 10-20 min | 20s | ~60 |

Videos over 20 minutes are skipped.

```bash
# Generate both text and multimodal
python3 generate.py --domain chrome --mode both

# Text only (no video download needed beyond transcript)
python3 generate.py --domain chrome --mode text

# Multimodal only
python3 generate.py --domain chrome --mode multimodal

# Single topic
python3 generate.py --domain chrome --node safe-browsing
```

### Output structure

```
skills/os-world/text/chrome-knowledge/
├── SKILL.md                              # Auto-generated index
├── tabs-windows/
│   ├── open-close-tabs/guide.md
│   └── pin-tabs/guide.md
└── privacy-security/
    └── safe-browsing/guide.md

skills/os-world/multimodal/chrome-knowledge/
├── SKILL.md
├── tabs-windows/
│   ├── open-close-tabs/
│   │   ├── guide.md
│   │   ├── step01.png
│   │   ├── step03.png
│   │   └── step05.png
│   └── ...
└── ...
```

## Phase 4: Evolve (`evolve.py`) — planned

Incrementally update the taxonomy as new tasks arrive. Uses COBWEB-style operations:

| Operation | When |
|-----------|------|
| **ABSORB** | Task fits an existing leaf |
| **CREATE** | No leaf matches → add new leaf |
| **SPLIT** | A leaf is too broad → break into sub-leaves |
| **MERGE** | Two siblings overlap → combine |

See [DESIGN.md](DESIGN.md) for full details.

## Data layout

```
preprocess/skill-pipeline/
├── README.md
├── DESIGN.md           # Full design document
├── discover.py         # Phase 1+2
├── generate.py         # Phase 3
├── taxonomy.py         # Shared tree data structure
├── evolve.py           # Phase 4 (planned)
└── data/
    └── chrome/
        ├── taxonomy.json       # Living taxonomy
        ├── evolution_log.json  # Phase 4 audit trail (planned)
        └── videos/             # Downloaded videos + frames (gitignored)
```

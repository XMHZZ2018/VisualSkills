---
name: opentoonz-text-stage1
description: "Practical text-only guides for OpenToonz 1.7. Consult via the load_topic MCP tool — it returns the guide text in one atomic call."
---

# OpenToonz 1.7 Knowledge (text-stage1)

## How to consult this skill

This skill exposes two MCP tools (already registered for you):

- **`load_topic(topic)`** — returns the chosen topic's `guide.md` as one tool response. **Use this instead of `Read` for any `*.md` inside this skill.**
- **`list_topics()`** — returns every topic path available, one per line.

Each entry in the TOC below has the form `[Title](<topic>/guide.md)`. The `<topic>` part (the path before `/guide.md`) is what you pass to `load_topic`.

> You will receive the guide text in a single tool result — no extra `Read` calls needed.

**Rules:**

1. Before any GUI action where you are unsure of the menu path / dialog / icon, find the matching topic in the TOC and call `load_topic` first.
2. You may call `load_topic` **at any step** of the trajectory, not only at the start. If the task moves into a new area, call `load_topic` again for the new area.

## Guides

### Installation and Setup

- [Installing OpenToonz](installation-and-setup/installing-opentoonz/guide.md) — Download and install OpenToonz on Windows, macOS, Linux, or BSD
  - **Use when:** installing OpenToonz on Windows, installing OpenToonz on macOS, installing OpenToonz on Linux, bypassing SmartScreen or Gatekeeper warnings, installing OpenToonz via package manager, installing OpenToonz via Flatpak or Snap
- [Configuring FFmpeg](installation-and-setup/configuring-ffmpeg/guide.md) — Install and configure FFmpeg for video format support
  - **Use when:** installing FFmpeg for OpenToonz, setting FFmpeg path in Preferences, exporting animation as mp4 or webm, rendering gif on Mac/Linux, clearing macOS Gatekeeper for FFmpeg, enabling video formats in Output Settings
- [Customizing the Interface](installation-and-setup/customizing-the-interface/guide.md) — Configure rooms, panes, and interface appearance
  - **Use when:** switching workspace rooms, customizing command bar buttons, changing interface language, changing UI theme, docking and undocking panes, locking room layout
- [Managing Projects](installation-and-setup/managing-projects/guide.md) — Set up projectroot, create projects, configure default folders, and use the project browser
  - **Use when:** creating a new project, setting the projectroot path, switching active projects, configuring default folder aliases, using $scenepath for per-scene folders, adding custom aliases in project_folders.txt
- [Setting Up a Scene](installation-and-setup/setting-up-a-scene/guide.md) — Configure camera, frame rate, working unit, color calibration, and memory settings
  - **Use when:** setting working units and camera units, configuring frame rate in Scene Settings, setting camera size and resolution, enabling color calibration with 3D LUT, tuning undo memory size, saving default settings per project
- [Choosing a Production Workflow](installation-and-setup/choosing-a-production-workflow/guide.md) — Select between traditional (paper-based) and paperless animation workflows
  - **Use when:** scanning and cleaning up paper drawings, setting up paperless cutout animation, painting levels with index-linked palette styles, building reusable character library assets, distributing renders across a farm via TCP/IP, splitting animatics into scene files
- [Configuring Keyboard Shortcuts](installation-and-setup/configuring-keyboard-shortcuts/guide.md) — Customize and use predefined keyboard shortcuts
  - **Use when:** remapping keyboard shortcuts in Configure Shortcuts dialog, saving and loading shortcut presets, temporary tool switching by holding keys, brush size shortcuts, playback navigation shortcuts

### Scanning and Cleanup

- [Scanning Paper Drawings](scanning-and-cleanup/scanning-paper-drawings/guide.md) — Set up scanners, define animation levels, and scan drawings with autocentering
  - **Use when:** defining scanner driver (Internal vs TWAIN), setting scan mode (black and white/greyscale/color), creating a scan level in Xsheet, configuring scan settings and paper feeder, scanning paper drawings to TIF sequences, setting and resetting cropbox
- [Cleaning Up Scanned Drawings](scanning-and-cleanup/cleaning-up-scanned-drawings/guide.md) — Configure cleanup settings, preview results, and process scanned artwork
  - **Use when:** autocentering scanned drawings to pegbar holes, line processing with greyscale or color mode, configuring Cleanup Settings dialog, removing dust with despeckling, batch cleanup via Tasks pane, saving CLN cleanup presets

### Drawing and Painting

- [Drawing Animation Levels](drawing-and-painting/drawing-animation-levels/guide.md) — Draw in OpenToonz using animation techniques, onion skin, and shift and trace
  - **Use when:** creating new animation levels in Xsheet, drawing with Brush and Geometric tools, vector inbetweening with easing, configuring Onion Skin overlays, using Shift and Trace for light table, setting Default Level Type in Preferences
- [Editing Animation Levels](drawing-and-painting/editing-animation-levels/guide.md) — Use the level strip, merge levels, process, save, and export animation levels
  - **Use when:** rearranging frames in Level Strip, renumbering animation levels, merging levels in Xsheet, adjusting brightness and contrast of frames, exporting levels to PNG/TGA/TIF, reverting level to last saved version
- [Managing Palettes and Styles](drawing-and-painting/managing-palettes-and-styles/guide.md) — Use the palette editor, studio palette, animate palettes, and edit styles
  - **Use when:** editing palette styles in Palette Editor, linking styles to Studio Palette, animating palette colors with keyframes, adjusting colors with Palette Gizmo, organizing styles into pages, using Style Editor color/texture tabs
- [Painting Animation Levels](drawing-and-painting/painting-animation-levels/guide.md) — Fill areas, paint lines, and use color models with painting tools
  - **Use when:** filling areas with Fill tool, closing gaps with Tape tool, painting lines and strokes, applying match lines between columns, loading color models, using Fill Depth and Frame Range options

### Xsheet and Timeline

- [Exposing and Managing Levels](xsheet-and-timeline/exposing-and-managing-levels/guide.md) — Expose levels in the Xsheet, edit level settings, and use the file browser
  - **Use when:** loading levels into Xsheet, replacing exposed levels, adjusting Level Settings (DPI/premultiply/subsampling), importing vs loading external assets, exposing Scene Cast levels, toggling column visibility and opacity
- [Working with Columns, Layers, and Cells](xsheet-and-timeline/working-with-columns-layers-and-cells/guide.md) — Manage columns/layers, edit cells, and work globally with frames
  - **Use when:** reordering Xsheet columns/layers, retiming cells with Step/Stretch, folding/collapsing columns, creating Sub-Xsheets, selecting and moving cell ranges, toggling column render/lock/opacity
- [Using Sub-Xsheets](xsheet-and-timeline/using-sub-xsheets/guide.md) — Create and manage sub-xsheets for scene organization
  - **Use when:** collapsing columns into Sub-Xsheet, opening and editing Sub-Xsheet contents, loading TNZ as Sub-Xsheet, exploding Sub-Xsheet into columns, cloning Sub-Xsheet, saving Sub-Xsheet as standalone scene
- [Creating Soundtracks and Lip Syncing](xsheet-and-timeline/soundtrack-and-lip-syncing/guide.md) — Add audio to the timeline and synchronize mouth shapes to dialogue
  - **Use when:** loading WAV/AIFF/MP3 audio into Xsheet, adjusting column volume and render toggle, scrubbing and trimming audio clips, auto lip sync with Rhubarb, importing Papagayo-NG DAT lip sync data, importing Magpie TLS lip sync files
- [Saving and Exporting Scenes](xsheet-and-timeline/saving-and-exporting-scenes/guide.md) — Save, load, import, and export scene files
  - **Use when:** saving scenes and levels, loading recent scene files, configuring auto-save interval, recovering scene backups, exporting scenes between projects, collecting external assets

### Animation

- [Creating Movements](animation/creating-movements/guide.md) — Use the stage schematic to link and animate objects, work in 3D space
  - **Use when:** animating with keyframes and the Animate tool, linking objects in Stage Schematic, creating motion paths, using hooks for walk cycles, adjusting Z-depth in 3D view, setting global keys for transformations
- [Editing Curves and Expressions](animation/editing-curves-and-expressions/guide.md) — Use the function editor to define keyframes, interpolations, and mathematical expressions
  - **Use when:** adding keyframes in Function Editor, editing interpolation curves, writing expressions with variables, looping animation cycles, exporting .curve files, adjusting Speed In/Out Bezier handles
- [Creating Cutout Animation](animation/creating-cutout-animation/guide.md) — Build skeletons, create models with hooks, and animate using inverse kinematics
  - **Use when:** building a cutout skeleton, setting pivot points with Skeleton tool, linking parent-child sections, placing hooks for animated levels, animating with Inverse Kinematics, pinning joints for walk cycles
- [Animating with the Plastic Tool](animation/animating-with-plastic-tool/guide.md) — Build and modify meshes and skeletons for mesh deformation animation
  - **Use when:** creating a Plastic mesh, building a Plastic skeleton, animating vertex poses with keyframes, painting mesh rigidity, setting vertex stacking order, linking vertices with expressions

### Effects and Rendering

- [Applying Special Effects](effects-and-rendering/applying-special-effects/guide.md) — Use the FX schematic, edit effect settings, create presets and macro FX
  - **Use when:** adding effects in FX Schematic, wiring effect nodes, editing FX Settings parameters, animating effect keyframes, saving effect presets, creating Macro FX
- [Using the Particles Effect](effects-and-rendering/using-the-particles-effect/guide.md) — Configure particle images, control images, birth parameters, and environment settings
  - **Use when:** adding particle effects for rain/snow/smoke, configuring particle birth rate and lifetime, connecting texture and control images to Particles node, setting gravity/wind/friction in Environment tab, animating particle opacity and size over lifespan, tinting particles with Colors tab spectrums
- [Previewing and Rendering](effects-and-rendering/previewing-and-rendering/guide.md) — Preview animations and render final output
  - **Use when:** previewing animation in Viewer or Flipbook, configuring Output Settings for render, rendering with transparent alpha background, using Sub-camera for faster preview, background rendering with Tasks pane, caching FX nodes for preview speed
- [Using the Toonz Farm](effects-and-rendering/using-the-toonz-farm/guide.md) — Install and configure distributed rendering across multiple machines
  - **Use when:** setting up Toonz Farm controller and server nodes, configuring FARMROOT shared folder, editing controller.txt and servers.txt, switching between Render Farm and Local processing, troubleshooting farm server "Down" status, configuring Windows service Log On credentials for network shares

### Scripting and Collaboration

- [ToonzScript](scripting-and-collaboration/toonzscript/guide.md) — Automate tasks using the script console with ToonzScript specifications and code examples
  - **Use when:** batch scripting in OpenToonz, running ToonzScript from console, automating vectorization with script, renumbering frames via script, rendering scenes programmatically, loading and saving levels in ToonzScript
- [Using Version Control](scripting-and-collaboration/using-version-control/guide.md) — Install and use the version control system for collaborative production
  - **Use when:** configuring SVN in versioncontrol.xml, locking files with Edit before modifying, putting and getting scene contents, retrieving past revisions by date, editing frame ranges for concurrent work, reading version control status icons


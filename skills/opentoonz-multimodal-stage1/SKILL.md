---
name: opentoonz-multimodal-stage1
description: "Practical with-screenshots guides for OpenToonz 1.7. Consult via the load_topic MCP tool — it returns the guide text and every figure in one atomic call."
---

# OpenToonz 1.7 Knowledge (multimodal-stage1)

## How to consult this skill

This skill exposes two MCP tools (already registered for you):

- **`load_topic(topic)`** — returns the chosen topic's `guide.md` AND every figure (PNG) in that topic folder as one tool response. **Use this instead of `Read` for any `*.md` or `figXX.png` inside this skill.**
- **`list_topics()`** — returns every topic path available, one per line.

Each entry in the TOC below has the form `[Title](<topic>/guide.md)`. The `<topic>` part (the path before `/guide.md`) is what you pass to `load_topic`.

> You will receive the guide text plus the relevant figures in a single tool result — no extra `Read` calls needed.

**Rules:**

1. Before any GUI action where you are unsure of the menu path / dialog / icon, find the matching topic in the TOC and call `load_topic` first.
2. You may call `load_topic` **at any step** of the trajectory, not only at the start. If the task moves into a new area, call `load_topic` again for the new area.
3. Do **not** issue separate `Read` calls for `figXX.png` files inside this skill — they are delivered by `load_topic` automatically.

## Guides

### Installation and Setup

- [Installing OpenToonz](installation-and-setup/installing-opentoonz/guide.md) — Download and install OpenToonz on Windows, macOS, Linux, or BSD
  - **Use when:** installing OpenToonz on Windows, installing OpenToonz on macOS, installing OpenToonz on Linux, bypassing SmartScreen unsigned installer warning, installing via Chocolatey/Homebrew/Flatpak/Snap, configuring OpenToonz stuff folder location
- [Configuring FFmpeg](installation-and-setup/configuring-ffmpeg/guide.md) — Install and configure FFmpeg for video format support
  - **Use when:** installing FFmpeg for OpenToonz, setting FFmpeg path in Preferences Import/Export, rendering mp4 webm gif output, clearing macOS Gatekeeper quarantine for FFmpeg, verifying FFmpeg in Output Settings format dropdown
- [Customizing the Interface](installation-and-setup/customizing-the-interface/guide.md) — Configure rooms, panes, and interface appearance
  - **Use when:** switching and managing workspace rooms, docking and resizing panes, customizing the Command Bar, changing interface language, switching or creating QSS themes, locking room pane layout
- [Managing Projects](installation-and-setup/managing-projects/guide.md) — Set up projectroot, create projects, configure default folders, and use the project browser
  - **Use when:** creating a new project, setting projectroot path, switching active projects, configuring default folder aliases, adding custom aliases in project_folders.txt, using $scenepath for per-scene subfolders
- [Setting Up a Scene](installation-and-setup/setting-up-a-scene/guide.md) — Configure camera, frame rate, working unit, color calibration, and memory settings
  - **Use when:** setting frame rate in Scene Settings, configuring camera resolution and aspect ratio, applying 3D LUT color calibration, changing working units to pixels or inches, adjusting undo memory size, saving scene defaults to project
- [Choosing a Production Workflow](installation-and-setup/choosing-a-production-workflow/guide.md) — Select between traditional (paper-based) and paperless animation workflows
  - **Use when:** scanning paper drawings into OpenToonz, setting up Render Farm, building reusable character libraries, compositing in Xsheet with Sub-Xsheets, choosing traditional vs paperless workflow, creating a Color Model for painting
- [Configuring Keyboard Shortcuts](installation-and-setup/configuring-keyboard-shortcuts/guide.md) — Customize and use predefined keyboard shortcuts
  - **Use when:** remapping keyboard shortcuts in Configure Shortcuts dialog, saving and loading shortcut presets, exporting shortcuts for backup or sharing, clearing all shortcut bindings, temporary tool switching with press-and-hold keys, default tool and navigation hotkey reference

### Scanning and Cleanup

- [Scanning Paper Drawings](scanning-and-cleanup/scanning-paper-drawings/guide.md) — Set up scanners, define animation levels, and scan drawings with autocentering
  - **Use when:** defining scanner driver (TWAIN/Internal), scanning paper drawings into Xsheet, setting scan mode (black and white/greyscale/color), preparing pegbar holes for autocentering, creating scan levels in Xsheet, configuring cropbox for scan area
- [Cleaning Up Scanned Drawings](scanning-and-cleanup/cleaning-up-scanned-drawings/guide.md) — Configure cleanup settings, preview results, and process scanned artwork
  - **Use when:** autocentering scanned drawings to pegbar holes, adjusting line processing sharpness and despeckling, setting cleanup camera resolution and field size, previewing cleanup with opacity check, batch cleanup via Tasks pane, saving CLN cleanup settings

### Drawing and Painting

- [Drawing Animation Levels](drawing-and-painting/drawing-animation-levels/guide.md) — Draw in OpenToonz using animation techniques, onion skin, and shift and trace
  - **Use when:** creating new animation levels in Xsheet, configuring Brush tool presets, vector inbetweening with interpolation curves, enabling Onion Skin relative and fixed modes, using Shift and Trace for light-table inbetweening, setting default level type in Preferences
- [Editing Animation Levels](drawing-and-painting/editing-animation-levels/guide.md) — Use the level strip, merge levels, process, save, and export animation levels
  - **Use when:** rearranging frames in Level Strip, renumbering and adding frames, merging animation levels, adjusting brightness/contrast/thickness, exporting levels to PNG/TGA/TIF, saving and reverting level edits
- [Managing Palettes and Styles](drawing-and-painting/managing-palettes-and-styles/guide.md) — Use the palette editor, studio palette, animate palettes, and edit styles
  - **Use when:** organizing styles across palette pages, linking styles to Studio Palette, animating palette colors with keyframes, applying textures to vector strokes, batch adjusting colors with Palette Gizmo, loading or merging Studio Palette into level palette
- [Painting Animation Levels](drawing-and-painting/painting-animation-levels/guide.md) — Fill areas, paint lines, and use color models with painting tools
  - **Use when:** filling areas and lines with the Fill tool, closing outline gaps with the Tape tool, frame range interpolation for batch painting, applying match lines between levels, loading a color model for reference, configuring Autopaint for Lines in Style Editor

### Xsheet and Timeline

- [Exposing and Managing Levels](xsheet-and-timeline/exposing-and-managing-levels/guide.md) — Expose levels in the Xsheet, edit level settings, and use the file browser
  - **Use when:** loading levels into Xsheet, exposing levels from Scene Cast, editing level settings (DPI/path/premultiply), replacing levels in cells, removing unused levels, using Level Strip to reorder frames
- [Working with Columns, Layers, and Cells](xsheet-and-timeline/working-with-columns-layers-and-cells/guide.md) — Manage columns/layers, edit cells, and work globally with frames
  - **Use when:** reordering Xsheet columns, retiming cells with Step/Each/Reverse, using Time Stretch dialog, toggling column Render/Lock/Camera Stand, inserting/removing global frames, extending sequences with Smart Fill Handle
- [Using Sub-Xsheets](xsheet-and-timeline/using-sub-xsheets/guide.md) — Create and manage sub-xsheets for scene organization
  - **Use when:** collapsing columns into Sub-Xsheet, loading TNZ scene as Sub-Xsheet, exploding Sub-Xsheet, cloning Sub-Xsheet, editing Sub-Xsheet in place, saving Sub-Xsheet as standalone scene
- [Creating Soundtracks and Lip Syncing](xsheet-and-timeline/soundtrack-and-lip-syncing/guide.md) — Add audio to the timeline and synchronize mouth shapes to dialogue
  - **Use when:** importing WAV/AIFF/MP3 audio clips, trimming and moving audio in Xsheet, scrubbing audio for sync, manual lip sync with Skeleton tool, Rhubarb auto lip sync, importing Papagayo DAT lip-sync data
- [Saving and Exporting Scenes](xsheet-and-timeline/saving-and-exporting-scenes/guide.md) — Save, load, import, and export scene files
  - **Use when:** saving TNZ scene files, configuring autosave interval, recovering scene backups, importing scenes between projects, exporting scenes to another project, collecting external assets

### Animation

- [Creating Movements](animation/creating-movements/guide.md) — Use the stage schematic to link and animate objects, work in 3D space
  - **Use when:** animating with keyframes and the Animate tool, linking objects in the Stage Schematic, creating motion paths for curved trajectories, using hooks to pin movement to drawing features, setting Z-axis depth and stacking order, configuring parent-child object hierarchies
- [Editing Curves and Expressions](animation/editing-curves-and-expressions/guide.md) — Use the function editor to define keyframes, interpolations, and mathematical expressions
  - **Use when:** adding keyframes in Function Editor, editing interpolation curves, writing expressions with variables, loading external DAT motion data, saving and loading CURVE files, activating animation cycles
- [Creating Cutout Animation](animation/creating-cutout-animation/guide.md) — Build skeletons, create models with hooks, and animate using inverse kinematics
  - **Use when:** building character skeleton rigs, setting pivot points for cutout pieces, linking parent-child sections with hooks, posing with Inverse Kinematics, animating rotation and translation with Skeleton tool, using Global Key for keyframes
- [Animating with the Plastic Tool](animation/animating-with-plastic-tool/guide.md) — Build and modify meshes and skeletons for mesh deformation animation
  - **Use when:** creating a Plastic mesh over artwork, building a skeleton with Build Skeleton mode, posing vertices across frames in Animate mode, painting rigid regions with Paint Rigid, setting vertex Stacking Order for overlapping limbs, driving vertices with Function Editor expressions

### Effects and Rendering

- [Applying Special Effects](effects-and-rendering/applying-special-effects/guide.md) — Use the FX schematic, edit effect settings, create presets and macro FX
  - **Use when:** adding effects in FX Schematic, connecting effect nodes to columns, editing effect parameters and keyframes, saving effect presets, creating and exploding Macro FX, managing multiple Output nodes
- [Using the Particles Effect](effects-and-rendering/using-the-particles-effect/guide.md) — Configure particle images, control images, birth parameters, and environment settings
  - **Use when:** configuring particle spawn area and birth rate, connecting texture and control images to Particles effect, setting gravity wind and friction forces, animating particle rotation and opacity fade, tinting particles with color spectrums, using built-in Particles presets
- [Previewing and Rendering](effects-and-rendering/previewing-and-rendering/guide.md) — Preview animations and render final output
  - **Use when:** previewing animation in the Viewer, configuring Preview Settings and Sub-camera, comparing frames in Flipbook, setting Output Settings for rendering, background rendering with Tasks pane, rendering with transparency for compositing
- [Using the Toonz Farm](effects-and-rendering/using-the-toonz-farm/guide.md) — Install and configure distributed rendering across multiple machines
  - **Use when:** configuring Toonz Farm controller and server nodes, editing FARMROOT config files, setting Windows service Log On account for network shares, connecting OpenToonz client to render farm, monitoring batch server status, troubleshooting farm log files

### Scripting and Collaboration

- [ToonzScript](scripting-and-collaboration/toonzscript/guide.md) — Automate tasks using the script console with ToonzScript specifications and code examples
  - **Use when:** batch vectorizing drawings, rendering scenes via script, running ToonzScript from console, automating xsheet frame operations, rasterizing vector levels, scripting image transforms and compositing
- [Using Version Control](scripting-and-collaboration/using-version-control/guide.md) — Install and use the version control system for collaborative production
  - **Use when:** configuring SVN repository in versioncontrol.xml, getting and putting files via right-click, locking files with Edit and Edit Frame Range, retrieving older revisions by date, reading version control status icons, enabling version control in Preferences


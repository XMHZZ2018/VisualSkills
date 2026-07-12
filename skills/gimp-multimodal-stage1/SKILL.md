---
name: gimp-multimodal-stage1
description: "Practical with-screenshots guides for GIMP 2.10. Consult via the load_topic MCP tool — it returns the guide text and every figure in one atomic call."
---

# GIMP 2.10 Knowledge (multimodal-stage1)

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

### File Management

- [Creating New Images](file-management/creating-new-images/guide.md) — Create new image files from scratch or from templates
  - **Use when:** creating a new blank image, setting canvas dimensions and units, choosing image templates, configuring bit depth and precision, setting fill and transparency options, adjusting print resolution
- [Opening Files](file-management/opening-files/guide.md) — Open images from disk, URLs, clipboard, drag-and-drop, or file manager
  - **Use when:** opening images via File Open dialog, opening image from URL, importing file as layers, drag-and-drop into GIMP, handling embedded color profiles on import, importing PDF pages at specific resolution
- [Saving and Exporting Images](file-management/saving-and-exporting/guide.md) — Save in native format or export to JPEG, PNG, GIF and other file formats
  - **Use when:** saving images as XCF, exporting to JPEG/PNG/GIF/TIFF/WebP, adjusting JPEG quality and subsampling, configuring PNG compression and interlacing, exporting GIF animations, overwriting imported files
- [Preparing Images for the Web](file-management/preparing-images-for-web/guide.md) — Optimize file size, quality ratio, and transparency for web use
  - **Use when:** exporting JPEG with quality slider, exporting PNG with transparency, flattening alpha channel before export, converting to Indexed mode for smaller PNG, choosing JPEG vs PNG for web, adding alpha channel for transparent PNG
- [Printing Images](file-management/printing-images/guide.md) — Set print size and print images
  - **Use when:** setting image print resolution, using Print Size dialog, positioning image on page for printing, choosing ppi for print quality, using File Print and Print Preview, adjusting print dimensions without resampling

### Selections

- [Basic Selection Tools](selections/basic-selection-tools/guide.md) — Use rectangle, ellipse, and free (lasso) selection tools
  - **Use when:** rectangle select tool, ellipse and circle selection, free select lasso tool, add subtract intersect selections, feather selection edges, stroke or fill a selection
- [Intelligent Selection Tools](selections/intelligent-selection-tools/guide.md) — Select by color, fuzzy select (magic wand), intelligent scissors, and foreground select
  - **Use when:** fuzzy select magic wand threshold, select by color across layers, intelligent scissors edge snapping, foreground select subject extraction, sample merged selection, feather edges antialiasing selection modes
- [Modifying Selections](selections/modifying-selections/guide.md) — Feather, shrink, grow, border, sharpen, invert, and distort selections
  - **Use when:** feathering selection edges, shrinking or growing selections, creating border selections, inverting selections, sharpening selection edges, distorting selection contours
- [Adding and Subtracting Selections](selections/combining-selections/guide.md) — Combine selections by adding, subtracting, or intersecting
  - **Use when:** combining multiple selections, adding to selection with Shift, subtracting from selection with Ctrl, intersecting selections, using Quick Mask for selection touch-ups, selection tool mode options
- [Using QuickMask](selections/quickmask/guide.md) — Paint selections using QuickMask mode
  - **Use when:** painting a selection with QuickMask, toggling QuickMask mode with Shift+Q, creating feathered edges with partial selections, saving QuickMask to channel, transferring selections between images via cut and paste
- [Converting Selections to Paths and Channels](selections/selection-to-path-and-channel/guide.md) — Save selections to channels, convert to/from paths
  - **Use when:** saving selection to channel, converting selection to path, reloading selection from channel, path to selection conversion, refining selection with path tool, Select to Path dialog options

### Painting and Drawing

- [Brush Tools](painting-and-drawing/brush-tools/guide.md) — Paint with pencil, paintbrush, airbrush, ink, and MyPaint brush tools
  - **Use when:** painting with pencil/paintbrush/airbrush/ink tools, configuring brush opacity and spacing, drawing straight lines with Shift-click, setting up pen tablet dynamics, installing MyPaint brushes, adjusting jitter and smooth stroke settings
- [Bucket Fill and Gradient](painting-and-drawing/fill-and-gradient/guide.md) — Fill areas with color, pattern, or gradient
  - **Use when:** bucket fill with color or pattern, fill by line art detection, adjusting fill threshold, creating gradients with shape presets, editing gradient stops on canvas, repeating gradient patterns
- [Erasing](painting-and-drawing/eraser/guide.md) — Erase pixels to background color or transparency
  - **Use when:** erasing to transparency, anti-erase to restore pixels, eraser tool options, hard edge erasing, picking background color with eraser, trimming floating selections
- [Clone, Heal, and Perspective Clone](painting-and-drawing/clone-and-heal/guide.md) — Clone from a source, heal blemishes, or clone with perspective correction
  - **Use when:** cloning pixels between image areas, removing blemishes with Heal tool, setting clone source point, perspective clone on receding surfaces, choosing clone alignment mode, cloning from a pattern
- [Blur, Sharpen, Smudge, Dodge, and Burn](painting-and-drawing/blur-sharpen-smudge-dodge-burn/guide.md) — Locally adjust sharpness, smudge paint, or dodge/burn exposure
  - **Use when:** blurring image details with brush, sharpening edges locally, smudging colors with smudge tool, dodging and burning tones, adjusting blur/sharpen rate and opacity, constraining smudge to straight lines
- [Managing and Creating Brushes](painting-and-drawing/managing-brushes/guide.md) — Add new brushes, create custom brushes, change brush size, and use animated brushes
  - **Use when:** installing custom brush files, creating brush from selection, exporting .gbr grayscale brush, configuring animated .gih brush options, resizing brushes with keyboard shortcuts, using the Brush Editor for parametric brushes
- [Drawing Simple Shapes and Lines](painting-and-drawing/drawing-shapes/guide.md) — Draw straight lines, rectangles, ellipses, and other basic shapes
  - **Use when:** drawing straight lines with Shift key, filling rectangle selections, stroking ellipse selections, constraining to perfect square or circle, setting stroke line width, rounded corners in Rectangle Select
- [Gradients, Patterns, and Palettes](painting-and-drawing/gradients-and-patterns/guide.md) — Use and manage gradients, patterns, and color palettes
  - **Use when:** filling selections with gradients, creating custom .ggr gradients, pattern fill with Bucket Fill tool, adding custom patterns to GIMP, importing palettes from images, editing indexed color palettes
- [Paint Dynamics](painting-and-drawing/paint-dynamics/guide.md) — Configure pressure sensitivity and other brush dynamics
  - **Use when:** selecting paint dynamics preset, creating custom paint dynamics, editing dynamics response curves, linking brush parameters to stylus inputs, configuring fade length and repeat options, using dynamics with drawing tablet
- [Symmetry Painting](painting-and-drawing/symmetry-painting/guide.md) — Paint with mirror, tiling, or radial symmetry
  - **Use when:** enabling symmetry painting mode, mirror strokes across axes, repositioning symmetry axis, creating tiling patterns with interval spacing, painting radial mandala effects, disabling brush transform for mirrored strokes

### Layers

- [Creating and Managing Layers](layers/creating-and-managing-layers/guide.md) — Create, duplicate, delete, reorder, and merge layers
  - **Use when:** creating new layers, duplicating and deleting layers, reordering layer stack, merging visible layers, flattening image before export, linking layers for grouped transforms
- [Layer Groups](layers/layer-groups/guide.md) — Organize layers into groups for complex compositions
  - **Use when:** creating layer groups, nesting and organizing layers into folders, applying pass-through blending mode to groups, adding layer masks to groups, hiding and collapsing layer groups, locating layers with Alt+Middle-click
- [Layer Masks](layers/layer-masks/guide.md) — Add, apply, edit, and delete layer masks for non-destructive editing
  - **Use when:** adding a layer mask, painting on layer mask to hide or reveal, initializing mask from selection or alpha channel, disabling or deleting layer mask, applying layer mask to alpha channel, converting mask to selection
- [Layer Blend Modes](layers/layer-modes/guide.md) — Apply blend modes (normal, lighten, darken, contrast, HSV, LCh) to control layer compositing
  - **Use when:** setting layer blend mode in Layers dialog, brightening with Screen or Dodge, darkening with Multiply or Burn, boosting contrast with Overlay or Soft Light, recoloring objects with HSV Hue mode, converting to grayscale with HSV Saturation
- [Layer Transparency and Alpha Channel](layers/layer-transparency/guide.md) — Add/remove alpha channel, color to alpha, alpha to selection
  - **Use when:** adding alpha channel to background layer, removing alpha channel, color to alpha for line art, alpha to selection, erasing to transparent, converting transparency to selection
- [Transforming Layers](layers/layer-transform/guide.md) — Flip, rotate, scale, offset, and resize individual layers
  - **Use when:** flipping layers horizontally or vertically, rotating layers 90° or 180°, arbitrary rotation angle, offsetting layer content for tileable patterns, resizing layer boundary size, scaling layer with interpolation

### Image Transforms

- [Scaling Images](transforms/scaling-images/guide.md) — Resize images for screen or print output
  - **Use when:** resizing image dimensions, Scale Image dialog, setting pixel width and height, choosing interpolation method, scaling a single layer, changing print resolution
- [Cropping Images](transforms/cropping/guide.md) — Crop images manually, to selection, or with zealous crop
  - **Use when:** cropping with fixed aspect ratio, crop to selection, autocrop to content, zealous crop interior strips, allow growing beyond canvas, auto shrink to contrast edge
- [Rotating and Flipping](transforms/rotating-and-flipping/guide.md) — Rotate images by fixed angles or arbitrary degrees, flip horizontally or vertically
  - **Use when:** rotating image 90° or 180°, arbitrary angle rotation with Rotate tool, straightening crooked photos with Corrective mode, flipping image horizontally or vertically, flipping along a guide axis, rotating a single layer
- [Perspective, Warp, and 3D Transform](transforms/perspective-and-warp/guide.md) — Apply perspective correction, warp deformations, cage transform, and 3D transforms
  - **Use when:** perspective transform with corner handles, 3D rotation with vanishing point, cage transform freeform warp, warp transform brush pushing pixels, creating warp animation GIF, unified transform combining rotate scale shear perspective
- [Changing Canvas Size](transforms/canvas-size/guide.md) — Resize the canvas, fit to layers or selection
  - **Use when:** resizing canvas dimensions, setting canvas offset and centering layers, fit canvas to layers or selection, resizing layers with canvas, filling new canvas area with transparency or color
- [Aligning and Moving](transforms/align-and-move/guide.md) — Align layers and move objects within the image
  - **Use when:** aligning layers to image or selection, distributing layers evenly, using Align Visible Layers dialog, moving layers with Move tool, nudging selections with arrow keys, snapping to guides and grids

### Color Adjustments

- [Levels and Curves](color-adjustments/levels-and-curves/guide.md) — Adjust tonal range with Levels or fine-tune with Curves
  - **Use when:** adjusting levels dialog black and white points, fixing color cast per channel, using curves for tonal correction, creating S-curve for contrast, color correcting with individual channel curves, setting output levels for print
- [Brightness, Contrast, and Exposure](color-adjustments/brightness-contrast-exposure/guide.md) — Adjust brightness, contrast, exposure, and shadows/highlights
  - **Use when:** adjusting brightness-contrast sliders, correcting exposure and black level, recovering shadows and highlights, editing brightness-contrast as levels, using split view preview, saving color correction presets
- [Hue, Saturation, and Color Balance](color-adjustments/hue-saturation-color-balance/guide.md) — Shift hue, adjust saturation, color temperature, and color balance
  - **Use when:** adjusting hue-saturation per color range, correcting color casts with Color Balance, fixing white balance with Color Temperature dialog, shifting hue chroma in LCh model, boosting global saturation scale
- [Automatic Color Correction](color-adjustments/auto-color-correction/guide.md) — Apply equalize, white balance, stretch contrast, and color enhance
  - **Use when:** auto color correction, equalize histogram, white balance stretch, stretch contrast, color enhance saturation boost, Colors Auto menu
- [Desaturate and Colorize](color-adjustments/desaturate-and-colorize/guide.md) — Convert to grayscale, apply sepia tone, or colorize an image
  - **Use when:** converting layer to grayscale with Desaturate dialog, applying sepia tone effect, tinting with Colors Colorize dialog, choosing desaturation mode (Luminance/Luma/Value), using Color to Gray for local contrast
- [Threshold, Posterize, and Dither](color-adjustments/threshold-posterize-dither/guide.md) — Reduce color depth with threshold, posterize, or dithering
  - **Use when:** converting image to black and white with Threshold, cleaning up scanned text, creating selection masks from channels, reducing colors with Posterize, applying Floyd-Steinberg or Bayer dithering, fixing color banding with Colors Dither dialog
- [Color Mapping](color-adjustments/color-mapping/guide.md) — Remap colors with gradient map, palette map, color rotation, and color exchange
  - **Use when:** applying gradient map to image, rotating hue ranges with Rotate Colors, replacing specific color with Color Exchange, colorizing grayscale with Sample Colorize, mapping luminosity to palette entries
- [Tone Mapping](color-adjustments/tone-mapping/guide.md) — Apply HDR tone mapping with Fattal, Mantiuk, Reinhard, Stress, or Retinex
  - **Use when:** tone mapping HDR images, Fattal et al 2002 filter settings, Mantiuk 2006 contrast compression, Reinhard 2005 brightness adjustment, Retinex underexposed shadow recovery, converting to 32-bit floating point for HDR
- [Channel Mixer and Components](color-adjustments/channel-operations/guide.md) — Mix channels, extract/compose/decompose color components
  - **Use when:** mixing RGB channels with Channel Mixer, extracting single color component as grayscale, decomposing image into color model channels, composing grayscale layers into color image, recomposing after channel editing, creating luminosity masks from channels
- [Inverting Colors](color-adjustments/invert-colors/guide.md) — Invert image colors (perceptual, linear, or value invert)
  - **Use when:** inverting colors to photographic negative, using Colors > Invert, linear invert for compositing, Value Invert for luminosity only, reversing brightness without changing hue
- [Image Mode and Precision](color-adjustments/image-mode-and-precision/guide.md) — Convert between RGB, grayscale, and indexed modes; change bit depth/precision
  - **Use when:** switching image color mode to RGB/Grayscale/Indexed, converting to indexed palette with dithering, changing bit depth via Image Precision dialog, choosing linear light vs perceptual gamma encoding, fixing grayed-out filters by changing mode, reducing bit depth with dithering options

### Text

- [Creating and Editing Text](text/creating-and-editing-text/guide.md) — Use the text tool to create and manage text layers
  - **Use when:** adding text to canvas, changing font and text formatting, text along a path, converting text to path, vertical text orientation, dynamic vs fixed text box
- [Adding and Managing Fonts](text/adding-fonts/guide.md) — Install new fonts and troubleshoot font issues
  - **Use when:** installing fonts for GIMP on Linux/Windows/macOS, refreshing font list without restarting, using the Fonts dockable dialog, setting custom font search paths in Preferences, troubleshooting font-related crashes on startup
- [Text Along a Path](text/text-along-path/guide.md) — Place text along a vector path for curved text effects
  - **Use when:** curving text along a path, stroking text-shaped path, creating vector text outlines, flipping reversed text on path, transforming text path with perspective or rotate, neon glow text effect with gradient map

### Paths

- [Creating and Editing Paths](paths/creating-and-editing-paths/guide.md) — Draw and manipulate vector paths with the Paths tool
  - **Use when:** drawing Bézier curves with Paths tool, converting path to selection, stroking or filling a path, editing anchor points and handles, transforming paths with Scale/Rotate, managing paths in Paths dialog
- [Stroking and Filling Paths](paths/stroking-and-filling-paths/guide.md) — Stroke a path with a brush or fill a path with color/pattern
  - **Use when:** stroking a path with paint tools, filling a path with color or pattern, setting dash pattern and line style, choosing cap and join style, using Edit > Stroke Path dialog, emulating brush dynamics on paths
- [Converting Between Paths and Selections](paths/paths-and-selections/guide.md) — Convert paths to selections and selections to paths
  - **Use when:** convert selection to path, path to selection, Select to Path menu, Shift+V from path, refine selection with Bézier curves, Paths dialog buttons
- [Importing and Exporting SVG Paths](paths/paths-and-svg/guide.md) — Exchange vector paths with SVG files
  - **Use when:** exporting paths to SVG from Paths dialog, importing SVG paths into GIMP, converting SVG shapes to GIMP paths, transferring paths between GIMP and Inkscape, using Import Path and Export Path commands

### Color Management

- [Setting Up a Color-Managed Workflow](color-management/color-managed-workflow/guide.md) — Configure GIMP for consistent color across devices using ICC profiles
  - **Use when:** setting RGB working space in Color Management preferences, assigning monitor ICC profile, converting embedded color profiles on image open, assigning color profile to untagged images, enabling soft proofing for print
- [Assigning and Converting Color Profiles](color-management/assigning-and-converting-profiles/guide.md) — Assign, convert, discard, or save ICC color profiles
  - **Use when:** assigning ICC color profile, converting color space for print, discarding embedded profile, saving ICC profile to disk, choosing rendering intent, using Image Color Management menu

### Photo Enhancement

- [Improving Photo Composition](photo-enhancement/improving-composition/guide.md) — Crop, straighten, and reframe photographs for better composition
  - **Use when:** straightening a tilted horizon with Rotate tool, corrective rotation mode, cropping with rule of thirds, removing empty corners after rotation, Crop tool Delete cropped pixels option
- [Removing Unwanted Objects](photo-enhancement/removing-objects/guide.md) — Remove blemishes, objects, or backgrounds from photographs
  - **Use when:** removing dust spots with Despeckle filter, cloning out unwanted objects with Clone tool, healing skin blemishes with Heal tool, removing background with Foreground Select, red eye removal filter
- [Adjusting Sharpness](photo-enhancement/adjusting-sharpness/guide.md) — Sharpen or reduce noise in photographs
  - **Use when:** sharpening with Unsharp Mask filter, reducing grain with Selective Gaussian Blur, softening overly crisp images, sharpening without color fringing via HSV decompose, using Blur/Sharpen tool for selective sharpening, removing noise with Despeckle filter

### Customization and Configuration

- [Configuring Preferences](customization/preferences/guide.md) — Set system resources, interface, display, input devices, and folder preferences
  - **Use when:** setting tile cache and undo levels, configuring keyboard shortcuts, calibrating monitor resolution, setting up drawing tablet input devices, managing brush and pattern folder paths, adjusting GIMP system resources
- [Creating Keyboard Shortcuts](customization/keyboard-shortcuts/guide.md) — Customize and create keyboard shortcuts for menu commands
  - **Use when:** assigning dynamic keyboard shortcuts, enabling Use dynamic keyboard shortcuts in Preferences, using Edit Keyboard Shortcuts dialog, reassigning conflicting shortcuts, removing a shortcut with Backspace, saving keyboard shortcuts on exit
- [Using Grids and Guides](customization/grids-and-guides/guide.md) — Configure and display grids, create guides, and use snapping
  - **Use when:** configuring grid style and spacing, snapping to grid, creating and positioning guides, removing guides, slicing image using guides, rendering permanent grid lines
- [Tool Presets](customization/tool-presets/guide.md) — Save and manage tool option presets for quick access
  - **Use when:** saving tool presets, restoring tool configurations, organizing presets with tags, editing tool preset resources, managing .gtp preset files, refreshing presets folder
- [Setting Tile Cache for Performance](customization/tile-cache/guide.md) — Configure memory tile cache to optimize GIMP performance
  - **Use when:** setting tile cache size, configuring GIMP system resources preferences, choosing swap folder location, optimizing GIMP memory usage, adjusting RAM allocation for GIMP

### Scripting and Plugins

- [Installing and Using Plugins](scripting-and-plugins/installing-plugins/guide.md) — Find, install, and use GIMP plugins
  - **Use when:** installing GIMP plugins on Linux with gimptool, installing plugins on Windows, finding the plug-ins folder in Preferences, locating installed plugins via command search, troubleshooting plugin crashes
- [Using Script-Fu Scripts](scripting-and-plugins/using-script-fu/guide.md) — Install and run Script-Fu scripts in GIMP
  - **Use when:** installing .scm scripts in GIMP, refreshing Script-Fu scripts, finding script folders in Preferences, locating scripts in Filters menu, troubleshooting Script-Fu dialogs, installing gimp-data-extras standalone scripts
- [Writing Script-Fu Scripts](scripting-and-plugins/writing-script-fu/guide.md) — Learn Scheme basics and write custom Script-Fu automation scripts
  - **Use when:** writing .scm scripts for GIMP, using the Script-Fu Console, registering scripts with script-fu-register, placing scripts in GIMP menus, discovering PDB functions via Procedure Browser, creating Script-Fu dialogs with parameter types
- [Using Python-Fu](scripting-and-plugins/python-fu/guide.md) — Access the Python-Fu console and run Python scripts
  - **Use when:** opening Python-Fu console, browsing PDB procedures, running interactive Python commands in GIMP, saving console session, converting PDB constant names to Python syntax, automating GIMP tasks with scripts

### Troubleshooting

- [Tools Not Working as Expected](troubleshooting/tools-not-working/guide.md) — Fix non-responsive brushes, eraser, move tool, and other tool issues
  - **Use when:** fixing floating selection blocking tools, brush or eraser paints nothing, transform tool has no effect, eraser paints background color instead of transparency, brush paints wrong colors on layer mask, crop tool leaves empty space around image
- [Selection and Layer Issues](troubleshooting/selection-and-layer-issues/guide.md) — Fix floating selection, hidden selection, invisible layers, acting outside selection/layer
  - **Use when:** anchoring floating selections, clearing hidden selections, painting outside layer boundary, activating invisible layers, inverting selections with Quick Mask, fixing "cannot paint on layer groups" error
- [Fixing Missing Windows and Dialogs](troubleshooting/missing-windows-and-dialogs/guide.md) — Restore missing toolbox, tool options, tool icons, or image toolbar
  - **Use when:** restoring hidden docks with TAB, recovering Tool Options dialog, finding grouped tool icons in Toolbox, showing image tab bar in single-window mode, locking tabs to dock, toggling Hide Docks
- [Fixing Export Problems](troubleshooting/export-problems/guide.md) — Fix transparency loss in JPEG and color changes in GIF exports
  - **Use when:** fixing JPEG transparency loss, flattening image before export, exporting as PNG instead of JPEG, fixing GIF color shift, converting to indexed mode, choosing dithering for GIF export


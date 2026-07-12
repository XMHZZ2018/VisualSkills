---
name: gimp-text-stage1
description: "Practical text-only guides for GIMP 2.10. Consult via the load_topic MCP tool — it returns the guide text in one atomic call."
---

# GIMP 2.10 Knowledge (text-stage1)

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

### File Management

- [Creating New Images](file-management/creating-new-images/guide.md) — Create new image files from scratch or from templates
  - **Use when:** creating a new blank canvas, setting image dimensions and units, choosing color space and bit depth, setting canvas resolution for print, filling background with transparency, saving custom image templates
- [Opening Files](file-management/opening-files/guide.md) — Open images from disk, URLs, clipboard, drag-and-drop, or file manager
  - **Use when:** opening images via File Open dialog, opening files from a URL, importing as layers, drag-and-drop into canvas, selecting file type manually for unrecognized formats, opening PDF pages at specific resolution, handling embedded color profiles on open
- [Saving and Exporting Images](file-management/saving-and-exporting/guide.md) — Save in native format or export to JPEG, PNG, GIF and other file formats
  - **Use when:** saving as XCF, exporting to JPEG/PNG/GIF, JPEG quality slider settings, PNG transparency export, GIF animation loop settings, File Export As dialog, overwriting original image file
- [Preparing Images for the Web](file-management/preparing-images-for-web/guide.md) — Optimize file size, quality ratio, and transparency for web use
  - **Use when:** exporting as JPEG or PNG for web, setting JPEG quality slider, converting to indexed color mode, flattening alpha channel, adding transparency for PNG, using File Export As dialog
- [Printing Images](file-management/printing-images/guide.md) — Set print size and print images
  - **Use when:** setting print size, adjusting print resolution, using Print Size dialog, configuring page setup, centering image on page, print preview

### Selections

- [Basic Selection Tools](selections/basic-selection-tools/guide.md) — Use rectangle, ellipse, and free (lasso) selection tools
  - **Use when:** rectangle select tool, ellipse select tool, free select lasso tool, adding and subtracting selections, feathering selection edges, constraining selection aspect ratio
- [Intelligent Selection Tools](selections/intelligent-selection-tools/guide.md) — Select by color, fuzzy select (magic wand), intelligent scissors, and foreground select
  - **Use when:** selecting similar colors with Magic Wand, selecting scattered color with Select By Color, snapping selection to edges with Intelligent Scissors, extracting foreground from background, adjusting selection threshold by dragging, converting Intelligent Scissors path to selection
- [Modifying Selections](selections/modifying-selections/guide.md) — Feather, shrink, grow, border, sharpen, invert, and distort selections
  - **Use when:** feathering selection edges, sharpening selections, shrinking or growing selections, creating border selections, inverting selections, distorting selection contours
- [Adding and Subtracting Selections](selections/combining-selections/guide.md) — Combine selections by adding, subtracting, or intersecting
  - **Use when:** combining selections with Shift/Ctrl modifiers, adding to selection, subtracting from selection, intersecting selections, building irregular selections from simple shapes, using Quick Mask for selection touch-ups
- [Using QuickMask](selections/quickmask/guide.md) — Paint selections using QuickMask mode
  - **Use when:** painting a selection with QuickMask, toggling QuickMask mode, creating feathered edges with gray values, saving QuickMask to channel, transferring selections between images
- [Converting Selections to Paths and Channels](selections/selection-to-path-and-channel/guide.md) — Save selections to channels, convert to/from paths
  - **Use when:** saving selection to channel, converting selection to path, reloading selection from channel, editing selection as vector path, converting path to selection, Select > To Path dialog

### Painting and Drawing

- [Brush Tools](painting-and-drawing/brush-tools/guide.md) — Paint with pencil, paintbrush, airbrush, ink, and MyPaint brush tools
  - **Use when:** painting pixel art with Pencil tool, adjusting airbrush rate and flow, installing MyPaint brushes, constraining brush strokes to straight lines, stroking selections or paths with paint tools, configuring brush dynamics and jitter
- [Bucket Fill and Gradient](painting-and-drawing/fill-and-gradient/guide.md) — Fill areas with color, pattern, or gradient
  - **Use when:** filling area with color or pattern, adjusting bucket fill threshold, filling line art with gap detection, applying gradient with shape options, editing gradient stops on canvas, repeating gradient stripe effects
- [Erasing](painting-and-drawing/eraser/guide.md) — Erase pixels to background color or transparency
  - **Use when:** erasing to transparency, erasing to background color, anti erase restoring pixels, hard edge pixel-perfect erase, tablet stylus eraser assignment, erasing floating selection shape
- [Clone, Heal, and Perspective Clone](painting-and-drawing/clone-and-heal/guide.md) — Clone from a source, heal blemishes, or clone with perspective correction
  - **Use when:** cloning pixels from a source area, healing blemishes and wrinkles, perspective cloning on vanishing-point surfaces, setting clone source alignment, using sample merged for non-destructive cloning, painting with a pattern fill
- [Blur, Sharpen, Smudge, Dodge, and Burn](painting-and-drawing/blur-sharpen-smudge-dodge-burn/guide.md) — Locally adjust sharpness, smudge paint, or dodge/burn exposure
  - **Use when:** blurring image areas with brush, sharpening local contrast, smudging colors like wet paint, dodging to lighten tones, burning to darken tones, adjusting Rate and Exposure sliders
- [Managing and Creating Brushes](painting-and-drawing/managing-brushes/guide.md) — Add new brushes, create custom brushes, change brush size, and use animated brushes
  - **Use when:** installing custom brush files, creating brushes from clipboard, making grayscale or color .gbr brushes, changing brush size with keyboard shortcuts, creating animated .gih brushes, adjusting brush spacing
- [Drawing Simple Shapes and Lines](painting-and-drawing/drawing-shapes/guide.md) — Draw straight lines, rectangles, ellipses, and other basic shapes
  - **Use when:** drawing straight lines with Shift-click, filling rectangle and ellipse selections, stroking selection outlines via Edit menu, constraining selections to perfect squares or circles, chaining connected line segments with brush tools
- [Gradients, Patterns, and Palettes](painting-and-drawing/gradients-and-patterns/guide.md) — Use and manage gradients, patterns, and color palettes
  - **Use when:** applying gradient tool to selection, painting with gradient dynamics, using Gradient Map filter, filling with patterns via Bucket Fill, creating custom gradients in Gradient Editor, importing palettes from images
- [Paint Dynamics](painting-and-drawing/paint-dynamics/guide.md) — Configure pressure sensitivity and other brush dynamics
  - **Use when:** selecting paint dynamics preset, editing dynamics matrix parameters, mapping brush size to pressure or velocity, configuring fade distance and repeat mode, creating custom paint dynamics, using gradient color in brush strokes
- [Symmetry Painting](painting-and-drawing/symmetry-painting/guide.md) — Paint with mirror, tiling, or radial symmetry
  - **Use when:** enabling symmetry painting mode, mirror painting across axis, repositioning symmetry axis, creating tiled seamless patterns, configuring mandala radial strokes, setting tiling interval and shift

### Layers

- [Creating and Managing Layers](layers/creating-and-managing-layers/guide.md) — Create, duplicate, delete, reorder, and merge layers
  - **Use when:** creating new layers, duplicating layers, reordering layer stack, anchoring floating selections, merging visible layers, flattening image for export
- [Layer Groups](layers/layer-groups/guide.md) — Organize layers into groups for complex compositions
  - **Use when:** creating layer groups, nesting groups inside groups, adding layers to a group, setting group opacity and visibility, using Pass Through blend mode, applying masks to layer groups
- [Layer Masks](layers/layer-masks/guide.md) — Add, apply, edit, and delete layer masks for non-destructive editing
  - **Use when:** adding a layer mask, editing layer mask with paint tools, disabling or previewing layer mask, applying layer mask to alpha channel, converting mask to selection, initializing mask from selection or channel
- [Layer Blend Modes](layers/layer-modes/guide.md) — Apply blend modes (normal, lighten, darken, contrast, HSV, LCh) to control layer compositing
  - **Use when:** setting layer blend mode in Layers dialog, brightening with Screen or Dodge, darkening with Multiply or Burn, boosting midtone contrast with Overlay or Soft Light, aligning layers using Difference mode, recoloring with HSV Hue blend mode
- [Layer Transparency and Alpha Channel](layers/layer-transparency/guide.md) — Add/remove alpha channel, color to alpha, alpha to selection
  - **Use when:** adding alpha channel to layer, removing alpha channel, color to alpha background removal, alpha to selection, combining alpha selection with existing selection, making layer transparent
- [Transforming Layers](layers/layer-transform/guide.md) — Flip, rotate, scale, offset, and resize individual layers
  - **Use when:** flipping layers horizontally or vertically, rotating layers by fixed or arbitrary angle, offsetting layer content for tileable patterns, resizing layer boundary size, scaling layer with interpolation

### Image Transforms

- [Scaling Images](transforms/scaling-images/guide.md) — Resize images for screen or print output
  - **Use when:** resizing image pixel dimensions, using Scale Image dialog, setting print resolution, choosing interpolation method, scaling a single layer with Scale Tool, sharpening after upscaling
- [Cropping Images](transforms/cropping/guide.md) — Crop images manually, to selection, or with zealous crop
  - **Use when:** cropping with the Crop Tool, setting fixed aspect ratio, crop to selection, crop to content, zealous crop, auto shrink crop rectangle
- [Rotating and Flipping](transforms/rotating-and-flipping/guide.md) — Rotate images by fixed angles or arbitrary degrees, flip horizontally or vertically
  - **Use when:** rotate image 90 or 180 degrees, arbitrary angle rotation with Rotate tool, straighten crooked photo with corrective rotation, flip image horizontally or vertically, flip layer along a guide axis
- [Perspective, Warp, and 3D Transform](transforms/perspective-and-warp/guide.md) — Apply perspective correction, warp deformations, cage transform, and 3D transforms
  - **Use when:** correcting perspective distortion in photos, warping pixels with brush strokes, rotating layers in 3D with vanishing point, using unified transform handles, deforming regions with cage transform, animating warp transform as GIF
- [Changing Canvas Size](transforms/canvas-size/guide.md) — Resize the canvas, fit to layers or selection
  - **Use when:** changing canvas size, setting canvas offset, resizing layers with canvas, fit canvas to layers, fit canvas to selection, Image Canvas Size dialog
- [Aligning and Moving](transforms/align-and-move/guide.md) — Align layers and move objects within the image
  - **Use when:** aligning layers to image or selection, distributing layers evenly, align visible layers dialog, moving layers with Move tool, nudging selections with arrow keys, linking layers to move together

### Color Adjustments

- [Levels and Curves](color-adjustments/levels-and-curves/guide.md) — Adjust tonal range with Levels or fine-tune with Curves
  - **Use when:** adjusting input/output levels, using Curves dialog, setting black and white points, creating S-curve contrast, correcting underexposed photos, per-channel color correction
- [Brightness, Contrast, and Exposure](color-adjustments/brightness-contrast-exposure/guide.md) — Adjust brightness, contrast, exposure, and shadows/highlights
  - **Use when:** adjusting brightness and contrast sliders, using Colors Exposure dialog, recovering shadows and highlights, drag-on-canvas brightness shortcut, editing settings as Levels, compressing tonal range with Shadows-Highlights
- [Hue, Saturation, and Color Balance](color-adjustments/hue-saturation-color-balance/guide.md) — Shift hue, adjust saturation, color temperature, and color balance
  - **Use when:** shifting hue with Hue-Saturation dialog, adjusting saturation and lightness per color channel, fixing color casts with Color Balance, correcting white balance with Color Temperature, using Hue-Chroma for perceptual color adjustment
- [Automatic Color Correction](color-adjustments/auto-color-correction/guide.md) — Apply equalize, white balance, stretch contrast, and color enhance
  - **Use when:** equalizing histogram, auto white balance, stretching contrast, boosting color saturation, automatic color correction, Colors Auto menu
- [Desaturate and Colorize](color-adjustments/desaturate-and-colorize/guide.md) — Convert to grayscale, apply sepia tone, or colorize an image
  - **Use when:** converting image to grayscale, desaturate modes luminance luma lightness, Color to Gray local contrast, applying sepia tone effect, colorize with hue saturation lightness, single-hue toning cyanotype
- [Threshold, Posterize, and Dither](color-adjustments/threshold-posterize-dither/guide.md) — Reduce color depth with threshold, posterize, or dithering
  - **Use when:** converting image to black and white with Threshold, cleaning up scanned text, reducing color levels with Posterize, choosing a dithering method, creating pop-art flat-color effect, preserving smooth gradients with fewer colors
- [Color Mapping](color-adjustments/color-mapping/guide.md) — Remap colors with gradient map, palette map, color rotation, and color exchange
  - **Use when:** applying gradient map to image, remapping colors with palette map, rotating hue ranges with Color Rotation, replacing specific color with Color Exchange, colorizing grayscale with Sample Colorize
- [Tone Mapping](color-adjustments/tone-mapping/guide.md) — Apply HDR tone mapping with Fattal, Mantiuk, Reinhard, Stress, or Retinex
  - **Use when:** tone mapping HDR images, Fattal gradient detail recovery, Mantiuk contrast compression, Reinhard brightness adaptation, Retinex shadow detail enhancement, converting to 32-bit linear light for HDR
- [Channel Mixer and Components](color-adjustments/channel-operations/guide.md) — Mix channels, extract/compose/decompose color components
  - **Use when:** mixing RGB channel levels, extracting single channel as grayscale, decomposing image into color model layers, composing grayscale layers into color image, recomposing edited channels, converting between RGB HSV LAB CMYK color spaces
- [Inverting Colors](color-adjustments/invert-colors/guide.md) — Invert image colors (perceptual, linear, or value invert)
  - **Use when:** inverting colors, linear invert for compositing, value invert preserving hue, Colors menu invert operations, flipping luminosity without changing hue
- [Image Mode and Precision](color-adjustments/image-mode-and-precision/guide.md) — Convert between RGB, grayscale, and indexed modes; change bit depth/precision
  - **Use when:** converting image to RGB/Grayscale/Indexed mode, changing bit depth via Image Precision, reducing colors for GIF with indexed palette, choosing dithering options for mode conversion, selecting linear light vs perceptual gamma encoding

### Text

- [Creating and Editing Text](text/creating-and-editing-text/guide.md) — Use the text tool to create and manage text layers
  - **Use when:** adding text to canvas, changing font and size of selected text, text along a path, converting text to path or selection, setting text box dynamic vs fixed mode, adjusting kerning and baseline
- [Adding and Managing Fonts](text/adding-fonts/guide.md) — Install new fonts and troubleshoot font issues
  - **Use when:** installing fonts on Linux/Windows/macOS, adding custom font directories in Preferences, refreshing fonts without restarting GIMP, fixing font-related startup crashes, using --no-fonts flag, configuring GIMP font search path
- [Text Along a Path](text/text-along-path/guide.md) — Place text along a vector path for curved text effects
  - **Use when:** placing text along a path, bending text to follow a curve, converting text path to selection, stroking text path with brush, adjusting letter spacing on curves, filling curved text outlines

### Paths

- [Creating and Editing Paths](paths/creating-and-editing-paths/guide.md) — Draw and manipulate vector paths with the Paths tool
  - **Use when:** drawing Bézier paths, converting paths to selections, stroking and filling paths, editing path anchor points and handles, managing paths in Paths dialog, transforming paths with Scale/Rotate/Perspective
- [Stroking and Filling Paths](paths/stroking-and-filling-paths/guide.md) — Stroke a path with a brush or fill a path with color/pattern
  - **Use when:** stroking a path with paint tools, filling a path with color or pattern, setting dash patterns and line styles, choosing cap and join styles, using Edit Stroke Path dialog, filling enclosed path areas
- [Converting Between Paths and Selections](paths/paths-and-selections/guide.md) — Convert paths to selections and selections to paths
  - **Use when:** converting selection to path, converting path to selection, Select to Path command, Path to Selection button, refining selections with Bézier curves, Shift+V path to selection shortcut
- [Importing and Exporting SVG Paths](paths/paths-and-svg/guide.md) — Exchange vector paths with SVG files
  - **Use when:** exporting paths as SVG, importing SVG paths into Paths dialog, converting SVG shapes to editable paths, opening SVG as rasterized image, round-trip workflow with Inkscape

### Color Management

- [Setting Up a Color-Managed Workflow](color-management/color-managed-workflow/guide.md) — Configure GIMP for consistent color across devices using ICC profiles
  - **Use when:** assigning ICC monitor profile, converting embedded color profiles on open, soft proofing for print, configuring Color Management preferences, assigning or converting image profiles via Image menu
- [Assigning and Converting Color Profiles](color-management/assigning-and-converting-profiles/guide.md) — Assign, convert, discard, or save ICC color profiles
  - **Use when:** assigning ICC color profile, converting to color profile, choosing rendering intent, discarding embedded profile, saving ICC profile to disk, Image Color Management menu

### Photo Enhancement

- [Improving Photo Composition](photo-enhancement/improving-composition/guide.md) — Crop, straighten, and reframe photographs for better composition
  - **Use when:** straightening a tilted photo with Rotate tool, using Backward Corrective transform direction, cropping empty corners after rotation, composing with rule of thirds, avoiding rotation blur with single-pass correction
- [Removing Unwanted Objects](photo-enhancement/removing-objects/guide.md) — Remove blemishes, objects, or backgrounds from photographs
  - **Use when:** removing sensor dust with Despeckle filter, cloning out unwanted objects, healing skin blemishes, removing backgrounds with Foreground Select, content-aware fill with Resynthesizer plug-in
- [Adjusting Sharpness](photo-enhancement/adjusting-sharpness/guide.md) — Sharpen or reduce noise in photographs
  - **Use when:** sharpening photos with Unsharp Mask, reducing color fringing via HSV decompose, using Blur/Sharpen tool for selective sharpening, reducing noise with Selective Gaussian Blur, removing grain with Despeckle filter, softening images with Blur filter

### Customization and Configuration

- [Configuring Preferences](customization/preferences/guide.md) — Set system resources, interface, display, input devices, and folder preferences
  - **Use when:** setting tile cache and memory allocation, configuring keyboard shortcuts, calibrating monitor resolution, mapping tablet input devices, changing swap and temp folder paths, adding custom brush and pattern folders
- [Creating Keyboard Shortcuts](customization/keyboard-shortcuts/guide.md) — Customize and create keyboard shortcuts for menu commands
  - **Use when:** assigning dynamic keyboard shortcuts, enabling save keyboard shortcuts on exit, using Keyboard Shortcuts dialog, rebinding tool and filter shortcuts, removing existing shortcuts, resolving shortcut conflicts
- [Using Grids and Guides](customization/grids-and-guides/guide.md) — Configure and display grids, create guides, and use snapping
  - **Use when:** showing and configuring the image grid, snapping to grid lines, creating and positioning guides, removing all guides, snap to guides for alignment, rendering a grid with the Grid filter
- [Tool Presets](customization/tool-presets/guide.md) — Save and manage tool option presets for quick access
  - **Use when:** saving tool presets, restoring tool configurations, organizing presets with tags, editing tool preset settings, sharing .gtp preset files, managing Tool Presets dialog
- [Setting Tile Cache for Performance](customization/tile-cache/guide.md) — Configure memory tile cache to optimize GIMP performance
  - **Use when:** setting tile cache size, adjusting GIMP memory usage, configuring System Resources preferences, optimizing GIMP performance with RAM, changing swap directory location, Edit Preferences Folders swap disk

### Scripting and Plugins

- [Installing and Using Plugins](scripting-and-plugins/installing-plugins/guide.md) — Find, install, and use GIMP plugins
  - **Use when:** installing GIMP plugins, setting plugin search paths in Preferences, compiling plugins with gimptool, finding plugins via command search, troubleshooting plugin crashes
- [Using Script-Fu Scripts](scripting-and-plugins/using-script-fu/guide.md) — Install and run Script-Fu scripts in GIMP
  - **Use when:** installing .scm Script-Fu files, refreshing scripts without restarting GIMP, configuring script folder paths in Preferences, finding installed scripts in menus, troubleshooting scripts that appear to do nothing, retrieving removed standalone scripts from gimp-data-extras
- [Writing Script-Fu Scripts](scripting-and-plugins/writing-script-fu/guide.md) — Learn Scheme basics and write custom Script-Fu automation scripts
  - **Use when:** writing Script-Fu scripts in GIMP, registering script menu entries with script-fu-register, using Script-Fu Console for testing, declaring variables and functions in TinyScheme, calling GIMP procedures from scripts, installing .scm script files
- [Using Python-Fu](scripting-and-plugins/python-fu/guide.md) — Access the Python-Fu console and run Python scripts
  - **Use when:** opening Python-Fu console, browsing PDB procedures, running interactive Python scripts in GIMP, saving console session output, converting PDB constants to Python syntax, calling gimp object-oriented API

### Troubleshooting

- [Tools Not Working as Expected](troubleshooting/tools-not-working/guide.md) — Fix non-responsive brushes, eraser, move tool, and other tool issues
  - **Use when:** anchoring floating selection to unlock tools, brush or eraser not painting visibly, eraser shows white instead of transparency, adding alpha channel to layer, move or transform tool not responding, crop tool leaving empty canvas
- [Selection and Layer Issues](troubleshooting/selection-and-layer-issues/guide.md) — Fix floating selection, hidden selection, invisible layers, acting outside selection/layer
  - **Use when:** anchoring floating selections, showing hidden selection marching ants, painting outside selection or layer boundary, activating correct layer, using Quick Mask to visualize selection, resizing layer to canvas with Layer to Image Size
- [Fixing Missing Windows and Dialogs](troubleshooting/missing-windows-and-dialogs/guide.md) — Restore missing toolbox, tool options, tool icons, or image toolbar
  - **Use when:** restoring vanished docks with Tab key, recovering missing Tool Options dialog, finding grouped tool icons in Toolbox, showing image tab bar in single-window mode, toggling dock visibility via Windows menu
- [Fixing Export Problems](troubleshooting/export-problems/guide.md) — Fix transparency loss in JPEG and color changes in GIF exports
  - **Use when:** JPEG export loses transparency, GIF color banding fix, exporting with alpha channel, converting to indexed mode, File Export As format selection, GIF palette and dithering settings


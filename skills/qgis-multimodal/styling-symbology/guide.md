No `guide.md` yet. Here is the guide:

---

## Style Manager, Symbol Selector & Label Settings for cartographic styling of layers in QGIS 3.44.

---

## Style Manager

The Style Manager is a modeless dialog that stores and organizes all reusable style items — symbols, color ramps, text formats, and label settings — in a shared database tied to your user profile.

### Opening the Style Manager

Three entry points:

- **Settings > Style Manager…** from the main menu
- The Style Manager toolbar button in the **Project toolbar** (Read the screenshot `fig03.png` in this directory — it shows the Style Manager toolbar button icon)
- The Style Manager button inside **Layer Properties** while configuring a symbol or text format (Read the screenshot `fig04.png` in this directory — it shows the same icon as it appears inside a properties dialog)

### Layout of the Dialog

Read the screenshot `fig10.png` in this directory — it shows the full Style Manager dialog with the left-side category panel, tab bar across the top, and the central symbol preview grid.

Key UI areas:

- **Top-left dropdown**: choose the style database — `Default` (shared across all projects) or `Project Styles` (project-scoped only)
- **Left panel**: categories — `Favorites`, `All`, `Tags`, and `Smart Groups`
- **Tab bar across the top**: filters the central grid by type: `All`, `Marker`, `Line`, `Fill`, `Color Ramp`, `Text Format`, `Label Settings`, `Legend Patch Shapes`, `3D Symbols`
- **Bottom toolbar**: Add item (Read the screenshot `fig05.png` in this directory — it shows the green + add button), Remove item, Edit item, and Import/Export
- **Bottom-right**: toggle between Icon View and List View; thumbnail size slider

### Organizing Items

- **Tags**: right-click any item > **Add to Tag** to assign it. Tags are manual.
- **Smart Groups**: click **Add Smart Group…** to define filter conditions (name contains string, has a tag, etc.). Items matching the condition are added automatically.
- To edit a smart group: select it > **Modify group… > Edit smart group…**

### Adding, Editing, and Removing Items

1. Select the appropriate tab (e.g., `Line` to work with line symbols).
2. Press the **+** (Add item) button at the bottom — this opens the Symbol Selector or relevant builder.
3. To edit an existing item: select it, press the **Edit item** (pencil) button.
4. To delete: select it, press the **Remove item** (red –) button or right-click > **Remove Item(s)**.

Right-click on any selection for additional options: Copy/Paste Item, Export as PNG/SVG, add to Favorites, or assign tags.

### Sharing Styles (Import/Export)

- **Export**: click **Import/Export > Export Item(s)…**, select items, press **Export** — saves as `.xml`.
- **Import**: click **Import/Export > Import Item(s)**, point to a `.xml` file or URL, optionally control tag import and favorites assignment.
- Alternatively, drag a `.xml` style file from the **Browser panel** onto the map canvas, or right-click it > **Import Style…**

---

## Symbol Selector

The Symbol Selector is the editor that opens whenever you configure a Marker, Line, or Fill symbol — from the Style Manager, Layer Properties, or any color/symbol button.

Read the screenshot `fig02.png` in this directory — it shows the full Symbol Selector dialog for a Line symbol, with the symbol layer tree at the top, global symbol properties (Unit, Opacity, Color, Width) in the middle, the library preview below, and Save Symbol / Advanced buttons at the bottom.

### Symbol Layer Tree

The tree (upper section of the dialog) shows stacked symbol layers that compose the final symbol. A live preview updates as you edit.

Toolbar buttons above/beside the tree:

- Read the screenshot `fig13.png` in this directory — it shows the green + button to add a new symbol layer
- Read the screenshot `fig08.png` in this directory — it shows the red – button to remove the selected symbol layer
- Read the screenshot `fig11.png` in this directory — it shows the lock icon to lock a layer's color, preventing it from changing when the top-level color is modified
- Read the screenshot `fig14.png` in this directory — it shows the duplicate layer button to copy a symbol layer or group

Use the up/down arrows to reorder layers.

### Global Symbol Properties

Set at the top level of the tree (applies to the whole symbol):

| Property | Notes |
|---|---|
| **Unit** | Millimeters, Points, Pixels, Meters at Scale, Map units, Inches |
| **Opacity** | 0–100% |
| **Color** | Propagates to all unlocked sub-layers |
| **Size / Width** | Proportionally resizes all embedded layers |
| **Rotation** | Marker symbols only |

### Symbol Layer Properties

Select any layer in the tree to configure it. Available types vary by geometry:

- **Marker**: Simple marker, Ellipse marker, SVG marker, Font marker, Filled marker, Raster image marker, Geometry generator, etc.
- **Line**: Simple line, Marker line, Hashed line, Arrow, Interpolated line, etc.
- **Fill**: Simple fill, Centroid fill, Gradient fill, Shapeburst fill, SVG fill, etc.

Common per-layer controls: color selector, unit selector, data-defined override button (yellow icon) next to almost every field, **Enable symbol layer** checkbox to hide without deleting, and **Draw effects** for paint effects.

### Saving a Custom Symbol

1. Configure the symbol in the tree.
2. Press **Save Symbol…** at the bottom-right.
3. Choose a **Destination** database, enter a **Name**, add **Tags**, and optionally check **Add to favorites**.

The **Advanced** menu provides: Clip features to canvas extent (line/fill), Force right-hand rule (fill), Buffer settings/halo (marker), Animation settings, Symbol levels, and data-defined size legend.

---

## Text Formats & Label Settings

Text formats store the visual formatting of text (font, color, buffer, shadow, background) independently of placement logic. Label settings combine a text format with layer-type-specific options like placement, priority, callouts, and rendering scale.

Read the screenshot `fig06.png` in this directory — it shows the Style Manager on the **Text Format** tab, displaying named text format presets (BlueUnderline, Default, GreyBuffer, lowerRed, RedUnderline, Shadowed) as large "Aa" previews organized by tag (Colorful, Grayscale, Showcase, Topography).

### Managing Text Formats in Style Manager

1. Open Style Manager > click the **Text Format** tab.
2. Press **+** to open the text format builder — configure font family, size, color, and optional buffer/shadow/background.
3. Save it with a name and tags for reuse across layers and print layouts.

### Managing Label Settings in Style Manager

1. Open Style Manager > click the **Label Settings** tab.
2. Press **+** to open the label settings builder — this includes all text format options plus placement (around point, curved on line, etc.), rendering (scale-based visibility), callouts, priority, and overlap handling.
3. Label settings are geometry-type-specific (point, line, polygon); choose accordingly.

Read the screenshot `fig12.png` in this directory — it shows the Label Settings tab icon (the "abc" labeling icon used throughout QGIS to identify label-related controls).

### Applying from Layer Properties

- Open **Layer Properties > Symbology** to apply symbols directly to a layer.
- Open **Layer Properties > Labels** to apply label settings; the same text format sub-options appear there inline.
- Use the Style Manager button inside either dialog to save a configuration for reuse or to load a saved preset.
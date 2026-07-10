Compose and export maps using QGIS's dedicated print layout designer, accessible from the Project menu.

## Opening & Managing Layouts

**Create a new layout:** `Project → New Print Layout` (or click the New Print Layout icon in the Project toolbar). You'll be prompted for a title.

**Layout Manager:** `Project → Layout Manager…` — lists all layouts in the project. From here you can create, duplicate, rename, delete, or open layouts. You can also drag a `.qpt` template file onto the map canvas to instantly create a layout from it.

**Reopen an existing layout:** `Project → Layouts →` (submenu lists all layouts by name).

## The Print Layout Window

The layout window has four main zones:

- **Left toolbar** — item-add tools (Add Map, Add Scale Bar, Add Legend, etc.) and navigation/selection tools
- **Canvas (center)** — the paper surface; what you design is what gets exported
- **Right panels (upper)** — Items list and Undo History
- **Right panels (lower)** — Layout (page/export settings), Item Properties (selected item), Atlas Generation

The **status bar** at the bottom shows mouse position, current page number, zoom level, and selected item count.

Toggle panels and toolbars via right-click on any toolbar or `View → Toolbars / Panels`.

## Building a Layout: Core Workflow

1. Open or create a layout (`Project → New Print Layout`).
2. Click **Add Map** in the left toolbar, then click-and-drag a rectangle on the canvas. The current QGIS map view renders inside it.
3. Click **Add Scale Bar**, then click on the canvas to place it.
4. Click **Add Legend**, then click-and-drag a rectangle to place the legend.
5. Click the **Select/Move Item** tool (arrow icon) to select any item and reposition it by dragging.
6. Resize a selected item by dragging the small white corner handles.
7. With an item selected, open the **Item Properties** panel (lower right) to adjust item-specific settings — map scale/rotation, legend contents, scale bar style, label text, etc.
8. Use the **Layout** panel (lower right) to set page size, orientation, and export resolution.

## Aligning & Arranging Items

- Select multiple items with `Shift+click` or rubber-band drag.
- Use `Edit → Select All` (`Ctrl+A`) to select everything.
- Alignment tools are in the toolbar: align left edges, center, distribute evenly, etc.
- `Delete` or `Backspace` removes selected items.
- The **Items panel** (upper right) shows a layer-like list; click to select, drag to reorder, toggle visibility with the eye icon.

## Page Settings

Right-click the canvas background → **Page Properties**, or `Layout → Page Properties…`. Set paper size, orientation, and background color per page.

Add pages: `Layout → Add Pages…`.

## Exporting

All export options are under the **Layout menu** or the Layout toolbar.

### Export as PDF (`Layout → Export as PDF…`)
Best for print-ready output. Set export resolution in the dialog. Enable **Always export as vectors** if you need editable vector output. Watch for raster layer "seams" — enable **Disable tiled raster layer exports** if you see them (uses more memory).

### Export as Image (`Layout → Export as Image…`)
Supports PNG, TIFF, JPG, BMP, and others.
- Set resolution and optionally override page dimensions in the **Image Export Options** dialog.
- **Crop to content** trims the output to the bounding box of all items.
- **Generate world file** creates a georeferenced sidecar file (`.tfw`, `.pnw`, etc.).
- Multi-page layouts export each page as a separate file (e.g., `map_2.png`, `map_3.png`).
- Use PNG or TIFF (not JPG/BMP) when items extend beyond the page edge — BMP/JPG renders transparent areas as black.

### Export as SVG (`Layout → Export as SVG…`)
- Enable **Export map layers as SVG groups** to get named, editable layers in Inkscape/Illustrator.
- **Simplify geometries** reduces file size by removing redundant vertices below the export resolution threshold.
- **Text export** controls whether labels export as editable text or outlined paths.

### Print (`Ctrl+P`)
Sends to a connected printer or PostScript file.

## Saving Layouts

- **Save project** (`Ctrl+S`) — embeds the layout in the `.qgz`/`.qgs` project file.
- **Save as Template** (`Layout → Save as Template…`) — saves a `.qpt` file for reuse across projects.
- **Load template items** (`Layout → Add Items from Template`) — imports items from a `.qpt` into the current layout.

## Common Pitfalls

- **Map doesn't update after layer changes:** Right-click the map item → Update Preview, or check that the map item is linked to the correct map canvas in Item Properties.
- **Legend shows all layers, not just visible ones:** In the Legend item properties, uncheck **Auto update** and manually remove unwanted layers.
- **Export looks different from canvas preview:** Caused by rendering options that require rasterization. Check **Export as raster** (Layout panel) or accept the tradeoff with **Always export as vectors**.
- **Scale bar unlinked warning on export:** The scale bar's linked map item may have been deleted or renamed. Re-link it in the scale bar's Item Properties.
- **Items excluded from export unexpectedly:** Check Item Properties for each item — the **Exclude item from exports** checkbox may be enabled.
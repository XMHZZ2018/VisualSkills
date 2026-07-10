## Print Layout: Compose and export maps using QGIS's dedicated map designer.

## Opening a Print Layout

Create a new layout from the **Project toolbar** or menu:

- **Project menu**: Project → New Print Layout (or click the New Print Layout icon)  
  Read the screenshot `fig01.png` in this directory — it shows the New Print Layout toolbar button
- You will be prompted to enter a title for the layout.
- To manage all existing layouts (open, rename, duplicate, delete, create from template): **Project → Layout Manager…**, or click the Layout Manager button.  
  Read the screenshot `fig15.png` in this directory — it shows the Layout Manager toolbar button

## The Print Layout Interface

Read the screenshot `fig02.png` in this directory — it shows a complete print layout with map, legend, scale bar, attribute table, HTML frame, and the full panel layout including Items, Layout, Item Properties, and Atlas panels on the right side

Key areas:
- **Left toolbar**: buttons to add items (map, scale bar, legend, labels, images, shapes, tables, HTML frames) and to navigate/select
- **Right panels (upper)**: **Items** (layer list of all layout elements) and **Undo History**
- **Right panels (lower)**: **Layout** (page/export settings), **Item Properties** (settings for the selected item), **Atlas**
- **Status bar** (bottom): mouse position, current page number, zoom level, selected item count

## Building a Layout: Step-by-Step

### 1. Add a Map
1. Click the **Add Map** button in the left toolbar.  
   Read the screenshot `fig05.png` in this directory — it shows the Add Map toolbar icon (an open book with a map pin)
2. Click and drag a rectangle on the canvas — the current QGIS map view renders inside it.
3. Resize by dragging the white corner handles; move by dragging the item body.

### 2. Add a Scale Bar
1. Click the **Add Scale Bar** button.  
   Read the screenshot `fig07.png` in this directory — it shows the Add Scale Bar toolbar icon
2. Click anywhere on the canvas to place it. It auto-links to the map item.

### 3. Add a Legend
1. Click the **Add Legend** button.  
   Read the screenshot `fig09.png` in this directory — it shows the Add Legend toolbar icon (a small grid of colored squares)
2. Click and drag a rectangle to define the legend area.

### 4. Select and Adjust Items
- Switch to the **Select/Move Item** tool to select, move, or resize items.  
  Read the screenshot `fig11.png` in this directory — it shows the Select/Move Item cursor icon
- With an item selected, use the **Item Properties** panel (lower right) to adjust settings — e.g., set **Map orientation** to rotate the map view by a specific angle.
- Delete items with the **Delete** or **Backspace** key.

### 5. Save the Project
- Save at any time with **Ctrl+S** or the Save Project button.  
  Read the screenshot `fig13.png` in this directory — it shows the Save Project (floppy disk) toolbar icon

## Exporting the Layout

Access all export options via **Layout menu** or the Layout toolbar.

### Print
- **Layout → Print…** (`Ctrl+P`) — sends to a connected printer or PostScript file.  
  Read the screenshot `fig04.png` in this directory — it shows the Print toolbar icon (a printer)

### Export as Image
1. Click the **Export as Image** icon.  
   Read the screenshot `fig06.png` in this directory — it shows the Export as Image toolbar icon (a map with a floppy disk)
2. Choose format (PNG, TIFF, JPG, BMP, etc.) and output path.
3. In the **Image Export Options** dialog:
   - Override **Export resolution** (default from Layout panel, typically 300 dpi)
   - Enable **antialiasing** for smoother output
   - Check **Generate world file** to create a georeferenced sidecar file (`.tfw`, `.pnw`, `.jgw`)  
     Read the screenshot `fig14.png` in this directory — it shows an unchecked checkbox, as the Generate world file option appears unchecked by default
   - Check **Crop to content** to trim the output to the bounding box of all items
   - Check **Open file after exporting** to auto-open the result
4. Multi-page layouts export one file per page (e.g., `mymap_2.png`).

> **Tip**: Use PNG or TIFF (not JPG/BMP) when items extend beyond the page — those formats support transparency for the background area.

### Export as SVG
1. Click the **Export as SVG** icon.  
   Read the screenshot `fig08.png` in this directory — it shows the Export as SVG toolbar icon
2. In the **SVG Export Options** dialog, key options:
   - **Export map layers as SVG groups** — layers are named to match QGIS layer names
   - **Always export as vectors** — keeps objects as vectors (may differ visually from preview)
   - **Export RDF metadata** — embeds title, author, date, description
   - **Simplify geometries** — reduces file size by removing redundant vertices
   - **Text export** — choose whether labels export as text objects or outlines
   - **Crop to content**, **Disable tiled raster exports** (fixes visible seams at cost of memory)

### Export as PDF
1. Click the **Export as PDF** icon.  
   Read the screenshot `fig10.png` in this directory — it shows the Export as PDF toolbar icon (a red PDF icon)
2. Choose output path; options mirror the SVG dialog (resolution, crop, vector/raster, metadata).

## Export Settings Reference

The **Layout panel** (lower-right) controls default export behavior:
- **Export resolution** — DPI for raster output
- **Print as raster** — rasterize the entire output
- **Always export as vectors** — override per-item rasterization
- **Save world file** — default state for the georeferenced export option

Individual pages and items can be excluded from exports via their respective properties panels (**Exclude page from exports** / **Exclude item from exports**).

## Layout Manager

Use **Project → Layout Manager…** to organize layouts across the project:
- Open, duplicate, rename, or delete any layout
- Create new layouts from scratch or from `.qpt` template files
- Template search paths can be added at **Settings → Options → Layouts**

> **Tip**: Drag a `.qpt` template file onto the map canvas or double-click it in the Browser panel to instantly create a layout from it.
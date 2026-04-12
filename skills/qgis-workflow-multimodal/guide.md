Practical step-by-step workflows for QGIS 3.44 GUI tasks. Use these workflows whenever you need to perform GIS operations.

## QGIS Screen Layout

Read the screenshot `fig01_qgis_layout.png` in this directory — it shows the complete QGIS interface with numbered regions:
- **Region 1 (top, y≈25)**: Menu bar — Project, Edit, View, Layer, Settings, Plugins, Vector, Raster, Database, Web, Mesh, Processing, Help
- **Region 2 (y≈50-80)**: Toolbars with icon buttons
- **Region 3 (left panel)**: Browser panel (top) and Layers panel (bottom) — shows loaded layers
- **Region 4 (center)**: Map canvas — the main map display area
- **Region 5 (bottom, y≈700)**: Status bar with coordinates and scale
- **Right panel**: Processing Toolbox (if open) — this is where you search and run algorithms

**CRITICAL**: The menu bar items are at the very top of the screen (y≈25). From left to right: Project, Edit, View, Layer, Settings, Plugins, Vector, Raster, Database, Web, Mesh, Processing, Help. Click precisely on the text.

## Workflow 1: Loading Data Files

Data files for tasks are typically on the Desktop (`/home/user/Desktop/`) or in the home directory.

### Method A: Browser Panel (PREFERRED — most reliable)
1. Look at the **left panel** — the Browser panel shows the filesystem
2. Expand **Home** or **Desktop** folder in the Browser tree
3. **Double-click** the data file (GeoJSON, Shapefile, GeoPackage) to add it as a layer
4. The layer appears in the Layers panel below and on the map canvas

### Method B: Layer Menu
1. Click **Layer** in the menu bar (y≈25, approximately x≈175)
2. Click **Add Layer** → **Add Vector Layer** (or Add Raster Layer)
3. In the dialog, click the **...** button next to "Vector Dataset(s)"

Read the screenshot `fig07_add_vector_dialog.png` in this directory — it shows the Add Vector Layer dialog with Source Type and file browser button

4. Navigate to the file, select it, click **Open**
5. Click **Add**, then **Close**

### Method C: Drag and Drop
1. If the file manager is open, drag the file directly onto the map canvas

## Workflow 2: Running a Processing Algorithm (MOST COMMON)

Almost all QGIS tasks require running Processing algorithms (Buffer, Clip, Join, Reproject, etc.).

### Step 1: Open the Processing Toolbox
- Click **Processing** in the menu bar (near the right end, y≈25, approximately x≈830)
- Click **Toolbox** in the dropdown
- OR use keyboard shortcut: **Ctrl+Alt+T**
- The toolbox panel opens on the RIGHT side of the screen

Read the screenshot `fig02_toolbox_panel.png` in this directory — it shows the Processing Toolbox panel with categories like Cartography, Database, Vector analysis, Vector geometry, etc.

### Step 2: Search for the Algorithm
- At the TOP of the Processing Toolbox panel, there is a **search bar** (text field with magnifying glass icon)
- **Click the search bar** and type the algorithm name (e.g., "buffer", "clip", "join")
- Results filter as you type

Read the screenshot `fig03_toolbox_search.png` in this directory — it shows search results after typing "ag" in the search bar, with matching algorithms listed below

### Step 3: Open the Algorithm Dialog
- **Double-click** the algorithm name in the search results
- A dialog window opens with parameters

Read the screenshot `fig04_algorithm_dialog.png` in this directory — it shows the algorithm dialog with Parameters tab, input fields, and Run button at the bottom

### Step 4: Set Parameters
- **Input layer**: Click the dropdown to select from loaded layers
- **Parameters**: Set values as needed (distance, field names, etc.)
- **Output**: By default creates a temporary layer. To save to file, click the **...** button next to the output field and choose "Save to File..."
- Set the output path (e.g., `/home/user/Desktop/output.geojson`)

### Step 5: Run the Algorithm
- Click the **Run** button (bottom of dialog)
- Wait for completion — the Log tab shows progress

Read the screenshot `fig05_algorithm_log.png` in this directory — it shows the Log tab with execution details and "Algorithm completed" message

- Click **Close** when done
- The result layer is automatically added to the Layers panel

### Common Processing Algorithms
| Task | Algorithm Name | Location |
|------|---------------|----------|
| Buffer | "Buffer" | Vector geometry → Buffer |
| Clip | "Clip" | Vector overlay → Clip |
| Intersect | "Intersection" | Vector overlay → Intersection |
| Union | "Union" | Vector overlay → Union |
| Dissolve | "Dissolve" | Vector geometry → Dissolve |
| Join by location | "Join attributes by location" | Vector general |
| Join by field | "Join attributes by field value" | Vector general |
| Reproject | "Reproject layer" | Vector general |
| Centroids | "Centroids" | Vector geometry |
| Polygonize | "Polygonize" | Raster conversion |
| Heatmap/KDE | "Heatmap (Kernel Density)" | Interpolation |
| Field Calculator | "Field calculator" | Vector table |
| Select by expression | "Select by expression" | Vector selection |
| Extract by expression | "Extract by expression" | Vector selection |
| Save selected | "Save selected features" | Vector general |
| Multipart to singlepart | "Multipart to singleparts" | Vector geometry |
| Distance matrix | "Distance matrix" | Vector analysis |
| Hub lines | "Join by lines (hub lines)" | Vector analysis |
| Simplify | "Simplify" | Vector geometry |

## Workflow 3: Attribute Table & Field Calculator

### Opening the Attribute Table
1. **Right-click** the layer name in the Layers panel (left side)
2. Click **Open Attribute Table**
3. OR select the layer and press **F6**

Read the screenshot `fig08_attribute_table.png` in this directory — it shows the attribute table with columns, rows, and the quick field calculation bar at top

### Using the Field Calculator
1. In the attribute table, click the **Toggle editing** button (pencil icon, top-left toolbar)
2. Click the **Field Calculator** button (abacus icon) — OR press **Ctrl+I**
3. Choose "Create a new field" or "Update existing field"
4. Set field name and type
5. Write expression (e.g., `$area`, `$length`, `$x`, `$y`)
6. Click **OK**
7. Click **Toggle editing** again to save, confirm save

Read the screenshot `fig09_field_calculator.png` in this directory — it shows the Field Calculator dialog with expression builder

### Alternative: Use Processing "Field Calculator" Algorithm
- Open Processing Toolbox → search "Field calculator"
- This is sometimes easier than the GUI field calculator

## Workflow 4: Exporting Layers

### Method A: Right-click Export (PREFERRED)
1. **Right-click** the layer in the Layers panel
2. Click **Export** → **Save Features As...**
3. Set format (GeoJSON, GPKG, CSV, Shapefile)
4. Set filename and path
5. Set CRS if needed
6. Click **OK**

### Method B: Processing Algorithm
- Use "Save vector features to file" algorithm
- Or use "Package layers" to export multiple layers

## Workflow 5: Setting CRS / Reprojecting

### Reprojecting a Layer (creates new layer in target CRS)
1. Open Processing Toolbox → search "Reproject"
2. Double-click "Reproject layer"
3. Set Input layer
4. Set Target CRS (click the globe icon, type EPSG code like "4326", "3857", "32610")
5. Click Run

### Setting Project CRS
1. Click the CRS indicator in the bottom-right status bar (shows current EPSG code)
2. Or go to **Project** → **Properties** → **CRS** tab
3. Search for the desired CRS

## Workflow 6: Saving the Project

1. Press **Ctrl+S** or click **Project** → **Save As...**
2. Navigate to desired location
3. Enter filename
4. Click **Save**

## Key Keyboard Shortcuts
| Shortcut | Action |
|----------|--------|
| Ctrl+Alt+T | Open Processing Toolbox |
| Ctrl+Shift+O | Open Data Source Manager |
| F6 | Open Attribute Table |
| Ctrl+I | Open Field Calculator (in edit mode) |
| Ctrl+S | Save Project |
| Ctrl+Z | Undo |
| V | Select tool |
| Ctrl+Shift+E | Export as image |

## Troubleshooting Common Issues

### Can't find an algorithm
- Make sure Processing Toolbox is open (Ctrl+Alt+T)
- Try different search terms (e.g., "buffer" not "create buffer zone")
- Check if the algorithm is under a different provider (QGIS vs GDAL)

### Menu doesn't open
- Click precisely on the menu text (y≈25 pixels from top)
- If a dialog is open, close it first (click X or press Escape)
- Click on the map canvas first to ensure QGIS has focus

### Processing algorithm fails
- Check that input layers are loaded and valid
- Check that the CRS is appropriate for the operation
- Read the Log tab for error messages

### Layer not visible on map
- Check the checkbox next to the layer name in Layers panel
- Right-click layer → Zoom to Layer

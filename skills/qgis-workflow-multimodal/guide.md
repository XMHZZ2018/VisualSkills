Practical step-by-step workflows for QGIS 3.44 GUI tasks. Study the screenshots carefully — they show you exactly what each UI element looks like so you can find it on screen.

## QGIS Screen Layout

Read the screenshot `fig01_qgis_layout.png` in this directory — it shows the complete QGIS interface with numbered annotations. Study this image to understand the layout:

- **Menu bar** (top strip with text labels): Project, Edit, View, Layer, Settings, Plugins, Vector, Raster, Database, Web, Mesh, Processing, Help — these are plain text labels in a horizontal row at the very top of the window
- **Toolbars** (below menu bar): rows of small icon buttons for common actions
- **Browser panel** (left side, upper): filesystem tree for navigating to data files — expand Home or Desktop to find files
- **Layers panel** (left side, lower): shows all loaded layers with checkboxes for visibility
- **Map canvas** (large center area): the main map display
- **Processing Toolbox** (right side, if open): panel with search bar at top and category tree below — this is where you find and run algorithms
- **Status bar** (very bottom): shows coordinates, scale, and CRS info

## Workflow 1: Loading Data Files

Data files for tasks are typically on the Desktop or in the home directory.

### Method A: Browser Panel (RECOMMENDED — most reliable)
1. Find the **Browser** panel on the left side of the screen — it's a tree view showing filesystem locations
2. Look for **Home** or **Desktop** entries in the tree
3. Click the triangle/arrow next to the folder name to expand it
4. **Double-click** the data file (.geojson, .shp, .gpkg) to add it as a layer
5. Confirm the layer appears in the **Layers** panel and features show on the map canvas

### Method B: Keyboard Shortcut (RELIABLE FALLBACK)
1. Press **Ctrl+Shift+V** to open the Add Vector Layer dialog directly
2. Or press **Ctrl+Shift+O** to open the Data Source Manager

Read the screenshot `fig06_data_source_manager.png` in this directory — it shows the Data Source Manager with Browser tab on the left sidebar and filesystem tree on the right

Read the screenshot `fig07_add_vector_dialog.png` in this directory — it shows the Add Vector Layer dialog with a "Source Type" section (File/Directory/Database radio buttons), an Encoding dropdown, and a "Vector Dataset(s)" file browser with a **...** button to browse for files

### Method C: Layer Menu
1. Click **Layer** in the menu bar — it's the 4th text label from the left in the top menu strip
2. Hover over **Add Layer** to expand the submenu
3. Click **Add Vector Layer** (or Add Raster Layer for raster data)

## Workflow 2: Running a Processing Algorithm (MOST IMPORTANT)

Almost ALL QGIS tasks require running Processing algorithms (Buffer, Clip, Join, Reproject, etc.). Master this workflow.

### Step 1: Open the Processing Toolbox
- **BEST**: Press **Ctrl+Alt+T** — this keyboard shortcut reliably opens/toggles the Processing Toolbox
- Alternative: Click **Processing** in the menu bar (near the right end of the menu text labels), then click **Toolbox**

Read the screenshot `fig02_toolbox_panel.png` in this directory — it shows what the Processing Toolbox panel looks like: a narrow panel with a search field at the top (magnifying glass icon) and a tree of algorithm categories below (Cartography, Database, Interpolation, Layer tools, Network analysis, Raster analysis, Raster tools, Vector analysis, Vector creation, Vector geometry, Vector overlay, Vector selection, Vector table)

### Step 2: Search for the Algorithm
- The Processing Toolbox has a **search bar** at the very top — it's a text input field with a magnifying glass icon
- Click in the search bar and type the algorithm name (e.g., "buffer", "clip", "simplify")
- As you type, the tree below filters to show only matching algorithms

Read the screenshot `fig03_toolbox_search.png` in this directory — it shows the toolbox after typing "ag" in the search bar, with filtered results showing matching algorithms from different categories. Notice the search bar at the top with the typed text, and the filtered category tree below.

### Step 3: Open the Algorithm Dialog
- **Double-click** the algorithm name in the filtered results
- A dialog window opens with the algorithm name in the title bar

Read the screenshot `fig04_algorithm_dialog.png` in this directory — it shows a typical algorithm dialog (Vector Geometry - Centroids). Key elements:
- **Title bar**: shows the algorithm category and name
- **Parameters tab** (left side): input fields for the algorithm — dropdowns for layer selection, checkboxes for options, text fields for output paths
- **Description** (right side): explains what the algorithm does
- **Input layer dropdown**: click to select from loaded layers
- **Output field**: by default says "[Create temporary layer]" — click the **...** button to save to a specific file
- **Run button**: at the bottom of the dialog — click this to execute
- **Close button**: next to Run — click after execution completes

### Step 4: Set Parameters
- **Input layer**: Click the dropdown to select from loaded layers in your project
- **Parameters**: Fill in values as required (distances, field names, expressions)
- **Output file**: To save results to a specific location:
  1. Click the **...** button next to the output field
  2. Choose "Save to File..."
  3. Set the format (GeoJSON, GeoPackage, Shapefile) and file path
  4. Common path: `/home/user/Desktop/output.geojson`

### Step 5: Run and Verify
- Click the **Run** button at the bottom of the dialog
- The dialog switches to the **Log** tab showing progress

Read the screenshot `fig05_algorithm_log.png` in this directory — it shows the Log tab after successful execution with "Algorithm 'Centroids' starting..." and "Execution completed" messages, plus the output file path

- When complete, click **Close**
- The result layer automatically appears in the Layers panel

### Common Processing Algorithms Reference
| What You Need To Do | Search For | Category |
|------|---------------|----------|
| Create buffer zones | "Buffer" | Vector geometry |
| Clip one layer by another | "Clip" | Vector overlay |
| Find intersection of layers | "Intersection" | Vector overlay |
| Merge/union layers | "Union" | Vector overlay |
| Dissolve features | "Dissolve" | Vector geometry |
| Join layers by location | "Join attributes by location" | Vector general |
| Join layers by field value | "Join attributes by field value" | Vector general |
| Change coordinate system | "Reproject layer" | Vector general |
| Get polygon centers | "Centroids" | Vector geometry |
| Raster to vector | "Polygonize" | Raster conversion |
| Create heatmap | "Heatmap (Kernel Density)" | Interpolation |
| Add/calculate field | "Field calculator" | Vector table |
| Filter by expression | "Extract by expression" | Vector selection |
| Select by expression | "Select by expression" | Vector selection |
| Split multipart features | "Multipart to singleparts" | Vector geometry |
| Distance between features | "Distance matrix" | Vector analysis |
| Connect points to hubs | "Join by lines (hub lines)" | Vector analysis |
| Simplify geometry | "Simplify" | Vector geometry |
| Calculate line lengths | "Add geometry attributes" | Vector geometry |

## Workflow 3: Attribute Table & Field Calculator

### Opening the Attribute Table
- Select the layer in the **Layers panel** (click its name), then press **F6**
- Or: right-click the layer name → **Open Attribute Table**

Read the screenshot `fig08_attribute_table.png` in this directory — it shows the attribute table window with column headers (id, name_2, type_2), rows of data, and a toolbar at the top. Note the quick field calculation bar at the top with a field dropdown, operator, and expression field.

### Using the Field Calculator
1. First enable editing: click the **pencil icon** (Toggle Editing) in the attribute table toolbar — it's the leftmost icon
2. Open Field Calculator: press **Ctrl+I** or click the **abacus icon** in the toolbar
3. In the Field Calculator dialog:
   - Choose "Create a new field" or "Update existing field"
   - Set **Output field name** and **Output field type**
   - Build expression in the expression editor (e.g., `$area`, `$length`, `$x`, `$y`, `length($geometry)`)
   - Click **OK**

Read the screenshot `fig09_field_calculator.png` in this directory — it shows the Field Calculator with "Create a new field" option, output field name/type fields on the left, and the expression builder on the right with function categories

4. Save edits: click the **pencil icon** again → confirm save
5. Or use the **Quick Field Calculation Bar** at the top of the attribute table for simple calculations

### Alternative: Processing Field Calculator (OFTEN EASIER)
Instead of the GUI field calculator, search "Field calculator" in the Processing Toolbox — it works as a processing algorithm with input/output layer fields.

## Workflow 4: Exporting Layers

### Method A: Right-click Export (STANDARD)
1. **Right-click** the layer name in the Layers panel
2. Click **Export** → **Save Features As...**
3. In the export dialog:
   - Set **Format** (GeoJSON, GPKG, CSV, ESRI Shapefile)
   - Set **File name** using the **...** browse button
   - Set **CRS** if you need to reproject during export
   - Click **OK**

### Method B: From Processing Algorithm Output
When running a Processing algorithm, set the output path directly in the algorithm dialog (see Workflow 2, Step 4).

## Workflow 5: Setting CRS / Reprojecting

### Reprojecting a Layer (creates new layer in target CRS)
1. Open Processing Toolbox (**Ctrl+Alt+T**)
2. Search for "Reproject"
3. Double-click "Reproject layer"
4. Set Input layer and Target CRS
5. For CRS selection: click the **globe icon** next to the CRS field, then type the EPSG code (e.g., "4326", "3857", "32610") in the search/filter box
6. Click Run

### Checking/Setting Project CRS
- Look at the **bottom-right corner** of the status bar — it shows the current project CRS (e.g., "EPSG:4326")
- Click it to change the project CRS

## Workflow 6: Saving the Project
1. Press **Ctrl+Shift+S** (Save As) or **Ctrl+S** (Save)
2. Navigate to the desired location
3. Enter the filename (saves as .qgz)
4. Click **Save**

## Essential Keyboard Shortcuts
| Shortcut | Action |
|----------|--------|
| Ctrl+Alt+T | Toggle Processing Toolbox panel |
| Ctrl+Shift+V | Add Vector Layer dialog |
| Ctrl+Shift+R | Add Raster Layer dialog |
| Ctrl+Shift+O | Open Data Source Manager |
| F6 | Open Attribute Table for selected layer |
| Ctrl+I | Open Field Calculator (when editing) |
| Ctrl+S | Save Project |
| Ctrl+Shift+S | Save Project As |
| Ctrl+Z | Undo |
| Escape | Close current dialog/cancel operation |
| Alt+Tab | Switch between windows |

## Troubleshooting

### If a menu click doesn't work
- Try the keyboard shortcut instead (see table above)
- Make sure no dialog is blocking — press Escape first
- Click once on the map canvas to ensure QGIS has focus, then try again

### If you get stuck repeating the same action
- STOP and try a completely different approach
- Use keyboard shortcuts instead of mouse clicks
- If Processing Toolbox isn't visible, press Ctrl+Alt+T

### If a Processing algorithm fails
- Check the Log tab for the specific error message
- Common issues: wrong CRS for distance calculations, missing input layer, invalid field name
- Try running with default output (temporary layer) first, then export separately

### If the QGIS window disappears
- Press **Alt+Tab** to cycle through windows
- Or click the QGIS icon in the taskbar at the bottom of the screen

Use the Processing Toolbox, Graphical Modeler, and batch processing to build and automate spatial analysis workflows in QGIS.

## Opening the Processing Toolbox

**Processing → Toolbox** (or `Ctrl+Alt+T` on some installations). The panel docks on the right side by default — a scrollable tree of algorithm providers grouped by source (QGIS native, GDAL, GRASS, SAGA, etc.).

Top toolbar buttons in the Toolbox:
- **Models** — Create New Model / Open Existing Model / Add Model to Toolbox
- **Scripts** — Create / Open Python scripts
- **History** — log of past algorithm runs
- **Results Viewer** — view non-layer outputs (HTML reports, tables)
- **Edit Features In-Place** — filters toolbox to show only algorithms that modify the active layer directly (no new output layer)
- **Options** — Processing settings

## Finding and Running Algorithms

1. Type any word in the **Search...** box at the top of the Toolbox — results filter in real time.
2. The top of the list shows **Recently Used** and **Favorites** sections for quick re-access.
3. **Double-click** any algorithm to open its dialog, or right-click for options:
   - Execute...
   - Execute as Batch Process...
   - Add to Favorites / Remove from Favorites
   - Edit Rendering Styles for Outputs...

## The Algorithm Dialog

The dialog has two tabs on the left (**Parameters** and **Log**) and a description panel on the right.

### Key parameter types

| Type | UI element |
|---|---|
| Vector/raster layer | Dropdown; `...` button to browse files or databases |
| Numerical value | Spin box; data-defined override button for expressions |
| Field | Dropdown populated from selected layer's attributes |
| CRS | Dropdown + button; drag a layer onto the widget to copy its CRS |
| String | Text box |
| Range | Two text boxes (min/max) |

**Vector layer widget extras:**
- **Iterator button** (cycle icon) — runs the algorithm once per feature instead of once per layer; useful for per-feature processing without manual splitting.
- **Advanced options** (gear icon) — set invalid geometry handling, limit feature count, or add an expression-based feature filter to subset input on the fly.
- Checkbox at bottom: **Selected features only** — restricts execution to the current selection.

**Tip:** Drag layers from the Layers or Browser panel directly into parameter dropdowns instead of using the menu.

### Running and output

- Click **Run** to execute. Watch the **Log** tab for progress and errors.
- Output layers load automatically into the project unless you set a file path in the output field (leave blank for a temporary scratch layer, or click `...` to save to disk).
- To save default parameter values for an algorithm, set them and use the **Save** button in the dialog (where available).

## Batch Processing

Right-click any algorithm → **Execute as Batch Process...** to open the batch dialog.

1. Each row = one execution of the algorithm.
2. Click **Add row** to add more runs; click a cell to set its value.
3. Use **Autofill...** on any column to populate it from a list of files or layer names automatically.
4. The output column lets you set a naming pattern (e.g., `output_@{INPUT_LAYER}`) so files are named automatically.
5. Click **Run** — all rows execute sequentially; the log shows per-row results.

## Graphical Modeler

**Processing → Model Designer** opens the modeler in a new window.

### Interface layout

- **Left panels** (5 tabs): Inputs, Toolbox, Model Properties, Variables, Undo History
- **Central canvas**: drag-and-drop workflow design area
- **Top menus/toolbar**: Model menu, Edit menu, View menu

### Building a model

**Step 1 — Set model identity:**
In the **Model Properties** panel, enter a Name (required) and Group. This controls where the model appears in the Processing Toolbox.

**Step 2 — Add inputs:**
In the **Inputs** panel, double-click an input type (e.g., Vector Layer, Raster Layer, Number) to configure it. Set the description (shown to users), default value, and whether it's mandatory or advanced. Each input appears as a box on the canvas.

You can also drag input types directly onto the canvas.

**Step 3 — Add algorithms:**
Search in the **Toolbox** panel and double-click (or drag) an algorithm onto the canvas. A configuration dialog opens — wire up parameters to your model inputs or to outputs from earlier algorithms using the dropdowns.

**Step 4 — Connect outputs to subsequent steps:**
When configuring an algorithm, any parameter dropdown will list "Algorithm outputs" from upstream steps — select these to chain algorithms together.

**Step 5 — Mark final outputs:**
In an algorithm's configuration, give output fields a name to expose them as model outputs (shown to end users). Leave unnamed to use as intermediate only.

**Step 6 — Validate and run:**
- **Model → Validate Model** — checks for broken connections or missing inputs.
- **F5** (or Model → Run Model) — runs the full model.
- **Shift+F5** — runs only selected steps (useful for debugging).

### Key modeler shortcuts

| Action | Shortcut |
|---|---|
| Run model | F5 |
| Run selected steps | Shift+F5 |
| Save | Ctrl+S |
| Save as | Ctrl+Shift+S |
| Undo | Ctrl+Z |
| Redo | Ctrl+Y |
| Delete selected | Del |
| Zoom full | Ctrl+0 |

### Organizing large models

- **Edit → Add Group Box** — draw a labeled background box to visually group related components.
- **View → Show Comments** — display per-component notes on the canvas.
- **Edit → Snap selected components to Grid** — aligns components for a clean layout.

### Saving and sharing models

- **Save Model** → `.model3` file on disk (re-openable and editable).
- **Save Model in project** — embeds the model in the `.qgz` file for easy sharing.
- **Export as Script Algorithm** — converts the model to a Python script for further customization.

## Common Pitfalls

- **Algorithm missing from modeler:** Not all toolbox algorithms work in the modeler — only those with well-defined output counts. Look in the **Modeler Tools** group for modeler-specific alternatives.
- **CRS mismatches:** Always check that input layers share a CRS or reproject before analysis; the layer widget shows CRS next to the layer name to help catch this.
- **Temporary outputs lost on close:** Scratch layers (no file path set) are lost when QGIS closes. Set a file path for outputs you need to keep.
- **Batch process output naming:** Without a naming pattern, batch outputs overwrite each other. Always set a pattern using `@{PARAMETER_NAME}` tokens.
- **Iterator on multi-input algorithms:** The iterator only applies to the first toggled vector parameter in declaration order — not all vector inputs iterate simultaneously.
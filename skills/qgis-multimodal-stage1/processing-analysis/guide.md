Here is the multimodal guide:

---

QGIS's Processing framework provides three interconnected tools for spatial analysis: the Toolbox for running individual algorithms, the Graphical Modeler for chaining algorithms into reusable workflows, and Batch Processing for running the same algorithm across multiple inputs.

## Processing Toolbox

Open via **Processing > Toolbox** or press **Ctrl+Alt+T**. The panel docks to the right side of the QGIS window by default.

Read the screenshot `fig01.png` in this directory — it shows the Processing Toolbox panel with algorithms grouped by provider (Vector analysis, Raster analysis, GDAL, etc.) in a collapsible tree.

The toolbar at the top of the Toolbox contains:

- Read the screenshot `fig04.png` in this directory — it shows the Models icon used to create, open, or add models to the toolbox
- Read the screenshot `fig07.png` in this directory — it shows the Scripts icon for creating or loading Python script tools
- Read the screenshot `fig10.png` in this directory — it shows the History icon that opens the Processing History panel (a log of all previously run algorithms)
- Read the screenshot `fig13.png` in this directory — it shows the Results Viewer icon for inspecting outputs from algorithms that produce non-layer results (e.g. HTML reports)

### Running an Algorithm

1. Type a keyword in the **Search...** box at the top of the Toolbox to filter algorithms.
2. Double-click an algorithm to open its dialog.
3. Read the screenshot `fig06.png` in this directory — it shows a typical algorithm dialog (Centroids), with a **Parameters** tab on the left for inputs, a **Log** tab to monitor execution, and an algorithm description on the right. Output defaults to `[Create temporary layer]`; click `...` to save to file.
4. Click **Run**. A progress bar appears at the bottom; output layers load automatically into the Layers panel.

**Right-click** any algorithm in the Toolbox for additional options: Execute, Execute as Batch Process, Edit Rendering Styles for Outputs, Add/Remove from Favorites.

### In-Place Editing Mode

Click the **Edit Features In-Place** button in the Toolbox toolbar to filter the list to only algorithms that modify the active layer directly without creating a new output layer.

---

## Graphical Modeler

Open via **Processing > Model Designer**.

Read the screenshot `fig02.png` in this directory — it shows the Model Designer window: a large canvas on the right where the workflow graph is built, and a left panel with five tabs: **Inputs**, **Toolbox**, **Model Properties**, **Variables**, and **Undo History**.

### Building a Model

1. In **Model Properties**, set a **Name** (required) and **Group** — this controls where the model appears in the Processing Toolbox.
2. From the **Inputs** panel, double-click an input type (e.g. Vector Layer, Raster Layer, Number) to add it to the canvas. A dialog prompts for description, default value, and whether the input is mandatory.
3. From the **Toolbox** panel, search for and double-click an algorithm to add it to the canvas. In the algorithm's configuration dialog, connect its inputs to the model's input parameters or to outputs from earlier algorithms.
4. To mark an algorithm's output as a final model output, give it a name in the output field (rather than leaving it blank).
5. Drag connections between components directly on the canvas to wire the workflow.

### Key Model Menu Actions

| Action | Shortcut |
|---|---|
| Run Model | **F5** |
| Run Selected Steps only | **Shift+F5** |
| Save Model (.model3) | **Ctrl+S** |
| Open Model | **Ctrl+O** |
| Undo | **Ctrl+Z** |

- Read the screenshot `fig05.png` in this directory — it shows the green checkmark Validate icon used to verify that all algorithms and inputs in the model are correctly connected before saving or sharing
- Read the screenshot `fig08.png` in this directory — it shows the Run (play) button in the Navigation toolbar to execute the model
- Read the screenshot `fig14.png` in this directory — it shows the Run Selected Steps button, which executes only highlighted components — useful for debugging part of a complex model

**Export options**: Save the model's canvas diagram as Image, PDF, or SVG (via **Model > Export**), or export the entire model as a Python script algorithm.

---

## Batch Processing

Batch processing runs one algorithm repeatedly across multiple inputs in a single operation.

### Launching Batch Mode

**Method 1 — From the Toolbox:** Right-click any algorithm and choose **Execute as Batch Process...**

Read the screenshot `fig03.png` in this directory — it shows the right-click context menu on a toolbox algorithm with "Execute as Batch Process..." highlighted

**Method 2 — From the Algorithm Dialog:** Click **Run as Batch Process...** in the bottom-left of any open algorithm dialog (visible in `fig06.png`).

### Using the Batch Interface

Read the screenshot `fig09.png` in this directory — it shows the Batch Processing dialog as a spreadsheet-style table where each row is one execution run, with columns for each input parameter and output path

1. Each row = one algorithm run. Click Read the screenshot `fig15.png` in this directory — it shows the green **+** button to add rows.
2. For file-based inputs, use the **...** button in each cell to select input files, or use **Select files...** to populate multiple rows at once from a file selection dialog.
3. Set output file paths per row, or use **Autofill > Fill with parameter values** to auto-generate output filenames from input names.
4. Check **Load layers on completion** to automatically add all outputs to the project.
5. Click **Run** to execute all rows sequentially. A progress log appears; failed rows are flagged without stopping remaining runs.

**Tip:** In the batch dialog, you can select a subset of rows and click **Run Selected** (Read the screenshot `fig12.png` in this directory — it shows the algorithm/processing icon for running only checked rows) to re-run or test specific entries without re-running the entire batch.
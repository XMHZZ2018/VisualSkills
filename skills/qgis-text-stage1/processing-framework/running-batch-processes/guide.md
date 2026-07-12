The markdown has no accompanying image files — just figure captions. I have enough from the text to write the guide.

# Running Batch Processes (QGIS 3.44)

Any algorithm in the Processing Toolbox — including custom models — can run as a batch process, meaning you feed it multiple inputs and it executes once per row without you babysitting each run.

To kick one off, right-click any algorithm in the **Processing Toolbox** and choose **Execute as Batch Process**. Alternatively, if you already have an algorithm's dialog open, hit **Run as Batch Process…** at the bottom.

You'll get a table where each row is one execution and each column is a parameter. The toolbar at the top lets you add or remove rows, toggle advanced parameters, and save/load the configuration as a `.JSON` file for reuse later.

The real power is in the **Autofill…** menu at the top of each column. **Fill Down** copies the first row's value everywhere. **Calculate by Expression…** lets you derive values using QGIS expressions — you can reference other columns as variables (e.g., `@DISTANCE`, `@INPUT`). **Add Values by Expression…** generates new rows from an array expression like `generate_series(100, 1000, 50)`.

For file/layer inputs, the autofill menu also offers **Add Files by Pattern…** (e.g., `*.shp` in a folder), **Select Files…**, **Add All Files from a Directory…**, or **Select from Open Layers…**.

Outputs can be left blank (skipped), saved as temporary layers, written to files, or stored as tables in a GeoPackage. For file outputs, choosing a path triggers an auto-complete dialog offering **Fill with numbers** (appends incremental suffixes) or **Fill with parameter values** (appends a column's value to the filename).

Tick **Load layers on completion** at the bottom if you want results added to your project automatically. When everything looks right, click **Run** — the Log panel shows progress for the entire batch.

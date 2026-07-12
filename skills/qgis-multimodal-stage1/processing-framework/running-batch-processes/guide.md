# Running Batch Processes (QGIS 3.44)

Any algorithm in the Processing Toolbox — including custom models — can be run as a batch process. Instead of feeding it one set of inputs and clicking Run, you give it a whole table of inputs and let it churn through them all in one go. Great for repetitive tasks like buffering dozens of layers or clipping a stack of rasters.

To kick things off, right-click any algorithm in the **Processing Toolbox** and choose **Execute as Batch Process**. Alternatively, if you already have the algorithm's dialog open, hit the **Run as Batch Process…** button at the bottom.

See `fig01.png`.

The batch interface presents a table where each row is one execution and each column is a parameter. By default you get two rows — the top row holds **Autofill…** menus, and the second row is your first real entry. Add more rows with the **Add row** button in the toolbar. You can also save and load the entire configuration as a `.JSON` file for reuse later.

See `fig02.png`.

Filling the table cell by cell works, but the **Autofill…** drop-downs are where the real power lives. **Fill Down** copies the first row's value to every row below. **Calculate by Expression…** lets you write a QGIS expression that references other column values as variables — for example, `CASE WHEN @DISTANCE > 20 THEN 12 ELSE 8 END` to vary segment counts by buffer distance. **Add Values by Expression…** generates new rows from an array expression like `generate_series(100, 1000, 50)`.

For file or layer parameters you get extra autofill options: **Add Files by Pattern…** (e.g., `*.shp` in a folder), **Select Files…** individually, **Add All Files from a Directory…**, or **Select from Open Layers…** in your current project.

Outputs follow the same logic. Leave a cell blank to skip output, type a name and choose **Create Temporary Layer** from the **…** drop-down for an in-memory result, or pick **Select File/Folder…** to write to disk. When saving to file, a secondary dialog offers auto-naming: append incrementing numbers or append a parameter value from the same row so each output is named after its input.

For database outputs, paste an OGR connection string directly — something like `ogr:dbname='C:/Path/To/File.gpkg' table="output_table" (geom)` — and use **Calculate by Expression…** to vary the table name per row.

Once everything looks right, tick **Load layers on completion** if you want results added to your map, then click **Run**. The **Log** panel shows progress for each iteration, and a global progress bar tracks the overall batch.

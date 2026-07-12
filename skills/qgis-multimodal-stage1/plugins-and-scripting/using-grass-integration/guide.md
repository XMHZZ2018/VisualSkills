# Using GRASS GIS Integration (QGIS 3.44)

GRASS GIS lives inside QGIS as both a data provider and a plugin. The provider lets you browse and load GRASS layers straight from the Browser panel — just navigate to your `grassdata` folder, expand a LOCATION and MAPSET, and double-click or drag any raster or vector layer onto the canvas. If you don't see the GRASS icon in the browser tree, confirm the provider is loaded under **Help > About > Providers**.

To unlock the full editing and analysis toolkit, enable the plugin via **Plugins > Manage and Install Plugins…**, tick **GRASS**, and click **OK**. This adds a **Plugins > GRASS** menu with items like **Open Mapset**, **New Mapset**, **Open GRASS Tools**, and **Display Current GRASS Region**.

Before doing any analysis you need an open mapset — right-click a mapset in the Browser and choose **Open mapset**, or use the **Open MAPSET** toolbar button and walk through the wizard. GRASS organizes data hierarchically: a GISDBASE folder holds LOCATIONs (each with its own CRS), and each LOCATION holds MAPSETs that act as workspaces. You can only write to a MAPSET you own.

See `fig01.png`.

Importing data is as simple as dragging a layer from the Browser onto a target mapset — QGIS handles reprojection automatically. For the classic approach, open the GRASS Toolbox and use `r.in.gdal` for rasters or `v.in.ogr` for vectors, set your input file and output name, then click **Run** and watch the Output tab for "Successfully finished."

GRASS uses a topological vector model. Areas aren't closed polygons — they're boundaries plus a centroid that carries the attributes. To digitize a polygon, first draw the boundary with **New Boundary**, then drop a **New Centroid** inside it. All geometry types (points, lines, boundaries, centroids) can coexist in a single vector map, organized into numbered "layers."

When editing a GRASS vector layer, changes are written immediately to disk — there's no deferred save. You still get undo/redo and can discard all changes on close, but be aware that the map file updates in real time. Make sure your canvas CRS matches the layer's CRS so snapping produces exact coordinate matches, which is critical for clean topology.

The **GRASS region** defines the spatial extent and resolution for raster operations (vectors aren't affected). Toggle its visibility with **Display Current GRASS Region**, and adjust bounds in the Region tab of the GRASS Tools dock or interactively by dragging a rectangle on the canvas.

The GRASS Toolbox (opened via the toolbar icon) exposes roughly 200 modules organized in a searchable tree. Pick a module, fill in the Options tab, click **Run**, and monitor progress in the Output tab. Each module also has a Manual tab with full HTML documentation. Click **View Output** after a successful run to immediately add results to your map.

See `fig02.png`.

A quick example: to generate contour lines, open **Raster > Surface Management > Generate vector contour lines** (`r.contour`), set your input DEM, choose an interval (e.g., 100 meters), name the output, and run. Smooth the result afterward with `v.generalize` using Chaiken's algorithm for cleaner cartographic output.

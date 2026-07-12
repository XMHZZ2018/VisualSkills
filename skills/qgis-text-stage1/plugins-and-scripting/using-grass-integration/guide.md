The markdown doesn't reference any inline images — it only has figure captions. I have all the information needed from the text content to write the guide.

# Using GRASS GIS Integration (QGIS 3.44)

GRASS GIS lives inside QGIS as both a data provider and a plugin. The provider lets you browse and load GRASS layers directly from the Browser panel. The plugin unlocks 400+ analysis modules, vector editing, and region management.

**Data structure:** GRASS organizes everything under a GISDBASE folder (commonly `grassdata`). Inside that you have LOCATIONs (each with one CRS) and MAPSETs (workspaces within a location). You can only write to MAPSETs you own.

To load GRASS data, just expand a GRASS location in the Browser panel and double-click or drag any raster/vector layer onto your canvas. If you don't see the GRASS icon, check **Help > About > Providers** to confirm the GRASS provider is loaded.

Importing external data is drag-and-drop: navigate to your target mapset in the Browser, find the layer you want to import, and drop it onto the mapset. QGIS handles reprojection automatically. For traditional imports, open the GRASS Toolbox and use `r.in.gdal` for rasters or `v.in.ogr` for vectors.

Enable the plugin via **Plugins > Manage and Install Plugins…**, then tick **GRASS**. Once active, open a mapset by right-clicking it in the Browser and choosing **Open mapset**. This unlocks the GRASS toolbar and **Plugins > GRASS** menu — giving you **Open GRASS Tools**, **Display Current GRASS Region**, and mapset management.

The GRASS region defines the spatial extent and resolution for all raster operations. Toggle its visibility with **Display current GRASS region** on the toolbar, and adjust bounds in the Region tab of the GRASS Tools dock or interactively by dragging on the canvas.

GRASS uses a topological vector model — polygons are built from shared boundaries plus a centroid, not closed rings. When digitizing, draw boundaries first, then drop a centroid inside to create an area. Standard QGIS sketching tools work, but edits save immediately to the GRASS map (undo/redo still available until you close editing). Keep your canvas CRS matching the layer CRS for accurate snapping.

The GRASS Toolbox (**Open GRASS Tools** button) organizes ~200 modules into a searchable tree. Pick a module, fill in the Options tab, click **Run**, and watch progress in the Output tab. Hit **View Output** to add results straight to your map. For advanced flags not shown in the GUI, drop into the GRASS shell tab and run commands directly.

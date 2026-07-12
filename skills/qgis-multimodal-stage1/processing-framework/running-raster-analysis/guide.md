# Running Raster Analysis Algorithms (QGIS 3.44)

All raster terrain and analysis tools live in the QGIS native algorithm provider, so they work out of the box with no extra plugins or configuration. Open the Processing Toolbox via **Processing > Toolbox** (or press Ctrl+Alt+T) and expand the **Raster terrain analysis** group to find the core surface tools: **Hillshade**, **Slope**, **Aspect**, **Relief**, **Ruggedness index**, and more.

To generate a hillshade, double-click **Hillshade** in the toolbox. Point it at your DEM layer, then set the light azimuth (default 300°) and vertical angle (default 40°). The Z factor lets you exaggerate elevation if your horizontal and vertical units differ — bump it up for flat terrain so the shading actually pops. Hit **Run** and the output loads as a new grayscale layer.

**Slope** works the same way: feed it a DEM and it produces a raster where each cell holds the steepness in degrees. **Aspect** gives you compass direction of the downhill face (0–360°), handy for solar exposure analysis. Both accept the same Z factor parameter as Hillshade.

For a color-coded elevation overview, try **Relief** — it auto-generates color bands across your elevation range, or you can define custom classes. **Ruggedness index** quantifies how rough the terrain is cell-by-cell, useful for habitat or trafficability studies.

Beyond terrain, the **Raster analysis** group holds the **Raster calculator** for band math expressions, **Reclassify by table** for binning continuous values into classes, and **Zonal statistics** for summarizing raster values within polygon zones. **Cell statistics** lets you compute per-cell stats (mean, max, min, etc.) across a stack of aligned rasters.

Every algorithm dialog also exposes a **Run as Batch Process** button at the bottom, so you can queue the same tool across multiple input layers in one go — great for producing slope, aspect, and hillshade from the same DEM in a single batch.

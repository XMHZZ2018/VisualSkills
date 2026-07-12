# Running Raster Analysis Algorithms (QGIS 3.44)

All raster terrain tools live in the Processing Toolbox under **QGIS algorithms > Raster terrain analysis**. Open it via **Processing > Toolbox** if it's not already docked. These algorithms work out of the box with no extra configuration — they use the native QGIS API.

To generate a **Hillshade**, search "Hillshade" in the toolbox or navigate to **Raster terrain analysis > Hillshade**. Point it at your DEM layer, set the light azimuth and altitude angles, and hit **Run**. The result gives you that familiar shaded-relief look, perfect for visual context under other layers.

**Slope** and **Aspect** work the same way — select your elevation raster as input, and each produces a new raster. Slope outputs steepness in degrees (or percent), while Aspect gives compass direction of the downhill face (0–360°). Both are under **Raster terrain analysis > Slope** and **Raster terrain analysis > Aspect**.

For a color-coded elevation visualization, try **Relief** — it automatically assigns color bands to elevation ranges. **Ruggedness Index** quantifies terrain variability per cell, useful for habitat or erosion studies. And **Fill sinks (Wang & Liu)** preprocesses your DEM for hydrological analysis by eliminating depressions.

If you need custom math across rasters, use **Raster analysis > Raster calculator** — write expressions referencing any loaded raster bands. For statistics, **Raster layer statistics** and **Zonal statistics** summarize values globally or within polygon zones.

All tools accept output as a temporary layer or a file path. Chain them together using the **Processing > Graphical Modeler** for repeatable workflows.

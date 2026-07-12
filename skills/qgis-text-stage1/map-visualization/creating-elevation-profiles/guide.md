# Creating Elevation Profiles (QGIS 3.44)

The Elevation Profile view gives you a cross-section side view of your terrain and features along any line you draw. It works with raster DEMs, vector layers, mesh, and point cloud data.

Open the panel from **View > Elevation Profile**. You can have multiple profile views open simultaneously — dock them, stack them, or float them wherever you like.

To draw your profile line, grab **Capture Curve** from the panel toolbar, then left-click vertices on the map canvas and right-click to finish. Alternatively, use **Capture Curve From Feature** to trace an existing line feature instead of drawing freehand. All standard sketching aids (snapping, tracing, advanced digitizing) work here.

Once you have a line, click **Show Layer Tree** in the profile panel to see which layers are included. Not every project layer appears automatically — click **Add Layers** to pull in additional ones. Toggle visibility for the layers you care about, then double-click any layer to open its **Elevation** properties tab where you control how it renders in the profile (band selection for rasters, attribute mapping for vectors, etc.).

Under the **Options** menu, set a **Tolerance** value to widen the capture buffer around your profile line — useful for pulling in nearby point cloud or vector features that don't sit exactly on the line.

You can nudge the entire profile line left or right with **Nudge Left** (`Ctrl+Alt+,`) and **Nudge Right** (`Ctrl+Alt+.`) to find the best cross-section without redrawing. Use **Enable Snapping** for precise coordinate readouts and **Measure Distances** to get horizontal distance, elevation difference, and slope distance between any two points on the plot.

When you're happy with the result, export via **Export As PDF** for vector-quality output, **Export As Image** for raster formats, or **Export Results** to save the profile geometry as DXF, CSV, GeoPackage, or Shapefile — with options for 3D features, 2D profile lines, or a distance/elevation table.

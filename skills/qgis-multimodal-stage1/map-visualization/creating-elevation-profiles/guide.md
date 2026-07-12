# Creating Elevation Profiles (QGIS 3.44)

The Elevation Profile view gives you a side-view cross-section of your terrain and features along any line you draw. It works with raster DEMs, vector layers, mesh data, and point clouds — both 2D and 3D.

Open the panel from **View > Elevation Profile**. You can have multiple profile views open at once, docked or floating however you like.

See `fig01.png`.

To generate a profile, you need to define a line across the map. Grab **Capture Curve** from the panel toolbar, then left-click to place vertices on the map canvas and right-click to finish. Alternatively, use **Capture Curve From Feature** to trace an existing line feature — just click it on the map. All the usual digitizing aids (snapping, tracing, the advanced digitizing panel) work here.

Once you have a line, open the layer tree by clicking **Show Layer Tree** in the panel. Not every project layer appears automatically — click **Add Layers** to pull in additional ones that have elevation data. You can also hold `Ctrl` and drag layers from the main Layers panel directly into the profile's layer tree. Toggle visibility for the layers you care about; only checked layers render in the profile.

Double-click any layer in the tree (or right-click > **Properties**) to open its **Elevation** properties tab. This is where you configure how that layer's data maps to elevation — band selection for rasters, Z attribute for vectors, and so on. The profile plot updates live as you configure layers.

Under the **Options** dropdown, set the **Tolerance** to control how wide a buffer around your profile line is used to capture nearby features. A larger tolerance pulls in more surrounding points and polygons. You can also enable **Show Subsections Indicator** to mark vertex positions along the profile with vertical lines.

For navigation, use **Pan** (or hold `Space`), **Zoom X Axis** to stretch horizontally without changing the vertical scale, or **Zoom** for proportional zoom. **Zoom Full** resets to the entire profile extent. Enable **Snapping** for precise coordinate retrieval, and use **Measure Distances** to get horizontal distance, elevation difference, and total distance between two clicked points.

The **Nudge Left** / **Nudge Right** buttons (`Ctrl+Alt+,` and `Ctrl+Alt+.`) shift your profile line sideways by the tolerance distance — handy for finding the best cross-section without redrawing.

When you're happy with the result, export via the toolbar: **Export As PDF** for vector-quality output with configurable page size and axis intervals, **Export As Image** for raster formats, or **Export Results** to save the profile as 3D features, 2D profile geometry, or a distance/elevation table in formats like GeoPackage, DXF, or CSV.

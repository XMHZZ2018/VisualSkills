# Working with Mesh Layers (QGIS 3.44)

A mesh layer is an unstructured grid of vertices, edges, and faces (triangles or quads) that can carry temporal datasets — think hydrodynamic model output, wind fields, or bathymetry. QGIS reads these via MDAL drivers, supporting formats like GRIB, NetCDF, XMDF, and more.

To load one, open **Layer > Data Source Manager** and switch to the **Mesh** tab. Browse to your file and hit **Add**. Once loaded, double-click the layer (or **Layer > Layer Properties…**) to configure it.

Under **Symbology > Datasets**, pick which scalar or vector group to display — click the icon next to a dataset name to activate it. The **Contours** tab lets you set opacity, choose a color ramp shader, adjust min/max values, and control resampling between vertices and faces. For vector data (currents, wind), flip to the **Vectors** tab and choose from Arrows, Streamlines, Traces, or Wind Barbs — each with its own sizing and coloring options.

The **Temporal** tab ties your mesh to QGIS's temporal controller so you can animate timesteps. Set the reference time and matching method, then drag the time slider on the map canvas. For 3D layered meshes, use **Symbology > Stacked mesh averaging method** to flatten volume data onto 2D faces.

To edit geometry, toggle **Toggle Editing** on the Sketching toolbar. The **Digitize Mesh Elements** tool lets you add vertices (double-click) and faces (click vertices then right-click to close). Select elements with a rectangle, polygon, or expression, then move, transform coordinates via **Transform Vertices Coordinates**, or delete with `Ctrl+Del`. Green rubber-band previews mean valid geometry; red means fix it before confirming.

The **Force by Selected Geometries** tool lets you imprint break lines (like riverbanks) onto the mesh — pick a vector feature or draw a line, and faces get split along it. After heavy edits, run **Mesh > Reindex Faces and Vertices** to clean up gaps in the index.

For derived analysis, open **Mesh > Mesh Calculator**. Double-click dataset groups to build expressions with arithmetic, statistics (`min`, `max`, `sum`), and conditionals. Output can be written to a new file or kept as a virtual on-the-fly group attached to the layer. Set spatial and temporal extents to limit the calculation scope, and check **Add result to project** to see results immediately.

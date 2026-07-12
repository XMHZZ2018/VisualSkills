# Working with Mesh Layers (QGIS 3.44)

A mesh is an unstructured grid of vertices, edges, and faces (triangles or quads) that carries time-varying datasets — think water depth, wind speed, or wave direction stored at each node across multiple timesteps. QGIS reads mesh data via the MDAL library, supporting formats like NetCDF, GRIB, XMDF, and more.

To load a mesh layer, open **Layer > Data Source Manager** and switch to the **Mesh** tab. Browse to your file, hit **Add**, and the layer appears in the Layers panel. Once loaded, double-click the layer (or **Layer > Layer Properties**) to access all configuration.

Under the **Symbology > Datasets** tab, pick which dataset groups are active — click the scalar or vector icon beside each group name to control what gets rendered on the canvas. Scalar data shows as coloured contours; vector data renders as arrows, streamlines, traces, or wind barbs depending on what you choose in the **Vectors** tab.

See `fig01.png`.

In the **Contours** tab, adjust opacity, set a custom min/max range, pick a resampling method (Neighbour average smooths face-centred data onto vertices), and classify values with a colour ramp shader. For vectors, the **Vectors** tab lets you control arrow length scaling, streamline seeding, line width, and colouring method — single colour or magnitude-based ramp.

The **Temporal** tab wires the layer into QGIS's temporal navigation controller. Set or accept the reference time, choose a matching method (closest before, or closest overall), and adjust the time unit so playback speed aligns with other layers in your project.

To inspect values interactively, grab the **Identify Features** tool from the Attributes toolbar and click any mesh element — the results panel shows active dataset values, geometry coordinates, and snapped vertex/edge info.

Editing starts with **Toggle Editing** on the Sketching toolbar. The **Digitize Mesh Elements** tool lets you add vertices (double-click) and faces (click vertices sequentially, right-click to finish). A green rubberband means the face is valid; red means it self-intersects or overlaps. Use `Ctrl+Del` to remove selected vertices and fill holes, or `Shift+Del` to strip faces while keeping vertices.

See `fig02.png`.

The **Transform Vertices Coordinates** tool is handy for bulk Z edits — select vertices, open the dialog, write an expression or literal value for X/Y/Z, preview (green = valid), then apply. For constraining edges along a river bank or road, the **Force by Selected Geometries** tool splits existing faces along a drawn or selected line feature, with options to interpolate Z from the mesh or from the forcing geometry.

Finally, the **Mesh Calculator** (**Mesh > Mesh Calculator**) lets you run arithmetic and logical expressions across dataset groups to produce derived outputs — either written to disk or kept as a virtual on-the-fly group in your project. Set spatial and temporal extents to limit the computation scope, then build your expression from the operators panel.

See `fig03.png`.

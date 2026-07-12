# Measuring Distances and Areas (QGIS 3.44)

QGIS gives you four ways to measure geometries: interactive tools on the map canvas, the **Field Calculator**, the **Identify Features** tool, and **Vector > Geometry Tools > Export/Add Geometry Columns**. This guide focuses on the interactive approach — the quickest way to get a number without building an expression or running a processing tool.

By default, QGIS measures ellipsoidally using the ellipsoid set in **Project > Properties… > General**. If you need flat/planimetric measurements instead, set the measurement ellipsoid to "None/Planimetric" in that same dialog.

To start measuring, click the **Measure** icon on the Attributes toolbar. The small down arrow next to it lets you switch between **Measure Line**, **Measure Area**, **Measure Bearing**, and **Measure Angle**. The default unit comes from your project properties, but you can change it on the fly using the drop-down in the measure dialog.

For line measurement, left-click to place points on the map — each segment length and a running total appear in the Measure window along with coordinates. Right-click to finish. You can toggle between **Cartesian** and **Ellipsoidal** calculation right in the dialog, and the **Copy** button grabs all coordinates and distances to the clipboard at once.

See `fig01.png`.

Area measurement works the same way: left-click vertices to draw a polygon, right-click to close it, and the accumulated area appears with a unit selector so you can flip between square meters, hectares, etc.

See `fig02.png`.

For bearings, click a start point then move the cursor to a second point — the bearing displays in a popup. For angles, click to define the first ray, then click again to form the angle; the result appears immediately.

If you need your clicks to snap to an existing feature, configure snapping in the digitizing settings first — the measure tools honour those tolerances. Clicking **Configuration** at the bottom of any measure dialog jumps you to **Settings > Options > Map Tools**, where you can change the rubberband color, decimal precision, and preferred units.

# Measuring Distances and Areas (QGIS 3.44)

The measure tools live in the **Attributes Toolbar**. Click the drop-down arrow next to the ruler icon to switch between **Measure Line**, **Measure Area**, **Measure Bearing**, and **Measure Angle**.

To measure a distance, select **Measure Line** and click points on the map — each segment length and a running total appear in the Measure dialog. Right-click to finish. You can toggle between **Cartesian** and **Ellipsoidal** calculation directly in the dialog, and change units (meters, feet, etc.) from the drop-down next to the total.

For areas, choose **Measure Area** and click vertices to outline your polygon. The accumulated area updates live. Right-click to close the shape and see the final result.

**Measure Bearing** takes just two clicks — an origin and a direction — and reports the azimuth in degrees. **Measure Angle** needs three clicks (two segments) and shows the angle between them.

By default, measurements are ellipsoidal using the ellipsoid set in **Project › Properties… › General**. To get flat/planimetric results instead, set the measurement ellipsoid to "None/Planimetric" in that same dialog.

All measure tools respect your project's snapping settings, so enable snapping on a layer if you want clicks to lock precisely onto existing features.

Hit **New** in the Measure dialog to start a fresh measurement without closing the tool, or **Copy** to send all coordinates and segment values to your clipboard. The **Configuration** button jumps to **Settings › Options › Map Tools** where you control rubber-band color, decimal precision, and default units.

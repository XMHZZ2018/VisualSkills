# Using the Temporal Controller (QGIS 3.44)

The Temporal Controller lets you filter and animate map layers based on time. Before it does anything useful, your layers need temporal properties enabled — open a layer's properties and configure its temporal tab (vectors filter by attribute time values, rasters show/hide by time range, mesh layers animate dataset groups). A small clock icon appears next to temporally-enabled layers in the Layers panel.

Open the controller via the **Temporal Controller Panel** button on the Map Navigation toolbar, or through **View › Panels › Temporal controller panel**. The panel offers four modes: **Turn off temporal navigation** (renders everything normally), **Fixed range** (shows only data overlapping a single time window), **Animated temporal navigation** (steps through time frame by frame), and **Animated movie** (advances frames without time-filtering).

To build an animation, activate **Animated temporal navigation** mode. Set the **Animation range** start and end — click the refresh button to auto-populate from all time-enabled layers, a preset project range, or a single layer's extent. Then choose a **Step** size (seconds through centuries, or `source timestamps` to jump between irregular available dates like a WMS-T service). Hit **Play** to watch QGIS render each frame. You can also drag the time slider manually, or scroll horizontally over the map canvas to scrub through time. Check **Loop** to repeat continuously.

Under the **Settings** gear icon, adjust **Frames rate** (steps per second) and optionally enable **Cumulative range** — this keeps the start date fixed while advancing only the end date, so data accumulates rather than sliding as a window.

To export, click **Export Animation**. Set a filename **Template** (use `####` for the frame number sequence), pick an **Output directory**, and adjust extent/resolution under **Map Settings**. Under **Temporal Settings** you can override the range and step. The result is a numbered image sequence you can stitch into video with any editor.

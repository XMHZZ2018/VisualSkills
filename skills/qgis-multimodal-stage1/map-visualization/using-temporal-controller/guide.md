# Using the Temporal Controller (QGIS 3.44)

QGIS can filter and animate map layers based on time. The idea is simple: you configure layers with temporal properties (a date field, a time range, etc.), then use the Temporal Controller to scrub through time or play an animation that shows only the data relevant to each moment.

To get started, your layers need dynamic temporal properties enabled. For vector layers, this typically means filtering features by a date/time attribute; for raster and mesh layers, it controls which time-slice is displayed. When a layer has temporal settings active, a small clock icon appears next to it in the **Layers** panel — click that icon anytime to adjust the configuration.

Open the Temporal Controller panel from the **Map Navigation** toolbar (the clock icon) or via **View > Panels > Temporal controller panel**. The panel offers four modes: off (no filtering), fixed range (static time window), animated navigation (stepped playback through a range), and movie mode (frame-based progression without time filtering).

See `fig01.png`.

For a typical animation, switch to **Animated temporal navigation** mode. Set the **Animation range** start and end — the refresh button lets you auto-fill this from all temporal layers, the project range, or a single layer's extent. Then choose a **Step** size (anything from seconds to centuries). There's also a "source timestamps" option that jumps between each layer's actual available times, which is handy for irregularly-spaced data like WMS-T services.

Hit **Play** and QGIS steps through each frame, rendering only the features or datasets that overlap the current time window. You can also drag the time slider manually, or scroll horizontally with the mouse wheel over the map canvas to scrub back and forth. Check **Loop** to repeat the animation continuously.

Under the **Settings** gear icon you'll find the frame rate (steps per second) and a **Cumulative range** option. Cumulative range keeps the start date fixed while advancing only the end date — useful when you want data to accumulate on the map rather than slide past in a moving window.

When you're happy with the animation, click **Export animation** to save it as a numbered image sequence. You specify a filename template (use `####` for the frame number), an output directory, the spatial extent and resolution, and can override the time range and step for the export. Combine the frames afterward in any video editor.

See `fig02.png`.

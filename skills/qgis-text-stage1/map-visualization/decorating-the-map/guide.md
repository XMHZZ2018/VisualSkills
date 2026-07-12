# Decorating the Map (QGIS 3.44)

All map decorations live under **View > Decorations**. Each one overlays cartographic furniture directly onto the map canvas — no print layout required. Decorations are saved with your project file and restored automatically next session.

**Grid** (**View > Decorations > Grid…**) draws coordinate lines or markers across the canvas. Check **Enable Grid**, pick Line or Marker type, and set X/Y intervals in map units. You can auto-calculate spacing from canvas extents or active raster resolution. Enable **Draw Annotations** to label grid lines, choosing direction (horizontal, vertical, or boundary-following) and font.

**Title Label** (**View > Decorations > Title Label…**) places a text banner on the canvas. Type your title — or build a dynamic one with **Insert or Edit an Expression…** — then set font, background bar color, and placement (default is Top Center). Adjust margin from edge in mm, px, or percentage.

**Copyright Label** (**View > Decorations > Copyright Label…**) works identically to the title but defaults to Bottom Right placement. Use it for attribution text like `© Organisation 2024`; expressions are supported here too.

**North Arrow** (**View > Decorations > North Arrow…**) drops a compass indicator on the canvas. Set fill/outline color, size in mm, and optionally load a custom SVG. Leave **Automatic** checked for the angle and QGIS will derive true north from your project CRS.

**Scale Bar** (**View > Decorations > Scale Bar…**) adds a distance reference that respects your project's distance units. Choose a style (Tick Down, Single Box, etc.), set bar size, pick fill/outline colors and font. Check **Automatically snap to round number on resize** to keep labels clean as you zoom.

**Layout Extents** (**View > Decorations > Layout Extents**) outlines the visible area of every map item in your print layouts as a labeled dotted rectangle — handy for positioning labels without switching to the layout manager.

For all decorations, placement is any corner or center edge, and margin can be fine-tuned in millimeters, pixels, or canvas percentage. Hit **Apply** to preview before committing with **OK**.

# Painting Animation Levels (OpenToonz 1.7)

Every Toonz level drawing is made of **lines** (strokes from scanned or vector art) and **areas** (regions enclosed by closed lines). You paint both using styles stored in the level's palette.

**Filling areas** is the core workflow. Grab the **Fill** tool, set Mode to **Areas**, pick a style from the Palette, and click inside any closed region. If color won't flood into tight corners on raster drawings, bump up the **Fill Depth** value or Shift-click to use the maximum. For vector drawings, outlines can be a single closed vector or several joined vectors — both work.

To paint many areas at once, switch the Fill type to **Rectangular**, **Freehand**, or **Polyline** and drag a selection — everything fully enclosed gets filled. Combine this with the **Selective** option to only hit unpainted areas, which is great for a final cleanup pass. The **Frame Range** option lets you click the same region on a first and last frame, and OpenToonz interpolates the fill across the whole range automatically.

**Painting lines** works similarly: set the Fill tool's Mode to **Lines** and click a stroke. On Toonz Raster levels, clicking paints the entire continuous line sharing that style. For partial recoloring, activate the **Segment** option (splits lines at thickness/direction changes) or use the **Paint Brush** tool set to **Lines** mode and brush over just the section you want.

When areas won't fill because of gaps in the outline, use the **Tape** tool. For vector drawings, set Mode to **Endpoint to Endpoint** (or **Endpoint to Line**) and drag across the gap. For raster drawings, just click in the viewer — it auto-closes gaps within the set **Distance** and **Angle** thresholds. Enable **View > Gap Check** to preview which gaps the Tape tool can currently detect.

Use **View > Transparency Check** or **Paint Check** to verify coverage — unpainted slivers along antialiased edges become obvious. The **Onion Skin** option on the Fill tool lets you pick styles directly from a previously painted frame and apply them to the current drawing in one click-and-release gesture.

**Match lines** let you merge drawings from two columns. Expose the base level and the match-line level side by side, select both column headers, then choose **Xsheet > Apply Match Lines…**. You can preserve original ink styles, force a single ink, or let OpenToonz merge matching indexes automatically.

For shadow/highlight lines that should auto-match their adjacent fill color, select the line's style in the Palette, open the **Style Editor > Settings** page, and enable **Autopaint for Lines**. Now whenever you fill an area bordered by that style, the line takes on the area's color.

**Color models** serve as your painting reference. Load one via **File > Load Color Model…** (or drag an image into the Color Model viewer). You can click directly on the color model to pick styles without switching tools. Store a color model alongside a Studio Palette entry and it auto-loads whenever that palette is assigned to a level.

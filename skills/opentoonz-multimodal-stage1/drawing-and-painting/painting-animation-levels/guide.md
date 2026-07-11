# Painting Animation Levels (OpenToonz 1.7)

Every Toonz drawing is made of **lines** (the strokes) and **areas** (closed regions bounded by those lines). You paint both using styles from the level's palette, and nothing is saved until you hit **File > Save All**.

The main workhorse is the **Fill** tool. Select it, pick a style in the palette, and click inside any closed area to flood it. Set **Mode** to **Areas**, **Lines**, or **Lines and Areas** depending on what you're targeting. The **Type** option controls how you designate what gets filled: **Normal** (single click), **Rectangular** (drag a box), **Freehand** (lasso), or **Polyline** (click a polygon). Combine **Rectangular** with **Selective** to batch-fill all unpainted areas in one sweep — great for large flat-color passes.

For Toonz Raster levels, the **Fill Depth** slider controls how aggressively color bleeds through antialiased edges. A low value respects even thin semitransparent pixels; hold Shift-click to temporarily use the maximum value. The **Segment** option lets you target a portion of a continuous line where the stroke changes thickness or direction.

The **Frame Range** option is a huge time-saver: click a region on the first frame, then click the same region on the last frame, and OpenToonz interpolates the fill across all frames in between. You can Shift-click intermediate frames to add keypoints for better accuracy.

The **Paint Brush** tool works like a freehand brush that only colors inside existing lines or areas (Toonz Raster only). Set **Mode** to **Lines** and adjust **Size** to repaint specific line segments by hand — useful for partial recoloring the Fill tool can't easily reach.

When fill floods everywhere or nowhere, the outline probably has gaps. Use the **Tape** tool to close them. For vector drawings, set **Mode** to **Endpoint to Endpoint** (or **Endpoint to Line**) and drag between the open ends. For raster drawings, just click — the tool auto-detects and closes nearby gaps based on the **Distance** and **Angle** thresholds. Turn on **View > Gap Check** to see detected gaps highlighted in magenta before committing.

To paint lines themselves, switch the Fill tool's mode to **Lines** and click a stroke. On raster levels, the fill affects the entire continuous line sharing that style; on vector levels, it targets one stroke at a time. Alternatively, select vector strokes with the **Selection** tool and simply pick a new palette style — done.

**Match lines** let you merge a secondary level (shadow outlines, ink variants) onto a primary level. Expose both in adjacent columns, select both column headers, then choose **Xsheet > Apply Match Lines…**. The dialog lets you control ink usage and line prevalence (0 = match lines behind, 100 = on top). Delete them later with **Xsheet > Delete Match Lines** if needed.

See `fig01.png`.

The **Autopaint for Lines** feature (found in the Style Editor's **Settings** page) marks a style so that whenever you fill an area bounded by that style's lines, the lines automatically adopt the area's color. Perfect for shadow or highlight outlines that should match their fill.

For color reference while painting, load a model via **File > Load Color Model…** (or drag an image into the Color Model viewer). Click any region in the color model to instantly pick its style — no need to hunt through the palette. If the model is a multi-frame level, scrub through frames for different character views (front, back, three-quarter).

See `fig02.png`.

You can permanently associate a color model with a palette stored in the **Studio Palette**, so it loads automatically whenever you assign that palette to a new level.

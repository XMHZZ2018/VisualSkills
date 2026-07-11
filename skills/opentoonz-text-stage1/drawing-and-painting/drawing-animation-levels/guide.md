Here's the guide:

# Drawing Animation Levels (OpenToonz 1.7)

OpenToonz supports three level types: **Toonz Vector** (PLI, resolution-independent), **Toonz Raster** (TLV, bitmap with palette), and **Raster** (TIF sequences). Set your default via **File > Preferences… > Drawing** under **Default Level Type**.

To create a new level, select an empty Xsheet/Timeline cell and choose **Level > New > New Level…** — pick your type, set frame count, step, and increment, then hit OK. Alternatively, set **Autocreation** to **Enabled** in Preferences and just start drawing on an empty cell; a level is created automatically. The **Use Xsheet as Animation Sheet** autocreation mode mimics traditional workflow — keys first, then breakdowns and inbetweens, with drawing numbers taken from the scene frame.

The **Brush** tool supports pressure sensitivity for variable-thickness strokes. Adjust **Size Min/Max** with Ctrl+Alt drag (horizontal for max, vertical for min). The **Geometric** tool draws rectangles, ellipses, circles, polygons, polylines, and arcs with constant thickness. Both tools offer **Snap**, **Pencil** mode, and **Cap/Join** options for vector work.

For vector animation, duplicate a drawing via **Cells > Duplicate Drawing**, then reshape it with the **Pinch**, **Pump**, **Bender**, or **Iron** tools — paint fills follow shape changes automatically. The **Inbetween** command interpolates between two key drawings: select a frame range in the Level Strip, click the vertical **INBETWEEN** bar, choose an easing (Linear, Ease In, Ease Out, Ease In/Out), and confirm.

**Onion Skin** lets you see adjacent frames as ghosted overlays. Click the diamond markers left of the Xsheet frame column for relative mode (moves with the cursor), or the ghosted markers further left for fixed mode (stays on a specific frame). Customize transparency and tinting under **File > Preferences… > Onion Skin**. Right-click the viewer and choose **Extend Onion Skin to Scene** to see all columns, or **Limit Onion Skin to Level** for just the active one.

**Shift and Trace** simulates a light table for inbetweening. Enable **View > Shift and Trace** on the target frame, then activate **View > Edit Shift** to reposition the previous/next reference drawings — drag inside the bounding box to move, outside to rotate, or Ctrl-drag to create a path-of-action line that aligns both references automatically. Toggle **View > No Shift** to compare, and **View > Reset Shift** to start over.

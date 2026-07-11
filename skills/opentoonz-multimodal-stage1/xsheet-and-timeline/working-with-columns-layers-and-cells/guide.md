# Working with Columns, Layers, and Cells (OpenToonz 1.7)

The Xsheet and Timeline are two views of the same data. The Xsheet reads vertically — columns hold layers, rows hold frames. The Timeline flips this horizontally — layers stack bottom-to-top, frames run left-to-right. Everything you can do in one, you can do in the other.

Columns stack left-to-right in the Xsheet (bottom-to-top in the Timeline), so what's further right (or higher) composites on top. Cells are color-coded by level type: dark yellow for Toonz Vector, green for Toonz Raster, light blue for raster images, and violet for Sub-Xsheets.

See `fig01.png`.

Each column header gives you quick toggles: the **Render** toggle includes/excludes it from final output, the **Camera Stand** toggle shows/hides it in the viewer, and the **Lock** toggle prevents accidental edits. Click the small triangle for **Opacity** and **Color Filter** settings — handy for dimming reference layers while you animate. Double-click the column name to rename it.

To select columns, click a header; Ctrl-click (Cmd on Mac) to add more, or Shift-click to extend. Drag any selected header to reorder. Right-click a header for **Cut**, **Copy**, **Paste**, **Insert**, or **Delete** operations — these shift neighbouring columns as you'd expect. You can also **Fold** columns you're not actively working on to save screen space.

Cells reference drawings — they don't contain them. Changing a drawing updates every cell that references it. Select cells by clicking and dragging, or click the vertical strip (Xsheet) or horizontal strip (Timeline) beside a level's contiguous run. Standard **Cut/Copy/Paste/Delete/Insert** from the Edit menu all work; pasted cells shift existing content down (or right in Timeline).

The Cells menu offers timing tools: **Step 2/3/4** to hold each drawing for multiple frames, **Each 2/3/4** to thin out a selection, **Reverse** to flip order, **Swing** for a ping-pong cycle, and **Roll Up/Down** to rotate cell contents. The **Smart Fill Handle** — a small tab at the bottom (or right) of your selection — lets you drag to extend progressive sequences or repeat cycles directly in the grid.

When you need to retime a whole section, select your cells and open **Cells > Time Stretch…**. Set a new frame range and the selection scales proportionally — useful for converting between frame rates or adjusting scene pacing.

See `fig02.png`.

To insert or remove a single frame globally (affecting all columns, keys, and FX parameters at once), use **Xsheet > Insert Frame** or **Xsheet > Remove Frame**. This shifts everything downstream, keeping your animation in sync across the board.

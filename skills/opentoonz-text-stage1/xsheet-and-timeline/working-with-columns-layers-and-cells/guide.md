Here's the reference guide:

# Working with Columns, Layers, and Cells (OpenToonz 1.7)

The Xsheet (vertical) and Timeline (horizontal) are two views of the same data. Columns in the Xsheet correspond to layers in the Timeline; rows are frames. Stacking order runs left-to-right in the Xsheet and bottom-to-top in the Timeline — stuff on the right/top renders in front.

Each column/layer header shows a **Name**, a **Render toggle** (include in output), a **Camera Stand toggle** (show/hide in viewer), and a **Lock toggle** (prevent edits). Click the triangle icon to adjust **Opacity** or apply a **Color Filter** for viewing. Double-click the name area to rename a column.

To select columns, click a header; Ctrl/Cmd-click to add more, or Shift-click to extend. Drag selected headers to reorder them. Right-click a header for **Cut**, **Copy**, **Paste**, **Delete**, or **Insert** empty columns. You can also **Fold Column** from that menu to collapse columns you don't need visible, and click the fold marker later to unfold.

Cells hold references to level drawings — editing a drawing updates every cell that points to it. Click-drag across cells to select a range, or click the strip on the left (Xsheet) / top (Timeline) to grab a whole level chunk. Drag that strip to move cells; hold Ctrl/Cmd to duplicate, Shift to insert, or Alt to overwrite at the destination.

The **Cells** menu has handy timing tools: **Reverse**, **Swing**, **Step 2/3/4**, **Each 2/3/4**, **Increase Step**, **Decrease Step**, **Roll Up/Down**, and **Repeat** (loop a selection N times). Use the **Fill Handle** — the small tab at the bottom/right of a selection — to smart-extend or shorten sequences by dragging.

To retime globally, select cells and choose **Cells → Time Stretch…**, set your new frame range, and hit **Stretch**. For whole-scene timing changes, use **Xsheet → Insert Frame** or **Xsheet → Remove Frame** — these shift all columns and any animation keys together.

Sub-Xsheets let you nest an entire scene inside one column. Collapse selected columns via **Xsheet → Collapse**, or load a saved TNZ with **File → Load As Sub-Xsheet…**. Open one with **Xsheet → Open Sub-Xsheet**, close with **Xsheet → Close Sub-Xsheet**. Use **Xsheet → Explode Sub-Xsheet** to flatten it back out, or **Clone Sub-Xsheet** to get an independently editable copy.

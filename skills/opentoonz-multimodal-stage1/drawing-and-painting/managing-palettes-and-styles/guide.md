# Managing Palettes and Styles (OpenToonz 1.7)

Every Toonz Vector and Toonz Raster level carries its own palette — styles are linked to drawn lines and filled areas by index, so editing a style instantly updates every stroke and fill that uses it. Raster levels share a single **Raster Drawing Palette** stored in the project's **+palettes** folder instead.

The **Palette Editor** shows styles for the current level. You can switch between **Small/Medium/Large Thumbnails View** or **List View** by clicking the option button in the editor's top bar. Use the **+** and **-** shortcut keys to resize chips on the fly. Click the **Switch** button in the title bar to freeze the editor on one level's palette while you work elsewhere — handy for comparing palettes side by side.

See `fig01.png`.

Add styles with the **New Style** button, rename them by double-clicking, and organize them across pages using the **New Page** button or by Ctrl-dragging (Cmd on Mac) chips onto a page tab. Right-click the palette for **Remove Unused Styles** to clean house. Cut styles will turn any painted areas red as a warning; deleted styles prompt you to choose whether to erase associated artwork too.

The **Studio Palette** (under **Windows > Studio Palette**) is your production-wide color library. It has two root folders: **Global Palettes** (available in every session) and **Project Palettes** (scoped to the active project). Drag your level palette's **Palette** button into the Studio Palette tree to store it, then later right-click a stored palette and choose **Load into Current Palette** or **Merge to Current Palette** to bring colors back. Imported styles show a small white square; right-click and choose **Toggle Link to Studio Palette** to keep them synced — a linked style auto-updates whenever the Studio Palette version changes, giving you production-wide color consistency from a single edit.

See `fig02.png`.

To animate palette colors, select a frame in the Xsheet/Timeline and click the **Key** button in the Palette Editor's top bar. Navigate keys with the **Previous Key** / **Next Key** arrows. The animation is tied to absolute Xsheet timing, not to the level's frame count — so a five-frame level can have palette keys spanning frame 1 to 100.

Open the **Style Editor** via **Windows > Style Editor** (or double-click any style chip). It offers tabs for **Color**, **Texture**, **Vector**, **Raster**, and **Settings**. Toggle the **Auto** button to apply edits live, or leave it off and hit **Apply** manually. The color wheel and HSV/RGB sliders handle plain colors; the **RGB Picker** tool lets you sample directly from the viewer using normal, rectangular, freehand, or polyline selection modes.

See `fig03.png`.

Textures tile across lines or areas — add custom ones via the **Custom Texture** button and configure mapping options (scale, rotation, position mode) in the **Settings** tab. Generated styles produce procedural effects (polka dots, frieze patterns) along vectors; Trail styles repeat an image sequence along a stroke. Vector Brush styles apply a PLI drawing's shape to every stroke. For batch adjustments, select multiple styles, right-click, and open the **Palette Gizmo** to shift or scale hue, saturation, value, and alpha across the selection, or blend/fade them toward a target color.

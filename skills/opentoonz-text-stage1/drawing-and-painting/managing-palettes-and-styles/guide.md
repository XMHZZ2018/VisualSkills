# Managing Palettes and Styles (OpenToonz 1.7)

Every Toonz Vector and Toonz Raster level carries its own palette — styles are linked by index, so editing a color instantly updates every line and fill that uses it. Raster levels share a single **Raster Drawing Palette** stored in the project's **+palettes** folder.

The **Palette Editor** shows styles for the active level. Toggle the thumbnail size with the option button in the top bar or zoom with **+**/**-** keys. Click the **Switch** button in the title bar to freeze the editor on one palette while you work elsewhere. Add styles with **New Style**, organize them into pages via **New Page**, and drag styles between pages with Ctrl/Cmd+drag. Right-click and choose **Remove Unused Styles** to clean house.

The **Studio Palette** (under **Windows > Studio Palette**) is your production-wide color library. It splits into **Global Palettes** (available in every session) and **Project Palettes** (scoped to the current project). Drag a level's palette handle into the Studio Palette tree to store it, then later right-click a stored palette and choose **Load into Current Palette** or **Merge to Current Palette** to bring colors back. Imported styles show a small white square; right-click and choose **Toggle Link to Studio Palette** to keep them synced with the master.

To animate palette colors, select a frame in the Xsheet/Timeline and click the **Key** button in the Palette Editor's top bar. Navigate keys with the **Previous Key** / **Next Key** arrows. Animation is tied to absolute Xsheet timing, independent of level length.

Open the **Style Editor** via **Windows > Style Editor** (or double-click any style). Tabs include **Color**, **Texture**, **Vector** (Generated, Trail, Vector Brushes), and **Raster**. Use the color wheel or HSV/RGB sliders to tweak colors; the **Alpha** slider controls opacity. Toggle **Auto** to apply edits live, or leave it off and hit **Apply** manually. To revert, click the old-color swatch at the bottom-right corner.

For batch adjustments, select multiple styles, right-click, and open **Palette Gizmo** — it lets you scale or shift hue, saturation, value, and alpha across the selection, blend between endpoints, or fade toward a target color. The **Name Editor** (also in the right-click menu) helps standardize style names with preset Character, Part, and Suffix tokens.

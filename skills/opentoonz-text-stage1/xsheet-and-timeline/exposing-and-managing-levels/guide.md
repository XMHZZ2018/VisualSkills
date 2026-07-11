# Exposing and Managing Levels (OpenToonz 1.7)

Levels — animation sequences, background images, clips — need to be exposed in the Xsheet (or Timeline) to appear in your scene. Each column holds one level, each row is a frame, and cells are just references to drawings, not copies.

The **File Browser** is your main entry point for bringing assets in. Its left tree gives you **My Computer**, **Library**, **History**, and your **Projectroot** folders. Drag files straight from the browser into the Xsheet, or use **Level > Load Level…** to pick a file and optionally set a frame range with **Load Subsequence Level**. You can also load entire directories via **File > Load Folder…**. Files dragged from Finder/Explorer work too.

When loading assets stored outside your project, OpenToonz asks whether to **Import** (copy into your project's `+drawings`/`+extras` folders) or **Load** in place. Importing is strongly recommended — OpenToonz may overwrite level files on save.

Once loaded, every level lives in the **Scene Cast** regardless of whether it's currently exposed. To expose something from the Cast, select it and choose **Level > Expose in Xsheet**, or just drag it onto a cell. To pull specific frames from a level, display it in the **Level Strip** (right-click in the Cast > **Display in Level Strip**), select the drawings you need, then drag them into the Xsheet.

To swap one level for another while keeping your cell timing intact, select the exposed cells and choose **Level > Replace Level…**, then pick the new file.

Open **Level Settings** (right-click a level in the Xsheet > **Level Settings…**) to adjust the **Name**, **Path**, **DPI**, **Width/Height**, or toggle **Premultiply** and **White As Transparent**. Hit **Use Camera DPI** if the level matches camera size but displays at the wrong scale. **Subsampling** speeds up playback by skipping pixels — handy for heavy raster levels.

Control column visibility with the header toggles: the eye icon shows/hides in the viewer, the filmstrip icon includes/excludes from renders, and the lock prevents edits. Click the triangle for per-column **Opacity** and **Color Filter** overlays.

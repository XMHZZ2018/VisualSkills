# Creating and Saving Projects (QGIS 3.44)

QGIS works on one project at a time. A project captures your entire session state — layers, styles, map views, print layouts, digitizing settings, and more — so you can pick up exactly where you left off.

To start fresh, go to **Project > New** (Ctrl+N). If you've made unsaved changes, QGIS will ask whether to save first. The title bar shows "Untitled Project" until you explicitly save.

See `fig01.png`.

Opening an existing project is straightforward: use **Project > Open…** (Ctrl+O), or browse **Project > Open Recent** for something you worked on lately. At startup, QGIS shows your recent projects with thumbnails — double-click any entry to jump straight in. You can right-click entries to pin favorites or remove stale ones from the list.

Save your work with **Project > Save** (Ctrl+S) or **Project > Save As…** (Ctrl+Shift+S). By default QGIS saves in the compressed `.qgz` format, which bundles the XML project file (`.qgs`) and an auxiliary SQLite database (`.qgd`) into a single zip archive. A backup (`.qgs~`) is created automatically alongside uncompressed saves.

Projects don't have to live on disk. You can store them directly in PostgreSQL, GeoPackage, or Oracle databases via **Project > Save To** and reopen them with **Project > Open From**. Projects in those stores also appear in the Browser panel — just double-click or drag them onto the canvas.

If QGIS can't find a layer's data source when opening a project — maybe a file moved or a database went offline — a **Handle Unavailable Layers** dialog appears. You can double-click the path to fix it manually, hit **Browse** to point to the new location, or try **Auto-Find** to let QGIS scan for matches. Alternatively, keep unavailable layers as placeholders and repair them later from the layer's right-click menu via **Repair Data Source…**.

When you're ready to share your map visually, **Project > Import/Export** lets you export the canvas to image formats (PNG, JPG, TIFF) or PDF — with optional georeferencing — or to DXF for CAD workflows. For polished cartographic output, **Project > New Print Layout…** (Ctrl+P) opens the full layout designer.

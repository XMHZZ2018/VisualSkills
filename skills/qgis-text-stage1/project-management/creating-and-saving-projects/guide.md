# Creating and Saving Projects (QGIS 3.44)

A QGIS project captures your entire session — layers, styles, map views, print layouts, digitizing settings, and more — in a single file. QGIS works on one project at a time.

To start fresh, go to **Project → New** (Ctrl+N). You'll be prompted to save any unsaved changes first, and the title bar will read "Untitled Project" until you save.

Save your work with **Project → Save** (Ctrl+S) or **Project → Save As…** (Ctrl+Shift+S). The default format is `.qgz`, a compressed archive bundling the XML project (`.qgs`) with an SQLite auxiliary database (`.qgd`). A backup `.qgs~` file is created automatically alongside uncompressed saves.

Open existing projects via **Project → Open…** (Ctrl+O), **Project → New from Template**, or **Project → Open Recent**. You can also double-click project files in the Browser panel. At startup, QGIS shows recent projects with thumbnails — right-click entries to pin them or open their directory.

Projects can live in databases too. Use **Project → Open From** or **Project → Save To** for PostgreSQL, GeoPackage, or Oracle storage.

If layers can't be found when opening a project, QGIS shows the **Handle Unavailable Layers** dialog. You can double-click the datasource path to fix it manually, use **Browse** to point to the new location, or hit **Auto-Find** to let QGIS search for matches. Alternatively, keep broken layers and repair them later via right-click → **Repair Data Source…** in the Layers panel.

For output beyond the project file, look under **Project → Import/Export** to export your map canvas as an image (PNG, JPG, TIFF), PDF, or DXF. Use **Project → New Print Layout…** (Ctrl+P) for full cartographic composition.

# Using Spatial Bookmarks (QGIS 3.44)

Spatial bookmarks let you save a particular map extent — zoom level, position, rotation — and jump back to it instantly. Think of them as named "views" you can recall anytime without manually panning around.

Bookmarks come in two flavors: **User Bookmarks** persist in your profile and follow you across every project, while **Project Bookmarks** are saved inside the project file itself, making them shareable with collaborators.

To create a bookmark, navigate the map canvas to the view you want to save, then go to **View > New Spatial Bookmark…** (or press `Ctrl+B`). You can also right-click the **Spatial Bookmarks** entry in the Browser panel and choose **New Spatial Bookmark**. The Bookmark Editor dialog lets you give it a name, assign it to a group, tweak the extent, set a rotation, choose the CRS, and pick whether it lives under User or Project bookmarks. Hit **Save** when you're happy.

See `fig01.png`.

To manage your bookmarks, open the Spatial Bookmark Manager with **View > Show Spatial Bookmark Manager** (`Ctrl+7`). From there, double-click any bookmark to zoom straight to it, or select one and click the **Zoom to bookmark** button. You can also find bookmarks in the Browser panel via **View > Show Spatial Bookmarks** (`Ctrl+Shift+B`).

Editing is straightforward — in the Manager, just change values directly in the table (name, group, extent, storage location). In the Browser, right-click a bookmark and choose **Edit Spatial Bookmark…** to reopen the full editor. You can drag bookmarks between User and Project folders, or between groups, to reorganize them.

Need to share bookmarks with someone who isn't on the project? Use the **Import/Export Bookmarks** button in the Manager to export them as XML, or right-click a folder in the Browser and choose **Export Spatial Bookmarks…** for a subset. Importing works the same way in reverse.

For quick access without opening any panel, just type a bookmark's name into the locator bar at the bottom of the QGIS window — it will appear as a match you can jump to immediately.

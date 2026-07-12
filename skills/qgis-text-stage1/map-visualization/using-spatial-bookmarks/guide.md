# Using Spatial Bookmarks (QGIS 3.44)

Spatial bookmarks save a map extent so you can snap back to it later — handy for jumping between areas of interest without manually panning and zooming every time.

Bookmarks come in two flavors: **User Bookmarks** persist across all your projects (stored in your profile), while **Project Bookmarks** live inside the project file and travel with it when shared.

**Creating a bookmark:** Navigate to the extent you want to save, then go to **View > New Spatial Bookmark…** (or press `Ctrl+B`). In the Bookmark Editor, give it a name, optionally assign it to a group, confirm the extent and CRS, choose whether to save it as a User or Project bookmark, and hit **Save**.

**Recalling a bookmark:** Open the Spatial Bookmark Manager with **View > Show Spatial Bookmark Manager** (`Ctrl+7`). Double-click any bookmark to zoom straight to it. You can also find bookmarks in the Browser panel via **View > Show Spatial Bookmarks** (`Ctrl+Shift+B`), or just type a bookmark name into the locator bar for instant access.

**Managing bookmarks:** Edit values directly in the Manager table — name, group, extent, and storage location are all fair game. Delete a bookmark by selecting it and clicking the **Delete bookmark** button. You can drag bookmarks between User and Project folders in the Browser panel to change where they're stored.

**Import/Export:** In the Spatial Bookmark Manager, click **Import/Export Bookmarks** to save all bookmarks to XML or load them back in. The Browser panel gives finer control — right-click a specific folder or group to export just that subset.

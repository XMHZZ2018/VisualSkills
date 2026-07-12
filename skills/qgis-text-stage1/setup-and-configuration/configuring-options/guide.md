# Configuring Global Options (QGIS 3.44)

Open the Options dialog via **Settings > Options**. The left panel lists every category — changes apply globally to your active user profile and persist across sessions. Some tweaks require a restart.

Under **General**, the Application section lets you pick a UI theme (default, Night Mapping, or Blend of Gray), adjust icon size, and set a custom font. The Project Files section controls what happens at launch — show the Welcome Page, open a new blank project, reopen the last project, or load a specific one. You can also set your default project file format to QGZ (archive with embedded auxiliary data) or plain-text QGS.

**CRS and Transforms** determines how new projects get their coordinate reference system: either from the first layer added or from a default CRS you specify. You can also configure what happens when a layer has no CRS — leave it unknown, prompt, or silently assign one.

**Data Sources** controls attribute table behavior (docked vs. floating, which features to show on open) and how the Browser panel scans directories and compressed files. The GDAL sub-tab lets you enable/disable specific raster and vector drivers and customize creation option profiles for formats like GeoTiff.

**Rendering** offers performance knobs: toggling feature simplification for vector layers, setting the map update interval, controlling raster resampling (Nearest Neighbour, Bilinear, Cubic), and enabling anti-aliasing at the cost of some speed.

**Canvas & Legend** sets your default map background/selection colors and controls legend behavior — what a double-click does, where new layers land in the layer tree, and whether to respect your monitor's physical DPI for accurate on-screen scaling.

**Map Tools** is where you configure default measurement units (distance, area, angles), the Identify tool's search radius and highlight style, zoom factor, and your list of predefined map scales. The **Digitizing** sub-tab covers snapping defaults, vertex markers, and rubberband styling.

**Network** handles request timeouts, WMS/WMTS cache expiration, and proxy configuration (HTTP, SOCKS5, or system default). Point the cache directory somewhere with enough space, or leave it on "Smart" to auto-size based on disk availability.

Installed plugins can inject their own tabs into this same dialog, so don't be surprised if you see extra entries beyond the core set.

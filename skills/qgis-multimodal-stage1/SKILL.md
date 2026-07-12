---
name: qgis-multimodal-stage1
description: "Practical with-screenshots guides for QGIS 3.44. Consult via the load_topic MCP tool — it returns the guide text and every figure in one atomic call."
---

# QGIS 3.44 Knowledge (multimodal-stage1)

## How to consult this skill

This skill exposes two MCP tools (already registered for you):

- **`load_topic(topic)`** — returns the chosen topic's `guide.md` AND every figure (PNG) in that topic folder as one tool response. **Use this instead of `Read` for any `*.md` or `figXX.png` inside this skill.**
- **`list_topics()`** — returns every topic path available, one per line.

Each entry in the TOC below has the form `[Title](<topic>/guide.md)`. The `<topic>` part (the path before `/guide.md`) is what you pass to `load_topic`.

> You will receive the guide text plus the relevant figures in a single tool result — no extra `Read` calls needed.

**Rules:**

1. Before any GUI action where you are unsure of the menu path / dialog / icon, find the matching topic in the TOC and call `load_topic` first.
2. You may call `load_topic` **at any step** of the trajectory, not only at the start. If the task moves into a new area, call `load_topic` again for the new area.
3. Do **not** issue separate `Read` calls for `figXX.png` files inside this skill — they are delivered by `load_topic` automatically.

## Guides

### Setup and Configuration

- [Installing QGIS](setup-and-configuration/installing-qgis/guide.md) — Install QGIS from binaries, source, or external media
  - **Use when:** installing QGIS from binaries, building QGIS from source, running QGIS from USB drive, downloading Alaska sample data, using --profiles-path for portable installation
- [Configuring Global Options](setup-and-configuration/configuring-options/guide.md) — Set application-wide preferences and behavior settings
  - **Use when:** setting locale and UI theme, choosing default project format (QGZ/QGS), configuring custom environment variables, setting default CRS and datum transforms, configuring network proxy settings, managing global expression variables
- [Managing User Profiles](setup-and-configuration/managing-user-profiles/guide.md) — Create and switch between user profiles with separate settings
  - **Use when:** creating a new user profile, switching between profiles, setting startup profile behavior, launching profile from command line, troubleshooting corrupted profile, customizing profile selector icon
- [Customizing Keyboard Shortcuts](setup-and-configuration/customizing-keyboard-shortcuts/guide.md) — Define and modify keyboard shortcuts for QGIS actions
  - **Use when:** remapping keyboard shortcuts in QGIS, resolving shortcut conflicts, exporting shortcuts to XML, importing shortcut configurations, resetting default keybindings, searching actions in Settings > Keyboard Shortcuts dialog
- [Customizing the Interface](setup-and-configuration/customizing-gui/guide.md) — Show/hide panels, toolbars, and menu items
  - **Use when:** showing/hiding panels and toolbars, toggling full-screen map-only mode, removing menu items via Interface Customization dialog, exporting UI customization to .ini file, resetting UI to default settings

### Project Management

- [Creating and Saving Projects](project-management/creating-and-saving-projects/guide.md) — Create, open, save, and manage QGIS project files
  - **Use when:** creating a new QGIS project, saving as .qgz or .qgs, saving project to PostgreSQL or GeoPackage, repairing unavailable layer data sources, exporting map canvas to PDF or image, opening recent projects
- [Handling Broken File Paths](project-management/handling-broken-file-paths/guide.md) — Repair or skip layers with missing data sources when opening a project
  - **Use when:** fixing broken layer paths, using Handle Unavailable Layers dialog, Auto-Find missing data sources, Repair Data Source from context menu, removing unavailable layers, --skipbadlayers command-line flag
- [Configuring Project Properties](project-management/configuring-project-properties/guide.md) — Set project-level CRS, metadata, and default styles
  - **Use when:** setting project CRS and datum transformations, configuring canvas selection and background colors, choosing ellipsoid and measurement units, linking external style databases, defining project color palette variables, setting layer path storage as relative or absolute
- [Exporting Map Output](project-management/exporting-map-output/guide.md) — Export the map view as image, PDF, or DXF
  - **Use when:** exporting map to image, exporting map to PDF, exporting project to DXF, appending georeference world file, creating geospatial PDF, copying map to clipboard

### Data Sources

- [Opening and Loading Layers](data-sources/opening-and-loading-layers/guide.md) — Load vector, raster, mesh, and delimited text files into QGIS
  - **Use when:** opening Data Source Manager, loading vector layers from file, adding raster layers, importing delimited text with coordinates, drag-and-drop layers onto canvas, browsing mesh data
- [Creating New Layers](data-sources/creating-new-layers/guide.md) — Create GeoPackage, Shapefile, SpatiaLite, scratch, and virtual layers
  - **Use when:** creating new GeoPackage layers, creating shapefiles, creating SpatiaLite layers, creating temporary scratch layers, writing virtual layer SQL queries, pasting features as new vector layer
- [Georeferencing Rasters](data-sources/georeferencing-rasters/guide.md) — Assign spatial coordinates to unreferenced raster images
  - **Use when:** georeferencing rasters with GCPs, adding ground control points from map canvas, choosing transformation type for georeferencer, setting resampling method and target CRS, saving and loading GCP points files, checking residual errors in GCP table
- [Connecting to Databases](data-sources/connecting-to-databases/guide.md) — Load layers from PostgreSQL, SpatiaLite, and other database sources
  - **Use when:** creating a PostgreSQL connection in Data Source Manager, adding a SpatiaLite layer, configuring pg_service.conf, testing database credentials, loading layers by schema and geometry type, running SQL in DB Manager
- [Exploring Data Formats and Fields](data-sources/exploring-data-formats/guide.md) — Inspect supported formats and explore layer field structure
  - **Use when:** creating spatial index for shapefiles, enforcing CSV field types with .csvt, loading PostGIS views without primary key, exporting to GeoJSON with RFC7946, creating field domains in GeoPackage, fixing layers split at 180° longitude

### Projections and Coordinate Reference Systems

- [Setting Layer and Project CRS](projections-and-crs/setting-layer-and-project-crs/guide.md) — Assign or change coordinate reference systems for layers and the project
  - **Use when:** setting layer CRS with Ctrl+Shift+C, changing project CRS in Project Properties, configuring CRS fallback behavior in Options, setting project CRS from layer, changing default CRS for new projects, using CRS selector dialog
- [Creating a Custom CRS](projections-and-crs/creating-custom-crs/guide.md) — Define a new coordinate reference system with custom parameters
  - **Use when:** creating a custom CRS in QGIS, opening the Custom CRS dialog, entering Proj String or WKT parameters, validating a CRS definition, testing CRS with known coordinates, adding NTv2 grid-shift file to PROJ
- [Configuring Datum Transformations](projections-and-crs/configuring-datum-transformations/guide.md) — Set transformation pipelines between different datums
  - **Use when:** setting default datum transformation, configuring CRS transformation fallback, installing grid-shift files for projections, selecting transformation pipeline in Select Datum Transformations dialog, project-specific CRS override in Project Properties

### Map Visualization

- [Navigating the 2D Map View](map-visualization/navigating-2d-map-view/guide.md) — Zoom, pan, and explore the 2D map canvas
  - **Use when:** panning and zooming the map canvas, copying coordinates from map right-click, enabling or disabling map rendering, opening additional map views, using zoom history navigation, animating temporal data with Temporal Controller
- [Using the 3D Map View](map-visualization/using-3d-map-view/guide.md) — Visualize and navigate data in a 3D perspective view
  - **Use when:** configuring 3D terrain elevation from DEM, adding lights and shadows in 3D view, navigating and orbiting 3D camera, creating flythrough animation keyframes, exporting 3D view as image or OBJ, measuring 3D distances
- [Creating Elevation Profiles](map-visualization/creating-elevation-profiles/guide.md) — Generate cross-section elevation profiles from terrain data
  - **Use when:** creating elevation profiles from terrain data, capturing cross-section lines on map, configuring layer elevation properties, exporting profiles as PDF or CSV, measuring distances along elevation profile, nudging profile line with tolerance buffer
- [Measuring Distances and Areas](map-visualization/measuring-distances-and-areas/guide.md) — Measure line distances, areas, and angles on the map
  - **Use when:** measuring distance on map canvas, measuring area of polygon, measuring bearing between points, measuring angle, switching ellipsoidal vs planimetric calculation, configuring measure tool units and precision
- [Decorating the Map](map-visualization/decorating-the-map/guide.md) — Add grid, scale bar, north arrow, title, and copyright decorations
  - **Use when:** adding map grid, inserting title label, adding copyright label, overlaying image decoration, configuring north arrow, setting up scale bar
- [Using Spatial Bookmarks](map-visualization/using-spatial-bookmarks/guide.md) — Save and recall map extents as named bookmarks
  - **Use when:** creating spatial bookmarks with Ctrl+B, zooming to saved map extents, managing bookmarks in Spatial Bookmark Manager, importing/exporting bookmarks as XML, organizing user vs project bookmarks, finding bookmarks via locator bar
- [Using the Temporal Controller](map-visualization/using-temporal-controller/guide.md) — Animate and filter map data by time
  - **Use when:** configuring temporal properties on layers, animating map data over time, setting animation range and step size, using cumulative range option, exporting animation as image sequence, scrubbing the temporal controller slider

### Vector Data

- [Editing Vector Geometry](vector-data/editing-vector-geometry/guide.md) — Digitize, reshape, split, merge, and modify vector features
  - **Use when:** sketching polygon/line/point features, configuring snapping options, using vertex tool to move/add/delete vertices, reshaping and splitting geometries, CAD-precise digitizing with Advanced Digitizing Panel, merging selected features
- [Working with the Attribute Table](vector-data/working-with-attribute-table/guide.md) — View, edit, sort, filter, and calculate field values
  - **Use when:** opening and filtering the attribute table, selecting features by expression, editing field values with Field Calculator, bulk updating with multi edit mode, conditional formatting of rows and cells, identifying feature attributes on map
- [Configuring Vector Layer Properties](vector-data/configuring-vector-properties/guide.md) — Set symbology, labels, rendering, and metadata for vector layers
  - **Use when:** renaming vector layer display name, setting coordinate reference system, filtering features with Query Builder, configuring symbology renderers, labeling vector features, setting scale-dependent visibility
- [Joining and Relating Layers](vector-data/joining-and-relating-layers/guide.md) — Create table joins and relations between vector layers
  - **Use when:** joining layers by shared attribute, defining one-to-many relations in Project Properties, setting up many-to-many with pivot tables, adding polymorphic relations, discovering database relationships, editing joined fields in attribute table
- [Selecting Features](vector-data/selecting-features/guide.md) — Select features by expression, location, or interactive tools
  - **Use when:** selecting features by polygon or freehand shape, Select Features By Expression dialog, Select Features By Value with field operators, Select by Location spatial query, refining selection with Shift/Ctrl modifiers, deselecting and reselecting features
- [Identifying Features](vector-data/identifying-features/guide.md) — Click features to inspect their attributes and geometry
  - **Use when:** identifying features by click or area selection, viewing feature attributes and geometry, configuring identify mode and layer querying, zooming to or highlighting identified features, disabling identifiable layers in project properties, auto-opening feature form for editing

### Raster, Mesh, and Point Cloud Data

- [Configuring Raster Layer Properties](raster-and-mesh-data/configuring-raster-properties/guide.md) — Set band rendering, transparency, pyramids, and histogram for rasters
  - **Use when:** setting raster band rendering and symbology, adjusting raster transparency and no data values, computing raster histogram, building raster pyramids for performance, configuring raster resampling method, applying pseudocolor or hillshade to DEM
- [Using the Raster Calculator](raster-and-mesh-data/using-raster-calculator/guide.md) — Perform map algebra operations on raster bands
  - **Use when:** raster map algebra expressions, converting elevation units, masking raster values by condition, classifying raster into categories, creating on-the-fly virtual raster, setting output extent and resolution
- [Working with Mesh Layers](raster-and-mesh-data/working-with-mesh-layers/guide.md) — Load, style, edit, and analyze mesh datasets
  - **Use when:** loading mesh layers (NetCDF/GRIB/XMDF), configuring mesh symbology contours and vectors, temporal navigation for mesh datasets, digitizing and editing mesh elements, transform vertices coordinates dialog, running Mesh Calculator expressions
- [Working with Point Clouds](raster-and-mesh-data/working-with-point-clouds/guide.md) — Load, style, and explore LiDAR and other point cloud data
  - **Use when:** loading LAS/LAZ/EPT point clouds, styling with Attribute by Ramp or Classification renderer, triangulating point surface rendering, configuring 3D view and eye dome lighting, building virtual point cloud (VPC), filtering points with PDAL expressions
- [Working with Vector Tiles](raster-and-mesh-data/working-with-vector-tiles/guide.md) — Load and style vector tile datasets
  - **Use when:** adding vector tile XYZ or MBTiles source, styling vector tile rules by sub-layer and zoom, importing MapBox GL JSON style, labeling vector tile layers, setting vector tile opacity and blending mode, configuring scale-dependent visibility for tiles
- [Working with 3D Tiles](raster-and-mesh-data/working-with-3d-tiles/guide.md) — Load and configure 3D tile datasets for visualization
  - **Use when:** adding 3D tile layers from tileset URL, configuring 3D tile symbology and wireframe rendering, adjusting maximum screen space error for tile detail, setting scale-dependent visibility for 3D tiles, applying elevation offset and scale to 3D tiles, opening a new 3D map view

### Styling and Labeling

- [Managing the Style Library](styling-and-labeling/managing-styles/guide.md) — Organize, import, export, and share symbols and styles
  - **Use when:** organizing symbols with tags and smart groups, exporting symbols to XML or SVG, importing styles from XML or URL, creating custom color ramps, defining legend patch shapes as WKT, switching between style databases
- [Configuring Symbols](styling-and-labeling/configuring-symbols/guide.md) — Create and customize marker, line, and fill symbols
  - **Use when:** configuring marker/line/fill symbol layers, setting SVG marker dynamic parameters, using Geometry Generator expressions, saving symbols to library, controlling symbol draw order with symbol levels, setting dash patterns and arrow line styles
- [Setting Labels](styling-and-labeling/setting-labels/guide.md) — Configure text labels with placement, formatting, and rendering rules
  - **Use when:** configuring label text and font in Layer Properties, adding label buffers and drop shadows, setting label placement for points lines and polygons, enabling HTML formatting in labels, using callouts for displaced labels, controlling label overlap and rendering rules
- [Creating 3D Symbols](styling-and-labeling/creating-3d-symbols/guide.md) — Define symbol styles for 3D map visualization
  - **Use when:** creating 3D point line polygon symbols in Style Manager, configuring 3D symbol shading (Phong, textured, Gooch, metal roughness), setting altitude clamping mode, extruding polygons with data-defined height, importing custom 3D models (.obj .glTF .fbx), adjusting 3D symbol culling and back faces

### Expressions

- [Writing Expressions](expressions/writing-expressions/guide.md) — Build expressions for labeling, filtering, styling, and calculations
  - **Use when:** writing expressions in the Expression string builder, selecting features with Select By Expression, calculating field values with Field Calculator, creating custom Python functions with @qgsfunction, saving and sharing user expressions as .json, data-defined overrides for symbology and layouts
- [Using Expression Functions](expressions/using-expression-functions/guide.md) — Reference available functions for geometry, string, math, and aggregates
  - **Use when:** writing field calculator expressions, selecting features by expression, dynamic labeling with geometry functions, aggregating values across layers, string manipulation in expressions, using variables in print layouts

### Print Layout and Map Export

- [Designing Print Layouts](print-layout/designing-print-layouts/guide.md) — Create and configure map compositions for printing or export
  - **Use when:** creating print layouts, exporting layout as PDF/image/SVG, aligning items with guides and snapping, adding map/legend/scalebar/label items, managing layout pages and templates, configuring export resolution and georeferencing
- [Adding Layout Items](print-layout/adding-layout-items/guide.md) — Insert maps, legends, scale bars, tables, and images into a layout
  - **Use when:** adding maps legends and scale bars to print layout, placing north arrows and pictures, adding attribute tables and HTML frames, grouping locking and reordering layout items, repositioning and resizing items on canvas
- [Creating Print Output](print-layout/creating-print-output/guide.md) — Export layouts as PDF, image, or SVG
  - **Use when:** exporting layout as image with world file, exporting layout as SVG with layer groups, exporting layout as geospatial PDF, generating atlas from coverage layer, previewing and exporting atlas pages, configuring image export resolution and crop to content
- [Creating Reports](print-layout/creating-reports/guide.md) — Build multi-page reports with iterating sections
  - **Use when:** creating multi-page reports, adding field group sections, nesting atlas iterations in reports, exporting report as PDF/SVG/images, data-defining dynamic pictures per feature, configuring report header and footer

### Processing Framework

- [Using the Processing Toolbox](processing-framework/using-processing-toolbox/guide.md) — Find and run geoprocessing algorithms from the toolbox
  - **Use when:** searching and filtering algorithms in Processing Toolbox, running geoprocessing algorithms with parameters, iterating algorithm over individual features, saving output to GeoPackage or temporary layer, copying PyQGIS or qgis_process command from dialog, reprojecting layers before processing
- [Building Graphical Models](processing-framework/building-graphical-models/guide.md) — Chain processing algorithms into reusable workflow models
  - **Use when:** creating graphical processing models, chaining algorithms in Model Designer, defining model inputs and parameters, running and debugging model workflows, saving .model3 files, exporting model as Python script
- [Running Batch Processes](processing-framework/running-batch-processes/guide.md) — Execute an algorithm on multiple inputs in one operation
  - **Use when:** running algorithms as batch process, autofilling batch parameters with expressions, adding files by pattern to batch table, saving batch configuration as JSON, auto-naming batch output files, writing batch outputs to GeoPackage database
- [Writing Processing Scripts](processing-framework/writing-processing-scripts/guide.md) — Create custom processing algorithms in Python
  - **Use when:** writing custom Processing algorithms in Python, creating scripts from template in Processing Toolbox, defining algorithm parameters and outputs, using processAlgorithm with feedback and cancellation, chaining algorithms with processing.run, using @alg decorator for scripts
- [Running Vector Geoprocessing](processing-framework/running-vector-geoprocessing/guide.md) — Execute buffer, clip, dissolve, intersection, and other vector operations
  - **Use when:** buffering vector features, dissolving by attribute, clipping with overlay polygon, computing intersection or difference, union of two layers, extracting by bounding box extent
- [Running Raster Analysis Algorithms](processing-framework/running-raster-analysis/guide.md) — Execute hillshade, slope, aspect, and other terrain analysis tools
  - **Use when:** generating hillshade from DEM, calculating slope and aspect, raster calculator band math, reclassify raster by table, zonal statistics with polygons, batch processing raster terrain tools
- [Configuring External Applications](processing-framework/configuring-external-applications/guide.md) — Set up GDAL, GRASS, SAGA, and other third-party processing providers
  - **Use when:** enabling external processing providers, configuring GRASS/GDAL/R/LAStools/OTB paths, setting R provider plugin folder, pointing LAStools folder in Processing options, configuring OTB application folder and RAM, troubleshooting external tool file format issues

### Remote Services and Protocols

- [Connecting to WMS/WMTS Services](remote-services/connecting-to-wms-wmts/guide.md) — Load map imagery from OGC Web Map Services
  - **Use when:** adding WMS/WMTS server connection, configuring WMTS KVP or RESTful URL, selecting WMS layer encoding and CRS, loading WMS layers separately or merged, setting WMS tile cache and proxy, configuring temporal properties for time-aware WMS layers
- [Connecting to WFS Services](remote-services/connecting-to-wfs/guide.md) — Load and edit vector features from OGC Web Feature Services
  - **Use when:** adding a WFS layer in Data Source Manager, configuring WFS server connection URL, filtering WFS features with SQL Query Composer, editing WFS-T features remotely, setting WFS feature paging and max count, connecting to OGC API Features endpoint
- [Using STAC Catalogs](remote-services/using-stac-catalogs/guide.md) — Browse and load data from SpatioTemporal Asset Catalogs
  - **Use when:** connecting to STAC catalogs, browsing STAC collections and items, filtering STAC API by spatial and temporal extent, downloading STAC assets, previewing item footprints on map, adding cloud-optimized rasters from STAC
- [Connecting to ArcGIS REST Servers](remote-services/connecting-to-arcgis-rest/guide.md) — Load layers from ArcGIS MapServer and FeatureServer endpoints
  - **Use when:** adding ArcGIS REST server connection, configuring ArcGIS authentication in Browser panel, loading MapServer or FeatureServer layers, editing FeatureServer layers in QGIS, refreshing ArcGIS REST layers
- [Using XYZ Tile Services](remote-services/using-xyz-tile-services/guide.md) — Add raster basemaps from XYZ tile providers
  - **Use when:** adding XYZ tile connections, configuring tile URL with z/x/y placeholders, setting zoom levels and authentication, decoding terrain RGB tiles as elevation rasters, exporting XYZ tiles to local file, saving and sharing tile connections as XML

### Plugins and Scripting

- [Managing Plugins](plugins-and-scripting/managing-plugins/guide.md) — Install, update, enable, and remove QGIS plugins
  - **Use when:** installing plugins from Plugin Manager, enabling experimental or deprecated plugins, installing plugin from ZIP file, adding third-party plugin repository, upgrading or uninstalling plugins, activating or deactivating installed plugins
- [Using the Python Console](plugins-and-scripting/using-python-console/guide.md) — Run Python commands and scripts within QGIS
  - **Use when:** opening Python console in QGIS, running PyQGIS commands interactively, using code editor with syntax highlighting, auto-completion for PyQGIS and PyQt5, executing shell commands from console, sharing scripts as GitHub Gist
- [Using GRASS GIS Integration](plugins-and-scripting/using-grass-integration/guide.md) — Access GRASS tools, manage mapsets, and edit GRASS vector layers
  - **Use when:** loading GRASS layers from Browser panel, creating and opening a GRASS mapset, importing rasters with r.in.gdal, digitizing topological boundaries and centroids, setting GRASS region extent and resolution, running GRASS Toolbox modules like r.contour
- [Tracking GPS Data](plugins-and-scripting/tracking-gps-data/guide.md) — Connect to GPS devices and perform live tracking
  - **Use when:** connecting GPS receiver to QGIS, digitizing features from live GPS position, logging GPS tracks to GeoPackage, configuring Bluetooth GPS device, viewing satellite signal strength panel, setting GPS destination layer


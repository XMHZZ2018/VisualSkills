---
name: qgis-text-stage1
description: "Practical text-only guides for QGIS 3.44. Consult via the load_topic MCP tool — it returns the guide text in one atomic call."
---

# QGIS 3.44 Knowledge (text-stage1)

## How to consult this skill

This skill exposes two MCP tools (already registered for you):

- **`load_topic(topic)`** — returns the chosen topic's `guide.md` as one tool response. **Use this instead of `Read` for any `*.md` inside this skill.**
- **`list_topics()`** — returns every topic path available, one per line.

Each entry in the TOC below has the form `[Title](<topic>/guide.md)`. The `<topic>` part (the path before `/guide.md`) is what you pass to `load_topic`.

> You will receive the guide text in a single tool result — no extra `Read` calls needed.

**Rules:**

1. Before any GUI action where you are unsure of the menu path / dialog / icon, find the matching topic in the TOC and call `load_topic` first.
2. You may call `load_topic` **at any step** of the trajectory, not only at the start. If the task moves into a new area, call `load_topic` again for the new area.

## Guides

### Setup and Configuration

- [Installing QGIS](setup-and-configuration/installing-qgis/guide.md) — Install QGIS from binaries, source, or external media
  - **Use when:** downloading QGIS installer, building QGIS from source, portable QGIS on flash drive with --profiles-path, downloading sample dataset, launching QGIS from terminal or project file
- [Configuring Global Options](setup-and-configuration/configuring-options/guide.md) — Set application-wide preferences and behavior settings
  - **Use when:** setting UI theme and icon size, configuring default CRS for new projects, managing GDAL raster/vector drivers, tuning map rendering performance, setting measurement units and map scales, configuring network proxy and WMS cache
- [Managing User Profiles](setup-and-configuration/managing-user-profiles/guide.md) — Create and switch between user profiles with separate settings
  - **Use when:** creating a new user profile, switching between profiles, setting default startup profile, launching profile from command line, locating profile folder, troubleshooting with fresh profile
- [Customizing Keyboard Shortcuts](setup-and-configuration/customizing-keyboard-shortcuts/guide.md) — Define and modify keyboard shortcuts for QGIS actions
  - **Use when:** remapping keyboard shortcuts in QGIS, exporting shortcuts to XML or PDF, importing shortcut configuration, clearing or resetting default shortcuts, Settings Keyboard Shortcuts dialog
- [Customizing the Interface](setup-and-configuration/customizing-gui/guide.md) — Show/hide panels, toolbars, and menu items
  - **Use when:** customizing toolbars and panels visibility, toggling map-only or full-screen view, interface customization via settings dialog, saving and loading interface customization .ini files, resetting user interface to defaults, catching widgets to hide UI elements

### Project Management

- [Creating and Saving Projects](project-management/creating-and-saving-projects/guide.md) — Create, open, save, and manage QGIS project files
  - **Use when:** creating a new QGIS project, saving as .qgz or .qgs, opening projects from PostgreSQL or GeoPackage, repairing unavailable layers, exporting map canvas to PDF or DXF, pinning recent projects
- [Handling Broken File Paths](project-management/handling-broken-file-paths/guide.md) — Repair or skip layers with missing data sources when opening a project
  - **Use when:** fixing broken file paths, Handle Unavailable Layers dialog, Auto-Find missing data sources, Repair Data Source for broken layers, removing unavailable layers, --skipbadlayers flag
- [Configuring Project Properties](project-management/configuring-project-properties/guide.md) — Set project-level CRS, metadata, and default styles
  - **Use when:** setting project CRS and datum transformations, configuring measurement units and ellipsoid, editing project metadata, setting default layer symbols and opacity, attaching shared style databases, setting project title and home folder
- [Exporting Map Output](project-management/exporting-map-output/guide.md) — Export the map view as image, PDF, or DXF
  - **Use when:** exporting map to image or PDF, creating geospatial PDF, appending georeference world file, exporting project to DXF, copying map canvas to clipboard, setting export extent and resolution

### Data Sources

- [Opening and Loading Layers](data-sources/opening-and-loading-layers/guide.md) — Load vector, raster, mesh, and delimited text files into QGIS
  - **Use when:** loading vector layers via Data Source Manager, adding raster or mesh layers, importing delimited text CSV with coordinates, dragging files from Browser panel, connecting to PostgreSQL/WMS/WFS databases, opening GeoPackage or Shapefile
- [Creating New Layers](data-sources/creating-new-layers/guide.md) — Create GeoPackage, Shapefile, SpatiaLite, scratch, and virtual layers
  - **Use when:** creating GeoPackage layers, creating shapefiles, creating SpatiaLite layers, creating temporary scratch layers, defining virtual layers with SQL, pasting features as new vector layer
- [Georeferencing Rasters](data-sources/georeferencing-rasters/guide.md) — Assign spatial coordinates to unreferenced raster images
  - **Use when:** georeferencing a raster image, placing ground control points, choosing transformation type, configuring resampling and target CRS, generating GeoTIFF from unpositioned raster, loading and refining .points file
- [Connecting to Databases](data-sources/connecting-to-databases/guide.md) — Load layers from PostgreSQL, SpatiaLite, and other database sources
  - **Use when:** connecting to PostgreSQL/SpatiaLite/MS SQL Server, creating new database connections in Browser Panel, using Data Source Manager, testing database connections, loading database tables as map layers, running SQL queries via DB Manager
- [Exploring Data Formats and Fields](data-sources/exploring-data-formats/guide.md) — Inspect supported formats and explore layer field structure
  - **Use when:** creating spatial index for shapefiles, declaring CSV column types with .csvt, exporting GeoJSON with RFC7946, connecting PostGIS layers in QGIS, setting up field domains in GeoPackage, fixing 180° antimeridian split geometries

### Projections and Coordinate Reference Systems

- [Setting Layer and Project CRS](projections-and-crs/setting-layer-and-project-crs/guide.md) — Assign or change coordinate reference systems for layers and the project
  - **Use when:** setting layer CRS with Ctrl+Shift+C, setting project CRS from status bar, configuring default CRS for new projects, choosing datum transformations, handling layers with unknown CRS, setting project CRS from layer
- [Creating a Custom CRS](projections-and-crs/creating-custom-crs/guide.md) — Define a new coordinate reference system with custom parameters
  - **Use when:** defining a custom CRS, adding WKT or Proj String parameters, validating projection definitions, testing CRS with known coordinates, installing NTv2 grid files
- [Configuring Datum Transformations](projections-and-crs/configuring-datum-transformations/guide.md) — Set transformation pipelines between different datums
  - **Use when:** setting default datum transformation, choosing PROJ pipeline for CRS pair, installing missing grid packages, configuring per-project CRS overrides, enabling datum transformation prompt dialog

### Map Visualization

- [Navigating the 2D Map View](map-visualization/navigating-2d-map-view/guide.md) — Zoom, pan, and explore the 2D map canvas
  - **Use when:** panning and zooming the map canvas, copying coordinates from map click, zooming to layer or selection extent, suspending map rendering, opening synchronized map views, navigating zoom extent history
- [Using the 3D Map View](map-visualization/using-3d-map-view/guide.md) — Visualize and navigate data in a 3D perspective view
  - **Use when:** opening a 3D map view, configuring terrain elevation and DEM, adding lights and shadows, creating flythrough animations, exporting 3D scene to .obj, measuring distances in 3D
- [Creating Elevation Profiles](map-visualization/creating-elevation-profiles/guide.md) — Generate cross-section elevation profiles from terrain data
  - **Use when:** drawing elevation profile lines, configuring elevation layer properties, exporting profiles as PDF or DXF, measuring slope and distance on profiles, nudging profile cross-sections, setting profile tolerance for point clouds
- [Measuring Distances and Areas](map-visualization/measuring-distances-and-areas/guide.md) — Measure line distances, areas, and angles on the map
  - **Use when:** measuring distances on map, measuring polygon areas, measuring bearing azimuth, measuring angles between segments, switching ellipsoidal vs planimetric calculation, configuring measure tool units and precision
- [Decorating the Map](map-visualization/decorating-the-map/guide.md) — Add grid, scale bar, north arrow, title, and copyright decorations
  - **Use when:** adding map grid, adding title label, adding copyright label, adding north arrow, adding scale bar, showing layout extents on canvas
- [Using Spatial Bookmarks](map-visualization/using-spatial-bookmarks/guide.md) — Save and recall map extents as named bookmarks
  - **Use when:** creating spatial bookmarks with Ctrl+B, recalling bookmarks via Spatial Bookmark Manager, importing/exporting bookmarks to XML, switching between User and Project bookmarks, zooming to saved map extents, organizing bookmarks into groups
- [Using the Temporal Controller](map-visualization/using-temporal-controller/guide.md) — Animate and filter map data by time
  - **Use when:** enabling temporal properties on layers, animating map data over time, setting animation range and step size, exporting frame sequence for video, using fixed range temporal filtering, configuring cumulative range mode

### Vector Data

- [Editing Vector Geometry](vector-data/editing-vector-geometry/guide.md) — Digitize, reshape, split, merge, and modify vector features
  - **Use when:** digitizing and sketching vector features, snapping and topological editing, vertex tool selection and editing, reshaping and splitting geometries, advanced digitizing panel coordinates, shape digitizing toolbar
- [Working with the Attribute Table](vector-data/working-with-attribute-table/guide.md) — View, edit, sort, filter, and calculate field values
  - **Use when:** opening attribute table, filtering features by expression, bulk updating field values with field calculator, creating virtual fields, multi-edit mode for batch attribute changes, selecting features by expression
- [Configuring Vector Layer Properties](vector-data/configuring-vector-properties/guide.md) — Set symbology, labels, rendering, and metadata for vector layers
  - **Use when:** styling vector layers with renderers, configuring label placement and text, setting scale-dependent visibility, adjusting layer opacity and blending modes, editing layer metadata, saving and loading named styles
- [Joining and Relating Layers](vector-data/joining-and-relating-layers/guide.md) — Create table joins and relations between vector layers
  - **Use when:** joining layers by shared field, configuring one-to-many relations, setting up many-to-many with pivot table, discovering PostgreSQL relations, editing joined attributes with upsert/cascade, adding polymorphic relations
- [Selecting Features](vector-data/selecting-features/guide.md) — Select features by expression, location, or interactive tools
  - **Use when:** selecting features by area or polygon or freehand or radius, selecting features by expression or attribute value, selecting by location or within distance, inverting or reselecting features, copying selected features to new layer, using selection toolbar and sketches
- [Identifying Features](vector-data/identifying-features/guide.md) — Click features to inspect their attributes and geometry
  - **Use when:** identifying feature attributes on map click, using Identify Results panel, querying multiple layers with identify mode, copying feature attributes, configuring identifiable layer capabilities, zooming to identified feature

### Raster, Mesh, and Point Cloud Data

- [Configuring Raster Layer Properties](raster-and-mesh-data/configuring-raster-properties/guide.md) — Set band rendering, transparency, pyramids, and histogram for rasters
  - **Use when:** setting raster band rendering and symbology, adjusting raster transparency and no-data pixels, building raster pyramids for performance, computing raster histogram, configuring raster resampling method
- [Using the Raster Calculator](raster-and-mesh-data/using-raster-calculator/guide.md) — Perform map algebra operations on raster bands
  - **Use when:** raster calculator expressions, map algebra on raster bands, creating on-the-fly virtual raster, masking raster pixels by condition, setting output extent and resolution, converting or classifying raster values
- [Working with Mesh Layers](raster-and-mesh-data/working-with-mesh-layers/guide.md) — Load, style, edit, and analyze mesh datasets
  - **Use when:** loading mesh layers from GRIB/NetCDF/XMDF, styling mesh contours and vector arrows, animating mesh temporal timesteps, digitizing and editing mesh elements, using Force by Selected Geometries for break lines, running Mesh Calculator expressions
- [Working with Point Clouds](raster-and-mesh-data/working-with-point-clouds/guide.md) — Load, style, and explore LiDAR and other point cloud data
  - **Use when:** loading LAS/LAZ files, styling point cloud symbology, filtering points by classification, configuring eye dome lighting, creating virtual point cloud VPC, inspecting point cloud statistics
- [Working with Vector Tiles](raster-and-mesh-data/working-with-vector-tiles/guide.md) — Load and style vector tile datasets
  - **Use when:** adding vector tile connections via Data Source Manager, styling vector tile layers with symbology rules, importing MapBox GL JSON styles, setting zoom-dependent visibility, configuring MBTiles and XYZ tile sources
- [Working with 3D Tiles](raster-and-mesh-data/working-with-3d-tiles/guide.md) — Load and configure 3D tile datasets for visualization
  - **Use when:** adding 3D tiled scene layer, configuring 3D Tiles symbology and wireframe renderer, adjusting maximum screen space error, setting up 3D map view for Cesium tiles, applying elevation scale and offset to 3D tiles, loading Google Photorealistic 3D Tiles

### Styling and Labeling

- [Managing the Style Library](styling-and-labeling/managing-styles/guide.md) — Organize, import, export, and share symbols and styles
  - **Use when:** opening Style Manager dialog, importing/exporting style XML files, creating color ramps, tagging and organizing symbols, browsing online styles from hub.qgis.org, defining legend patch shapes
- [Configuring Symbols](styling-and-labeling/configuring-symbols/guide.md) — Create and customize marker, line, and fill symbols
  - **Use when:** configuring marker/line/fill symbols, stacking symbol layers in Symbol Selector, setting custom dash patterns, using Geometry generator expressions, parametrizing SVG symbols, saving symbols to style library
- [Setting Labels](styling-and-labeling/setting-labels/guide.md) — Configure text labels with placement, formatting, and rendering rules
  - **Use when:** configuring label font and HTML formatting, adding label buffers and shadows, setting label placement for points lines and polygons, using callouts and mask tabs, controlling label overlap and priority, adding background shapes to labels
- [Creating 3D Symbols](styling-and-labeling/creating-3d-symbols/guide.md) — Define symbol styles for 3D map visualization
  - **Use when:** creating 3D point line polygon symbols in Style Manager, extruding polygons with data-defined height, setting altitude clamping modes, applying Phong or PBR shading materials, importing custom 3D models (.obj .glTF .fbx), configuring rendered facade walls and roofs

### Expressions

- [Writing Expressions](expressions/writing-expressions/guide.md) — Build expressions for labeling, filtering, styling, and calculations
  - **Use when:** writing QGIS expressions, using the Expression string builder dialog, quoting field names and strings in expressions, conditional labeling with CASE WHEN, creating custom Python functions in Function Editor, saving user expressions across projects
- [Using Expression Functions](expressions/using-expression-functions/guide.md) — Reference available functions for geometry, string, math, and aggregates
  - **Use when:** writing geometry expressions for area and length, using spatial predicates like intersects and contains, formatting label text with string functions, computing aggregate statistics across features, buffering and transforming geometries in expressions, using cross-layer aggregate functions

### Print Layout and Map Export

- [Designing Print Layouts](print-layout/designing-print-layouts/guide.md) — Create and configure map compositions for printing or export
  - **Use when:** creating print layouts, adding map/scale bar/legend/label items, aligning items with guides and snapping, exporting layout as PDF/image/SVG, configuring atlas for batch export, saving layout as .qpt template
- [Adding Layout Items](print-layout/adding-layout-items/guide.md) — Insert maps, legends, scale bars, tables, and images into a layout
  - **Use when:** adding map items to print layout, inserting legend in layout, adding scale bar, adding attribute table to layout, inserting north arrow or picture, positioning and resizing layout items
- [Creating Print Output](print-layout/creating-print-output/guide.md) — Export layouts as PDF, image, or SVG
  - **Use when:** exporting print layout as image or PDF, generating georeferenced world file, exporting layout as SVG, creating geospatial PDF, generating atlas map book, cropping export to content
- [Creating Reports](print-layout/creating-reports/guide.md) — Build multi-page reports with iterating sections
  - **Use when:** creating multi-page reports, adding report headers and footers, configuring field group sections for atlas iteration, nesting child field groups, data-defining dynamic images in reports, exporting reports as PDF

### Processing Framework

- [Using the Processing Toolbox](processing-framework/using-processing-toolbox/guide.md) — Find and run geoprocessing algorithms from the toolbox
  - **Use when:** searching Processing Toolbox algorithms, running geoprocessing tools, saving output to GeoPackage or database, batch processing multiple inputs, copying algorithm as Python command, reprojecting layers for third-party tools
- [Building Graphical Models](processing-framework/building-graphical-models/guide.md) — Chain processing algorithms into reusable workflow models
  - **Use when:** creating graphical processing models, chaining algorithms in Model Designer, wiring model inputs and outputs, saving .model3 files, exporting model as Python script, debugging model with partial runs
- [Running Batch Processes](processing-framework/running-batch-processes/guide.md) — Execute an algorithm on multiple inputs in one operation
  - **Use when:** running algorithms as batch process, autofilling batch parameters with expressions, saving batch configuration as JSON, adding input files by pattern or directory, naming batch outputs with incremental suffixes, loading batch results on completion
- [Writing Processing Scripts](processing-framework/writing-processing-scripts/guide.md) — Create custom processing algorithms in Python
  - **Use when:** creating custom processing scripts, extending QgsProcessingAlgorithm, using @alg decorator, chaining algorithms with processing.run, declaring script inputs and outputs, reporting progress with feedback object
- [Running Vector Geoprocessing](processing-framework/running-vector-geoprocessing/guide.md) — Execute buffer, clip, dissolve, intersection, and other vector operations
  - **Use when:** buffering vector features, dissolving geometries by attribute, clipping layers to polygon boundary, computing layer intersection, running symmetrical difference, union of overlapping layers
- [Running Raster Analysis Algorithms](processing-framework/running-raster-analysis/guide.md) — Execute hillshade, slope, aspect, and other terrain analysis tools
  - **Use when:** generating hillshade from DEM, calculating slope and aspect, filling sinks for hydrological analysis, using raster calculator expressions, computing zonal statistics, chaining raster tools in Graphical Modeler
- [Configuring External Applications](processing-framework/configuring-external-applications/guide.md) — Set up GDAL, GRASS, SAGA, and other third-party processing providers
  - **Use when:** configuring GRASS path in Processing providers, enabling GDAL algorithms, setting up R provider plugin, configuring LAStools folder with Wine, setting OTB folder and application path, handling format compatibility with external tools

### Remote Services and Protocols

- [Connecting to WMS/WMTS Services](remote-services/connecting-to-wms-wmts/guide.md) — Load map imagery from OGC Web Map Services
  - **Use when:** adding a WMS/WMTS connection, configuring WMTS KVP or RESTful URL, setting WMS authentication credentials, selecting layers and image encoding, loading WMS layers as separate or merged, configuring network proxy for WMS
- [Connecting to WFS Services](remote-services/connecting-to-wfs/guide.md) — Load and edit vector features from OGC Web Feature Services
  - **Use when:** connecting to WFS server, configuring WFS connection options, loading WFS layers, filtering WFS features with SQL, editing WFS-T features, detecting WFS server version
- [Using STAC Catalogs](remote-services/using-stac-catalogs/guide.md) — Browse and load data from SpatioTemporal Asset Catalogs
  - **Use when:** creating a STAC connection in Browser panel, browsing static STAC catalogs, filtering STAC API results by extent and date, downloading STAC assets, viewing STAC item details and footprints, adding cloud-optimized rasters from STAC
- [Connecting to ArcGIS REST Servers](remote-services/connecting-to-arcgis-rest/guide.md) — Load layers from ArcGIS MapServer and FeatureServer endpoints
  - **Use when:** adding ArcGIS REST Server connection in Data Source Manager, loading MapServer or FeatureServer layers, browsing ArcGIS REST service layers, editing FeatureServer layers in QGIS, converting ArcGIS symbology to QGIS symbols
- [Using XYZ Tile Services](remote-services/using-xyz-tile-services/guide.md) — Add raster basemaps from XYZ tile providers
  - **Use when:** adding XYZ tile basemap, creating custom tile connection, setting tile zoom levels and resolution, decoding terrain RGB tiles, exporting and importing XYZ connections XML, configuring tile service authentication

### Plugins and Scripting

- [Managing Plugins](plugins-and-scripting/managing-plugins/guide.md) — Install, update, enable, and remove QGIS plugins
  - **Use when:** installing QGIS plugins, adding third-party plugin repositories, installing plugin from ZIP, enabling experimental or deprecated plugins, upgrading or uninstalling plugins, Plugin Manager dialog settings
- [Using the Python Console](plugins-and-scripting/using-python-console/guide.md) — Run Python commands and scripts within QGIS
  - **Use when:** opening QGIS Python console, running PyQGIS scripts in built-in editor, using console command history and auto-completion, executing shell commands from Python console, configuring Python console editor options, accessing PyQGIS API docs from console
- [Using GRASS GIS Integration](plugins-and-scripting/using-grass-integration/guide.md) — Access GRASS tools, manage mapsets, and edit GRASS vector layers
  - **Use when:** loading GRASS layers in Browser panel, importing data into GRASS mapset, enabling GRASS plugin, setting GRASS region extent and resolution, digitizing topological vectors, running GRASS Toolbox modules
- [Tracking GPS Data](plugins-and-scripting/tracking-gps-data/guide.md) — Connect to GPS devices and perform live tracking
  - **Use when:** connecting GPS receiver in QGIS, configuring GPS serial port or Bluetooth, logging GPS tracks to GeoPackage, digitizing features from live GPS, viewing satellite signal strength, rotating map to match GPS direction


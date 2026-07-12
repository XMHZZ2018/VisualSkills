# Identifying Features (QGIS 3.44)

The **Identify Features** tool lets you click anywhere on the map canvas and instantly see attribute and geometry information for whatever's underneath. It works with nearly every layer type QGIS supports — vector, raster, mesh, point cloud, WMS, WFS, and more.

Activate it from **View > Identify Features**, press `Ctrl+Shift+I`, or click the **Identify Features** button on the Attributes toolbar. Then click a feature or pixel on the active layer. The clicked item highlights on the canvas and its details appear in the **Identify Results** panel.

See `fig01.png`.

At the bottom of the results panel, the **Mode** dropdown controls which layers get queried. Set it to **Current layer** to restrict results to whatever's selected in the Layers panel, **Top down, stop at first** to get only the topmost hit, **Top down** to query all visible layers, or **Layer selection** for a context menu letting you pick the exact layer.

The **View** dropdown switches between a **Tree** (the default hierarchical list), **Table** (for raster layers), or **Graph** layout. In Tree view, each result nests under its layer name — expand a feature to see derived geometry properties like area, perimeter, and vertex count alongside your regular attribute fields.

Beyond simple clicking, a dropdown in the toolbar offers alternative identify modes: **Identify by rectangle** (click-and-drag), **by mouse-over** (hover to highlight), **by polygon** (draw or pick an existing polygon), **by freehand**, or **by radius**. Right-clicking during a rectangle identify gives a contextual list of overlapping features grouped by layer, so you can choose exactly which one to inspect.

Right-click any result in the panel for a context menu with handy actions: **Zoom to feature**, **Copy feature attributes**, **Toggle feature selection**, **View feature form** to inspect or edit attributes directly, or **Highlight all** to flash every identified item on the canvas.

To keep certain layers from responding to identify clicks, go to **Project > Properties... > Data Sources > Layer Capabilities** and uncheck the **Identifiable** column for those layers. Under the **Identify Settings** gear icon in the panel, you can also enable **Auto open form for single feature results** — great when you want to immediately edit attributes without an extra click.

# Identifying Features (QGIS 3.44)

The **Identify Features** tool lets you click anything on the map canvas — vector, raster, mesh, point cloud, even WMS — and instantly see its attributes and geometry details in a popup panel.

Activate it from **View > Identify Features**, press `Ctrl+Shift+I`, or click the **Identify Features** button on the Attributes toolbar. Then click a feature on the map. The clicked item highlights, and the Identify Results panel opens showing its field values, derived geometry properties (area, perimeter, coordinates), and any related features.

At the bottom of the results panel, the **Mode** dropdown controls which layers get queried: *Current layer* (only the active layer), *Top down, stop at first* (topmost hit only), *Top down* (all layers under the click), or *Layer selection* (you pick from a context menu).

Beyond simple clicks, a dropdown in the panel toolbar offers alternative identify methods: click-and-drag a rectangle, hover to identify on mouse-over, draw a polygon or freehand shape, or specify a radius. Each returns all overlapping features from the target layers.

Right-click any result to **Zoom to feature**, **Copy feature attributes**, **Toggle feature selection**, or **Open the feature form** for quick edits. You can also highlight all results at once or activate the source layer directly from the context menu.

To exclude noisy layers from results, go to **Project > Properties... > Data Sources > Layer Capabilities** and uncheck the *Identifiable* column for layers you want to skip. Under the panel's **Identify Settings** gear icon, toggle options like *Auto open form for single feature results* or *Hide NULL values from results* to streamline your workflow.

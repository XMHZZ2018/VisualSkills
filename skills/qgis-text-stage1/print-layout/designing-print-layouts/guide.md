# Designing Print Layouts (QGIS 3.44)

Open a new layout via **Project > New Print Layout** and give it a name. You'll land on a blank canvas representing your paper — the left toolbar has everything you need to populate it.

Grab the **Add Map** tool from the left toolbar and drag a rectangle on the canvas to place your map view. Then do the same with **Add Scale Bar**, **Add Legend**, and **Add Label** to build out the composition. Use **Select/Move Item** (`V`) to reposition or resize anything — drag corner handles to scale.

Each item you select exposes its settings in the **Item Properties** panel on the right. That's where you adjust map rotation, legend contents, scale bar style, and label text. The **Layout** panel above it controls global settings like export resolution, the reference map (used for georeferencing and coordinate calculations), and grid/guide snapping.

For precise alignment, enable **View > Show Guides** and **View > Snap to Guides**, then drag from the rulers to place guide lines. **Smart Guides** (`Ctrl+Alt+;`) snap to other items dynamically as you move things around.

Multi-page layouts are supported — use **Layout > Add Pages…** to insert pages of any size or orientation. Right-click a page and choose **Page Properties…** to change its background or exclude it from export.

When you're happy, export via **Layout > Export as PDF…**, **Export as Image…**, or **Export as SVG…**. The output is automatically georeferenced based on your reference map. For batch output across features, configure the **Atlas** panel and export from the **Atlas** menu.

Save the layout as a reusable `.qpt` template with **Layout > Save as Template…**, or manage all your layouts from **Project > Layout Manager…**.

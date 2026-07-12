# Designing Print Layouts (QGIS 3.44)

To start a new layout, go to **Project > New Print Layout** in the main QGIS window (or hit `Ctrl+N` from within an existing layout). You'll be asked for a title — pick something descriptive since the **Layout Manager** (**Project > Layout Manager…**) lists all layouts in the project and lets you duplicate, rename, or delete them.

The layout window opens with a blank canvas representing your paper. On the left toolbar you'll find all the item tools: **Add Map**, **Add Legend**, **Add Scale Bar**, **Add Label**, plus shapes, tables, pictures, and more. Draw a rectangle on the canvas to place each item. Use **Select/Move Item** (`V`) to reposition or resize things afterward — drag the corner handles to scale.

See `fig01.png`.

On the right side, the **Item Properties** panel is where the real customization happens. Click any item on the canvas and its settings appear there — map extent, legend entries, scalebar style, label text, rotation, and so on. The **Layout** panel above it controls page-level settings: export resolution, reference map (used for georeferencing and scale), and grid/guide snapping preferences.

For precise alignment, enable **View > Show Guides** and **View > Snap to Guides**. Drag from the rulers to create guide lines, or use the **Guides** panel for exact coordinate placement. Smart guides (snapping to other items' edges) activate via **View > Smart Guides**.

Pages can be mixed sizes and orientations — add more through **Layout > Add Pages…** and set each page's dimensions independently in its properties. Right-click empty canvas space and choose **Page Properties…** to change the background or size of the current page.

See `fig02.png`.

When you're ready to export, use **Layout > Export as PDF…**, **Export as Image…**, or **Export as SVG…**. The export resolution defaults from the Layout panel but can be overridden per export. Check **Print as raster** if you're using blending modes that don't render well as vectors, or **Always export as vectors** to keep everything crisp. Georeferencing is automatic for formats that support it (TIFF, PDF) based on your reference map item.

Save your composition as a reusable `.qpt` template with **Layout > Save as Template…**, then load it into any future layout via **Add Items from Template** or the Layout Manager's template picker. You can also drag a `.qpt` file onto the map canvas from the Browser panel to instantly spin up a new layout from it.

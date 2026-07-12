# Decorating the Map (QGIS 3.44)

Decorations are lightweight cartographic elements — grid, title, copyright, north arrow, scale bar, and more — drawn directly on the map canvas. They all live under **View > Decorations**, and any changes you make are saved with the project file.

**Grid.** Open **View > Decorations > Grid…** and tick **Enable Grid**. Choose between a Line or Marker grid type, then set the X/Y interval and offset in map units. You can auto-fill sensible values by clicking **Canvas Extents** or **Active Raster Layer**. Enable **Draw Annotations** to label grid lines — pick an annotation direction (horizontal, vertical, or boundary-following), set the font, and adjust the distance from the map frame.

See `fig01.png`.

**Title Label.** Head to **View > Decorations > Title Label…**, tick **Enable Title Label**, and type your text. The label supports QGIS expressions for dynamic content (click the expression button). Choose a font, set a background bar colour, pick a placement corner (default is Top Center), and fine-tune position with margin values in mm, px, or percentage.

**Copyright Label.** Almost identical to the title workflow: **View > Decorations > Copyright Label…**. It defaults to the Bottom Right corner — handy for attribution text. Same font, expression, and margin controls apply.

**Image Decoration.** Use **View > Decorations > Image…** to overlay a logo or legend graphic. Browse to a PNG, JPG, or SVG file, set its size in mm, and pick a corner. SVG images additionally let you customise fill and stroke colours.

**North Arrow.** Open **View > Decorations > North Arrow…** and tick **Enable north arrow**. Adjust fill/outline colour, size, and optionally load a custom SVG. Leave the angle on **Automatic** and QGIS will align the arrow to true north based on your project CRS. Place it in any corner with optional margin offsets.

See `fig02.png`.

**Scale Bar.** Go to **View > Decorations > Scale Bar…** and enable it. Pick a style (Single Box, Double Box, Tick Down, etc.), set fill and outline colours, choose a font, and define the bar's size in the project's active distance unit. Tick **Automatically snap to round number on resize** for clean labels as you zoom. Place it wherever suits your map.

See `fig03.png`.

**Layout Extents.** If you're working with print layouts, **View > Decorations > Layout Extents** overlays a dotted rectangle showing exactly what each layout's map item will capture — invaluable for positioning labels without constantly switching to the layout view.

All decorations persist in the project and can be included when exporting the canvas via **Project > Import/Export** by ticking **Draw active decorations**.

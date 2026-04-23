# Architecture Diagrams (LibreOffice Impress 7.3.7)

Start by laying out your tier structure using basic shapes. Open the Drawing toolbar and pick **Rectangle** from the regular shapes — click the triangle ▼ next to the shape icon to access sub-categories like **Block Arrows** or **Flowchart** if you need something more specific. Click and drag on the slide to place each shape, holding **Shift** to constrain it to a square or equal proportions.

To label a shape, just double-click it and start typing. You can format the text through **Format > Character** or **Format > Paragraph** for alignment. Give each tier's components distinct fill colors via **Format > Object and Shape > Area** so the diagram reads at a glance.

For tier groupings (e.g., "Presentation Tier," "Business Logic," "Data Tier"), draw a large rectangle behind the component shapes to act as a visual container. Send it to the back with **Format > Object and Shape > Behind Object** or right-click and choose the stacking order. Add a label to this background rectangle to name the tier.

Now wire everything together with connectors. Click the triangle ▼ next to **Connectors** on the Drawing toolbar to pick a connector type — **Standard** gives you right-angle routed lines, **Line** creates segmented paths, **Straight** draws direct lines, and **Curved** uses Bézier curves. Hover over a shape until you see the glue points (small crosses at the edges), then click and drag from one glue point to another shape's glue point. The connector stays attached even when you reposition shapes.

Visual reference: connectors linking shapes via glue points, showing right-angle and curved connector types.

To fine-tune a connector's routing, right-click it and select **Connector** to open the properties dialog, where you can adjust **Line Spacing** values and change the connector **Type**. If the default glue points aren't in the right spot, open the Glue Points toolbar via **View > Toolbars > Glue Points**, click **Insert Glue Point**, and place custom attachment points exactly where you need them.

Visual reference: the Connector dialog with Type, Line Skew, and Line Spacing settings.

Once your diagram is assembled, select all the shapes in a single tier by holding **Shift** and clicking each one, then group them with **Format > Group > Group** (or **Ctrl+Shift+G**). This locks their relative positions so you can move or resize an entire tier as one unit. To edit an individual shape inside a group later, press **F3** or go to **Format > Group > Enter Group**, make your changes, then **Format > Group > Exit Group** to return.

Visual reference: three grouped shapes (rectangle, ellipse, diamond) selected as a single unit with shared selection handles.

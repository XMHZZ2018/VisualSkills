# Connectors and glue points (LibreOffice Impress 7.3)

Connectors are lines anchored to glue points on the border of objects. When an object with a connector is moved or resized, the connector automatically adjusts. **When creating flowcharts, organization charts, or diagrams, use connectors instead of simple lines.**

## Connectors

### Drawing connectors

1. Click the triangle next to **Connectors** on the Drawing toolbar to open the Connectors sub-toolbar.
2. Select the type of connector required.
3. Move the cursor over one of the objects to be connected — small crosses appear around the object edges (these are glue points).
4. Click on a glue point to attach one end of the connector, then hold and drag to another object.
5. When the cursor is over a glue point of the target object, release — the connector is drawn.
6. Use the square selection handles on the connector to adjust its path.

### Connector types

Connectors fall into four type groups:

- **Standard** — name starts with *Connector*. Line segments run vertically and horizontally with 90-degree bends.
- **Line** — name starts with *Line*. A line segment with smaller segments at the ends that bend near glue points.
- **Straight** — name starts with *Straight*. A single straight line connector.
- **Curved** — name starts with *Curved*. Based on Bezier curves, creating a curved line connector.

Each type comes with different termination shapes: none, arrow, or circle at start/end.

### Formatting connectors

- To **detach or reposition**: click on a round selection handle at either end and drag to a different location.
- To **change the route**: click on a square control handle on the connector line and drag it.
- To **change connector type**: right-click the connector > **Connector** to open the Connector dialog.

**Connector dialog options:**
- **Type** — select connector type from the drop-down list.
- **Line skew** — defines the skew of the line; sets the distance between overlapping connectors.
- **Line spacing** — sets the horizontal and vertical space between the connector and the object at each end (Begin horizontal, End horizontal, Begin vertical, End vertical).
- **Preview window** — left click zooms in, right click zooms out.

**Note:** The ends of a connector cannot be swapped. To swap direction, create a new connector in the opposite direction.

---

## Glue points

Glue points fix a connector to an object so the connector stays attached when the object moves. All objects have glue points (visible only when **Connectors** is selected on the Drawing toolbar). By default, most objects have four glue points.

### Opening the Glue Points toolbar

- **View > Toolbars > Glue Points**
- **Edit > Glue Points**
- Click **Show Glue Point Functions** on the Drawing toolbar.

### Glue point types

The left six tools on the Glue Points toolbar:
- **Insert Glue Point** — inserts a glue point when clicking twice on an object.
- **Exit Direction Left/Top/Right/Bottom** — connector attaches to the specified edge of the selected glue point.
- **Glue Point Relative** — maintains the relative position of a glue point when the object is resized (selected by default).

### Inserting glue points

1. Open the Glue Points toolbar (no objects selected).
2. Select the object, then click **Insert Glue Point**.
3. Click on the position within the object to insert the glue point.
4. Repeat to insert more glue points.
5. Select the glue point type from the toolbar options.
6. Drag glue points to reposition them.
7. Deselect **Insert Glue Point** when done.

### Customizing glue point exit direction

1. Open the Glue Points toolbar.
2. Double-click on an inserted glue point to select it.
3. Select an exit direction from the Glue Points toolbar, or right-click and select the exit direction.
4. Deselect **Insert Glue Point** when done.

### Deleting glue points

1. Open the Glue Points toolbar.
2. Select the previously inserted glue point.
3. Press **Delete** or **Backspace**, or go to **Edit > Cut**.

**Note:** Only glue points that have been manually inserted can be customized or deleted. The default four glue points cannot be removed.

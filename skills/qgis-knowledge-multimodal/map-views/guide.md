Here is the multimodal guide:

---

QGIS 3.44 provides a 2D map canvas as the central workspace and an optional 3D map view for terrain and volumetric visualization, both accessible from the **View** menu.

## 2D Map View

Read the screenshot `fig01.png` in this directory — it shows the full QGIS GUI layout with the map canvas (center), Layers panel (left), Browser panel (upper-left), and Processing Toolbox (right), with the status bar along the bottom showing coordinates, scale, magnifier, and rotation.

The 2D map canvas opens by default when QGIS starts. When you add a layer, QGIS reprojects it on-the-fly to the project CRS and zooms to its extent (if the canvas is otherwise blank).

### Navigation Tools

Navigation tools live in the **Navigation Toolbar** (second toolbar row) and are also accessible via **View** menu.

| Tool | Icon | Action |
|------|------|--------|
| Pan Map | Read the screenshot `fig03.png` in this directory — it shows the pan hand cursor icon | Left-click to center; click-drag to pan |
| Zoom In | Read the screenshot `fig05.png` in this directory — it shows the zoom-in magnifier with a + symbol | Left-click to double scale; drag rectangle to zoom to area; hold **Alt** to temporarily switch to Zoom Out |
| Zoom Out | Read the screenshot `fig07.png` in this directory — it shows the zoom-out magnifier with a – symbol | Left-click to halve scale; drag rectangle to zoom out; hold **Alt** to temporarily switch to Zoom In |
| Pan to Selection | Read the screenshot `fig13.png` in this directory — it shows the pan-to-selected icon (map with arrow) | Centers canvas on selected features across all selected layers |
| Zoom to Selection | Read the screenshot `fig15.png` in this directory — it shows the zoom-to-selected icon (magnifier over features) | Zooms to selected features; also in layer right-click context menu |
| Zoom Full | Read the screenshot `fig11.png` in this directory — it shows the zoom-full-extent icon | Zooms to the extent of all project layers |

**Keyboard shortcuts:**
- **Space + drag** — pan
- **Arrow keys** — pan in cardinal directions
- **PgUp** / `Ctrl++` — zoom in
- **PgDown** / `Ctrl+-` — zoom out
- **Shift + drag rectangle** — zoom to area (when Identify or Measure tool is active)
- **Esc** — stop map rendering mid-draw

**Mouse shortcuts:**
- **Mouse wheel** — zoom in/out (hold **Ctrl** for finer steps)
- **Middle-click + drag** — pan
- **Back/Forward mouse buttons** — navigate zoom history

**Right-click** on the canvas to copy coordinates of the clicked point in the map CRS, WGS84, or a custom CRS.

### Controlling Rendering

To suspend all rendering (useful when loading many layers before drawing):
1. Uncheck the **Render** checkbox in the bottom-right corner of the status bar.
2. Add/configure your layers.
3. Re-check **Render** — the canvas refreshes immediately.

To stop an in-progress render: press **Esc**.

### Temporal Navigation

For time-aware layers, enable the **Temporal Controller** panel via:
- **View › Panels › Temporal controller panel**, or
- **View › Data Filtering › Temporal controller panel**, or
- The clock icon in the Map Navigation toolbar.

Modes include: off, fixed range, animated (step through time), and movie (frame-by-frame without time filtering). Configure frame rate and cumulative range in the Settings tab of the panel.

---

## 3D Map View

### Opening a 3D View

Go to **View › 3D Map Views › New 3D Map View**.

Read the screenshot `fig02.png` in this directory — it shows the New 3D Map View toolbar button icon.

A floating/dockable panel appears. To manage existing views (rename, duplicate, remove): **View › 3D Map Views › Manage 3D Map Views**. Views are saved with the project even when hidden.

Read the screenshot `fig04.png` in this directory — it shows the 3D Map View dialog with a city rendered in 3D, a compass rose in the upper-right, navigation arrows on the right edge, and a keyframe/animation bar at the bottom.

### 3D Toolbar Tools

The toolbar runs across the top of the 3D panel:

- **Camera Control** — Read the screenshot `fig06.png` in this directory — it shows the pan/camera-control hand icon. Moves the camera laterally without changing angle or direction.
- **Zoom Full** — Read the screenshot `fig08.png` in this directory — it shows the zoom-full icon. Fits the view to all layers or the configured reference extent.
- **Toggle On-Screen Navigation** — Read the screenshot `fig10.png` in this directory — it shows the 3D navigation widget icon (compass rose). Shows/hides the on-screen navigation widget for mouse-free camera control.
- **Identify** — Read the screenshot `fig12.png` in this directory — it shows the identify cursor (arrow with info badge). Click terrain or a 3D feature to return attribute information.
- **Measurement Line** — Read the screenshot `fig14.png` in this directory — it shows the measurement ruler icon. Click to add points; right-click to finish; reports horizontal, vertical, and total 3D distance.

### 3D Navigation Controls

In the 3D canvas:
- **Left-click + drag** — rotate/tilt the view
- **Middle-click + drag** (or **Shift + drag**) — pan the camera
- **Scroll wheel** — zoom in/out
- **Ctrl + drag** — fine tilt/rotation

The on-screen compass widget (top-right of the 3D panel) provides clickable arrows for pan, rotate, and tilt without a mouse.

### Configuring the 3D Scene

Click **Configure…** (gear icon) in the 3D panel toolbar to open the 3D configuration dialog.

**General tab:** Set a spatial extent to clip the scene — only terrain and features within that extent load. Enable **Show in 2D map view** to display the 3D camera footprint as a rubber band on the main canvas.

**Terrain tab:** Choose the terrain type:
- Flat
- DEM raster layer
- Online (Mapzen elevation tiles)
- Mesh dataset
- Quantized Mesh layer

Key terrain settings:
- **Vertical scale** — exaggerate elevation differences
- **Tile resolution** — higher values = more detail, more GPU cost
- **Skirt height** — fills cracks between terrain tiles
- **Offset** — shift terrain up/down to align with point clouds or other data

### Camera / 2D–3D Sync

Use the **Camera** menu in the 3D toolbar to:
- Sync the 2D canvas to follow the 3D camera, or vice versa
- Show the camera's visible area as an overlay on the 2D canvas
- Clip the 3D scene to an extent drawn on the 2D canvas (**Set 3D scene on 2D map view**)
- Draw a **Cross Section** through the terrain: click start point on the 2D canvas, move to define direction, click end point; use **Disable Cross Section** to remove it

### Exporting the 3D Scene

Use the **Export** menu in the 3D toolbar:
- **Save as Image…** — exports current 3D view to PNG/JPG
- **Export 3D Scene** — saves as `.obj` for post-processing in Blender or similar; configure scene name, terrain resolution, texture resolution, model scale, smooth edges, normals, and textures

### Visual Effects

Click the **Effects** button (shadow icon) to enable:
- **Shadows**
- **Eye dome lighting** (improves depth perception for point clouds)
- **Ambient occlusion** (adds contact shadow realism)
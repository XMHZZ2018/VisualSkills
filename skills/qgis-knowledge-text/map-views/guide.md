2D and 3D map canvas interaction, navigation tools, and spatial visualization in QGIS.

## 2D Map Canvas

The main map canvas is the central view, automatically linked to the Layers panel. When you add a layer, QGIS zooms to its extent (if the project is empty); otherwise it stays at the current view.

### Navigation Tools & Shortcuts

Find navigation tools in the **Navigation Toolbar** or **View** menu.

| Action | Tool / Shortcut |
|---|---|
| Pan | Click+drag, or `Space`+mouse, or arrow keys |
| Zoom In | Scroll up, `PgUp`, `Ctrl++`, or click/drag with Zoom In tool |
| Zoom Out | Scroll down, `PgDown`, `Ctrl+-`, or click/drag with Zoom Out tool |
| Fine zoom | `Ctrl`+scroll wheel |
| Zoom to full extent | **Zoom Full** button |
| Zoom to selected features | **Zoom To Selection** (also in layer right-click menu) |
| Zoom to layer(s) | **Zoom To Layer(s)** (also in layer right-click menu) |
| Pan to selection | **Pan Map to Selection** |
| Back/forward in zoom history | **Zoom Last** / **Zoom Next**, or mouse back/forward buttons |
| Zoom to native raster resolution | **Zoom to Native Resolution** (layer right-click menu) |
| Zoom to area (while Identify/Measure active) | `Shift`+drag rectangle |
| Stop rendering | `Esc` |
| Copy coordinates at click point | Right-click on canvas → Copy coordinates (map CRS, WGS84, or custom) |

### Controlling Rendering

- **Suspend rendering**: uncheck the **Render** checkbox in the bottom-right status bar. Use this before loading many large layers or configuring symbology — re-check to trigger a refresh.
- Rendering also triggers on: layer visibility toggle, symbology changes, adding layers, pan/zoom, window resize.

## Temporal Navigation

Use this to animate time-aware layers (vector, raster, WMTS, mesh).

### Setup

1. Enable temporal properties on individual layers (Layer → Properties → Temporal tab).
2. Open the **Temporal Controller Panel**: click the clock icon in the Map Navigation toolbar, or **View → Panels → Temporal controller panel**.

### Temporal Controller Modes

- **Turn off temporal navigation** — disables all time filtering; layers render normally.
- **Fixed range** — set a start/end time; only features whose time range overlaps are shown.
- **Animated** — splits a time range into steps and plays through them frame by frame.
- **Animated movie** — advances through a fixed frame count without time-based filtering.

Settings include **Frame rate** (frames/second) and **Cumulative range** (accumulate data from start rather than a sliding window).

Layers with temporal control active show a clock indicator icon in the Layers panel; click it to edit temporal settings.

## 3D Map View

### Opening a 3D View

**View → 3D Map Views → New 3D Map View** — opens a floating/dockable panel matching the 2D canvas extent.

Manage existing views: **View → 3D Map Views → Manage 3D Map Views** (open, duplicate, remove, rename). Views are saved with the project even when turned off.

### 3D Toolbar Buttons

| Button | Function |
|---|---|
| Camera Control | Move camera (pan), keeping angle/direction |
| Zoom Full | Fit view to all layers (or reference extent) |
| Toggle On-Screen Navigation | Show/hide navigation widget |
| Identify | Click terrain or 3D features for info |
| Measurement Line | Click to add points, right-click to finish; measures horizontal/vertical/3D distance |
| Animations | Show/hide animation player |
| Export | Save as image or export as 3D scene (.obj for Blender etc.) |
| Set View Theme | Choose a predefined map theme |
| Camera menu | Sync 2D↔3D views; show camera area in 2D; cross-section tool |
| Effects | Shadows, eye dome lighting, ambient occlusion |
| Configure… | Opens full 3D scene configuration dialog |

### 3D Scene Configuration

Open via the **Configure…** button. Key tabs:

**General tab**
- Limit scene to a 2D map extent (clips terrain and features to that area).
- Check **Show in 2D map view** to display the 3D scene extent as a rubberband on the 2D canvas.

**Terrain tab**
- **Type**: Flat, DEM raster layer, Online (Mapzen), Mesh dataset, or Quantized Mesh.
- **Vertical scale**: exaggerate elevation differences.
- **Tile resolution**: higher = more detail but slower rendering (default 16px per tile).
- **Skirt height**: raise to hide cracks between terrain tiles.
- **Offset**: shift terrain up/down to align with point clouds or other layers with different elevation reference.

### 2D↔3D Synchronization

Via the **Camera** menu in the 3D toolbar:
- **2D map view follows 3D camera** and/or **3D camera follows 2D map view**.
- **Set 3D scene on 2D map view**: draw an extent on the 2D canvas to clip what loads in 3D.
- **Cross Section Tool**: click start point, drag to set direction, click end point on 2D canvas — creates a cross-section slice in the 3D view. Press `Esc` or right-click to reset.

## Common Pitfalls

- **Layers not appearing after add**: rendering may be suspended (check the **Render** checkbox in the status bar).
- **3D terrain looks flat**: terrain type defaults to Flat — set it to a DEM raster in Configure → Terrain.
- **Cracks between terrain tiles**: increase **Skirt height** in terrain configuration.
- **Point clouds floating above/below terrain**: use the terrain **Offset** setting to align elevation references.
- **Zoom to area shortcut doesn't work**: `Shift`+drag only works when Identify, Measure, or similar tools are active — not with selection or edit tools active.
- **Alt key in zoom tools**: while Zoom In is active, holding `Alt` temporarily switches to Zoom Out (and vice versa).
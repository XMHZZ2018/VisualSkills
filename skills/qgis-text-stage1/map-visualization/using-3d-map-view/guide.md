# Using the 3D Map View (QGIS 3.44)

Open a 3D view from **View › 3D Map Views › New 3D Map View**. A floating panel appears showing your current 2D extent rendered in perspective. You can dock it, float it, or manage multiple named views from **View › 3D Map Views › Manage 3D Map Views**.

The toolbar across the top gives you **Camera Control** (pan without changing angle), **Zoom Full** (reset to layer or reference extent), **Toggle On-Screen Navigation** (a compass widget for intuitive rotation), **Identify** (click features for attribute info), and **Measurement Line** (click points to get horizontal, vertical, and 3D distances; right-click to finish).

For navigation: drag with the left mouse button to pan, scroll to zoom, and hold `Shift` + drag (or middle-button drag) to tilt and rotate. Arrow keys move the camera; `Page Up`/`Page Down` change altitude. Hold `Ctrl` + drag to pivot the camera in place without moving it.

Hit **Configure…** to open scene settings. Under **Terrain**, pick your elevation source — a flat plane, a DEM raster, an online Mapzen service, a mesh, or quantized mesh tiles. Crank up **Vertical scale** to exaggerate relief, and adjust **Tile resolution** for detail vs. performance.

In the **Lights** tab, add up to eight point lights or four directional lights. Directional lights work like the sun (parallel rays, azimuth + altitude controls); point lights fall off with distance.

The **Effects** tab is where you enable **shadows** (tied to a directional light), **Eye Dome Lighting** (EDL) for enhanced depth on point clouds, and **Screen-Space Ambient Occlusion** (SSAO) to darken crevices. EDL and SSAO combine well together.

Under **Camera & Skybox**, enable a 3D axis (CRS-based or interactive cube — click a cube face to snap the view), set up 2D/3D navigation sync, and optionally add a skybox (panoramic or six-face texture).

To animate a flythrough, toggle **Animations**, click **Add keyframe**, set a time in seconds, then position the camera. Repeat for each keyframe. Press play to preview — QGIS interpolates between positions. Export frames to an image sequence with **Export animation frames**.

For 3D vector rendering, open a vector layer's properties, go to the **3D View** section, and enable **Enable 3D Renderer**. You can export the full scene as an `.obj` file via **Export › Export 3D Scene** for use in Blender or similar tools.

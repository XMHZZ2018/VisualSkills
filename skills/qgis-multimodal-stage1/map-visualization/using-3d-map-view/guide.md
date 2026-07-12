# Using the 3D Map View (QGIS 3.44)

Open a 3D view from **View > 3D Map Views > New 3D Map View**. A floating panel appears showing your current 2D extent rendered in perspective. You can dock it, float it, or manage multiple named 3D views from the same menu — they all persist when you save the project.

See `fig01.png`.

The toolbar across the top gives you **Camera Control** (pan without changing angle), **Zoom Full** (snap to full layer extent), **Toggle On-Screen Navigation** (a compass widget for mouse-based orbit), **Identify** (click features for attribute info), and **Measurement Line** (click points to get horizontal, vertical, and 3D distances — right-click to finish).

To configure the scene, hit the **Configure…** button. The Terrain tab is where the real 3D happens: set the elevation Type to a DEM raster layer, an online service, a mesh, or quantized mesh tiles. Crank up **Vertical scale** to exaggerate relief, and tweak **Tile resolution** for detail vs. performance. If you see hairline cracks between tiles, bump the **Skirt height** value.

See `fig02.png`.

Under **Lights**, you can add up to eight point lights and four directional lights. Directional lights work like the sun — set azimuth and altitude to control shadow direction. The **Effects** tab lets you toggle shadows, Eye Dome Lighting (EDL), and Screen-Space Ambient Occlusion (SSAO). EDL makes edges pop by comparing pixel depths; SSAO darkens crevices for a more grounded look. Both combine well for point cloud scenes.

See `fig03.png` for the four-panel EDL/SSAO comparison.

For navigation: drag with the left button to pan, middle-button drag (or `Shift` + left drag) to tilt and rotate, scroll wheel to zoom, and `Ctrl` + drag to reorient the camera without moving it. `Page Up`/`Page Down` adjusts altitude directly.

To create a flythrough animation, toggle **Animations** in the toolbar, add keyframes with the **+** button at specific times, position the camera for each, then hit play. Choose an interpolation curve (linear, inQuad, outCirc, etc.) and export the frames as an image sequence for video assembly.

You can export the current view as a static image via **Export > Save as Image**, or as a full `.obj` 3D scene for post-processing in Blender. Vector layers participate in the 3D view once you enable **3D Renderer** in their layer properties under the 3D View section.

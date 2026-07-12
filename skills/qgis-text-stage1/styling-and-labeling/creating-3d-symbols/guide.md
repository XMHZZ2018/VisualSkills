# Creating 3D Symbols (QGIS 3.44)

The Style Manager is your hub for building 3D symbols. Open it and switch to the **3D Symbols** tab, then expand the **Add** button to create a new 3D point, line, or polygon symbol.

**Point symbols** offer several shape types — Sphere, Cylinder, Cube, Cone, Plane, Torus, a custom 3D Model (`.obj`, `.glTF`, `.fbx`), or a Billboard that keeps a stable screen size (handy for point clouds). Dimensions are in project CRS units. Under **Transformations**, you can translate, scale, or rotate the shape along any axis.

**Line symbols** use **Width**, **Height**, and **Extrusion** to give flat lines a 3D volume. Toggle **Render as simple 3D lines** if you just want thin strokes without extrusion. **Altitude binding** controls whether clamping happens per-vertex or at the feature centroid.

**Polygon symbols** also support **Extrusion** — and you can data-define it from an attribute so each polygon gets a different height. Set **Rendered facade** to *Walls*, *Roofs*, or *Walls and roofs* to control which faces draw. If faces look wrong, start with **Culling mode → Back** and **Add back faces** disabled; if that's still off, enable **Add back faces** and set culling to *No Culling*.

All geometry types share **Altitude clamping** (Absolute, Relative, or Terrain) which determines how z-values relate to the terrain surface.

**Shading** controls material appearance. *Realistic (Phong)* blends diffuse and specular reflection with an opacity slider. *Realistic Textured (Phong)* adds a diffuse texture image with scale/rotation controls. *CAD (Gooch)* uses warm/cool tones so edges stay prominent. *Metal Roughness* is a PBR material defined by base color, metalness, and roughness. 3D Model shapes can also use *Embedded Textures* directly from the model file.

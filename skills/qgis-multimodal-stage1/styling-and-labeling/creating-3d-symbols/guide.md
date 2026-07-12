# Creating 3D Symbols (QGIS 3.44)

The **Style Manager** is your hub for building 3D symbols. Open it, switch to the **3D Symbols** tab, and expand the add button to create a new 3D point, line, or polygon symbol. Each one gets stored in your style library so you can reuse it across projects and 3D map views.

**Point symbols** offer the most variety in shape. You can pick from Sphere, Cylinder, Cube, Cone, Plane, Torus, a custom 3D Model (`.obj`, `.glTF`, `.fbx`), or a Billboard that renders a flat marker symbol at a fixed screen size — handy for point clouds. Each shape is sized in CRS units, so a Sphere with radius 5 means 5 meters if your project is in a metric CRS. Under **Transformations**, you can translate, scale, and rotate the shape on all three axes to fine-tune placement.

See `fig01.png`.

**Line symbols** are controlled by **Width**, **Height**, and **Extrusion**. If your lines lack Z values, extrusion fakes volume by pushing the geometry upward. You can also toggle **Render as simple 3D lines** for a lightweight wireframe look. **Altitude binding** determines whether clamping uses every vertex individually or the feature's centroid — vertex-level binding follows terrain more closely but costs more to render.

**Polygon symbols** add a few extra tricks. **Extrusion** can be data-defined (use the expression button to pull heights from an attribute column, so each building gets its own roofline). **Rendered facade** lets you choose between Walls, Roofs, or both. If faces look inside-out or invisible, adjust **Culling mode** — start with *Back* culling and *Add back faces* off; if it still looks wrong, switch to *No Culling* with *Add back faces* enabled.

See `fig02.png`.

**Shading** controls how light interacts with your 3D surfaces. *Realistic (Phong)* blends diffuse and specular reflections and supports an opacity slider for semi-transparent objects. *Realistic Textured* is the same but maps an image onto the surface (set texture scale and rotation). *CAD (Gooch)* keeps edges and highlights crisp by restricting shading to mid-tones — you supply warm and cool colors plus alpha/beta blending weights. *Metal Roughness* is a physically based option where you set base color, metalness, and roughness for photorealistic results.

For all geometry types, **Altitude clamping** offers three modes: *Absolute* (Z values are real-world elevations), *Relative* (Z values are offsets above terrain), and *Terrain* (features drape directly onto the surface). Pick the one that matches how your data encodes height.

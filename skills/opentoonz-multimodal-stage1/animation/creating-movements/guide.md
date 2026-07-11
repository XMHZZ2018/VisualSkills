# Creating Movements (OpenToonz 1.7)

Every scene in OpenToonz has transformable objects — columns/layers, pegbars, cameras, and the table. Set a transformation at a specific frame and you've created a keyframe; set two and the software interpolates everything in between. That's your basic animation workflow.

The **Stage Schematic** is where you wire it all together. Open it via **Window > Schematic**, then toggle the FX/Stage button in the bottom bar until the title reads "Stage Schematic." You'll see nodes for every object in your scene arranged in a hierarchy rooted at the Table. Columns appear automatically when you load content; add pegbars or cameras with their respective buttons in the bottom bar, or right-click the schematic background.

See `fig01.png`.

To link objects — creating parent/child relationships for shared or relative movement — drag from a node's left port (child side) to another node's right port (parent side). A column linked to a pegbar inherits that pegbar's motion plus its own. Cameras can be linked too, letting you build complex shots that follow a character. Delete a link via **Edit > Delete** and it reverts to the default parent (the Table).

For animation, grab the **Animate** tool. The **Object** dropdown in the tool options bar lets you pick any column, pegbar, or camera. Set **Mode** to **All** to get the full interactive handle in the viewer — a double-circle with arms for position, rotation, scale, shear, and center. Drag the circle tip to rotate, the double-square tip to scale, the parallelogram tip to shear, and anywhere else to reposition.

See `fig02.png`.

Move to a new frame, transform the object again, and a second keyframe drops in automatically. Enable **Global Key** in the options bar if you want every transformation type keyed at once whenever you touch any single property.

Motion paths give you curved trajectories. Hit the **New Motion Path** button in the schematic's bottom bar, draw the path in the viewer with any drawing tool, then connect the path's top port to your object's bottom port. The object snaps to the path and keyframes become percentages (0% = start, 100% = end). A toggle on the object node's bottom port switches between preserving orientation and auto-rotating along the curve.

See `fig03.png`.

Hooks let you pin movement to specific drawing features — say, a character's foot during a walk cycle. Select the **Hook** tool, click on the drawing to place a hook, then reference its number in the Stage Schematic ports to link other objects to that tracked point. Split a hook with **Alt-drag** to pass the reference from one feature to another (foot to foot) and prevent moonwalking.

For depth, click the **3D View** button in the viewer title bar. Every object gains a Z-axis position — increase it to push something farther from camera, decrease to pull closer. Objects nearer the camera render on top regardless of column order. Use the **SO** (stacking order) field in the Animate tool options to override compositing order without rearranging columns, and animate it over time if an element needs to pass in front of and behind another.

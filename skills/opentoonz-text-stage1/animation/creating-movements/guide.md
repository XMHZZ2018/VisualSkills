# Creating Movements (OpenToonz 1.7)

Every scene object — columns/layers, pegbars, cameras, the table — can be transformed and animated. Set a transformation at a given frame and OpenToonz creates a keyframe; add another keyframe later and in-betweens are interpolated automatically.

Open the Stage Schematic via **Window > Schematic**, then toggle the **FX/Stage** button in the bottom bar until the title reads "Stage Schematic." This node graph shows every object and its parent-child links. Drag from a node's left port to another node's right port to link them — child objects inherit their parent's movement and add their own on top.

To animate, grab the **Animate** tool and select an object (click it in the Viewer with **Pick: Column** or **Pick: Pegbar**, or select its node in the schematic). Set the **Mode** to **All** to get the full on-canvas handle: drag anywhere to reposition, drag the circle tip to rotate, the double-square tip to scale, or the parallelogram tip to shear. Each interaction auto-creates a keyframe for that transformation only — enable **Global Key** in the tool options if you want every property keyed at once.

For path-based motion, click **New Motion Path** in the schematic's bottom bar, draw the path in the Viewer with any drawing tool, then drag the path node's top port onto the object's bottom port. The object snaps to the path start and its position is now expressed as a percentage (0–100%) along the curve. Toggle the square/rotated-square icon on the object's bottom port to choose between preserving orientation or auto-rotating along the path.

Hooks let you pin objects to specific features of an animation level. Select the **Hook** tool, click on a drawing to place a numbered reference point, then in the schematic scroll the column's port numbers (hover the port, drag the double-arrow) to link another object to that hook. For walk cycles, place a hook on the grounded foot and **Alt-drag** to split it when weight transfers — this prevents the classic moon-walk.

To work in 3D, click the **3D View** button in the Viewer title bar. Adjust any object's **Z** value in the Animate tool options to push it farther from or closer to the camera — closer objects composite on top regardless of column order. Use the **SO** field to override stacking order without rearranging columns when you need a layer to pop in front or behind mid-scene.

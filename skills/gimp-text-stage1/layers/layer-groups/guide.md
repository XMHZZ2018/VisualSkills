# Layer Groups (GIMP 2.10)

Layer groups let you bundle related layers into collapsible folders — essential once a composition grows beyond a handful of layers.

**Creating a group:** Click the **New Layer Group** button at the bottom of the Layers dialog, or go to **Layer → New Layer Group**. The empty group appears above your current layer. Double-click its name (or press **F2**) to rename it something meaningful right away — generic names like "Layer Group #1" get confusing fast.

**Adding layers:** Drag existing layers into the group. Watch for the cursor to shrink and a thin horizontal line to appear showing where the layer will land. To create a fresh layer directly inside a group, select the group first, then hit **Shift+Ctrl+N**. Grouped layers appear indented in the stack, and a small arrow icon lets you collapse or expand the group.

**Nesting:** You can embed groups inside other groups — just activate a group and use **Layer → New Layer Group** again. There's no practical nesting limit beyond your RAM.

**Visibility and opacity:** Toggling the eye icon on a group hides everything inside it. Adjusting opacity on a group applies uniformly to all its children.

**Layer modes matter here.** A mode set on a layer *inside* a group only affects layers within that group. A mode on a layer *above* the group affects everything underneath it, group contents included. The special **Pass Through** mode (new in 2.10) makes grouped layers blend as though they weren't grouped at all — handy when you want organizational structure without composite isolation.

**Masks:** You can apply a layer mask directly to a group. It automatically sizes itself to the group's combined bounds and crops if children are removed.

**Finding layers quickly:** Use **Alt+Middle-click** on the canvas to cycle through layers at that point — the active layer updates and its name flashes in the status bar.

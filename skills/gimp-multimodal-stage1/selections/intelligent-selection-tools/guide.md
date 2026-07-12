# Intelligent Selection Tools (GIMP 2.10)

GIMP's intelligent selection tools go beyond simple rectangles and lassos — they use color and edge information to figure out what you actually want selected. Here's how each one works and when to reach for it.

**Fuzzy Select (Magic Wand)** is the tool most beginners grab first. Activate it with **Tools > Selection Tools > Fuzzy Select** or just press **U**. Click anywhere on your image and it floods outward, grabbing contiguous pixels whose color is similar to where you clicked. Drag downward or to the right to increase the threshold (selecting more), or drag up/left to tighten it. It's great for solid-colored backgrounds but frustrating on complex edges. The **Threshold** slider in Tool Options sets the starting sensitivity, and enabling **Draw Mask** fills the growing selection with magenta so you can actually see what you're getting before you release the mouse.

See `fig01.png`.

**Select by Color** works almost identically — same threshold dragging, same options — but it selects *all* matching pixels across the entire image, not just the ones touching your click point. Activate it via **Tools > Selection Tools > By Color Select** or **Shift+O**. This is the one you want when the same unwanted color appears in multiple disconnected regions and you'd rather nuke it all at once.

**Intelligent Scissors** takes a different approach entirely. Press **I** to activate it, then click along the edge of your subject to drop control nodes. The tool snaps the path between nodes to the nearest high-contrast edge it can find. Once you close the loop (click back on the first node — the cursor turns yellow), click *inside* the closed curve to convert it into a selection. Hold **Shift** while placing nodes to disable edge-snapping and position them manually. Hit **Backspace** to undo the last segment or **Escape** to abandon everything. Fair warning: don't click inside the curve or switch tools until you're done adjusting — there's no going back without starting over.

See `fig02.png`.

**Foreground Select** is the heavy hitter for separating a subject from its background. Activate it from **Tools > Selection Tools > Foreground Select** (no default shortcut). First, roughly lasso around your subject — include a margin of background. Press **Enter** to generate the initial mask; the background turns dark blue. Now paint a stroke across the foreground object to tell GIMP which colors belong to it. Toggle **Preview** (or press **Enter** again) to check the result. If background bleeds through, switch Draw Mode to **Draw background** and paint over the offending areas. For unselected foreground outside your initial lasso, use **Draw unknown**. When it looks right, click **Select** to finalize.

See `fig03.png`.

The **Engine** option matters here: **Matting Levin** is more accurate but memory-hungry on large images; **Matting Global** is faster but rougher. Increase **Levels** if processing is too slow, at the cost of precision.

All four tools share the standard selection mode buttons (replace, add, subtract, intersect), **Antialiasing**, and **Feather edges** — those behave identically across the set. The **Sample Merged** checkbox, available on Fuzzy Select and Select by Color, tells the tool to look at the composite of all visible layers rather than just the active one. Enable it when your subject spans multiple layers.

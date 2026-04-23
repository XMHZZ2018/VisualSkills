# Aligning & Distributing Objects (LibreOffice Impress 7.3.7)

Alignment tools let you line up two or more selected objects relative to each other. They only become active once you've selected multiple objects — so grab at least two before you start.

The alignment options break into two groups: **Left**, **Centered**, and **Right** control horizontal alignment, while **Top**, **Center**, and **Bottom** handle the vertical axis. Each one snaps the selected objects to match the corresponding edge or midpoint.

To access these, click the triangle next to **Align Objects** on the Line and Filling toolbar and pick an option. Alternatively, go to **View > Toolbars > Align Objects** to open a dedicated toolbar. You can also right-click your selection and choose **Align Objects** from the context menu.

The **Properties** sidebar offers quick alignment too. Select your objects, open the **Properties** deck, and expand the **Position and Size** panel — the **Align** row at the bottom has icon buttons for all six alignment options.

For even spacing, select three or more objects, right-click, and choose **Distribution**. This opens a dialog where you can distribute objects evenly along the horizontal axis (by left edge, center, spacing, or right edge) and the vertical axis (by top edge, center, spacing, or bottom edge). Pick the axes you need and hit **OK**.

When you need pixel-perfect placement, the snap grid helps. Turn it on via **View > Snap Guides > Snap to Grid**, or click **Snap to Grid** on the Options toolbar. Configure grid spacing and behavior under **Tools > Options > LibreOffice Impress > Grid**. You can also enable **Snap to Snap Guides** and **Snap to Object Border/Points** from the same menus for more snapping control.

For precise coordinates, press **F4** (or go to **Format > Object and Shape > Position and Size**) to open the **Position and Size** dialog, where you can type exact X/Y positions and dimensions. Check **Keep ratio** if you want proportional resizing.

## Multi-selecting objects reliably

The alignment menu is greyed out until **two or more objects are selected at once**. Three ways to build that multi-selection, ordered by reliability:

1. **Tab-cycle + Shift+Tab** — click one object, then press **Tab** to cycle through the other objects on the slide, holding **Shift** to add each to the current selection. This is the most reliable method when click+drag selection is flaky.
2. **Marquee drag in empty space** — click and drag from an empty area of the slide around the objects you want. **Important:** start the drag in a truly empty region; starting on an object will *move* that object instead of starting a selection rectangle (see `marquee_vs_move.jpg` for the cursor difference: crosshair means marquee, hand means move).
3. **Ctrl+A then deselect** — press **Ctrl+A** to select everything, then **Shift+click** any object you want to drop from the selection.

## Use the Format > Align menu, not manual positioning

When a task says "center-align the images horizontally" or "distribute them evenly", **do not type X/Y coordinates per image** — that almost always drifts off-center and is slow. Instead, multi-select and use **Format > Align Objects > Centered** (horizontal midpoint) / **Center** (vertical midpoint), then **Format > Distribute Selection > Horizontally Centered**. See `align_menu_target.jpg` for the menu path and expected result: all images share the same vertical axis (or horizontal axis) with equal gaps between them.

# Layer Groups (GIMP 2.10)

Layer groups let you bundle related layers into a collapsible folder, keeping complex compositions manageable. Think of them as directories in a file system — you can nest them, move them around, and apply effects to the whole bundle at once.

To create one, click the **New Layer Group** button at the bottom of the Layers dialog, or go to **Layer > New Layer Group**. The empty group appears above the current layer. Double-click its name (or press **F2**) to rename it immediately — you'll thank yourself later when you have a dozen groups.

Drag existing layers into the group to organize them. Watch for the cursor to shrink and a thin insertion line to appear before you release. To add a fresh layer directly inside the group, select the group first, then hit **Shift+Ctrl+N**. Child layers indent to the right so you can see the hierarchy at a glance. Click the small arrow icon next to a group to fold or unfold it.

Hiding a group (click its eye icon) hides everything inside it. If the group is expanded, you'll see struck-out eyes on the child layers — they're technically visible within the group but hidden from the canvas.

Layer modes on a group affect only its children. A mode applied to a layer *above* a group, however, bleeds through to everything underneath. GIMP 2.10 introduces **Pass Through** mode specifically for groups — it makes the children blend as though the group boundary doesn't exist, interacting with layers below the group directly. Switch back to **Normal** to treat the group contents as a single flattened unit before blending downward.

Adjusting a group's opacity scales all its children together. You can also apply a layer mask to the group itself (new in 2.10) — the mask crops automatically to the group's combined bounds.

Groups can be nested without practical limit, duplicated with the **Duplicate Layer** button, or dragged between open images. To quickly locate a layer on a busy canvas, **Alt+Middle-click** the element — GIMP cycles through candidates and shows the layer name in the status bar (available since 2.10.10).

If large projects feel sluggish, disable group preview rendering under **Edit > Preferences > Interface**.

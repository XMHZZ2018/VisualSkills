# Applying Special Effects (OpenToonz 1.7)

All effects live in the **FX Schematic** — open it by clicking the schematic toggle in the bottom bar of the Schematic window until the title bar reads **FX Schematic**. Every column/layer appears as a node flowing rightward into the **Xsheet** node, then to the **Output** node. Effects slot in between.

To add an effect, select a column node and choose **Xsheet > New FX…** (or click the **New FX** button in the schematic's bottom bar) to open the FX Browser. Pick an effect and hit **Insert** to splice it into the existing link, or **Add** to branch a new link from the node. You can also right-click any node and use **Insert FX** / **Add FX** / **Replace FX** from the context menu.

Wire nodes by dragging an output port to an input port. To quickly re-route, **Alt-click and drag** an effect node onto a link to insert it, or away from a link to extract it. Delete a link by selecting it and pressing Delete.

To tweak parameters, double-click the effect node (or right-click > **Edit FX…**) to open the **FX Settings** window. Adjust sliders, color pickers, or spectrums as needed. A swatch preview at the bottom lets you check results — toggle it with the **Preview** or **Camera Preview** buttons. Some effects also expose gadgets directly in the Viewer; just select the node and drag the on-canvas handles.

Animate any parameter by clicking its small **Set Key** button (turns orange when a keyframe is set). Use the **Next Key** / **Previous Key** arrows to jump between keyframes. If no keys are set, values apply to the entire scene.

Save a tuned effect as a preset: right-click the node > **Save As Preset**, give it a name, and it appears inside the effect's folder in the FX Browser for future reuse. To build a reusable combo, select multiple effect nodes, right-click > **Make Macro FX** — the nodes collapse into a single macro node editable via tabs. Save the macro the same way (**Save As Preset**) and it shows up under the **Macro** folder in the browser.

# Applying Special Effects (OpenToonz 1.7)

All effects work through the **FX Schematic** — a node-based graph where each Xsheet column (or Timeline layer) is a node whose output flows rightward toward the **Xsheet** node and finally an **Output** node. To open it, click the schematic toggle button in the bottom bar of the Schematic window until the title bar reads **FX Schematic**.

To add an effect, open the FX Browser via **Xsheet > New FX…** (or the **FX** button in the schematic's bottom bar). The browser organizes effects into folders — Blur, Distort, Gradients, Light, etc. Select the column node you want to affect, pick an effect, then click **Insert** to splice it into the existing link, or **Add** to branch a new link from that node. You can also right-click any node and use the **Insert FX** / **Add FX** submenus directly.

See `fig01.png`.

Three node flavours exist. **Basic effects** (like Blur) have one Source input and modify a single column. **Combined effects** (like Matte In) have multiple inputs — connect your main art to *Source* and your mask or reference to the other port. **Generated effects** (like Radial Gradient) produce imagery from scratch and appear as orange nodes with only an output port.

See `fig02.png`.

To edit an effect's parameters, double-click its node (or right-click and choose **Edit FX…**). The **FX Settings** window shows sliders, fields, and a collapsible **Swatch Viewer** preview at the bottom. You can animate any parameter by clicking the small **Set Key** button next to its name — grey means no keyframe, orange means a key exists at the current frame. Use the **Next Key** / **Previous Key** arrows to hop between keyframes. Some effects also offer interactive gadgets directly in the Viewer; just select the effect node and drag the on-canvas handles.

See `fig03.png`.

To save a particular effect configuration for reuse, right-click the effect node and choose **Save As Preset**, then give it a name. That preset will appear inside the effect's folder in the FX Browser and in right-click submenus on any future project sharing the same project root.

For more complex reuse, you can combine several effect nodes into a **Macro FX**. Select the nodes you want to bundle, right-click, and choose **Make Macro FX**. The macro appears as a single node in the schematic, but you can open it (right-click > **Open Macro FX**) to inspect or tweak internals. Save it with **Save As Preset** and it lands in the **Macro** folder at the bottom of the FX Browser. To dissolve a macro back into its individual nodes, right-click it and choose **Explode Macro FX**.

A few practical shortcuts: **Alt-drag** an effect node onto a link to insert it in-place; **Alt-drag** it away to extract it. Links flow left-to-right, and you can route one column's output to multiple destinations — for instance, rendering it normally *and* feeding it as a matte elsewhere. If you need to limit your render to just one branch of the graph, add a new **Output** node (bottom-bar button or right-click > **New Output**) and connect it to the desired point; right-click that output and choose **Activate** to make it the live render target.

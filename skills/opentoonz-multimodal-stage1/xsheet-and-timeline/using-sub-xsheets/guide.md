# Using Sub-Xsheets (OpenToonz 1.7)

A Sub-Xsheet is essentially a scene nested inside a single column (or layer, in the Timeline). Think of it as a folder for your animation — it can hold as many columns as you need, and even other Sub-Xsheets inside it. When closed, it appears as a violet-colored column with a rendered preview in its icon. Each cell number maps directly to a frame inside the Sub-Xsheet.

See `fig01.png`.

The closed Sub-Xsheet's length is set when you first create it and won't change automatically if you edit its contents later. You can animate it, apply FX to it as a whole, and edit its cells (cycling, cutting, pasting) just like any other level. If you need an independent copy whose internal edits won't affect the original, use **Xsheet > Clone Sub-Xsheet** rather than plain copy-paste.

To create one, select the columns you want to group together, then go to **Xsheet > Collapse** (or right-click the column header and choose **Collapse**). You'll be asked whether to bring along any linked pegbars. Once collapsed, open it with **Xsheet > Open Sub-Xsheet** and close it again with **Xsheet > Close Sub-Xsheet** — both are also available as toolbar buttons.

You can load a previously saved TNZ scene as a Sub-Xsheet via **File > Load As Sub-Xsheet…** or by using **Level > Load Level…** and picking a TNZ file. Its assets get imported into your current project's default folders automatically. If the imported scene has different camera settings, you'll be asked which to keep.

To flatten a Sub-Xsheet back into the parent Xsheet, select it and choose **Xsheet > Explode Sub-Xsheet**. The internal columns reappear in the main Xsheet, grouped in the FX Schematic for easy identification. Note that any FX applied to the Sub-Xsheet column itself won't transfer to the exploded columns.

By default, opening a Sub-Xsheet shows only its own contents in the viewer. Toggle **Xsheet > Toggle Edit in Place** if you need to see the surrounding scene while editing inside. To reset a Sub-Xsheet's cell timing back to its original sequential order, use **Xsheet > Resequence**. And to save a Sub-Xsheet out as a standalone scene for reuse elsewhere, open it and choose **Xsheet > Save Sub-Xsheet As…**.

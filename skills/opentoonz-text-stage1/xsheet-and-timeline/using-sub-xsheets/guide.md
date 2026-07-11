# Using Sub-Xsheets (OpenToonz 1.7)

A Sub-Xsheet is an entire scene nested inside a single Xsheet column (or Timeline layer). When closed, it shows up as a violet column whose cells reference its internal frames. You can animate it, apply FX to it, and edit its cell exposure just like any other level.

To create one, select the columns you want to bundle together, then go to **Xsheet > Collapse** (or right-click a column header and choose **Collapse**). You'll be asked whether to include linked pegbars — say yes if the columns have animation parented to them. The selected columns fold down into a single Sub-Xsheet column.

To open a Sub-Xsheet and edit its contents, select its column and choose **Xsheet > Open Sub-Xsheet**. When you're done, come back out with **Xsheet > Close Sub-Xsheet**. If you need to see surrounding scene context while editing inside, toggle **Xsheet > Toggle Edit in Place**.

You can load a previously saved OpenToonz scene (TNZ file) directly as a Sub-Xsheet via **File > Load As Sub-Xsheet…** or by dragging a TNZ file from the browser into the Xsheet. Each import is independent — editing won't touch the original file.

To break a Sub-Xsheet back into its component columns, select it and choose **Xsheet > Explode Sub-Xsheet**. If you need a truly independent copy whose internal edits won't affect the original, use **Xsheet > Clone Sub-Xsheet** instead of copy-paste. To reset a Sub-Xsheet's exposure back to its original frame order and length, use **Xsheet > Resequence**.

To save a Sub-Xsheet out as a standalone scene for reuse in other projects, open it first, then choose **Xsheet > Save Sub-Xsheet As…**. This makes it available as a TNZ file you can load anywhere.

One caveat: audio files loaded *inside* a Sub-Xsheet are ignored during final rendering, since the ability to reorder Sub-Xsheet cells could produce an inconsistent soundtrack. Keep audio clips in the main Xsheet instead.

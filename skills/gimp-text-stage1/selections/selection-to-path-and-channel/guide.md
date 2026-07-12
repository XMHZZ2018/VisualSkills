# Converting Selections to Paths and Channels (GIMP 2.10)

Selections in GIMP are temporary by nature — once you click elsewhere or start a new selection, they're gone. Converting them to channels or paths lets you store and refine them for later use.

**Saving a selection to a channel** is the quickest way to preserve it. Go to **Select > Save to Channel** and GIMP stores the selection as a channel mask, visible in the Channels dialog. You can reload it anytime by right-clicking the channel and choosing "Channel to Selection." This is ideal when you want to reuse an exact selection shape without recreating it.

**Converting a selection to a path** gives you editable vector control. Use **Select > To Path** and the selection's outline becomes a path listed in the Paths dialog. The canvas won't look different, but now you can grab the Path tool and tweak anchor points for pixel-precise adjustments — great for cleaning up rough edges from fuzzy selections. The Paths dialog also offers advanced options for fine-tuning how the conversion handles curves.

**Going the other direction — path to selection —** is just as simple. Hit **Select > From Path** (or the keyboard shortcut **Shift+V**) and the current path becomes an active selection. If the path isn't closed, GIMP connects the endpoints with a straight line automatically. You can also click the **Path to Selection** button directly in the Paths dialog.

A common workflow: make a rough selection with any tool, save it to a channel as a backup, convert it to a path for fine editing, then convert the polished path back to a selection when you're ready to paint or mask.

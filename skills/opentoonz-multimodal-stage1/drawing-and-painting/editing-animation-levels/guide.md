Here's the guide:

# Editing Animation Levels (OpenToonz 1.7)

The Level Strip is your main workspace for managing individual animation levels. It displays every drawing in the current level in numbering order — even frames not exposed in the Xsheet/Timeline. Select a cell in the Xsheet containing a drawing from the level you want to edit, or right-click the level icon in the Scene Cast and choose **Display in Level Strip**. Click any frame in the strip to load that drawing into the Viewer for direct editing.

You can select frames the usual ways — click, shift-click for ranges, Ctrl/Cmd-click for non-contiguous picks — then use **Edit > Copy**, **Cut**, **Paste**, **Paste Into**, **Delete**, or **Insert** to rearrange things. Paste shifts subsequent frames down and renumbers automatically; Paste Into overwrites the selected frames without shifting anything. If you delete or cut a frame that's still referenced in the Xsheet, that cell's level name turns red as a warning.

For sequence manipulation, the **Cells** menu offers handy shortcuts: **Reverse** flips the selection order, **Swing** appends a reversed copy (minus the duplicate last frame), and **Step 2/3/4** or **Each 2/3/4** let you stretch or thin out frame timing. **Duplicate Drawing** copies the first selected drawing into the next frame, shifting everything else down.

To make room for new drawings without manually shifting, open **Level > Renumber…** and set a new **Start Frame** and **Step** for the selected frames. Alternatively, **Level > Add Frames…** inserts a range of blank frames at the numbering you specify. Both commands fail gracefully if the target frame numbers already exist.

If you mess something up, select the affected frames and hit **Level > Reload** to restore the last saved version. For Toonz Raster levels that went through cleanup, **Level > Revert to Cleaned Up** brings back the original cleaned-up artwork (requires the backup preference to have been active during cleanup).

Merging multiple levels into one is straightforward. Select the columns/layers you want to combine and choose **Xsheet > Merge Levels** for Vector or standard Raster levels, or **Xsheet > Merge TLV Levels** for Toonz Raster levels. The result follows the frame numbering of the leftmost column (or bottommost layer in Timeline), and geometrical transformations from column/pegbar edits are preserved.

Under **Level > Adjust**, you'll find image processing tools — **Brightness and Contrast**, **Color Fade**, **Antialias**, **Adjust Levels**, and **Binarize** all work on Raster frames. For Toonz Vector levels specifically, **Adjust Thickness** lets you scale, add, or set constant line thickness across selected frames. Each dialog has a resizable preview area so you can check results before hitting **Apply**.
Edits aren't persisted until you explicitly save. Use **Level > Save Level** for the current level, or **Level > Save Level As…** to write a copy to a new location (the scene keeps referencing the original). The scene-wide **Save All** command saves every modified level at once. Enable **Backup Scene and Animation Levels when Saving** in Preferences to get automatic `_backup` suffixed copies.

To export a level for use outside OpenToonz, go to **Level > Export Level…**, pick a destination and format (BMP, JPG, PNG, TGA, TIF, or TLV for vector-to-raster). For Vector levels you can set the output size, resolution, line thickness range, and toggle **No Antialias**. The **Retas Compliant** option auto-names files with a four-digit suffix and forces TGA format. Hit **Export** and you're done — the scene's internal level reference stays unchanged.

No images referenced in this file. I have everything I need from the text content to write the guide.

# Editing Animation Levels (OpenToonz 1.7)

The Level Strip is your main workspace for rearranging an animation level. Open it by selecting any cell belonging to the level in the Xsheet/Timeline, or right-click the level in the Scene Cast and choose **Display in Level Strip**. It shows every drawing in the level by numbering order — even frames not currently exposed.

Select frames by clicking, shift-clicking for ranges, or Ctrl/Cmd-clicking to cherry-pick. From there, standard **Cut**, **Copy**, **Paste**, and **Delete** operations work as expected. **Paste Into** overwrites the target selection rather than inserting. **Insert** adds blank frames before your selection and renumbers everything after.

To reorder or repeat frames, look under the **Cells** menu: **Reverse** flips the selection, **Swing** appends a mirror of it, and **Step 2/3/4** repeats drawings for held-frame animation. **Each 2/3/4** thins the selection down. **Duplicate Drawing** copies the first selected drawing into the next frame slot.

When you need room for new drawings, use **Level > Renumber...** to set a custom start frame and step, or **Level > Add Frames...** to inject a numbered range directly. Both fail if the target numbers already exist.

To merge multiple levels into one, select the columns/layers and run **Xsheet > Merge Levels** (for vector or standard raster) or **Xsheet > Merge TLV Levels** (for Toonz Raster). The leftmost column drives the frame count and resolution. Each column must contain only one level.

For image processing, select frames then visit **Level > Adjust**. Options include **Brightness and Contrast...**, **Color Fade...**, **Antialias...**, **Adjust Levels...**, and **Binarize...**. For vector levels only, **Adjust Thickness...** lets you scale, add, or set constant stroke width across a range. All dialogs have a resizable preview area.

If you make a mistake, select the affected frames and hit **Level > Reload** to revert to the last saved version. For cleaned-up Toonz Raster levels, **Level > Revert to Cleaned Up** restores the original cleanup output (requires the backup preference enabled).

Save your work with **Level > Save Level** or **Level > Save Level As...** for a renamed copy. The scene-wide **Save All** also persists all modified levels at once. Enable **Backup Scene and Animation Levels when Saving** in Preferences to keep `_backup` copies automatically.

To export for other software, use **Level > Export Level...**. Pick from BMP, JPG, PNG, TGA, TIF, or TLV (vector-to-TLV only). For vector exports you can set output size, line thickness range, and toggle **No Antialias**. The **Retas Compliant** option auto-names files with four-digit suffixes in TGA format. Exported files are independent copies — the scene still references the original level.

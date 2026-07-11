# Creating Soundtracks and Lip Syncing (OpenToonz 1.7)

OpenToonz supports WAV and AIFF audio natively (8- or 16-bit uncompressed). If you've configured FFmpeg in **File > Preferences… > Import/Export**, you can also load MP3 files. There's no limit on how many audio clips a scene can contain.

To bring audio in, use the file browser or right-click a cell and choose **Load Level…**. Each clip lands in its own column (Xsheet) or layer (Timeline), displayed as a pale-green waveform. The number of frames the clip occupies depends on your scene's frame rate — a 3-second clip at 24 fps takes 72 frames. Imported audio files are stored in the project's *+extras* folder and appear in the Scene Cast's **Audio** folder.

See `fig01.png`.

The audio column header gives you a **Render toggle** (include in final output), a **Camera Stand toggle** (include when scrubbing), a **Lock toggle**, a volume control under the **Additional settings** button, and a loudspeaker icon for instant playback. You can adjust per-column volume and the final soundtrack merges all audio columns together. Rendered output in MP4, MOV, WebM, or AVI will embed the merged soundtrack automatically. Note that audio inside Sub-Xsheets is ignored during rendering.

To trim a clip, drag its start or end edge directly in the column — a colored marker shows where you trimmed, and you can drag it back to restore hidden audio. Move clips to different frames by dragging the strip on the left (Xsheet) or top (Timeline) of the cells. Standard cut/copy/paste/delete all work on audio cells the same way they work on drawing cells.

Scrubbing is your main tool for synchronizing animation to sound. Drag the frame cursor in the Xsheet frame column, the Timeline ruler, or the viewer framebar to hear all audio columns whose Camera Stand toggle is active. On Windows you can also click-drag the dashed strip beside the audio cells for immediate section playback.

For manual lip syncing, create a single animation level with your mouth shapes (open, closed, smile, etc.), expose it in a column, then scrub the audio to identify where each phoneme falls. Select the mouth column and use the **Skeleton** tool set to **Animate** mode — click the level-name label near the pivot point and drag up/down (or click the arrowheads) to flip through drawings and pick the right mouth for each frame.

For automated lip sync, install Rhubarb separately and point to it in Preferences. Expose at least one drawing from your mouth-shapes level, right-click the target cell, and choose **Lip Sync > Apply Auto Lip Sync to Column**. In the dialog, pick your **Audio Source** (an Xsheet column or a file on disk), optionally type a transcript in the **Audio Script** field to improve accuracy, then assign a drawing to each Preston Blair phoneme using the arrow buttons. Hit **Apply** and Rhubarb fills the column automatically.

See `fig02.png` for the Auto Lip Sync dialog.

You can also import lip-sync data from Papagayo-NG. Export a MOHO-format DAT file from Papagayo, then in OpenToonz select your target cell and choose **Apply Lip Sync Data to Column** (right-click menu or **Xsheet** menu). Browse to the DAT file, assign drawings to phonemes, set **Insert at Frame**, and optionally enable **Extend Rest Drawing to End Marker** to fill remaining frames with the closed-mouth pose.

Now I have all the information needed to write the guide.

# Creating Soundtracks and Lip Syncing (OpenToonz 1.7)

OpenToonz supports WAV, AIFF (8/16-bit), and MP3 audio (MP3 requires FFmpeg configured in **File > Preferences... > Import/Export**). Load a clip via **Level > Load Level...** or drag it from the file browser into the Xsheet/Timeline. Each clip lands in its own column/layer as a visible waveform — its frame span depends on clip duration and your scene's frame rate.

Audio columns have a loudspeaker icon in the header for instant playback. Adjust per-column volume by clicking the **Additional settings** triangle and moving the **Volume** slider. Use the **Camera stand toggle** to include or exclude a column when scrubbing, and the **Render toggle** to control whether it ends up in the final output.

To scrub audio, drag the frame cursor in the Xsheet frame column, the Timeline ruler, or the Viewer framebar. On Windows you can also click-drag the dashed strip beside the audio cells to hear a selection played back in real time.

Trim clips by dragging their start or end edges directly in the column. Move, cut, copy, or delete sections with standard edit commands — the file on disk is never modified.

For lip sync, create an animation level with your mouth shape drawings (typically based on Preston Blair phonemes: A I, E, O, U, F V, L, M B P, W Q, C D G K N R S Th Y Z, and Rest). Expose at least one drawing from that level in the Xsheet/Timeline.

**Auto Lip Sync (Rhubarb):** Right-click the target cell and choose **Lip Sync > Apply Auto Lip Sync to Column**. Pick your audio source from the **Audio Source** dropdown, optionally type a transcript in **Audio Script** for better accuracy, assign drawings to each phoneme with the arrow buttons, then hit **Apply**.

**Papagayo-NG import:** Export a MOHO-format DAT file from Papagayo-NG. In OpenToonz, right-click a cell and choose **Apply Lip Sync Data to Column**, browse to the DAT file, map drawings to phonemes, set **Insert at Frame**, and click **Apply**.

**Magpie import:** Choose **File > Import Toonz Lip Sync File...**, load the TLS file, set frame range and phoneme-to-drawing assignments, then click **Import**.

When rendering to MP4, MOV, WebM, or AVI the merged soundtrack is embedded automatically. Audio inside Sub-Xsheets is ignored in the final render.

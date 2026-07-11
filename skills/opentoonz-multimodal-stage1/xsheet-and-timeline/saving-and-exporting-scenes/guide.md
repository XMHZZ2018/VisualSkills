# Saving and Exporting Scenes (OpenToonz 1.7)

Every scene lives as a TNZ file inside your project's *+scenes* folder. Until you save it, OpenToonz assigns a default name like "untitled1" and stashes everything in a temporary `projects\temp` directory — clear that out periodically to reclaim disk space.

To save your work, hit **File > Save Scene** for the scene file alone, or **File > Save All** to save the scene plus every modified level at once. If you want a copy under a new name, use **File > Save Scene As…**, pick a location within *+scenes* (or a subfolder), name it, and click **Save**. When a scene has unsaved changes, an asterisk appears next to its name in the title bar.

You can enable autosave under **File > Preferences… > Saving** — toggle **Save Automatically**, set the interval in minutes, and choose whether it covers the scene file, non-scene files, or both.

Loading is straightforward: **File > Load Scene…** opens a browser pointed at your project's scenes. You can also drag a TNZ file from the standard browser onto the clapboard icon in the Scene Cast, or use **File > Open Recent Scene File** for quick access. If you need to discard edits and start fresh, **File > Revert Scene** reloads the last saved version.

OpenToonz keeps the four most recent backup copies of each scene in `+scenes\backups\<scene_name>`. The highest-numbered backup is the newest. To recover one, rename it (strip the backup number) and drop it back into *+scenes*.

When you need to move a scene to a different project, you have two paths. To bring an outside scene *in*, load it and choose **Import Scene** when prompted — all assets from the original project's default folders get copied into yours. Alternatively, right-click one or more scenes in the browser and pick **Import Scene** without loading them. To push scenes *out*, right-click and choose **Export Scene…**, then either select an existing project or create a new one based on your current settings.

See `fig01.png`.

If a scene references files loaded from external folders (outside your project defaults), those won't travel with the project automatically. Run **Collect Assets** (right-click the scene in the browser) to pull every external file into the proper default folders and update all internal paths in one shot.

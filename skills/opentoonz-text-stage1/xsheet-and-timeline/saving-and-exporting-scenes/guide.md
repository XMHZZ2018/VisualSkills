# Saving and Exporting Scenes (OpenToonz 1.7)

Every new scene starts life as "untitled" with a number appended. Untitled scenes live in `OpenToonz stuff/projects/temp` — they're deleted if you never properly save, so don't leave work there.

To save everything at once — scene file plus all modified levels — use **File > Save All**. If you only want to save the scene structure without touching levels, **File > Save Scene** does the job. To save a copy under a new name, go **File > Save Scene As…** and pick a location inside your project's *+scenes* folder (or a subfolder of it).

Loading is straightforward: **File > Load Scene…** opens a browser pointed at your project's scenes. You can also right-click a TNZ file in the built-in browser and choose **Load Scene…**, or drag it onto the clapboard icon in the Scene Cast. Recent files are available under **File > Open Recent Scene File**. If something goes wrong, **File > Revert Scene** snaps you back to the last saved version.

For auto-saving, head to **File > Preferences… > Saving**, enable **Save Automatically**, and set your interval in minutes. You can choose whether it covers the scene file, non-scene files, or both.

OpenToonz keeps four backup versions of every saved scene in `+scenes/backups/<scene_name>`. To recover one, rename the backup file (strip the trailing number) and drop it back into the *+scenes* folder.

When you need to move a scene to a different project, select it in the browser, right-click, and choose **Export Scene…**. You can target an existing project or create a new one on the spot — all assets are collected and copied automatically. Going the other direction, loading a scene from another project prompts you to **Import Scene** (copies assets into your current project) or **Change Project**. You can also batch-import scenes without loading them by selecting them in the browser and choosing **Import Scene** from the right-click menu.

If your scene references files from outside the project folders, use **Collect Assets** (right-click selected scenes in the browser) to pull everything into the proper default folders and fix the paths automatically.

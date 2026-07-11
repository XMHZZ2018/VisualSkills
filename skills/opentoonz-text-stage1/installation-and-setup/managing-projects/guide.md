# Managing Projects (OpenToonz 1.7)

Projects give every scene in a production consistent settings and a shared folder structure. When you create a scene inside a project, it automatically inherits the project's defaults — and files like scanned drawings land in the right place without manual filing.

**The projectroot** is where OpenToonz stores all project databases. On Windows, edit the registry key at `HKEY_LOCAL_MACHINE\SOFTWARE\OpenToonz\OpenToonz` → double-click TOONZPROJECTS and set your path. On Mac, right-click the OpenToonz app → **Show Package Contents**, then edit `Contents/Resources/SystemVar.ini`. Separate multiple roots with a semicolon. Restart OpenToonz after any change.

To create a project, go to **File → Project Management → New Project…**, pick a projectroot, name your project, and configure the default folder paths. Each alias — **+inputs**, **+drawings**, **+scenes**, **+extras**, **+outputs**, **+palettes** — points to where that category of file lives. Paths can be absolute (e.g., `C:\production\drawings01`) or relative to the project folder.

To switch projects, click the small round indicator beside the project name in the file browser — it turns red when active. Any new scene you create via **File → New Scene** belongs to whichever project is current. Adjust existing folder paths anytime through **File → Project Management → Project Settings…**, but be aware older scenes may lose track of their files.

The `$scenepath` variable is powerful for per-scene organization. Place it in a folder definition (like `$scenepath\mydrawings`) and OpenToonz auto-creates scene-specific subfolders when you save. Alternatively, tick **Append $scenepath** in the New Project dialog to append the scene's save-path to the alias automatically — you can't use both methods on the same alias.

For custom aliases beyond the built-in six, edit `OpenToonz stuff/profiles/project_folders.txt` — list one folder name per line. In the project browser, folders targeted by aliases appear in blue, giving you quick access to production material regardless of where it physically lives on disk.

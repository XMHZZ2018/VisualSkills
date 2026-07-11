# Managing Projects (OpenToonz 1.7)

Projects give every scene in your production a shared set of default folders and settings. Once a project is configured, new scenes automatically inherit its folder paths and scene properties — no manual setup each time.

## The Projectroot

The projectroot is the top-level folder where OpenToonz stores all project databases. By default it lives at `C:\OpenToonz stuff\projects` (Windows) or `/Applications/OpenToonz/OpenToonz stuff/projects` (Mac). On Windows, you change it by editing the `TOONZPROJECTS` value in the Registry at `HKEY_LOCAL_MACHINE\SOFTWARE\OpenToonz\OpenToonz`. On Mac, right-click the OpenToonz app, choose **Show Package Contents**, then edit `Contents/Resources/SystemVar.ini`. You can define multiple projectroots by separating paths with a semicolon — handy when teams share a network drive.

See `fig01.png`.

## Creating and Switching Projects

To create a project, go to **File > Project Management > New Project…**. Pick a projectroot, give the project a name, and set paths for each default folder. Hit **OK** and you're done. Each folder slot (+inputs, +drawings, +scenes, +extras, +outputs, +palettes) can use a relative path (created inside the project folder) or an absolute path pointing anywhere on the network.

See `fig02.png`.

To switch projects, find the project tree in the file browser and click the small round indicator next to the project name — it turns red when active. Any scene you create with **File > New Scene** now belongs to that project.

## Default Folders and Aliases

The six standard aliases map to production stages: **+inputs** (scanned TIFs), **+drawings** (TLV/PLI levels), **+scenes** (TNZ files), **+extras** (imported media), **+outputs** (renders), and **+palettes** (project palettes). These aliases work as shorthand throughout OpenToonz — loading paths, save dialogs, and the project browser all resolve them automatically.

You can add custom aliases by editing `OpenToonz stuff/profiles/project_folders.txt` — just list one folder name per line. After a restart, your new aliases (like +backgrounds or +3D) appear in project settings.

## Organizing with $scenepath

If you want per-scene subfolders created automatically, enable **Append $scenepath** in the New Project dialog for +drawings, +inputs, or +extras. When you save a scene, OpenToonz appends the scene's save path to that alias, so each scene gets its own isolated folder without manual effort.

Alternatively, embed `$scenepath` directly in the folder definition (e.g., `$scenepath\mydrawings`) for more control over where the scene name lands in the hierarchy. You can't combine both approaches on the same alias.

See `fig03.png` for the resulting folder structures.

## The Project Browser

At the bottom of the file browser tree you'll find all your projects listed under their projectroot. Folders that are alias targets show up in blue, making it easy to spot where files actually land. When paths are absolute, the browser displays just the alias names as shortcuts — no need to dig through the filesystem to find your production material.

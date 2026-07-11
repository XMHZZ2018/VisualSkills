# Using Version Control (OpenToonz 1.7)

OpenToonz integrates with **Subversion** (SVN) to give your team a shared central repository with full revision history. Everyone works on a local copy — you **Get** files down to edit them and **Put** them back when you're done, and SVN tracks every version along the way.

**Setting up the server and client.** You need a Subversion 1.6+ server (local network machine or a hosted service like Assembla) and a matching client on each workstation. On Windows, grab the CollabNet Subversion Command-Line Client from the Subversion packages page. On macOS Snow Leopard or later, SVN ships with the OS — nothing extra to install.

**Configuring OpenToonz.** Open `OpenToonz stuff/config/versioncontrol.xml` in a text editor. Remove the two XML comment sentinel lines, then fill in your repository name, local working copy path, and the repository URL. Next, open `permissions.xml` in the same folder and add a `<user>` block for each team member, mapping their OpenToonz username to SVN credentials. Save both files.

**Activating version control.** Inside OpenToonz, go to **File > Preferences… > Version Control** and enable the **Enable Version Control** option, then restart. Your repository appears at the bottom of the File Browser tree — right-click it and choose **Get** to pull the initial working copy.

See `fig01.png`.

**Getting and putting files.** Right-click any folder or file in the browser and choose **Get** to pull the latest version, or **Put** to push your changes back. When putting, a dialog lets you select which files to include and add a comment describing what changed. For scene files (.tnz), tick **Get Scene Contents** or **Put Scene Contents** to include all referenced materials.

See `fig02.png`.

**Editing (locking) files.** Before you load a file for modification, right-click it and choose **Edit** — this locks the file so nobody else can change it simultaneously. You can leave a comment explaining what you're working on. For Toonz Vector or Raster levels, use **Edit Frame Range** instead to lock only the frames you need, letting teammates work on other frames of the same level concurrently. When you're finished, right-click and choose **Unlock** to release the lock.

**Retrieving older revisions.** Right-click a file and choose **Get Revision** to open a timeline of every past version, showing dates, authors, and comments. Select any entry and click **Get Selected Revision** to restore it. For a multi-file selection, the dialog lets you specify a relative time offset (hours, days, weeks) or an exact date.

See `fig03.png`.

**Reading the icons.** Folder and file icons in the browser tell you everything at a glance: a grey folder means it's only on the server (needs a **Get**); a green-marked folder is fully up to date; a yellow mark means something's out of sync. For files, a grey checkmark means read-only and current, a green checkmark means you have it in edit mode, a red exclamation means you've modified it locally (ready to **Put**), an orange exclamation means someone else updated the server copy (time to **Get**), and a lock icon means another user has it checked out.

If the browser's automatic refresh feels sluggish over a slow connection, disable it at **File > Preferences… > Version Control** by unchecking **Automatically Refresh Folder Contents**, then right-click folders and choose **Refresh** manually when you need an update.

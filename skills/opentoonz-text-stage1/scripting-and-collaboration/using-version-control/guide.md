# Using Version Control (OpenToonz 1.7)

OpenToonz integrates with **Subversion (SVN)** to let teams share a central repository of project files. You work on a local copy, and the system tracks every revision so nothing is ever lost.

**Installation:** Install the Subversion client (v1.6+). On Windows, grab the CollabNet command-line client from the Subversion packages page. On macOS Snow Leopard or later, it's already built in — older systems need a manual install (note the install path, usually `/opt/subversion/bin`).

**Configuration:** Edit `OpenToonz stuff/config/versioncontrol.xml` — remove the two comment lines that disable SVN, then fill in your repository name, local working copy path, and the repository URL. Next, open `permissions.xml` and add each user with their SVN credentials inside a `<svn name="..." password="..." />` tag. You can define multiple repositories and assign users to each.

**Initialization:** Go to **File > Preferences… > Version Control** and enable **Enable Version Control**, then restart OpenToonz. Your repository appears at the bottom of the File Browser tree. Right-click it and choose **Get** to pull the initial content into your working copy.

**Getting and Putting files:** Right-click any folder or file in the browser and choose **Get** to pull the latest version, or **Put** to push your changes back. When putting, you can select which files to include and add a comment describing your changes. For scene files (.tnz), toggle **Get Scene Contents** or **Put Scene Contents** to include all referenced materials.

**Editing and Locking:** Before modifying a file, right-click it and choose **Edit** — this locks it so no one else can change it simultaneously. Add a comment so teammates know what you're doing. Use **Edit Frame Range** to lock only specific frames of a Toonz level, letting multiple artists work on the same level concurrently. When you're done, right-click and choose **Unlock** to release the lock.

**Retrieving Revisions:** Right-click a file and choose **Get Revision** to browse a timeline of all past versions with dates, authors, and comments. Select any revision and click **Get Selected Revision** to restore it. For multiple files, you can retrieve versions by time offset, days, weeks, or exact date.

**Reading the icons:** Grey folders/files exist only in the repository (use **Get**). A green check means your copy is current. A red exclamation mark means you have local changes to **Put**. An orange exclamation mark means a newer version exists remotely. A lock icon means another user is editing that file. A plus mark means the file is local-only and ready to be added with **Put**.

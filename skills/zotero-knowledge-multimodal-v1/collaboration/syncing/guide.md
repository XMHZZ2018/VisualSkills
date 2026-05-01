# Syncing Your Library (Zotero 7)

Zotero keeps everything on your local machine by default, but syncing lets you access your library from any computer — or recover it if something goes wrong. There are two layers: **data syncing** (your items, notes, tags, and links) and **file syncing** (PDFs, images, and other attachments). You can use data syncing on its own without file syncing.

To get started, create a free account at zotero.org, then open **Edit > Settings** (or **Zotero > Settings** on macOS) and head to the **Sync** pane. Enter your Zotero username and password in the **Data Syncing** section. Once linked, Zotero will automatically sync changes within seconds of you making them. If you'd rather control the timing yourself, uncheck **Sync automatically** and hit the green circular-arrow **Sync with zotero.org** button in the toolbar whenever you're ready.

See `fig01.png`.

Syncing is bidirectional — edits on one machine flow to every other synced machine. If the same item gets changed in conflicting ways on two computers before a sync happens, Zotero will pop up a conflict resolution dialog so you can pick which version to keep.

For attachment files, you have two options. **Zotero Storage** is the simplest: every account gets 300 MB free, with paid upgrades available, and it also handles group library files and gives you web access to your PDFs on zotero.org. Alternatively, if your institution provides **WebDAV** storage, you can point Zotero at it in the same **Sync** pane — enter the URL, credentials, and click **Verify Server** to confirm the connection. Note that WebDAV only works for your personal library, not groups.

One important warning: never put your Zotero data directory inside a cloud-synced folder (Dropbox, Google Drive, iCloud, etc.). This will almost certainly corrupt your database. If you want to avoid Zotero's servers entirely, close Zotero first, then manually copy the entire data directory to another machine — treat it like a backup and restore. Another option is to use Zotero's data sync but store attachments as **linked files** in an externally synced folder, keeping only the attachment files (not the database) in the cloud.

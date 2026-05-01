# Syncing Your Library (Zotero 7)

Zotero stores everything locally by default, but syncing lets you access your library from any computer. There are two parts: **data syncing** (items, notes, tags, links) and **file syncing** (PDFs, images, and other attachments). You can use data syncing on its own — it's free and unlimited.

To get started, create a free account at zotero.org, then open **Edit > Settings > Sync** (or **Zotero > Settings > Sync** on macOS) and enter your login credentials in the **Data Syncing** section. By default, Zotero syncs automatically whenever you make changes. If you'd rather control it yourself, uncheck **Sync automatically** and hit the green circular arrow button in the toolbar to sync manually.

Syncing is bidirectional — changes on one machine flow to all others. If the same item gets edited in conflicting ways on two computers before a sync happens, Zotero will pop up a conflict resolution dialog so you can pick which version to keep.

For attachment files, you have two options. **Zotero Storage** is the easiest — every account gets 300 MB free, with paid upgrades available. It also handles group library files and gives you web access to your PDFs on zotero.org. Alternatively, you can use a **WebDAV** server (personal libraries only). Enter the server URL, username, and password in the **Sync** preferences, then click **Verify Server** to confirm it works.

Once syncing is configured on multiple computers, everything stays in sync transparently. If you ever move to a new machine, just sign in under **Settings > Sync** and Zotero pulls down your entire library automatically.

One important warning: **never** put your Zotero data directory inside a cloud storage folder (Dropbox, Google Drive, etc.) — this will corrupt your database. If you want to avoid Zotero's servers entirely, you can manually copy the data directory between machines (with Zotero closed), or use linked files with an external sync service for attachments only.

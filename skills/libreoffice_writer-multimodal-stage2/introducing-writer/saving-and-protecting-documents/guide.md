# Saving and Protecting Documents (LibreOffice Writer 7.3.7)

You can save a document in Writer using several commands, and the differences matter. **File > Save** keeps the current filename and location. **File > Save As** (or Ctrl+Shift+S) lets you pick a new name, location, or file format. If you need to stash a copy while keeping the original open, use **File > Save a Copy** — the copy is saved but never opened. And **File > Save All** saves every open document in one go. For remote files, **File > Save Remote** stores the document on a remote server directly.

Writer can automatically save recovery copies at regular intervals. Head to **Tools > Options > Load/Save > General**, tick **Save AutoRecovery information every**, and set your preferred interval (the default is 10 minutes). While you're there, consider enabling **Always create backup copy** for an extra safety net.

If you need to share files with Microsoft Office users, go to **File > Save As** and pick a `.docx` format from the **File type** drop-down. Note that any changes you make from that point on will only appear in the Word version — you'd need to reopen the `.odt` original to keep working in ODF. To default to Word format permanently, go to **Tools > Options > Load/Save > General**, find **Default File Format and ODF Settings**, set **Document type** to *Text document*, and choose your preferred Word format under **Always save as**.

Writer offers two kinds of document protection: password-based and OpenPGP encryption. To password-protect a file, use **File > Save As** and tick the **Save with password** checkbox in the lower-left corner, then click **Save**.

See `fig01.png`.

A Set Password dialog appears with two sections. Enter a password in the **File Encryption Password** fields to fully lock the file — nobody opens it without the password. For a lighter touch, click **Options**, select **Open file read-only** under *File Sharing Password*, and optionally set a separate editing password so some people can read while others can also edit.

See `fig02.png`.

Be warned: LibreOffice uses strong encryption, so if you lose the password, the document is effectively gone. To change or remove a password later, open the document and go to **File > Properties > General**, then click **Change Password**.

For OpenPGP encryption, you'll need GPG software and a personal key pair already set up on your system. In the **Save As** dialog, select **Encrypt with GPG key** instead of (or alongside) the password option, click **Save**, and choose the recipient's public key from the list that appears. The recipient must have the corresponding private key to decrypt the file.

Writer can also open and save files on remote servers over FTP, WebDAV, Windows Share, SSH, or cloud services like Google Drive and Microsoft OneDrive. For details on setting up remote connections, see the *Getting Started Guide*.

---

## UI Reference  —  File Open & Save As Dialogs

_Scope: Save As dialog: file format dropdown (18 formats), Save with password, Encrypt with GPG key_

Both dialogs use the GTK file chooser with a sidebar of quick-access locations, breadcrumb navigation, searchable/sortable file list, and format selectors.

Read the screenshot `ui-file-dialogs.png` in this directory.

## Save As Dialog (Shift+Ctrl+S)

Opened via File > Save As... or Shift+Ctrl+S.

**Top bar:**
- **Cancel** button (top-left)
- **Name** text field — pre-filled with document title; pressing Return triggers Save
- **Search** button (magnifying glass) — toggles inline search field replacing the breadcrumb bar
- **Save** button (blue, top-right) — saves with current name/format/location

**Navigation:**
- **Back arrow** (◄) — navigates back in folder history
- **Breadcrumb path segments** — clickable buttons showing current path (e.g. ga > Documents)
- **Create Folder** button (folder+ icon, top-right of file browser) — opens inline popup with folder name field

**Left sidebar:** Home, Documents, Downloads, Music, Pictures, Videos, + Other Locations (shows mounted drives, networks, Connect to Server bar)

**File browser:** Sortable columns — Name, Size, Type, Modified. Right-click context menu: Open With File Manager, Copy Location, Add to Bookmarks, Rename, Move to Trash, Show Hidden Files, column visibility toggles, Sort Folders before Files.

**Bottom controls:**
- **Encrypt with GPG key** checkbox
- **Edit filter settings** checkbox (greyed for most formats; enabled for e.g. Text - Choose Encoding)
- **Save with password** checkbox (ODF formats only)
- **File format dropdown** — 18 formats: ODF Text Document (.odt, default), ODF Template (.ott), Flat XML ODF (.fodt), Unified Office Format (.uot), Word 2010-365 (.docx), Word 2010-365 Template (.dotx), Word 2007 (.docx), Word 2007 Template (.dotx), Word 2003 XML (.xml), Rich Text (.rtf), Word 97-2003 (.doc/.dot), DocBook (.xml), HTML (.html), Text (.txt), Text - Choose Encoding (.txt), Word 2007 VBA (.docm)

## Open Dialog (Ctrl+O)

Opened via File > Open... or Ctrl+O.

**Top bar:** Cancel, "Open" title label, Search button, Open button (blue)

**Navigation:** Same breadcrumb bar as Save As. **Ctrl+L** or typing **/** opens an inline "Enter location or URL" text field with live path autocomplete.

**Left sidebar:** Recent (shows recently opened files with Location and Accessed columns), Home, Documents, Downloads, Music, Pictures, Videos, Trash, + Other Locations.

**File browser:** Same sortable columns as Save As.

**Bottom controls:**
- **Version** dropdown (for versioned ODF files)
- **Read-only** checkbox — opens file in read-only mode
- **File type filter** dropdown — ~50+ format types covering all LibreOffice-supported formats plus legacy word processors (WordPerfect, Lotus WordPro, AppleWorks, etc.)

## Remote Files Dialog

Opened via File > Open Remote.... Provides a two-pane browser (folder tree + file listing) with:
- **Service** dropdown + **Manage services** button
- **Add service** dialog supporting: Google Drive, WebDAV, SSH, Windows Share, SharePoint 2010/2013, Alfresco, IBM FileNet, Nuxeo, OpenDataSpace, and other CMIS servers
- List/Icon view toggle, file name field, filter dropdown

---

## UI Reference  —  File Menu

_Scope: Save, Save As, Save Remote, Save a Copy, Save All commands_

The File menu manages the full document lifecycle: creating, opening, saving, exporting, printing, and closing documents.

Read the screenshot `ui-file-menu.png` in this directory.

## Elements

- **New** (►) — Create a new document of any type (Text, Spreadsheet, Presentation, Drawing, etc.). Ctrl+N for Text Document.
- **Open…** (Ctrl+O) — Open an existing file.
- **Open Remote…** — Open a file from a remote server.
- **Recent Documents** (►) — List of recently opened files.
- **Close** — Close the current document.
- **Wizards** (►) — Step-by-step creation wizards: Letter, Fax, Agenda, Document Converter, Address Data Source.
- **Templates** (►) — Edit Template, Save as Template, Manage Templates (Shift+Ctrl+N).
- **Reload** — Reload document from disk (greyed on unsaved documents).
- **Versions…** — Manage saved versions of the document.
- **Save** (Ctrl+S) — Save in current format.
- **Save As…** (Shift+Ctrl+S) — Save with a new name or format.
- **Save Remote…** — Save to a remote server.
- **Save a Copy…** — Save a copy without changing the working file.
- **Save All** — Save all open documents.
- **Export…** — Export in a non-native format.
- **Export As** (►) — Export as PDF (dialog or direct), Export as EPUB (dialog or direct).
- **Send** (►) — Email document in various formats (ODF, Word, PDF), send via Bluetooth, create Master/HTML document.
- **Preview in Web Browser** — Open document preview in default browser.
- **Print Preview** (Shift+Ctrl+O) — Toggle print-preview layout.
- **Print…** (Ctrl+P) — Open the Print dialog.
- **Printer Settings…** — Configure printer options.
- **Properties…** — Open the 6-tab document properties dialog (General, Description, Custom Properties, Security, Font, Statistics).
- **Digital Signatures** (►) — Digital Signatures…, Sign Existing PDF…
- **Exit LibreOffice** (Ctrl+Q) — Quit the entire suite.


# Creating and Opening Documents (LibreOffice Writer 7.3.7)

When you first launch LibreOffice, you land at the Start Center — a hub showing your recent documents and quick-access buttons for creating new ones. To jump straight into a blank text document, just click **Create: Writer Document**. If you'd rather work from a template, click **Templates** instead to browse what's available.

See `fig01.png`.

If Writer is already open and you want a fresh document, hit *Ctrl+N* or go to **File > New > Text Document** on the Menu bar. You can also click the **New** icon on the Standard toolbar. Either way, a brand-new document opens in its own window.

Templates are handy when you need consistent formatting across multiple documents — same headers, footers, fonts, and styles every time. A default installation ships with only a few, but you can grab more from the extensions site or create your own. To open the Templates dialog, press *Ctrl+Shift+N*, or choose **File > Templates > Manage Templates**, or go through **File > New > Templates**. You can also click the arrow next to the **New** toolbar icon and select **Templates** from the drop-down. Once you find a template you like in the **Documents** folder, double-click it to create a new document based on it, or right-click it and choose **Open**.

See `fig02.png`.

Opening an existing document is just as straightforward. From the Start Center, click **Open File** (or **Remote Files** for cloud-stored documents). If Writer is already running, use **File > Open** or press *Ctrl+O*. You can also click the **Open** icon on the Standard toolbar, or use the small triangle next to it for a list of recently opened files. Another quick route is **File > Recent Documents**. The Start Center itself shows thumbnails of your recent documents — just click one to reopen it. If a file has been moved or deleted, its thumbnail may linger in the list; hover over it until an **X** appears in the corner, then click to remove it.

---

## UI Reference  —  File Open & Save As Dialogs

_Scope: Open dialog: breadcrumb navigation, sidebar locations, file browser, file type filter, Read-only checkbox_

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

_Scope: New, Open, Open Remote, Recent Documents, Templates submenu entries_

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

---

## UI Reference  —  Standard Toolbar

_Scope: New (Ctrl+N) and Open (Ctrl+O) buttons_

The first toolbar row below the menu bar provides quick access to file operations, clipboard, editing, and insert commands.

Read the screenshot `ui-standard-toolbar.png` in this directory.

## Elements

Row (left → right):

- **New** (Ctrl+N, split-button ▼) — New document; dropdown lists all document types.
- **Open** (Ctrl+O) — Open file dialog.
- **Save** (Ctrl+S, split-button ▼) — Save; dropdown: Save As…, Export…, Save a Copy…, Save as Template…, Save Remote File…
- **Export Directly as PDF** — One-click PDF export.
- **Print** (Ctrl+P) — Print dialog.
- **Toggle Print Preview** (Shift+Ctrl+O)

| *(separator)* |

- **Cut** (Ctrl+X) / **Copy** (Ctrl+C) / **Paste** (Ctrl+V, split-button ▼)
- **Clone Formatting** — Paint-format brush; double-click for persistent mode.

| *(separator)* |

- **Undo** (Ctrl+Z, split-button ▼) / **Redo** (Ctrl+Y)

| *(separator)* |

- **Find and Replace** (Ctrl+H) — Opens Find & Replace dialog.
- **Check Spelling** (F7)
- **Toggle Formatting Marks** (Ctrl+F10) — Show/hide ¶ marks, spaces, tabs.

| *(separator)* |

- **Insert Table** (Ctrl+F12, split-button ▼) — Dialog or visual grid picker for row×column count.
- **Insert Image** — File picker for images.
- **Insert Chart** — Embed chart OLE object.
- **Insert Text Box** — Draw a text frame on canvas.
- **Insert Page Break** (Ctrl+Return)
- **Insert Field** (split-button ▼) — Page Number, Page Count, Date/Time, Title, Author, Subject, More Fields…
- **Insert Special Characters** (split-button ▼) — Full character picker or favorites quick-pick.

| *(separator)* |

- **Insert Hyperlink** (Ctrl+K) — Hyperlink dialog.
- **Insert Footnote** / **Insert Endnote**
- **Insert Bookmark** — Bookmark dialog.
- **Insert Cross-reference** — Cross-reference dialog.
- **Insert Comment** (Ctrl+Alt+C)
- **Show Track Changes Functions** — Toggle Track Changes toolbar.

| *(separator)* |

- **Insert Line** — Line-drawing mode; double-click for persistent mode.
- **Basic Shapes** (split-button ▼) — 4×6 shape palette.
- **Show Draw Functions** — Toggle Drawing toolbar.


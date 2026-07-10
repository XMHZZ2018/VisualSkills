# Loading and Saving Options (LibreOffice Writer 7.3.7)

Head over to **Tools > Options** and expand **Load/Save** on the left to find all the settings that control how Writer opens and saves your documents. The General page is the one you'll use most.

Under the **Load** section, you'll see **Load user-specific settings with the document**. When this is on, Writer applies the original author's settings (like printer config) when you open their file. If you're working in an office where documents bounce between people and printers, you might want to turn this off so your own system settings take priority. Note that some things — like data source links, spacing options for paragraphs before text tables, and field function update settings — always load with the document regardless.

There's also **Load printer settings with the document**. Leaving it enabled means a document could try to print to a network printer you don't have access to, so disable it if that's a concern.

See `fig01.png`.

The **Save** section is where you set up your safety net. **Save AutoRecovery information every __ minutes** tells Writer how often to stash recovery data. Keep this on — if Writer crashes, you'll be glad it saved a snapshot ten minutes ago instead of never. You can adjust the interval to taste.

**Edit document properties before saving** pops up the document's Properties dialog the first time you save (or use Save As), handy if you like to fill in metadata early. **Always create backup copy** saves the previous version of your file with a `.bak` extension in a separate folder. You can find (or change) that folder under **Tools > Options > LibreOffice > Paths**.

Under **Default File Format and ODF Settings**, pick the ODF format version and set what **Always save as** defaults to — for instance, ODF Text Document (`.odt`). If you regularly exchange files with Microsoft Office users, you could set this to a Word format instead, though you'll get a warning when saving in non-ODF formats. The **Warn when not saving in ODF or default format** checkbox controls that nudge.

If you work on long documents or anything you can't afford to lose, seriously consider enabling both AutoRecovery and backup copies. They work independently: AutoRecovery protects against crashes, while backup copies protect against accidental overwrites. Belt and suspenders.

---

## UI Reference  —  File Open & Save As Dialogs

_Scope: Save As file format dropdown (18 formats including ODF and Word variants)_

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

## UI Reference  —  Tools Menu

_Scope: Options > Load/Save sub-tree_

The Tools menu provides document proofing, language settings, automation, and application-wide configuration.

Read the screenshot `ui-tools-menu.png` in this directory.

## Elements

- **Spelling…** (F7) — Open the spelling dialog.
- **Automatic Spell Checking** (Shift+F7) — Toggle live spell-check underlines.
- **Thesaurus…** (Ctrl+F7) — Look up synonyms (requires thesaurus dictionary).
- **Language** (►) — Set language For Selection / For Paragraph / For All Text, Hyphenation…, More Dictionaries Online…
- **Word Count…** — Show detailed word/character counts.
- **Accessibility Check…** (Alt+8) / **Automatic Accessibility Checking** — Audit document for accessibility issues.
- **AutoCorrect** (►) — While Typing (toggle), Apply, Apply and Edit Changes, AutoCorrect Options… (5-tab dialog: Replace, Exceptions, Options, Localized Options, Word Completion).
- **AutoText…** (Ctrl+F3) — Manage reusable text blocks.
- **Redact** / **Auto-Redact** — Document redaction tools.
- **Heading Numbering…** — Configure outline numbering for headings.
- **Line Numbering…** — Enable/configure line numbers (position, interval, separator).
- **Footnote/Endnote Settings…** — Configure footnote/endnote formatting.
- **Mail Merge Wizard…** — Step-by-step mail merge.
- **Bibliography Database** / **Address Book Source…** — Database connections.
- **Update** (►) — Refresh: Update All, Page Formatting, Fields (F9), Indexes and Tables, Links, Charts.
- **Protect Document** (►) — Protect Fields (checkbox), Protect Bookmarks (checkbox).
- **Calculate** (Ctrl++) / **Sort…** — In-document calculation and sorting.
- **Macros** (►) — Run Macro…, Edit Macros…, Organize Macros, Digital Signature…, Organize Dialogs…
- **Development Tools** — Toggle developer panel.
- **XML Filter Settings…** / **Extensions…** (Ctrl+Alt+E) / **Customize…**
- **Options…** (Alt+F12) — Opens the comprehensive Options dialog with tree navigation: LibreOffice (User Data, General, View, Print, Paths, Fonts, Security, etc.), Load/Save, Languages, LibreOffice Writer, and more.


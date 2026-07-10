# Customizing Menus, Toolbars, and UI (LibreOffice Writer 7.3.7)

Writer gives you a lot of freedom to reshape the interface to match the way you actually work. Menus, toolbars, even the overall UI layout — it's all fair game.

To get started with any customization, head to **Tools > Customize**. This opens the Customize dialog, which has tabs for **Menus**, **Toolbars**, **Notebookbar**, **Context Menus**, **Keyboard**, and **Events**. The **Scope** drop-down in the upper right lets you decide whether your changes apply to all of Writer or just the current document.

See `fig01.png`.

**Tweaking an existing menu** is straightforward. On the **Menus** tab, pick the menu you want from the **Target** drop-down — you'll see its current commands listed under **Assigned Commands**. To add a command, find it in the **Available Commands** list on the left (use the **Search** box or filter by **Category**), then click the right arrow to move it over. Reorder items with the up/down arrows, or remove one by selecting it and clicking the left arrow. You can rename entries via **Modify > Rename** and insert separators or submenus from the **Insert** drop-down.

If you need an entirely **new menu**, click the symbol next to **Target** and choose **Add**. Give it a name, position it among the existing menus, and hit **OK**. Then populate it with commands using the same process described above.

**Customizing toolbars** works almost identically. Switch to the **Toolbars** tab, pick the toolbar from **Target**, and add or remove commands the same way. You can show or hide individual commands by toggling the checkbox next to each item in the **Assigned Commands** list. To **create a new toolbar**, click the symbol next to **Target**, select **Add**, name it, and choose whether to save it for Writer globally or just the current document.

See `fig02.png`.

Toolbar buttons typically display icons rather than text. If a command doesn't have a default icon, select it and go to **Modify > Change Icon**. The Change Icon dialog lets you pick from built-in icons or **Import** a custom one (16×16 pixels, no more than 256 colors works best).

For a bigger UI overhaul, Writer offers alternative interface layouts. Go to **View > User Interface** to switch between variants like **Tabbed**, **Tabbed Compact**, and **Groupedbar Compact** — these replace the traditional menu bar and toolbars with a ribbon-style interface organized by context tabs. Once you've selected a variant, fine-tune which tabs appear using the **Notebookbar** tab back in **Tools > Customize**. Hit **Reset** any time you want to return to the defaults.

When you're happy with everything, click **OK** to save your changes and close the Customize dialog.

---

## UI Reference  —  Edit, View, Window & Help Menus

_Scope: View > Toolbars > Customize…; View > User Interface…_

These menus provide standard editing operations, display controls, window management, and help access.

## Edit Menu

(see screenshot `ui-edit-menu.png`)

- **Undo** (Ctrl+Z) / **Redo** (Ctrl+Y) / **Repeat** (Shift+Ctrl+Y)
- **Cut** (Ctrl+X) / **Copy** (Ctrl+C) / **Paste** (Ctrl+V) — standard clipboard operations.
- **Paste Special** (►) — Paste Unformatted Text (Shift+Ctrl+Alt+V), Paste Special… (Shift+Ctrl+V), Paste as Nested Table, Paste as Rows Above, Paste as Columns Before.
- **Select All** (Ctrl+A)
- **Selection Mode** (►) — Standard (default) or Block Area (Shift+Alt+F8) for column selection.
- **Find…** (Ctrl+F) — Opens the inline Find toolbar.
- **Find and Replace…** (Ctrl+H) — Opens the Find and Replace dialog (see [Formatting Dialogs](formatting-dialogs.md)).
- **Go to Page…** (Ctrl+G) — Jump to a specific page number.
- **Track Changes** (►) — Record, Show, Manage, Accept/Reject individual or all changes, Compare/Merge documents.
- **Comment** (►) — Reply, Resolve, Delete comments and comment threads.
- **Reference** (►) — Insert Footnote/Endnote, Index Entry, Bibliography Entry.
- **Fields…** / **External Links…** / **OLE Object** (►) — Context-sensitive editing commands.
- **Exchange Database…** — Switch the document's database source.
- **Direct Cursor Mode** — Toggle: click anywhere on the page to place the cursor.
- **Edit Mode** (Shift+Ctrl+M) — Toggle between edit and read-only mode.

## View Menu

(see screenshot `ui-view-menu.png`)

- **Normal** / **Web** — Radio pair for print-layout vs web-layout editing view.
- **User Interface…** — Choose from 7 UI variants (Standard Toolbar, Tabbed, Single Toolbar, Sidebar, etc.).
- **Toolbars** (►) — Toggle ~27 available toolbars on/off. Includes Customize… and Lock Toolbars.
- **Status Bar** — Toggle status bar visibility.
- **Rulers** (►) — Toggle horizontal ruler (Shift+Ctrl+R) and vertical ruler.
- **Scrollbars** (►) — Toggle horizontal and vertical scrollbars.
- **Grid and Helplines** (►) — Display Grid, Snap to Grid, Helplines While Moving.
- **Formatting Marks** (Ctrl+F10) — Show/hide paragraph marks, spaces, tabs.
- **Text/Table/Section Boundaries**, **Images and Charts**, **Whitespace** — Visibility toggles (all on by default).
- **Show Tracked Changes** — Toggle track-change markup display.
- **Field Shadings** (Ctrl+F8) / **Field Names** (Ctrl+F9) / **Field Hidden Paragraphs** — Field display options.
- **Sidebar** (Ctrl+F5) — Toggle the right sidebar panel.
- **Styles** (F11) / **Gallery** — Quick access to sidebar panels.
- **Navigator** (F5) — Toggle the document structure navigator.
- **Data Sources** (Shift+Ctrl+F4) — Toggle the database data-source view.
- **Full Screen** (Shift+Ctrl+J) — Hide menus/toolbars for maximum editing area.
- **Zoom** (►) — Presets (Entire Page, Page Width, 50%–200%) and full Zoom & View Layout dialog.

## Window Menu

- **New Window** — Open a second window for the same document.
- **Close Window** (Ctrl+W) — Close the current window.
- Active document list — bullet marks the current window.

## Help Menu

- **LibreOffice Help** (F1), **What's This?**, **User Guides**
- **Show Tip of the Day**, **Search Commands** (Shift+Escape)
- **Get Help Online**, **Send Feedback**, **Restart in Safe Mode…**
- **Get Involved**, **Donate to LibreOffice**, **License Information**, **About LibreOffice**

---

## UI Reference  —  Tools Menu

_Scope: Customize… command opening the Customize dialog (Menus/Toolbars/Keyboard tabs)_

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


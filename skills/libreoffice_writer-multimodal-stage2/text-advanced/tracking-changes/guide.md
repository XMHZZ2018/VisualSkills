# Tracking Changes (LibreOffice Writer 7.3.7)

Writer's change tracking feature — sometimes called "redlines" or "revision marks" — lets you record every addition, deletion, and formatting tweak so that you or a colleague can review them later. Not everything gets tracked (tab stops, formulas, and linked graphics are notable exceptions), but for day-to-day text editing it covers what you need.

**Turning it on** is simple: go to **Edit > Track Changes > Record**. The menu item appears highlighted when recording is active. To toggle the visual markup on or off without stopping the recording, use **Edit > Track Changes > Show**. Hover over any marked change to see a tooltip with the author, date, time, and type of edit.

You can also add a comment to a specific change by placing your cursor in the changed area and choosing **Edit > Track Changes > Comment**, or clicking the **Insert Track Change Comment** button on the Track Changes toolbar. Use the arrow buttons inside the comment dialog to step through changes one by one.

When you're done editing, stop recording with another click on **Edit > Track Changes > Record**.

See `fig01.png`.

**Preparing a document for review** is worth a moment of setup. First, check whether the file already contains multiple versions (**File > Versions**); if so, save the current state as a separate document and use that as your review copy. Make sure recording is on, then lock it down with **Edit > Track Changes > Protect** — enter a password (twice) and click **OK**. Now reviewers must supply the password before they can turn off tracking or accept/reject changes. A shortcut: you can do the same thing from **File > Properties > Security** by selecting **Record changes**, clicking **Protect**, and entering the password.

**Accepting or rejecting changes** can happen several ways. For quick, inline decisions, right-click a tracked change and choose **Accept Change** or **Reject Change** from the context menu. Accepting a change makes it permanent; rejecting it reverts the text to its original state.

For a broader view, open **Edit > Track Changes > Manage**. The Manage Changes dialog lists every pending change with its action type, author, date, and any comment. Select a change and the corresponding text highlights in the document so you can see exactly what's affected. Click **Accept** or **Reject** for individual changes, or use **Accept All** / **Reject All** to handle everything at once.

See `fig02.png`.

Need to narrow things down? Switch to the **Filter** tab in the Manage Changes dialog to filter by date range, author, action type, or comment text. Once your filter is set, flip back to the **List** tab to see only the changes that match.

If a reviewer forgot to turn on tracking altogether, you can still recover the differences. Open the edited document, then go to **Edit > Track Changes > Compare Document**, pick the original file, and click **Open**. Writer marks all the differences as tracked changes, and from there you accept or reject them in the usual way.

---

## UI Reference  —  Right Sidebar

_Scope: Manage Changes panel (Alt+7): List tab with Accept/Reject, Filter tab_

The collapsed right sidebar is a vertical strip of 8 icon buttons along the right edge of the window. Each opens a full docked panel. Toggle the sidebar with Ctrl+F5 or View > Sidebar.

Read the screenshot `ui-right-sidebar-location.png` in this directory.

## Panel Buttons (top to bottom)

- **Properties** (Alt+1) — Formatting panel with three collapsible sections:
  - *Style:* Paragraph style dropdown, Clone Formatting, Update/New Style buttons.
  - *Character:* Font family, size, Bold/Italic/Underline/Strikethrough, Font Color, Highlighting, Change Case, Super/Subscript.
  - *Paragraph:* Alignment, lists/indent toolbar, line spacing, above/below spacing fields, left/right/first-line indent.

- **Styles** (Alt+2 / F11) — Full style manager: category toolbar (Paragraph/Character/Frame/Page/List/Table Styles), hierarchical style list, Fill Format Mode, filter dropdown. See [Styles](styles.md).

- **Gallery** (Alt+3) — Clip-art browser: categories (Arrows, BPMN, Bullets, Diagrams, Flow chart, Icons), thumbnail grid, Icon/Detailed view, New… button.

- **Navigator** (Alt+4 / F5) — Document structure tree: Headings, Tables, Frames, Images, OLE objects, Bookmarks, Sections, Hyperlinks, References, Indexes, Comments, Drawing objects, Fields, Footnotes, Endnotes. Includes page navigation controls and drag-mode options.

- **Page** (Alt+5) — Page layout panel:
  - *Format:* Size (A4), Width/Height, Orientation (Portrait/Landscape), Margins.
  - *Styles:* Page number format, Background, Layout, Columns.
  - *Header/Footer:* Enable toggles, margins, spacing, same-content options.

- **Style Inspector** (Alt+6) — Two-column Properties/Value tree showing all applied styles: Paragraph Styles, Paragraph Direct Formatting, Character Styles, Character Direct Formatting (50+ properties per node).

- **Manage Changes** (Alt+7) — Two tabs:
  - *List:* Action/Author/Date/Comment table with Accept/Reject/Accept All/Reject All buttons.
  - *Filter:* Date range, Author, Action, Comment filters.

- **Accessibility Check** (Alt+8) — Runs an accessibility audit and lists issues by category, each with a Fix… button.

---

## UI Reference  —  Edit, View, Window & Help Menus

_Scope: Edit > Track Changes submenu: Record, Show, Manage, Accept/Reject, Compare/Merge_

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


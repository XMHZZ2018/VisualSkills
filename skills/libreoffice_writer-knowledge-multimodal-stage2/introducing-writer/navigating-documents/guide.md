# Navigating Documents (LibreOffice Writer 7.3.7)

Writer gives you several handy ways to jump around a document without endless scrolling. The two main tools are **Go to Page** and the **Navigator**, and once you know them, moving through even a huge document feels effortless.

**Go to Page** is the quickest way to land on a specific page. Open it with **Edit > Go to Page**, by pressing **Ctrl+G**, or simply by clicking the page number field on the Status Bar. A small dialog pops up showing the current page and the total page count — type your target page number, hit **OK**, and you're there. You can also use the *Go to Page* field at the top right of the Navigator for the same purpose.

See `fig01.png`.

The **Navigator** is the real powerhouse. It lives in the Sidebar — click the **Navigator** tab on the right, press **F5**, or go to **View > Navigator** on the Menu bar. It lists every heading, table, text frame, graphic, bookmark, and other object in your document in a collapsible tree. Click the little arrow next to a category to expand it, then double-click any item to jump straight to its location.

See `fig02.png`.

At the top of the Navigator you'll find a *Navigate By* drop-down list where you pick what type of object you want to step through — headings, bookmarks, tables, graphics, index entries, and more. Once you've chosen a type, use the **Previous** and **Next** icons (or buttons) to hop from one instance to the next throughout the document.

If you only care about one category — say, Headings — highlight it and click the **Content Navigation View** icon. This hides everything else so you can focus. Click it again to restore the full list. You can also adjust the number of heading levels displayed.

**Setting reminders** is a lesser-known gem. Click the **Set Reminder** icon in the Navigator to drop a bookmark at the cursor's current spot. You can set up to five reminders in a document (a sixth replaces the first). To revisit them, select **Reminder** in the *Navigate By* drop-down and click **Previous** or **Next**. They aren't visible in the text and aren't saved with the document — they're purely for your current editing session.

One practical tip: objects are much easier to find if you give them meaningful names when you create them. By default, Writer names things generically (Image1, Table1, etc.). You can rename an object later by right-clicking it in the Navigator and choosing **Rename**, or via **Image > Rename** in the context menu.

---

## UI Reference  —  Right Sidebar

_Scope: Navigator panel (Alt+4/F5) with document structure tree and page navigation_

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

_Scope: Edit > Go to Page (Ctrl+G); View > Navigator (F5)_

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

## UI Reference  —  Status Bar

_Scope: Page Number segment: left-click opens Go to Page dialog_

The status bar runs across the bottom of the window. Every segment is interactive.

Read the screenshot `ui-status-bar.png` in this directory.

## Segments (left to right)

- **Page Number** ("Page 1 of 1") — Left-click opens Go to Page dialog (page number spinner). Right-click shows bookmark list.

- **Word / Character Count** ("0 words, 0 characters") — Left-click opens Word Count dialog showing Words, Characters (incl/excl spaces), Comments for both selection and whole document.

- **Page Style** ("Default Page Style") — Left-click opens the Page Style dialog (9 tabs: Organizer, Page, Area, Transparency, Header, Footer, Borders, Columns, Footnote). Right-click shows quick-change list of all page styles: Default Page Style, First Page, Left Page, Right Page, Envelope, Index, HTML, Footnote, Endnote, Landscape.

- **Language** ("English (USA)") — Click opens language popup: current language (checked), None (no spell-check), Reset to Default Language, More…, Set Language for Paragraph (►).

- **Selection Mode** — Click opens radio-button popup: Standard selection, Extending selection, Adding selection, Block selection.

- **View Layout buttons** — Three icons:
  - Single-page view (one page at a time)
  - Multiple-page view (pages side by side)
  - Book view (two-page spread)

- **Zoom controls** — Zoom Out (−) button, drag slider, Zoom In (+) button.

- **Zoom Percentage** ("100%") — Left-click opens Zoom & View Layout dialog (Optimal, Fit width and height, Fit width, 100%, Custom; View Layout: Automatic, Single page, Columns, Book mode). Right-click shows quick-pick presets: Entire Page, Page Width, Optimal View, 50%–200%.


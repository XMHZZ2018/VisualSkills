# Selecting, Cutting, Copying, and Pasting Text (LibreOffice Writer 7.3.7)

Selecting text in Writer works much like any other application. You can swipe the mouse cursor over text to highlight it, or use multiple clicks for quick selections: double-click grabs a word, triple-click selects a sentence, and quadruple-click selects the entire paragraph.

For more control, click where you want to start, then press *F8* to enter **Extending selection** mode. Now just use the arrow keys to extend your selection precisely, and press *F8* again when you're done. This is especially handy when you need to highlight a large or awkward block without dragging.

You can change the selection mode from the **Selection icon** on the Status Bar at the bottom of the window. Right-click it to choose between **Standard selection**, **Extending selection** (*F8*), **Adding selection** (*Shift+F8*), and **Block selection** (*Ctrl+Shift+F8*). Left-clicking the icon cycles through them.

See `fig01.png`.

To select non-consecutive items — say, a word in one paragraph and another word three paragraphs down — use the mouse in **Standard selection** mode: select the first piece, hold *Ctrl*, then select the next piece. Repeat as needed. If you prefer the keyboard, select your first piece, press *Shift+F8* to enter **Adding selection** mode, arrow-navigate to the next piece, and hold *Shift* to extend. Press *Esc* when you're finished.

See `fig02.png`.

Need to select a vertical block of text — like a column of data that spans several lines? Use **Edit > Selection Mode > Block Area**, press *Ctrl+F8*, or click the **Selection** icon and choose **Block selection**. Then just drag or use the keyboard to highlight a rectangular region.

See `fig03.png`.

Once you've got your text selected, cutting, copying, and pasting work exactly as you'd expect. Use **Edit > Cut**, **Edit > Copy**, and **Edit > Paste** from the menu bar, or stick with the familiar keyboard shortcuts: *Ctrl+X* to cut, *Ctrl+C* to copy, and *Ctrl+V* to paste. You can move text within a document, between documents, or even between Writer and other applications — just select, cut or copy, click where you want it, and paste.

---

## UI Reference  —  Edit, View, Window & Help Menus

_Scope: Edit: Cut/Copy/Paste, Select All, Selection Mode (Standard/Block Area)_

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

_Scope: Selection Mode segment: Standard/Extending/Adding/Block selection toggle_

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


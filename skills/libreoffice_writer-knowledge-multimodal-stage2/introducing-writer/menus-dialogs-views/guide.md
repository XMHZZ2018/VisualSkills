# Context Menus, Dialogs, and Document Views (LibreOffice Writer 7.3.7)

Writer gives you several ways to interact beyond the main menu bar — context menus, dialogs, and different document views all help you work more efficiently. Here's how they fit together.

**Context menus** are the right-click menus that pop up throughout Writer. Right-click on a paragraph, image, table, or any other object and you'll get a menu tailored to whatever you selected. The options change depending on context — right-clicking a word offers spelling and formatting choices, while right-clicking an image gives you anchoring and wrap options. Context menus are especially handy when you're not sure where a function lives in the main menu bar; chances are it's a right-click away.

**Dialogs** are the pop-up windows that appear when you choose a menu item ending in ellipses, like **Format > Paragraph...**. A dialog either informs you of something, asks for input, or both — it provides controls so you can specify exactly how to carry out an action. While a dialog is open, you can only interact with it, not the document behind it. Clicking **OK** (or a similar button) saves your changes and closes the dialog; clicking **Cancel** discards everything. Some dialogs, like **Find & Replace**, are non-modal — you can switch back and forth between them and your document as you work.

Writer offers three **document views**, all accessible from the **View** menu. **Normal** is the default editing view with full page layout. **Web** shows your document as it would appear in a browser, which is useful if you're authoring HTML content. **Full Screen** hides toolbars and menus to maximize your editing space — press *Esc* to return to the normal interface.

You can also adjust the **view layout** using the icons on the Status Bar at the bottom of the window. Choose between single-page, multiple-page, and book layout to control how pages are arranged on screen. These interact with the zoom level: dragging the **Zoom** slider or clicking the **+** and **−** signs changes magnification, and you can right-click the zoom percentage for a list of preset values.

See `fig01.png`.

Between context menus for quick access, dialogs for detailed settings, and view options for comfortable reading, you've got plenty of ways to tailor Writer to how you actually work.

---

## UI Reference  —  Edit, View, Window & Help Menus

_Scope: View menu: Normal/Web views, Zoom submenu with presets, Full Screen toggle_

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

_Scope: View Layout buttons and Zoom slider/percentage with presets_

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


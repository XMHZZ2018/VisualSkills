# Adding Comments (LibreOffice Writer 7.3.7)

Comments let authors and reviewers exchange ideas, flag issues, or suggest changes without altering the document text itself. You can attach a comment to a selected block of text — even spanning multiple paragraphs — or drop one at a single insertion point.

To insert a comment, select the text you want to annotate (or just place your cursor where the comment should go), then choose **Insert > Comment** or press **Ctrl+Alt+C**. You can also click the **Insert Track Change Comment** button on the Track Changes toolbar. A dotted line connects your anchor point to a box on the right-hand side of the page where you type your note. A **Comments** button also appears to the right of the horizontal ruler; click it to toggle comment display on and off.

See `fig01.png`.

Writer automatically stamps each comment with your name and a timestamp. If the name shown isn't right, head to **Tools > Options > LibreOffice > User Data** and update the Author field.

When you're done typing, just click somewhere else on the page — the comment is saved in place. If more than one person edits the document, each author's comments get a different background color so you can tell them apart at a glance. When an author selects text that overlaps another author's comments, the replies are nested under the first author's notes.

Right-click any comment to open a context menu where you can delete that single comment, all comments from the same author, or every comment in the document. From the same menu, choose **Format all comments** to apply basic formatting — font type, size, and alignment — to the comment text.

Once a comment has been addressed, you can mark it as resolved or unresolved via the comment's context menu. The word "Resolved" appears beneath the date, and you can show or hide all resolved comments with **View > Resolved Comments**.

To jump between comments, open the Navigator with **F5**, expand the **Comments** section, and double-click an entry to land at its anchor in the document. Alternatively, select **Comment** in the **Navigate By** box at the top of the Navigator and use the Up and Down arrows. The keyboard works too: **Ctrl+Alt+Page Down** moves to the next comment, **Ctrl+Alt+Page Up** goes to the previous one.

When it's time to print, you have options. Go to **File > Print > LibreOffice Writer** tab and look at the **Comments** drop-down list. You can print comments only, place them at end of document, at end of page, or in the margins — whatever suits your workflow.

See `fig02.png`.

---

## UI Reference  —  Insert Menu

_Scope: Comment (Ctrl+Alt+C) command_

The Insert menu provides commands for adding content elements — breaks, images, tables, shapes, fields, footnotes, hyperlinks, and more — into the document.

Read the screenshot `ui-insert-menu.png` in this directory.

## Elements

- **Page Break** (Ctrl+Return) — Insert a manual page break at cursor.
- **More Breaks** (►) — Manual Row Break (Shift+Return), Column Break (Shift+Ctrl+Return), Manual Break… (dialog to choose break type and page style).
- **Image…** — Open file chooser to insert a raster or vector image.
- **Chart…** — Embed a chart OLE object.
- **Media** (►) — Gallery, Scan, Audio or Video…
- **OLE Object** (►) — Formula Object (Shift+Alt+E), QR and Barcode…, OLE Object…
- **Shape** (►) — 7 shape categories: Line, Basic Shapes, Block Arrows, Symbol Shapes, Stars and Banners, Callout Shapes, Flowchart — each opens a named-shape palette.
- **Section…** — Opens Insert Section dialog (tabs: Section, Columns, Indents, Area, Footnotes/Endnotes). Supports linked sections, write protection, and conditional hiding.
- **Text from File…** — Insert text from an external file.
- **Text Box** — Draw a floating text frame on the canvas.
- **Comment** (Ctrl+Alt+C) — Insert an annotation balloon.
- **Frame** (►) — Frame Interactively (draw) or Frame… (dialog).
- **Fontwork…** — Decorative text shapes gallery.
- **Hyperlink…** (Ctrl+K) — Hyperlink dialog with 4 type modes: Internet, Mail, Document, New Document.
- **Bookmark…** — Insert/manage bookmarks.
- **Cross-reference…** — Link to headings, bookmarks, figures, or other elements.
- **Special Character…** — Character picker dialog with search, font/block selectors, hex/decimal codes, favorites/recent.
- **Formatting Mark** (►) — No-break Space (Shift+Ctrl+Space), Non-breaking Hyphen, Soft Hyphen, Narrow No-break Space, Zero-width Space, Word Joiner.
- **Horizontal Line** — Insert a horizontal rule.
- **Footnote and Endnote** (►) — Insert Footnote, Endnote, or open the Footnote/Endnote dialog.
- **Table of Contents and Index** (►) — TOC/Index/Bibliography dialog, Index Entry, Bibliography Entry.
- **Page Number…** — Page number insertion dialog.
- **Field** (►) — Page Number, Page Count, Date/Time (fixed or variable), Title, Author, Subject, More Fields… (Ctrl+F2).
- **Header and Footer** (►) — Enable/disable headers and footers per page style.
- **Envelope…** — Envelope configuration dialog.
- **Signature Line…** — Digital-signature placeholder line.

---

## UI Reference  —  Edit, View, Window & Help Menus

_Scope: Edit > Comment submenu: Reply, Resolve, Delete_

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

## UI Reference  —  Standard Toolbar

_Scope: Insert Comment (Ctrl+Alt+C) button_

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


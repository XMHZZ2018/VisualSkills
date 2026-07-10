# Using Drawing Tools (LibreOffice Writer 7.3.7)

Writer has a surprisingly capable set of built-in drawing tools for creating simple diagrams with rectangles, circles, lines, arrows, and predefined shapes. You can place drawing objects directly on a page or group them into a frame. For complex drawings, you're better off in LibreOffice Draw, but for quick illustrations, Writer handles things just fine.

To get started, show the Drawing toolbar by going to **View > Toolbars > Drawing**, or click the **Show Draw Functions** icon on the standard toolbar. The toolbar gives you access to lines, arrows, rectangles, ellipses, polygons, curves, callouts, flowcharts, block arrows, stars, and more.

Pick a tool from the toolbar, then click and drag on your document to create the shape. The cursor turns into a crosshair — just draw out the size you want and release. The tool stays active afterward so you can draw another object of the same type. Press **Esc** or click the **Select** icon (the arrow) on the Drawing toolbar when you're done.

Once you've drawn something, the normal Formatting toolbar swaps out for the **Drawing Object Properties** toolbar. From there you can quickly adjust fill color, line style, line width, arrow styles, and anchoring. For even more control, click the **Area** or **Line** icons on that toolbar to open detailed dialogs.

See `fig01.png` for the Drawing Object Properties toolbar with labeled icons.

You can set default properties for future objects before you draw them: click the **Select** tool, then adjust properties on the Drawing Object Properties toolbar. Those defaults stick for the current document and session only — they won't carry over to other files.

To reposition or resize a drawing object, select it and drag a handle. Hold **Shift** while dragging a corner handle to keep the original proportions. For precise control, right-click the object and choose **Position and Size**, or go to **Format > Text Box and Shape > Position and Size**, where you can set exact dimensions, rotation, and corner radius.

Grouping is handy when you've arranged several objects together and want them to behave as one unit. Select the objects by holding **Shift** and clicking each one, then go to **Format > Group > Group** (or right-click and choose **Group**). Editing within a group is easy — just go to **Format > Group > Enter Group**, make your changes, then **Format > Group > Exit Group** when you're done. To break a group apart entirely, select it and use **Format > Group > Ungroup**.

---

## UI Reference  —  Insert Menu

_Scope: Shape submenu (7 categories: Line, Basic Shapes, Block Arrows, etc.)_

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

## UI Reference  —  Standard Toolbar

_Scope: Insert Line, Basic Shapes palette, Show Draw Functions button_

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


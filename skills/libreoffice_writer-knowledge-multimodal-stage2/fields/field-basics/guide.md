# Field Basics and Document Properties (LibreOffice Writer 7.3.7)

Fields let you insert dynamic data into your document — things like the current date, page count, author name, or a product title that might change later. They show up with a gray background on screen (unless you've turned that off via **View > Field Shadings**), and that shading won't appear in print or PDF export.

A few keyboard shortcuts are worth memorizing. **Ctrl+F2** opens the full Fields dialog, **Ctrl+F8** toggles field shading on and off, **Ctrl+F9** switches between showing field names and their values, and **F9** forces all fields to update.

For everyday inserts, you don't need the full dialog. Just go to **Insert > Page Number** or **Insert > Field** on the Menu bar and pick from the submenu — page number, page count, date, time, title, first author, subject, and more are all one click away.

See `fig01.png`.

When you need fields tied to your document's own metadata, head to **File > Properties**. This dialog has six tabs; the General and Statistics tabs are auto-populated by Writer. The ones you care about are **Description** and **Custom Properties**.

On the **Description** tab you'll find fields for Title, Subject, Keywords, and Comments. Fill these in and you can reference them anywhere in the document as fields. Change the value here once, and every reference updates automatically — handy when a draft title becomes a final one.

See `fig02.png`.

The **Custom Properties** tab is where it gets flexible. It may be blank in a new document, or pre-filled if you started from a template. Hit the **Add Property** button in the lower right to create a new row. Give it a name (there's a dropdown of common choices, or type your own), pick a type — Text, DateTime, Date, Duration, Number, or Yes/No — and set its value. For example, you might store a "Guide Name" as Text with the value "Writer Guide", or a "LibreOffice Version" set to "7.3".

See `fig03.png`.

Once properties are defined, you can insert them as fields anywhere in the document through **Insert > Field > More Fields** (or **Ctrl+F2**). Whenever you update a property back in **File > Properties**, every field referencing it refreshes throughout the document. This makes Custom Properties ideal for information that appears in multiple places — project names, version numbers, client details — so you only ever maintain it in one spot.

---

## UI Reference  —  Insert Menu

_Scope: Field submenu: Page Number, Page Count, Date/Time, Title, Author, Subject, More Fields… (Ctrl+F2)_

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

_Scope: Insert Field split-button: Page Number, Date/Time, Title, Author, More Fields…_

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


# Other Types of Index (LibreOffice Writer 7.3.7)

Beyond the standard alphabetical index, Writer lets you build indexes of illustrations, tables, objects, and even user-defined categories. They all live under the same dialog and follow roughly the same workflow.

## Creating an Index of Tables, Illustrations, or Objects

Start by placing your cursor where you want the index to appear. Then go to **Insert > Table of Contents and Index > Table of Contents, Index or Bibliography**. In the dialog that opens, use the **Type** drop-down list to pick the kind of index you want — options include *Table of Figures*, *Index of Tables*, *Index of Objects*, and more.

The tabs in this dialog — entries, styles, columns, background — work much the same way as they do for a table of contents, so the concepts from those sections carry over here. Adjust whatever you need, then click **OK** to insert the index.

For a figures or tables index to work smoothly, your captions should have been created with **Insert > Caption** or by using a number range variable (as described in the Fields chapter). Writer relies on those caption categories to know what to collect into the index.

## Viewing and Editing Existing Index Entries

If you need to tweak entries after the fact, first turn on **View > Field Shadings** (or press *Ctrl+F8*) so that index entries are easy to spot in your text. Then place your cursor inside the field shading of an entry, right-click, and choose **Index Entry** from the context menu.

See `fig01.png`.

A dialog appears letting you modify the entry text, keys, or index assignment. Use the forward and back arrow buttons to step through all the entries in the document — handy for a quick review pass. When you're done, click **OK** to save your changes.

## User-Defined Indexes

You can also create a completely custom index. In the same **Type** drop-down, choose *User-Defined*. This lets you build an index around your own categories, giving you full control over what gets collected and how it's labeled. The process is identical: mark your entries in the document, then generate the index from the dialog.

---

## UI Reference  —  Insert Menu

_Scope: Table of Contents and Index > TOC/Index/Bibliography dialog_

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


# Generating Barcodes and QR Codes (LibreOffice Writer 7.3.7)

Writer, Calc, Impress, and Draw can all generate barcodes and QR codes directly — no extensions needed. Barcodes are used for all sorts of purposes, and a QR code (Quick Response code) is simply a type of barcode. QR codes often contain data that points to a website or application.

To get started, go to **Insert > Object > QR and Barcode** on the menu bar. This opens the **QR and Barcode** dialog where you configure everything in one place.

See `fig01.png`.

In the **URL/Text** field, type whatever data you want encoded — a URL like `www.libreoffice.org`, an ISBN number, a product code, or any plain text. Next, pick an **Error correction** level (Low, Medium, Quartile, or High). Higher correction makes the code more resilient to damage or smudging but also more complex visually.

Set the **Margin** value to control the whitespace border around the generated graphic. Finally, use the **Type** dropdown to choose between **QR Code** and **Barcode**. Hit **OK** and Writer drops the generated graphic right into your document.

See `fig02.png` for the barcode example.

Once the code is in your document, it behaves like any other embedded object. You can click it to select it, drag the handles to resize it, or reposition it on the page. If you need to change the encoded data or settings after the fact, just right-click the code and select **Edit Barcode** — the same dialog reopens so you can tweak anything.

---

## UI Reference  —  Insert Menu

_Scope: OLE Object > QR and Barcode…_

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


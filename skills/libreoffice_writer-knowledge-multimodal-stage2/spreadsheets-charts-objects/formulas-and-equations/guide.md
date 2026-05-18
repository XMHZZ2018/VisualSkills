# Formulas and Equations (LibreOffice Writer 7.3.7)

To drop a formula into your document, go to **Insert > Object > Formula** on the Menu bar. This opens the Math editor right inside Writer — the formula is embedded as an OLE object, so it lives inline with your text. You can also insert one via **Insert > OLE Object** if you prefer that route.

If you want numbered equations (handy for academic or technical documents), Writer has a neat AutoText shortcut. Start a new line, type `fn`, and press **F3**. A two-column table appears with no borders: the left cell holds a sample formula and the right cell holds an auto-incrementing reference number. Just delete the sample formula in the left cell and replace it with your own equation.
Alternatively, you can insert your formula into the document first using **Insert > Object > Formula**, then run through the `fn` AutoText trick and swap in your formula afterward — whichever order feels more natural.

While you're creating or editing a formula, the **Math** menu appears on the Menu bar, giving you access to all the symbol and structure tools from Math.

One thing to watch: make sure your formula's font size visually matches the surrounding text. If it looks off, double-click the formula to enter edit mode, then head to **Format > Font Size** on the Menu bar to adjust. To change the actual typeface, use **Format > Fonts** instead.

For deeper coverage of the Math markup language and all available operators, check out the dedicated *Math Guide* or Chapter 9, "Getting Started with Math," in the *Getting Started Guide*.

---

## UI Reference  —  Insert Menu

_Scope: OLE Object > Formula Object (Shift+Alt+E)_

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


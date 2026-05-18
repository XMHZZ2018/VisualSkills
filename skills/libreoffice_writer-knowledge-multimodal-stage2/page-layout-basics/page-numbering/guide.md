# Numbering Pages (LibreOffice Writer 7.3.7)

Page numbers in Writer are fields you insert into a header or footer — they update automatically on every page. To get started, place your cursor in a header or footer and go to **Insert > Page Number**, or use **Insert > Field > Page Number**. The number appears with a gray background on screen (that's just the field marker; it won't print).

See `fig01.png`.

To align the page number, click in the footer paragraph and use the alignment icons on the Formatting toolbar, or right-click and choose **Paragraph > Paragraph**, then pick an alignment on the **Alignment** tab.

By default, page numbers display as Arabic numerals (1, 2, 3…). If you want a different format — say, lowercase Roman numerals for a preface — right-click the text area, select **Page Style**, and on the **Page** tab find the **Page numbers** drop-down under *Layout Settings*. Pick the format you need and click **OK**. Keep in mind this changes every page that shares the same page style.

See `fig02.png`.

When you need to restart numbering — common after a title page or table of contents — you'll work with paragraph breaks. Place the cursor in the first paragraph of the page where numbering should restart. Open **Format > Paragraph** (or right-click and choose **Paragraph > Paragraph**), then go to the **Text Flow** tab. In the *Breaks* area, check **Insert**, set *Type* to **Page**, *Position* to **Before**, and tick **With page style** choosing the appropriate style (e.g., Default Page Style). Then check **Page number** and type the number you want to start from — typically 1. Click **OK**.

See `fig03.png`.

If you want the first page of your document to start at a number other than 1, the process is the same: insert a page number field in the header or footer, then apply the paragraph break settings above to the first paragraph, entering whatever starting number you like. Note that setting an even starting number will produce a blank page before it, since Writer follows the convention of odd numbers on right-hand pages.

You can also combine page numbers with other text in the header. For instance, type "Page " before the field, or add a Page Count field via **Insert > Field > Page Count** to get something like "Page 2 of 12." For chapter-based numbering (1-1, 1-2, 2-1…), first set up chapter numbering with **Tools > Chapter Numbering**, then insert a Chapter field from **Insert > Field > More Fields** on the **Document** tab, choosing **Chapter number** in the *Format* list, alongside your page number.

---

## UI Reference  —  Insert Menu

_Scope: Page Number…, Field > Page Number/Page Count_

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


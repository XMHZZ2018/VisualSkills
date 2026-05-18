# Inserting Page Breaks (LibreOffice Writer 7.3.7)

Writer automatically flows text from one page to the next as you add or remove content. Most of the time that's exactly what you want — but sometimes you need to take control and force a break at a specific spot. Here's how.

## Controlling automatic page flow

Before inserting manual breaks, know that Writer gives you a few paragraph-level options to influence how text flows. Open the Paragraph dialog by right-clicking and choosing **Paragraph > Paragraph**, then head to the **Text Flow** tab.

Turn on **Keep with next paragraph** to glue a heading to the paragraph that follows it, preventing an awkward split across pages. **Do not split paragraph** does what it says — keeps an entire paragraph on one page. You can also use **Orphan control** and **Widow control** here to avoid stray single lines at the top or bottom of a page.

See `fig01.png`.

If you want a paragraph to *always* start on a new page — chapter titles are the classic case — set that up in a paragraph style rather than inserting manual breaks everywhere. See the paragraph style's Text Flow options for details.

## Inserting a break without changing the page style

Sometimes you just need a simple page break — say, to push a heading to the top of the next page. Click where you want the new page to begin and go to **Insert > More Breaks > Manual Break**. In the dialog, **Page break** is preselected by default, and **Style** is set to [None]. Just click **OK** and you're done.

## Inserting a break and switching to a new page style

If the new page needs a different page style — switching from a First Page style to Left Page, for instance — use the same **Insert > More Breaks > Manual Break** path. This time, open the **Style** drop-down in the *Type* section and pick the page style you want for the next page.

A word of caution: don't try to change a page style for a single page without inserting a page break. Doing so can unexpectedly change the style of other pages in your document.

---

## UI Reference  —  Insert Menu

_Scope: Page Break (Ctrl+Return), More Breaks submenu_

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


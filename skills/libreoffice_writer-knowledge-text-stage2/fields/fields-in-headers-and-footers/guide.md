# Fields in Headers and Footers (LibreOffice Writer 7.3.7)

Headers and footers really come alive when you drop fields into them — things like page numbers, dates, chapter titles, and document info that update automatically. No more manually typing "Page 3 of 12" on every page.

You can insert fields into headers or footers the same way you would anywhere else in your document. To add a page number, document title, author, creation date and time, current date and time, or total page count, head to **Insert > Field > [item]** on the Menu bar, or open Document Properties (see the guide's page 437) and choose the field you need from there.

If you want to insert a cross-reference to a bookmark, heading, or other item, use **Insert > Cross-reference** or go to **Insert > Field > More Fields > Cross-references** tab.

Here's a handy trick for chapter-based documents: if you've been using Heading 1 for your chapter titles, you can insert a Document field that automatically pulls in the current chapter's title. As you move from chapter to chapter, the header or footer updates on its own. Writer calls these chapter titles "Chapter names" in the Fields dialog. If you've used outline numbering on your Heading 1, you can also choose whether to include the chapter number, the name, or both. Set this up via **Insert > Field > More Fields > Document**.

You can even cross-reference other heading levels by specifying a value in the Level box on the Document tab of the Fields dialog. Level 1 corresponds to Heading 1, Level 2 to Heading 2, and so on — so you can pull in sub-chapter headings just as easily.

One more thing worth knowing: fields like "Chapter" and "Statistics" are especially useful during writing because they stay current as your document grows. Drop them into a footer early on and forget about them — they'll keep themselves accurate right through to your final draft.

---

## UI Reference  —  Insert Menu

_Scope: Header and Footer submenu, Field submenu entries_

The Insert menu provides commands for adding content elements — breaks, images, tables, shapes, fields, footnotes, hyperlinks, and more — into the document.

The screenshot shows the fully expanded Insert drop-down menu from the LibreOffice Writer menu bar. It displays a single-column list of menu entries from top to bottom: Page Break, More Breaks, Image…, Chart…, Media, OLE Object, Shape, Section…, Text from File…, Text Box, Comment, Frame, Fontwork…, Caption… (grayed out), then a separator followed by Hyperlink…, Bookmark…, Cross-reference…, another separator, Special Character…, Formatting Mark, a checkbox-style Horizontal Line entry, Footnote and Endnote, Table of Contents and Index, Page Number…, Field, Header and Footer, Envelope…, and Signature Line…. Several entries have right-pointing arrows indicating submenus, and the menu appears against the document editing area with part of the formatting toolbar visible behind it.

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

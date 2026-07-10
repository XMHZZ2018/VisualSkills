# Bibliographies (LibreOffice Writer 7.3.7)

A bibliography is a list of references used in a document. Writer lets you store references in a central bibliographic database or directly within the document itself, then generate a formatted bibliography from them.

Writer ships with a shared bibliographic database that all your documents can pull from. Open it via **Tools > Bibliography Database** — you'll see a spreadsheet-like table at the top with all your records, and the fields for the selected record at the bottom. Each entry uses the Identifier (Short Name) field to link citations in your text, so give every entry a unique, meaningful short name.

The Bibliography Database main window is split into two panels. The upper panel shows a spreadsheet-style table with columns for Identifier, Type, Address, Annote, Author, Booktitle, Chapter, Edition, Editor, Howpublish, Institution, and Journal, listing all stored records (11 records are shown in this example). A toolbar above the table provides a Table selector (set to "biblio"), a Search Key field, filter icons, Column Arrangement, and Data Source buttons. The lower panel displays the detail fields for the currently selected record, arranged in a form layout with fields such as Short name, Type (a drop-down set to "Book"), Year, Author(s), Title, Publisher, Address, ISBN, Chapter, Page(s), Editor, Edition, Book title, Volume, Publication type, Organization, Institution, University, Type of report, Month, Journal, Number, and Series.

To add a new record, select **Data > Record** on the Bibliography Database menu bar (or click the **+** icon), then fill in the Short Name and whatever fields your citation style requires — typically author, title, publisher, and year. You only need about half a dozen fields filled in per entry; which ones matter depends on whether you're using APA, MLA, Chicago, Turabian, or AMA style. Modified entries save automatically when the cursor moves off the record.

When you're ready to cite a source in your document, place the cursor where the citation should appear and go to **Insert > Table of Contents and Index > Bibliography Entry**. Choose **Bibliography database** as the source, pick the entry from the **Short name** drop-down, and click **Insert**. You can keep the dialog open to insert several citations in a row, then hit **Close** when you're done. If you'd rather store a reference only in the current document, select **Document content** instead and click **New** to define the entry on the spot.

The Insert Bibliography Entry dialog has a "Bibliography Source" section at the top with two radio buttons: "Bibliography Database" (selected) and "Document Content". Below that is the "Entry" section containing a "Short name" drop-down (showing "LOD00" in this example), followed by read-only Author and Title fields displaying the corresponding data for the selected entry (here, "LibreOffice Documentation Team" and "Getting Started with LibreOffice 6.4"). Along the bottom of the dialog are five buttons: Help, New, Edit, Close, and Insert (highlighted in blue as the default action).

To edit an existing citation, right-click it and choose **Bibliography Entry**. You can quickly change the short name and click **Apply**, or click **Edit** to open the full Define Bibliography Entry dialog for deeper changes. Note that edits to document-stored citations stay local — they won't touch the database.

To generate the actual bibliography list, place your cursor where you want it and go to **Insert > Table of Contents and Index > Table of Contents, Index or Bibliography**, then set the **Type** to **Bibliography**. On the *Type* tab, choose whether citations display as the short name text or as numbered references. The *Entries* tab controls the structure line — which fields appear and in what order for each source type (book, article, journal, etc.). You can format individual elements with the **Character Style** selector, for instance making titles italic.

The "Table of Contents, Index or Bibliography" dialog is shown with five tabs across the top: Type (currently selected), Entries, Styles, Columns, and Background. In the "Type and Title" section, the Title field is set to "Bibliography" and the Type drop-down is also set to "Bibliography", with a "Protected against manual changes" checkbox enabled. The "Formatting of the Entries" section contains an unchecked "Number entries" checkbox and a "Brackets" drop-down set to square brackets. At the bottom, a "Sort" section provides a Language drop-down (set to "English (USA)") and a Key type drop-down (set to "Alphanumeric").

If you want numbered entries with brackets (like [1], [2]), you'll need to customize the Bibliography 1 paragraph style. In the Styles deck, right-click **Numbering 123**, create a new list style with bracket characters in the *Customize* tab's Before and After boxes, then apply that list style to Bibliography 1 via its **Outline & List** tab.

Once the bibliography is in your document, right-click anywhere inside it to **Update Index**, **Edit Index** (reopens the formatting dialog), or **Delete Index**. If Writer's built-in bibliography feels too limited, Zotero is a solid free alternative that integrates well with Writer.

---

## UI Reference  —  Insert Menu

_Scope: Table of Contents and Index > Bibliography Entry_

The Insert menu provides commands for adding content elements — breaks, images, tables, shapes, fields, footnotes, hyperlinks, and more — into the document.

The Insert menu is shown expanded from the Writer menu bar, displaying a vertical list of all available commands in order: Page Break, More Breaks, Image…, Chart…, Media, OLE Object, Shape, Section…, Text from File…, Text Box, Comment, Frame, Fontwork…, Caption… (grayed out), then a separator followed by Hyperlink…, Bookmark…, Cross-reference…, another separator, Special Character…, Formatting Mark, a separator, Horizontal Line, Footnote and Endnote, Table of Contents and Index, Page Number…, Field, Header and Footer, Envelope…, and Signature Line…. Several items have a right-pointing arrow indicating submenus.

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

# Alphabetic Indexes (LibreOffice Writer 7.3.7)

An alphabetic index is a list of keywords or phrases used throughout your document, paired with page numbers so readers can find things fast. Writer lets you mark entries manually, optionally use a concordance file, and then generate the index in a few clicks.

To add an index entry, place your cursor in the word you want indexed — or select an entire phrase — and go to **Insert > Table of Contents and Index > Index Entry**. The selected text appears in the **Entry** field; tweak it if you like, then hit **Insert**. You don't have to close the dialog between entries — just click somewhere else in your document, click the dialog again, adjust the entry, and press **Insert** to keep going.

The Insert Index Entry dialog has a **Selection** section at the top. It contains an **Index** dropdown (set to "Alphabetical Index"), an **Entry** text field showing the word to be indexed (e.g., "location"), editable **1st key** and **2nd key** dropdown fields for grouping entries, a **Main entry** checkbox, and an **Apply to all similar texts** checkbox with subordinate **Match case** and **Whole words only** options. At the bottom of the dialog are **Help**, **Close**, and **Insert** buttons.

You can organize entries into groups using the **1st key** field. For example, if your index should list "Calc," "Impress," and "Writer" as subentries under "LibreOffice," type "LibreOffice" in the **1st key** box for each of those entries. A **2nd key** adds another nesting level, though that degree of complexity is rarely needed. Check **Main entry** if one page is the primary reference for a term — you can later style that page number in bold to make it stand out.

If you have a lot of terms to index, a concordance file saves time. It's a plain text file where each line follows the format: `Search_term;Alternative_entry;1st_key;2nd_key;Match_case;Word_only`. Writer scans the document for each search term and creates the entries automatically. The trade-off is less precision — you may get unwanted hits for common words.

When you're ready to generate the index, click where you want it to appear and open **Insert > Table of Contents and Index > Table of Contents, Index or Bibliography**. On the **Type** tab, set the type to **Alphabetical Index**. Consider enabling **Combine identical entries with p or pp** for cleaner page ranges, and tick **Case sensitive** if capitalization matters. If you prepared a concordance file, select **Concordance file** and browse to it. Click **OK** and the index drops in.

The "Table of Contents, Index or Bibliography" dialog is shown with the **Type** tab selected (other tabs visible are Entries, Styles, Columns, and Background). The **Type and Title** section has a Title field set to "Alphabetical Index," a Type dropdown also set to "Alphabetical Index," and a "Protected against manual changes" checkbox (checked). Below that, a **Create Index or Table of Contents** section has a "For" dropdown set to "Entire document." The **Options** section presents checkboxes in two columns: on the left are "Combine identical entries" (checked), "Combine identical entries with p or pp," "Combine with -," and "Case sensitive"; on the right are "AutoCapitalize entries," "Keys as separate entries," and "Concordance file" with a grayed-out **File** button. At the bottom, a **Sort** section offers a Language dropdown (set to "English (USA)") and a Key type dropdown (set to "Alphanumeric").

To customize the look, right-click anywhere in the generated index and choose **Edit Index**. The **Entries** tab controls the structure of each line — the **E** icon is the entry text, **T** is a tab stop, and **#** is the page number. You can apply character styles to any element (handy for making page numbers a different size). Under the **Format** section, enable **Alphabetical delimiter** to get letter headings (A, B, C…) separating groups, or choose **Key separated by commas** to put subentries on one line.

The **Columns** tab lets you lay the index out in multiple columns — just set the number and optionally add a separator line between them. The **Styles** and **Background** tabs work the same way as for a table of contents.

Writer won't update the index automatically when you add or remove entries. Right-click the index and select **Update Index** whenever your content changes, or use the Navigator to find and update it. To remove the index entirely, right-click it and choose **Delete Index**.

---

## UI Reference  —  Insert Menu

_Scope: Table of Contents and Index > Index Entry_

The Insert menu provides commands for adding content elements — breaks, images, tables, shapes, fields, footnotes, hyperlinks, and more — into the document.

The Insert menu is shown expanded from the Writer menu bar. It lists items top-to-bottom in this order: Page Break, More Breaks, Image…, Chart…, Media, OLE Object, Shape, Section…, Text from File…, Text Box, Comment, Frame, Fontwork…, Caption… (grayed out), then a separator, followed by Hyperlink…, Bookmark…, Cross-reference…, then another separator, Special Character…, Formatting Mark, a separator, Horizontal Line, Footnote and Endnote, Table of Contents and Index, Page Number…, Field, Header and Footer, Envelope…, and Signature Line…. Several entries have a right-arrow indicating submenus.

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

# Adding Comments (LibreOffice Writer 7.3.7)

Comments let authors and reviewers exchange ideas, flag issues, or suggest changes without altering the document text itself. You can attach a comment to a selected block of text — even spanning multiple paragraphs — or drop one at a single insertion point.

To insert a comment, select the text you want to annotate (or just place your cursor where the comment should go), then choose **Insert > Comment** or press **Ctrl+Alt+C**. You can also click the **Insert Track Change Comment** button on the Track Changes toolbar. A dotted line connects your anchor point to a box on the right-hand side of the page where you type your note. A **Comments** button also appears to the right of the horizontal ruler; click it to toggle comment display on and off.

The document page shows three comment boxes stacked along the right margin, each connected to its anchor point in the body text by a dashed line. Two comments by "John Smith" have yellow backgrounds, while a comment by "Joe Soap" has a light-blue background, illustrating how different authors receive distinct colors. The top yellow comment reads "This comment is nested due to overlapping text selection," the blue comment reads "Comment on selected text," and the bottom yellow comment reads "A single point comment." Each box displays the author name and a timestamp (e.g., "Today, 20:54"), with a small drop-down arrow button in the lower-right corner for the context menu. At the top-right of the page, a "Comments" button appears beside the horizontal ruler.

Writer automatically stamps each comment with your name and a timestamp. If the name shown isn't right, head to **Tools > Options > LibreOffice > User Data** and update the Author field.

When you're done typing, just click somewhere else on the page — the comment is saved in place. If more than one person edits the document, each author's comments get a different background color so you can tell them apart at a glance. When an author selects text that overlaps another author's comments, the replies are nested under the first author's notes.

Right-click any comment to open a context menu where you can delete that single comment, all comments from the same author, or every comment in the document. From the same menu, choose **Format all comments** to apply basic formatting — font type, size, and alignment — to the comment text.

Once a comment has been addressed, you can mark it as resolved or unresolved via the comment's context menu. The word "Resolved" appears beneath the date, and you can show or hide all resolved comments with **View > Resolved Comments**.

To jump between comments, open the Navigator with **F5**, expand the **Comments** section, and double-click an entry to land at its anchor in the document. Alternatively, select **Comment** in the **Navigate By** box at the top of the Navigator and use the Up and Down arrows. The keyboard works too: **Ctrl+Alt+Page Down** moves to the next comment, **Ctrl+Alt+Page Up** goes to the previous one.

When it's time to print, you have options. Go to **File > Print > LibreOffice Writer** tab and look at the **Comments** drop-down list. You can print comments only, place them at end of document, at end of page, or in the margins — whatever suits your workflow.

The Print dialog's "LibreOffice Writer" tab is shown, with a "Contents" section containing checkboxes for Page background, Images and other graphic objects, Hidden text, Text placeholders, and Form controls. Below these checkboxes is a "Comments" drop-down list, which is expanded to reveal five options: "None (document only)" (currently selected and highlighted), "Comments only," "Place at end of document," "Place at end of page," and "Place in margins." Partially visible below are "Color" and "Pages" sections with additional print settings.

---

## UI Reference  —  Insert Menu

_Scope: Comment (Ctrl+Alt+C)_

The Insert menu provides commands for adding content elements — breaks, images, tables, shapes, fields, footnotes, hyperlinks, and more — into the document.

The Insert drop-down menu is shown open from the LibreOffice Writer menu bar, displaying a single-column list of commands in top-to-bottom order: Page Break, More Breaks, Image…, Chart…, Media, OLE Object, Shape, Section…, Text from File…, Text Box, Comment, Frame, Fontwork…, Caption… (grayed out), Hyperlink…, Bookmark…, Cross-reference…, Special Character…, Formatting Mark, Horizontal Line, Footnote and Endnote, Table of Contents and Index, Page Number…, Field, Header and Footer, Envelope…, and Signature Line…. The "Comment" entry appears roughly in the middle of the list, and some items such as More Breaks, Media, OLE Object, Shape, Frame, Formatting Mark, Footnote and Endnote, Table of Contents and Index, Field, and Header and Footer have sub-menu arrows indicating additional options.

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

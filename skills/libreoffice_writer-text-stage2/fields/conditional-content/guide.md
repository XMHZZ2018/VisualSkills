# Developing Conditional Content (LibreOffice Writer 7.3.7)

Conditional content lets you include or exclude text and graphics from a document based on a condition you define. A classic use case: a reminder letter where the first and second notices say "Reminder Notice" in the subject line, but the third says "Final Notice" with a different closing paragraph. Another common scenario is a product manual that ships in both Pro and Lite editions — one file, two outputs.

Writer gives you four main tools for this: **conditional text**, **hidden text**, **hidden paragraphs**, and **hidden sections**. Conditional text swaps between two alternatives (show one phrase if true, another if false). Hidden text is simpler — it's either visible or invisible. Hidden paragraphs let you hide an entire paragraph, and hidden sections can hide multiple paragraphs, headings, or even graphics. Pick whichever fits the scope of what you need to show or hide.

Before you set up any conditional content, you need a variable to test against. Open **Insert > Fields > More Fields**, go to the **Variables** tab, and select **Set variable** in the Type list. Choose **Text** as the format, give it a name (say, `ProLite`), set a value like `Lite`, tick **Invisible**, then click **Insert**. A tiny gray mark appears in your document where the field lives.

The Fields dialog is shown with the **Variables** tab selected. The left Type list has "Set variable" highlighted, and the right Format list has "Text" highlighted at the top, followed by numeric format options such as General, -1235, and -1234.57. At the bottom of the dialog, the Name field contains "ProLite" and the Value field contains "Lite." The **Invisible** checkbox in the lower-right area is checked. Buttons at the bottom include Help, Close, and Insert.

To insert conditional text, switch to the **Functions** tab of the same Fields dialog and select **Conditional text** in the Type list. In the **Condition** box, type something like `ProLite EQ "Lite"`. Fill in the **Then** box with the text to display when true and the **Else** box with the alternative, then click **Insert**. Note that conditions are case-sensitive and string values need quotation marks.

The Fields dialog is shown with the **Functions** tab active. In the left Type list, "Conditional text" is highlighted, with other entries including Input list, Input field, Execute macro, Placeholder, Combine characters, Hidden text, and Hidden Paragraph visible below it. On the right side, the Condition field contains `ProLite EQ "Lite"`, the Then field contains "Great Product Lite", and the Else field contains "Great Product Pro."

For hidden text, choose **Hidden text** on that same **Functions** tab. Enter your condition and the text that should be hidden when the condition is true, then insert. To reveal all hidden text while editing, go to **Tools > Options > LibreOffice Writer > View** and enable **Display fields: Hidden text**.

Hidden paragraphs work similarly — click in the paragraph you want to conditionally hide, select **Hidden Paragraph** in the Type list, and enter the condition. To see hidden paragraphs again, toggle **View > Field Hidden Paragraphs** on the menu bar, or enable the option under **Tools > Options > LibreOffice Writer > View**.

Hidden sections are the most powerful option since they can wrap multiple paragraphs and graphics. Select the content you want, then choose **Insert > Section**. On the Section tab, tick **Hide** and type your condition in the **With Condition** box. Give the section a name so you can find it later. To edit a hidden section, open **Format > Sections**, deselect **Hide**, and click **OK**.

The Insert Section dialog is displayed with the **Section** tab selected. Five tabs run across the top: Section, Columns, Indents, Area, and Footnotes/Endnotes. On the left, the New Section name field shows "Extra features." The right side contains a Link group (with unchecked Link and DDE checkboxes, a File name field, and a Browse button), a Write Protection group (with an unchecked Protect checkbox and a grayed-out "With password" option), a **Hide** group where the Hide checkbox is checked and the "With Condition" field contains `ProLite EQ "Lite"`, and a Properties group with an unchecked "Editable in read-only document" option. Buttons at the bottom are Help, Reset, Cancel, and Insert.

When you're ready to switch editions — say, from Lite to Pro — just find the variable field, right-click it, choose **Fields** from the context menu, and change its value. If automatic updating is on (**Tools > Options > LibreOffice Writer > General**, check **Fields** under **Automatically Update**), every conditional field, hidden text, and hidden section tied to that variable updates instantly.

---

## UI Reference  —  Insert Menu

_Scope: Field > More Fields… (Ctrl+F2) for conditional/hidden fields_

The Insert menu provides commands for adding content elements — breaks, images, tables, shapes, fields, footnotes, hyperlinks, and more — into the document.

The Insert menu is shown expanded from the Writer menu bar. It lists entries from top to bottom: Page Break, More Breaks, Image…, Chart…, Media, OLE Object, Shape, Section…, Text from File…, Text Box, Comment, Frame, Fontwork…, Caption… (grayed out), then a separator followed by Hyperlink…, Bookmark…, Cross-reference…, another separator, Special Character…, Formatting Mark, Horizontal Line, then Footnote and Endnote, Table of Contents and Index, Page Number…, Field, Header and Footer, Envelope…, and Signature Line… at the bottom.

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

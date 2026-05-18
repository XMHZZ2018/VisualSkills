# Creating Headers and Footers (LibreOffice Writer 7.3.7)

Headers and footers are portions of a document that appear at the top and bottom of every page. They typically hold page numbers, titles, or other recurring info. In Writer, headers and footers are tied to page styles — so all pages sharing the same style get the same header and footer, though the content can vary (for instance, a first page of a chapter might differ from the rest).

The quickest way to insert a header is to click above the top of the text area so the Header marker appears, then click the **+** button. For a footer, do the same at the bottom of the text area. That's it — you're typing in a header or footer.

The top of a Writer page is shown with the cursor hovering above the text area, causing a "Header (Default Page Style)" marker to appear in the upper-right corner of the page along with a **+** button. Below the dashed header boundary line, the document body begins with a heading titled "Introduction" and body text about page styles.

You can also go through the menu: **Insert > Header and Footer > Header > [Page Style]**. The submenu lists every page style in your document, plus an **All** entry that activates headers on every page regardless of style. For footers, it's **Insert > Header and Footer > Footer > [Page Style]**. If you just want headers or footers on Default Page Style pages, select that entry specifically.

A Writer page is shown with a header already enabled and active. The header area at the top of the page contains the bold, centered text "Page Header" on a light blue background, separated from the body text below. The body text starts with the bold title "The Old Salt" followed by lines of verse. The horizontal ruler is visible along the top of the editing area.

Once your header or footer is in place, just type in it like any paragraph. You can format the text using the same tools you'd use in the body — fonts, alignment, tabs, and so on. Writer even provides dedicated paragraph styles for headers and footers that you can modify through **Format > Styles**.

To fine-tune the layout — margins, spacing, and height — open the page style dialog. You can get there by clicking **Format > Page Style**, or by right-clicking the page and choosing **Page Style**, or by clicking in the header/footer area and selecting **Format Header** or **Format Footer** from the dropdown arrow. On the **Header** or **Footer** tab of the Page Style dialog, adjust margins, spacing, and height as needed. Check or uncheck options like **Same content on left and right pages** or **Same content on first page** depending on your layout.

The Page Style dialog is shown with the "Footer" tab selected. The dialog title bar reads "Page Style: Default Style" and tabs along the top include Organizer, Page, Area, Transparency, Header, Footer, Borders, Columns, and Footnote. On the Footer tab, the "Footer on" checkbox is checked to enable the footer. Below that are checkboxes for "Same content on left and right pages" (unchecked) and "Same content on first page" (checked). Numeric spin boxes set Left margin to 0.00 cm, Right margin to 0.00 cm, Spacing to 0.50 cm, and Height to 0.50 cm, with an "AutoFit height" checkbox checked. A small page preview appears on the right side, and a **More...** button at the bottom opens additional border and background options.

If you want borders or a background color behind your header or footer, click the **More...** button on that same tab to open the **Border/Background** dialog, where you can set line styles, colors, padding, and even a background image.

---

## UI Reference  —  Key Formatting Dialogs

_Scope: Page Style dialog Header and Footer tabs_

These multi-tab dialogs provide detailed control over character formatting, paragraph layout, page styles, and search/replace.

## Find and Replace (Ctrl+H)

The Find and Replace dialog is shown with the title "Find and Replace" in the upper-right corner. It contains a "Find:" text field at the top with an empty input box, followed by "Match case" and "Whole words only" checkboxes. Below that is a "Replace:" text field. Three buttons appear in a row: "Find All", "Find Previous", and "Find Next". An expanded "Other options" section shows checkboxes for "Current selection only", "Comments", "Regular expressions", as well as partially visible options for "Replace" (backwards) and "Paragraph Styles" on the right side.

Opened via Edit > Find and Replace… or Ctrl+H.

- **Find** text field (with history dropdown)
- **Match case** / **Whole words only** checkboxes
- **Replace** text field (with history dropdown)
- **Buttons:** Find All, Find Previous, Find Next, Replace, Replace All
- **Other options** (collapsible): Current selection only, Comments, Regular expressions, Similarity search (with Similarities… button), Diacritic-sensitive, Replace backwards, Paragraph Styles
- **Attributes…** / **Format…** / **No Format** buttons for format-aware search

## Character Dialog (Format > Character…)

The Character dialog is shown with the "Font" tab active. Visible tabs along the top include Font, Font Effects, Position, and Hyperlink. On the Font tab, the Family field shows "Liberation Serif" with a dropdown list displaying available fonts including Linux Biolinum Keyboard O, Linux Biolinum O, Linux Libertine Display O, Linux Libertine Initials O, Linux Libertine Mono O, and Linux Libertine O. Below the font list, the Style field is set to "Regular", Size to "12 pt", and Language to "English (USA)". A partial preview line is visible at the bottom.

**Tabs:** Font, Font Effects, Position, Hyperlink, Highlighting, Borders

- **Font tab:** Family, Style (Regular/Bold/Italic/Bold Italic), Size, Language, Features… button, font preview.
- **Font Effects tab:** Font Color + Transparency, Overlining style+color, Strikethrough style, Underlining style+color+Individual words, Case dropdown, Relief, Hidden/Outline/Shadow checkboxes.
- **Position tab:** Normal/Superscript/Subscript radio + raise/lower %, Rotation (0°/90°/270°) + Scale width + Fit to line, Character spacing + Pair kerning.

## Paragraph Dialog (Format > Paragraph…)

The Paragraph dialog is shown with the "Indents & Spacing" tab selected. Tabs visible along the top include Indents & Spacing, Alignment, Outline & List, Tabs, Drop Caps, and Borders. The Indent section contains spin boxes for "Before text" (0.00"), "After text" (0.00"), and "First line" (0.00") with increment/decrement buttons, plus an "Automatic" checkbox. The Spacing section has "Above paragraph" (0.00") and "Below paragraph" (0.00") spin boxes and a "Do not add space between paragraphs of the same style" checkbox. The Line Spacing section shows a dropdown currently set to "Single".

**Tabs:** Indents & Spacing, Alignment, Text Flow, Outline & List, Tabs, Drop Caps, Borders, Area, Transparency

- **Indents & Spacing:** Before/After text indent, First line indent, Automatic; Spacing above/below paragraph; Line Spacing dropdown (Single/1.15/1.5/Double/Proportional/At least/Leading/Fixed); Activate page line-spacing.
- **Alignment:** Left/Center/Right/Justified radio; Last line dropdown; Expand single word; Text-to-text alignment; Text direction.
- **Text Flow:** Hyphenation settings, page/column breaks, orphan/widow control.
- **Tabs:** Tab stop position, type (Left/Right/Center/Decimal), fill character.

## Page Style Dialog (Format > Page Style…, Shift+Alt+P)

The Page Style dialog is shown with the "Organizer" tab selected. The dialog title bar reads "Page Style: Default Page Style" and visible tabs include Organizer, Page, Area, Transparency, Header, and Footer (with additional tabs cut off to the right). The Organizer tab displays a Style section with fields for Name ("Default Page Style"), Next style ("Default Page Style"), Inherit from (empty), and Category ("Custom Styles"). Below that, a "Contains" section summarizes the style properties, showing dimensions of 11.69 inch, top and bottom margins of 0.79 inch, text direction left-to-right, and no page line-spacing.

**Tabs:** Organizer, Page, Area, Transparency, Header, Footer, Borders, Columns, Footnote

- **Organizer:** Style name, Next style dropdown, Inherit from, Category, Contains description.
- **Page:** Paper format (size, width, height, portrait/landscape, paper tray), Margins (left/right/top/bottom/gutter), Layout settings (page layout, page numbers, gutter position).
- **Header/Footer:** Enable checkbox, margins, spacing, same content on left/right pages.
- **Columns:** Column count, width/spacing, separator line options.

---

## UI Reference  —  Insert Menu

_Scope: Header and Footer submenu: enable/disable per page style_

The Insert menu provides commands for adding content elements — breaks, images, tables, shapes, fields, footnotes, hyperlinks, and more — into the document.

The Insert menu is shown fully expanded as a dropdown from the menu bar. It lists the following entries from top to bottom: Page Break, More Breaks, Image…, Chart…, Media, OLE Object, Shape, Section…, Text from File…, Text Box, Comment, Frame, Fontwork…, Caption… (grayed out), Hyperlink…, Bookmark…, Cross-reference…, Special Character…, Formatting Mark, Horizontal Line, Footnote and Endnote, Table of Contents and Index, Page Number…, Field, Header and Footer, Envelope…, and Signature Line…. Some entries have submenu arrows indicating nested menus, and a few items like Hyperlink and Horizontal Line show small icons to their left.

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

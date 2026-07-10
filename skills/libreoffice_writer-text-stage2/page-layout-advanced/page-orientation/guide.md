# Changing Page Orientation Within a Document (LibreOffice Writer 7.3.7)

A document can contain pages in more than one orientation — a common scenario is slipping a landscape page into the middle of a portrait document for a wide table or chart. The trick is that orientation lives in a *page style*, so you need a Landscape page style and then tell Writer where to switch to it and back.

## Setting up a Landscape page style

Open the Styles deck in the Sidebar, right-click **Landscape** in the list of page styles, and choose **Modify**. On the *Organizer* tab of the Page Style dialog, make sure **Next Style** is set to **Landscape** — this lets you have several landscape pages in a row without Writer flipping back to portrait after the first one.

The Page Style dialog is shown with the Organizer tab selected. The dialog title reads "Page Style: Landscape" and displays four fields under a "Style" heading: **Name** is set to "Landscape," **Next style** is set to "Landscape" (highlighted in blue), **Inherit from** is blank, and **Category** reads "Custom Styles." An "Edit Style" button appears beside the Next style and Inherit from dropdowns. Tabs for Page, Area, Transparency, Header, Footer, Borders, Columns, and Footnote run across the top of the dialog.

Now switch to the *Page* tab and confirm the **Orientation** is set to **Landscape**. While you're here, adjust the margins so they correspond to the portrait page's margins, just rotated: the portrait top margin becomes the landscape left margin, and so on. Click **OK** to save.

The Page Style: Landscape dialog is now showing the Page tab. Under **Paper Format**, the Format dropdown is set to "A4" with Width 29.70 cm and Height 21.00 cm, and the **Orientation** radio buttons show "Landscape" selected. A small page preview on the right depicts a horizontal rectangle. Below, the **Margins** section has Left, Right, Top, and Bottom all set to 2.00 cm. On the right side, **Layout Settings** shows Page layout set to "Right and left," Page numbers to "1, 2, 3, …," a Register-true checkbox (unchecked), and a Paper tray dropdown set to "[From printer settings]."

## Applying the landscape style in your document

Place your cursor in the paragraph or table at the start of the page you want in landscape. Right-click and choose **Paragraph > Paragraph** or **Table Properties** from the context menu. Go to the *Text Flow* tab, select **Insert** (or **Break** for a table) and tick **With Page Style**, then set the page style to **Landscape**. Click **OK** and that page — and everything after it — will be landscape.

To switch back to portrait, position the cursor in the paragraph where portrait should resume. Open the same **Text Flow** settings again, insert a break **With Page Style**, and this time pick the portrait page style that was in use before the landscape section. Click **OK**.

The Paragraph dialog is displayed with the Text Flow tab active. On the left side is the **Hyphenation** section with an "Automatically" checkbox (unchecked), a "Don't hyphenate words in CAPS" checkbox, and spin boxes for "Characters at line end" (2), "Characters at line begin" (2), and "Maximum number of consecutive hyphens" (0). On the right side is the **Breaks** section: the **Insert** checkbox is ticked, **Type** is set to "Page," **Position** is set to "Before," the **With page style** checkbox is ticked with the dropdown set to "Landscape," and a **Page number** spin box is set to 1 (unchecked). Other tabs visible across the top include Indents & Spacing, Alignment, Outline & List, Tabs, Drop Caps, Borders, Area, and Transparency.

## Portrait headers and footers on landscape pages

If your landscape pages sit between portrait pages and the document will be printed, you probably want headers and footers aligned with the portrait pages — rotated 90° on the landscape sheet so everything looks consistent when bound. Writer can't do this natively through the page style, but you can fake it with frames: copy the header or footer text from a portrait page, paste it into the landscape page, rotate it via **Format > Character** on the *Position* tab (set **Rotation / Scaling** to **270 degrees**), then wrap it in a frame (**Insert > Frame > Frame**) sized and positioned to match the portrait page's header or footer area.

---

## UI Reference  —  Key Formatting Dialogs

_Scope: Page Style dialog Page tab: orientation setting_

These multi-tab dialogs provide detailed control over character formatting, paragraph layout, page styles, and search/replace.

## Find and Replace (Ctrl+H)

The Find and Replace dialog is a compact floating window titled "Find and Replace." At the top is a **Find** text field (empty, with a blue-highlighted border), followed by **Match case** and **Whole words only** checkboxes. Below is a **Replace** text field. Three buttons appear in a row: **Find All**, **Find Previous**, and **Find Next**. An expanded **Other options** section shows checkboxes for "Current selection only," "Comments," "Regular expressions," a partially visible "Replace…" checkbox on the right, and a partially visible "Parag…" (Paragraph Styles) checkbox.

Opened via Edit > Find and Replace… or Ctrl+H.

- **Find** text field (with history dropdown)
- **Match case** / **Whole words only** checkboxes
- **Replace** text field (with history dropdown)
- **Buttons:** Find All, Find Previous, Find Next, Replace, Replace All
- **Other options** (collapsible): Current selection only, Comments, Regular expressions, Similarity search (with Similarities… button), Diacritic-sensitive, Replace backwards, Paragraph Styles
- **Attributes…** / **Format…** / **No Format** buttons for format-aware search

## Character Dialog (Format > Character…)

The Character dialog is shown with the **Font** tab selected. Visible tabs across the top are Font, Font Effects, Position, and Hyperlink. The Font tab displays a **Family** field set to "Liberation Serif" with a dropdown list showing available fonts (Liberation Serif is highlighted in blue, followed by Linux Biolinum Keyboard O, Linux Biolinum O, Linux Libertine Display O, and others). Below the family list are **Style** set to "Regular," **Size** set to "12 pt," and **Language** set to "English (USA)." A partial font preview is visible at the bottom of the dialog.

**Tabs:** Font, Font Effects, Position, Hyperlink, Highlighting, Borders

- **Font tab:** Family, Style (Regular/Bold/Italic/Bold Italic), Size, Language, Features… button, font preview.
- **Font Effects tab:** Font Color + Transparency, Overlining style+color, Strikethrough style, Underlining style+color+Individual words, Case dropdown, Relief, Hidden/Outline/Shadow checkboxes.
- **Position tab:** Normal/Superscript/Subscript radio + raise/lower %, Rotation (0°/90°/270°) + Scale width + Fit to line, Character spacing + Pair kerning.

## Paragraph Dialog (Format > Paragraph…)

The Paragraph dialog is displayed with the **Indents & Spacing** tab active. Visible tabs across the top include Outline & List, Tabs, Drop Caps, Borders, and a second row showing Indents & Spacing and Alignment. Under **Indent**, there are fields for "Before text" (0.00″), "After text" (0.00″), and "First line" (0.00″), each with minus and plus buttons, and an "Automatic" checkbox. Under **Spacing**, "Above paragraph" and "Below paragraph" are both 0.00″ with plus/minus buttons, and a "Do not add space between paragraphs of the same style" checkbox. Under **Line Spacing**, a dropdown is set to "Single."

**Tabs:** Indents & Spacing, Alignment, Text Flow, Outline & List, Tabs, Drop Caps, Borders, Area, Transparency

- **Indents & Spacing:** Before/After text indent, First line indent, Automatic; Spacing above/below paragraph; Line Spacing dropdown (Single/1.15/1.5/Double/Proportional/At least/Leading/Fixed); Activate page line-spacing.
- **Alignment:** Left/Center/Right/Justified radio; Last line dropdown; Expand single word; Text-to-text alignment; Text direction.
- **Text Flow:** Hyphenation settings, page/column breaks, orphan/widow control.
- **Tabs:** Tab stop position, type (Left/Right/Center/Decimal), fill character.

## Page Style Dialog (Format > Page Style…, Shift+Alt+P)

The Page Style dialog is shown with the **Organizer** tab selected, titled "Page Style: Default Page Style." Under the **Style** heading, the **Name** field reads "Default Page Style," **Next style** is set to "Default Page Style," **Inherit from** is blank, and **Category** is "Custom Styles." Below is a **Contains** section summarizing the style properties: "11.69 inch + From top 0.79 inch, From bottom 0.79 inch + Text direction left-to-right (ho… Default Page Style + Not page line-spacing." Tabs visible across the top include Organizer, Page, Area, Transparency, Header, Footer, and partially visible Borders tab.

**Tabs:** Organizer, Page, Area, Transparency, Header, Footer, Borders, Columns, Footnote

- **Organizer:** Style name, Next style dropdown, Inherit from, Category, Contains description.
- **Page:** Paper format (size, width, height, portrait/landscape, paper tray), Margins (left/right/top/bottom/gutter), Layout settings (page layout, page numbers, gutter position).
- **Header/Footer:** Enable checkbox, margins, spacing, same content on left/right pages.
- **Columns:** Column count, width/spacing, separator line options.

# Changing Page Orientation Within a Document (LibreOffice Writer 7.3.7)

A document can contain pages in more than one orientation — a common scenario is slipping a landscape page into the middle of a portrait document for a wide table or chart. The trick is that orientation lives in a *page style*, so you need a Landscape page style and then tell Writer where to switch to it and back.

## Setting up a Landscape page style

Open the Styles deck in the Sidebar, right-click **Landscape** in the list of page styles, and choose **Modify**. On the *Organizer* tab of the Page Style dialog, make sure **Next Style** is set to **Landscape** — this lets you have several landscape pages in a row without Writer flipping back to portrait after the first one.

See `fig01.png`.

Now switch to the *Page* tab and confirm the **Orientation** is set to **Landscape**. While you're here, adjust the margins so they correspond to the portrait page's margins, just rotated: the portrait top margin becomes the landscape left margin, and so on. Click **OK** to save.

See `fig02.png`.

## Applying the landscape style in your document

Place your cursor in the paragraph or table at the start of the page you want in landscape. Right-click and choose **Paragraph > Paragraph** or **Table Properties** from the context menu. Go to the *Text Flow* tab, select **Insert** (or **Break** for a table) and tick **With Page Style**, then set the page style to **Landscape**. Click **OK** and that page — and everything after it — will be landscape.

To switch back to portrait, position the cursor in the paragraph where portrait should resume. Open the same **Text Flow** settings again, insert a break **With Page Style**, and this time pick the portrait page style that was in use before the landscape section. Click **OK**.

See `fig03.png`.

## Portrait headers and footers on landscape pages

If your landscape pages sit between portrait pages and the document will be printed, you probably want headers and footers aligned with the portrait pages — rotated 90° on the landscape sheet so everything looks consistent when bound. Writer can't do this natively through the page style, but you can fake it with frames: copy the header or footer text from a portrait page, paste it into the landscape page, rotate it via **Format > Character** on the *Position* tab (set **Rotation / Scaling** to **270 degrees**), then wrap it in a frame (**Insert > Frame > Frame**) sized and positioned to match the portrait page's header or footer area.

---

## UI Reference  —  Key Formatting Dialogs

_Scope: Page Style dialog Page tab orientation (Portrait/Landscape) setting_

These multi-tab dialogs provide detailed control over character formatting, paragraph layout, page styles, and search/replace.

## Find and Replace (Ctrl+H)

(see screenshot `ui-find-replace-dialog.png`)

Opened via Edit > Find and Replace… or Ctrl+H.

- **Find** text field (with history dropdown)
- **Match case** / **Whole words only** checkboxes
- **Replace** text field (with history dropdown)
- **Buttons:** Find All, Find Previous, Find Next, Replace, Replace All
- **Other options** (collapsible): Current selection only, Comments, Regular expressions, Similarity search (with Similarities… button), Diacritic-sensitive, Replace backwards, Paragraph Styles
- **Attributes…** / **Format…** / **No Format** buttons for format-aware search

## Character Dialog (Format > Character…)

(see screenshot `ui-character-dialog.png`)

**Tabs:** Font, Font Effects, Position, Hyperlink, Highlighting, Borders

- **Font tab:** Family, Style (Regular/Bold/Italic/Bold Italic), Size, Language, Features… button, font preview.
- **Font Effects tab:** Font Color + Transparency, Overlining style+color, Strikethrough style, Underlining style+color+Individual words, Case dropdown, Relief, Hidden/Outline/Shadow checkboxes.
- **Position tab:** Normal/Superscript/Subscript radio + raise/lower %, Rotation (0°/90°/270°) + Scale width + Fit to line, Character spacing + Pair kerning.

## Paragraph Dialog (Format > Paragraph…)

(see screenshot `ui-paragraph-dialog.png`)

**Tabs:** Indents & Spacing, Alignment, Text Flow, Outline & List, Tabs, Drop Caps, Borders, Area, Transparency

- **Indents & Spacing:** Before/After text indent, First line indent, Automatic; Spacing above/below paragraph; Line Spacing dropdown (Single/1.15/1.5/Double/Proportional/At least/Leading/Fixed); Activate page line-spacing.
- **Alignment:** Left/Center/Right/Justified radio; Last line dropdown; Expand single word; Text-to-text alignment; Text direction.
- **Text Flow:** Hyphenation settings, page/column breaks, orphan/widow control.
- **Tabs:** Tab stop position, type (Left/Right/Center/Decimal), fill character.

## Page Style Dialog (Format > Page Style…, Shift+Alt+P)

(see screenshot `ui-page-style-dialog.png`)

**Tabs:** Organizer, Page, Area, Transparency, Header, Footer, Borders, Columns, Footnote

- **Organizer:** Style name, Next style dropdown, Inherit from, Category, Contains description.
- **Page:** Paper format (size, width, height, portrait/landscape, paper tray), Margins (left/right/top/bottom/gutter), Layout settings (page layout, page numbers, gutter position).
- **Header/Footer:** Enable checkbox, margins, spacing, same content on left/right pages.
- **Columns:** Column count, width/spacing, separator line options.


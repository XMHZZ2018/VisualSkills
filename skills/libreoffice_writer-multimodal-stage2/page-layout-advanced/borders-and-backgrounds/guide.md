# Defining Borders and Backgrounds (LibreOffice Writer 7.3.7)

Borders and backgrounds can be applied to many elements in Writer — paragraphs, pages, frames, sections, and even character and paragraph styles. The dialogs are similar across all of these, so once you learn one, the rest feel familiar. We'll use a frame as the example here, but the same ideas apply everywhere.

Page backgrounds can fill the entire sheet or just the area inside the margins (controlled via page styles). Page borders, meanwhile, surround only the area within the margins, including any header or footer. Tables of data also support borders and backgrounds, though background choices there are limited to Color or Bitmap.

**Adding a border.** Select your frame (or paragraph, page style, etc.), right-click, and choose **Properties**. Head over to the **Borders** tab. You'll see four main sections: *Line Arrangement* lets you pick a preset or click individual edges in the User-defined area to format each line separately. *Line* controls the style, width, and color. *Padding* sets the space between the border and the content — check **Synchronize** if you want equal spacing on all sides. Finally, *Shadow Style* adds a drop shadow with adjustable position, distance, and color.

See `fig01.png`.

**Adding a background color.** Still in **Properties**, switch to the **Area** tab and choose **Color**. Pick a color from the grid or define a custom one, then click **OK**. For selected text or characters, use **Character > Character** instead — there the background is called "highlighting" and only offers Color or None.

See `fig02.png`.

**Using a bitmap image as a background.** On the same **Area** tab, choose **Bitmap**. You can select from the built-in thumbnails or click **Add/Import** to bring in your own image. Under *Options*, set the style (custom position, tiled, or stretched), adjust the size (check *Scale* to stretch or shrink to fit), and pick the position. Hit **OK** when it looks right in the preview.

**Gradients, patterns, and hatching** are also available on the **Area** tab — just choose the corresponding button. Each type shows its own set of options and a live preview. For more detailed gradient and pattern design, the *Draw Guide* has you covered.

**Removing a background** is straightforward: go to the **Area** tab and select **None** at the top.

**Adjusting transparency.** If you want a watermark effect — say, a faded company logo or a "Draft" stamp behind your text — switch to the **Transparency** tab. You can set a flat transparency percentage or use a gradient transparency with types like Linear, Axial, Radial, and others for more creative fading effects.

See `fig03.png`.

---

## UI Reference  —  Key Formatting Dialogs

_Scope: Page Style dialog Area and Transparency tabs; Paragraph dialog Borders tab_

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


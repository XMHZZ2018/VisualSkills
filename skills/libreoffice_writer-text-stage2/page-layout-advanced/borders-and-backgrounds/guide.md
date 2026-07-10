# Defining Borders and Backgrounds (LibreOffice Writer 7.3.7)

Borders and backgrounds can be applied to many elements in Writer — paragraphs, pages, frames, sections, and even character and paragraph styles. The dialogs are similar across all of these, so once you learn one, the rest feel familiar. We'll use a frame as the example here, but the same ideas apply everywhere.

Page backgrounds can fill the entire sheet or just the area inside the margins (controlled via page styles). Page borders, meanwhile, surround only the area within the margins, including any header or footer. Tables of data also support borders and backgrounds, though background choices there are limited to Color or Bitmap.

**Adding a border.** Select your frame (or paragraph, page style, etc.), right-click, and choose **Properties**. Head over to the **Borders** tab. You'll see four main sections: *Line Arrangement* lets you pick a preset or click individual edges in the User-defined area to format each line separately. *Line* controls the style, width, and color. *Padding* sets the space between the border and the content — check **Synchronize** if you want equal spacing on all sides. Finally, *Shadow Style* adds a drop shadow with adjustable position, distance, and color.

The Frame dialog is shown with the Borders tab selected. On the left, the Line Arrangement section displays five preset border icons and a User-defined preview area showing a gray rectangle with clickable edges. Below that, the Line section has dropdowns for Style (set to a solid line), Color (Black), and a Width spinner (0.05 pt). On the right, the Padding section provides Left, Right, Top, and Bottom spinners (all 0.00 cm) with a checked Synchronize checkbox. Below the padding, the Shadow Style section offers five position icons, a Color dropdown (Black), and a Distance spinner (0.10 cm).

**Adding a background color.** Still in **Properties**, switch to the **Area** tab and choose **Color**. Pick a color from the grid or define a custom one, then click **OK**. For selected text or characters, use **Character > Character** instead — there the background is called "highlighting" and only offers Color or None.

The Frame dialog is shown with the Area tab selected and the Color button active. Along the top of the tab are buttons for None, Color, Gradient, Bitmap, Pattern, and Hatch. The left side displays a Colors section with a Palette dropdown set to "standard" and a grid of color swatches, plus Recent Colors and a Custom Palette area with Add and Delete buttons. The center shows the Active color preview (black) with R, G, B, and Hex fields, and the right shows the New color preview (a medium blue) with editable R (114), G (159), B (207), and Hex (729fcf) fields, along with a Pick button for the color picker.

**Using a bitmap image as a background.** On the same **Area** tab, choose **Bitmap**. You can select from the built-in thumbnails or click **Add/Import** to bring in your own image. Under *Options*, set the style (custom position, tiled, or stretched), adjust the size (check *Scale* to stretch or shrink to fit), and pick the position. Hit **OK** when it looks right in the preview.

**Gradients, patterns, and hatching** are also available on the **Area** tab — just choose the corresponding button. Each type shows its own set of options and a live preview. For more detailed gradient and pattern design, the *Draw Guide* has you covered.

**Removing a background** is straightforward: go to the **Area** tab and select **None** at the top.

**Adjusting transparency.** If you want a watermark effect — say, a faded company logo or a "Draft" stamp behind your text — switch to the **Transparency** tab. You can set a flat transparency percentage or use a gradient transparency with types like Linear, Axial, Radial, and others for more creative fading effects.

The Frame dialog is shown with the Transparency tab selected, titled "Area Transparency Mode." Three radio buttons appear on the left: No transparency, Transparency (with a spinner set to 50%), and Gradient (currently selected). The Gradient option expands to show a Type dropdown (set to Linear, with a visible list including Axial, Radial, Ellipsoid, Quadratic, and Square), Center X and Center Y fields, an Angle spinner (0°), a Border spinner (0%), and Start value (0%) and End value (100%) spinners. A large white preview rectangle is displayed on the right side of the dialog.

---

## UI Reference  —  Key Formatting Dialogs

_Scope: Page Style dialog Area/Transparency tabs; Paragraph dialog Borders tab_

These multi-tab dialogs provide detailed control over character formatting, paragraph layout, page styles, and search/replace.

## Find and Replace (Ctrl+H)

The Find and Replace dialog is shown with the title "Find and Replace" in the header. It contains a Find text field (empty, with focus) and a Replace text field below it. Between them are Match case and Whole words only checkboxes (both unchecked). Three buttons appear in a row: Find All, Find Previous, and Find Next. Below is an expanded "Other options" section showing checkboxes for Current selection only, Comments, Regular expressions, and partially visible checkboxes for Replace (backwards) and Paragraph Styles.

Opened via Edit > Find and Replace… or Ctrl+H.

- **Find** text field (with history dropdown)
- **Match case** / **Whole words only** checkboxes
- **Replace** text field (with history dropdown)
- **Buttons:** Find All, Find Previous, Find Next, Replace, Replace All
- **Other options** (collapsible): Current selection only, Comments, Regular expressions, Similarity search (with Similarities… button), Diacritic-sensitive, Replace backwards, Paragraph Styles
- **Attributes…** / **Format…** / **No Format** buttons for format-aware search

## Character Dialog (Format > Character…)

The Character dialog is shown with the Font tab active. Visible tabs along the top are Font, Font Effects, Position, and Hyperlink. The Font tab displays a Family field set to "Liberation Serif" with a scrollable font list below it (showing Liberation Serif highlighted, along with Linux Biolinum Keyboard O, Linux Biolinum O, Linux Libertine Display O, Linux Libertine Initials O, Linux Libertine Mono O, and Linux Libertine O). Below the list are Style (Regular), Size (12 pt), and Language (English (USA)) fields, with a partial font preview at the bottom.

**Tabs:** Font, Font Effects, Position, Hyperlink, Highlighting, Borders

- **Font tab:** Family, Style (Regular/Bold/Italic/Bold Italic), Size, Language, Features… button, font preview.
- **Font Effects tab:** Font Color + Transparency, Overlining style+color, Strikethrough style, Underlining style+color+Individual words, Case dropdown, Relief, Hidden/Outline/Shadow checkboxes.
- **Position tab:** Normal/Superscript/Subscript radio + raise/lower %, Rotation (0°/90°/270°) + Scale width + Fit to line, Character spacing + Pair kerning.

## Paragraph Dialog (Format > Paragraph…)

The Paragraph dialog is shown with the Indents & Spacing tab selected. Visible tabs across the top include Outline & List, Tabs, Drop Caps, Borders on the upper row, and Indents & Spacing and Alignment on the lower row. The Indent section has Before text, After text, and First line fields (all 0.00″) with increment/decrement buttons and an Automatic checkbox. The Spacing section shows Above paragraph and Below paragraph fields (both 0.00″) with a "Do not add space between paragraphs of the same style" checkbox. The Line Spacing section at the bottom has a dropdown set to Single.

**Tabs:** Indents & Spacing, Alignment, Text Flow, Outline & List, Tabs, Drop Caps, Borders, Area, Transparency

- **Indents & Spacing:** Before/After text indent, First line indent, Automatic; Spacing above/below paragraph; Line Spacing dropdown (Single/1.15/1.5/Double/Proportional/At least/Leading/Fixed); Activate page line-spacing.
- **Alignment:** Left/Center/Right/Justified radio; Last line dropdown; Expand single word; Text-to-text alignment; Text direction.
- **Text Flow:** Hyphenation settings, page/column breaks, orphan/widow control.
- **Tabs:** Tab stop position, type (Left/Right/Center/Decimal), fill character.

## Page Style Dialog (Format > Page Style…, Shift+Alt+P)

The Page Style dialog is shown with the title "Page Style: Default Page Style" and the Organizer tab selected. Visible tabs include Organizer, Page, Area, Transparency, Header, Footer, and a partially visible Borders tab. The Style section displays Name (Default Page Style), Next style (Default Page Style), Inherit from (empty), and Category (Custom Styles) fields. Below that, the Contains section summarizes the current settings: "11.69 inch + From top 0.79 inch, From bottom 0.79 inch + Text direction left-to-right… Default Page Style + Not page line-spacing."

**Tabs:** Organizer, Page, Area, Transparency, Header, Footer, Borders, Columns, Footnote

- **Organizer:** Style name, Next style dropdown, Inherit from, Category, Contains description.
- **Page:** Paper format (size, width, height, portrait/landscape, paper tray), Margins (left/right/top/bottom/gutter), Layout settings (page layout, page numbers, gutter position).
- **Header/Footer:** Enable checkbox, margins, spacing, same content on left/right pages.
- **Columns:** Column count, width/spacing, separator line options.

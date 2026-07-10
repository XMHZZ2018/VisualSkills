# Formatting Characters (LibreOffice Writer 7.3.7)

The quickest way to format characters is with **character styles** — just select your text, then pick a style from the Character Styles tab on the Styles deck in the Sidebar, the **Styles** menu, or the Formatting (Styles) toolbar. Styles keep things consistent and easy to update later, so reach for them before falling back to direct formatting.

That said, direct formatting is perfectly fine for one-off tweaks. Select your text and use the buttons on the Formatting toolbar or the Character panel in the Properties deck of the Sidebar. You'll find controls for font name, font size, bold, italic, underline, strikethrough, font color, highlighting color, superscript, subscript, and more right there. Click the drop-down arrow next to a button to access extra choices like double underline or a specific color from the palette.

The Properties deck of the Sidebar is shown with its Character section expanded. At the top are the Font Name dropdown (set to "Liberation Sans") and the Font Size dropdown (set to "12 pt"). Below those is a row of formatting buttons numbered 3 through 9: Bold, Italic, Underline (with a dropdown arrow), Strikethrough, Toggle Shadow, Increase Font Size, and Decrease Font Size. A second row contains buttons numbered 10 through 15: Font Color (with a red underline indicator and dropdown), Highlight Color (with a yellow marker icon and dropdown), Clear Direct Formatting (eraser icon), Set Character Spacing (with dropdown), Superscript, and Subscript. A "More Options" link (labeled 16) in the upper-right corner opens the full Character dialog. Below the Character section, a collapsed Paragraph section is also visible.

To bump the font size up or down quickly, use the **Increase Font Size** and **Decrease Font Size** buttons on the Sidebar — though they step in fixed increments (usually 2pt). For precise sizing, type directly into the Font Size drop-down instead.

For the full set of options, select your text and open **Format > Character...** (or click **More Options** on the Sidebar). The Character dialog has six tabs. The **Font** tab lets you pick family, typeface (regular, bold, italic, bold italic), and size, with a live preview at the bottom. The **Font Effects** tab is where you control font color, transparency, overlining, strikethrough style, underlining style, case changes (uppercase, lowercase, small capitals), and relief effects like embossed or engraved.

The Character dialog is shown open to the Font Effects tab. Six tabs are visible across the top: Font, Font Effects (currently selected and highlighted in blue), Position, Hyperlink, Highlighting, and Borders. The tab body is divided into three sections. The "Font Color" section has a Font color dropdown set to "Automatic" and a Transparency spinner set to "0%". The "Text Decoration" section contains three dropdown rows — Overlining, Strikethrough, and Underlining — each set to "(Without)", with Overlining and Underlining also having an adjacent color dropdown set to "Automatic"; an "Individual words" checkbox appears below Underlining. The "Effects" section at the bottom has a Case dropdown and a Relief dropdown, both set to "(Without)", along with checkboxes for Hidden, Outline, and Shadow.

The **Position** tab handles superscripts and subscripts with fine-grained control over raise/lower amount and relative font size. It also includes rotation/scaling settings and character spacing — use the Pair Kerning checkbox to let the font's built-in kerning do its thing. For a quick spacing adjustment without opening the dialog, use the **Character Spacing** drop-down on the Sidebar, which offers presets from Very Tight to Very Loose plus a custom value option.

The **Hyperlink** tab lets you turn selected text into a clickable link to a URL, another part of the document, or another file — it's a lighter alternative to **Insert > Hyperlink**. The **Highlighting** tab sets a background color behind selected characters, handy for marking up drafts.

One thing to keep in mind: direct character formatting overrides character styles, just as direct paragraph formatting overrides paragraph styles. If your text isn't responding to a style change, check whether leftover direct formatting is getting in the way — use **Clear Direct Formatting** on the Sidebar to strip it out.

---

## UI Reference  —  Format Menu

_Scope: Text submenu (Bold, Italic, Underline, case transforms), Character…, Clear Direct Formatting_

The Format menu controls text styling, paragraph formatting, page layout, and document-level formatting options.

The Format menu is shown fully expanded as a single-column dropdown. The top section contains three submenu entries — Text, Spacing, and Align Text — each with a right-pointing arrow indicating submenus. Below that are Clone Formatting (with a paintbrush icon), Clear Direct Formatting, and Spotlight (with a submenu arrow). A separator line precedes Character…, Paragraph…, Lists (submenu), and Bullets and Numbering…. Another group contains Theme…, Page Style…, Title Page…, Columns…, and Watermark…, with Sections… grayed out. The bottom section shows context-sensitive entries: Image, Text Box and Shape, Frame and Object, Name… and Alt Text… (both grayed out), followed by Anchor, Wrap, Arrange, Rotate or Flip, and Group.

## Elements

- **Text** (►) — 19 text style commands: Bold (Ctrl+B), Italic (Ctrl+I), Single/Double Underline, Strikethrough, Overline, Superscript (Shift+Ctrl+P), Subscript (Shift+Ctrl+B), Shadow, Outline Font Effect, Increase/Decrease Size (Ctrl+]/[), case transforms (UPPERCASE, lowercase, Cycle Case Shift+F3, Sentence case, Capitalize Every Word, tOGGLE cASE), Small Capitals (Shift+Ctrl+K).
- **Spacing** (►) — Line Spacing (1, 1.15, 1.5, 2), Increase/Decrease Paragraph Spacing, Increase/Decrease Indent.
- **Align Text** (►) — Left (Ctrl+L), Centered (Ctrl+E), Right (Ctrl+R), Justified (Ctrl+J).
- **Clone Formatting** — Paint formatting from selection to other text.
- **Clear Direct Formatting** (Ctrl+M) — Remove all manual formatting, revert to style defaults.
- **Spotlight** (►) — Highlight formatting in document: Character Direct Formatting, Paragraph Styles, Character Styles.
- **Character…** — Opens the Character dialog (see [Formatting Dialogs](formatting-dialogs.md)).
- **Paragraph…** — Opens the Paragraph dialog (see [Formatting Dialogs](formatting-dialogs.md)).
- **Lists** (►) — No List (Shift+Ctrl+F12), Unordered List (Shift+F12), Ordered List (F12), Demote/Promote Outline Level, Move Item Down/Up (Ctrl+Alt+Down/Up), Insert Unnumbered Entry, Restart Numbering, Add to List.
- **Bullets and Numbering…** — Full list formatting dialog.
- **Theme…** — Document theme settings.
- **Page Style…** (Shift+Alt+P) — Opens the Page Style dialog (see [Formatting Dialogs](formatting-dialogs.md)).
- **Title Page…** — Add/configure title pages.
- **Columns…** — Multi-column page layout dialog.
- **Watermark…** — Insert or configure a watermark.
- Context-sensitive submenus (active when an object is selected): Image, Text Box and Shape, Frame and Object, Anchor, Wrap, Arrange, Rotate or Flip, Group.

---

## UI Reference  —  Key Formatting Dialogs

_Scope: Character dialog tabs: Font, Font Effects, Position, Hyperlink, Highlighting, Borders_

These multi-tab dialogs provide detailed control over character formatting, paragraph layout, page styles, and search/replace.

## Find and Replace (Ctrl+H)

The Find and Replace dialog is shown with the title bar reading "Find and Replace." At the top is a Find text field (empty, with a blue focus outline), followed by "Match case" and "Whole words only" checkboxes on the same row. Below is a Replace text field. Three buttons — Find All, Find Previous, and Find Next — appear in a row beneath the Replace field. An "Other options" disclosure triangle is expanded, revealing checkboxes for "Current selection only," "Comments," "Regular expressions," and partially visible options for "Replace backwards" and "Paragraph Styles" on the right side.

Opened via Edit > Find and Replace… or Ctrl+H.

- **Find** text field (with history dropdown)
- **Match case** / **Whole words only** checkboxes
- **Replace** text field (with history dropdown)
- **Buttons:** Find All, Find Previous, Find Next, Replace, Replace All
- **Other options** (collapsible): Current selection only, Comments, Regular expressions, Similarity search (with Similarities… button), Diacritic-sensitive, Replace backwards, Paragraph Styles
- **Attributes…** / **Format…** / **No Format** buttons for format-aware search

## Character Dialog (Format > Character…)

The Character dialog is shown open to the Font tab. The title bar reads "Character" (partially visible). Four tabs are visible across the top: Font (currently selected), Font Effects, Position, and Hyperlink. The Font tab displays a Family field set to "Liberation Serif" with a scrollable list below showing installed fonts (Liberation Serif highlighted in blue, followed by Linux Biolinum Keyboard O, Linux Biolinum O, Linux Libertine Display O, Linux Libertine Initials O, Linux Libertine Mono O, and Linux Libertine O). Below the font list are a Style field set to "Regular," a Size field set to "12 pt," and a Language field set to "English (USA)." A partial preview note at the bottom reads "The same font will be used on both your pri…".

**Tabs:** Font, Font Effects, Position, Hyperlink, Highlighting, Borders

- **Font tab:** Family, Style (Regular/Bold/Italic/Bold Italic), Size, Language, Features… button, font preview.
- **Font Effects tab:** Font Color + Transparency, Overlining style+color, Strikethrough style, Underlining style+color+Individual words, Case dropdown, Relief, Hidden/Outline/Shadow checkboxes.
- **Position tab:** Normal/Superscript/Subscript radio + raise/lower %, Rotation (0°/90°/270°) + Scale width + Fit to line, Character spacing + Pair kerning.

## Paragraph Dialog (Format > Paragraph…)

The Paragraph dialog is shown open to the Indents & Spacing tab. The title bar reads "Paragraph." Two rows of tabs are visible: the top row contains Outline & List, Tabs, Drop Caps, and Borders; the bottom row shows Indents & Spacing (currently selected, with a blue underline) and Alignment. The Indent section has three spinner fields — "Before text," "After text," and "First line" — all set to 0.00″, each with minus and plus buttons. An "Automatic" checkbox sits below. The Spacing section has "Above paragraph" and "Below paragraph" spinners (both 0.00″) with plus/minus buttons, and a checkbox labeled "Do not add space between paragraphs of the same style." The Line Spacing section at the bottom has a dropdown set to "Single."

**Tabs:** Indents & Spacing, Alignment, Text Flow, Outline & List, Tabs, Drop Caps, Borders, Area, Transparency

- **Indents & Spacing:** Before/After text indent, First line indent, Automatic; Spacing above/below paragraph; Line Spacing dropdown (Single/1.15/1.5/Double/Proportional/At least/Leading/Fixed); Activate page line-spacing.
- **Alignment:** Left/Center/Right/Justified radio; Last line dropdown; Expand single word; Text-to-text alignment; Text direction.
- **Text Flow:** Hyphenation settings, page/column breaks, orphan/widow control.
- **Tabs:** Tab stop position, type (Left/Right/Center/Decimal), fill character.

## Page Style Dialog (Format > Page Style…, Shift+Alt+P)

The Page Style dialog is shown open to the Organizer tab with the title bar reading "Page Style: Default Page Style." Seven tabs are visible across the top: Organizer (currently selected), Page, Area, Transparency, Header, Footer, and a partially visible tab (Borders). The Style section contains four fields: Name set to "Default Page Style," Next style set to "Default Page Style," Inherit from (empty), and Category set to "Custom Styles." Below is a Contains section displaying a summary: "11.69 inch + From top 0.79 inch, From bottom 0.79 inch + Text direction left-to-right (ho… Default Page Style + Not page line-spacing."

**Tabs:** Organizer, Page, Area, Transparency, Header, Footer, Borders, Columns, Footnote

- **Organizer:** Style name, Next style dropdown, Inherit from, Category, Contains description.
- **Page:** Paper format (size, width, height, portrait/landscape, paper tray), Margins (left/right/top/bottom/gutter), Layout settings (page layout, page numbers, gutter position).
- **Header/Footer:** Enable checkbox, margins, spacing, same content on left/right pages.
- **Columns:** Column count, width/spacing, separator line options.

---

## UI Reference  —  Formatting Toolbar

_Scope: Font Name/Size, Bold, Italic, Underline, Strikethrough, Super/Subscript, Font Color, Highlighting_

The second toolbar row provides all character and paragraph formatting controls with split-button dropdowns.

The Formatting toolbar is displayed as a single horizontal row. From left to right, it contains: a Paragraph Style dropdown showing "Default Paragraph Style," two small style-management icons (Update Selected Style and New Style from Selection), a Font Name dropdown showing "Liberation Serif," a Font Size dropdown showing "12 pt," then a separator followed by Bold (B), Italic (I), Underline (U with a dropdown arrow), Strikethrough (S), Superscript (x²), and Subscript (x₂) buttons. After another separator are the Font Color button (A with a red underline), a highlighting/text-effect button, and a character highlighting color button (with a colored underline indicator). The row continues with alignment buttons for Left, Center, Right, and Justified, followed by list and indent controls toward the right end.

## Elements

Row (left → right):

- **Paragraph Style** dropdown — Shows current style (e.g. "Default Paragraph Style"). Dropdown lists: Clear formatting, Default Paragraph Style, Body Text, Title, Subtitle, Heading 1–4, Block Quotation, Preformatted Text, More Styles…
- **Update Selected Style** (Shift+Ctrl+F11) — Update current style to match cursor formatting.
- **New Style from Selection** (Shift+F11) — Create a new style from current formatting.
- **Font Name** dropdown — Shows/changes the font (e.g. "Liberation Serif"). Lists all installed fonts rendered in their own typeface.
- **Font Size** dropdown — Shows/changes size in pt (6–48, plus custom values).

| *(separator)* |

- **Bold** (Ctrl+B) / **Italic** (Ctrl+I)
- **Underline** (Ctrl+U, split-button ▼) — Toggle; dropdown offers 11 underline styles (single, double, bold, dotted, dashed, wavy, etc.) plus More Options…
- **Strikethrough**
- **Superscript** (Shift+Ctrl+P) / **Subscript** (Shift+Ctrl+B)
- **Clear Direct Formatting** (Ctrl+M) — Eraser icon; removes all manual formatting.

| *(separator)* |

- **Font Color** (split-button ▼) — Applies current color; dropdown opens ~120-swatch color picker with Custom Color… option.
- **Character Highlighting Color** (split-button ▼) — Marker-pen highlight; dropdown opens color picker.

| *(separator)* |

- **Align Left** (Ctrl+L) / **Align Center** (Ctrl+E) / **Align Right** (Ctrl+R) / **Justified** (Ctrl+J)

| *(separator)* |

- **Toggle Unordered List** (Shift+F12, split-button ▼) — Bullet list; dropdown shows 8 bullet styles + Customize…
- **Toggle Ordered List** (F12, split-button ▼) — Numbered list; dropdown shows 8 numbering styles + Customize…
- **Select Outline Format** (split-button ▼) — Multi-level outline presets.
- **Increase Indent** / **Decrease Indent**

| *(separator)* |

- **Set Line Spacing** (split-button ▼) — Presets (1, 1.15, 1.5, 2) plus custom value editor.
- **Increase Paragraph Spacing** / **Decrease Paragraph Spacing**

---

## UI Reference  —  Right Sidebar

_Scope: Properties > Character section: font, size, bold/italic, color, highlighting_

The collapsed right sidebar is a vertical strip of 8 icon buttons along the right edge of the window. Each opens a full docked panel. Toggle the sidebar with Ctrl+F5 or View > Sidebar.

The full LibreOffice Writer window is shown with an empty document. Along the right edge of the window is a narrow vertical strip of icon buttons representing the collapsed sidebar. The topmost button is highlighted with a red rectangle and a tooltip reading "Properties (Alt+1)." Below it are seven additional small icons for the other sidebar panels (Styles, Gallery, Navigator, Page, Style Inspector, Manage Changes, and Accessibility Check), arranged vertically. The main document area shows a blank page with a cursor in the upper-left corner, and the Formatting toolbar and Standard toolbar are visible across the top of the window.

## Panel Buttons (top to bottom)

- **Properties** (Alt+1) — Formatting panel with three collapsible sections:
  - *Style:* Paragraph style dropdown, Clone Formatting, Update/New Style buttons.
  - *Character:* Font family, size, Bold/Italic/Underline/Strikethrough, Font Color, Highlighting, Change Case, Super/Subscript.
  - *Paragraph:* Alignment, lists/indent toolbar, line spacing, above/below spacing fields, left/right/first-line indent.

- **Styles** (Alt+2 / F11) — Full style manager: category toolbar (Paragraph/Character/Frame/Page/List/Table Styles), hierarchical style list, Fill Format Mode, filter dropdown. See [Styles](styles.md).

- **Gallery** (Alt+3) — Clip-art browser: categories (Arrows, BPMN, Bullets, Diagrams, Flow chart, Icons), thumbnail grid, Icon/Detailed view, New… button.

- **Navigator** (Alt+4 / F5) — Document structure tree: Headings, Tables, Frames, Images, OLE objects, Bookmarks, Sections, Hyperlinks, References, Indexes, Comments, Drawing objects, Fields, Footnotes, Endnotes. Includes page navigation controls and drag-mode options.

- **Page** (Alt+5) — Page layout panel:
  - *Format:* Size (A4), Width/Height, Orientation (Portrait/Landscape), Margins.
  - *Styles:* Page number format, Background, Layout, Columns.
  - *Header/Footer:* Enable toggles, margins, spacing, same-content options.

- **Style Inspector** (Alt+6) — Two-column Properties/Value tree showing all applied styles: Paragraph Styles, Paragraph Direct Formatting, Character Styles, Character Direct Formatting (50+ properties per node).

- **Manage Changes** (Alt+7) — Two tabs:
  - *List:* Action/Author/Date/Comment table with Accept/Reject/Accept All/Reject All buttons.
  - *Filter:* Date range, Author, Action, Comment filters.

- **Accessibility Check** (Alt+8) — Runs an accessibility audit and lists issues by category, each with a Fix… button.

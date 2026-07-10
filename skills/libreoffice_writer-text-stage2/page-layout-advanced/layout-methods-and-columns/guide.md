# Layout Methods and Columns (LibreOffice Writer 7.3.7)

Writer gives you several ways to control page layout: columns, frames, tables, sections, page orientation changes, and borders/backgrounds. Every page in a Writer document is based on a page style, and all the other layout methods build on top of that underlying style.

A quick tip before you start: turn on layout helpers by going to **Tools > Options > LibreOffice > Application Colors** to show text, object, table, and section boundaries. You can also tweak paragraph marks, tabs, and breaks under **Tools > Options > LibreOffice Writer > Formatting Aids**. These visual cues make complex layouts much easier to wrangle.

## Choosing a layout method

Which technique you pick depends on what your final document needs to be. For a book-style layout with one column of text and the occasional figure, page styles alone will carry you. If you need two or more columns — like an index where text flows left-to-right then down — use sections with columns. For a newsletter with two or three columns per page and articles that jump across pages, combine page styles with linked frames and anchored graphics.

Keep in mind that if you're targeting HTML, EPUB, or another reflowable format, stick to minimal layout techniques. Columns, frames, and wide tables often don't export cleanly to those formats.

## Defining columns on a page

Start by setting up your base page style (typically *Default Page Style*) with the column count you'll use most. Open it via **Format > Page Style** on the menu bar, or right-click the page and choose **Page Style** from the context menu. Head over to the **Columns** tab.

In the **Settings** section, pick the number of columns and set the spacing between them. You can choose one of Writer's predefined column layouts or create a custom one. The live preview on the right side of the dialog shows exactly how your layout will look. Hit **OK** when you're happy.

The Page Style: Default Style dialog is shown with the Columns tab selected. At the top, the Settings section has a Columns spin box set to 2 and a row of predefined column layout icons beside it, with a live page preview on the far right showing a two-column layout. Below that, the Width and Spacing section has AutoWidth unchecked, with individual width fields for columns 1 and 2 set to 8.25 cm each and a spacing value of 0.50 cm. At the bottom, a Separator Line section provides controls for the line style (set to a solid line), width (0.25 pt), color (Black), height (100%), and position (Top).

If you want different column counts on the same page — say a full-width title above a two-column body — you'll need sections instead of page-level columns. That's covered under "Using sections for page layout."

## Column width and spacing

By default, **AutoWidth** is selected, which divides space equally among all columns. To set custom widths, deselect **AutoWidth** in the *Width and Spacing* section, then type a width for each column individually. Use the **Spacing** line to control the gap between each pair of columns. If you have more than three columns, use the arrow buttons on the *Column* line to scroll through them.

---

## UI Reference  —  Format Menu

_Scope: Columns… dialog_

The Format menu controls text styling, paragraph formatting, page layout, and document-level formatting options.

The Format menu is shown open as a dropdown from the menu bar. It lists entries from top to bottom: Text (with a submenu arrow), Spacing (submenu arrow), Align Text (submenu arrow), Clone Formatting, Clear Direct Formatting, Spotlight (submenu arrow), then a separator followed by Character…, Paragraph…, Lists (submenu arrow), Bullets and Numbering…, Theme…, then another separator with Page Style…, Title Page…, Columns…, Watermark…, and the grayed-out Sections…. Below a final separator are context-sensitive items: Image, Text Box and Shape, Frame and Object, the grayed-out Name… and Alt Text…, then Anchor, Wrap, Arrange, Rotate or Flip, and Group.

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

_Scope: Page Style dialog Columns tab_

These multi-tab dialogs provide detailed control over character formatting, paragraph layout, page styles, and search/replace.

## Find and Replace (Ctrl+H)

The Find and Replace dialog is a floating window titled "Find and Replace." It contains a Find text field at the top with checkboxes for "Match case" and "Whole words only" beneath it, followed by a Replace text field. Below these are three buttons in a row: Find All, Find Previous, and Find Next. An expanded "Other options" section shows additional checkboxes including "Current selection only," "Comments," "Regular expressions," "Replace backwards" (partially visible), and "Paragraph Styles" (partially visible).

Opened via Edit > Find and Replace… or Ctrl+H.

- **Find** text field (with history dropdown)
- **Match case** / **Whole words only** checkboxes
- **Replace** text field (with history dropdown)
- **Buttons:** Find All, Find Previous, Find Next, Replace, Replace All
- **Other options** (collapsible): Current selection only, Comments, Regular expressions, Similarity search (with Similarities… button), Diacritic-sensitive, Replace backwards, Paragraph Styles
- **Attributes…** / **Format…** / **No Format** buttons for format-aware search

## Character Dialog (Format > Character…)

The Character dialog is shown with the Font tab active. Visible tabs along the top are Font, Font Effects, Position, and Hyperlink. The Font tab displays a Family field set to "Liberation Serif" with a scrollable list of available fonts below it (showing Liberation Serif highlighted in blue, along with Linux Biolinum Keyboard O, Linux Biolinum O, Linux Libertine Display O, and others). Below the font list are fields for Style (set to "Regular"), Size (set to "12 pt"), and Language (set to "English (USA)").

**Tabs:** Font, Font Effects, Position, Hyperlink, Highlighting, Borders

- **Font tab:** Family, Style (Regular/Bold/Italic/Bold Italic), Size, Language, Features… button, font preview.
- **Font Effects tab:** Font Color + Transparency, Overlining style+color, Strikethrough style, Underlining style+color+Individual words, Case dropdown, Relief, Hidden/Outline/Shadow checkboxes.
- **Position tab:** Normal/Superscript/Subscript radio + raise/lower %, Rotation (0°/90°/270°) + Scale width + Fit to line, Character spacing + Pair kerning.

## Paragraph Dialog (Format > Paragraph…)

The Paragraph dialog is shown with the Indents & Spacing tab selected. Visible tabs along the top row are Outline & List, Tabs, Drop Caps, and Borders; a second row shows Indents & Spacing and Alignment. The Indent section has fields for "Before text," "After text," and "First line," all set to 0.00″, each with minus and plus buttons and an "Automatic" checkbox. The Spacing section has "Above paragraph" and "Below paragraph" fields (both 0.00″) with a checkbox for "Do not add space between paragraphs of the same style." The Line Spacing section at the bottom has a dropdown set to "Single."

**Tabs:** Indents & Spacing, Alignment, Text Flow, Outline & List, Tabs, Drop Caps, Borders, Area, Transparency

- **Indents & Spacing:** Before/After text indent, First line indent, Automatic; Spacing above/below paragraph; Line Spacing dropdown (Single/1.15/1.5/Double/Proportional/At least/Leading/Fixed); Activate page line-spacing.
- **Alignment:** Left/Center/Right/Justified radio; Last line dropdown; Expand single word; Text-to-text alignment; Text direction.
- **Text Flow:** Hyphenation settings, page/column breaks, orphan/widow control.
- **Tabs:** Tab stop position, type (Left/Right/Center/Decimal), fill character.

## Page Style Dialog (Format > Page Style…, Shift+Alt+P)

The Page Style: Default Page Style dialog is shown with the Organizer tab active. Visible tabs along the top are Organizer, Page, Area, Transparency, Header, and Footer (with Borders and additional tabs partially cut off to the right). Under the Style heading, the Name field shows "Default Page Style," the Next style field shows "Default Page Style," the Inherit from field is empty, and Category is set to "Custom Styles." A Contains section below summarizes the style as "11.69 inch + From top 0.79 inch, From bottom 0.79 inch + Text direction left-to-right … Default Page Style + Not page line-spacing."

**Tabs:** Organizer, Page, Area, Transparency, Header, Footer, Borders, Columns, Footnote

- **Organizer:** Style name, Next style dropdown, Inherit from, Category, Contains description.
- **Page:** Paper format (size, width, height, portrait/landscape, paper tray), Margins (left/right/top/bottom/gutter), Layout settings (page layout, page numbers, gutter position).
- **Header/Footer:** Enable checkbox, margins, spacing, same content on left/right pages.
- **Columns:** Column count, width/spacing, separator line options.

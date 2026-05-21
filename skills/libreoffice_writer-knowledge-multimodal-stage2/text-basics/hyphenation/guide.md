# Hyphenating Words (LibreOffice Writer 7.3.7)

Writer gives you two ways to hyphenate words at the end of a line: let it happen automatically through paragraph styles and hyphenation dictionaries, or insert soft hyphens manually right where you want them. You can also just skip hyphenation entirely — it's up to you.

## Automatic hyphenation

Automatic hyphenation is style-driven and overrides whatever you set under **Tools > Options**. To turn it on, click the **Styles** tab on the Sidebar to open the Styles deck. In the Paragraph Styles list, right-click **Default Paragraph Style** and choose **Modify**. In the dialog that opens, go to the **Text Flow** tab and look for the *Hyphenation* section — select or deselect **Automatically**. When it's on, you can also set criteria like how many characters to leave before or after a line break. Hit **OK** to save.

See `fig01.png`.

Keep in mind that turning on hyphenation for the *Default Style* affects all paragraph styles based on it. If you don't want headings hyphenated, for example, you can individually change those styles. Styles not based on Default Style won't be affected at all.

You can fine-tune hyphenation behavior globally under **Tools > Options > Language Settings > Writing Aids**. These settings only kick in when there's no specific setting in a paragraph style and automatic hyphenation is already enabled. Near the bottom of the Options area, you'll find controls for the minimum number of characters for hyphenation, characters before/after a line break, and more. Select an item and click **Edit** to change it.

See `fig02.png`.

Two handy options live here: **Hyphenate without inquiry** (Writer silently hyphenates words the dictionary doesn't recognize, instead of prompting you) and **Hyphenate special regions** (extends hyphenation into footnotes, headers, and footers).

## Manual hyphenation

When you need precise control, use a soft hyphen. Unlike a regular hyphen, a soft hyphen only appears when the word actually falls at the end of a line — if the text reflows, it vanishes. Place your cursor where you'd like the break and press **Ctrl+hyphen (minus sign)**, or go to **Insert > Formatting Mark > Insert Soft Hyphen**. The word will break at that spot when it lands at line's end, even if automatic hyphenation is off for that paragraph.

---

## UI Reference  —  Key Formatting Dialogs

_Scope: Paragraph dialog Text Flow tab Hyphenation settings_

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

---

## UI Reference  —  Tools Menu

_Scope: Language > Hyphenation… command_

The Tools menu provides document proofing, language settings, automation, and application-wide configuration.

Read the screenshot `ui-tools-menu.png` in this directory.

## Elements

- **Spelling…** (F7) — Open the spelling dialog.
- **Automatic Spell Checking** (Shift+F7) — Toggle live spell-check underlines.
- **Thesaurus…** (Ctrl+F7) — Look up synonyms (requires thesaurus dictionary).
- **Language** (►) — Set language For Selection / For Paragraph / For All Text, Hyphenation…, More Dictionaries Online…
- **Word Count…** — Show detailed word/character counts.
- **Accessibility Check…** (Alt+8) / **Automatic Accessibility Checking** — Audit document for accessibility issues.
- **AutoCorrect** (►) — While Typing (toggle), Apply, Apply and Edit Changes, AutoCorrect Options… (5-tab dialog: Replace, Exceptions, Options, Localized Options, Word Completion).
- **AutoText…** (Ctrl+F3) — Manage reusable text blocks.
- **Redact** / **Auto-Redact** — Document redaction tools.
- **Heading Numbering…** — Configure outline numbering for headings.
- **Line Numbering…** — Enable/configure line numbers (position, interval, separator).
- **Footnote/Endnote Settings…** — Configure footnote/endnote formatting.
- **Mail Merge Wizard…** — Step-by-step mail merge.
- **Bibliography Database** / **Address Book Source…** — Database connections.
- **Update** (►) — Refresh: Update All, Page Formatting, Fields (F9), Indexes and Tables, Links, Charts.
- **Protect Document** (►) — Protect Fields (checkbox), Protect Bookmarks (checkbox).
- **Calculate** (Ctrl++) / **Sort…** — In-document calculation and sorting.
- **Macros** (►) — Run Macro…, Edit Macros…, Organize Macros, Digital Signature…, Organize Dialogs…
- **Development Tools** — Toggle developer panel.
- **XML Filter Settings…** / **Extensions…** (Ctrl+Alt+E) / **Customize…**
- **Options…** (Alt+F12) — Opens the comprehensive Options dialog with tree navigation: LibreOffice (User Data, General, View, Print, Paths, Fonts, Security, etc.), Load/Save, Languages, LibreOffice Writer, and more.


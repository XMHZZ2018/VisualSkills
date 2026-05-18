# Hyphenating Words (LibreOffice Writer 7.3.7)

Writer gives you two ways to hyphenate words at the end of a line: let it happen automatically through paragraph styles and hyphenation dictionaries, or insert soft hyphens manually right where you want them. You can also just skip hyphenation entirely — it's up to you.

## Automatic hyphenation

Automatic hyphenation is style-driven and overrides whatever you set under **Tools > Options**. To turn it on, click the **Styles** tab on the Sidebar to open the Styles deck. In the Paragraph Styles list, right-click **Default Paragraph Style** and choose **Modify**. In the dialog that opens, go to the **Text Flow** tab and look for the *Hyphenation* section — select or deselect **Automatically**. When it's on, you can also set criteria like how many characters to leave before or after a line break. Hit **OK** to save.

The "Paragraph Style: Default Paragraph Style" dialog is shown with the **Text Flow** tab selected. The left side of the tab contains a **Hyphenation** section with the **Automatically** checkbox checked, an unchecked **Don't hyphenate words in CAPS** checkbox, and three spin boxes: "Characters at line end" set to 2, "Characters at line begin" set to 2, and "Maximum number of consecutive hyphens" set to 0. The right side contains a **Breaks** section with options for inserting page or column breaks. Multiple other tabs are visible along the top of the dialog, including Organizer, Indents & Spacing, Alignment, Font, Font Effects, Position, Highlighting, Tabs, Drop Caps, Area, Transparency, Borders, and Outline & Numbering.

Keep in mind that turning on hyphenation for the *Default Style* affects all paragraph styles based on it. If you don't want headings hyphenated, for example, you can individually change those styles. Styles not based on Default Style won't be affected at all.

You can fine-tune hyphenation behavior globally under **Tools > Options > Language Settings > Writing Aids**. These settings only kick in when there's no specific setting in a paragraph style and automatic hyphenation is already enabled. Near the bottom of the Options area, you'll find controls for the minimum number of characters for hyphenation, characters before/after a line break, and more. Select an item and click **Edit** to change it.

The **Options** section from the Writing Aids dialog is shown, containing a scrollable list with five entries: "Minimum number of characters for hyphenation: 5" (currently selected and highlighted), "Characters before line break: 2", "Characters after line break: 2", "Hyphenate without inquiry" (unchecked), and "Hyphenate special regions" (checked). An **Edit…** button appears to the right of the list, and up/down arrow buttons are on the far right for reordering items.

Two handy options live here: **Hyphenate without inquiry** (Writer silently hyphenates words the dictionary doesn't recognize, instead of prompting you) and **Hyphenate special regions** (extends hyphenation into footnotes, headers, and footers).

## Manual hyphenation

When you need precise control, use a soft hyphen. Unlike a regular hyphen, a soft hyphen only appears when the word actually falls at the end of a line — if the text reflows, it vanishes. Place your cursor where you'd like the break and press **Ctrl+hyphen (minus sign)**, or go to **Insert > Formatting Mark > Insert Soft Hyphen**. The word will break at that spot when it lands at line's end, even if automatic hyphenation is off for that paragraph.

---

## UI Reference  —  Tools Menu

_Scope: Language > Hyphenation…_

The Tools menu provides document proofing, language settings, automation, and application-wide configuration.

The **Tools** drop-down menu is shown open in the LibreOffice Writer menu bar. It displays a vertical list of menu items organized into logical groups separated by dividers: Spelling…, Automatic Spell Checking (checked), Thesaurus…, Language, Word Count…, Accessibility Check…, Automatic Accessibility Checking (unchecked), AutoCorrect, AutoText…, ImageMap (grayed out), Redact, Auto-Redact, Heading Numbering…, Line Numbering…, Footnote/Endnote Settings…, Mail Merge Wizard…, Bibliography Database, Address Book Source…, Update, Protect Document, Calculate (grayed out), Sort… (grayed out), Macros, Development Tools (unchecked), XML Filter Settings…, Extensions…, Customize…, and Options… at the bottom.

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

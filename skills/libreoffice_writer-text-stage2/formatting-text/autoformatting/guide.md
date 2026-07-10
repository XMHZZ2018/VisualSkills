# Autoformatting (LibreOffice Writer 7.3.7)

Writer can automatically format parts of your document as you type — things like replacing straight quotes with curly ones, capitalizing the first letter of sentences, or applying bulleted list styles. All of this is controlled through the AutoCorrect dialog at **Tools > AutoCorrect > AutoCorrect Options**.

If you ever notice unexpected formatting changes popping up in your document, that dialog is the first place to look. You can also quickly toggle features on or off via **Tools > AutoCorrect**, where you'll find several submenu options.

**While Typing** automatically formats the document as you go — it's the most common mode. **Apply** does a one-shot format of the entire document. **Apply and Edit Changes** does the same but opens a dialog letting you accept or reject each change individually, which is handy when you want more control.

The **Localized Options** tab (in the AutoCorrect dialog) handles quotation marks and apostrophes. Most fonts include curly ("smart") quotes, and Writer will swap them in automatically. But if you're working with things like geographic coordinates or minutes/seconds notation, you may want straight quotes instead — just uncheck the **Replace** boxes under Single Quotes or Double Quotes.

The image shows two views of the AutoCorrect dialog. The upper portion displays the Localized Options tab, which has a language selector set to "English (USA)" and five tabs across the top (Replace, Exceptions, Options, Localized Options, Word Completion). The Localized Options tab body contains a checklist of four items with [M] and [T] columns — including options for non-breaking spaces in French text, formatting ordinal number suffixes, transliterating to Old Hungarian, and replacing angle brackets with angle quotes — followed by separate Single Quotes and Double Quotes sections, each with a "Replace" checkbox and Start quote / End quote character selectors with Default buttons. The lower portion shows the Options tab of the same dialog, listing approximately 18 autocorrect rules each with [M] and [T] checkboxes, such as "Use replacement table," "Correct TWo INitial CApitals," "Capitalize first letter of every sentence," "URL Recognition," "Replace dashes," "Create table," and more. At the bottom, a legend explains that [M] means "Replace while modifying existing text" and [T] means "AutoCorrect while typing," alongside an Edit button.

The **Options** tab is where the real power lives. Here you'll find toggles for things like capitalizing the first letter of every sentence, correcting accidental caps lock usage, replacing dashes, removing blank paragraphs, and even creating tables automatically. The tab also distinguishes between modifying existing text (**[M]**) and autocorrecting while typing (**[T]**), so you can fine-tune which rules apply in which mode.

Most people leave smart quotes on and use **Insert > Special Characters** for the occasional straight quote. Beyond that, it's worth scanning the Options tab once to disable anything that fights with your particular writing style.

---

## UI Reference  —  Format Menu

_Scope: Clone Formatting, Clear Direct Formatting (Ctrl+M)_

The Format menu controls text styling, paragraph formatting, page layout, and document-level formatting options.

The screenshot shows the Format drop-down menu open from the Writer menu bar. The menu lists items in order from top to bottom: Text, Spacing, Align Text (each with a submenu arrow), then Clone Formatting (with a paintbrush icon) and Clear Direct Formatting, followed by Spotlight (with a submenu arrow). A separator precedes Character…, Paragraph…, Lists (with a submenu arrow), and Bullets and Numbering…. Another group contains Theme…, Page Style…, Title Page…, Comments… (grayed out), Columns…, Watermark…, and Sections… (grayed out). The lower section shows context-sensitive entries: Image, Text Box and Shape, Frame and Object, Name… and Alt Text… (both grayed out), then Anchor, Wrap, Arrange, Rotate or Flip, and Group.

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

## UI Reference  —  Tools Menu

_Scope: AutoCorrect submenu: While Typing, Apply, AutoCorrect Options…_

The Tools menu provides document proofing, language settings, automation, and application-wide configuration.

The screenshot shows the Tools drop-down menu open from the Writer menu bar. From top to bottom, the entries are: Spelling… (with a spellcheck icon), Automatic Spell Checking (with a checked checkbox and icon), Thesaurus… (grayed out), Language (with a submenu arrow), Word Count…, Accessibility Check…, and Automatic Accessibility Checking (with an unchecked checkbox). Below a separator: AutoCorrect (with a submenu arrow), AutoText…, and ImageMap (grayed out). The next group contains Redact and Auto-Redact, then Heading Numbering…, Line Numbering…, and Footnote/Endnote Settings…. Further down: Mail Merge Wizard…, Bibliography Database, and Address Book Source…. Another separator precedes Update and Protect Document (both with submenu arrows), then Calculate (grayed out) and Sort… (grayed out). The bottom section lists Macros (with a submenu arrow), Development Tools (with an unchecked checkbox), XML Filter Settings…, Extensions…, Customize…, and Options….

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

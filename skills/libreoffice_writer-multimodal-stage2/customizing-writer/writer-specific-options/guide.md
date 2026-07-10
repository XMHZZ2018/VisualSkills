# Writer-Specific Options (LibreOffice Writer 7.3.7)

All of Writer's own settings live under **Tools > Options**, then click the marker (+ or triangle) next to **LibreOffice Writer** on the left side of the dialog. Let's walk through the key pages.

## General

The **LibreOffice Writer – General** page controls link and field updating, measurement units, and tab stop distance. You can tell Writer to automatically update fields and charts while you work, or turn that off if it's slowing things down. Under *Update Links when Loading*, pick **Always**, **On request**, or **Never** depending on whether your documents link to external files. The **Tab stops** setting also drives the indent distance used by the **Increase Indent** and **Decrease Indent** buttons on the toolbar, so set it thoughtfully. Further down, you can define additional word-count separators and enable a standardized page count for publishing workflows.

See `fig01.png`.

## View and Formatting Aids

Two pages handle how your document looks on screen. The **View** page lets you toggle the display of images, tables, drawings, comments, and field codes like hidden text or hidden paragraphs. You can also choose to show tracked deletions in the margin and enable tooltips on tracked changes. The **Formatting Aids** page controls which non-printing symbols appear when you turn on **View > Formatting Marks** — paragraph marks, tabs, spaces, breaks, and more. There's also a **Direct Cursor** option that lets you click anywhere on a blank page and start typing, though be warned: it can introduce odd formatting and clashes with strict style usage. The **Image – Anchor** setting here determines the default anchor type for newly inserted images.

See `fig02.png`.

## Grid, Basic Fonts, and Print

**Snap to grid** on the **Grid** page is handy when you're aligning frames or graphics — configure the resolution and subdivision to taste. The **Basic Fonts (Western)** page sets default fonts and sizes for paragraph text, headings, lists, captions, and indexes; these apply to new documents unless overridden by a template. Hit **Default** to restore the original values. On the **Print** page, you can choose what gets printed — images, form controls, page backgrounds, hidden text — and whether to print only left or right pages for manual duplexing. The **Print text in black** option forces color text to print as black, useful for monochrome printers.

## Table Options

The **Table** page sets defaults for new tables: whether they get a heading row, borders, and whether **Do not split** prevents rows from breaking across pages. **Number recognition** auto-formats numbers, dates, and currency in table cells — convenient if your tables hold data, but potentially annoying if you want numbers treated as plain text. The **Keyboard Handling** section defines how much cells move or resize when you nudge them with keyboard shortcuts, and the **Behavior of rows/columns** setting (Fixed, Fixed proportional, Variable) controls how resizing ripples through adjacent columns or the whole table.

## Changes and Comparison

If you use change tracking, the **Changes** page lets you customize how insertions, deletions, and changed attributes appear — pick attributes like underline or strikethrough, and assign colors by author or a fixed color. Change bars in the margin mark every altered line. The **Comparison** page configures **Edit > Track Changes > Compare Document**, letting you compare by word or by character and optionally ignore pieces of a certain length.

## Compatibility

The **Compatibility** page matters most when you exchange documents with Microsoft Word users. Options like *Add spacing between paragraphs and tables*, *Add paragraph and table spacing at tops of pages*, and *Use printer metrics for document formatting* help Writer mimic Word's layout behavior. If you're unsure, leave the defaults — they're tuned for best results. Click **Use as Default** to apply your choices to all future documents.

## AutoCaption and Mail Merge Email

Finally, the **AutoCaption** page lets Writer automatically insert captions whenever you add a table, image, frame, or OLE object — pick the object type, set a category like "Figure" or "Table," and choose numbering and separator styles. The **Mail Merge Email** page stores your outgoing mail server details for sending form letters directly from Writer.

---

## UI Reference  —  Tools Menu

_Scope: Options > LibreOffice Writer sub-tree (General, View, Formatting Aids, Table, Changes)_

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


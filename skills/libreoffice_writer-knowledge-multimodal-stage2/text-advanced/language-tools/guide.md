# Built-in Language Tools (LibreOffice Writer 7.3.7)

Writer has a handful of built-in language tools that make life easier when you're working with multilingual documents or just want spelling and grammar checks to target the right language. The key idea is simple: you can tag any chunk of text — a word, a paragraph, or the whole document — with a specific language, and Writer will use the matching dictionaries for spell-checking, hyphenation, and AutoCorrect.

The main hub for this is **Tools > Language** on the menu bar. It gives you three scopes to choose from: **For Selection** applies the language to whatever text you've highlighted, **For Paragraph** targets the paragraph where your cursor sits, and **For All Text** changes the language for the entire document, including anything you type going forward. If the language you need isn't listed in the submenu, just click **More...** to open the Character dialog and pick from the full list. There's also a handy **Reset to Default Language** option that snaps everything back to whatever you set in **Tools > Options**.

See `fig01.png`.

You can also set the default language for new documents (or just the current one) via **Tools > Options > Language Settings > Languages**. Under *Default Languages for Documents*, pick your Western, Asian, or Complex text layout language. Be careful here — changes apply to all future documents unless you tick the **For the current document only** checkbox.

See `fig02.png`.

If the spelling checker doesn't seem to work for a particular language, look for a checkmark symbol next to it in the language list. No checkmark means no dictionary is installed — you can grab one through **Tools > Language > More Dictionaries Online**.

Sometimes you don't want spell-checking at all for certain text — code snippets, URLs, that kind of thing. Set the language for those passages to **None (Do not check spelling)** and Writer will skip right over them.

For paragraph-level control, you can bake a language right into a paragraph style. Open the style, go to the **Font** tab, and set the **Language** dropdown. This is great when you have a document mixing, say, English and French body text — just create styles like "Text Body-EN" and "Text Body-FR" and apply them as needed.

See `fig03.png`.

Finally, the quickest way to check or change the language is right on the **Status bar** at the bottom of the window. It shows the current language next to the page style. Click it to get a menu where you can switch languages for the selection or paragraph, toggle off spell-checking, or reset to the default — all without diving into any dialogs.

---

## UI Reference  —  Status Bar

_Scope: Language segment: click to change language for selection/paragraph or set to None_

The status bar runs across the bottom of the window. Every segment is interactive.

Read the screenshot `ui-status-bar.png` in this directory.

## Segments (left to right)

- **Page Number** ("Page 1 of 1") — Left-click opens Go to Page dialog (page number spinner). Right-click shows bookmark list.

- **Word / Character Count** ("0 words, 0 characters") — Left-click opens Word Count dialog showing Words, Characters (incl/excl spaces), Comments for both selection and whole document.

- **Page Style** ("Default Page Style") — Left-click opens the Page Style dialog (9 tabs: Organizer, Page, Area, Transparency, Header, Footer, Borders, Columns, Footnote). Right-click shows quick-change list of all page styles: Default Page Style, First Page, Left Page, Right Page, Envelope, Index, HTML, Footnote, Endnote, Landscape.

- **Language** ("English (USA)") — Click opens language popup: current language (checked), None (no spell-check), Reset to Default Language, More…, Set Language for Paragraph (►).

- **Selection Mode** — Click opens radio-button popup: Standard selection, Extending selection, Adding selection, Block selection.

- **View Layout buttons** — Three icons:
  - Single-page view (one page at a time)
  - Multiple-page view (pages side by side)
  - Book view (two-page spread)

- **Zoom controls** — Zoom Out (−) button, drag slider, Zoom In (+) button.

- **Zoom Percentage** ("100%") — Left-click opens Zoom & View Layout dialog (Optimal, Fit width and height, Fit width, 100%, Custom; View Layout: Automatic, Single page, Columns, Book mode). Right-click shows quick-pick presets: Entire Page, Page Width, Optimal View, 50%–200%.

---

## UI Reference  —  Tools Menu

_Scope: Language submenu: For Selection/Paragraph/All Text, More Dictionaries Online…_

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


# Built-in Language Tools (LibreOffice Writer 7.3.7)

Writer has a handful of built-in language tools that make life easier when you're working with multilingual documents or just want spelling and grammar checks to target the right language. The key idea is simple: you can tag any chunk of text — a word, a paragraph, or the whole document — with a specific language, and Writer will use the matching dictionaries for spell-checking, hyphenation, and AutoCorrect.

The main hub for this is **Tools > Language** on the menu bar. It gives you three scopes to choose from: **For Selection** applies the language to whatever text you've highlighted, **For Paragraph** targets the paragraph where your cursor sits, and **For All Text** changes the language for the entire document, including anything you type going forward. If the language you need isn't listed in the submenu, just click **More...** to open the Character dialog and pick from the full list. There's also a handy **Reset to Default Language** option that snaps everything back to whatever you set in **Tools > Options**.

The Tools menu is shown open with the Language submenu expanded. The Language flyout lists three scope options — For Selection, For Paragraph, and For All Text — each with its own submenu arrow. The For Selection submenu is visible, showing language choices including English (Australia), English (USA) (which has a checkmark indicating it is currently active), None (Do not check spelling), Reset to Default Language, and More…. Below the three scope options, the Language submenu also shows Hyphenation…, grayed-out Chinese Conversion… and Hangul/Hanja Conversion… entries, and a More Dictionaries Online… link.

You can also set the default language for new documents (or just the current one) via **Tools > Options > Language Settings > Languages**. Under *Default Languages for Documents*, pick your Western, Asian, or Complex text layout language. Be careful here — changes apply to all future documents unless you tick the **For the current document only** checkbox.

The Default Languages for Documents section from the Options dialog is shown. It contains three dropdown rows: Western (set to "English (USA)" with a small spell-check icon), Asian (checked and set to "[None]"), and Complex text layout (checked and set to "[None]"). Below the dropdowns is an unchecked "For the current document only" checkbox. A separate "Enhanced Language Support" section appears beneath, with an unchecked "Ignore system input language" checkbox.

If the spelling checker doesn't seem to work for a particular language, look for a checkmark symbol next to it in the language list. No checkmark means no dictionary is installed — you can grab one through **Tools > Language > More Dictionaries Online**.

Sometimes you don't want spell-checking at all for certain text — code snippets, URLs, that kind of thing. Set the language for those passages to **None (Do not check spelling)** and Writer will skip right over them.

For paragraph-level control, you can bake a language right into a paragraph style. Open the style, go to the **Font** tab, and set the **Language** dropdown. This is great when you have a document mixing, say, English and French body text — just create styles like "Text Body-EN" and "Text Body-FR" and apply them as needed.

The Paragraph Style dialog is shown, titled "Paragraph Style: Heading 2," with the Font tab selected (highlighted in blue among a row of tabs including Organizer, Indents & Spacing, Alignment, Text Flow, Font, Font Effects, Position, Highlighting, Outline & Numbering, Tabs, Drop Caps, Area, Transparency, and Borders). The Font tab displays three columns: Family (set to "Liberation Sans"), Typeface (set to "Bold"), and Size (set to "14 pt"), each with a scrollable list below. At the bottom of the dialog, highlighted with a red rectangle, is the Language dropdown set to "English (USA)" — this is where the language for the paragraph style is configured.

Finally, the quickest way to check or change the language is right on the **Status bar** at the bottom of the window. It shows the current language next to the page style. Click it to get a menu where you can switch languages for the selection or paragraph, toggle off spell-checking, or reset to the default — all without diving into any dialogs.

---

## UI Reference  —  Tools Menu

_Scope: Language submenu: For Selection/Paragraph/All Text, More Dictionaries Online_

The Tools menu provides document proofing, language settings, automation, and application-wide configuration.

The Tools dropdown menu is shown fully expanded in the menu bar. From top to bottom, the entries are: Spelling…, Automatic Spell Checking (with a checked checkbox), Thesaurus… (grayed out), Language, Word Count…, Accessibility Check…, Automatic Accessibility Checking (unchecked), AutoCorrect, AutoText…, ImageMap (grayed out), Redact, Auto-Redact, Heading Numbering…, Line Numbering…, Footnote/Endnote Settings…, Mail Merge Wizard…, Bibliography Database, Address Book Source…, Update, Protect Document, Calculate (grayed out), Sort… (grayed out), Macros, Development Tools (unchecked), XML Filter Settings…, Extensions…, Customize…, and Options… at the bottom.

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

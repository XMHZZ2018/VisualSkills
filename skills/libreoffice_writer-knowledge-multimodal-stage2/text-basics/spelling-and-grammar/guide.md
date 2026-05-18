# Checking Spelling and Grammar (LibreOffice Writer 7.3.7)

LibreOffice Writer comes with four built-in dictionaries per language: a spelling checker, grammar checker, hyphenation dictionary, and thesaurus. The spelling checker flags words not found in its dictionary, while the grammar checker works alongside it to catch structural errors.

To have Writer check spelling as you go, head to **Tools > Automatic Spell Checking** on the Menu bar, or toggle the same icon on the Standard Toolbar. You can also enable it under **Tools > Options > Language Settings > Writing Aids** and tick **Check spelling as you type**. Once active, misspelled words get a wavy red underline. Right-click a flagged word to see suggested corrections, choose **Ignore** or **Ignore All** to skip it, or hit **Add to Dictionary** to teach Writer the word is valid. The **Always correct to** submenu lets you save a correction as a permanent AutoCorrect replacement.

See `fig01.png`.

For a more thorough sweep, run the full checker with **Tools > Spelling** or press **F7**. This opens the Spelling dialog, which walks through the document from the cursor onward (and wraps back to the start when it reaches the end). The dialog shows the unrecognized word in context, lists suggestions below, and gives you buttons to **Ignore Once**, **Ignore All**, **Add to Dictionary**, **Correct**, or **Correct All**. If you edit the sentence directly in the upper pane, the replacement reflects your edit. **Always Correct** works like AutoCorrect, remembering the fix for next time. The **Options** button opens dictionary and rule settings.

See `fig02.png`.

Grammar errors show up as a wavy blue underline when **Check grammar as you type** is enabled in **Tools > Options > Language Settings > Writing Aids** (Automatic Spell Checking must also be on). Right-clicking a grammar error displays a context menu whose first entry describes the broken rule, sometimes with an **Explanations** link to a web page with more detail. The Spelling dialog handles grammar too — just tick **Check grammar** in its lower-left corner, and grammatical issues appear in a colored bar below the text language selector, with a **More…** link for additional info.

For deeper grammar coverage, open **Tools > Options > Language Settings > English Sentence Checking** or go to **Tools > Extension Manager**, select **English spelling dictionaries**, and click **Options**. The English Sentence Checking page lets you toggle rules for capitalization, word duplication, parentheses matching, word and sentence spacing, quotation marks, apostrophes, dashes, and more. After changing these settings, restart LibreOffice or reload the document for them to take effect.

See `fig03.png`.

---

## UI Reference  —  Tools Menu

_Scope: Spelling… (F7), Automatic Spell Checking (Shift+F7)_

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


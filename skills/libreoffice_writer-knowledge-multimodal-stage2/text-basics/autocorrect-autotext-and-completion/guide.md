# AutoCorrect, Word Completion, and AutoText (LibreOffice Writer 7.3.7)

Writer's AutoCorrect feature ships with a big list of common misspellings, typos, and special-character codes that it fixes on the fly as you type. It's on by default. If it ever gets in your way, you can disable it entirely by unchecking **Tools > AutoCorrect > While Typing**.

To customize what gets corrected, open **Tools > AutoCorrect > AutoCorrect Options** and head to the **Replace** tab. You'll see two columns — the typo on the left, its replacement on the right. Delete any pair you don't want by selecting it and clicking **Delete**, or add your own by typing into the **Replace** and **With** boxes and clicking **New**. This is also handy for inserting special characters: for instance, typing `:smiling:` can auto-replace with ☺.

See `fig01.png`.

Word Completion is a separate feature that watches what you type and offers to finish long words for you. Once you've typed a word at least twice in a document, Writer will suggest it in future — just press **Enter** to accept or keep typing to ignore. You can turn it off via **Tools > AutoCorrect > AutoCorrect Options**, then the **Word Completion** tab, where you uncheck **Enable word completion**. On that same tab you can tweak the minimum word length, the maximum number of remembered words, the acceptance key (choose from **Enter**, **End**, **Tab**, or **Space bar**), and whether completions appear inline or as a hover tip via **Show as tip**.

See `fig02.png`.

AutoText lets you store reusable chunks — text, tables, graphics, fields — and recall them with a short abbreviation. To create one, type and select the content in your document, then go to **Tools > AutoText** (or press **Ctrl+F3**). Give it a name, adjust the suggested shortcut if you like, pick a category such as *My AutoText*, then click the **AutoText** button and choose **New** (to keep original formatting) or **New (text only)**. Close the dialog and you're set.

To insert an AutoText entry later, just type its shortcut and press **F3** — the full content drops right in. If you want a printable list of all your entries, navigate to **Tools > Macros > Organize Macros > Basic**, expand **Gimmicks** under *Macro From*, select **AutoText**, and click **Run**.

---

## UI Reference  —  Tools Menu

_Scope: AutoCorrect submenu (While Typing, Options…), AutoText… (Ctrl+F3)_

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


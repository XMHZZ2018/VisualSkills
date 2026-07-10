# AutoCorrect, Word Completion, and AutoText (LibreOffice Writer 7.3.7)

Writer's AutoCorrect feature ships with a big list of common misspellings, typos, and special-character codes that it fixes on the fly as you type. It's on by default. If it ever gets in your way, you can disable it entirely by unchecking **Tools > AutoCorrect > While Typing**.

To customize what gets corrected, open **Tools > AutoCorrect > AutoCorrect Options** and head to the **Replace** tab. You'll see two columns — the typo on the left, its replacement on the right. Delete any pair you don't want by selecting it and clicking **Delete**, or add your own by typing into the **Replace** and **With** boxes and clicking **New**. This is also handy for inserting special characters: for instance, typing `:smiling:` can auto-replace with ☺.

The AutoCorrect dialog is shown with the **Replace** tab selected. At the top is a language dropdown set to "English (Australia)," and five tabs are visible: Replace, Exceptions, Options, Localized Options, and Word Completion. Below the tabs are two text-entry fields labeled **Replace** and **With**, with a **Text only** checkbox checked to their right and **New** and **Delete** buttons on the far right. The main area of the dialog is a two-column scrollable list showing replacement pairs — for example, `.*(C)` maps to ©, `.*(R)` to ®, `.*(tm)` to ™, `1/2` to ½, and common typos like "abotu" to "about" and "accomodate" to "accommodate." At the bottom are **Help**, **Reset**, **Cancel**, and **OK** buttons.

Word Completion is a separate feature that watches what you type and offers to finish long words for you. Once you've typed a word at least twice in a document, Writer will suggest it in future — just press **Enter** to accept or keep typing to ignore. You can turn it off via **Tools > AutoCorrect > AutoCorrect Options**, then the **Word Completion** tab, where you uncheck **Enable word completion**. On that same tab you can tweak the minimum word length, the maximum number of remembered words, the acceptance key (choose from **Enter**, **End**, **Tab**, or **Space bar**), and whether completions appear inline or as a hover tip via **Show as tip**.

The AutoCorrect dialog is shown with the **Word Completion** tab active. On the left side, the **Enable word completion** checkbox is checked, followed by an unchecked **Append space** checkbox and a checked **Show as tip** checkbox. Below those are an **Accept with** dropdown set to the Enter key, a **Min. word length** spinner set to 8, and a **Max. entries** spinner set to 1000. On the right side, under the heading **Collected Words**, the **Collect words** checkbox is checked and a **Delete** button sits beside it. A scrollable list displays collected words alphabetically (e.g., "accepted," "addition," "Additional," "Advanced," "affected," and so on). At the bottom is an unchecked option labeled "When closing a document, remove the words collected from it from the list."

AutoText lets you store reusable chunks — text, tables, graphics, fields — and recall them with a short abbreviation. To create one, type and select the content in your document, then go to **Tools > AutoText** (or press **Ctrl+F3**). Give it a name, adjust the suggested shortcut if you like, pick a category such as *My AutoText*, then click the **AutoText** button and choose **New** (to keep original formatting) or **New (text only)**. Close the dialog and you're set.

To insert an AutoText entry later, just type its shortcut and press **F3** — the full content drops right in. If you want a printable list of all your entries, navigate to **Tools > Macros > Organize Macros > Basic**, expand **Gimmicks** under *Macro From*, select **AutoText**, and click **Run**.

---

## UI Reference  —  Tools Menu

_Scope: AutoCorrect submenu (While Typing, Options…), AutoText… (Ctrl+F3)_

The Tools menu provides document proofing, language settings, automation, and application-wide configuration.

The screenshot shows the **Tools** dropdown menu open in the LibreOffice Writer menu bar. The menu lists items from top to bottom: Spelling…, Automatic Spell Checking (with a checkbox, currently checked), Thesaurus… (grayed out), Language, Word Count…, Accessibility Check…, Automatic Accessibility Checking (unchecked checkbox), AutoCorrect (with a submenu arrow), AutoText…, ImageMap (grayed out), Redact, Auto-Redact, Heading Numbering…, Line Numbering…, Footnote/Endnote Settings…, Mail Merge Wizard…, Bibliography Database, Address Book Source…, Update, Protect Document, Calculate (grayed out), Sort… (grayed out), Macros, Development Tools (unchecked checkbox), XML Filter Settings…, Extensions…, Customize…, and Options… at the bottom.

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

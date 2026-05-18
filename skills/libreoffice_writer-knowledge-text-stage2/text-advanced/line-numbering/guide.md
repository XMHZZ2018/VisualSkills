# Line Numbering (LibreOffice Writer 7.3.7)

Line numbers in the margin are handy for legal documents, poetry, or code listings. Writer can number an entire document or just selected paragraphs, and the numbers show up when you print.

To turn on line numbering for the whole document, go to **Tools > Line Numbering** and check **Show numbering** in the top-left corner of the dialog. Hit **OK** and you're done — every line gets a number.

The Line Numbering dialog has a **Show numbering** checkbox at the top. Below it, a **View** section on the left contains drop-down and spinner fields for **Character style** (set to "Line Numbering"), **Format** (set to "1, 2, 3, …"), **Position** (set to "Left"), **Spacing** (set to "0.50 cm"), and **Interval** (set to "5 lines"). On the right, a **Count** section provides checkboxes for **Blank lines** (checked), **Lines in text frames** (unchecked), **Include header and footer** (unchecked), and **Restart every new page** (unchecked). At the bottom, a **Separator** section offers a **Text** field and an **Every** spinner (set to "3 lines").

From that same dialog you can tweak quite a bit. The **Interval** field controls how often numbers appear (every line, every 5th, every 10th — whatever you like). **Position** sets which margin the numbers sit in, and **Spacing** adjusts the gap between the number and the text. You can pick a **Character style** to change how the numbers look, and choose a **Format** (1, 2, 3 or i, ii, iii, etc.). Under **Count**, you'll find options to skip blank lines, lines in text frames, or header/footer lines, and you can choose whether numbering restarts on each new page.

If you want a visual separator between groups of lines, fill in the **Separator** section — pick some text (a short dash, say) and set how often it appears.

To disable line numbering for the whole document, edit the *Default Paragraph Style*. Open the **Styles** pane in the Sidebar, right-click **Default Paragraph Style**, choose **Modify**, go to the **Outline & List** tab, and deselect **Include this paragraph in line numbering**. Click **OK**.

The Paragraph Style: Default Paragraph Style dialog is shown with the **Outline & List** tab selected. It displays two rows of tabs along the top (Organizer, Indents & Spacing, Alignment, Text Flow, Font, Font Effects, Position, Highlighting, Tabs, Drop Caps, Area, Transparency, Borders, and Outline & List). The tab content is divided into three sections: **Outline** with an "Outline level" drop-down set to "Text Body," **Apply List Style** with a "List style" drop-down set to "No List" and an "Edit Style" button, and **Line Numbering** with an **Include this paragraph in line numbering** checkbox (currently checked), a **Restart at this paragraph** checkbox (unchecked), and a **Start with** spinner set to "1."

To enable numbering for only specific paragraphs, first disable it document-wide as described above, then select the paragraphs you want numbered. Open **Format > Paragraph** (or right-click and choose **Paragraph > Paragraph**), go to the **Outline & List** tab, and check **Include this paragraph in line numbering**. You can also disable numbering for individual paragraphs the same way — just deselect that checkbox.

If you need numbering to start at a specific value, click in the target paragraph, open the **Outline & List** tab again, make sure **Include this paragraph in line numbering** is selected, then check **Restart at this paragraph** and type the starting number in the **Start with** box.

---

## UI Reference  —  Tools Menu

_Scope: Line Numbering… dialog_

The Tools menu provides document proofing, language settings, automation, and application-wide configuration.

The Tools drop-down menu is open in the Writer menu bar. It lists entries from top to bottom: Spelling…, Automatic Spell Checking (with a checkbox, currently checked), Thesaurus… (grayed out), Language, Word Count…, Accessibility Check…, Automatic Accessibility Checking (with an unchecked checkbox), AutoCorrect, AutoText…, ImageMap (grayed out), Redact, Auto-Redact, Heading Numbering…, Line Numbering…, Footnote/Endnote Settings…, Mail Merge Wizard…, Bibliography Database, Address Book Source…, Update, Protect Document, Calculate (grayed out), Sort… (grayed out), Macros, Development Tools (with an unchecked checkbox), XML Filter Settings…, Extensions…, Customize…, and Options… at the bottom.

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

# Outlining with Paragraph Styles (LibreOffice Writer 7.3.7)

LibreOffice gives you a couple of ways to outline using paragraph styles. The most direct route is **Tools > Chapter Numbering**, where you pick a numbering style for each paragraph style to pull it into the outline hierarchy. Alternatively, you can pair each Heading style with a separate list style right from the Styles deck on the Sidebar.

If you'd rather keep things simple, just create a single list style for all your outlining. Set up the different levels on the list style's **Customize** tab manually, or pick a pre-defined pattern from the style's **Outline** tab and let Writer handle it.

Once you're working with a paragraph style that's tied to a list, pressing **Enter+Tab** adds a sub-level paragraph. The sub-level automatically picks up the numbering pattern from the list style. To promote a paragraph back up a level, hit **Enter+Shift+Tab**.

**Setting up a single paragraph style for outlining** is straightforward. First, create a list style and link it to one of the pre-defined formats on the **Outline** tab. Then pick or create a paragraph style — just avoid Heading 1–10, since those are reserved for the standard outline and mixing them up causes confusion. On the **Organizer** tab of your paragraph style, set **Next Style** to itself so new paragraphs stay in the same style. Finally, assign the list style to the paragraph style using the **Numbering** field on the style's **Outline & List** tab.

**Outline levels** are how Writer connects paragraph styles to higher-level features like the Navigator and table of contents. By default, the Heading 1–10 styles map to Outline Levels 1–10 (Heading 1 is Level 1, and so on). You can reassign or add your own paragraph styles to any outline level through the **Outline level** field on the **Outline & List** tab of the Paragraph Style dialog.

The Paragraph Style dialog is shown for the style "Index Heading," with the **Outline & List** tab selected (the rightmost tab in the second row, alongside Highlighting, Tabs, Drop Caps, Area, Transparency, and Borders). Under the **Outline** section, the **Outline level** dropdown is expanded, revealing options from "Text Body" through "Level 1" to "Level 10"; "Level 2" is currently highlighted. Below the Outline section, the dialog also shows an **Apply List Style** section with a **List style** field, and a **Line Numbering** section with checkboxes for "Include this paragraph" and "Restart at this paragraph," plus a "Start with" field.

This is especially handy when you want custom-named styles (like "Chapter Title" or "Appendix Header") to appear in the Navigator and be picked up by auto-generated tables of contents — just assign them the appropriate outline level and they'll behave just like the built-in headings.

---

## UI Reference  —  Tools Menu

_Scope: Heading Numbering… dialog_

The Tools menu provides document proofing, language settings, automation, and application-wide configuration.

The Tools menu is shown open in the LibreOffice Writer menu bar. It is a single-column dropdown listing items from top to bottom: Spelling…, Automatic Spell Checking (with a checked checkbox), Thesaurus… (grayed out), Language, Word Count…, Accessibility Check…, Automatic Accessibility Checking (unchecked checkbox), AutoCorrect, AutoText…, ImageMap (grayed out), Redact, Auto-Redact, Heading Numbering…, Line Numbering…, Footnote/Endnote Settings…, Mail Merge Wizard…, Bibliography Database, Address Book Source…, Update, Protect Document, Calculate (grayed out), Sort… (grayed out), Macros, Development Tools (unchecked checkbox), XML Filter Settings…, Extensions…, Customize…, and Options… at the bottom. Separator lines divide the menu into logical groups.

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

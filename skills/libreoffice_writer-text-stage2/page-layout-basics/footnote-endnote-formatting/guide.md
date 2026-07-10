# Formatting Footnotes and Endnotes (LibreOffice Writer 7.3.7)

Footnotes sit at the bottom of the page where they're referenced; endnotes gather at the end of the document. Both are easy to insert, but you'll probably want to tweak how they look and where exactly they land on the page. Here's how.

## Footnote Location and the Separator Line

The placement of footnotes and the style of the separator line between them and the body text are controlled at the *page style* level. Since your document might use several page styles, you may need to adjust this on each one individually.

Open the page style dialog by going to **Format > Page** on the Menu bar (or right-click the page and choose **Page** from the context menu). Switch to the **Footnote** tab to see your options.

The Page Style dialog (titled "Page Style: Default Style") opens with two rows of tabs — Organizer, Page, Area, Transparency on the top row, and Header, Footer, Borders, Columns, Footnote on the bottom row — with the **Footnote** tab selected. The tab is divided into two sections: **Footnote Area** at the top, which contains a radio button for "Not larger than page area" (selected by default), a radio button for "Maximum footnote height" with a spin box set to 2.54 cm, and a "Space to text" spin box set to 0.10 cm; and **Separator Line** below, which provides drop-downs and spin boxes for Position (set to "Left"), Style (showing a thin solid line), Thickness (0.50 pt), Color (Black), Length (25%), and Spacing to footnote contents (0.10 cm).

Under **Footnote Area**, the default **Not larger than page area** lets Writer calculate space automatically based on how many footnotes appear. If you'd rather cap it yourself, select **Maximum footnote height** and type in a value — any footnote content that doesn't fit will spill onto the next page.

The **Space to text** field controls the gap between your body text and the first footnote.

## Customizing the Separator Line

In the **Separator Line** section of that same tab, you can set the line's **Position** (left, center, or right), its **Style**, **Thickness**, **Color**, and **Length** (as a percentage of the page width). There's also a **Spacing to footnote contents** value that controls the gap between the line and the footnotes themselves.

Once everything looks right, click **OK** to save your changes. These settings apply to the current page style, so if your document uses multiple page styles, repeat the process for each one that carries footnotes.

---

## UI Reference  —  Tools Menu

_Scope: Footnote/Endnote Settings…_

The Tools menu provides document proofing, language settings, automation, and application-wide configuration.

The Tools menu is shown expanded from the Menu bar, displaying a single-column drop-down list of entries grouped by horizontal separators. From top to bottom the visible items are: Spelling…, Automatic Spell Checking (with a checked checkbox), Thesaurus… (grayed out), Language, Word Count…, Accessibility Check…, Automatic Accessibility Checking (unchecked checkbox), AutoCorrect, AutoText…, ImageMap (grayed out), Redact, Auto-Redact, Heading Numbering…, Line Numbering…, Footnote/Endnote Settings…, Mail Merge Wizard…, Bibliography Database, Address Book Source…, Update, Protect Document, Calculate (grayed out), Sort… (grayed out), Macros, Development Tools (unchecked checkbox), XML Filter Settings…, Extensions…, Customize…, and Options… at the bottom.

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

# Defining a Different First Page (LibreOffice Writer 7.3.7)

Many documents — letters, memos, reports — need a first page that looks different from the rest. A letterhead might have a unique header, or a report's first page might skip the header and footer entirely. Writer gives you a few ways to pull this off.

**The simplest approach: one page style.** If you just need different headers or footers on the first page, you can stick with the Default page style. Right-click anywhere on the page, choose **Page Style**, then go to the **Header** or **Footer** tab. Turn on **Header on** (or **Footer on**), and deselect **Same content on first page**. You can optionally deselect **Same content on left and right pages** too. Now just type your first-page header or footer content on page one, and different content on any subsequent page — Writer keeps them independent.

See `fig01.png`.

**The more flexible approach: separate page styles.** Writer ships with a built-in *First Page* style and a *Default* style that work as a pair. The idea is that the First Page style automatically flows into the Default style for every page after it. To set this up, open the Page Style dialog for the First Page style, go to the **Organizer** tab, and set the **Next style** dropdown to **Default Style**. Now your first page uses one style, and everything after it switches automatically.

See `fig02.png`.

**The quick route: title pages.** If you want to convert existing pages into title pages (or insert new ones), head to **Format > Title Page**. This dialog lets you choose how many title pages to add, where to place them, and whether to restart page numbering afterward. You can also pick which page style to apply. It's especially handy for books or long documents where you need title, copyright, and decorative pages up front before the main content begins.

See `fig03.png`.

Between these three methods — toggling first-page content within one style, chaining two page styles together, or using the Title Page feature — you can handle just about any first-page scenario Writer throws at you.

---

## UI Reference  —  Format Menu

_Scope: Title Page… dialog_

The Format menu controls text styling, paragraph formatting, page layout, and document-level formatting options.

Read the screenshot `ui-format-menu.png` in this directory.

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


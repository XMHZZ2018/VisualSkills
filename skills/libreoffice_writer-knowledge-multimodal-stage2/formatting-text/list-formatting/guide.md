# Formatting Lists (LibreOffice Writer 7.3.7)

Writer gives you two main ways to create bulleted and numbered lists: **paragraph styles** and **direct formatting**. Styles are the cleaner approach whenever possible, so let's start there.

## Using list styles

To create an unordered (bulleted) list, apply one of the built-in paragraph styles — **List 1**, **List 2**, **List 3**, and so on. These automatically pull in the Bullet list style. For ordered (numbered) lists, use **Numbering 1**, **Numbering 2**, **Numbering 3**, etc., which rely on the Numbering list styles. The paragraph styles handle the text formatting, while the attached list styles control the bullet character or number sequence.

Paragraph styles also make nested lists easy. Each style level corresponds to an outline level, so you can demote an item by pressing **Tab** at the start of the line (after the bullet or number) or promote it back up with **Shift+Tab**. Once you've set up nested levels, changing the hierarchy is effortless.

## Formatting lists directly

If you just need a quick list without fussing over styles, select your text and hit the **Toggle Unordered List** or **Toggle Ordered List** buttons on the Formatting toolbar, the Formatting (Styles) toolbar, or the Paragraph panel of the Sidebar's Properties deck. You can also open **View > Toolbars > Bullets and Numbering** for a dedicated toolbar with promote, demote, move up/down, and nesting controls.

On the toolbar, buttons let you **Promote One Level**, **Demote One Level**, **Move Up**, **Move Down**, and handle subpoints — all in one click. Keyboard shortcuts work here too: **Tab** demotes a level, **Shift+Tab** promotes. To insert a tab stop after the number, press **Ctrl+Tab**.

## Bullets and Numbering palettes on the Sidebar

Over on the Sidebar's Properties deck, click the arrow next to the **Toggle Unordered List** control to open a palette of bullet styles, or the arrow next to **Toggle Ordered List** for numbering styles. These palettes also give you quick access to the full Bullets and Numbering dialog.

See `fig01.png`.

## The Bullets and Numbering dialog

For full control, open the **Bullets and Numbering** dialog (click its button on the toolbar or Sidebar). It has six tabs: **Unordered**, **Ordered**, **Outline**, **Image**, **Position**, and **Customize**. The first four let you pick pre-defined symbols, sequences, outline schemes, or image bullets. The **Position** tab controls alignment, indent, and tab stop spacing for each level. **Customize** lets you define your own formats from scratch.

See `fig02.png` for the Position tab.

One thing to keep in mind: direct list formatting applied this way can't be removed with **Format > Clear Direct Formatting** or **Ctrl+M**. Instead, toggle it off by clicking the relevant list button again on the toolbar or Sidebar.

---

## UI Reference  —  Format Menu

_Scope: Lists submenu (Unordered/Ordered, Demote/Promote), Bullets and Numbering…_

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

---

## UI Reference  —  Formatting Toolbar

_Scope: Toggle Unordered/Ordered List, Select Outline Format, Increase/Decrease Indent_

The second toolbar row provides all character and paragraph formatting controls with split-button dropdowns.

Read the screenshot `ui-formatting-toolbar.png` in this directory.

## Elements

Row (left → right):

- **Paragraph Style** dropdown — Shows current style (e.g. "Default Paragraph Style"). Dropdown lists: Clear formatting, Default Paragraph Style, Body Text, Title, Subtitle, Heading 1–4, Block Quotation, Preformatted Text, More Styles…
- **Update Selected Style** (Shift+Ctrl+F11) — Update current style to match cursor formatting.
- **New Style from Selection** (Shift+F11) — Create a new style from current formatting.
- **Font Name** dropdown — Shows/changes the font (e.g. "Liberation Serif"). Lists all installed fonts rendered in their own typeface.
- **Font Size** dropdown — Shows/changes size in pt (6–48, plus custom values).

| *(separator)* |

- **Bold** (Ctrl+B) / **Italic** (Ctrl+I)
- **Underline** (Ctrl+U, split-button ▼) — Toggle; dropdown offers 11 underline styles (single, double, bold, dotted, dashed, wavy, etc.) plus More Options…
- **Strikethrough**
- **Superscript** (Shift+Ctrl+P) / **Subscript** (Shift+Ctrl+B)
- **Clear Direct Formatting** (Ctrl+M) — Eraser icon; removes all manual formatting.

| *(separator)* |

- **Font Color** (split-button ▼) — Applies current color; dropdown opens ~120-swatch color picker with Custom Color… option.
- **Character Highlighting Color** (split-button ▼) — Marker-pen highlight; dropdown opens color picker.

| *(separator)* |

- **Align Left** (Ctrl+L) / **Align Center** (Ctrl+E) / **Align Right** (Ctrl+R) / **Justified** (Ctrl+J)

| *(separator)* |

- **Toggle Unordered List** (Shift+F12, split-button ▼) — Bullet list; dropdown shows 8 bullet styles + Customize…
- **Toggle Ordered List** (F12, split-button ▼) — Numbered list; dropdown shows 8 numbering styles + Customize…
- **Select Outline Format** (split-button ▼) — Multi-level outline presets.
- **Increase Indent** / **Decrease Indent**

| *(separator)* |

- **Set Line Spacing** (split-button ▼) — Presets (1, 1.15, 1.5, 2) plus custom value editor.
- **Increase Paragraph Spacing** / **Decrease Paragraph Spacing**

---

## UI Reference  —  Styles Menu & Styles Panel

_Scope: Styles menu List styles section: Bullet, Numbering presets_

LibreOffice Writer uses a style-based formatting system. The Styles menu provides quick-apply shortcuts, while the Styles panel (F11) offers full management.

Read the screenshot `ui-styles-menu.png` in this directory.

## Styles Menu

The menu has three radio-button sections for quick style application:

**Paragraph styles:**
- Body Text (Ctrl+0), Title, Subtitle, Heading 1 (Ctrl+1), Heading 2 (Ctrl+2), Heading 3 (Ctrl+3), Block Quotation, Preformatted Text

**Character styles:**
- No Character Style (default), Emphasis, Strong Emphasis, Quotation, Source Text

**List styles:**
- No List (Shift+Ctrl+F12), Bullet • List Style, Numbering 123/ABC/abc/IVX/ivx List Styles

**Management commands:**
- Edit Style… (Alt+P), Update Selected Style (Shift+Ctrl+F11), New Style from Selection (Shift+F11), Load Styles from Template, Manage Styles (F11)

## Styles Panel (F11 / Alt+2)

The Styles panel in the right sidebar provides full style management:

- **Category toolbar:** Paragraph Styles, Character Styles, Frame Styles, Page Styles, List Styles, Table Styles, Fill Format Mode, Styles actions ▼
- **Style list:** Hierarchical tree of all styles (Default Paragraph Style, Body Text, Caption, Heading, Index, etc.)
- **Right-click on a style:** New…, Edit Style…, Hide, Show, Delete…
- **Show Previews** / **Spotlight** checkboxes
- **Filter dropdown:** Hierarchical, All Styles, Hidden Styles, Applied Styles, Custom Styles, Automatic, Text/Document/List/Index/Special/HTML/Conditional Styles
- **Styles actions dropdown:** New Style from Selection, Update Selected Style, Load Styles from Template


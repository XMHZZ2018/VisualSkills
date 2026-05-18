# Formatting List Styles (LibreOffice Writer 7.3.7)

LibreOffice Writer ships with several default list styles for both ordered and unordered lists. You can modify any of them or create your own from the Styles deck on the Sidebar. A handy trick: give your list style, paragraph style, and character style the same name — it makes related styles much easier to find later.

There are two ways to format a list. The quick way is to pick a preset from the **Unordered**, **Ordered**, **Outline**, or **Image** tabs of the List Style dialog. For full control, switch to the **Customize** and **Position** tabs, which let you configure up to ten levels independently.

To set up an ordered list, open the **Customize** tab and pick a numbering scheme from the **Number** drop-down — options include Arabic numerals, upper/lower case letters, and Roman numerals. You can add text before or after the number using the **Before** and **After** fields (a closing parenthesis is common). The **Show sublevels** field controls how many outline levels appear, so setting it to 3 would produce numbering like 1.1.1. The **Character style** field defaults to *Numbering Symbols* for numbered lists and *Bullets* for bulleted ones; change it if you want a different font, size, or color for the numbers or bullets.

See `fig01.png`.

For unordered lists, you can swap the default bullet character via the **Character** field on the **Customize** tab, which opens a symbol picker for the current font. If you'd rather use a graphic, choose **Graphics** or **Linked Graphics** from the **Number** drop-down, then pick an image from the Gallery or a file. Set the **Width**, **Height**, and **Alignment** to taste — enable **Keep ratio** so the image scales proportionally.

The **Position** tab is where you dial in spacing and indents. **Aligned at** sets where the number or bullet sits (measured from the left margin). **Numbering alignment** controls whether the number is left-, center-, or right-aligned at that point. **Numbering followed by** determines the space between the number and the text — choose Tab stop, Space, or Nothing. Finally, **Indent at** sets where the text itself begins. For most lists, leave the level at 1 unless you're building a multi-level outline.

See `fig02.png`.

When a list style is linked to a paragraph style, changes you make on the **Position** tab automatically flow through to the paragraph's **Indents & Spacing** settings. The reverse is also true, but editing position from the list style side avoids the negative *First Line* values that paragraph-side changes can introduce.

Numbers with two digits can push list text out of alignment. To fix this, either add a bit more space in the **Indent at** field, adjust the number size through a character style, or set **Numbering Alignment** to **Right** so single- and double-digit numbers line up neatly on their trailing edge.

See `fig03.png`.

To connect everything, create a paragraph style for your list items and go to its **Outline & List** tab. Pick your list style from the **List style** drop-down and click **OK**. Now just apply that paragraph style to any text, and the list formatting follows automatically. If numbering in a subsequent list continues from a previous one and you want to restart at 1, right-click and choose **List > Restart numbering**.

---

## UI Reference  —  Format Menu

_Scope: Bullets and Numbering… dialog_

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

_Scope: List split-button dropdowns with Customize… option_

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


# Applying and Naming List Styles (LibreOffice Writer 7.3.7)

List styles handle properties like indentation, numbering format (1, 2, 3 or a, b, c or bullets), and punctuation after the number. They don't control font, borders, or text flow — those belong to paragraph styles.

You *can* apply list styles from the **Styles** menu on the Menu bar or the Styles deck on the Sidebar, but that's not recommended. Instead, pair list styles with paragraph styles — Writer ships with two sets designed for exactly this.

For unordered lists, use the paragraph styles **List 1**, **List 2**, **List 3**, and so on. These rely on Bullet list styles under the hood. For ordered lists, use **Numbering 1**, **Numbering 2**, **Numbering 3**, etc., which map to the list styles Numbering 1, Numbering 2, and so on.

Writer includes several predefined list styles with different bullet symbols or number sequences (1-2-3, a-b-c, A-B-C, and more). You can redefine any of them — changing the numbering or bullet symbol, the indentation — or create entirely new series of your own.

Lists can nest up to ten levels deep. To move between levels, use the **Promote One Level** or **Demote One Level** icons on the Bullets and Numbering toolbar, press **Tab** (demote) or **Shift+Tab** (promote), or right-click the list element and choose **List > Promote One Level** or **Demote One Level**.

When you have more than one ordered list of the same type in a chapter, Writer sequentially numbers them all by default. Sometimes that's what you want — say, when illustrations sit between list items. Other times you need the numbering to start fresh.

To restart numbering, right-click the paragraph and select **List > Restart Numbering**, or open the **Restart at this paragraph** option in the Numbering section of the Paragraph dialog (**Format > Paragraph…**). See `fig01.png` for the Paragraph dialog with restart numbering option.

---

## UI Reference  —  Formatting Toolbar

_Scope: Toggle Unordered/Ordered List buttons, indent controls for list level changes_

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

_Scope: List Styles category; Styles menu list style entries_

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


# Applying and Naming List Styles (LibreOffice Writer 7.3.7)

List styles handle properties like indentation, numbering format (1, 2, 3 or a, b, c or bullets), and punctuation after the number. They don't control font, borders, or text flow — those belong to paragraph styles.

You *can* apply list styles from the **Styles** menu on the Menu bar or the Styles deck on the Sidebar, but that's not recommended. Instead, pair list styles with paragraph styles — Writer ships with two sets designed for exactly this.

For unordered lists, use the paragraph styles **List 1**, **List 2**, **List 3**, and so on. These rely on Bullet list styles under the hood. For ordered lists, use **Numbering 1**, **Numbering 2**, **Numbering 3**, etc., which map to the list styles Numbering 1, Numbering 2, and so on.

Writer includes several predefined list styles with different bullet symbols or number sequences (1-2-3, a-b-c, A-B-C, and more). You can redefine any of them — changing the numbering or bullet symbol, the indentation — or create entirely new series of your own.

Lists can nest up to ten levels deep. To move between levels, use the **Promote One Level** or **Demote One Level** icons on the Bullets and Numbering toolbar, press **Tab** (demote) or **Shift+Tab** (promote), or right-click the list element and choose **List > Promote One Level** or **Demote One Level**.

When you have more than one ordered list of the same type in a chapter, Writer sequentially numbers them all by default. Sometimes that's what you want — say, when illustrations sit between list items. Other times you need the numbering to start fresh.

To restart numbering, right-click the paragraph and select **List > Restart Numbering**, or open the **Restart at this paragraph** option in the Numbering section of the Paragraph dialog (**Format > Paragraph…**). The Paragraph dialog is shown with the "Outline & List" tab selected (among tabs including Indents & Spacing, Alignment, Text Flow, Tabs, Drop Caps, Borders, Area, and Transparency). The lower section of this tab, highlighted with a red border, is labeled "Apply List Style" and contains a "List style" dropdown set to "Numbering 1" with an "Edit Style" button beside it, a checked "Restart numbering at this paragraph" checkbox, and beneath it a checked "Start with" checkbox with a spin box set to the value 1.

---

## UI Reference  —  Styles Menu & Styles Panel

_Scope: Styles menu: List styles (Bullet, Numbering 123/ABC/abc/IVX/ivx)_

LibreOffice Writer uses a style-based formatting system. The Styles menu provides quick-apply shortcuts, while the Styles panel (F11) offers full management.

The Styles dropdown menu is open from the Menu bar (visible between Format and Table). It displays three groups of radio-button entries arranged vertically. The first group lists paragraph styles: Body Text, Title, Subtitle, Heading 1, Heading 2, Heading 3, Block Quotation, and Preformatted Text. The second group lists character styles: No Character Style (selected), Emphasis, Strong Emphasis, Quotation, and Source Text. The third group lists list styles: No List (selected), Bullet • List Style, Numbering 123 List Style, Numbering ABC List Style, Numbering abc List Style, Numbering IVX List Style, and Numbering ivx List Style. Below the radio buttons, five management commands appear: Edit Style…, Update Selected Style, New Style from Selection, Load Styles from Template, and Manage Styles.

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

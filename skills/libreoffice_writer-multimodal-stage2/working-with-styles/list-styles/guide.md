# Working with List Styles (LibreOffice Writer 7.3.7)

List styles work hand-in-hand with paragraph styles to control indentation, alignment, and the bullet or numbering characters used for list items. You can define anything from a simple bulleted list to a complex multi-level nested outline. The big advantage over manually formatting lists with the **Toggle Ordered List** or **Toggle Unordered List** toolbar buttons is consistency — change the style once, and every list using it updates automatically.

To create a new list style, open the **Styles** deck in the sidebar, switch to the **List Styles** tab, right-click in the list, and choose **New Style**. The dialog that opens has six tabs beyond the usual **Organizer**: **Unordered**, **Ordered**, **Image**, **Outline**, **Position**, and **Customize**.

The **Unordered**, **Ordered**, and **Image** tabs offer predefined bullet and numbering formats. Just click the one you want — a thick border highlights your selection. The **Image** tab works the same way but uses small graphics instead of font characters.

The **Outline** tab gives you eight predefined nested-list layouts. Pick one as a starting point, then refine it with the **Position** and **Customize** tabs.

On the **Position** tab you dial in the spacing and alignment for each level. **Aligned at** sets how far the numbering symbol sits from the left margin. **Numbering alignment** (Left, Right, or Centered) controls how the symbol itself is justified at that position. **Numbering followed by** lets you choose a tab stop, a space, or nothing after the number. Finally, **Indent at** sets where the actual text of the list item begins. You can adjust these per level or select **1 – 10** to change all levels at once.

See `fig01.png`.

The **Customize** tab is where you define what each level actually looks like. Select a level on the left (or **1 – 10** for all), then set the **Number** format, **Start at** value, **Character style**, and how many **Show sublevels** to display. The **Separator** fields let you add text before or after the number — handy for formats like "(1)" or "Section 1.2". Check **Consecutive numbering** at the bottom if you want numbering to continue across levels rather than restarting.

See `fig02.png`.

Once your list style is ready, apply it by assigning it to a paragraph style via the paragraph style's **Outline & List** tab, or by selecting text and double-clicking the list style in the Styles deck. For details on how list styles and paragraph styles interact in more advanced scenarios, see Chapter 12 of the Writer Guide.

---

## UI Reference  —  Styles Menu & Styles Panel

_Scope: List Styles category in Styles panel toolbar_

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


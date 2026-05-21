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

## UI Reference  —  Styles Menu & Styles Panel

_Scope: List Styles in Styles panel: right-click Edit Style… to format_

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


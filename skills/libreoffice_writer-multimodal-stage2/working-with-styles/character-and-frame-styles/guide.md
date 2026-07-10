# Working with Character and Frame Styles (LibreOffice Writer 7.3.7)

Character styles override the formatting within a paragraph style. They apply to groups of characters — words, phrases, or even individual letters — rather than whole paragraphs. Reach for a character style whenever you want to change the appearance of part of a paragraph without affecting the rest. Common examples include **bold**, *italic*, colored words, or a different typeface.

Beyond simple formatting, character styles are handy for chapter numbers, page numbers, list numbers larger than surrounding text, and formatted hyperlinks. You can also assign a language to a character style so that, say, French words in an English document get spell-checked with the right dictionary.

## Creating a new character style

The Character Styles dialog looks a lot like the one for paragraph styles. Open the **Styles** deck in the Sidebar, right-click in the character styles list, and choose **New Style**. On the **Organizer** tab, name your style and set its hierarchical level. The **Font** tab lets you pick the font, style, and size — you can specify size as a percentage or point increase/decrease relative to the paragraph font, and you can set the language for correct spell-checking.

The **Font Effects** tab is where things get interesting: font color, underlining, relief, strikethrough, and more. If you frequently use hidden text, define a character style with the **Hidden** option marked — relief effects work nicely for drop caps or chapter-number emphasis too. Use the **Highlighting** tab to apply a colored background (same result as the **Highlight Color** tool on the Standard toolbar). The **Borders** tab adds a border and shadow, and the **Position** tab handles subscript, superscript, rotation, condensed, and expanded text.
Note that when rotating characters, you need to specify whether the rotated text fits within the line or is allowed to expand above and below it. This property is active only for character styles, not paragraph styles.

## Working with frame styles

Frames are containers for text or graphics. To keep their appearance consistent, define frame styles — for instance, photographs in a drop-shadowed border, line drawings in a plain border, or marginal notes without a border but with a shaded background. Writer ships with several predefined frame styles: **Frame**, **Formula**, **Graphics**, **Labels**, **Marginalia**, **OLE**, and **Watermark**. You can modify any of these or create new ones.
When you add an object to Writer, it's automatically wrapped in a frame of a predefined type. The frame controls placement on the page and interaction with surrounding elements. You can edit the frame by modifying its style or by applying a manual override. To format a frame manually, select **Insert > Frame** on the Menu bar — the dialog that opens contains all the settings available when frame styles are set up, plus a few that only appear when the frame is already inserted.

If you work with a mix of graphics, consider defining two related styles: one with a border for images on white backgrounds, and one without a border for everything else. Beyond that, the default frame styles generally cover most needs — you may just want to add a style or two for text frames.

---

## UI Reference  —  Styles Menu & Styles Panel

_Scope: Character Styles and Frame Styles categories in Styles panel toolbar_

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


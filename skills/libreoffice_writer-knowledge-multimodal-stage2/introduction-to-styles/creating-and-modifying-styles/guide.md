# Creating, Modifying, and Deleting Styles (LibreOffice Writer 7.3.7)

Writer ships with plenty of predefined styles, but you'll often want to tweak them or build your own. Any style you create or modify lives inside the document where you made it — to reuse it elsewhere, save it into a template or load it from one.

There are several ways to create or change a style: from a selection, via the Style dialog, by loading styles from another document, or even by dragging a text selection into the Styles deck. Let's walk through each.

**Creating a style from a selection** is the fastest route. Format a paragraph (or frame, or other object) exactly how you want it, select it, then open the Styles deck in the Sidebar. Click the **Styles actions** icon at the top and choose **New Style from Selection**. Give it a name, hit **OK**, and you're done.

See `fig01.png`.

**Updating an existing style from a selection** works similarly. Format a paragraph the way you want the style to look, click in it, select the target style in the Styles deck, then click **Styles actions > Update Selected Style**. Just make sure every property in your paragraph is uniform — mixed font sizes, for instance, won't carry over.

**Loading styles from a template or another document** lets you pull in whole sets of styles at once. Click **Styles actions > Load Styles from Template**, pick a template (or click **From File** to browse for a regular document), tick the style categories you want — Paragraph and Character, Frame, Page, Numbering, List — and choose whether to **Overwrite** existing styles of the same name. Click **OK** to import them.

**Changing a style through the Style dialog** gives you full control. Right-click any style in the Styles deck and choose **Modify** (or **New** to create one from scratch). The dialog's Organizer tab is where you set the style's name, the Next Style that kicks in when you press Enter, and the Inherit from field that chains it to a parent style. The remaining tabs — Indents & Spacing, Alignment, Font, and so on — cover every formatting property.

See `fig02.png`.

**Deleting styles** is straightforward but limited: you cannot remove any of Writer's predefined styles. Custom styles can be deleted by selecting them in the Styles deck (hold Ctrl for multiples), right-clicking, and choosing **Delete**. If the style is in use, Writer warns you first; objects using it will revert to the parent style, though some manual formatting may linger.

**Worked example — Poem and PoemHeading styles.** To create a *Poem* paragraph style, open the Styles deck, right-click **Default Paragraph Style**, and choose **New**. On the Organizer tab, name it "Poem", set Next Style to "Poem", Inherit from to "– None –", and Category to **Custom Styles**. On the **Alignment** page choose **Center**, and on the **Font** page set the size to **12pt**. Click **OK**. For a companion *PoemHeading* style, repeat the process but name it "PoemHeading", set Next Style to "Poem" (so pressing Enter drops you into the poem body), Inherit from to "Heading", and on the Font page pick **Bold** at **14pt**. Now if you want to restyle every poem later — say, left-aligned instead of centered — just right-click the style, choose **Modify**, and change the alignment. Every paragraph using that style updates instantly across the entire document.

See `fig03.png` for the initial configuration of the Poem style.

---

## UI Reference  —  Styles Menu & Styles Panel

_Scope: Styles actions: New Style from Selection, Update Selected Style, Load from Template; right-click New/Edit/Delete_

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


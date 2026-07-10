# Creating Custom Styles (LibreOffice Writer 7.3.7)

Beyond the predefined styles that ship with LibreOffice, you can create your own custom styles to match your specific formatting needs. There are three ways to do this: drag-and-drop, the **New Style from Selection** icon on the Styles deck, and the Style dialog. The first two are quick and convenient because you can preview the results as you go, but if you want full control over the style — including its relationship to other styles — the Style dialog is the way to go.

To use the Style dialog, open the Styles deck on the Sidebar and pick the category of style you want (paragraph, character, etc.) by clicking the appropriate icon at the top. Then right-click anywhere in the styles list and choose **New** from the context menu. The dialog that appears depends on the style type you selected.

See `fig01.png`.

The **Organizer** tab is common to virtually all style categories and is where you set the essentials. Give your style a meaningful name in the **Name** field. The **Next Style** field (paragraph and page styles only) controls which style is automatically applied to the next element — handy for things like having a heading automatically followed by body text. **Inherit from** sets the parent style your new style will be based on; any properties you don't explicitly override are pulled from that parent. And **Category** lets you file it under one of the groups shown in the Styles deck for easier filtering.

If **AutoUpdate** is checked (available for paragraph and frame styles), be careful — Writer will push any manual formatting you apply to a paragraph right back into the style definition itself, which can unexpectedly reformat other parts of your document.

Style inheritance is a powerful concept here. When your new style inherits from a parent, changes to the parent cascade down to all child styles automatically. For example, if every heading style inherits from a common "Heading" parent, changing the font color on that parent updates all heading levels at once. Note, though, that any property you explicitly set on a child style won't be overridden by parent changes. You can always check which properties are unique to a style by looking at the **Contains** section on the Organizer tab, and hitting the **Standard** button at the bottom of the dialog resets a child style back to its parent's defaults.

See `fig02.png` for the hierarchical view showing style inheritance between Heading styles.

---

## UI Reference  —  Styles Menu & Styles Panel

_Scope: Styles panel right-click New…, Styles actions > New Style from Selection_

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


# Understanding Styles (LibreOffice Writer 7.3.7)

Most people format text by picking a font, size, and weight directly — say, Helvetica 12pt bold. Styles flip that approach: instead of describing *how* text looks, you label *what* it is. You assign a name like "Title" or "Heading 1" and let Writer handle the appearance. The payoff is that when you change a style's definition, every paragraph using it updates instantly — no hunting through a long document to fix each heading by hand.

Styles also unlock Writer's more powerful features. A well-styled document can auto-generate a table of contents, maintain consistent indentation, and keep your headings in a clear hierarchy without any extra effort.

Writer organizes styles into six categories. **Paragraph styles** cover entire paragraphs and are by far the most common — headings, body text, footers, and list items are all paragraph styles. **Character styles** handle inline formatting within a paragraph, like a bold keyword or a hyperlink. **Page styles** control page-level layout (size, margins, orientation). **Frame styles** govern frames and images, **List styles** manage numbered and bulleted lists, and **Table styles** set the look of tables of data.

One thing to watch out for: manual formatting (also called "direct formatting") always wins over a style. If you bold a word by hand and then change the style, that manual bold sticks around. To strip it, select the text, then go to **Format > Clear Direct Formatting** on the Menu bar — or just right-click and choose **Clear Direct Formatting** from the context menu. The keyboard shortcut is **Ctrl+M**.

To work with styles, open the Styles deck in the Sidebar. You can get there a few ways: click the **Styles** icon on the Sidebar, choose **Styles > Manage Styles** from the Menu bar, or press **F11** (**⌘+T** on macOS). Six icons along the top of the deck let you switch between the style categories — click one to see all available styles of that type.
From the Styles deck you can apply an existing style (just double-click it), modify one to change its formatting, or create a brand-new style from scratch. It's the central hub for keeping your document's look consistent and easy to update.

---

## UI Reference  —  Right Sidebar

_Scope: Styles panel: category toolbar icons, hierarchical style list, filter dropdown_

The collapsed right sidebar is a vertical strip of 8 icon buttons along the right edge of the window. Each opens a full docked panel. Toggle the sidebar with Ctrl+F5 or View > Sidebar.

The screenshot shows the full LibreOffice Writer window with an empty document open. Along the far-right edge of the window, a narrow vertical toolbar is visible containing eight small icon buttons stacked top to bottom; the topmost button (Properties, Alt+1) is highlighted with a red rectangle to call attention to the sidebar's location. A tooltip reading "Properties (Alt+1)" is displayed next to that button. The main document area, menu bar, standard toolbar, and formatting toolbar occupy the rest of the window to the left of this sidebar strip.

## Panel Buttons (top to bottom)

- **Properties** (Alt+1) — Formatting panel with three collapsible sections:
  - *Style:* Paragraph style dropdown, Clone Formatting, Update/New Style buttons.
  - *Character:* Font family, size, Bold/Italic/Underline/Strikethrough, Font Color, Highlighting, Change Case, Super/Subscript.
  - *Paragraph:* Alignment, lists/indent toolbar, line spacing, above/below spacing fields, left/right/first-line indent.

- **Styles** (Alt+2 / F11) — Full style manager: category toolbar (Paragraph/Character/Frame/Page/List/Table Styles), hierarchical style list, Fill Format Mode, filter dropdown. See [Styles](styles.md).

- **Gallery** (Alt+3) — Clip-art browser: categories (Arrows, BPMN, Bullets, Diagrams, Flow chart, Icons), thumbnail grid, Icon/Detailed view, New… button.

- **Navigator** (Alt+4 / F5) — Document structure tree: Headings, Tables, Frames, Images, OLE objects, Bookmarks, Sections, Hyperlinks, References, Indexes, Comments, Drawing objects, Fields, Footnotes, Endnotes. Includes page navigation controls and drag-mode options.

- **Page** (Alt+5) — Page layout panel:
  - *Format:* Size (A4), Width/Height, Orientation (Portrait/Landscape), Margins.
  - *Styles:* Page number format, Background, Layout, Columns.
  - *Header/Footer:* Enable toggles, margins, spacing, same-content options.

- **Style Inspector** (Alt+6) — Two-column Properties/Value tree showing all applied styles: Paragraph Styles, Paragraph Direct Formatting, Character Styles, Character Direct Formatting (50+ properties per node).

- **Manage Changes** (Alt+7) — Two tabs:
  - *List:* Action/Author/Date/Comment table with Accept/Reject/Accept All/Reject All buttons.
  - *Filter:* Date range, Author, Action, Comment filters.

- **Accessibility Check** (Alt+8) — Runs an accessibility audit and lists issues by category, each with a Fix… button.

---

## UI Reference  —  Styles Menu & Styles Panel

_Scope: Styles panel structure: category toolbar, style list, filter dropdown_

LibreOffice Writer uses a style-based formatting system. The Styles menu provides quick-apply shortcuts, while the Styles panel (F11) offers full management.

The screenshot shows the Styles drop-down menu opened from the menu bar. It is divided into three groups of radio-button entries separated by dividers: the first group lists paragraph styles (Body Text, Title, Subtitle, Heading 1, Heading 2, Heading 3, Block Quotation, and Preformatted Text), the second group lists character styles (No Character Style — selected by default with a filled radio button — Emphasis, Strong Emphasis, Quotation, and Source Text), and the third group lists list styles (No List — also selected — Bullet • List Style, and several Numbering list styles for 123, ABC, abc, IVX, and ivx). Below the radio-button sections, five plain-text commands appear: Edit Style…, Update Selected Style, New Style from Selection, Load Styles from Template, and Manage Styles.

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

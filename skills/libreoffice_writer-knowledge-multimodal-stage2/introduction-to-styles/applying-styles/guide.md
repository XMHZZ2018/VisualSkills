# Applying Styles (LibreOffice Writer 7.3.7)

Writer gives you five categories of styles — paragraph, character, page, frame, and list — and several ways to apply each one. The quickest place to find them all is the **Styles** deck on the Sidebar (press **F11** or go to **View > Sidebar**). Just click the icon at the top of the deck to switch between Paragraph Styles, Character Styles, Page Styles, Frame Styles, and List Styles. Use the filter drop-down at the bottom to show **All Styles**, **Applied Styles**, or **Custom Styles** depending on how cluttered you want the list.

See `fig01.png`.

For **paragraph styles**, the fastest method is the **Set Paragraph Style** drop-down at the left end of the Formatting toolbar. Click the arrow, pick a style, and the current paragraph updates instantly. You can also go to **Styles > [name of paragraph style]** on the Menu bar, or right-click and choose **Paragraph** from the context menu to reach a smaller submenu of common styles. Keyboard shortcuts work too: *Ctrl+0* applies Text Body, *Ctrl+1* through *Ctrl+5* apply Heading 1 through Heading 5.

**Character styles** work similarly but require you to select text first (or just place the cursor in a single word). Open the Character Styles tab on the Styles deck and double-click the style you want, or right-click your selection and choose **Character** from the context menu to see common options. If you need to strip a character style back off, select the text, click the **Character Styles** icon in the Styles deck, and double-click **No Character Style**. It's also good practice to clear direct formatting first with **Format > Clear Direct Formatting** (*Ctrl+M*) before applying character styles.

See `fig02.png`.

**Frame styles** are handy when you insert images or other objects — Writer wraps them in an invisible frame automatically. Select the frame, click the **Frame Styles** icon in the Styles deck, and double-click the desired style. After applying it, you can still tweak anchoring (**Format > Anchor**), arrangement (**Format > Arrange**), or add a hyperlink (**Insert > Hyperlink**) manually.

**Page styles** control layout, headers, footers, and margins for entire pages. The current page style is shown on the Status bar at the bottom of the window. To switch it, right-click the style name on the Status bar and pick a different one. For more control — like starting a new chapter on a *First Page* style that flows into a *Default Page Style* — insert a manual page break via **Insert > More Breaks > Manual Break**, choose **Page break**, and select the desired page style from the list.

See `fig03.png` for the Insert Break dialog.

**List styles** define indentation, numbering format, and bullet symbols, but they work best when paired with paragraph styles. Use paragraph styles like *List 1*, *List 2*, *List 3* for bulleted lists (these reference Bullet list styles) and *Numbering 1*, *Numbering 2*, etc. for ordered lists. You can redefine bullet symbols, numbering sequences, and indentation by modifying the underlying list style.

One more power move: **Fill Format Mode**. Click the paint-bucket icon at the top of the Styles deck, select a style, then click or drag across paragraphs, frames, or pages to stamp that style onto everything you touch. Press *Esc* when you're done. It's the fastest way to restyle scattered content without hunting through menus repeatedly.

---

## UI Reference  —  Formatting Toolbar

_Scope: Paragraph Style dropdown, Update Selected Style (Shift+Ctrl+F11), New Style from Selection_

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

## UI Reference  —  Right Sidebar

_Scope: Styles panel (Alt+2/F11): style categories, style list, Fill Format Mode, filter dropdown_

The collapsed right sidebar is a vertical strip of 8 icon buttons along the right edge of the window. Each opens a full docked panel. Toggle the sidebar with Ctrl+F5 or View > Sidebar.

Read the screenshot `ui-right-sidebar-location.png` in this directory.

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

_Scope: Styles menu quick-apply (Ctrl+0-3), Fill Format Mode, Edit/Update/New Style_

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


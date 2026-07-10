# Using the Style Inspector (LibreOffice Writer 7.3.7)

The Style Inspector is a Sidebar panel that shows you exactly what's happening with the formatting of any text your cursor is sitting in. It breaks down paragraph styles, character styles, and any direct formatting that's been applied — super handy when something looks off and you can't figure out why.

To open it, look in the Sidebar (if the Sidebar isn't visible, toggle it with **View > Sidebar**). The Style Inspector lives there alongside panels like Properties and Styles. You can also find it listed as one of the Sidebar deck options.

Once it's open, just click into any text in your document. The Style Inspector immediately updates to show a tree of everything affecting that text. At the top you'll see **Paragraph Styles** — this tells you the paragraph style in use (e.g., "Text Body"). Below that is **Paragraph Direct Formatting**, which lists any manual overrides you've applied on top of the paragraph style, like toggling "Para Keep Together" to true.

See `fig01.png`.

Further down, you'll find **Character Styles** and **Character Direct Formatting**. If you've applied a character style like "Strong Emphasis," it shows up here along with its attributes — things like Char Font Char Set, Char Font Name, Char Font Style Name, and Char Weight. Any direct character formatting (say, you manually bolded a word or changed the font) appears separately so you can tell what came from a style versus what was hand-applied.

This distinction between style-based and direct formatting is the real power here. When formatting in a document looks inconsistent or broken, the Style Inspector lets you pinpoint whether the culprit is a rogue direct format override or a misapplied style.

For advanced users, the Style Inspector can also reveal hidden RDF (Resource Description Framework) metadata attached to text spans, paragraphs, and bookmarks. If you work with annotated text, the "Nested Text Content" item shows boundaries of nested annotated ranges and metadata fields.

You can also set custom color metadata field shadings on annotated text ranges to visually distinguish metadata categories in the editor. Toggle these on or off with **View > Field Shadings** or *Ctrl+F8*.

---

## UI Reference  —  Right Sidebar

_Scope: Style Inspector panel (Alt+6): paragraph/character styles and direct formatting property tree_

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


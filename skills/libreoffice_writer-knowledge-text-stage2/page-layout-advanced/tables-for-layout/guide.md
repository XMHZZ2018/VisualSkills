# Using Tables for Page Layout (LibreOffice Writer 7.3.7)

Tables in Writer aren't just for data — they're a handy way to build structured page layouts like sideheads, multi-column arrangements, and neatly aligned header or footer content. Think of a table as an invisible grid you can drop text and graphics into, giving you far more control than tabs or spaces ever could.

## Positioning info in headers and footers

Instead of fussing with frames or manual spacing, drop a borderless table into a header or footer. This lets you cleanly position elements like page numbers on the left, the document title in the center, and the author on the right — all in a single row. For even simpler cases, fields (**Insert > Header and Footer > Fields**) might be enough.

## Creating sideheads with tables

Sideheads — those marginal labels you see in resumes and user guides — are easy to pull off with a two-column table. The narrow left column holds your sidehead text, while the wider right column carries the main body content. The first paragraph in each cell aligns beside the sidehead, giving that classic offset look.

To set one up, place your cursor where you want it and go to **Table > Insert Table** (or press **Ctrl+F12**). Create a two-column, one-row table with no heading, and pick **None** under Styles so the table is borderless. Hit **Insert**.

The Insert Table dialog shows a General section at the top with a Name field (set to "Table1"), Columns set to 2, and Rows set to 1. Below that, the Options section has the Heading checkbox unchecked, along with options for "Repeat heading rows on new pages" and "Don't split table over pages." At the bottom, the Styles list has "None" selected (highlighted in green), and a preview pane on the right shows a sample table with data. The dialog has Help, Cancel, and Insert buttons along the bottom.

Now right-click the table and choose **Table Properties**. On the **Columns** tab, set your column widths — for example, 3.30 cm for the sidehead and 13.70 cm for the body text, matching your page's left margin offset.

The Table Properties dialog is open on the Columns tab, which also has tabs for Table, Text Flow, Borders, and Background. Two checkboxes at the top — "Adapt table width" and "Adjust columns proportionally" — are both unchecked. A "Remaining space" field shows 0.00 cm. Below that, under the Column Width heading, column 1 is set to 3.30 cm and column 2 is set to 13.70 cm, with columns 3 through 6 left blank since only two columns are in use.

Then switch to the **Table** tab in the same dialog. Under Spacing, set **Above** and **Below** to match the top and bottom spacing of your regular body paragraphs so the table blends seamlessly into the page flow. Give the table a meaningful name in the Properties section and click **OK**.

If you'd rather have each paragraph break onto its own row (handy when content grows), put each chunk in a separate table row and let the table break between pages. Alternatively, keep everything in one row if you want text and graphics to reflow together when you edit.

**Tip:** You can quickly check a paragraph's spacing by clicking into it and opening the Properties deck in the Sidebar — look under *Paragraph > Spacing* for the values.

---

## UI Reference  —  Table & Form Menus

_Scope: Insert Table, Size, Properties for layout tables_

The Table menu manages table creation and editing. The Form menu provides form controls and design tools. Most Table items are context-sensitive and greyed when the cursor is not in a table.

## Table Menu

The Table drop-down menu in Writer's menu bar shows a vertical list of items: Insert Table…, Insert (with a submenu arrow), Delete (submenu arrow), Select (submenu arrow), and Size (submenu arrow), followed by a separator. Next come Merge Cells, Split Cells…, Merge Table, and Split Table…, then another separator with Protect Cells and Unprotect Cells. Further down are AutoFormat Styles… and Number Format…, a Number Recognition toggle with an unchecked checkbox, then Header Rows Repeat Across Pages and Row to Break Across Pages (both greyed out). Near the bottom are Convert (submenu arrow), Edit Formula, Sort… (greyed out), and Properties… (greyed out).

- **Insert Table…** (Ctrl+F12) — Opens the Insert Table dialog (name, columns, rows, heading options, table style presets).
- **Insert** (►) — Rows Above/Below, Rows…, Columns Before/After, Columns…
- **Delete** (►) — Rows, Columns, or entire Table.
- **Select** (►) — Cell, Row, Column, or Table.
- **Size** (►) — Row Height, Minimal/Optimal Row Height, Distribute Rows Evenly; Column Width, Minimal/Optimal Column Width, Distribute Columns Evenly.
- **Merge Cells** / **Split Cells…** / **Merge Table** / **Split Table…**
- **Protect Cells** / **Unprotect Cells**
- **AutoFormat Styles…** / **Number Format…**
- **Number Recognition** — Toggle checkbox.
- **Header Rows Repeat Across Pages** / **Row to Break Across Pages**
- **Convert** (►) — Text to Table…, Table to Text…
- **Edit Formula** (F2) / **Sort…** / **Properties…**

## Form Menu

- **Design Mode** (toggle, on by default) / **Control Wizards** (toggle, on by default)
- **Form controls:** Label, Text Box, Check Box, Option Button, List Box, Combo Box, Push Button, Image Button, Formatted Field, Group Box, Image Control, File Selection, Table Control, Navigation Bar.
- **More Fields** (►) — Date Field, Time Field, Numerical Field, Currency Field, Pattern Field.
- **Control Properties…** / **Form Properties…** / **Form Navigator…** / **Activation Order…**
- **Open in Design Mode** / **Automatic Control Focus** — toggles.
- **Content Controls** (►) — Word-compatible: Rich Text, Plain Text, Picture, Check Box, Combo Box, Drop-Down List, Date Control, Properties.

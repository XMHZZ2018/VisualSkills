# Formatting Tables (LibreOffice Writer 7.3.7)

Formatting a table in Writer is really a two-part job: getting the layout right (size, position, borders) and then making the text inside look good. Let's walk through both.

To control a table's overall size and position, right-click anywhere in the table and choose **Table Properties**, or go to **Table > Properties** on the Menu bar. On the **Table** tab you'll find alignment options — **Automatic** fills the full text area width, while **Left**, **Right**, **Center**, and **Manual** let you place the table precisely with custom spacing values.

See `fig01.png`.

The **Text Flow** tab is where you handle page-break behavior. You can insert breaks before or after the table, keep it with the next paragraph, and — crucially — check **Allow table to split across pages and columns** so long tables flow naturally. If your table has a header row, enable **Repeat heading** and set the number of rows to repeat on each new page.

For column widths, you can drag dividers directly on the horizontal ruler or inside the table itself. For finer control, open the **Columns** tab of the Table Properties dialog, where you can type exact widths and choose whether **Adapt table width** or **Adjust columns proportionally** is active. You can also resize with the keyboard: place the cursor in a cell, hold **Alt**, and press the arrow keys.

Merging and splitting cells is straightforward. Select the cells you want to combine, then right-click and choose **Merge Cells** (or **Table > Merge Cells**). To split, place the cursor in a cell and choose **Split Cells** from the same menu — you pick how many parts and whether to split horizontally or vertically. It's best to merge and split *after* you've settled on the overall layout, since these operations can behave unpredictably if you rearrange columns later.

For borders, open the **Borders** tab of Table Properties. The **Line Arrangement** presets handle the common cases quickly, or click in the **User-defined** area for full control over which edges get lines. Set **Style**, **Color**, and **Width** for the line itself, adjust **Padding** to control spacing between the border and cell content, and tick **Synchronize** if you want equal padding on all sides.

See `fig02.png`.

Background colors and images live on the **Background** tab. You can apply a background to a single **Cell**, a **Row**, or the entire **Table** — just pick the scope from the dropdown. Click the **Color** button to choose a solid fill, or the **Bitmap** button to insert an image. Keep contrast in mind: a cell's background sits in front of the row background, which sits in front of the table background.

To apply a consistent look fast, use table styles. Open the **Table Styles** tab on the Styles deck in the Sidebar and double-click a style name. For more options, go to **Table > AutoFormat Styles**, preview the formats, and click **OK**. You can create your own style by formatting a table the way you like it, then opening **AutoFormat Styles** and clicking **Add**.

See `fig03.png`.

Once the layout is set, format the text in cells just as you would any other paragraph — paragraph styles, character styles, and direct formatting all work. Vertical alignment is controlled by icons on the Table toolbar: **Align Top**, **Center Vertically**, or **Align Bottom**. For number formatting, select cells and choose **Table > Number Format**, where you can pick currency, date, percentage, and other categories. To rotate text (handy for narrow column headings), select it, go to **Format > Character**, and on the **Position** tab set the rotation angle to 90 or 270 degrees.

---

## UI Reference  —  Table & Form Menus

_Scope: Size submenu, Merge/Split Cells, AutoFormat Styles, Number Format, Properties_

The Table menu manages table creation and editing. The Form menu provides form controls and design tools. Most Table items are context-sensitive and greyed when the cursor is not in a table.

## Table Menu

(see screenshot `ui-table-menu.png`)

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


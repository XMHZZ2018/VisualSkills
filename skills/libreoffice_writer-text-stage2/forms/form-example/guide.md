# Building a Simple Form (LibreOffice Writer 7.3.7)

The goal here is a short "Favorite Shape Survey" — a form with a text field, option buttons, a dropdown list, and some check boxes. It's a great way to get comfortable with Writer's form controls.

Start by opening a new document via **File > New > Text Document** and typing out the form's static text: a title, a short instruction line, and labels like *Name:*, *Gender:*, *Favorite shape:*, and *All shapes you like:*. Think of this as sketching the layout before wiring anything up.

The completed form displays a bold "Favorite Shape Survey" heading followed by a two-line instruction ("Thank you for agreeing to take part in this survey. Please complete the form and return it by email to your teacher."). Below that are four rows of controls: a text box next to the "Name:" label, three option buttons labeled Male, Female, and Other next to "Gender:", a dropdown list (with a down-arrow button on its right end) next to "Favorite shape:", and four check boxes labeled Circle, Triangle, Square, and Pentagon arranged in a horizontal row beneath "All shapes you like:".

Now bring in the Form Controls toolbar by going to **View > Toolbars > Form Controls**. Click the **Design Mode** icon on that toolbar to activate it — you need to be in Design Mode to place and edit controls. Also make sure **Toggle Form Control Wizards** is OFF so you get direct control over each element.

Click the **Text Box** icon, then draw a text box in the document next to the *Name:* label. For *Gender:*, click the **Option Button** icon and draw three option buttons nearby — one each for Male, Female, and Other. Next, use the **List Box** icon to draw a dropdown list beside *Favorite shape:*. Finally, grab the **Check Box** icon and create four check boxes next to *All shapes you like:* for Circle, Triangle, Square, and Pentagon.

To configure the option buttons, double-click the first one to open its Properties dialog. On the **General** tab, set the **Label** to **Male** and the **Group name** to **Gender**. Repeat for the other two buttons, changing the Label to **Female** and **Other** respectively but keeping the Group name as **Gender** — this grouping ensures only one can be selected at a time.

The "Properties: Option Button" dialog is shown with three tabs along the top: General (currently selected), Data, and Events. On the General tab, visible fields listed vertically include Name (set to "Option Button 1"), Label (set to "Male," highlighted with a red border), Label Field (empty), Group name (set to "Gender," also highlighted with a red border), and Enabled (set to "Yes"). The Label and Group name fields are the two key settings to configure here.

For the list box, double-click it and find the **List entries** field on the **General** tab. Type each shape name (Circle, Triangle, Square, Pentagon) one at a time, pressing *Shift+Enter* after each to add a new line.

For the check boxes, double-click each one in turn and change the **Label** field to the matching shape name — Circle, Square, Triangle, Pentagon.

The "Properties: Check Box" dialog appears with the same three tabs: General, Data, and Events. The General tab shows the Name field set to "Check Box 1" and the Label field (highlighted with a red border) set to "Circle." Below those are Label Field (empty), Enabled (set to "Yes"), and Visible (set to "Yes"). The Label field is the one you need to edit for each check box.

If your controls look a bit scattered, select multiple option buttons by drawing a selection box around them with the **Select** tool, then right-click and choose **Align > Top** to tidy them up.

Once everything looks right, close the Properties dialog, turn **Design Mode** off, and give the form a spin — type in the text box, click an option button, pick from the dropdown, and tick some check boxes. That's your working form.

---

## UI Reference  —  Table & Form Menus

_Scope: Text Box, Option Button, List Box, Check Box controls for building forms_

The Table menu manages table creation and editing. The Form menu provides form controls and design tools. Most Table items are context-sensitive and greyed when the cursor is not in a table.

## Table Menu

The Table dropdown menu is shown open from the Writer menu bar. It lists the following items from top to bottom: Insert Table…, Insert (with a submenu arrow), Delete (submenu arrow), Select (submenu arrow), Size (submenu arrow), then a separator, followed by Merge Cells, Split Cells…, Merge Table, Split Table…, another separator, Protect Cells, Unprotect Cells, another separator, AutoFormat Styles…, Number Format…, a Number Recognition checkbox item, Header Rows Repeat Across Pages (truncated), Row to Break Across Pages (truncated), another separator, Convert (submenu arrow), Edit Formula, Sort…, and Properties…. Several items such as Merge Cells, Split Cells, and Sort appear greyed out because no table is currently selected.

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

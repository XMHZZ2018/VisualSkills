# Advanced Form Customization (LibreOffice Writer 7.3.7)

Once you've built a basic form, the real power comes from wiring up macros, locking down permissions, and fine-tuning how each control looks and behaves. Here's how to take your forms further.

## Linking Macros to Form Controls

Any form control — text boxes, buttons, checkboxes — can trigger a macro in response to an event like a keystroke, mouse click, or focus change. First, write your macro (see the Getting Started Guide, Chapter 13 for the basics). Then, make sure you're in design mode, right-click the control, and choose **Control Properties** from the context menu. Switch to the **Events** tab, where you'll see a list of available events such as *Changed*, *Key pressed*, *Mouse moved*, and more.

The Properties dialog for a Text Box is shown with the **Events** tab selected (alongside the General and Data tabs). It lists all available events in a single column — including Changed, Text modified, When receiving focus, When losing focus, Key pressed, Key released, Mouse inside, Mouse moved while key pressed, Mouse moved, Mouse button pressed, Mouse button released, Mouse outside, Prior to reset, After resetting, Before updating, and After updating — each with a blank assignment field and a browse ("...") button on the right.

Click the browse button next to any event to open the **Assign Action** dialog. Hit the **Macro** button, pick your macro from the Macro Selector, and confirm with **OK**. You can assign different macros to different events on the same control. If you need to attach macros to the form itself (rather than a single control), right-click the form control, select **Form Properties**, and use its **Events** tab instead.

The Assign Action dialog is displayed with two main areas: on the left, an **Assignments** table with an "Event" column and an "Assigned Action" column, listing all the same events (Changed, Text modified, When receiving focus, and so on) with "Text modified" currently highlighted in green; on the right, an **Assign** panel containing a **Macro…** button and a **Remove** button. At the bottom of the dialog are **Help**, **Cancel**, and **OK** buttons.

## Read-Only Documents and Database Permissions

When your form is finished and you want users to interact with it without altering the layout, go to **File > Properties > Security** and select **Open file read-only**. The form still works — users can browse and enter data — but the document structure stays locked.

By default, a database connection lets users add, edit, and delete records freely. To tighten that up, right-click a form control in design mode, choose **Form Properties**, and open the **Data** tab. You'll find toggles for *Allow additions*, *Allow modifications*, *Allow deletions*, and *Add data only* — set each to **Yes** or **No** as needed. To protect an individual field (say, a stock quantity you don't want edited), right-click that specific control, select **Control** from the context menu, go to the *General* tab, and set *Read-only* to **Yes**.

The Form Properties dialog is shown with the **Data** tab active (alongside General and Events tabs). At the top are data-source fields: Data source is set to "Bibliography", Content type to "Table", and Content to "biblio", followed by Analyze SQL command set to "Yes", and empty Filter and Sort fields with browse buttons. Below these, highlighted with a red rectangle, are the four permission toggles: Allow additions (Yes), Allow modifications (Yes), Allow deletions (Yes), and Add data only (No) — each with a dropdown selector. At the bottom are Navigation bar (Yes) and Cycle (Default) settings.

## Form Control Formatting Options

You can customize the appearance and behavior of any control through its **Control Properties** dialog (right-click the control in design mode, *General* tab). Set a label in the *Label* box, choose whether the control prints with the document via the *Print* option, and use the *Font* setting to control typeface and size for fields. For text boxes, setting a *maximum text length* that matches the database field's limit prevents frustrating data-entry errors. You can also set default values, configure password-masking characters, add help text, and style controls with background colors, 3-D effects, scroll bars, and borders.

---

## UI Reference  —  Table & Form Menus

_Scope: Control Properties…, Form Properties…, Activation Order…_

The Table menu manages table creation and editing. The Form menu provides form controls and design tools. Most Table items are context-sensitive and greyed when the cursor is not in a table.

## Table Menu

The Table drop-down menu is shown open from the LibreOffice Writer menu bar. It lists the following items from top to bottom: Insert Table…, Insert (submenu arrow), Delete (submenu arrow), Select (submenu arrow), Size (submenu arrow), then a separator, followed by Merge Cells, Split Cells…, Merge Table, Split Table…, another separator, Protect Cells, Unprotect Cells, a separator, AutoFormat Styles…, Number Format…, a Number Recognition checkbox (unchecked), Header Rows Repeat Across Pages (greyed out), Row to Break Across Pages (greyed out), a separator, Convert (submenu arrow), Edit Formula, Sort… (greyed out), and Properties… (greyed out).

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

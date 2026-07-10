# Building a Simple Form (LibreOffice Writer 7.3.7)

The goal here is a short "Favorite Shape Survey" — a form with a text field, option buttons, a dropdown list, and some check boxes. It's a great way to get comfortable with Writer's form controls.

Start by opening a new document via **File > New > Text Document** and typing out the form's static text: a title, a short instruction line, and labels like *Name:*, *Gender:*, *Favorite shape:*, and *All shapes you like:*. Think of this as sketching the layout before wiring anything up.

See `fig01.png` for the completed Favorite Shape Survey form with all controls.

Now bring in the Form Controls toolbar by going to **View > Toolbars > Form Controls**. Click the **Design Mode** icon on that toolbar to activate it — you need to be in Design Mode to place and edit controls. Also make sure **Toggle Form Control Wizards** is OFF so you get direct control over each element.

Click the **Text Box** icon, then draw a text box in the document next to the *Name:* label. For *Gender:*, click the **Option Button** icon and draw three option buttons nearby — one each for Male, Female, and Other. Next, use the **List Box** icon to draw a dropdown list beside *Favorite shape:*. Finally, grab the **Check Box** icon and create four check boxes next to *All shapes you like:* for Circle, Triangle, Square, and Pentagon.

To configure the option buttons, double-click the first one to open its Properties dialog. On the **General** tab, set the **Label** to **Male** and the **Group name** to **Gender**. Repeat for the other two buttons, changing the Label to **Female** and **Other** respectively but keeping the Group name as **Gender** — this grouping ensures only one can be selected at a time.

See `fig02.png` for the Properties dialog for an option button showing Label and Group name fields.

For the list box, double-click it and find the **List entries** field on the **General** tab. Type each shape name (Circle, Triangle, Square, Pentagon) one at a time, pressing *Shift+Enter* after each to add a new line.

For the check boxes, double-click each one in turn and change the **Label** field to the matching shape name — Circle, Square, Triangle, Pentagon.

See `fig03.png` for the Properties dialog for a check box showing the Label field.

If your controls look a bit scattered, select multiple option buttons by drawing a selection box around them with the **Select** tool, then right-click and choose **Align > Top** to tidy them up.

Once everything looks right, close the Properties dialog, turn **Design Mode** off, and give the form a spin — type in the text box, click an option button, pick from the dropdown, and tick some check boxes. That's your working form.

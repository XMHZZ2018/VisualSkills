# Accessing Data Sources (LibreOffice Writer 7.3.7)

The most common reason to build a form in Writer is to feed information into a database — think of a contacts database where people fill in names, addresses, and so on. Since the form lives inside a regular Writer document, you can dress it up with graphics, tables, and formatting just like any other page.

LibreOffice can talk to numerous data sources: ODBC, MySQL, Oracle JDBC, spreadsheets, and text files. Databases generally allow both reading and writing, while other sources like spreadsheets are read-only. To browse what's available on your system, go to **File > New > Database**, choose **Connect to an existing database** on the first page of the Database Wizard, and open the drop-down list.

This guide assumes you've already created and registered a database for use with Writer. If you haven't, Chapter 14 (Mail Merge) covers how to create and register one.

## Creating a form for data entry

Once your database is registered, open a fresh document with **File > New > Text Document** and lay out your form visually — labels, spacing, whatever looks right. Don't worry about the actual data fields yet; you can always add or rearrange them later. Show the Form Controls and Form Design toolbars, then click the **Design Mode** icon to switch the document into design mode. From there, click **Text Box** (or any other field type) and drag on the page to place your controls.

Now you need to wire the form to your data source. Click the **Form Properties** icon on the Form Design toolbar — or right-click any field you've placed and choose **Form Properties**. In the dialog that opens, switch to the **Data** tab. Set **Data Source** to your registered database, set **Content Type** to **Table**, and set Content to the specific table you want to access. Then close the dialog.

See `fig01.png`.

Next, connect each individual field to a database column. Click a control to select it (you'll see small green handles), right-click it, and choose **Control Properties**. On the **Data** tab, pick the appropriate column from the **Data Field** drop-down — for example, Address or Telephone. Repeat for every control on the form.

See `fig02.png`.

If your database has a Primary Key field with *AutoValue* set to **Yes**, that field doesn't need to appear on the form. But if AutoValue is **No**, users will have to manually enter a unique value every time they create a record — not ideal, so plan accordingly.

## Entering data into a form

When you're ready to use the form, make sure you're **not** in design mode — most toolbar buttons should be active, not grayed out. Turn on the Form Navigation toolbar via **View > Toolbars > Form Navigation**; it appears at the bottom of the workspace and lets you step through records, add new ones, or delete existing entries.

If the database already has data, use the navigation controls to browse records and edit values in place. To save a changed record, just press **Enter** with the cursor in the last field — Writer commits the update and moves to the next record. For a blank database, type directly into the form fields and press Enter in the last field to submit each new record.

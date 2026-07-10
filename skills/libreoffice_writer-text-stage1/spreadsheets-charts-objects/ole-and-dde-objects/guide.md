# OLE and DDE Objects (LibreOffice Writer 7.3.7)

OLE (Object Linking and Embedding) and DDE (Dynamic Data Exchange) both let you pull information from one application — say, a Calc spreadsheet — right into your Writer document. The key difference: a linked OLE object stays editable from both ends and keeps both documents in sync, while a DDE object acts more like a live mirror — changes flow from the source into Writer automatically, but you can't edit the DDE object directly inside Writer.

An **embedded** OLE object is a copy. There's no connection back to the source, so edits in either place stay independent. Embed when you want a self-contained document. A **linked** OLE object is a reference — change the original and the Writer copy updates too, but you need to keep the source file accessible and in the same location.

You can insert spreadsheets, charts, drawings, formulas, and presentations as OLE objects.

**Creating a new OLE object from scratch** is straightforward. Click where you want it, then go to **Insert > Object > OLE Object**. In the dialog that opens, keep **Create new** selected, pick the object type you want (spreadsheet, drawing, formula, etc.), and hit **OK**. Writer drops you straight into edit mode with the appropriate toolbars ready to go.

See `fig01.png`.

**Inserting an existing file as an OLE object** is just as easy. Open the same dialog via **Insert > Object > OLE Object**, but this time switch to **Create from file**. Click **Search** to browse for your file, then choose how you want it linked. If you want live syncing between the file and your document, check the **Link to file** option. If you'd rather show just an icon instead of the full content, tick **Display as icon**. Click **OK** and you're set.

See `fig02.png`.

**Editing an OLE object** is as simple as double-clicking it. Writer's toolbars swap out to match the embedded application — so if it's a Calc spreadsheet, you'll see Calc's menus and toolbars right inside your Writer window. Click outside the object to return to normal editing.

**DDE objects** work a bit differently. When a Calc spreadsheet is pasted as a DDE object, you can't edit it in Writer directly. But whenever the source Calc file is updated, those changes automatically appear in your Writer document. Use DDE when you want a read-only, always-current snapshot of external data.

On Windows, you'll also see a **Further Objects** option in the Object Type list, which lets you create OLE objects using other software compatible with OLE and LibreOffice.

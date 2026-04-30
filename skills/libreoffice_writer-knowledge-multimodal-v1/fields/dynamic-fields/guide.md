# Dynamic Fields and Numbering Sequences (LibreOffice Writer 7.3.7)

Fields in Writer are placeholders that update automatically — think of them as live references to information that might change over time. A project manager's name, a product title, or even your entire company name can be stored as a field. Update it once, and every instance in the document follows suit.

Writer gives you seven handy document properties — *Page Number*, *Page Count*, *Date*, *Time*, *Title*, *First Author*, and *Subject* — all available right from **Insert > Field**. Several of these pull their values from the Document Properties dialog. For richer metadata, head to the *DocInformation* and *Document* tabs of the Fields dialog by choosing **Insert > Field > More Fields** or pressing *Ctrl+F2*.

See `fig01.png`.

The *Custom* item in the *DocInformation* tab's Type list comes from the Custom Properties tab of **File > Properties**; it only shows up if you've actually defined custom properties. Some field values are pulled from **Tools > Options > LibreOffice** under the *User Data* page, so make sure that info is accurate. To insert any of these, pick your Type, choose a Select and Format option, then click **Insert**.

If a field should never change after insertion — say a creation date you want frozen — tick the **Fixed content** checkbox (bottom-right of the Fields dialog) when inserting it. You can always come back and uncheck it later if you change your mind.

## Saving Fields as AutoText

When you use the same fields repeatedly, AutoText saves you the trouble of re-inserting them manually. First, insert the field into your document, then select it and open **Tools > AutoText** (or press *Ctrl+F3*). Pick a group, give the entry a name and shortcut, then click the **AutoText** button and choose **New** — not **New (text only)**, which would strip the field and store plain text. Now just type the shortcut and press *F3* to drop the field in wherever you need it.

See `fig02.png`.

## Defining Custom Numbering Sequences

Sometimes built-in list styles don't cut it — maybe you need a "Step 1, Step 2, Step 3" sequence placed at arbitrary points in your text rather than as a formatted list. You can create your own using a number range variable field.

Place your cursor in a blank paragraph and open **Insert > Field > More Fields** (*Ctrl+F2*), then go to the *Variables* tab. Select **Number range** as the Type and **Arabic (1 2 3)** as the Format, and type a name (like "Step") in the Name field. Click **Insert** and a number field (starting at 1) appears in your document. Each additional click of **Insert** adds the next number in the sequence — 2, 3, 4, and so on.

Once you've seeded the sequence, you can delete the initial test fields; the "Step" variable remains available in the Select list of the Fields dialog for the rest of the session. For even faster access, save the field as an AutoText entry so you can drop in the next Step number with a quick shortcut and *F3*.

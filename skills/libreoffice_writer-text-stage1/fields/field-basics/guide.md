# Field Basics and Document Properties (LibreOffice Writer 7.3.7)

Fields let you insert dynamic data into your document — things like the current date, page count, author name, or a product title that might change later. They show up with a gray background on screen (unless you've turned that off via **View > Field Shadings**), and that shading won't appear in print or PDF export.

A few keyboard shortcuts are worth memorizing. **Ctrl+F2** opens the full Fields dialog, **Ctrl+F8** toggles field shading on and off, **Ctrl+F9** switches between showing field names and their values, and **F9** forces all fields to update.

For everyday inserts, you don't need the full dialog. Just go to **Insert > Page Number** or **Insert > Field** on the Menu bar and pick from the submenu — page number, page count, date, time, title, first author, subject, and more are all one click away.

See `fig01.png`.

When you need fields tied to your document's own metadata, head to **File > Properties**. This dialog has six tabs; the General and Statistics tabs are auto-populated by Writer. The ones you care about are **Description** and **Custom Properties**.

On the **Description** tab you'll find fields for Title, Subject, Keywords, and Comments. Fill these in and you can reference them anywhere in the document as fields. Change the value here once, and every reference updates automatically — handy when a draft title becomes a final one.

See `fig02.png`.

The **Custom Properties** tab is where it gets flexible. It may be blank in a new document, or pre-filled if you started from a template. Hit the **Add Property** button in the lower right to create a new row. Give it a name (there's a dropdown of common choices, or type your own), pick a type — Text, DateTime, Date, Duration, Number, or Yes/No — and set its value. For example, you might store a "Guide Name" as Text with the value "Writer Guide", or a "LibreOffice Version" set to "7.3".

See `fig03.png`.

Once properties are defined, you can insert them as fields anywhere in the document through **Insert > Field > More Fields** (or **Ctrl+F2**). Whenever you update a property back in **File > Properties**, every field referencing it refreshes throughout the document. This makes Custom Properties ideal for information that appears in multiple places — project names, version numbers, client details — so you only ever maintain it in one spot.

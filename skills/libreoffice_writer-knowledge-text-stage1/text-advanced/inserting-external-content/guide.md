# Inserting Material from Other Documents (LibreOffice Writer 7.3.7)

Sometimes you want to pull in content from another file — maybe you're assembling a set of instructions and several documents share common paragraphs. You could copy and paste, sure, but if those shared paragraphs ever get edited, you'd need to update every document by hand. Writer gives you smarter options.

There are two main tools for the job. The first is the **Section** dialog, found under **Format > Sections** (or when inserting via **Insert > Section**). Sections let you link a portion of your document to an external file so the content stays in sync. This approach is covered in detail in the Formatting Pages: Advanced chapter.

The second — and often quicker — method uses the **Navigator**. Open it with **F5** or **View > Navigator**. The Navigator has two drag modes that control what happens when you drag an item from a source document into your current one: **Insert as Link** and **Insert as Copy**. To pick the mode, right-click the drag mode icon in the Navigator toolbar.

To pull content in, first select the item you want from the source document inside the Navigator, then drag it into your target document. Choose **Insert as Link** if you want the content to update when the source changes, or **Insert as Copy** for a one-time snapshot. Keep in mind that you cannot create links or copies of graphics, OLE objects, references, or indexes this way — the Navigator's drag modes only work with text-based items like headings and sections.

See `fig01.png`.

If the shared content changes frequently, linking is the way to go — your document will pick up edits automatically. For static reuse where you just need the text once, a plain copy is simpler and has no external dependency.

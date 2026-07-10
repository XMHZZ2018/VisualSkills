# Master Document Overview (LibreOffice Writer 7.3.7)

A master document (.odm) is basically a container that pulls separate text documents (.odt) together into one big, unified piece. It handles formatting, table of contents, bibliography, index — all that stuff — across the whole combined document. If you're writing a book, thesis, or any long report, this is the tool you want. It's especially handy when the file is too large for comfortable editing, when multiple people are working on different chapters, or when subdocuments need to live as standalone files *and* as parts of a larger whole.

That said, a master document isn't always the answer. Sometimes a single large .odt file, or even an ordinary document with sections linked to other files, works just fine. For that approach, check out **Format > Sections** and the options covered under Formatting Pages: Advanced.

## The Navigator in Master View

The Navigator works differently depending on context. In a regular text document, it shows a tree of headings, tables, frames, images, and other objects. In a master document, you flip to master view by clicking the **Toggle Master View** icon at the upper left of the Navigator. Once you do, it switches to listing your subdocuments and text sections instead.

The image shows the Navigator panel in two side-by-side views. On the left is the standard Navigator for a regular text document, displaying a tree of categories including Headings, Tables, Frames, Images, OLE objects, Bookmarks, Sections, Hyperlinks, References, Indexes, Comments, and Drawing objects, along with toolbar buttons for navigation and a document selector dropdown at the bottom. On the right is the Navigator in master document mode, which instead lists a "Text" root node containing a "Contents" entry followed by a series of linked subdocument files (such as GS7000-Preface.odt, GS7001-IntroducingLO.odt, and so on through GS7016-OpenSourceStandardsDoc.odt), each shown with a chain-link icon, and ending with a "Text" entry at the bottom. The master view toolbar at the top shows icons for toggling master view, inserting, and reordering subdocuments.

From master view you can reorder subdocuments, insert new ones, or remove existing ones — all by right-clicking or using the Navigator's toolbar buttons. The details of inserting and combining subdocuments are covered further in the full chapter.

## Styles Across Subdocuments

Here's the key thing about styles: when you link a standalone document into a master document, it becomes a subdocument. Each subdocument can have its own style definitions (font, page size, margins, etc.), but the master document's styles take priority for the final output while the originals stay intact in the individual files.

A few rules to keep in mind. Custom styles in subdocuments — like paragraph styles you created yourself — get automatically imported into the master document. If two subdocuments define a custom style with the same name, only the version from the *first* subdocument linked gets imported. And if a built-in style like Default Style exists in both the master and a subdocument, the master document's definition wins.

Styles are only changed in the master document itself, so opening a subdocument on its own for editing won't disturb anything. A solid trick: use the same document template for the master and all subdocuments. That way everything looks consistent. If you need to tweak a style, make the change in the *template* (not the master or any subdocument directly), then reopen your files and the update flows through.

## Creating a Master Document

Your approach depends on where you're starting from. You might be starting fresh with no existing documents, planning a multi-chapter book with several authors. Or you might already have separate chapter files you want to combine under one master. A third scenario: you have a single large document you want to split into subdocuments controlled by the master. Each path is supported and covered in the full chapter.

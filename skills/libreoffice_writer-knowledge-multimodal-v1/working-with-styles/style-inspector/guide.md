# Using the Style Inspector (LibreOffice Writer 7.3.7)

The Style Inspector is a Sidebar panel that shows you exactly what's happening with the formatting of any text your cursor is sitting in. It breaks down paragraph styles, character styles, and any direct formatting that's been applied — super handy when something looks off and you can't figure out why.

To open it, look in the Sidebar (if the Sidebar isn't visible, toggle it with **View > Sidebar**). The Style Inspector lives there alongside panels like Properties and Styles. You can also find it listed as one of the Sidebar deck options.

Once it's open, just click into any text in your document. The Style Inspector immediately updates to show a tree of everything affecting that text. At the top you'll see **Paragraph Styles** — this tells you the paragraph style in use (e.g., "Text Body"). Below that is **Paragraph Direct Formatting**, which lists any manual overrides you've applied on top of the paragraph style, like toggling "Para Keep Together" to true.

See `fig01.png`.

Further down, you'll find **Character Styles** and **Character Direct Formatting**. If you've applied a character style like "Strong Emphasis," it shows up here along with its attributes — things like Char Font Char Set, Char Font Name, Char Font Style Name, and Char Weight. Any direct character formatting (say, you manually bolded a word or changed the font) appears separately so you can tell what came from a style versus what was hand-applied.

This distinction between style-based and direct formatting is the real power here. When formatting in a document looks inconsistent or broken, the Style Inspector lets you pinpoint whether the culprit is a rogue direct format override or a misapplied style.

For advanced users, the Style Inspector can also reveal hidden RDF (Resource Description Framework) metadata attached to text spans, paragraphs, and bookmarks. If you work with annotated text, the "Nested Text Content" item shows boundaries of nested annotated ranges and metadata fields.

You can also set custom color metadata field shadings on annotated text ranges to visually distinguish metadata categories in the editor. Toggle these on or off with **View > Field Shadings** or *Ctrl+F8*.

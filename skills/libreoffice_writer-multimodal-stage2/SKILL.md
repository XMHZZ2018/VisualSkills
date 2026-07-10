---
name: libreoffice_writer-multimodal-stage1
description: "Practical with-screenshots guides for LibreOffice Writer 7.3.7. Consult via the load_topic MCP tool — it returns the guide text and every figure in one atomic call."
---

# LibreOffice Writer 7.3.7 Knowledge (multimodal-v1)

## How to consult this skill

This skill exposes two MCP tools (already registered for you):

- **`load_topic(topic)`** — returns the chosen topic's `guide.md` AND every figure (PNG) in that topic folder as one tool response. **Use this instead of `Read` for any `*.md` or `figXX.png` inside this skill.**
- **`list_topics()`** — returns every topic path available, one per line.

Each entry in the TOC below has the form `[Title](<topic>/guide.md)`. The `<topic>` part (the path before `/guide.md`) is what you pass to `load_topic`. Example:

> To consult "Numbering Pages", call `load_topic("page-layout-basics/page-numbering")`. You will receive the guide text plus the 4 figures in that folder in a single tool result — no extra `Read` calls needed.

**Rules:**

1. Before any GUI action where you are unsure of the menu path / dialog / icon, find the matching topic in the TOC and call `load_topic` first.
2. You may call `load_topic` **at any step** of the trajectory, not only at the start. If the task moves into a new area (e.g. you started in page-layout and now need to deal with tables), call `load_topic` again for the new area.
3. Do **not** issue separate `Read` calls for `figXX.png` files inside this skill — they are delivered by `load_topic` automatically.

## Guides

### Introducing Writer

- [Writer Interface Overview](introducing-writer/writer-interface/guide.md) — Parts of the main Writer window, title bar, menus, toolbars, sidebar, and status bar
  - **Use when:** navigating menu bar and submenus, showing and hiding toolbars, customizing Sidebar decks and panels, docking and undocking toolbars, displaying vertical ruler, using Status bar controls
- [Context Menus, Dialogs, and Document Views](introducing-writer/menus-dialogs-views/guide.md) — Using right-click menus, dialog boxes, and switching between Normal, Web, and Full Screen views
  - **Use when:** right-click context menus, Format Paragraph dialog, Find & Replace dialog, Normal/Web/Full Screen view, zoom and view layout, Status Bar page layout
- [Creating and Opening Documents](introducing-writer/creating-and-opening-documents/guide.md) — Creating new documents from scratch or templates and opening existing files
  - **Use when:** creating blank writer document, opening existing document, using Start Center, browsing and applying templates, opening remote files, managing recent documents
- [Saving and Protecting Documents](introducing-writer/saving-and-protecting-documents/guide.md) — Saving in various formats, password protection, OpenPGP encryption, and working with remote servers
  - **Use when:** saving with a password, encrypting with GPG key, saving to .docx format, configuring AutoRecovery interval, setting default file format, saving to remote server
- [Navigating Documents](introducing-writer/navigating-documents/guide.md) — Moving quickly through a document using the Navigator, Go To Page, and other navigation tools
  - **Use when:** jumping to a specific page, using Navigator sidebar, navigating by object type, setting reminders in Navigator, renaming document objects, browsing headings and bookmarks
- [Undoing Changes, Multiple Views, and Closing](introducing-writer/undo-views-and-closing/guide.md) — Undoing and redoing edits, displaying multiple views, reloading, classifying, and closing documents
  - **Use when:** undoing and redoing multiple changes, displaying multiple views of same document, reloading document to last save, TSCP document classification, closing a document

### Working with Text: Basics

- [Selecting, Cutting, Copying, and Pasting Text](text-basics/selecting-and-editing-text/guide.md) — Methods for selecting text and using the clipboard to cut, copy, and paste
  - **Use when:** selecting text, extending selection with F8, adding non-consecutive selections, block selection mode, cut copy paste text, selection mode status bar
- [Finding and Replacing Text](text-basics/find-and-replace/guide.md) — Using the Find & Replace toolbar and dialog for basic text searches
  - **Use when:** find and replace text, Find toolbar, Find and Replace dialog, match case search, regular expressions search, paragraph style search
- [Inserting Special Characters](text-basics/special-characters/guide.md) — Inserting symbols, non-breaking spaces, dashes, and other special characters
  - **Use when:** inserting special characters via Special Character dialog, inserting non-breaking spaces and hyphens, inserting en dashes and em dashes, using formatting marks, AutoCorrect dash options, inserting Unicode symbols by name or code
- [Checking Spelling and Grammar](text-basics/spelling-and-grammar/guide.md) — Running spelling and grammar checks, managing dictionaries, and handling exceptions
  - **Use when:** checking spelling as you type, running Spelling dialog (F7), checking grammar as you type, adding words to dictionary, configuring English sentence checking rules, using AutoCorrect from spell check
- [Using Synonyms and the Thesaurus](text-basics/synonyms-and-thesaurus/guide.md) — Looking up synonyms and using the built-in thesaurus
  - **Use when:** finding synonyms via right-click, replacing words with Thesaurus dialog, Ctrl+F7 thesaurus shortcut, Tools > Thesaurus menu, installing language dictionaries for synonyms, looking up alternative words
- [Hyphenating Words](text-basics/hyphenation/guide.md) — Automatic and manual hyphenation settings and controls
  - **Use when:** inserting soft hyphens manually, enabling automatic hyphenation in paragraph styles, configuring hyphenation settings in Text Flow tab, tuning Writing Aids hyphenation options, hyphenating footnotes headers and footers
- [AutoCorrect, Word Completion, and AutoText](text-basics/autocorrect-autotext-and-completion/guide.md) — Configuring AutoCorrect replacements, Word Completion suggestions, and reusable AutoText entries
  - **Use when:** configuring AutoCorrect replacements, customizing Word Completion settings, creating and inserting AutoText entries, adding special character shortcuts, changing completion acceptance key, printing AutoText list via macro

### Working with Text: Advanced

- [Built-in Language Tools](text-advanced/language-tools/guide.md) — Using language-related tools including grammar checking, text-to-speech, and language settings
  - **Use when:** setting text language for selection/paragraph/all text, configuring default document language, installing spelling dictionaries, disabling spell-check for specific text, assigning language to paragraph styles, checking language via Status bar
- [Advanced Find and Replace](text-advanced/advanced-find-and-replace/guide.md) — Using regular expressions, paragraph styles, and other advanced options in Find & Replace
  - **Use when:** replacing paragraph styles in bulk, finding and replacing text formatting, similarity search in Find & Replace, using regular expressions in Find & Replace, clearing format criteria with No Format, fuzzy match configuration
- [Tracking Changes](text-advanced/tracking-changes/guide.md) — Recording, displaying, accepting, and rejecting changes in a document
  - **Use when:** tracking changes recording, accepting or rejecting changes, protecting tracked changes with password, comparing documents for differences, filtering changes by author or date, adding comments to tracked changes
- [Adding Comments](text-advanced/comments/guide.md) — Inserting, editing, navigating, and replying to comments in a document
  - **Use when:** inserting comments with Ctrl+Alt+C, changing comment author name, deleting comments, resolving and unresolving comments, navigating between comments, printing comments in margins or end of page
- [Using Footnotes and Endnotes](text-advanced/footnotes-and-endnotes/guide.md) — Inserting and managing footnotes and endnotes
  - **Use when:** inserting footnotes and endnotes, custom footnote characters, deleting and renumbering footnotes, configuring footnote numbering via Tools menu, formatting footnote appearance and separator lines
- [Cross-References and Navigator](text-advanced/cross-references-and-navigation/guide.md) — Linking to other parts of a document and rearranging content with the Navigator
  - **Use when:** inserting cross-references, inserting bookmarks, editing hyperlinks, rearranging headings with Navigator, configuring URL recognition, changing hyperlink colors
- [Inserting Material from Other Documents](text-advanced/inserting-external-content/guide.md) — Inserting text and objects from external files into the current document
  - **Use when:** inserting sections linked to external files, using Navigator drag modes, insert as link vs insert as copy, linking shared content across documents, Format Sections dialog
- [Line Numbering](text-advanced/line-numbering/guide.md) — Adding and configuring line numbers in the margin
  - **Use when:** enabling line numbering, setting line number interval and position, choosing line number format and character style, numbering specific paragraphs only, restarting line numbering at a specific value, adding line number separators

### Formatting Text

- [Formatting Paragraphs](formatting-text/paragraph-formatting/guide.md) — Applying paragraph styles and direct paragraph formatting including indents, spacing, alignment, and tab stops
  - **Use when:** setting paragraph alignment, adjusting line and paragraph spacing, configuring indentation and hanging indent, setting tab stops in Paragraph dialog, adding paragraph borders and drop caps, clearing direct formatting with Ctrl+M
- [Formatting Characters](formatting-text/character-formatting/guide.md) — Applying character styles and direct character formatting including fonts, size, color, and effects
  - **Use when:** changing font name/size/style, applying character styles, adjusting character spacing and kerning, inserting hyperlinks via Character dialog, highlighting text, clearing direct formatting
- [Formatting Lists](formatting-text/list-formatting/guide.md) — Applying list styles and direct list formatting for bulleted and numbered lists
  - **Use when:** creating bulleted lists, creating numbered lists, nesting list levels with Tab, Bullets and Numbering dialog, list paragraph styles, Sidebar bullet and numbering palettes
- [Autoformatting](formatting-text/autoformatting/guide.md) — Using AutoFormat to automatically apply formatting as you type
  - **Use when:** configuring AutoCorrect options, replacing smart quotes with straight quotes, capitalizing first letter of sentences, applying autoformat to entire document, toggling While Typing autoformat, accepting or rejecting autoformat changes

### Formatting Pages: Basics

- [Basic Page Layout and Margins](page-layout-basics/page-layout-setup/guide.md) — Setting up page size, orientation, and margins using page styles
  - **Use when:** setting page size and orientation, adjusting page margins, configuring gutter for double-sided printing, dragging margins on rulers, using Sidebar margin presets, modifying Default Page Style
- [Inserting Page Breaks](page-layout-basics/page-breaks/guide.md) — Inserting manual page breaks and controlling page flow
  - **Use when:** inserting manual page breaks, changing page style at break, controlling text flow across pages, keep with next paragraph setting, orphan and widow control, Insert More Breaks Manual Break dialog
- [Creating Headers and Footers](page-layout-basics/headers-and-footers/guide.md) — Adding, formatting, and customizing headers and footers
  - **Use when:** adding a header or footer, inserting header via menu or page marker, formatting header and footer text, adjusting header footer margins and spacing, setting different first page header, adding borders or background to header footer
- [Numbering Pages](page-layout-basics/page-numbering/guide.md) — Adding page numbers, changing number format, and restarting numbering
  - **Use when:** inserting page number fields in headers/footers, changing page number format to Roman numerals, restarting page numbering after title page, setting custom starting page number, adding page count field, chapter-based page numbering
- [Defining a Different First Page](page-layout-basics/first-page-setup/guide.md) — Configuring a distinct first page with a different page style
  - **Use when:** different first page header/footer, Same content on first page setting, chaining First Page and Default page styles, Format > Title Page dialog, restarting page numbering after title pages
- [Formatting Footnotes and Endnotes](page-layout-basics/footnote-endnote-formatting/guide.md) — Customizing the appearance and placement of footnotes and endnotes
  - **Use when:** formatting footnote location, customizing footnote separator line, setting maximum footnote height, adjusting footnote spacing, configuring Format > Page Footnote tab

### Formatting Pages: Advanced

- [Layout Methods and Columns](page-layout-advanced/layout-methods-and-columns/guide.md) — Choosing between layout methods and defining multi-column page layouts
  - **Use when:** setting up page columns, choosing layout method for columns/frames/sections, configuring column width and spacing, showing layout boundaries via Application Colors, using sections for multi-column pages, defining columns on a page style
- [Using Frames for Page Layout](page-layout-advanced/frames/guide.md) — Inserting, positioning, and linking frames for flexible page layout
  - **Use when:** inserting and positioning frames, setting frame anchor types, configuring frame borders and padding, linking and unlinking frames for text overflow, wrapping text around frames, drawing frames interactively
- [Using Tables for Page Layout](page-layout-advanced/tables-for-layout/guide.md) — Using tables as a structural layout tool for complex page designs
  - **Use when:** creating page layouts with tables, positioning elements in headers and footers, creating sideheads with tables, setting table column widths, configuring table spacing and borders, inserting borderless tables
- [Using Sections for Page Layout](page-layout-advanced/sections/guide.md) — Creating, editing, and formatting sections including linked and protected sections
  - **Use when:** inserting and naming sections, linking section content from external files, write-protecting sections with password, hiding sections conditionally, adding columns to part of a page, editing and removing sections via Format menu
- [Changing Page Orientation Within a Document](page-layout-advanced/page-orientation/guide.md) — Mixing portrait and landscape pages in the same document
  - **Use when:** mixed page orientation, inserting landscape page in portrait document, modifying Landscape page style, text flow break with page style, switching back to portrait, rotated headers on landscape pages
- [Defining Borders and Backgrounds](page-layout-advanced/borders-and-backgrounds/guide.md) — Adding borders and background colors or images to pages, paragraphs, and other elements
  - **Use when:** adding borders to frames/paragraphs/pages, setting background color, using bitmap image as background, applying gradients/patterns/hatching, adjusting background transparency, configuring shadow style

### Printing, Exporting, Emailing, and Signing

- [Printing Documents](printing-exporting/printing/guide.md) — Quick printing, the Print dialog, black-and-white printing, print preview, envelopes, and labels
  - **Use when:** printing a document, setting default printer, selecting page range, printing multiple pages per sheet, brochure printing, print preview, printing envelopes
- [Exporting to PDF](printing-exporting/exporting-to-pdf/guide.md) — Configuring PDF export options including security, initial view, and links
  - **Use when:** exporting document as PDF, PDF image compression and resolution, PDF/A archival and tagged PDF, setting PDF open and permissions passwords, digitally signing a PDF, PDF initial view and user interface options
- [Exporting to EPUB and Other Formats](printing-exporting/exporting-other-formats/guide.md) — Exporting documents to EPUB and other file formats
  - **Use when:** exporting directly as EPUB, configuring EPUB version and layout, setting EPUB cover image and metadata, exporting to XHTML or image formats, splitting EPUB chapters by heading or page break
- [Emailing and Digitally Signing Documents](printing-exporting/emailing-and-signing/guide.md) — Sending documents by email and applying digital signatures for authentication
  - **Use when:** emailing document as attachment, emailing as PDF or Word, digital signatures dialog, applying a certificate to sign, inserting a signature line, mail merge sending
- [Redaction and Removing Personal Data](printing-exporting/redaction-and-privacy/guide.md) — Stripping personal metadata and redacting sensitive content before sharing
  - **Use when:** redacting sensitive content in Writer, auto-redacting repeated terms, removing personal metadata before sharing, clearing version history, stripping author and user data, security options for personal data warnings

### Introduction to Styles

- [Understanding Styles](introduction-to-styles/understanding-styles/guide.md) — What styles are and how to use the Styles deck in the Sidebar
  - **Use when:** applying paragraph/character/page/frame/list/table styles, clearing direct formatting with Ctrl+M, opening Styles deck with F11, modifying or creating styles, auto-generating table of contents from styles
- [Applying Styles](introduction-to-styles/applying-styles/guide.md) — Methods for applying paragraph, character, page, frame, and list styles to content
  - **Use when:** applying paragraph styles via toolbar or keyboard shortcuts, applying character styles via Sidebar or context menu, applying page styles via Status bar or manual break, applying frame styles, applying list styles, using Fill Format Mode to batch-apply styles
- [Creating, Modifying, and Deleting Styles](introduction-to-styles/creating-and-modifying-styles/guide.md) — Creating new styles, modifying existing ones, and deleting custom styles with a worked example
  - **Use when:** creating styles from selection, updating styles from selection, loading styles from template, modifying styles via Style dialog, deleting custom styles, setting style inheritance and Next Style
- [Defining a Heading Hierarchy with Styles](introduction-to-styles/heading-hierarchy-with-styles/guide.md) — Using paragraph styles to establish a structured hierarchy of headings
  - **Use when:** assigning paragraph styles to outline levels, configuring Tools > Chapter Numbering dialog, setting up multi-level heading numbering, adjusting heading indent and position, mapping custom styles to heading hierarchy

### Working with Styles

- [Creating Custom Styles](working-with-styles/creating-custom-styles/guide.md) — Methods for creating new user-defined styles
  - **Use when:** creating custom paragraph/character/page styles, using Style dialog Organizer tab, setting style inheritance and parent styles, configuring Next Style for paragraphs, using New Style from Selection, resetting child style to parent defaults
- [Working with Paragraph Styles](working-with-styles/paragraph-styles/guide.md) — Configuring paragraph style options including indents, spacing, alignment, text flow, and outline level
  - **Use when:** applying paragraph indents and spacing, setting alignment and justified text options, controlling text flow and page breaks, assigning outline levels for table of contents, configuring drop caps, adding paragraph background color or gradient
- [Working with Character and Frame Styles](working-with-styles/character-and-frame-styles/guide.md) — Configuring character styles for inline formatting and frame styles for anchored objects
  - **Use when:** applying character styles, creating character styles, font effects and hidden text, frame styles for graphics, rotating text in character styles, spell-check language per character style
- [Working with Page Styles](working-with-styles/page-styles/guide.md) — Configuring page styles for layout, headers, footers, and columns
  - **Use when:** setting page margins and gutter, configuring paper size and orientation, creating and modifying page styles, mirrored layout for book printing, page numbering styles, setting up headers and footers per page style
- [Working with List Styles](working-with-styles/list-styles/guide.md) — Configuring list styles for bullets, numbering, and outline numbering
  - **Use when:** creating list styles, customizing bullet and numbering formats, adjusting list position and indentation, configuring multi-level outline lists, applying list styles to paragraph styles, customizing number separators and sublevels
- [Using the Style Inspector](working-with-styles/style-inspector/guide.md) — Inspecting applied styles and direct formatting on selected text
  - **Use when:** inspecting paragraph and character styles, identifying direct formatting overrides, opening Style Inspector sidebar, viewing RDF metadata on text, toggling field shadings for annotated text

### Working with Templates

- [Creating Documents from Templates](working-with-templates/using-templates/guide.md) — Using the Templates dialog to create a new document based on a template
  - **Use when:** creating document from template, opening Templates dialog, browsing template categories, setting default template, using Start Center templates, checking document template in File Properties
- [Creating and Editing Templates](working-with-templates/creating-and-editing-templates/guide.md) — Creating new templates, importing templates from other sources, and editing existing templates
  - **Use when:** creating a template from a document, saving as template via File menu, using document wizards for letters faxes agendas, importing templates from extensions site, editing an existing template, setting default template
- [Managing Templates](working-with-templates/managing-templates/guide.md) — Changing assigned templates, setting defaults, organizing template folders, and other management tasks
  - **Use when:** creating templates, editing templates, setting default template, resetting default template, organizing template categories, importing and exporting templates

### Images and Graphics

- [Adding Images to a Document](images-and-graphics/adding-images/guide.md) — Inserting images from files, clipboard, scanner, and the Gallery
  - **Use when:** inserting images via Insert > Image dialog, drag and drop images into document, linking vs embedding images, Edit Links to External Files dialog, scanning images into Writer, using Gallery sidebar for clip art
- [Positioning Images](images-and-graphics/positioning-images/guide.md) — Anchoring, aligning, wrapping text around, and arranging images within the page
  - **Use when:** anchoring images to page/paragraph/character, aligning image position on page, arranging overlapping image stacking order, setting text wrapping around images, editing contour wrapping, configuring default anchor type in Formatting Aids
- [Adding Captions to Images](images-and-graphics/image-captions/guide.md) — Inserting and formatting automatic captions for images and figures
  - **Use when:** adding captions to images, automatic captions via AutoCaption settings, Insert Caption dialog, caption numbering by chapter, manual caption with number range field, caption category and numbering style
- [Modifying Images](images-and-graphics/modifying-images/guide.md) — Cropping, resizing, rotating, and adjusting image color, contrast, and transparency
  - **Use when:** cropping images with crop tab, resizing with Type tab and Keep ratio, rotating and flipping images, adjusting image color and filters, setting image transparency, compressing images with Compress Image dialog
- [Using Drawing Tools](images-and-graphics/drawing-tools/guide.md) — Creating shapes, lines, and basic drawings directly in Writer
  - **Use when:** inserting shapes and lines, formatting drawing objects, positioning and resizing shapes, grouping and ungrouping objects, setting default drawing properties, showing the Drawing toolbar
- [Creating an Image Map](images-and-graphics/image-maps/guide.md) — Defining clickable hotspot regions on an image
  - **Use when:** creating an image map, adding clickable hotspots to an image, using the ImageMap Editor, drawing rectangle ellipse polygon hotspots, setting hotspot hyperlink address and frame target, attaching a macro to a hotspot
- [Managing the Gallery](images-and-graphics/gallery/guide.md) — Browsing, adding, and organizing clip art and media in the LibreOffice Gallery
  - **Use when:** adding images to Gallery theme, creating custom Gallery theme, deleting Gallery objects, browsing Gallery themes, installing Gallery extensions, Gallery Sidebar icon and detail view
- [Using Fontwork](images-and-graphics/fontwork/guide.md) — Creating styled, shaped, and textured text effects with Fontwork
  - **Use when:** creating fontwork text, changing fontwork shape, adjusting fontwork letter heights and alignment, fontwork character spacing, fontwork 3D extrusion, resizing and positioning fontwork objects
- [Generating Barcodes and QR Codes](images-and-graphics/barcodes-and-qr-codes/guide.md) — Inserting barcode and QR code graphics into a document
  - **Use when:** inserting QR codes, inserting barcodes, editing barcode settings, setting error correction level, Insert Object QR and Barcode dialog

### Lists

- [List Types and Basics](lists/list-types-and-basics/guide.md) — Overview of bulleted, numbered, and outline list types
  - **Use when:** creating bullet lists, creating numbered lists, creating outline lists, customizing list styles, changing list levels with Tab and Shift+Tab, adding custom toolbar buttons for lists
- [Combining Styles and Nesting Lists](lists/combining-styles-and-nesting/guide.md) — Using list and paragraph styles together and creating nested multi-level lists
  - **Use when:** combining paragraph and list styles, creating numbered paragraph styles, nesting ordered and unordered lists, configuring list levels with Tab and Shift+Tab, assigning numbering style on Outline & List tab, defining separate styles per list level
- [Outlining with Paragraph Styles](lists/outlining-with-styles/guide.md) — Using paragraph styles to create document outlines
  - **Use when:** assigning outline levels to paragraph styles, configuring Tools > Chapter Numbering, linking list styles to heading styles, creating single list style for outlining, promoting and demoting outline sub-levels, adding custom styles to Navigator and table of contents
- [Applying and Naming List Styles](lists/applying-list-styles/guide.md) — Applying list styles to content and understanding list style naming conventions
  - **Use when:** applying list styles via paragraph styles, nesting list levels with Tab or toolbar, restarting list numbering, customizing bullet symbols and number sequences, promoting and demoting list items, pairing paragraph styles with list styles
- [Formatting List Styles](lists/formatting-list-styles/guide.md) — Configuring number and bullet appearance, position, indent, and spacing for list styles
  - **Use when:** formatting list styles, customizing bullet characters, adjusting list indents and position, linking list style to paragraph style, configuring ordered list numbering scheme, restarting list numbering

### Tables

- [Creating Tables](tables/table-tools-and-creation/guide.md) — Table toolbar, menu tools, and methods for inserting and structuring tables
  - **Use when:** inserting a table via toolbar grid or dialog, converting text to table, converting table to text, nesting tables, AutoCorrect table creation with plus and hyphens, pasting spreadsheet data into Writer
- [Formatting Tables](tables/formatting-tables/guide.md) — Adjusting table layout, applying table styles, and formatting table text
  - **Use when:** table size and position alignment, text flow and page breaks for tables, column width adjustment, merging and splitting cells, table borders and padding, table background colors and images, table AutoFormat styles, cell number formatting, rotating text in table cells
- [Table Data and Operations](tables/table-data-and-operations/guide.md) — Entering data, sorting, using formulas, splitting, merging, and other table operations
  - **Use when:** navigating table cells with Tab and arrow keys, sorting table data with Table Sort dialog, using formulas in Writer tables, protecting and unprotecting table cells, inserting table captions, splitting and merging tables

### Mail Merge

- [Data Sources for Mail Merge](mail-merge/mail-merge-data-sources/guide.md) — Creating and registering address data sources for use in mail merge
  - **Use when:** setting up mail merge data source, registering external address book, connecting spreadsheet for mail merge, using Address Data Source wizard, testing data source connection
- [Creating a Form Letter](mail-merge/creating-form-letters/guide.md) — Building a form letter with merge fields from a data source
  - **Use when:** creating a form letter, mail merge fields from data source, registering address book data source, printing or saving merged letters, hiding blank lines with hidden paragraph, mail merge output to printer or file
- [Printing Mailing Labels and Envelopes](mail-merge/printing-labels-and-envelopes/guide.md) — Setting up and printing labels and envelopes using mail merge
  - **Use when:** printing mailing labels, printing envelopes, mail merge address fields, custom label dimensions, synchronize label contents, envelope sender and addressee setup
- [Using the Mail Merge Wizard](mail-merge/mail-merge-wizard/guide.md) — Step-by-step walkthrough of the Mail Merge Wizard to create form letters
  - **Use when:** creating mail merge form letters, matching address block fields, setting personalized salutation, adjusting mail merge layout, registering data source, printing or saving merged documents

### Tables of Contents, Indexes, and Bibliographies

- [Tables of Contents](toc-indexes-bibliographies/tables-of-contents/guide.md) — Creating, customizing, and updating a table of contents
  - **Use when:** inserting a table of contents, updating a TOC after heading changes, customizing TOC outline levels and scope, editing TOC entry structure and tab stops, assigning paragraph styles to TOC levels, configuring TOC background color
- [Alphabetic Indexes](toc-indexes-bibliographies/alphabetic-indexes/guide.md) — Adding index entries and generating an alphabetic index
  - **Use when:** creating index entries, using concordance file, generating alphabetic index, customizing index entries and columns, updating or deleting index, combining identical index entries
- [Other Types of Index](toc-indexes-bibliographies/other-indexes/guide.md) — Creating indexes of tables, illustrations, objects, and user-defined indexes
  - **Use when:** creating index of tables/illustrations/objects, inserting table of figures, using Insert Caption for index entries, viewing and editing index entries with Field Shadings, creating user-defined indexes, generating indexes via Table of Contents and Index dialog
- [Bibliographies](toc-indexes-bibliographies/bibliographies/guide.md) — Managing bibliography entries and generating a bibliography
  - **Use when:** inserting bibliography entries, editing citations, generating bibliography index, managing bibliography database, formatting numbered references, customizing Bibliography 1 paragraph style

### Master Documents

- [Master Document Overview](master-documents/master-document-overview/guide.md) — Purpose of master documents, using the Navigator, and managing styles across subdocuments
  - **Use when:** creating master documents, combining subdocuments via Navigator, managing styles across subdocuments, splitting large documents into subdocuments, using Toggle Master View in Navigator, generating cross-document TOC and index
- [Creating Master Documents](master-documents/creating-master-documents/guide.md) — Starting from scratch, combining existing documents, and splitting a document into master and subdocuments
  - **Use when:** creating master documents from scratch, combining existing documents into master document, splitting document by outline level, inserting subdocuments via Navigator, managing master document styles and templates, adding TOC and index to master document
- [Restarting Page Numbering](master-documents/page-numbering-in-master-documents/guide.md) — Controlling page numbering across subdocuments in a master document
  - **Use when:** restarting page numbering, creating paragraph style with page break, resetting page number in Text Flow tab, configuring Heading 1 for chapter numbering, master document page numbering, outline level for Table of Contents
- [Editing and Cross-Referencing](master-documents/editing-and-cross-referencing/guide.md) — Editing a master document and creating cross-references between subdocuments
  - **Use when:** editing master document styles via template, adding deleting renaming subdocuments, fixing broken subdocument links in Navigator, cross-referencing between subdocuments, inserting bookmarks and set references, using Insert Cross-Reference dialog
- [Templates and Final Export](master-documents/master-document-templates-and-export/guide.md) — Creating a master document template, exporting to a single file, and anchoring images
  - **Use when:** creating master document templates, exporting master document to single .odt, removing section protection via Format Sections, fixing image anchoring in master documents, saving as .otm template

### Fields

- [Field Basics and Document Properties](fields/field-basics/guide.md) — Quick field entry methods and using document property fields for metadata
  - **Use when:** inserting page number and date fields, toggling field shadings, updating fields with Ctrl+F9/F9, editing document description properties, adding custom document properties, inserting custom property fields via Ctrl+F2
- [Dynamic Fields and Numbering Sequences](fields/dynamic-fields/guide.md) — Using fields that change automatically, inserting fields via AutoText, and defining custom numbering sequences
  - **Use when:** inserting document property fields, fixing field content checkbox, saving fields as AutoText, defining custom number range variables, inserting numbering sequences via Variables tab, using Ctrl+F2 Fields dialog
- [Automatic Cross-References](fields/cross-reference-fields/guide.md) — Inserting and managing automatic cross-reference fields
  - **Use when:** inserting automatic cross-references, using Insert Cross-reference dialog, referencing headings and figures, setting bookmarks as reference targets, choosing cross-reference format options, cross-references vs hyperlinks
- [Fields in Headers and Footers](fields/fields-in-headers-and-footers/guide.md) — Using fields to display page numbers, dates, and other information in headers and footers
  - **Use when:** inserting page numbers in headers/footers, inserting date and time fields, displaying chapter names in headers, cross-referencing bookmarks or headings, using Insert Field More Fields Document tab, inserting total page count
- [Developing Conditional Content](fields/conditional-content/guide.md) — Using conditional fields, hidden text, hidden paragraphs, and input lists for variable document content
  - **Use when:** conditional text fields, hidden text fields, hidden paragraphs, hidden sections, setting document variables, switching document editions with conditions
- [Placeholder and Other Fields](fields/placeholder-and-other-fields/guide.md) — Using placeholder fields, miscellaneous field types, and classifying document contents
  - **Use when:** inserting placeholder fields, creating template placeholders, Insert Fields More Fields dialog, TSCP document classification, setting document security levels, pasting classification restrictions

### Forms

- [Form Basics](forms/form-basics/guide.md) — When to use forms and how to create a simple form in Writer
  - **Use when:** creating interactive forms, inserting form controls, enabling Design Mode, configuring form control properties, using Form Controls toolbar, enabling positioning grid for forms
- [Form Controls Reference](forms/form-controls/guide.md) — Overview of available form controls: text fields, checkboxes, list boxes, buttons, and more
  - **Use when:** inserting form controls in Writer, configuring control properties dialog, setting up list box and combo box entries, using Design Mode, assigning macros to buttons, managing tab activation order
- [Building a Simple Form](forms/form-example/guide.md) — Step-by-step example of designing and testing a simple form
  - **Use when:** inserting text box control, adding option buttons with group name, configuring list box entries, setting check box labels, using Form Controls toolbar and Design Mode, aligning form controls
- [Accessing Data Sources](forms/data-sources-for-forms/guide.md) — Connecting forms to databases and other external data sources
  - **Use when:** accessing data sources in Writer, creating a form for data entry, connecting form controls to database columns, Form Properties Data tab, entering data into a form, Form Navigation toolbar
- [Advanced Form Customization](forms/advanced-form-customization/guide.md) — Advanced form properties, macros, and custom validation
  - **Use when:** linking macros to form controls, assigning macro events to form elements, setting document read-only for forms, configuring database record permissions, formatting form control properties, setting max text length on form fields

### Spreadsheets, Charts, and Other Objects

- [OLE and DDE Objects](spreadsheets-charts-objects/ole-and-dde-objects/guide.md) — Understanding and inserting OLE and DDE embedded and linked objects
  - **Use when:** inserting OLE objects from file, creating new OLE objects, linking vs embedding OLE objects, editing embedded OLE objects, inserting DDE objects from Calc, displaying OLE as icon
- [Embedded Spreadsheets](spreadsheets-charts-objects/embedded-spreadsheets/guide.md) — Inserting and editing Calc spreadsheets within a Writer document
  - **Use when:** inserting OLE spreadsheet in Writer, pasting DDE link from Calc, editing embedded spreadsheet cells and formulas, managing sheets in embedded spreadsheet, formatting cells with Format Cells dialog, inserting or deleting rows and columns in embedded spreadsheet
- [Charts and Graphs](spreadsheets-charts-objects/charts-and-graphs/guide.md) — Creating, editing, and formatting charts and graphs in Writer
  - **Use when:** inserting a chart in Writer, choosing chart type, editing chart data table, formatting chart elements, resizing and positioning charts, adding titles and legends
- [Audio and Video](spreadsheets-charts-objects/audio-and-video/guide.md) — Embedding and playing audio and video media clips
  - **Use when:** insert audio or video files, link media files in documents, play media with Media Playback toolbar, insert media from Gallery sidebar, adjust video playback scaling, export documents with linked media
- [Formulas and Equations](spreadsheets-charts-objects/formulas-and-equations/guide.md) — Inserting mathematical formulas and equations using Math
  - **Use when:** inserting formulas via Insert Object Formula, numbered equations with fn AutoText, editing formula font size, changing formula typeface, using Math editor in Writer

### Customizing Writer

- [General LibreOffice Options](customizing-writer/general-options/guide.md) — Configuring user data, memory, view, print, paths, and security options for all of LibreOffice
  - **Use when:** setting user data for document properties, configuring default printer and paper warnings, customizing file paths for templates, substituting missing fonts, removing personal information on saving, changing application colors for margins and boundaries
- [Loading and Saving Options](customizing-writer/loading-and-saving-options/guide.md) — Setting default file formats, AutoRecovery, and compatibility options
  - **Use when:** configuring autorecovery interval, loading printer settings with document, setting default file format ODF or Word, enabling backup copy, editing document properties before saving, load/save general options
- [Writer-Specific Options](customizing-writer/writer-specific-options/guide.md) — Configuring options specific to Writer including view, formatting aids, tables, changes, and compatibility
  - **Use when:** configuring update links and tab stops, toggling formatting marks and direct cursor, setting default fonts for new documents, customizing table defaults and number recognition, change tracking appearance settings, Writer compatibility options for Word
- [Language Settings](customizing-writer/language-settings/guide.md) — Configuring languages, locale, writing aids, and dictionaries
  - **Use when:** setting locale and document language, installing spelling dictionaries, configuring automatic spell checking, enabling Asian and complex text layout languages, customizing grammar checking rules, managing user-defined dictionaries
- [Customizing Menus, Toolbars, and UI](customizing-writer/customizing-menus-toolbars-and-ui/guide.md) — Modifying menus, toolbars, and the user interface layout
  - **Use when:** adding menu commands, creating custom toolbars, changing toolbar icons, switching UI layout variants, customizing context menus, configuring Notebookbar tabs
- [Assigning Shortcut Keys](customizing-writer/keyboard-shortcuts/guide.md) — Creating and modifying keyboard shortcuts for commands and macros
  - **Use when:** assigning custom shortcut keys, Tools Customize Keyboard tab, binding macros to key combinations, saving and loading keyboard configuration .cfg files, deleting or resetting shortcut keys
- [Extensions and Macros](customizing-writer/extensions-and-macros/guide.md) — Assigning macros to events and adding functionality with extensions
  - **Use when:** installing extensions via Extension Manager, assigning macros to events, updating extensions, resetting keyboard shortcuts, browsing extensions online
- [Fonts, Colors, and Experimental Features](customizing-writer/fonts-colors-and-experiments/guide.md) — Adding custom fonts, defining custom colors, and enabling experimental features
  - **Use when:** installing custom fonts, adding custom colors via Area dialog, defining colors with RGB or Hex, enabling experimental features, outline folding in Writer, managing color palettes

### User Interface Variants

- [Selecting the User Interface](user-interface-variants/selecting-user-interface/guide.md) — Switching between Standard, Tabbed, and other interface modes
  - **Use when:** switching user interface layout, View User Interface dialog, Standard Toolbar vs Single Toolbar vs Tabbed, Apply to All vs Apply to Writer, enabling experimental UI variants, Tabbed Compact and Groupedbar Compact layouts
- [Tabbed Interface](user-interface-variants/tabbed-interface/guide.md) — Overview of the Tabbed interface with ribbon-like grouped tabs
  - **Use when:** switching to tabbed/ribbon interface, navigating Writer tab bar, using File/Home/Insert/Layout/References/Review tabs, contextual tabs for images/tables/drawings, customizing notebookbar icons, accessing hidden toolbar overflow icons
- [Compact and Contextual Interfaces](user-interface-variants/compact-and-contextual-interfaces/guide.md) — Using Tabbed Compact, Groupedbar Compact, and Contextual Single interface layouts
  - **Use when:** switching Writer UI layout, enabling Tabbed Compact interface, using Groupedbar Compact, Contextual Single toolbar, View > User Interface dialog, customizing toolbar space


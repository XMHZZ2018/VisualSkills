# Finding and Replacing Text (LibreOffice Writer 7.3.7)

Writer gives you two ways to hunt down text: a lightweight Find toolbar for quick searches, and a full Find and Replace dialog when you need more control. Both support wildcards, regular expressions, and even paragraph style matching — but let's start with the basics.

The **Find toolbar** is docked at the bottom of the Writer window by default, just above the Status Bar. If you don't see it, hit **Ctrl+F**, or go to **View > Toolbars > Find** (you can also reach it via **Edit > Find**). Just click in the search box, type your term, and press **Enter** to jump to the next match. Use the **Find Next** and **Find Previous** arrow buttons to move through results, or hit **Find All** to select every instance at once.

See `fig01.png`.

Toggle **Match Case** on the toolbar if you need an exact upper/lower case match. When you're done searching, close the toolbar by clicking the **X** button on the left or pressing **Esc** while the cursor is in the search box.

For replacing text — or for more advanced searches — open the full **Find and Replace** dialog. The quickest way is **Ctrl+H**, but you can also go to **Edit > Find and Replace**, or click the **Find and Replace** button on the Find toolbar. The dialog has a **Find** box and a **Replace** box: type what you're looking for up top, type what you want instead down below, then click **Find Next** to step through occurrences one at a time, or **Replace All** to swap them all in one shot. Click **Replace** to change the currently highlighted match and advance to the next one.

See `fig02.png`.

If you need finer control, click **Other options** to expand the dialog. This reveals additional checkboxes like **Match case**, **Whole words only**, **Regular expressions**, **Similarity search**, and more. You can even search by **Paragraph Styles** or use the **Attributes** and **Format** buttons to find text with specific formatting. It's a surprisingly powerful tool once you dig into those extras.

---

## UI Reference  —  Key Formatting Dialogs

_Scope: Find and Replace dialog (Ctrl+H): search/replace fields, Match case, Find All/Next_

These multi-tab dialogs provide detailed control over character formatting, paragraph layout, page styles, and search/replace.

## Find and Replace (Ctrl+H)

(see screenshot `ui-find-replace-dialog.png`)

Opened via Edit > Find and Replace… or Ctrl+H.

- **Find** text field (with history dropdown)
- **Match case** / **Whole words only** checkboxes
- **Replace** text field (with history dropdown)
- **Buttons:** Find All, Find Previous, Find Next, Replace, Replace All
- **Other options** (collapsible): Current selection only, Comments, Regular expressions, Similarity search (with Similarities… button), Diacritic-sensitive, Replace backwards, Paragraph Styles
- **Attributes…** / **Format…** / **No Format** buttons for format-aware search

## Character Dialog (Format > Character…)

(see screenshot `ui-character-dialog.png`)

**Tabs:** Font, Font Effects, Position, Hyperlink, Highlighting, Borders

- **Font tab:** Family, Style (Regular/Bold/Italic/Bold Italic), Size, Language, Features… button, font preview.
- **Font Effects tab:** Font Color + Transparency, Overlining style+color, Strikethrough style, Underlining style+color+Individual words, Case dropdown, Relief, Hidden/Outline/Shadow checkboxes.
- **Position tab:** Normal/Superscript/Subscript radio + raise/lower %, Rotation (0°/90°/270°) + Scale width + Fit to line, Character spacing + Pair kerning.

## Paragraph Dialog (Format > Paragraph…)

(see screenshot `ui-paragraph-dialog.png`)

**Tabs:** Indents & Spacing, Alignment, Text Flow, Outline & List, Tabs, Drop Caps, Borders, Area, Transparency

- **Indents & Spacing:** Before/After text indent, First line indent, Automatic; Spacing above/below paragraph; Line Spacing dropdown (Single/1.15/1.5/Double/Proportional/At least/Leading/Fixed); Activate page line-spacing.
- **Alignment:** Left/Center/Right/Justified radio; Last line dropdown; Expand single word; Text-to-text alignment; Text direction.
- **Text Flow:** Hyphenation settings, page/column breaks, orphan/widow control.
- **Tabs:** Tab stop position, type (Left/Right/Center/Decimal), fill character.

## Page Style Dialog (Format > Page Style…, Shift+Alt+P)

(see screenshot `ui-page-style-dialog.png`)

**Tabs:** Organizer, Page, Area, Transparency, Header, Footer, Borders, Columns, Footnote

- **Organizer:** Style name, Next style dropdown, Inherit from, Category, Contains description.
- **Page:** Paper format (size, width, height, portrait/landscape, paper tray), Margins (left/right/top/bottom/gutter), Layout settings (page layout, page numbers, gutter position).
- **Header/Footer:** Enable checkbox, margins, spacing, same content on left/right pages.
- **Columns:** Column count, width/spacing, separator line options.


# Advanced Find and Replace (LibreOffice Writer 7.3.7)

Open the Find & Replace dialog with **Ctrl+H** (or **View > Find & Replace**), then click **Other options** to reveal the full set of advanced features.

## Replacing Paragraph Styles

When you paste content from multiple sources, you often end up with a mess of unwanted paragraph styles. To fix this in bulk, check **Paragraph Styles** in the Other Options area. The *Search for* and *Replace* dropdowns will switch to listing every paragraph style in your document — just pick the one you want to hunt down, pick the replacement, and hit **Replace All**. Repeat for each style you need to clean up.

## Finding and Replacing Text Formatting

You can also search for specific character or paragraph formatting — bold, italic, a particular font size, and so on. These format criteria don't appear in the *Find* text box; instead they show up just below it. Check **Including Styles** if you want to match formatting applied through styles as well as direct formatting. Click the **Format…** button to open a dialog where you choose the attributes you're after (e.g., bold, 14 pt, Spacing above paragraph). Use **No Format** to clear any previous format criteria from the Find or Replace box.

See `fig01.png`.

To replace formatting on a specific word, type it in the *Find* box, then click into the *Replace* box and use **Format…** to set the new look. If you just want to change the formatting but keep the text, make sure the same word also appears in the *Replace* box — otherwise Writer will delete it.

## Similarity Search

Need a fuzzy match? Check **Similarity search** and click the **Similarities…** button to configure how many characters can be exchanged, added, or removed. For instance, setting exchange characters to 2 means "black" and "crack" would be considered similar. The **Combine** checkbox lets all three settings work together.

## Using Regular Expressions

For pattern-based searches, check **Regular expressions** under Other Options. Type your regex in the *Search for* box, and if needed, a replacement pattern in the *Replace* box (backreferences like `\n` work there too). Here are some handy patterns: a period (`.`) matches any single character; `[xyz]` matches one of those specific characters; `[x-y]` matches a range; `[^x]` matches anything *except* x; `\bstart` anchors to the beginning of a word; `end\b` anchors to the end; `$` marks a paragraph boundary; and `\n` finds a line break inserted with Shift+Enter. Note that `$` doesn't work as a replacement character — use `\n` instead, which inserts a paragraph marker when used in the *Replace* box.

Click **Find All**, **Replace**, or **Replace All** once your pattern is set. Prefer **Find Next** over **Replace All** when you're not 100% sure your regex is airtight.

---

## UI Reference  —  Key Formatting Dialogs

_Scope: Find and Replace Other options: Regular expressions, Similarity, Paragraph Styles, Format_

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


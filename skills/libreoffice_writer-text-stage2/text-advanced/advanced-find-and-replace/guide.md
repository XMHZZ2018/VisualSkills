# Advanced Find and Replace (LibreOffice Writer 7.3.7)

Open the Find & Replace dialog with **Ctrl+H** (or **View > Find & Replace**), then click **Other options** to reveal the full set of advanced features.

## Replacing Paragraph Styles

When you paste content from multiple sources, you often end up with a mess of unwanted paragraph styles. To fix this in bulk, check **Paragraph Styles** in the Other Options area. The *Search for* and *Replace* dropdowns will switch to listing every paragraph style in your document — just pick the one you want to hunt down, pick the replacement, and hit **Replace All**. Repeat for each style you need to clean up.

## Finding and Replacing Text Formatting

You can also search for specific character or paragraph formatting — bold, italic, a particular font size, and so on. These format criteria don't appear in the *Find* text box; instead they show up just below it. Check **Including Styles** if you want to match formatting applied through styles as well as direct formatting. Click the **Format…** button to open a dialog where you choose the attributes you're after (e.g., bold, 14 pt, Spacing above paragraph). Use **No Format** to clear any previous format criteria from the Find or Replace box.

The Find and Replace dialog is shown with the Other options section expanded. Beneath the Find text field, a format criteria label reads "Arial, 14 pt, Italic," demonstrating how selected formatting attributes appear just below the search box. A red annotation arrow points to the "Including Styles" checkbox on the right side of the Other options area, with a callout explaining that checking it includes formats in character and paragraph styles, while leaving it unchecked limits the search to direct (manual) formatting. At the bottom of the dialog, the "Format…" button is highlighted in blue, alongside the "Attributes…" and "No Format" buttons.

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

The Find and Replace dialog displays a "Find:" text field with a history dropdown at the top, followed by "Match case" and "Whole words only" checkboxes. Below that is a "Replace:" text field, also with a history dropdown. A row of action buttons — Find All, Find Previous, and Find Next — appears beneath the fields. The "Other options" section is expanded, revealing checkboxes for "Current selection only," "Comments," "Regular expressions," and partially visible options for "Replace backwards" and "Paragraph Styles" on the right side.

Opened via Edit > Find and Replace… or Ctrl+H.

- **Find** text field (with history dropdown)
- **Match case** / **Whole words only** checkboxes
- **Replace** text field (with history dropdown)
- **Buttons:** Find All, Find Previous, Find Next, Replace, Replace All
- **Other options** (collapsible): Current selection only, Comments, Regular expressions, Similarity search (with Similarities… button), Diacritic-sensitive, Replace backwards, Paragraph Styles
- **Attributes…** / **Format…** / **No Format** buttons for format-aware search

## Character Dialog (Format > Character…)

The Character dialog is open to the "Font" tab, with additional tabs visible along the top: Font Effects, Position, and Hyperlink. The Font tab shows a "Family" dropdown set to "Liberation Serif" with a scrollable list of available fonts below it (including Linux Biolinum Keyboard O, Linux Biolinum O, Linux Libertine Display O, and others). Below the font list are fields for "Style" (set to "Regular"), "Size" (set to "12 pt"), and "Language" (set to "English (USA)"). A partial font preview area is visible at the bottom of the dialog.

**Tabs:** Font, Font Effects, Position, Hyperlink, Highlighting, Borders

- **Font tab:** Family, Style (Regular/Bold/Italic/Bold Italic), Size, Language, Features… button, font preview.
- **Font Effects tab:** Font Color + Transparency, Overlining style+color, Strikethrough style, Underlining style+color+Individual words, Case dropdown, Relief, Hidden/Outline/Shadow checkboxes.
- **Position tab:** Normal/Superscript/Subscript radio + raise/lower %, Rotation (0°/90°/270°) + Scale width + Fit to line, Character spacing + Pair kerning.

## Paragraph Dialog (Format > Paragraph…)

The Paragraph dialog is open to the "Indents & Spacing" tab. Visible tabs along the top include Outline & List, Tabs, Drop Caps, Borders on the upper row, and Indents & Spacing and Alignment on the lower row. The Indent section contains numeric fields for "Before text," "After text," and "First line," all set to 0.00", each with minus and plus adjustment buttons, plus an "Automatic" checkbox. The Spacing section has "Above paragraph" and "Below paragraph" fields (both 0.00") and a checkbox labeled "Do not add space between paragraphs of the same style." The Line Spacing section at the bottom shows a dropdown set to "Single."

**Tabs:** Indents & Spacing, Alignment, Text Flow, Outline & List, Tabs, Drop Caps, Borders, Area, Transparency

- **Indents & Spacing:** Before/After text indent, First line indent, Automatic; Spacing above/below paragraph; Line Spacing dropdown (Single/1.15/1.5/Double/Proportional/At least/Leading/Fixed); Activate page line-spacing.
- **Alignment:** Left/Center/Right/Justified radio; Last line dropdown; Expand single word; Text-to-text alignment; Text direction.
- **Text Flow:** Hyphenation settings, page/column breaks, orphan/widow control.
- **Tabs:** Tab stop position, type (Left/Right/Center/Decimal), fill character.

## Page Style Dialog (Format > Page Style…, Shift+Alt+P)

The Page Style dialog is titled "Page Style: Default Page Style" and is open to the "Organizer" tab. Visible tabs along the top are Organizer, Page, Area, Transparency, Header, Footer, and a partially visible Borders tab. The Organizer tab displays a Style section with fields for "Name" (set to "Default Page Style"), "Next style" (set to "Default Page Style"), "Inherit from" (empty), and "Category" (set to "Custom Styles"). Below that is a "Contains" summary showing the page dimensions and settings: "11.69 inch + From top 0.79 inch, From bottom 0.79 inch + Text direction left-to-right" along with "Default Page Style + Not page line-spacing."

**Tabs:** Organizer, Page, Area, Transparency, Header, Footer, Borders, Columns, Footnote

- **Organizer:** Style name, Next style dropdown, Inherit from, Category, Contains description.
- **Page:** Paper format (size, width, height, portrait/landscape, paper tray), Margins (left/right/top/bottom/gutter), Layout settings (page layout, page numbers, gutter position).
- **Header/Footer:** Enable checkbox, margins, spacing, same content on left/right pages.
- **Columns:** Column count, width/spacing, separator line options.

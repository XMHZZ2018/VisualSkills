# Finding and Replacing Text (LibreOffice Writer 7.3.7)

Writer gives you two ways to hunt down text: a lightweight Find toolbar for quick searches, and a full Find and Replace dialog when you need more control. Both support wildcards, regular expressions, and even paragraph style matching — but let's start with the basics.

The **Find toolbar** is docked at the bottom of the Writer window by default, just above the Status Bar. If you don't see it, hit **Ctrl+F**, or go to **View > Toolbars > Find** (you can also reach it via **Edit > Find**). Just click in the search box, type your term, and press **Enter** to jump to the next match. Use the **Find Next** and **Find Previous** arrow buttons to move through results, or hit **Find All** to select every instance at once.

The Find toolbar appears as a narrow horizontal bar docked at the bottom of the Writer window, directly above the Status Bar. On the left is a red **X** close button, followed by a text input field labeled "Find toolbar" with a dropdown arrow, then upward and downward triangle arrow buttons for navigating matches, a **Find All** button, a **Match Case** checkbox, and a **Find and Replace** icon button on the right end. Below it, the Status Bar shows page number, word count, character count, and page style information.

Toggle **Match Case** on the toolbar if you need an exact upper/lower case match. When you're done searching, close the toolbar by clicking the **X** button on the left or pressing **Esc** while the cursor is in the search box.

For replacing text — or for more advanced searches — open the full **Find and Replace** dialog. The quickest way is **Ctrl+H**, but you can also go to **Edit > Find and Replace**, or click the **Find and Replace** button on the Find toolbar. The dialog has a **Find** box and a **Replace** box: type what you're looking for up top, type what you want instead down below, then click **Find Next** to step through occurrences one at a time, or **Replace All** to swap them all in one shot. Click **Replace** to change the currently highlighted match and advance to the next one.

The Find and Replace dialog is a modal window titled "Find and Replace" with a close button in the top-right corner. At the top is a **Find:** text field (shown containing the letter "x") with a dropdown history arrow, and below it are **Match case** and **Whole words only** checkboxes. Next is a **Replace:** text field, also with a dropdown arrow. A row of five buttons follows: **Find All**, **Find Previous**, **Find Next** (highlighted with a blue border as the default action), **Replace**, and **Replace All**. Below that, the **Other options** section is expanded, revealing checkboxes for **Current selection only**, **Comments**, **Regular expressions**, **Similarity search** (with a **Similarities…** button), **Diacritic-sensitive**, **Replace backwards**, and **Paragraph Styles**. At the bottom are three buttons — **Attributes…**, **Format…**, and **No Format** — along with **Help** and **Close** buttons in the lower corners.

If you need finer control, click **Other options** to expand the dialog. This reveals additional checkboxes like **Match case**, **Whole words only**, **Regular expressions**, **Similarity search**, and more. You can even search by **Paragraph Styles** or use the **Attributes** and **Format** buttons to find text with specific formatting. It's a surprisingly powerful tool once you dig into those extras.

---

## UI Reference  —  Key Formatting Dialogs

_Scope: Find and Replace dialog (Ctrl+H): search/replace fields, Match case, Find All/Next_

These multi-tab dialogs provide detailed control over character formatting, paragraph layout, page styles, and search/replace.

## Find and Replace (Ctrl+H)

The Find and Replace dialog is a compact window titled "Find and Replace" in the top-right corner of its title bar. It contains a **Find:** label with an empty text field highlighted in blue, **Match case** and **Whole words only** checkboxes beneath it, a **Replace:** label with its own text field, and a row of buttons: **Find All**, **Find Previous**, and **Find Next**. The **Other options** section is expanded below, showing checkboxes for **Current selection only**, **Comments**, **Regular expressions**, and partially visible options for **Replace backwards** and **Paragraph Styles** on the right side.

Opened via Edit > Find and Replace… or Ctrl+H.

- **Find** text field (with history dropdown)
- **Match case** / **Whole words only** checkboxes
- **Replace** text field (with history dropdown)
- **Buttons:** Find All, Find Previous, Find Next, Replace, Replace All
- **Other options** (collapsible): Current selection only, Comments, Regular expressions, Similarity search (with Similarities… button), Diacritic-sensitive, Replace backwards, Paragraph Styles
- **Attributes…** / **Format…** / **No Format** buttons for format-aware search

## Character Dialog (Format > Character…)

The Character dialog is shown open to the **Font** tab, with additional tabs visible along the top: **Font Effects**, **Position**, and **Hyperlink** (with more tabs likely scrolled out of view). On the Font tab, the **Family** field is set to "Liberation Serif" and a scrollable list below it shows available font families (Liberation Serif highlighted in blue, followed by Linux Biolinum Keyboard O, Linux Biolinum O, Linux Libertine Display O, and others). Below the list are **Style** set to "Regular", **Size** set to "12 pt", and **Language** set to "English (USA)", with a truncated font preview line at the bottom.

**Tabs:** Font, Font Effects, Position, Hyperlink, Highlighting, Borders

- **Font tab:** Family, Style (Regular/Bold/Italic/Bold Italic), Size, Language, Features… button, font preview.
- **Font Effects tab:** Font Color + Transparency, Overlining style+color, Strikethrough style, Underlining style+color+Individual words, Case dropdown, Relief, Hidden/Outline/Shadow checkboxes.
- **Position tab:** Normal/Superscript/Subscript radio + raise/lower %, Rotation (0°/90°/270°) + Scale width + Fit to line, Character spacing + Pair kerning.

## Paragraph Dialog (Format > Paragraph…)

The Paragraph dialog is shown open to the **Indents & Spacing** tab, with additional tabs visible along two rows at the top: **Outline & List**, **Tabs**, **Drop Caps**, **Borders** on the upper row, and **Indents & Spacing** and **Alignment** on the lower row. The tab content is divided into three sections: **Indent** (with "Before text," "After text," and "First line" spinner fields all set to 0.00″, plus an "Automatic" checkbox), **Spacing** (with "Above paragraph" and "Below paragraph" spinners both at 0.00″, and a "Do not add space between paragraphs of the same style" checkbox), and **Line Spacing** (with a dropdown currently set to "Single").

**Tabs:** Indents & Spacing, Alignment, Text Flow, Outline & List, Tabs, Drop Caps, Borders, Area, Transparency

- **Indents & Spacing:** Before/After text indent, First line indent, Automatic; Spacing above/below paragraph; Line Spacing dropdown (Single/1.15/1.5/Double/Proportional/At least/Leading/Fixed); Activate page line-spacing.
- **Alignment:** Left/Center/Right/Justified radio; Last line dropdown; Expand single word; Text-to-text alignment; Text direction.
- **Text Flow:** Hyphenation settings, page/column breaks, orphan/widow control.
- **Tabs:** Tab stop position, type (Left/Right/Center/Decimal), fill character.

## Page Style Dialog (Format > Page Style…, Shift+Alt+P)

The Page Style dialog is titled "Page Style: Default Page Style" and is shown open to the **Organizer** tab, with additional tabs visible along the top: **Page**, **Area**, **Transparency**, **Header**, **Footer**, and partially visible **Borders**. The Organizer tab displays a **Style** section with fields for **Name** ("Default Page Style"), **Next style** ("Default Page Style"), **Inherit from** (empty), and **Category** ("Custom Styles"). Below that, a **Contains** section summarizes the style properties as "11.69 inch + From top 0.79 inch, From bottom 0.79 inch + Text direction left-to-right… Default Page Style + Not page line-spacing."

**Tabs:** Organizer, Page, Area, Transparency, Header, Footer, Borders, Columns, Footnote

- **Organizer:** Style name, Next style dropdown, Inherit from, Category, Contains description.
- **Page:** Paper format (size, width, height, portrait/landscape, paper tray), Margins (left/right/top/bottom/gutter), Layout settings (page layout, page numbers, gutter position).
- **Header/Footer:** Enable checkbox, margins, spacing, same content on left/right pages.
- **Columns:** Column count, width/spacing, separator line options.

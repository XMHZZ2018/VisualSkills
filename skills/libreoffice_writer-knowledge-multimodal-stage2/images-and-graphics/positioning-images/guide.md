# Positioning Images (LibreOffice Writer 7.3.7)

When you drop an image into a Writer document, four settings govern how it sits on the page: **arrangement**, **alignment**, **anchoring**, and **text wrapping**. Getting comfortable with these gives you full control over your layout.

**Anchoring** tells Writer what the image is attached to. Right-click the image and look under **Anchor** in the context menu. *To Page* locks the image at a fixed spot on the page — great for letterheads or newsletter layouts where the image shouldn't move as you edit text. *To Paragraph* ties the image to a specific paragraph so it travels with it; handy for icons beside paragraphs. *To Character* is similar but anchors to a specific character position. *As Character* treats the image like a letter in the text flow, which is perfect for small inline icons or sequential screenshots. You can set a default anchor type under **Tools > Options > LibreOffice Writer > Formatting Aids**.

**Alignment** controls where the image sits relative to its anchor point. For fine-grained control, open the image dialog's **Type** tab and use the **Position** options. Pick a horizontal reference (Left, Right, or Center relative to the page text area or entire page) and a vertical one (Top, Bottom, Center from the top edge). If you select **From left** or **From top**, you can type an exact distance.

See `fig01.png`.

**Arranging** matters when images overlap. Use **Format > Arrange** (or right-click and choose from the context menu) to shuffle the stacking order: **Bring to Front**, **Forward One**, **Back One**, or **Send to Back**. For drawing objects there's also **To Background / To Foreground**. Tip: press the *Tab* key to cycle through overlapping objects until you reach the one you want.

**Text wrapping** defines how surrounding text behaves around the image. The most common options — available on the **Wrap** tab of the image dialog or via right-click — include: *None* (text only above and below), *Parallel* (text on all four sides), *Optimal* (text flows around the image, but Writer prevents narrow columns less than 2 cm), and *Through* (image sits on top of the text, useful with transparency). *Before* and *After* restrict text to one side. Use the **Spacing** section on the Wrap tab to add breathing room between image and text. If you need text to hug an irregular shape, select **Contour** wrapping, then right-click and choose **Wrap > Edit Contour** to open the Contour Editor and draw around the region you want to keep clear.

See `fig02.png`.

Note: when an image is anchored *As Character*, wrapping options are disabled — you can only adjust spacing. And contour wrapping isn't available for frames, only for images and drawing objects.

---

## UI Reference  —  Format Menu

_Scope: Anchor, Wrap, Arrange context-sensitive submenus_

The Format menu controls text styling, paragraph formatting, page layout, and document-level formatting options.

Read the screenshot `ui-format-menu.png` in this directory.

## Elements

- **Text** (►) — 19 text style commands: Bold (Ctrl+B), Italic (Ctrl+I), Single/Double Underline, Strikethrough, Overline, Superscript (Shift+Ctrl+P), Subscript (Shift+Ctrl+B), Shadow, Outline Font Effect, Increase/Decrease Size (Ctrl+]/[), case transforms (UPPERCASE, lowercase, Cycle Case Shift+F3, Sentence case, Capitalize Every Word, tOGGLE cASE), Small Capitals (Shift+Ctrl+K).
- **Spacing** (►) — Line Spacing (1, 1.15, 1.5, 2), Increase/Decrease Paragraph Spacing, Increase/Decrease Indent.
- **Align Text** (►) — Left (Ctrl+L), Centered (Ctrl+E), Right (Ctrl+R), Justified (Ctrl+J).
- **Clone Formatting** — Paint formatting from selection to other text.
- **Clear Direct Formatting** (Ctrl+M) — Remove all manual formatting, revert to style defaults.
- **Spotlight** (►) — Highlight formatting in document: Character Direct Formatting, Paragraph Styles, Character Styles.
- **Character…** — Opens the Character dialog (see [Formatting Dialogs](formatting-dialogs.md)).
- **Paragraph…** — Opens the Paragraph dialog (see [Formatting Dialogs](formatting-dialogs.md)).
- **Lists** (►) — No List (Shift+Ctrl+F12), Unordered List (Shift+F12), Ordered List (F12), Demote/Promote Outline Level, Move Item Down/Up (Ctrl+Alt+Down/Up), Insert Unnumbered Entry, Restart Numbering, Add to List.
- **Bullets and Numbering…** — Full list formatting dialog.
- **Theme…** — Document theme settings.
- **Page Style…** (Shift+Alt+P) — Opens the Page Style dialog (see [Formatting Dialogs](formatting-dialogs.md)).
- **Title Page…** — Add/configure title pages.
- **Columns…** — Multi-column page layout dialog.
- **Watermark…** — Insert or configure a watermark.
- Context-sensitive submenus (active when an object is selected): Image, Text Box and Shape, Frame and Object, Anchor, Wrap, Arrange, Rotate or Flip, Group.


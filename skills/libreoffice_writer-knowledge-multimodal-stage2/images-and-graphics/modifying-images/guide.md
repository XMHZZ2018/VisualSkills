# Modifying Images (LibreOffice Writer 7.3.7)

Writer comes with a surprisingly decent set of image-editing tools built right in. They won't replace GIMP for serious work, but for everyday tweaks — cropping, resizing, color adjustments — they do the job without ever leaving your document.

When you select an image, the **Image** toolbar appears (enable it permanently via **View > Toolbars > Image**). From here you can access filters, color adjustments, flip/rotate buttons, and a transparency slider. Two companion toolbars — the **Color** toolbar and the **Image Filter** toolbar — can be opened from it as well.

See `fig01.png`.

**Cropping** an image in Writer doesn't actually remove pixels — it just hides part of the image. The quickest way is to right-click the image, choose **Crop** from the context menu, then drag the crop handles that appear at the corners and midpoints. For precise control, right-click and select **Properties**, then go to the **Crop** tab. There you can enter exact values for **Left**, **Right**, **Top**, and **Bottom**. Two modes are available: **Keep scale** preserves proportions while changing the image size, and **Keep image size** maintains the dimensions but zooms in.

See `fig02.png`.

To **resize** an image, just drag its sizing handles. Hold **Shift** while dragging a corner handle to keep the original proportions. For exact dimensions, right-click the image, select **Properties**, and use either the **Crop** tab (scale percentages) or the **Type** tab (absolute width and height). On the Type tab, tick **Keep ratio** for symmetrical resizing, and use the **Original Size** button to revert any scaling.

**Rotating and flipping** is straightforward. Right-click the image and go to **Rotate or Flip** in the context menu — you'll find options for 90°, 180° rotations and vertical/horizontal flips. For arbitrary angles, right-click, choose **Properties**, open the **Image** tab, and type your desired angle in the **Rotation Angle** field. You can also rotate interactively: select the image, click the **Rotate** icon on the Image toolbar, then drag a rotation handle.

For **color and appearance** tweaks, use the Image toolbar's controls. The **Image Mode** dropdown lets you switch to grayscale, black-and-white, or watermark. The **Color** toolbar adjusts individual RGB channels plus brightness, contrast, and gamma. Various **Image Filters** — Smooth, Sharpen, Solarization, Aging, Posterize, and more — are available for quick special effects. If something goes wrong, just press **Ctrl+Z** to undo.

Bump up the **Transparency** percentage on the Image toolbar to make an image see-through — handy for watermarks or background images. And if you need to slim down your document's file size, right-click the image, choose **Compress**, and adjust quality or dimensions in the **Compress Image** dialog. Hit **Calculate New Size** to preview the savings before committing.

---

## UI Reference  —  Format Menu

_Scope: Image context submenu (when image selected)_

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


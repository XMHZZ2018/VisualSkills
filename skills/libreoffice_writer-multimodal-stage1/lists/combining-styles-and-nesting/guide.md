# Combining Styles and Nesting Lists (LibreOffice Writer 7.3.7)

Paragraph styles and list styles work hand-in-hand in Writer. When you apply a list style, the underlying paragraph style stays active — your font, size, and indentation all carry over. So the trick is to pair them intentionally rather than fighting one against the other.

Start by creating a list style you want to use for the paragraph — say, *MyNumberedList*. Then create a new paragraph style (something like *NumberedParagraph*). On the **Organizer** tab of the **Paragraph Style** dialog, set **Next Style** to *NumberedParagraph* so each new paragraph keeps the same style. Set **Inherited from** to *None* to keep things clean.

Now style the paragraph however you like — font, spacing, indents. Keep in mind that indentation is controlled by the list style, so avoid setting indents on the **Indents & Spacing** tab that would conflict. Head over to the **Outline & List** tab and assign *MyNumberedList* as the numbering style, then click **OK**.

See `fig01.png`.

For maximum control, consider defining separate paragraph styles for the first item (*List Start*), middle items (*List Continue*), and last item (*List End*). You can also create styles for nested levels or for an introductory paragraph before the list — handy for controlling spacing between the lead-in text and the first bullet.

## Nesting lists

A nested list is simply a list within a list — ordered inside unordered, or any combination you like. Instead of a flat sequence (1, 2, 3…), you get sub-items like 1, then a, b, c beneath it, with bullets or numbers at each level.

See `fig02.png`.

You have two approaches. The first is to use a single list style and configure multiple levels on the **Position** and **Customize** tabs. Each level can be formatted independently, and all levels stay connected. Press **Tab** to demote an item to the next level, or **Shift+Tab** to promote it back up. The preview pane shows how each level looks, and each level is tied to its own paragraph style.

The second approach is to create separate list styles — one per nesting level — and pair each with its own paragraph style. Neither method is strictly better; both give you the same options. Just remember that nested levels are always indented further than their parent, and each level typically uses a different bullet or numbering scheme.

# Creating Custom Styles (LibreOffice Writer 7.3.7)

Beyond the predefined styles that ship with LibreOffice, you can create your own custom styles to match your specific formatting needs. There are three ways to do this: drag-and-drop, the **New Style from Selection** icon on the Styles deck, and the Style dialog. The first two are quick and convenient because you can preview the results as you go, but if you want full control over the style — including its relationship to other styles — the Style dialog is the way to go.

To use the Style dialog, open the Styles deck on the Sidebar and pick the category of style you want (paragraph, character, etc.) by clicking the appropriate icon at the top. Then right-click anywhere in the styles list and choose **New** from the context menu. The dialog that appears depends on the style type you selected.

See `fig01.png`.

The **Organizer** tab is common to virtually all style categories and is where you set the essentials. Give your style a meaningful name in the **Name** field. The **Next Style** field (paragraph and page styles only) controls which style is automatically applied to the next element — handy for things like having a heading automatically followed by body text. **Inherit from** sets the parent style your new style will be based on; any properties you don't explicitly override are pulled from that parent. And **Category** lets you file it under one of the groups shown in the Styles deck for easier filtering.

If **AutoUpdate** is checked (available for paragraph and frame styles), be careful — Writer will push any manual formatting you apply to a paragraph right back into the style definition itself, which can unexpectedly reformat other parts of your document.

Style inheritance is a powerful concept here. When your new style inherits from a parent, changes to the parent cascade down to all child styles automatically. For example, if every heading style inherits from a common "Heading" parent, changing the font color on that parent updates all heading levels at once. Note, though, that any property you explicitly set on a child style won't be overridden by parent changes. You can always check which properties are unique to a style by looking at the **Contains** section on the Organizer tab, and hitting the **Standard** button at the bottom of the dialog resets a child style back to its parent's defaults.

See `fig02.png` for the hierarchical view showing style inheritance between Heading styles.

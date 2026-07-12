# Fixing Missing Windows and Dialogs (GIMP 2.10)

If you open GIMP and suddenly see nothing but a bare image window — no Toolbox, no Layers panel, nothing — you almost certainly hit **TAB** by accident. That's the default shortcut to hide every dock at once. Just press **TAB** again and everything comes back. You can also toggle this from **Windows > Hide Docks** in the menu bar.

See `fig01.png`.

One gotcha: **TAB** only works when the image canvas has focus. If you were clicking around inside a dock panel before things vanished, the shortcut might not respond. Click on the canvas first, then press **TAB**. Or just use the menu path above — that always works regardless of focus.

If specifically the **Tool Options** dialog is gone (you can select tools but have nowhere to adjust their settings), click the small triangle icon at the top-right corner of any remaining dock. From that menu choose **Add Tab > Tool Options** and the panel reappears in that dock. Alternatively, go to **Windows > Dockable Dialogs > Tool Options** — though this may drop the panel into a different dock. If it lands in the wrong spot, grab the "Tool Options" tab and drag it where you want it. To prevent future accidents, open the same triangle menu and check **Lock Tab to Dock**.

Can't find certain tool icons in the Toolbox? GIMP 2.10 groups similar tools together by default. Look for a small triangle in the bottom-right corner of a tool icon — that means more tools are hiding underneath. Hover over the icon (or click, depending on your settings) to reveal the rest. If grouping bugs you, disable it entirely under **Edit > Preferences > Toolbox**.

Finally, if you're in single-window mode and the tab bar showing your open images has disappeared from the top, head to **Windows > Show Tabs** and make sure it's checked. The tabs come right back.

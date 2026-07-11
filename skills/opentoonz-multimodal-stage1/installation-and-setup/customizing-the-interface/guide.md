# Customizing the Interface (OpenToonz 1.7)

OpenToonz organizes its workspace into **rooms** — preconfigured layouts of panes tailored to different tasks like drawing, animation, or compositing. You'll find the room tabs on the far right of the menu bar; just click one to switch. Double-click a tab to rename it, or drag tabs to reorder them. To add a fresh room, right-click the tab area and choose **New Room**. To remove one you no longer need, right-click its tab and pick **Delete Room** (you can't delete the room you're currently in). If things get messy, **Windows > Workspace > Reset to Default Rooms** brings everything back to factory state.

See `fig01.png`.

Within a room, you resize panes by dragging the separators between them. To bring in a new pane, open it from the **Windows** menu (it appears as a floating window), then drag its title bar toward the edge where you want it docked — release when you see the insertion highlight. Removing a pane is the reverse: drag its title bar out to undock it, then close the floating window. Double-click any pane's title bar to maximize it to full screen (double-click again to restore). Once your layout is dialed in, lock it with **Windows > Workspace > Lock Room Panes** so you don't accidentally rearrange things mid-session.

The **Command Bar** gives you quick-access buttons for your most-used tools and commands. Open it via **Windows > Command Bar**, then right-click it and choose **Customize Command Bar**. In the dialog that appears, drag items from the **Toolbar Items** tree on the right into the **Command Bar** list on the left. You can add separators for visual grouping, or right-click an item in the left list and hit **Remove** to drop it.

See `fig02.png`.

To change the interface language, go to **File > Preferences… > Interface** and pick from the **Language** dropdown — English, German, Spanish, French, Italian, Russian, Japanese, or Chinese are available. You'll need to restart OpenToonz for it to take effect.

Themes live in the same preferences panel: under **File > Preferences… > Interface**, use the **Theme** menu to switch between Default, Blue, Dark, Light, and Neutral. If you want to create your own theme, navigate to `OpenToonz stuff/config/qss`, duplicate an existing theme folder, rename both the folder and the QSS file inside, then edit the QSS (it's CSS-like syntax) and its associated PNG images to taste. Your new theme shows up in Preferences the next time you launch.

See `fig03.png` for the side-by-side comparison of Default and Light themes.

# Transitions & Animations (LibreOffice Impress 7.3.7)

## Slide Transitions

Transitions are the visual effects that play between slides during a show — fades, wipes, dissolves, and so on. They smooth out slide changes and add a polished feel. To set one up, click **Slide Transition** in the Sidebar (or go to **View > Slide Transition** if the deck isn't visible). Select the slide you want in the **Slides** pane or **Slide Sorter** view, then pick a transition from the list.

The Slide Transition sidebar panel displays a scrollable list of transition effects (such as None, Cut, Fade, Dissolve, Push, Wipe, and many others) at the top. Below the list, the **Modify Transition** section provides a **Variant** drop-down for directional or stylistic variants, a **Duration** spinner for the transition length in seconds, and a **Sound** drop-down to attach audio. At the bottom, the **Advance Slide** section offers two radio-button options — **On mouse click** and **After** with an adjustable time field — followed by the **Apply Transition to All Slides** button.

Once you've chosen a transition, fine-tune it under **Modify Transition**. Pick a **Variant** for directional styles, set the **Duration**, and optionally attach a **Sound**. Under **Advance Slide**, decide whether the slide moves forward *On mouse click* or automatically *After* a set number of seconds. If you want the same transition everywhere, hit **Apply Transition to All Slides** — though mixing too many different transitions can look messy.

To remove a transition, just open the **Slide Transition** deck, select the slide, and choose *None* at the top of the list. Slides that carry a transition are marked with a small star icon in the **Slides** pane.

You can also use transitions to play background music. In the **Slide Transition** deck, select *Other sound* from the **Sound** drop-down, browse to your audio file, and enable **Loop until next sound** if you want it to keep playing across slides. Note that the music file is linked, not embedded — it needs to be available on whatever machine runs the show.

## Object Animations

Animations work on individual elements within a slide — a title, a chart, a shape, a bullet list. Switch to **View > Normal**, select the object you want to animate, then open the **Animation** deck on the Sidebar (or right-click the object and choose **Animation**, or go to **View > Animation**).

Click the **Add Effect** button (the **+** icon) to register the object in the animation list. From there, choose a **Category** (Entrance, Emphasis, Exit, or Motion Paths), pick a specific **Effect**, and set how it **Start**s: *On click* waits for a mouse click, *With previous* fires alongside the prior animation, and *After previous* chains automatically after the last one finishes. Set the **Direction**, **Duration**, and **Delay** to taste.

The Animation sidebar panel shows an animation timeline list at the top, displaying each animated object with its sequence number and effect name. Below the list are toolbar buttons for **Add Effect** (+), **Remove Effect** (−), **Move Up**, and **Move Down**. The lower section contains drop-downs for **Category** (Entrance, Emphasis, Exit, Motion Paths), **Effect** (the specific animation within that category), **Start** (On click, With previous, After previous), and **Direction**, along with **Duration** and **Delay** spinners. At the very bottom are the **Play** button and the **Automatic Preview** checkbox.

For more control, click the **Options** button next to the **Direction** drop-down to open the **Effect Options** dialog. The **Effect** tab lets you add a sound, choose what happens after the animation (dim with color, hide, etc.), and control text animation mode — all at once, word by word, or letter by letter. The **Timing** tab gives you repeat and trigger options, including firing the animation on click of a specific shape. The **Text Animation** tab controls how grouped paragraphs are revealed — as one object, all at once, or by first-level paragraphs.

The Effect Options dialog is a tabbed window with three tabs: **Effect**, **Timing**, and **Text Animation**. The **Effect** tab shows a **Settings** section with a **Sound** drop-down, an **After animation** drop-down (with options like Don't dim, Dim with color, Hide after animation, Hide on next animation), and a **Text animation** drop-down (All at once, By word, By letter) with a percentage delay field. The **Timing** tab provides fields for **Start**, **Delay**, **Duration**, **Repeat** (including a count or "Until next click"/"Until end of slide"), and a **Trigger** section with radio buttons for animating as part of the click sequence or starting on click of a specified object. The **Text Animation** tab offers options for grouping text by paragraphs.

To reorder animations, use the **Move Up** / **Move Down** arrows in the Animation deck. To change an existing effect, select it in the animation list and adjust the controls. To remove one, select it and click **Remove Effect**. Always hit **Play** or enable **Automatic Preview** to sanity-check your work before running the full slide show.

A word of caution: animations can make a presentation more engaging, but heavy use gets distracting fast. Use them with purpose — to guide attention or reveal information progressively — rather than just for flash.

---

## UI Reference  —  Slide Menu

_Scope: Slide Transition entry opening sidebar panel_

The Slide menu manages slide creation, duplication, deletion, layout, master slides, visibility, and transitions.

The Slide menu is a vertical drop-down menu from the menu bar. It lists items top-to-bottom: **New Slide** (with Ctrl+M shortcut shown at right), **Duplicate Slide**, **Insert Slide from File...**, a **Layout** submenu arrow, a separator, **Delete Slide**, **Save Background Image...** (greyed out), **Set Background Image...**, **Slide Properties...**, another separator, **Change Slide Master...**, **New Master**, **Delete Master**, **Master Background** (checked), **Master Objects** (checked), **Master Elements...**, a separator, **Show Slide** / **Hide Slide**, **Rename Slide...**, **Jump to Last Edited Slide** (Shift+Alt+F5), **Move** submenu, **Navigate** submenu, a separator, **Summary Slide** and **Expand Slide** (both greyed out), and finally **Slide Transition** at the bottom.

## Elements

- **New Slide** (Ctrl+M) — Insert a blank slide after the current one
- **Duplicate Slide** — Create an identical copy of the current slide
- **Insert Slide from File...** — Import slides from another presentation
- **Layout** `▸` — 16 layout options: Blank Slide, Title Only, Title Slide, Title Content, Centered Text, Title and 2 Content, Title Content and 2 Content, Title 2 Content and Content, Title Content over Content, Title 2 Content over Content, Title 4 Content, Title 6 Content, Vertical Title Vertical Text, Vertical Title Text Chart, Title Vertical Text, Title 2 Vertical Text Clipart
- **Delete Slide** — Remove the selected slide (only available with 2+ slides)
- **Save Background Image...** — Save slide background (greyed unless custom background set)
- **Set Background Image...** — Set a background image for the slide
- **Slide Properties...** — Opens Slide Properties dialog (Slide, Background, Transparency tabs)
- **Change Slide Master...** — Change the master slide template
- **New Master** / **Delete Master** — Create or remove master slides
- **Master Background** ✓ / **Master Objects** ✓ — Toggle master background/objects visibility
- **Master Elements...** — Edit master slide elements
- **Show Slide** / **Hide Slide** — Toggle slide visibility during slideshow
- **Rename Slide...** — Rename the slide (opens dialog with name field)
- **Jump to Last Edited Slide** (Shift+Alt+F5) — Navigate to last edited slide
- **Move** `▸` — Slide to Start, Slide Up, Slide Down, Slide to End (context-sensitive)
- **Navigate** `▸` — To First/Previous/Next/Last Slide (context-sensitive)
- **Summary Slide** / **Expand Slide** — (greyed in normal conditions)
- **Slide Transition** — Opens the Slide Transition sidebar panel

---

## UI Reference  —  Slide Show Menu

_Scope: Start from First/Current Slide for previewing transitions_

The Slide Show menu controls presentation playback, rehearsal timings, custom shows, and presentation settings.

The Slide Show menu is a short drop-down menu from the menu bar containing five items: **Start from First Slide** (with F5 shortcut), **Start from Current Slide** (Shift+F5), **Rehearse Timings**, **Custom Slide Show...**, and **Slide Show Settings...** at the bottom.

The Slide Show Settings dialog is a wide dialog window titled "Slide Show." It is divided into several grouped sections arranged in columns. On the left, the **Range** section has three radio buttons: **All slides** (selected by default), **From:** with a slide-number spinner, and **Custom Slide Show** with a drop-down. In the center, the **Presentation Mode** section offers radio buttons for **Full Screen** (default), **In a window**, and **Loop and repeat after** with a time field, plus a **Show logo** checkbox that activates only with Loop mode. Below that, the **Options** section lists checkboxes: **Disable automatic change of slides**, **Change slides by clicking on background** (checked), **Mouse pointer visible**, **Mouse pointer as pen**, **Enable animated images** (checked), and **Keep Presentation always on top**. On the right side, the **Display** section has a presentation display drop-down, a **Presenter console** option set to Full screen, **Show navigation bar** with a **Buttons size** drop-down (set to Automatic). At the bottom right, the **Remote Control** section offers **Enable remote control**, a **Download App** link, and **Enable insecure WiFi connections**. The dialog has **OK**, **Cancel**, and **Help** buttons along the bottom.

## Elements

- **Start from First Slide** (F5) — Launch full-screen presentation from slide 1
- **Start from Current Slide** (Shift+F5) — Launch from the currently selected slide
- **Rehearse Timings** — Run slideshow in rehearsal mode, recording per-slide timings
- **Custom Slide Show...** — Create, edit, copy, delete, or start named subsets of slides
- **Slide Show Settings...** — Opens the Slide Show Settings dialog (see below)

## Slide Show Settings Dialog

The Slide Show Settings dialog is organized into clearly labeled sections: **Range** at top-left, **Presentation Mode** and **Options** in the center, and **Display** and **Remote Control** on the right, with **OK**, **Cancel**, and **Help** buttons at the bottom.

### Range
- All slides (default) / From: Slide N / Custom slide show

### Presentation Mode
- Full screen (default) / In a window / Loop and repeat after HH:MM:SS
- Show logo during pause (only with Loop mode)

### Presentation Options
- Disable automatic change of slides
- Change slides by clicking on background ✓
- Mouse pointer visible / Mouse pointer as pen
- Enable animated images ✓
- Keep Presentation always on top

### Display
- Presentation display dropdown
- Presenter console: Full screen
- Show navigation bar, Buttons size (Automatic)

### Remote Control
- Enable remote control, Download App link, Enable insecure WiFi connections

---

## UI Reference  —  View Menu

_Scope: Slide Transition and Animation sidebar panel entries for opening transition/animation decks_

The View menu controls presentation editing modes, UI panel visibility, and zoom settings.

The View menu is a long drop-down menu from the menu bar. At the top, it lists the editing modes as a group of radio-button items: **Normal** (selected), **Outline**, **Notes**, **Slide Sorter**, **Master Slide**, **Master Notes**, and **Master Handout**. Below a separator, toggle items with checkboxes appear: **Status Bar** (checked), **Slide Pane** (checked), **Views Tab Bar**, **Rulers** (Shift+Ctrl+R), **Comments** (checked), **Sidebar** (Ctrl+F5, checked), **Color Bar**, and **Navigator** (Shift+Ctrl+F5). After another separator come submenu entries: **User Interface...**, **Toolbars** ▸, **Grid and Helplines** ▸, **Snap Guides** ▸, and **Color/Grayscale** ▸. A further separator introduces the sidebar panel shortcuts: **Slide Layout**, **Slide Transition**, **Animation**, **Styles** (F11), and **Gallery**. At the bottom, a **Zoom** ▸ submenu provides zoom controls.

## Elements

### Editing Modes (radio buttons)
- **Normal** — Default slide editing mode with canvas, slides panel, and properties sidebar
- **Outline** — Text-only outline editor; toolbar switches to outline navigation tools
- **Notes** — Portrait layout with slide thumbnail + speaker notes area
- **Slide Sorter** — Grid of all slide thumbnails for reordering
- **Master Slide** — Edit the master slide template (title, outline levels, date/footer/number areas)
- **Master Notes** / **Master Handout** — Edit notes/handout master layouts

### UI Toggles (checkboxes)
- **Status Bar** ✓ — Toggle the bottom status bar
- **Slide Pane** ✓ — Toggle the left slide thumbnail panel
- **Views Tab Bar** — Tab bar with Normal/Outline/Notes/Slide Sorter tabs
- **Rulers** (Shift+Ctrl+R) — Horizontal and vertical rulers along the canvas
- **Comments** ✓ — Show/hide comment annotations
- **Sidebar** (Ctrl+F5) ✓ — Properties sidebar on the right
- **Color Bar** — Colour swatch bar at the bottom
- **Navigator** (Shift+Ctrl+F5) — Floating navigation panel

### Submenus
- **User Interface...** — UI mode selector
- **Toolbars** `▸` — Checklist of 30+ toolbars; enabled by default: Drawing, Presentation, Standard
- **Grid and Helplines** `▸` — Grid and guideline display options
- **Snap Guides** `▸` — Snap guide settings
- **Color/Grayscale** `▸` — Switch between Color, Grayscale, Black & White display

### Sidebar Panels
- **Slide Layout** / **Slide Transition** / **Animation** — Open the corresponding sidebar panel directly
- **Styles** (F11) — Opens the Styles panel
- **Gallery** — Opens the Gallery panel

### Zoom
- **Zoom** `▸` — Entire Page, Page Width, Optimal View, 50%–200%, Zoom & Pan, custom Zoom dialog

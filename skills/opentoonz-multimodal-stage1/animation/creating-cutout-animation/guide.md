# Creating Cutout Animation (OpenToonz 1.7)

Cutout animation works by splitting a character into separate sections — head, body, arms, legs — each on its own Xsheet column or Timeline layer. Instead of drawing new poses frame by frame, you animate by rotating and moving these pieces. The **Skeleton** tool ties everything together: it defines how sections connect and lets you pose them directly in the Viewer.

See `fig01.png`.

**Building the skeleton.** Select the **Skeleton** tool and set Mode to **Build Skeleton** in the tool options bar. Click a section in the Viewer to select it. You'll see a handle — a small yellow circle with an arm extending upward. Drag the yellow circle to reposition that section's pivot point (e.g., place the arm's pivot at the shoulder). Then drag the square at the top of the arm onto the parent section to create the link. Work outward from the trunk: trunk first, then upper arm linked to trunk, forearm linked to upper arm, hand linked to forearm, and so on down each limb.

See `fig02.png`.

**Using hooks for animated sections.** If a section is itself an animated level (say a trunk that bends across multiple drawings), a fixed center won't track the movement properly. Place hooks on each drawing with the **Hook** tool — enable **Snap** to align hooks precisely across levels. In Build Skeleton mode, click a hook's label to set it as that section's pivot, then drag the handle's square onto a hook on the parent section. When two hooks from different sections overlap perfectly, a shortcut label appears — just click it to link them instantly.

**Animating the model.** Switch the Skeleton tool's Mode to **Animate**. Click anywhere in the Viewer and drag to rotate the selected section; drag the green four-arrow square to translate it. Each manipulation auto-creates a keyframe on the current frame for that column. Enable **Global Key** in the tool options if you want every transformation channel (position, rotation, scale, shear) keyed together — handy for roughing out motion before adding squash-and-stretch later. To flip through alternate drawings in an animated level, click the level-name label next to the pivot and drag up/down.

**Inverse Kinematics.** Set Mode to **Inverse Kinematics** and the full skeleton displays with all joints. Now you can grab any endpoint — a hand, a foot — and drag it to a target position; all parent sections rotate automatically to accommodate. The pinned center (shown as a blue square, defaulting to the skeleton root) stays fixed in space. Click any joint's center to pin it instead — useful for walk cycles where you pin one ankle, then the other. Shift-click a center to temporarily pin it for the current frame only, constraining a shoulder or elbow while you pose the rest. To start fresh, right-click in the Viewer and choose **Reset Pinned Center**.

See `fig03.png`.

**Show Only Active Skeleton** in the tool options hides unrelated joints, which keeps complex rigs readable while you focus on one limb at a time.

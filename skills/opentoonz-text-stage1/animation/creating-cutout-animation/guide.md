# Creating Cutout Animation (OpenToonz 1.7)

Cutout animation works by splitting a character into separate sections — head, body, arms, legs — each on its own Xsheet column or Timeline layer. Instead of drawing new poses, you animate by rotating and moving those pieces.

**Building the skeleton.** Select the **Skeleton** tool and set its mode to **Build Skeleton**. Click a section in the Viewer to select it. Each section gets a handle: drag the **yellow circle** to position the pivot point (e.g., a shoulder joint), then drag the **square** at the top of the handle onto another section to parent it. Work outward from the trunk — set the trunk's pivot, link the arm to the trunk, link the forearm to the arm, and so on. To break a link, drag the square in the middle of the connecting wire away from the parent.

**Using hooks for animated sections.** If a section is itself an animated level (say, a bending trunk), fixed pivot points won't track the drawings. Place hooks on each drawing with the **Hook** tool (enable **Snap** to align hooks across levels precisely). In **Build Skeleton** mode, click a hook's label to promote it to that section's pivot, then drag the handle square to a hook on the parent section. When two hooks overlap perfectly, a shortcut label appears — click it to link instantly.

**Animating the model.** Switch the **Skeleton** tool mode to **Animate**. Click anywhere in the Viewer and drag to rotate the selected section; drag the **green square with four arrows** to translate it. Each adjustment auto-creates a keyframe on that frame. Enable **Global Key** in the tool options bar to keyframe all transforms (position, rotation, scale, shear) together — handy for adding squash-and-stretch later.

**Inverse Kinematics.** Set the mode to **Inverse Kinematics** and just drag any endpoint — the entire limb chain solves automatically. The **pinned center** (shown as a blue square) anchors one joint in place; click any other joint to re-pin it at a different frame, which is essential for walk cycles. **Shift-click** a joint to temporarily pin it for one pose only. To start fresh, right-click the Viewer and choose **Reset Pinned Center**.

Flip through alternate drawings for a section by clicking the **level name label** next to the pivot and dragging up/down. Toggle **Show Only Active Skeleton** in the tool options bar to declutter complex rigs.

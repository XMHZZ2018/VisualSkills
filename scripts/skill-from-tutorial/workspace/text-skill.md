---
name: chrome-clear-cookies
description: Configure Chrome to automatically delete cookies and site data every time the browser is closed, using the On-device site data settings.
---

# Set Chrome to Clear Cookies and Site Data on Close

## Steps

### Step 1: Open Chrome Settings

Click the Chrome address bar, type `chrome://settings/content/siteData`, and press **Enter**.

This navigates directly to the **On-device site data** settings page.

### Step 2: Select the auto-delete option

Under the **Default behavior** heading, you will see three radio button options:

1. **Allow sites to save data on your device** (default, currently selected)
2. **Delete data sites have saved to your device when you close all windows**
3. **Don't allow sites to save data on your device (not recommended)**

Click the **second radio button**: "Delete data sites have saved to your device when you close all windows."

The setting takes effect immediately — no Save button is needed.

### Step 3: (Optional) Add site exceptions

Below the radio buttons, there is a **Customized behaviors** section with three categories:

- **Allowed to save data on your device** — sites that keep their data even after Chrome closes
- **Always delete site data from your device when you close Chrome** — sites forced to clear regardless of the default
- **Not allowed to save data on your device** — sites blocked from storing any data

To add an exception, click the **Add** button next to the desired category, enter the site URL (e.g., `youtube.com`), and click **Add**.

## Verification

Confirm the second radio button ("Delete data sites have saved to your device when you close all windows") is filled/selected (solid blue circle).

## Notes

- The direct URL `chrome://settings/content/siteData` is the most reliable navigation path.
- If the direct URL does not work (older Chrome versions), navigate manually: **three-dot menu (⋮)** → **Settings** → **Privacy and security** → **Site settings** → scroll to **Additional content settings** → expand it → **On-device site data**.
- After enabling, you will be signed out of most sites when all Chrome windows close. Your Google Account stays signed in if you are signed in to Chrome itself.
- In older Chrome versions (pre-2023), the equivalent setting was a toggle called "Clear cookies and site data when you close all windows" found under **Privacy and security** → **Cookies and other site data**.

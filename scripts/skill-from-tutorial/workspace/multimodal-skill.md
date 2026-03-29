---
name: chrome-clear-cookies
description: Configure Chrome to automatically delete cookies and site data every time the browser is closed, using the On-device site data settings. Includes visual reference screenshots for each step.
---

# Set Chrome to Clear Cookies and Site Data on Close

## Steps

### Step 1: Open Chrome Settings

Click the **three-dot menu (⋮)** in the top-right corner of Chrome. From the dropdown, click **Settings**.

![Chrome three-dot menu with Settings option](./step_1_menu.png)

Alternatively, type `chrome://settings/content/siteData` in the address bar and press Enter to skip directly to Step 4.

### Step 2: Navigate to Privacy and security

In the Settings page, click **Privacy and security** in the left sidebar. The right pane will show options including "Delete browsing data," "Privacy Guide," "Third-party cookies," "Ad privacy," "Security," and **"Site settings."**

![Privacy and security section showing Site settings](./step_2_privacy.png)

Click **Site settings**.

### Step 3: Find On-device site data

Scroll down the Site settings page past the Permissions section. Look for **Additional content settings** near the bottom and click to expand it.

![Additional content settings section highlighted](./step_3_site_settings.png)

After expanding, scroll down and find **On-device site data** (described as "Sites can save data on your device"). Click on it.

![On-device site data option highlighted](./step_4_ondevice_option.png)

### Step 4: Select the auto-delete option

The On-device site data page shows a **Default behavior** section with three radio buttons:

1. **Allow sites to save data on your device** (default)
2. **Delete data sites have saved to your device when you close all windows**
3. **Don't allow sites to save data on your device (not recommended)**

![On-device site data page showing three radio options](./step_5_target.png)

Click the **second radio button**: "Delete data sites have saved to your device when you close all windows."

### Step 5: (Optional) Add site exceptions

Below the radio buttons is a **Customized behaviors** section. To keep specific sites signed in, click **Add** next to "Allowed to save data on your device," enter the site URL (e.g., `youtube.com`), and click **Add**.

## Verification

Confirm the second radio button is filled/selected (solid blue circle), as shown below:

![Second option selected with filled radio button](./step_6_verification.png)

The setting takes effect immediately — no Save button is needed.

## Notes

- The direct URL `chrome://settings/content/siteData` skips Steps 1–3 entirely.
- After enabling, you will be signed out of most sites when all Chrome windows close. Your Google Account stays signed in if you are signed in to Chrome itself.
- In older Chrome versions (pre-2023), the equivalent setting was a toggle called "Clear cookies and site data when you close all windows" under **Privacy and security** → **Cookies and other site data**.

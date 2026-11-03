# Bhadvengers

An independent, static fan-community site. It has no build step or package dependencies.

## Run locally

Double-click `Start Server.bat` in the project folder. It starts the website at `http://127.0.0.1:8000/` and opens it in your browser. Keep the server window open; press **Ctrl+C** there to stop the server. The local server only serves the public pages and site assets. Avoid running Python's generic `http.server` from the project folder; it can expose project files that are not part of the website.

## Temporary Cloudflare link

Install Python 3 and `cloudflared`, then double-click `Start Cloudflare Tunnel.bat`.
It starts the temporary tunnel and the website in the same window. Copy the
`https://*.trycloudflare.com` link printed by Cloudflare and share it while that
window remains open. Press **Ctrl+C** in that window to stop the tunnel and
local website.

Or, open PowerShell in this folder and run:

```powershell
.\Start cloudflare-Tunnel.ps1
```

The script stages only the site pages, styles, JavaScript, and images in a temporary folder, then opens the site on `127.0.0.1:8000` and creates a temporary public URL ending in `trycloudflare.com`. Project notes and design configuration are not served. Quick Tunnels do not require a Cloudflare login and are not permanent. Stop the regular `Start Server.bat` server first if it is already using port 8000.

Anyone with the public URL can view the website and its images while the tunnel is running. Uploaded join-form photos are resized and stored in each visitor's own browser; they are not uploaded or added to a roster shared between visitors.

## Member submissions

The join form compresses the selected photo and saves the profile in the current browser's local storage. New profiles appear on the Members page on that same browser and device; they are not uploaded or shared with other visitors.


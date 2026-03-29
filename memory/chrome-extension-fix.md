# OpenClaw Chrome Extension Relay Fix Guide

**Date:** March 28, 2026  
**Issue:** Chrome extension browser relay not connecting

## Symptoms
- Chrome extension shows "ON" but attach fails
- Badge shows "!" and stays stuck
- Error: "Wrong port: this is likely the gateway, not the relay. Use gateway port + 3"
- Error: "Relay not reachable/authenticated"

## Root Causes Found
1. OpenClaw version outdated (user had 2026.2.26, latest is 2026.3.24)
2. Gateway token mismatch - extension had "test123" but gateway config was different
3. Browser mode not enabled (`gateway.nodes.browser.mode` needed)
4. Wrong browser profile - needed "user" profile for existing-session, not "openclaw"
5. Missing config: `gateway.remote.token` needed to match `gateway.auth.token`

## Solution Steps

### 1. Update OpenClaw
```bash
openclaw update
openclaw doctor --fix
openclaw gateway restart
```

### 2. Set Gateway Token
Match the token in the Chrome extension manifest:
```bash
# Check your config file for the token, then:
openclaw config set gateway.auth.token test123
```

### 3. Enable Browser Mode
```bash
openclaw config set gateway.nodes.browser.mode relay
openclaw gateway restart
```

### 4. Configure User Profile (existing-session)
Edit config file (`~/.openclaw/openclaw.json`) to add:
```json
"browser": {
  "defaultProfile": "user",
  "profiles": {
    "user": {
      "driver": "existing-session",
      "attachOnly": true,
      "color": "#00AA00"
    }
  }
}
```

### 5. Set Remote Token
```bash
openclaw config set gateway.remote.token test123
openclaw gateway restart
```

### 6. Start User Profile
```bash
openclaw browser start --profile user
```

## Key Ports
- 18789 = Gateway (main service)
- 18791 = Browser control server
- 18792 = Relay (what Chrome extension connects to)
- 18800 = Managed browser (openclaw profile)

## Chrome Extension Version
- Latest version has bugs (2026.3.2)
- v2026.3.23+ includes browser attach fixes

## Lessons Learned
- Token must match between extension manifest and gateway config
- User profile = existing Chrome session (your logged-in state)
- Openclaw profile = isolated browser (no access to your logins)
- For TikTok/AI tool automation, need "user" profile to access logged-in sessions

---
**Contact:** justinclark3467@gmail.com
**Pika Account:** frankbot / HerbandSpice26!
# Session Memory - April 14, 2026

## Video Generation Tools Research
- Researched Pika, Runway, Kling, Luma for MainStreet Media
- Pika: max 20s, $8-35/mo, generous free tier
- Runway: max 16s, $12-76/mo, powerful editing
- Kling: max 2-3min, $9.99-19.99/mo, best value for 30s videos
- Luma: max 30s, $29.99-499.99/mo, expensive

### Kling Setup
- Installed Kling skill from GitHub (justinclark3467-source/Frank-master)
- Location: ~/.openclaw/workspace/skills/klingai/
- API Key: AYBtKRpFMAmBG9JADRQhCkf4mBmeFMrm (access key only)
- Problem: Need full AK/SK pair to generate JWT token
- API is reachable at api-singapore.klingai.com but returns "token expected 3 parts" error
- Skill installed and ready - just needs proper credentials

### Remote Browser via Tailscale
- User has Tailscale installed locally
- Need user's Tailscale IP to configure remote CDP profile
- Plan: Run Chrome locally with --remote-debugging-port=9222, connect via Tailscale

## AgentMail
- API Key saved: am_us_inbox_6947ef7cb2a7ab8201dd2346de18b0cca271931ceedf01e800adccf813a51b55
- Working, checked inbox - only test messages

---

# Previous Memory - April 11, 2026

## BrowserCat Integration (Just Added)
- Signed up for free account at browsercat.com
- API Key: TKDoxTWWufHnPZRcIelcIVzSyfHaKsWz4Vat5DOFIN2yy046e56GxwKEkCTxtKDP
- Free tier: 1,000 credits/month (~8 hrs browser time)
- Setup: Python venv at /root/.openclaw/venv with Playwright installed
- Test script: /root/.openclaw/workspace/browsercat_test.py
- Docs: /root/.openclaw/workspace/BROWSERCAT.md
- Note: Got 503 on first test - service may have temporary issues

## AgentMail Inbox
- mainstreetmedia@agentmail.to
- 4 old unread messages from April 2 cleaned up
- After replying, mark messages as read (new rule)

## Stories Project - COMPLETE
- Story 1 (Pepper): 48 letters total (Ma 1-24 + Joey 1-24)
- Location: /root/.openclaw/workspace/stories/

## Story 2: THE FAIR'S LIGHT (In Progress)
- World's Columbian Exposition, Chicago 1893
- Outline saved: /root/.openclaw/workspace/stories/STORY2-OUTLINE.md
- Just Eleanor's letters (to grandmother)
- 24 letters, target 850-950 words each
- Letters 1-6 written (1-2 in range, 3 needs trimming still)
- Letter 4: 889 words
- Letter 5: 929 words
- Letter 6: 925 words

### Characters
- BASIL CRAIN — 32, inventor
- ELEANOR VANCE — 24, daughter of steel magnate
- GRANDFATHER AUGUSTUS VANCE — 72
- GRANDMOTHER CLARA VANCE — bedridden
- MR. HARRISON VANCE — father
- MRS. CATHERINE VANCE — mother
- VIVIAN PENWORTH — social friend, starts rumors
- ARTHUR PENWORTH — her husband
- CONSTANCE BELMONT — shy friend

### Social Circle Plot
- Vivian and Arthur spread rumors about Eleanor/Basil
- Arthur tells Harrison, who confronts Eleanor
- Dad fast-tracks her engagement to Senator's son

### Plot Beats
- Act 1: Meet at fair
- Act 2: Engagement, sabotage, rumors
- Act 3: Basil arrested, maid steals notes, Eleanor recovers from warehouse (damaged)
- Act 4: Grandfather helps, walks into hearing room after 7 years public absence

---

## Story Ideas Folder (Saved)
- Location: /root/.openclaw/workspace/story-ideas/
- Idea 1: THE POTENTIAL TRADE - Fantasy, finite life-energy trading
- Idea 2: THE PAUSE - Sci-fi, civilization in time gaps
- Idea 3: THE MEMORY KEEPERS - Historical fantasy, ancient Egypt memory injection

## Previous Memory (April 2, 2026)

## Stories Project - COMPLETE
- Story 1 (Pepper): 48 letters total (Ma 1-24 + Joey 1-24)
- Location: /root/.openclaw/workspace/stories/

## Story 2: THE FAIR'S LIGHT (In Progress)
- World's Columbian Exposition, Chicago 1893
- Outline saved: /root/.openclaw/workspace/stories/STORY2-OUTLINE.md
- Just Eleanor's letters (to grandmother)
- 24 letters, target 850-950 words each
- Letters 1-6 written (1-2 in range, 3 needs trimming still)
- Letter 4: 889 words
- Letter 5: 929 words
- Letter 6: 925 words

### Characters
- BASIL CRAIN — 32, inventor
- ELEANOR VANCE — 24, daughter of steel magnate
- GRANDFATHER AUGUSTUS VANCE — 72
- GRANDMOTHER CLARA VANCE — bedridden
- MR. HARRISON VANCE — father
- MRS. CATHERINE VANCE — mother
- VIVIAN PENWORTH — social friend, starts rumors
- ARTHUR PENWORTH — her husband
- CONSTANCE BELMONT — shy friend

### Social Circle Plot
- Vivian and Arthur spread rumors about Eleanor/Basil
- Arthur tells Harrison, who confronts Eleanor
- Dad fast-tracks her engagement to Senator's son

### Plot Beats
- Act 1: Meet at fair
- Act 2: Engagement, sabotage, rumors
- Act 3: Basil arrested, maid steals notes, Eleanor recovers from warehouse (damaged)
- Act 4: Grandfather helps, walks into hearing room after 7 years public absence

---

## Story Ideas Folder (Saved)
- Location: /root/.openclaw/workspace/story-ideas/
- Idea 1: THE POTENTIAL TRADE - Fantasy, finite life-energy trading
- Idea 2: THE PAUSE - Sci-fi, civilization in time gaps
- Idea 3: THE MEMORY KEEPERS - Historical fantasy, ancient Egypt memory injection

## Previous Memory (April 1, 2026)
## Stories Project - COMPLETE
- Full collection: 24 Ma letters + 24 Joey letters = 48 stories
- Location: /root/.openclaw/workspace/stories/
- Docx versions: /root/.openclaw/workspace/stories/docx/

### Story Timeline - COMPLETE
**Ma Letters (Frank to Ma):**
- Ma 1-14: War begins, Frank finds Lucia in the grove
- Ma 15-18: Frank goes back to grove, discovers tunnels, finds Lucia
- Ma 19: Mission to move refugees through tunnels
- Ma 20: Battle, Frank injured by grenade, war ends
- Ma 21-22: Frank comes home with Lucia to Brooklyn
- Ma 23: Ma's journal entry to PA (deceased father) about Frank coming home
- Ma 24: Future letter - Frank in Italy with Lucia and son Antonio

**Joey Letters (Frank to Joey):**
- Joey 1-14: War, Frank finds book, learns about tunnels, Greek threat builds
- Joey 15-19: Greek escalates (inspector, lawyer, threats), Joey prepares
- Joey 20: Greek's men break in, Joey defeats them, Greek runs
- Joey 21-22: Frank comes home, Joey tells him about the Greek
- Joey 23: Joey's journal entry (matching Ma 23)
- Joey 24: Future letter - advice to Joey about fatherhood

### Word Counts
- Ma letters: 845-958 words each (target 850-950)
- Joey letters: 400-450 words each (target 400-450)

## Git History
- Latest commit: "Expand Ma 17-22 to complete story timeline"
- All stories backed up to git

## Previous Memory (March 26 - March 31)
[See above sections for full context on MainStreet Media, business planning, security, etc.]
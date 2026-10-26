# Changes

What's new in Brewtality, newest first.

Brewtality also has a Roblox version that copies this game exactly, and it reads this file to know what to copy. So every change to how the game plays, looks or sounds gets an entry here, in the same commit as the change. Write each entry like this:

```
### 2026-10-27 · Spitters aim ahead of you
- Spitter goo now leads a moving target instead of aiming where you stood.
- Numbers: goo speed 9 → 11; lead 0 → 0.35 s.
- Code: launchGoo, TYPES.spitter.
```

- **The first lines** are for players: what changed, in plain words.
- **Numbers** gives the old and new values, so they can be copied straight across.
- **Code** names the functions, tables or sections touched, so the change can be found without rereading the whole file.
- **Web only:** mark changes that only matter here, such as PeerJS co-op, the claude.ai page, the downloaded file, the test lab console, or this repo's tools. Write `Web only:` and the reason, so the Roblox side knows to skip it.
- **Fixes and refactors:** a bug fix is an entry too. A refactor with no visible effect gets one line.

---

### 2026-10-26 · A guide book on the title screen
- A red spellbook sits in the bottom-right corner of the title screen. It bobs, a crack of its cover breathes open on its own, and it falls open with its first page glowing when you point at it. Click it to read the guide.
- The guide is a parchment two-page spread (one page at a time on a phone) with four chapters on tabs: Controls (keyboard or touch, depending on the device), Brewing (scraping, the pot, all eight ingredients, and the combos you've found so far), Creatures (one page per creature and boss) and Co-op.
- Creature pages fill in as you meet things: until then they show the creature as an ink silhouette marked "???". Each page has a picture of the creature, what it shrugs off or is weak to, and how to deal with it.
- Turn pages with the arrow keys, the dog-eared corners, or the chapter tabs. Esc closes it.
- Numbers: book 150px in the corner (112px on a phone); cover opens 2.15 rad on hover; spread up to 900px wide and 62% of the screen tall; 22 pages (2 controls, 4 brewing, 14 creatures, 2 co-op).
- Saves: creatures you've met are kept between runs (`slingcam.seen`). A creature counts as met once it's out in the open in front of you during a run, or when a boss's intro banner plays. The test lab and the title screen don't count.
- Code: new `guide` section (the book, the creature pictures, the pages, `SCREENS.guide`), `buildModel` (pulled out of `spawnEnemy` so the guide can build a creature on its own), `seen` and `meetCreature` in data, `bossIntro`, the enemy-label pass in the loop, `uiNav`.
- Roblox note: the creature pictures are taken from the real models; a viewport frame per page would do the same job.

### 2026-10-26 · Patch notes
- This file, linked from the README.
- Web only: CHANGES.md, CLAUDE.md and tools/dev (a debug build for testing); the game itself is unchanged.

### 2026-10-23 · Stage 3: the Veiled Queen
- The Gloom Moths' mother joins the boss pool from floor 2, with her own floor, the Silk Halls.
- This log starts here: the Roblox version is being built up to this point (commit f7311a8), and everything above this entry is new to it.

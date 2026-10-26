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

### 2026-10-26 · Patch notes
- This file, linked from the README.
- Web only: CHANGES.md, CLAUDE.md and tools/dev (a debug build for testing); the game itself is unchanged.

### 2026-10-23 · Stage 3: the Veiled Queen
- The Gloom Moths' mother joins the boss pool from floor 2, with her own floor, the Silk Halls.
- This log starts here: the Roblox version is being built up to this point (commit f7311a8), and everything above this entry is new to it.

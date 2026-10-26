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

### 2026-10-26 · The Big Baby, turret orbs, and the guide in the pause menu
- **The Cyclops Chief is now the Big Baby**: a giant cyclops baby in a blue bonnet, a nappy and booties, with a dummy in its mouth and a rattle for a club. Same stairs-guarding spot from floor 1, same health.
- **It charges from floor 1** (was floor 3). A red lane lights up, then it runs. If it catches you it stops there. If it misses, it runs into the wall, sits down hard on its bottom and bawls for 3 s (was 1.8 s dazed): legs out, rubbing its eye, and that's your chance. The crash brings rocks down from the ceiling.
- **Tantrums replace its ground slam**: it spits its dummy out, wails, and stomps 4 times (6 once enraged). Every stomp hurts anyone inside the red ring round it and shakes rocks loose. It can throw one from across the room too, not just up close.
- **Falling rocks**: a red outline on the floor for half a second, then a rock drops out of the ceiling there (1 heart if you're under it) and crumbles away. Every other rock lands near a player; the rest land anywhere. Dust rains from the ceiling when it happens.
- Moves by floor: charge 1, rock toss 2, rage 3 (was 2), aftershocks 4 (now after a tantrum). First meeting says MIND THE CEILING. The Cyclops King is unchanged.
- **Turrets fire slow glowing red orbs** instead of dark darts: much easier to see and step aside from. Still aimed where you're standing, still hit creatures too.
- **COMBOS is gone from the title menu** (the guide book has a combos page). **The pause menu's COMBOS button is now GUIDE**, opening the guide book mid-run.
- Test lab: the Big Baby has TANTRUM and ROCKFALL instead of GROUND SLAM.
- Numbers: Big Baby (TYPES.chief) name 'Cyclops Chief' → 'Big Baby', colour 0xB8745A → 0xE8A28A; wall-crash daze 1.8 → 3.0 s (BABY_SIT); crash rocks 4 + floor (max 8); tantrum ring radius 2.4, 1 damage per stomp, wind-up 0.75 s then a stomp every 0.34 s, rocks per stomp 2/1 alternating; ranged tantrum chance 0.3/s when farther than reach + 1.2 and off cooldown; rock warning 0.5 s, falls from 0.1 below the ceiling at −4 m/s plus 30 m/s² gravity, hit radius 0.8, 1 damage, rubble lasts 1.6 s. Turret shot speed 10 → 3.6, radius 0.15 (glow halo ×1.8), lifetime 3 → 7 s, kill text DARTED → ZAPPED.
- Code: buildBaby (new; buildModel uses it for 'chief'), TYPES.chief, BOSS_MOVES.chief, bossIntro, bossCharge (the baby stops on a hit and sits on a wall), new section "the Big Baby" (ceilingRock, rockfall, startTantrum, endTantrum, babyTantrum, tantrumStomp, spitDummy, babyPose), enemyLook calls babyPose, the enemy AI loop (tantrum instead of the third-swing slam, and at range), SFX.wah, LAB_MOVES, LAB_NOTES.chief, guide BEASTS chief/king text; turrets: orbGeo/orbMat/orbHaloMat replace dartGeo in updateTraps; menus: SCREENS.title, SCREENS.pause, removed SCREENS.combos, comboGrid, renderMenu and the .combos/.cb CSS.
- Web only: co-op guests get the baby's sitting and tantrum state in the snapshot's last slot ([sitting, tantrum]) and the falling rocks as `goo` events with k: 'crock'.

### 2026-10-26 · Charged bonks, contact damage, spikes, and rancid on pickup
- **The bonk charges.** Tap for a jab: 1 damage, and it no longer dazes or shoves, so it can't interrupt an attack. Hold 1 s for a heavy bonk: 2 damage, dazes and shoves (bosses take the damage but aren't interrupted). Hold 2 s for a BIG BONK: 4 damage, a big shove that can slam them into a wall, and it staggers bosses too. You walk at 55% speed while winding up; the crosshair ring fills white, then orange at heavy, then flashes red at full; the ladle hauls back over your shoulder and trembles when it's full. A click sounds at heavy and a ding at full. The "every third bonk in a row is a BIG BONK" rule is gone.
- **Walking into a creature hurts** (1 heart, and you bounce off). Dazed, frozen and floating creatures are safe to touch. Enemies walking up to you don't count, only you walking into them.
- **Spiky creatures:** the Stumpling (pale thorns round its back and sides) and the Tin Knight (spiked pauldrons and a spike on its shield). Bonking one with anything less than a full charge pricks you for 1 heart. The first prick in a run shows a tip.
- **Spoilage is a roll, not a timer.** Doom shrooms, glowcaps, frost and cyclops eyes picked up in the dungeon (scraped, or dropped by a creature) come up rancid 1 time in 5. Nothing goes off while you carry it any more. Feathers, bog water, horns, iron, shop buys, fountain water and your starting shelf are always fresh. The pot screen's freshness bars are gone.
- **Preserving Salt** halves the rancid chance (was: ingredients keep twice as long). **Fermenting Jar** doubles it and still makes rancid extras hit everyone. With both, it's back to 1 in 5.
- **The chalked controls on the first room's floor are gone** (the guide book covers them). Floor decor in that room is no longer kept clear of where the chalk was.
- The guide's controls, scraping, Stumpling and Tin Knight pages, its SPIKY tag, the shop tags for the salt and jar, and the out-of-brew tip are updated to match.
- Numbers: jab / heavy / big damage 1 / 2 / 4 (was 1, and 2 on every third); hold for heavy 1.0 s, for big 2.0 s; daze none / 0.6 s / 1.1 s (bosses: none / none / 0.6 s; heavy creatures ×0.6); shove none / 3.5 / 7 (bosses ×0.25, heavy ×0.6); cooldown after a jab 0.55 s, after a heavy or big 0.4 s (was 0.48 s); walk speed while charging ×0.55; contact damage 1, reach your body + creature radius + 0.85, only while you're moving toward it (within 60°); spike prick 1; rancid chance 0.2 (salt ×0.5, jar ×2). Removed: ING `life` (80/65/45/70 s), the starting eye's 30 s head start.
- Code: `bonkDown`/`bonkUp`/`bonkTick`/`bonkTier` replace `bonk`; `bonkLand(tier)`; `BONK_HEAVY`, `BONK_FULL`; `vmState.charge`; the `#power` ring; `CONTACT_DMG` and the contact check in the player movement block; `spike()`, `TYPES.stump.spiky`, `TYPES.knight.spiky`, `buildStump`, `buildKnight`; `run.spikeTip`; `RANCID_CHANCE`, `rancidChance`, `gather` (replaces `checkSpoilage`, `lifeOf`, `freshness`); `ING.*.perishable`; `ITEMS.salt`, `ITEMS.jar`; `stockUp`; removed `drawChalk`, `chalkControls` and the start room's chalk keep-clear check in `buildRoom`; input handlers for V, right mouse and the touch BONK button (hold and release).

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

# Brewtality (web)

A first-person dungeon crawler where you brew potions and fling them at things with a ladle. The whole game is `index.html`: one file of HTML, CSS and about 550 KB of JavaScript on three.js r128 (loaded from cdnjs). A few people play it now, and the user wants it polished, so check every change in a browser before it ships.

## Two versions, two chats

There's also a Roblox version, an exact copy of this game, built in a separate chat in `~/Documents/brewtality-roblox` (a private repo).

- **This game is the source of truth.** The Roblox chat copies from it, never the other way round.
- **Don't touch the Roblox repo from here.**
- **Log every change in `CHANGES.md`, in the same commit as the change.** Give what players notice, the old and new numbers, and the functions touched. The format is at the top of that file.
  - That file is how the Roblox chat finds out what to copy. A change that isn't logged there won't reach Roblox.
  - Mark changes that only matter on the web (PeerJS, the claude.ai page, this repo's tools) as `Web only:`.

## Where it ships

- **GitHub:** https://github.com/tortleman383-blip/brewtality (public), branch `main`. Players use the Pages link, https://tortleman383-blip.github.io/brewtality/, and just refresh after a push. `README.md` is the players' guide (controls, bosses, co-op), so update it when those change.
- **claude.ai:** https://claude.ai/artifact/KwWrjH8e3H1NykSeSoypn4 is the same file, declared with the `room` and `user` capabilities so co-op works there.
  - Read it first, then publish `index.html` with `url` set to that link, keeping its capabilities.
  - A publish without `url` makes a separate copy with no co-op. That happened once.
- **Commits:** use `Treviathan <228856324+tortleman383-blip@users.noreply.github.com>`. It's already set in this clone's git config. Never use the user's personal email.
- **Pushing:** the user's GitHub token is only ever typed into a terminal by the user. Never ask for it in chat. When commits are ready, ask them to run `git push` in their terminal from this folder.

## Checking your work

1. **Syntax:** after every edit, run `python3 tools/dev/check.py` (it runs `node --check` on the game's script).
2. **In the browser:**
   - Run `python3 tools/dev/build.py`, then leave `python3 tools/dev/serve.py` running, and open http://127.0.0.1:8766/game.html in the browser pane.
   - Confirm `window.__errs` is empty and the console has no errors, play the change, and send the user a screenshot.
   - `window.__ev(src)` evaluates code inside the game's own scope, for jumping floors, spawning things or reading state.
   - `window.__snapReq = 'x.png'` saves the next frame to `tools/dev/out/`.
   - The **TEST LAB** on the title screen (Esc opens its console) runs any creature's attacks on demand.
3. **Co-op:** open `game.html?mock` in two tabs. They share a fake claude.ai room, so you can watch both sides of a sync.

## Finding your way around

- **Sections:** each section of the script starts with a `/* ===== name ===== */` header. `grep -n '/\* =====' index.html` lists them: data, audio, three setup (rooms, THEMES, BIOMES, buildRoom), creatures, brew logic, menus, the brewing station, bosses, the Mimicshroom, the Veiled Queen, traps, the den, the goblin shop, room flow, the brewer, co-op, loop.
- **Bosses:**
  - Each boss gets an entry in `BOSS_POOL` and `BOSS_MOVES` (moves learned by floor), a `BIOMES[bossId]` (`fight`, `start`, `boss` and `vault` themes, which dress the whole floor), and `LAB_SUBJECTS`/`LAB_MOVES` for the test lab.
  - No boss may hard-require an ingredient: the bonk always works.
- **Co-op:**
  - Floors come from seeded `genFloorRaw` (`withSeed`), and room decor is seeded by `r.dseed`, so partners see identical rooms.
  - The host runs fights and guests get snapshots.
  - Boss effects for guests ride the existing `goo` topic with a `k` field, so new rooms need no new topics.
- **Boss plan:**
  - Done: the pool with learned moves, the Mimicshroom (the Lurker and four bugs), and the Veiled Queen.
  - Talked about for later: a Bog Mother (splits on water hits); a Tin Colossus (fire bounces off, lightning arcs, iron pulls its plates, steam vents); then a Dragon as the fixed floor-5 final (a chasm, claw slams to bonk, fire breath down telegraphed lanes, a glowing throat to hit while it inhales, frost fizzling the breath).
  - For now the user wants polish.
- **Design mockups:** the user picked the boss looks from these pages: the Mimicshroom lineup https://claude.ai/artifact/NMWVXmtwT9gt7q2yx9bZWc, its cast and choreography https://claude.ai/artifact/ERUJb4HqNaJueL54Tk8Lww, and the moth queen lineup https://claude.ai/artifact/XgnoC7eG5zKYrMC15bpb5M. Their sources sit in `design/` (local only, gitignored).

## Traps that have broken this file before

- **Never put a `//` comment in the middle of a line.** The lines are dense, so it silently comments out the rest. It has eaten a camera setup, the bell echo and the room ceiling. When a patch replaces only the start of a line, check what followed it. Use `/* */` mid-line.
- **Never chain off three.js `parent.add(mesh)`.** It returns the parent, so `grp.add(m).rotation.x = …` turns the whole room. Make the mesh, transform it, then add it. `goodsModel`'s local `add()` is the exception: it returns the mesh.
- **Never `pgrep -f` or `pkill -f` a pattern that's in your own command line.** It matches your own shell: a wait loop never ends, and a kill takes out your shell. Match a PID, or use a pattern like `[p]ython3 tools/dev/serve.py`.

## Working with the user

- Plain, casual language, no jargon dumps.
- They give visual feedback as specific notes ("reads like a plunger") and like screenshots and renders.
- Art direction: low-poly, faceted, flat-shaded. Models needn't be built from primitive spheres, they just need a low polygon count.
- Their machine: a Razer Blade 15 running Ubuntu with KDE.

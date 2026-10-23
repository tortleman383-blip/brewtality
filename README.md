# Brewtality

A first-person dungeon crawler where you brew potions and fling them at things with a ladle. Five floors, the Cyclops King at the bottom, endless mode after that.

**Play:** open the GitHub Pages link for this repo, or download `index.html` and double-click it. It needs an internet connection for the 3D engine and fonts.

## Controls

| | |
|---|---|
| Move | WASD |
| Sling the brew | Hold left mouse, release to throw |
| Bonk | Right-click or V |
| Scrape ingredients | E (hold) |
| Brew | Tab |
| Swap ladle / water gun | Q |
| Swap brews (with the bandolier) | R |
| Emote (co-op) | G |
| Pause | Esc |

**Touchscreen:** put a finger down anywhere on the left side and drag to walk; drag on the right to look. The on-screen buttons sling, bonk, scrape and swap.

## Bosses

Each floor's stairs are guarded by a boss picked at random, and bosses learn new moves the deeper you find them.

The **Lurker** hides as one mushroom in a room full of them, on the floor, the walls and the ceiling. Hit the real one and it bursts out of the floor and chases you for a few seconds before burrowing and reshuffling the lot. Hit a wrong one and a bug comes out instead: Rootskitters from floor 1, Capbeetles from floor 2, Mantishrooms from floor 3 and Lampcaps from floor 4. The real one's tell is two spots that blink like clockwork on a doom shroom, or a ring of teeth clenching in the dirt round a glowcap.

## Test lab

**TEST LAB** on the title screen opens a containment chamber for watching any creature's attacks. Esc opens the console: pick the subject, the floor it's from (bosses learn moves the deeper they are), hold its AI, toggle god mode, and run any attack. In the chamber, the number keys fire attacks and 0 brings in a fresh subject.

## Co-op

1. One player picks **CO-OP → HOST WITH CODE** and reads out the 4-character code.
2. Everyone else picks **CO-OP → JOIN WITH CODE** and types it in.
3. Anyone presses **START RUN**.

### No-internet link

For two devices on the same network without the connection server (a phone hotspot works even with its data off; school Wi-Fi often blocks devices talking to each other):

1. Both pick **CO-OP → NO-INTERNET LINK**. One picks **HOST**, the other **JOIN**.
2. The joiner points their webcam at the QR code on the host's screen and gets a reply code.
3. The host picks **SCAN THEIR REPLY** and points their webcam at that.

No webcam? **COPY MY CODE** and paste it on the other device instead.

Everyone shares the floors, doors and enemies; hearts, coins, brews and loot are your own. If you go down, a partner clearing the room gets you back up. Connections are peer to peer through the free PeerJS service.

# Builds a debug copy of the working index.html into tools/dev/out/game.html, for testing in a browser:
# - window.__ev(src) evaluates code inside the game's own script scope (jump floors, spawn things, read state)
# - window.__errs collects uncaught errors
# - the game keeps ticking in a background tab
# - game.html?mock fakes claude.ai's co-op room across tabs, so two tabs can play together
# - window.__snapReq = 'name.png' saves the next frame into tools/dev/out (with serve.py running)
#   python3 tools/dev/build.py
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
s = open(os.path.join(HERE, "..", "..", "index.html")).read()

shim = "<script>window.requestAnimationFrame = cb => setTimeout(() => cb(performance.now()), 16); window.__errs = []; addEventListener('error', e => __errs.push(String(e.message)));</script>\n"
i = s.index('<script src="https://cdnjs')
s = s[:i] + shim + open(os.path.join(HERE, "mockroom.html")).read() + s[i:]
j = s.rindex("})();\n</script>")
s = s[:j] + "window.__ev = src => eval(src);\n" + s[j:]
s = s.replace("  renderer.render(scene, camera);", "  renderer.render(scene, camera); if (window.__snapReq) { const n = window.__snapReq; window.__snapReq = null; canvas.toBlob(b => fetch('/save?name=' + n, { method: 'POST', body: b }).then(() => { window.__snapDone = n; }), 'image/png'); }", 1)
a = "  return {\n    update, set, look,"
if a in s:  # the title screen's brewer, for posing and dances
    s = s.replace(a, "  window.__bw = { DANCES, pose, apply, scn, cam, getR: () => R, build, look, P1, shadow, getCh: () => ch };\n" + a, 1)

os.makedirs(OUT, exist_ok=True)
open(os.path.join(OUT, "game.html"), "w").write(s)
print("built tools/dev/out/game.html")

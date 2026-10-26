# Syntax-checks the game's script with node, the first thing to run after any edit to index.html.
#   python3 tools/dev/check.py [file]    (defaults to index.html)
import os, subprocess, sys, tempfile

path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "index.html")
s = open(path).read()
i = s.rindex("<script>\n") + len("<script>\n")
j = s.rindex("</script>")
with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
    f.write(s[i:j])
r = subprocess.run(["node", "--check", f.name])
os.unlink(f.name)
print("script OK" if r.returncode == 0 else "SYNTAX ERROR (above)")
sys.exit(r.returncode)

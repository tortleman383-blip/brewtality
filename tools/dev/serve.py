# Serves tools/dev/out on http://127.0.0.1:8766 (localhost only). A POST to /save?name=x.png saves its
# body into tools/dev/out, which is where the debug build's snapshots go.
#   python3 tools/dev/serve.py
import http.server, os, urllib.parse

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=OUT, **k)

    def do_POST(self):
        name = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query).get("name", ["out.bin"])[0]
        base = os.path.realpath(OUT)
        path = os.path.realpath(os.path.join(base, name))
        if not path.startswith(base + os.sep):
            self.send_response(400)
            self.end_headers()
            return
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            f.write(self.rfile.read(int(self.headers.get("Content-Length", 0))))
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"ok")

    def log_message(self, *a):
        pass


os.makedirs(OUT, exist_ok=True)
http.server.ThreadingHTTPServer(("127.0.0.1", 8766), Handler).serve_forever()

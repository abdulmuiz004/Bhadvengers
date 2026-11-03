from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Timer
from urllib.error import URLError
from urllib.parse import unquote, urlsplit
from urllib.request import urlopen
import webbrowser


HOST = "127.0.0.1"
PORT = 8000
URL = f"http://{HOST}:{PORT}/"
PROJECT_ROOT = Path(__file__).resolve().parent
ASSETS_ROOT = (PROJECT_ROOT / "assets").resolve()
PUBLIC_PAGES = {"/", "/index.html", "/members.html", "/join.html", "/styles.css", "/site.js"}


class WebsiteHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(PROJECT_ROOT), **kwargs)

    def _is_public_path(self):
        path = unquote(urlsplit(self.path).path)
        if path in PUBLIC_PAGES:
            return True
        if not path.startswith("/assets/"):
            return False

        asset = (PROJECT_ROOT / path.lstrip("/")).resolve()
        return asset.is_relative_to(ASSETS_ROOT) and asset.is_file()

    def _serve_public_file(self):
        if not self._is_public_path():
            self.send_error(404, "File not found")
            return
        if urlsplit(self.path).path == "/":
            self.path = "/index.html"
        super().do_GET()

    def do_GET(self):
        self._serve_public_file()

    def do_HEAD(self):
        if not self._is_public_path():
            self.send_error(404, "File not found")
            return
        if urlsplit(self.path).path == "/":
            self.path = "/index.html"
        super().do_HEAD()


try:
    with urlopen(URL, timeout=1) as response:
        if response.status == 200 and b"TWO FORCES." in response.read(65536):
            print(f"Bhadvengers is already running at {URL}")
            webbrowser.open(URL)
            raise SystemExit(0)
except URLError:
    pass

try:
    server = ThreadingHTTPServer((HOST, PORT), WebsiteHandler)
except OSError as error:
    raise SystemExit(f"Could not start Bhadvengers on port {PORT}: {error}") from error

print(f"Bhadvengers is ready at {URL}")
print("Keep this window open while you use the site. Press Ctrl+C to stop the server.")
browser_timer = Timer(1, webbrowser.open, args=(URL,))
browser_timer.daemon = True
browser_timer.start()

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nBhadvengers server stopped.")
finally:
    server.server_close()

"""Browser run (Playwright Chromium): what a portal player actually experiences.

The bundle is served gzip-compressed under a SUBPATH (/game/), the way portals host it, so absolute paths 404 here
exactly as they do there. Throttle = WebPageTest '4G' (9 Mbps, 170 ms RTT) + 4x CPU slowdown.
ttg_s here is engine-agnostic: navigation -> first non-blank frame with the network quiet for 1 s (a game whose
title screen waits for input is "playable" at that point). Portal SDK gameplay events, when present, are not used yet.
"""
import functools, gzip, hashlib, http.server, io, socketserver, threading, time
from pathlib import Path
from urllib.parse import urlparse, unquote

HERE = Path(__file__).resolve().parent
AXE = HERE / "vendor" / "axe-4.10.2.min.js"
NET_4G = dict(offline=False, latency=170, downloadThroughput=9_000_000 / 8, uploadThroughput=9_000_000 / 8)
PREFIX = "/game/"

INIT_JS = r"""
(() => {
  window.__pf = {ctx: [], playRejects: [], playOk: 0};
  for (const name of ['AudioContext', 'webkitAudioContext']) {
    const C = window[name]; if (!C) continue;
    const W = function (...a) { const c = new C(...a); window.__pf.ctx.push(c); return c; };
    W.prototype = C.prototype; window[name] = W;
  }
  const play = HTMLMediaElement.prototype.play;
  HTMLMediaElement.prototype.play = function (...a) {
    const p = play.apply(this, a);
    if (p && p.then) p.then(() => window.__pf.playOk++, e => window.__pf.playRejects.push(String(e && e.name)));
    return p;
  };
})();
"""


@functools.lru_cache(maxsize=512)
def _gz(path, mtime):
    return gzip.compress(Path(path).read_bytes(), 6)


class _Handler(http.server.SimpleHTTPRequestHandler):
    outside = None  # list, set per server

    def log_message(self, *a):
        pass

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_GET(self):
        path = unquote(urlparse(self.path).path)
        if not path.startswith(PREFIX):
            self.outside.append(path)
            self.send_error(404)
            return
        f = Path(self.directory) / path[len(PREFIX):]
        if f.is_dir():
            f = f / "index.html"
        if not f.is_file():
            self.send_error(404)
            return
        body = _gz(str(f), f.stat().st_mtime) if "gzip" in self.headers.get("Accept-Encoding", "") else f.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", self.guess_type(str(f)))
        if "gzip" in self.headers.get("Accept-Encoding", ""):
            self.send_header("Content-Encoding", "gzip")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        try:
            self.wfile.write(body)
        except (BrokenPipeError, ConnectionResetError):
            pass


_Handler.extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map, ".wasm": "application/wasm",
                           ".js": "text/javascript", ".mjs": "text/javascript", ".json": "application/json",
                           ".ogg": "audio/ogg", ".mp3": "audio/mpeg", ".m4a": "audio/mp4"}


def serve(root):
    outside = []
    h = type("H", (_Handler,), {"outside": outside})
    s = socketserver.ThreadingTCPServer(("127.0.0.1", 0), functools.partial(h, directory=str(root)))
    s.daemon_threads = True
    threading.Thread(target=s.serve_forever, daemon=True).start()
    return s, outside


def _shot(page):
    from PIL import Image
    png = page.screenshot()
    im = Image.open(io.BytesIO(png)).convert("RGB").resize((64, 36))
    colors = im.getcolors(64 * 36) or []
    top = max((c for c, _ in colors), default=0)
    blank = top > 0.985 * 64 * 36  # one colour covers the frame
    return hashlib.sha1(im.tobytes()).hexdigest(), blank, png


def run(root, entry="index.html", throttle=True, viewport=(1280, 720), timeout_s=45, shot_out=None):
    from playwright.sync_api import sync_playwright
    root = Path(root).resolve()
    rec = {"throttled": throttle, "viewport": f"{viewport[0]}x{viewport[1]}"}
    srv, outside = serve(root)
    origin = f"http://127.0.0.1:{srv.server_address[1]}"
    host = urlparse(origin).netloc
    reqs, failed, errors, console_err, pending = [], [], [], [], set()
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--enable-precise-memory-info", "--autoplay-policy=user-gesture-required"])
        ctx = b.new_context(viewport={"width": viewport[0], "height": viewport[1]}, has_touch=True)
        ctx.add_init_script(INIT_JS)
        page = ctx.new_page()
        cdp = ctx.new_cdp_session(page)
        cdp.send("Network.enable")
        cdp.send("Network.setCacheDisabled", {"cacheDisabled": True})
        if throttle:
            cdp.send("Network.emulateNetworkConditions", NET_4G)
            cdp.send("Emulation.setCPUThrottlingRate", {"rate": 4})
        cdp.send("Performance.enable")
        last_net = [time.monotonic()]

        def on_req(r):
            reqs.append((time.monotonic(), r.url))
            pending.add(r)
            last_net[0] = time.monotonic()

        def on_done(r):
            pending.discard(r)
            last_net[0] = time.monotonic()

        page.on("request", on_req)
        page.on("requestfinished", on_done)
        page.on("requestfailed", lambda r: (failed.append(r.url), on_done(r)))
        page.on("console", lambda m: console_err.append(m.text[:200]) if m.type == "error" else None)
        page.on("pageerror", lambda e: errors.append(str(e)[:200]))
        heap = [0]

        def sample_heap():
            try:
                m = {x["name"]: x["value"] for x in cdp.send("Performance.getMetrics")["metrics"]}
                heap[0] = max(heap[0], m.get("JSHeapUsedSize", 0))
            except Exception:
                pass

        t_nav = time.monotonic()
        page.goto(origin + PREFIX + entry, wait_until="commit", timeout=timeout_s * 1000)
        first_paint = ready = None
        png = None
        while time.monotonic() - t_nav < timeout_s:
            page.wait_for_timeout(250)
            sample_heap()
            _, blank, png = _shot(page)
            now = time.monotonic()
            if not blank and first_paint is None:
                first_paint = now - t_nav
            if first_paint is not None and not pending and now - last_net[0] >= 1.0:
                ready = last_net[0] - t_nav if last_net[0] - t_nav > first_paint else first_paint
                break
        rec["first_paint_s"] = round(first_paint, 2) if first_paint is not None else None
        rec["renders"] = first_paint is not None
        rec["ttg_s"] = round(ready, 2) if ready is not None else None
        rec["ttg_basis"] = "first non-blank frame + network quiet 1 s"
        if shot_out and png:
            Path(shot_out).write_bytes(png)
        if first_paint is not None:
            # animated without input? then a tap's effect cannot be told apart from animation
            h0, _, _ = _shot(page)
            page.wait_for_timeout(1000)
            h1, _, _ = _shot(page)
            ac_before = page.evaluate("window.__pf.ctx.map(c => c.state)")
            page.touchscreen.tap(viewport[0] // 2, viewport[1] // 2)
            page.mouse.click(viewport[0] // 2, viewport[1] // 2)
            page.keyboard.press("Space")
            page.wait_for_timeout(1500)
            h2, _, _ = _shot(page)
            rec["animated_idle"] = h0 != h1
            rec["touch_changes_frame"] = None if h0 != h1 else h2 != h1
            rec["audio_ctx_before_tap"] = ac_before
            rec["audio_ctx_after_tap"] = page.evaluate("window.__pf.ctx.map(c => c.state)")
            rec["audio_play_rejects"] = page.evaluate("window.__pf.playRejects")
            if throttle:
                cdp.send("Emulation.setCPUThrottlingRate", {"rate": 1})
            rec.update(axe(page))
            sample_heap()
        cut = t_nav + (ready if ready is not None else timeout_s)
        ext = sorted({u for _, u in reqs if urlparse(u).netloc != host and not u.startswith(("data:", "blob:"))})
        rec["external_requests"] = len(ext)
        rec["external_hosts"] = sorted({urlparse(u).netloc for u in ext})
        rec["external_urls"] = ext[:10]
        gz = 0
        for path in {unquote(urlparse(u).path) for t, u in reqs if t <= cut and urlparse(u).netloc == host}:
            f = root / path[len(PREFIX):] if path.startswith(PREFIX) else None
            if f and f.is_dir():
                f = f / "index.html"
            if f and f.is_file():
                gz += len(_gz(str(f), f.stat().st_mtime))
        rec["initial_requests"] = sum(1 for t, u in reqs if t <= cut)
        rec["initial_mb"] = round(gz / 1e6, 2)
        rec["initial_mb_basis"] = "gzip bytes of own files requested before ttg (external bytes not counted)"
        rec["outside_subpath_requests"] = sorted(set(outside))[:10]
        rec["failed_requests"] = sorted(set(failed))[:10]
        rec["page_errors"] = len(errors)
        rec["page_error_examples"] = errors[:5]
        rec["console_errors"] = console_err[:10]
        rec["peak_js_heap_mb"] = round(heap[0] / 1e6, 1)
        b.close()
    srv.shutdown()
    return rec


def axe(page):
    out = {}
    try:
        page.add_script_tag(content=AXE.read_text())
        r = page.evaluate("""async () => { const r = await axe.run(document, {runOnly: {type: 'tag',
            values: ['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa']}});
            return r.violations.map(v => ({id: v.id, impact: v.impact, nodes: v.nodes.length})); }""")
        out["axe_violations"] = sum(v["nodes"] for v in r)
        out["axe_rules"] = {v["id"]: v["nodes"] for v in r}
    except Exception as e:
        out["axe_error"] = str(e)[:200]
    return out

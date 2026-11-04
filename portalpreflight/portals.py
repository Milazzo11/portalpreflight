"""Per-portal rules: only numbers a portal publishes, each with its source and a short quote.

A rule maps a measured key to a limit. Verdict per rule: pass | fail | warn (advisory rule broken) | n/a (not measured).
Portal rules change: every rule carries `checked` (the date its source was last read); ruleradar snapshots
CrazyGames daily. Never add a number without a source URL.
"""

CG = "https://docs.crazygames.com/requirements/technical/"
POKI = "https://developers.poki.com/guide/requirements-quality"
PG = "https://wiki.playgama.com/playgama/game-requirements/technical-requirements.md"

# rule: (id, key, op, limit, level, text, source, quote)
#   op: "<=" numeric, "==" exact, "true" (key must be truthy), "false" (key must be falsy)
#   level: "must" (fail) | "should" (warn)
PORTALS = {
    "crazygames": {
        "name": "CrazyGames", "checked": "2026-11-04", "rules": [
            ("cg-total", "total_mb", "<=", 250, "must", "total file size <= 250 MB", CG,
             "A maximum total file size of 250MB is allowed."),
            ("cg-files", "file_count", "<=", 1500, "must", "<= 1500 files", CG,
             "There's a file count limit on 1500 files"),
            ("cg-initial", "initial_mb", "<=", 50, "must", "initial download <= 50 MB", CG,
             "The game must have an initial download size <= 50MB"),
            ("cg-mobile", "initial_mb", "<=", 20, "should", "initial download <= 20 MB (mobile homepage)", CG,
             "In order to be eligible for the mobile homepage, the initial download size needs to be <= 20MB."),
            ("cg-relative", "absolute_paths", "==", 0, "must", "relative paths only", CG,
             "Use only relative paths when referring to other files in the game bundle."),
            ("cg-ttg", "ttg_s", "<=", 20, "should", "time to gameplay <= 20 s", CG,
             "our QA team will evaluate based on the time it takes to reach gameplay (<= 20 seconds)"),
        ]},
    "poki": {
        "name": "Poki", "checked": "2026-11-04", "rules": [
            ("poki-external", "external_requests", "==", 0, "must", "no external requests", POKI,
             "No external requests. Poki blocks all external requests by default."),
            ("poki-load", "ttg_s", "<=", 10, "should", "playable within 10 s", POKI,
             "Players tend to move to another game if loading takes more than 10 seconds."),
            ("poki-ads", "foreign_ad_sdks", "==", 0, "must", "no other ad systems", POKI,
             "Poki's SDK handles ads, so no other ad systems are allowed."),
        ]},
    "playgama": {
        "name": "Playgama", "checked": "2026-11-04", "rules": [
            ("pg-total", "total_mb", "<=", 300, "must", "archive <= 300 MB", PG,
             "The total size of all game files does not exceed 300 MB"),
            ("pg-index", "root_index", "true", None, "must", "index.html at the root", PG,
             "An index.html file is added to the root of the archive."),
            ("pg-latin", "non_latin_names", "==", 0, "must", "Latin file names only", PG,
             "File and folder names use only Latin characters."),
            ("pg-external", "external_requests", "==", 0, "must", "no external resources", PG,
             "The game loads no external resources: everything it needs ships inside the archive."),
            ("pg-memory", "peak_js_heap_mb", "<=", 2000, "must", "startup memory < 2 GB (JS heap measured)", PG,
             "The game peaks below 2 GB of memory while it starts."),
        ]},
    "devvit": {
        "name": "Reddit Devvit Web", "checked": "2026-11-04", "rules": [
            ("dv-external", "external_requests", "==", 0, "must", "no external requests (webview CSP)",
             "https://developers.reddit.com/docs/", "(observed in our Devvit app builds; not quoted)"),
            ("dv-remote-code", "remote_scripts", "==", 0, "must", "no remote scripts",
             "https://developers.reddit.com/docs/", "(observed in our Devvit app builds; not quoted)"),
        ]},
    "generic": {
        "name": "Any portal (hygiene)", "checked": "2026-11-04", "rules": [
            ("gen-crash", "page_errors", "==", 0, "must", "no uncaught JS errors on load", "",
             "an uncaught exception at start is the most common QA rejection"),
            ("gen-render", "renders", "true", None, "must", "draws something within the timeout", "", ""),
            ("gen-mixed", "insecure_urls", "==", 0, "should", "no http:// URLs (portals serve https)", "", ""),
            ("gen-input", "touch_changes_frame", "true", None, "should", "a tap changes the screen (mobile input)", "", ""),
            ("gen-a11y", "axe_violations", "==", 0, "should", "axe-core WCAG 2.2 AA violations = 0", "", ""),
        ]},
}
DEFAULT_TARGETS = ["crazygames", "poki", "playgama", "devvit", "generic"]


def judge(rec, targets=None):
    """-> {portal: {"verdict": READY|FIXES|UNMEASURED|BLOCKED, "rules": [...]}}"""
    out = {}
    for t in targets or DEFAULT_TARGETS:
        p = PORTALS[t]
        rows, worst = [], "READY"
        for rid, key, op, limit, level, text, src, quote in p["rules"]:
            v = rec.get(key)
            if v is None:
                res = "n/a"
            elif op == "<=":
                res = "pass" if v <= limit else "fail"
            elif op == "==":
                res = "pass" if v == limit else "fail"
            elif op == "true":
                res = "pass" if v else "fail"
            else:
                res = "pass" if not v else "fail"
            if res == "fail" and level == "should":
                res = "warn"
            if res == "fail":
                worst = "BLOCKED"
            elif res == "warn" and worst == "READY":
                worst = "FIXES"
            rows.append({"id": rid, "key": key, "value": v, "limit": limit, "op": op, "level": level,
                         "result": res, "text": text, "source": src, "quote": quote})
        if worst == "READY" and any(r["result"] == "n/a" and r["level"] == "must" for r in rows):
            worst = "UNMEASURED"
        out[t] = {"name": p["name"], "checked": p["checked"], "verdict": worst, "rules": rows}
    return out

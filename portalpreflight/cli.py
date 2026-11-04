"""portalpreflight: dated portal-readiness scorecard for an HTML5 game bundle.

  python -m portalpreflight <dir|zip> [--targets crazygames,poki,...] [--static-only] [--no-throttle]
                            [--format md|json|github] [--json-out F] [--md-out F] [--shot F] [--fail-on blocked|fixes|never]
Exit 0 = verdicts within --fail-on, 1 = a target is worse, 2 = tool error.
"""
import argparse, json, os, sys, tempfile, time, zipfile
from pathlib import Path

from . import __version__, portals, static

ICON = {"READY": "READY", "FIXES": "FIXES", "BLOCKED": "BLOCKED"}
RES = {"pass": "ok", "fail": "FAIL", "warn": "warn", "n/a": "n/a"}


def unpack(path):
    p = Path(path)
    if p.is_dir():
        return p, None
    tmp = tempfile.mkdtemp(prefix="ppf-")
    with zipfile.ZipFile(p) as z:
        z.extractall(tmp)
    root = Path(tmp)
    kids = [k for k in root.iterdir() if k.name != "__MACOSX"]
    if len(kids) == 1 and kids[0].is_dir() and not (root / "index.html").exists():
        root = kids[0]
    return root, tmp


def preflight(path, name=None, entry="index.html", targets=None, dynamic=True, throttle=True, shot=None):
    root, _ = unpack(path)
    rec = {"tool": f"portalpreflight {__version__}", "game": name or Path(path).resolve().name,
           "date": time.strftime("%Y-%m-%d"), "entry": entry}
    rec.update(static.analyze(root, entry))
    if dynamic and rec["root_index"]:
        from . import dynamic as dyn
        try:
            d = dyn.run(root, entry, throttle=throttle, shot_out=shot)
            rec.update(d)
            rec["absolute_paths"] = max(rec["absolute_paths"], len(d.get("outside_subpath_requests", [])))
        except Exception as e:  # report, never crash the scorecard
            rec["browser_error"] = f"{type(e).__name__}: {e}"[:300]
    rec["loadavg1"] = round(os.getloadavg()[0], 1)
    rec["portals"] = portals.judge(rec, targets)
    return rec


def _fmt(v):
    if isinstance(v, bool):
        return "yes" if v else "no"
    return "-" if v is None else str(v)


def _mode(rec):
    if "throttled" not in rec:
        return "static checks only (no browser run)"
    return "Chromium, 4G + 4x CPU throttle, served under a subpath" if rec["throttled"] else "Chromium, unthrottled"


def markdown(rec):
    L = [f"## Portal Preflight: {rec['game']} ({rec['date']})", "",
         f"{rec['tool']} · {_mode(rec)}", "",
         "| Target | Verdict | Blocking | Advisory |", "|---|---|---|---|"]
    for t, p in rec["portals"].items():
        fails = [f"{r['text']} [{_fmt(r['value'])}]" for r in p["rules"] if r["result"] == "fail"]
        warns = [f"{r['text']} [{_fmt(r['value'])}]" for r in p["rules"] if r["result"] == "warn"]
        L.append(f"| {p['name']} | **{p['verdict']}** | {'; '.join(fails) or '-'} | {'; '.join(warns) or '-'} |")
    L += ["", "| Measure | Value |", "|---|---|"]
    for k in ("total_mb", "file_count", "initial_mb", "first_paint_s", "ttg_s", "external_requests", "absolute_paths",
              "remote_scripts", "page_errors", "insecure_urls", "peak_js_heap_mb", "axe_violations", "touch_changes_frame"):
        if k in rec:
            L.append(f"| {k} | {_fmt(rec[k])} |")
    fix = []
    if rec.get("external_hosts"):
        fix.append(f"Bundle these external hosts: {', '.join(rec['external_hosts'][:6])}")
    if rec.get("absolute_path_examples") or rec.get("outside_subpath_requests"):
        ex = (rec.get("absolute_path_examples") or []) + (rec.get("outside_subpath_requests") or [])
        fix.append(f"Make paths relative (portals host under a subpath): {', '.join(ex[:4])}")
    if rec.get("page_error_examples"):
        fix.append(f"Uncaught error on load: `{rec['page_error_examples'][0][:120]}`")
    if rec.get("browser_error"):
        fix.append(f"Browser run failed: {rec['browser_error'][:160]}")
    if not rec.get("root_index"):
        fix.append(f"No {rec['entry']} at the bundle root")
    if rec.get("ad_sdks"):
        fix.append(f"Third-party ad SDKs found: {', '.join(rec['ad_sdks'])} (portals with their own ads refuse these)")
    if fix:
        L += ["", "**Fix list**", ""] + [f"- {f}" for f in fix]
    L += ["", "Rules and sources: each verdict cites the portal's published requirement (`--format json` has the quotes). "
              "A preflight is not a portal's QA decision."]
    return "\n".join(L)


def github(rec):
    out = []
    for t, p in rec["portals"].items():
        for r in p["rules"]:
            if r["result"] in ("fail", "warn"):
                lvl = "error" if r["result"] == "fail" else "warning"
                out.append(f"::{lvl} title={p['name']}: {r['text']}::{r['key']}={_fmt(r['value'])} (limit {r['limit']}) {r['source']}")
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(prog="portalpreflight")
    ap.add_argument("bundle")
    ap.add_argument("--name")
    ap.add_argument("--entry", default="index.html")
    ap.add_argument("--targets", default=",".join(portals.DEFAULT_TARGETS))
    ap.add_argument("--static-only", action="store_true")
    ap.add_argument("--no-throttle", action="store_true")
    ap.add_argument("--format", choices=["md", "json", "github"], default="md")
    ap.add_argument("--json-out")
    ap.add_argument("--md-out")
    ap.add_argument("--shot")
    ap.add_argument("--fail-on", choices=["blocked", "fixes", "never"], default="never")
    a = ap.parse_args(argv)
    targets = [t for t in a.targets.split(",") if t]
    bad = [t for t in targets if t not in portals.PORTALS]
    if bad:
        print(f"unknown target(s): {', '.join(bad)}; known: {', '.join(portals.PORTALS)}", file=sys.stderr)
        return 2
    try:
        rec = preflight(a.bundle, a.name, a.entry, targets, not a.static_only, not a.no_throttle, a.shot)
    except Exception as e:
        print(f"portalpreflight: {type(e).__name__}: {e}", file=sys.stderr)
        return 2
    md = markdown(rec)
    if a.json_out:
        Path(a.json_out).write_text(json.dumps(rec, indent=1))
    if a.md_out:
        Path(a.md_out).write_text(md + "\n")
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as f:
            f.write(md + "\n")
    print({"md": md, "json": json.dumps(rec, indent=1), "github": github(rec) + "\n\n" + md}[a.format])
    order = {"READY": 0, "FIXES": 1, "UNMEASURED": 1, "BLOCKED": 2}
    worst = max((order[p["verdict"]] for p in rec["portals"].values()), default=0)
    limit = {"blocked": 2, "fixes": 1, "never": 9}[a.fail_on]
    return 1 if worst >= limit else 0

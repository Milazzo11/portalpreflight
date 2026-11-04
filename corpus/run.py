#!/usr/bin/env python3
"""Run the preflight on every game in corpus/games.json -> <out>/<name>.{json,md,png} + <out>/summary.json.

  run.py <out_dir> [--cache DIR] [--only a,b] [--no-throttle] [--runs N]
Fetches each repo at its pinned commit as a GitHub tarball (no git needed), runs `python -m portalpreflight` in a
subprocess per game (a crash in one game never stops the batch; the exit code is recorded).
--runs N keeps the median-ttg run (throttled timings are noisy on a loaded host).
"""
import argparse, io, json, os, subprocess, sys, tarfile, time, urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
PKG = HERE.parent


def fetch(g, cache):
    d = cache / f"{g['name']}-{g['commit'][:10]}"
    if (d / ".ok").exists():
        return d
    owner_repo = g["repo"].split("github.com/")[1]
    url = f"https://codeload.github.com/{owner_repo}/tar.gz/{g['commit']}"
    data = urllib.request.urlopen(url, timeout=300).read()
    d.mkdir(parents=True, exist_ok=True)
    with tarfile.open(fileobj=io.BytesIO(data)) as t:
        for m in t.getmembers():
            parts = m.name.split("/", 1)
            if len(parts) < 2 or not parts[1] or m.issym() or m.islnk() or ".." in parts[1].split("/"):
                continue
            m.name = parts[1]
            t.extract(m, d)
    (d / ".ok").write_text(url)
    return d


def one(g, root, out, throttle):
    args = [sys.executable, "-m", "portalpreflight", str(root), "--name", g["name"], "--entry", g.get("entry", "index.html"),
            "--format", "json", "--json-out", str(out / f"{g['name']}.json"), "--md-out", str(out / f"{g['name']}.md"),
            "--shot", str(out / f"{g['name']}.png")]
    if not throttle:
        args.append("--no-throttle")
    t0 = time.time()
    p = subprocess.run(args, capture_output=True, text=True, timeout=600, env={**os.environ, "PYTHONPATH": str(PKG)})
    rec = json.loads((out / f"{g['name']}.json").read_text()) if (out / f"{g['name']}.json").exists() else None
    return rec, p.returncode, round(time.time() - t0, 1), p.stderr[-400:]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--cache", default=str(Path.home() / ".cache/ilazy/ppf-tar"))
    ap.add_argument("--only")
    ap.add_argument("--no-throttle", action="store_true")
    ap.add_argument("--runs", type=int, default=1)
    a = ap.parse_args()
    out, cache = Path(a.out), Path(a.cache)
    out.mkdir(parents=True, exist_ok=True)
    games = json.loads((HERE / "games.json").read_text())["games"]
    if a.only:
        games = [g for g in games if g["name"] in a.only.split(",")]
    summary = []
    for i, g in enumerate(games, 1):
        row = {"name": g["name"], "repo": g["repo"], "commit": g["commit"]}
        try:
            root = fetch(g, cache)
            best = None
            runs = []
            for _ in range(max(1, a.runs)):
                rec, rc, secs, err = one(g, root, out, not a.no_throttle)
                runs.append({"rc": rc, "secs": secs, "ttg_s": rec and rec.get("ttg_s"), "stderr": err if rc == 2 else ""})
                if rec:
                    best = best or []
                    best.append(rec)
            if best:
                ok = sorted((r for r in best if r.get("ttg_s") is not None), key=lambda r: r["ttg_s"])
                rec = ok[len(ok) // 2] if ok else best[-1]
                if a.runs > 1:
                    rec["runs"] = [r.get("ttg_s") for r in best]
                (out / f"{g['name']}.json").write_text(json.dumps(rec, indent=1))
                sys.path.insert(0, str(PKG))
                from portalpreflight.cli import markdown
                (out / f"{g['name']}.md").write_text(markdown(rec) + "\n")
                row["verdicts"] = {k: v["verdict"] for k, v in rec["portals"].items()}
                row["browser_error"] = rec.get("browser_error")
            row["runs"] = runs
            row["crash"] = any(r["rc"] == 2 for r in runs) or not best
        except Exception as e:
            row["crash"] = True
            row["error"] = f"{type(e).__name__}: {e}"[:300]
        summary.append(row)
        print(f"[{i}/{len(games)}] {g['name']}: {row.get('verdicts') or row.get('error')}", flush=True)
    (out / "summary.json").write_text(json.dumps({"date": time.strftime("%Y-%m-%d"), "games": summary}, indent=1))
    crashes = sum(r["crash"] for r in summary)
    print(f"done: {len(summary)} games, {crashes} crashes")
    return 1 if crashes else 0


if __name__ == "__main__":
    sys.exit(main())

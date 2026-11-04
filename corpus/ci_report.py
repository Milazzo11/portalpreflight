#!/usr/bin/env python3
"""CI report job: scorecard artifacts -> one dated page + STATUS.json. ci_report.py <artifacts> <games.json> <out_dir>
A game with no record counts as a crash (its Action step failed before writing one). Always exits 0: the page is the report."""
import json, os, shutil, sys, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import page  # noqa: E402


def main(arts, games, out):
    arts, out = Path(arts), Path(out)
    out.mkdir(parents=True, exist_ok=True)
    rows = []
    for g in json.loads(Path(games).read_text())["games"]:
        rec = arts / f"scorecard-{g['name']}" / "portalpreflight.json"
        row = {"name": g["name"], "repo": g["repo"], "commit": g["commit"], "crash": not rec.exists()}
        if rec.exists():
            shutil.copy(rec, out / f"{g['name']}.json")
            row["verdicts"] = {k: v["verdict"] for k, v in json.loads(rec.read_text())["portals"].items()}
        rows.append(row)
    date = time.strftime("%Y-%m-%d")
    (out / "summary.json").write_text(json.dumps({"date": date, "games": rows}, indent=1))
    page.main(out, out / "README.md")
    crashes = [r["name"] for r in rows if r["crash"]]
    (out / "STATUS.json").write_text(json.dumps({
        "date": date, "games": len(rows), "scored": len(rows) - len(crashes), "crashes": crashes,
        "run_id": os.environ.get("GITHUB_RUN_ID"), "sha": os.environ.get("GITHUB_SHA"),
        "runner": os.environ.get("RUNNER_OS")}, indent=1))
    print(f"{len(rows) - len(crashes)}/{len(rows)} scored; crashes: {crashes or 'none'}")
    return 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:4]))

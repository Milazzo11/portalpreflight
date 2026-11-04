#!/usr/bin/env python3
"""<out_dir> (from run.py) -> one dated markdown page with every scorecard: page.py <out_dir> <page.md>"""
import json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from portalpreflight.cli import markdown  # noqa: E402
from portalpreflight import portals  # noqa: E402


def main(out, page):
    out = Path(out)
    summ = json.loads((out / "summary.json").read_text())
    recs = {g["name"]: json.loads((out / f"{g['name']}.json").read_text()) for g in summ["games"]
            if (out / f"{g['name']}.json").exists()}
    tg = portals.DEFAULT_TARGETS
    names = [portals.PORTALS[t]["name"].split(" (")[0] for t in tg]
    crashes = sum(g["crash"] for g in summ["games"])
    L = ["<!-- noindex until the publish word (R&D 102a) -->", f"# Portal Preflight: 20 open-source HTML5 games ({summ['date']})", "",
         f"{len(recs)} games from GitHub at pinned commits, each run as-is from its repository root. Tool crashes: {crashes}. "
         "Each game: Chromium on a throttled 4G link (9 Mbps, 170 ms RTT) with 4x CPU slowdown, served gzip-compressed under a "
         "subpath the way portals host it; median of the runs by time to gameplay. Verdicts cite each portal's published "
         "rules (see `portalpreflight/portals.py`); a preflight is not a portal's QA decision. These are open-source repos, "
         "not the authors' portal submissions: many were never meant for a portal, and a game whose repo needs a build step "
         "shows its missing build output as 404s (the scorecard measures what is committed). ttg = first non-blank frame "
         "with the network quiet for 1 s (engine-agnostic; a title screen counts).", "",
         "| Game | " + " | ".join(names) + " | ttg s | initial MB | external req |",
         "|---|" + "---|" * (len(tg) + 3)]
    count = {t: {} for t in tg}
    for n, r in recs.items():
        g = next(x for x in summ["games"] if x["name"] == n)
        cells = []
        for t in tg:
            v = r["portals"][t]["verdict"]
            count[t][v] = count[t].get(v, 0) + 1
            cells.append(v)
        L.append(f"| [{n}]({g['repo']}/tree/{g['commit'][:10]}) | " + " | ".join(cells)
                 + f" | {r.get('ttg_s', '-')} | {r.get('initial_mb', '-')} | {r.get('external_requests', '-')} |")
    L += ["", "Totals: " + "; ".join(f"{portals.PORTALS[t]['name']}: " + ", ".join(f"{k} {v}" for k, v in sorted(c.items()))
                                    for t, c in count.items()), ""]
    reasons = {}
    for r in recs.values():
        for t in tg:
            for rule in r["portals"][t]["rules"]:
                if rule["result"] in ("fail", "warn"):
                    reasons.setdefault(rule["text"], set()).add(r["game"])
    L += ["## Most common findings", "", "| Rule | Games |", "|---|---|"]
    for text, games in sorted(reasons.items(), key=lambda kv: -len(kv[1])):
        L.append(f"| {text} | {len(games)}: {', '.join(sorted(games))} |")
    L += ["", "## Scorecards", ""]
    for n, r in recs.items():
        L += [markdown(r).replace("## Portal Preflight: ", "### "), ""]
    Path(page).write_text("\n".join(L) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:3]))

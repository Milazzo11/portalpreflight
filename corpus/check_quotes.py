#!/usr/bin/env python3
"""PPF-1 check: every quoted portal rule still appears verbatim on its page. check_quotes.py <ruleradar snapshots dir>
Compares against ruleradar snapshots (0 tokens), ignoring markdown marks, case, curly quotes and whitespace. Exit 1 on a miss."""
import json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from portalpreflight import portals  # noqa: E402

PAGE = {"crazygames": "crazygames-technical", "poki": "poki-requirements", "playgama": "playgama-technical", "devvit": "devvit-web-overview"}


def norm(s):
    s = s.replace("’", "'").replace("“", '"').replace("”", '"').replace(" ", " ")
    s = re.sub(r"\s+", " ", re.sub(r"[*`_\\]", "", s))
    return re.sub(r" ([.,;:)])", r"\1", s).strip().lower()   # snapshots keep a space where an HTML tag ended


def main(snaps):
    misses = 0
    for t, page in PAGE.items():
        d = json.loads((Path(snaps) / f"{page}.json").read_text())
        text = norm(" ".join(str(v) for v in d.get("clauses", d).values()))
        for r in portals.PORTALS[t]["rules"]:
            ok = norm(r[7]) in text
            misses += not ok
            print(("ok  " if ok else "MISS"), r[0], "::", r[7])
    return 1 if misses else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))

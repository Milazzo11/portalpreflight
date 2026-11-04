import json, os, sys, tempfile, unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from portalpreflight import portals, static, cli  # noqa: E402


def bundle(files):
    d = Path(tempfile.mkdtemp())
    for name, body in files.items():
        p = d / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(body)
    return d


class Static(unittest.TestCase):
    def test_clean_bundle(self):
        d = bundle({"index.html": '<script src="js/game.js"></script>', "js/game.js": "let a = 1;"})
        r = static.analyze(d)
        self.assertTrue(r["root_index"])
        self.assertEqual((r["file_count"], r["absolute_paths"], r["remote_scripts"]), (2, 0, 0))

    def test_traps(self):
        d = bundle({"index.html": '<script src="https://cdn.example.com/lib.js"></script><img src="/img/a.png">'
                                  '<script src="http://ads.example.net/x.js"></script>',
                    "js/g.js": 'eval("1"); fetch("https://pagead2.googlesyndication.com/x")', "ü.png": "x"})
        r = static.analyze(d)
        self.assertEqual(r["remote_scripts"], 2)
        self.assertEqual(r["absolute_paths"], 1)
        self.assertEqual(r["non_latin_names"], 1)
        self.assertEqual(r["eval_uses"], 1)
        self.assertEqual(r["ad_sdks"], ["AdSense"])
        self.assertEqual(r["insecure_urls"], 1)  # the http:// <script>; JS strings are reported apart

    def test_no_index(self):
        r = static.analyze(bundle({"game.html": "x"}))
        self.assertFalse(r["root_index"])


class Judge(unittest.TestCase):
    def test_verdicts(self):
        rec = {"total_mb": 300, "file_count": 10, "initial_mb": 30, "absolute_paths": 0, "ttg_s": 5}
        j = portals.judge(rec, ["crazygames"])["crazygames"]
        self.assertEqual(j["verdict"], "BLOCKED")
        self.assertEqual({r["id"]: r["result"] for r in j["rules"]}["cg-mobile"], "warn")

    def test_unmeasured_is_not_ready(self):
        j = portals.judge({"total_mb": 1}, ["poki"])["poki"]
        self.assertEqual(j["verdict"], "UNMEASURED")

    def test_every_rule_has_source_or_is_generic(self):
        for t, p in portals.PORTALS.items():
            for rule in p["rules"]:
                if t != "generic":
                    self.assertTrue(rule[6].startswith("https://"), rule[0])


class Cli(unittest.TestCase):
    def test_static_cli(self):
        d = bundle({"index.html": "<canvas></canvas>"})
        out = Path(tempfile.mkdtemp()) / "r.json"
        rc = cli.main([str(d), "--static-only", "--json-out", str(out), "--format", "json"])
        self.assertEqual(rc, 0)
        rec = json.loads(out.read_text())
        self.assertIn("crazygames", rec["portals"])


if __name__ == "__main__":
    unittest.main()

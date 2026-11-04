import json, re, shutil, sys, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "corpus"))
import ci_report  # noqa: E402

RES = ROOT / "results" / "2026-11-04"


class CiReport(unittest.TestCase):
    def test_page_and_status_count_a_missing_record_as_crash(self):
        t = Path(tempfile.mkdtemp())
        games = [{"name": n, "repo": f"https://github.com/x/{n}", "commit": "a" * 40} for n in ("2048", "hextris", "gone")]
        (t / "games.json").write_text(json.dumps({"games": games}))
        for n in ("2048", "hextris"):
            d = t / "arts" / f"scorecard-{n}"
            d.mkdir(parents=True)
            shutil.copy(RES / f"{n}.json", d / "portalpreflight.json")
        ci_report.main(t / "arts", t / "games.json", t / "out")
        st = json.loads((t / "out" / "STATUS.json").read_text())
        self.assertEqual((st["games"], st["scored"], st["crashes"]), (3, 2, ["gone"]))
        page = (t / "out" / "README.md").read_text()
        self.assertIn("Tool crashes: 1", page)
        self.assertIn("### hextris", page)


class ActionYml(unittest.TestCase):
    def test_no_expression_inside_a_run_script(self):
        """Inputs in run: are shell injection in a public Action: they must go through env."""
        lines = (ROOT / "action.yml").read_text().splitlines()
        run_indent = None
        for line in lines:
            ind = len(line) - len(line.lstrip())
            if run_indent is not None and line.strip() and ind <= run_indent:
                run_indent = None
            if run_indent is not None:
                self.assertNotRegex(line, re.escape("${{"), line)
            if re.match(r"\s*(- )?run: \|", line):
                run_indent = ind


if __name__ == "__main__":
    unittest.main()

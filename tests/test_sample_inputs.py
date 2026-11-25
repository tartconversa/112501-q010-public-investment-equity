import csv
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1] / "samples"

class SampleContracts(unittest.TestCase):
    def read(self, path):
        with path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertTrue(rows)
        self.assertTrue(all(None not in row for row in rows))
        return rows

    def test_csv_sources_are_readable_and_unique(self):
        for path in sorted(ROOT.glob("*.csv")):
            rows = self.read(path)
            key = next(iter(rows[0]))
            self.assertEqual(len(rows), len({row[key] for row in rows}))

    def test_multiple_sources_and_version_anchor_exist(self):
        files = sorted(ROOT.glob("*.csv"))
        self.assertGreaterEqual(len(files), 4)
        names = " ".join(path.read_text(encoding="utf-8") for path in files)
        self.assertTrue("version" in names or "valid_" in names or "period" in names)

if __name__ == "__main__":
    unittest.main()

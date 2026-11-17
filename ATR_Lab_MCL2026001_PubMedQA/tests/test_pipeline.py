"""Small standalone tests against the genuine archived results."""
import csv
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.evaluation import parse_answer, summarize


class TestArchivedPubMedQA(unittest.TestCase):
    def test_parser(self):
        self.assertEqual(parse_answer("YES!", "direct"), "yes")
        self.assertEqual(parse_answer("maybe", "context"), "maybe")
        self.assertEqual(parse_answer("abstain", "context_abstain"), "abstain")
        self.assertEqual(parse_answer("abstain", "context"), "invalid")
        self.assertEqual(parse_answer("yes because", "direct"), "invalid")

    def test_split(self):
        split = json.loads((ROOT / "results/split_ids.json").read_text())
        dev, test = set(split["development_ids"]), set(split["test_ids"])
        self.assertEqual((len(dev), len(test)), (800, 200))
        self.assertFalse(dev & test)

    def test_rows_and_scores(self):
        with (ROOT / "results/predictions.csv").open(newline="") as fp:
            rows = list(csv.DictReader(fp))
        with (ROOT / "results/metrics_by_condition.csv").open(newline="") as fp:
            saved = {r["condition"]: r for r in csv.DictReader(fp)}
        self.assertEqual(len(rows), 800)
        for condition, ncorrect in [("majority", 110), ("direct", 22), ("context", 35), ("context_abstain", 41)]:
            group = [r for r in rows if r["condition"] == condition]
            score = summarize(group)
            self.assertEqual(len(group), 200)
            self.assertEqual(score["correct"], ncorrect)
            self.assertAlmostEqual(score["accuracy"], float(saved[condition]["accuracy"]))
            self.assertAlmostEqual(score["macro_f1"], float(saved[condition]["macro_f1"]))
            if condition != "majority":
                for r in group:
                    self.assertEqual(parse_answer(r["raw_response"], condition), r["prediction"])

    def test_abstention_and_no_class(self):
        with (ROOT / "results/predictions.csv").open(newline="") as fp:
            rows = list(csv.DictReader(fp))
        models = [r for r in rows if r["condition"] != "majority"]
        self.assertFalse(any(r["prediction"] == "no" for r in models))
        self.assertFalse(any(r["prediction"] == "abstain" for r in models))
        self.assertEqual(sum(r["prediction"] == "invalid" for r in models), 1)


if __name__ == "__main__":
    unittest.main()

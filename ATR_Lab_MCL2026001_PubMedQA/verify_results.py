"""Independently audit the archived Colab output using only the standard library."""
import csv
import json
import math
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
LABELS = ("yes", "no", "maybe")
CONDITIONS = ("majority", "direct", "context", "context_abstain")


def read_csv(name):
    with (RESULTS / name).open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def audit():
    split = json.loads((RESULTS / "split_ids.json").read_text())
    dev, test = set(split["development_ids"]), set(split["test_ids"])
    assert len(dev) == 800 and len(test) == 200 and not dev & test
    rows = read_csv("predictions.csv")
    assert len(rows) == 800 and {r["condition"] for r in rows} == set(CONDITIONS)
    archived = {r["condition"]: r for r in read_csv("metrics_by_condition.csv")}
    by_class = {(r["condition"], r["label"]): r for r in read_csv("per_class_metrics.csv")}
    expected_gold = None
    outcomes = {}
    for condition in CONDITIONS:
        group = [r for r in rows if r["condition"] == condition]
        assert len(group) == len(test) and {r["pmid"] for r in group} == test
        gold = {r["pmid"]: r["gold"] for r in group}
        if expected_gold is None:
            expected_gold = gold
        assert gold == expected_gold and set(gold.values()) == set(LABELS)
        for r in group:
            if condition == "majority":
                assert r["prediction"] == "yes"
                continue
            match = re.fullmatch(r"(yes|no|maybe|abstain)[.!]?", r["raw_response"].strip().lower())
            parsed = match[1] if match else "invalid"
            if parsed == "abstain" and condition != "context_abstain":
                parsed = "invalid"
            assert parsed == r["prediction"]
        matrix = Counter((r["gold"], r["prediction"]) for r in group)
        predicted = Counter(r["prediction"] for r in group)
        f_scores = []
        for label in LABELS:
            tp = matrix[label, label]
            support = sum(g == label for g in gold.values())
            precision = tp / predicted[label] if predicted[label] else 0
            recall = tp / support
            f1 = 2 * tp / (support + predicted[label])
            f_scores.append(f1)
            for key, value in {"precision": precision, "recall": recall, "f1-score": f1, "support": support}.items():
                assert math.isclose(float(by_class[condition, label][key]), value)
        correct = {r["pmid"] for r in group if r["gold"] == r["prediction"]}
        answered = sum(predicted[k] for k in LABELS)
        metrics = {
            "accuracy": len(correct) / len(group),
            "macro_f1": sum(f_scores) / len(LABELS),
            "coverage": answered / len(group),
            "selective_accuracy": len(correct) / answered,
            "abstention_rate": predicted["abstain"] / len(group),
            "invalid_rate": predicted["invalid"] / len(group),
        }
        for key, value in metrics.items():
            assert math.isclose(float(archived[condition][key]), value)
        timing = [float(r["batch_seconds_per_item"]) for r in group if r["batch_seconds_per_item"]]
        if timing:
            assert math.isclose(sum(timing) / len(timing), float(archived[condition]["mean_batch_seconds_per_item"]))
        outcomes[condition] = correct
        print(condition, len(correct), dict(predicted), metrics)
    print("Gold labels:", dict(Counter(expected_gold.values())))
    for a, b in [("context", "direct"), ("context_abstain", "context")]:
        print(f"{a} versus {b}: {len(outcomes[a] - outcomes[b])} gains, {len(outcomes[b] - outcomes[a])} losses")


if __name__ == "__main__":
    audit()

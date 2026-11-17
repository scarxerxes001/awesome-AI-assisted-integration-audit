"""Pure Python metrics and parsing for the saved PubMedQA labels."""
import re
from collections import Counter

LABELS = ("yes", "no", "maybe")


def parse_answer(text, condition):
    match = re.fullmatch(r"(yes|no|maybe|abstain)[.!]?", text.strip().lower())
    if match is None:
        return "invalid"
    answer = match.group(1)
    if answer == "abstain" and condition != "context_abstain":
        return "invalid"
    return answer


def summarize(rows):
    """Return per-class and aggregate scores for rows with gold/prediction fields."""
    if not rows:
        raise ValueError("At least one record is required")
    counts = Counter((r["gold"], r["prediction"]) for r in rows)
    gold = Counter(r["gold"] for r in rows)
    predicted = Counter(r["prediction"] for r in rows)
    if set(gold) - set(LABELS):
        raise ValueError("Unrecognized gold class")
    class_metrics = {}
    for label in LABELS:
        tp = counts[label, label]
        denom = gold[label] + predicted[label]
        class_metrics[label] = {
            "precision": tp / predicted[label] if predicted[label] else 0.0,
            "recall": tp / gold[label] if gold[label] else 0.0,
            "f1": 2 * tp / denom if denom else 0.0,
            "support": gold[label],
        }
    correct = sum(counts[label, label] for label in LABELS)
    answered = sum(predicted[label] for label in LABELS)
    return {
        "n": len(rows),
        "correct": correct,
        "accuracy": correct / len(rows),
        "macro_f1": sum(m["f1"] for m in class_metrics.values()) / len(LABELS),
        "coverage": answered / len(rows),
        "selective_accuracy": correct / answered if answered else None,
        "abstention_rate": predicted["abstain"] / len(rows),
        "invalid_rate": predicted["invalid"] / len(rows),
        "per_class": class_metrics,
        "predicted_counts": dict(predicted),
    }

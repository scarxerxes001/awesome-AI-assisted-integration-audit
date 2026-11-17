"""Recreate summary figures directly from archived prediction CSV.

The originals exported by Colab are not overwritten; additional reproducible
renders are written to results/figures_recreated/.
"""
import csv
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
OUT = RESULTS / "figures_recreated"
OUT.mkdir(exist_ok=True)
CONDITIONS = ["majority", "direct", "context", "context_abstain"]
LABELS = ["yes", "no", "maybe", "abstain", "invalid"]


def read_csv(filename):
    with (RESULTS / filename).open(newline="", encoding="utf-8") as fp:
        return list(csv.DictReader(fp))


def main():
    summary = {r["condition"]: r for r in read_csv("metrics_by_condition.csv")}
    x = list(range(len(CONDITIONS)))
    fig, ax = plt.subplots(figsize=(9, 4))
    width = 0.25
    for i, metric in enumerate(["accuracy", "macro_f1", "coverage"]):
        ax.bar([t + (i - 1) * width for t in x],
               [float(summary[c][metric]) for c in CONDITIONS], width=width, label=metric)
    ax.set_xticks(x, CONDITIONS, rotation=15)
    ax.set_ylim(0, 1)
    ax.set_ylabel("Score")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "condition_comparison.png", dpi=180)
    plt.close(fig)

    data = read_csv("predictions.csv")
    fig, axes = plt.subplots(2, 2, figsize=(11, 9))
    for ax, c in zip(axes.flat, CONDITIONS):
        counts = Counter((r["gold"], r["prediction"]) for r in data if r["condition"] == c)
        matrix = [[counts[(g, p)] for p in LABELS] for g in LABELS]
        ax.imshow(matrix, cmap="viridis")
        ax.set_title(c)
        ax.set_xticks(range(len(LABELS)), LABELS, rotation=45)
        ax.set_yticks(range(len(LABELS)), LABELS)
        ax.set_xlabel("Predicted")
        ax.set_ylabel("Gold")
        for i in range(len(LABELS)):
            for j in range(len(LABELS)):
                ax.text(j, i, str(matrix[i][j]), ha="center", va="center", color="white")
    fig.tight_layout()
    fig.savefig(OUT / "confusion_matrices.png", dpi=180)
    plt.close(fig)
    print("Recreated figures from archived CSV in", OUT)


if __name__ == "__main__":
    main()

# Baseline validation and reproduction audit — Prompts 08–11

**Execution evidence:** Uploaded `Untitled19.ipynb` (now preserved byte-for-byte as `notebooks/Complete_Research_Experiment.ipynb`) has six executed cells and saved outputs. It reports actual Colab Tesla T4 inference. `ATR_Experiment_Results.zip` contained the same ten result files as the original submission ZIP (all matching by SHA-256).

**Independent audit:** `python verify_results.py` was executed on the saved CSV files in this packaging workspace and passed. The audit confirms disjoint 800/200 IDs, 800 prediction rows, exactly 200 rows per condition, identical gold label per PMID across conditions, exact response-parser agreement, recalculated accuracy and per-class precision/recall/F1, saved timing means, and paired differences.

| Condition | Correct / 200 | Accuracy | Macro-F1 | Valid / 200 |
|---|---:|---:|---:|---:|
| Majority | 110 | 0.550 | 0.2366 | 200 |
| Direct | 22 | 0.110 | 0.0664 | 199 |
| Context | 35 | 0.175 | 0.1476 | 200 |
| Context + abstention | 41 | 0.205 | 0.1715 | 200 |

**Observed problems/limits:** All model conditions have zero `no` predictions, so recall is zero on 68 `no` examples. Abstention mode yields no `abstain` outputs, so no selective risk/coverage reduction can be studied. One direct completion was invalid. Qwen model commit revision is `null` in archived metadata. Dataset raw bytes were not provided for an independent download/hash recheck, although the recorded source and hash can be replayed.

**Nature of verification:** This is a test of archived output integrity and code inspection, **not** a new GPU inference run, faithful reproduction of the original PubMedQA paper, or proof that the model weights were identical to those used in a future session. All rerun commands are labeled by their execution status in the README.

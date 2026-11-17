# Dataset and baseline validation — Prompt 06

**Data source:** `https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/data/ori_pqal.json` (expert-labeled PQA-L). The user-executed notebook recorded 1,000 data records and SHA-256 `8b3276be8942ebbd77f3ddcda12c1749bf0e490045a736fd8438ee40cf37a41d`. The raw JSON is **not** included in this archive; the recorded checksum should be checked after download. See `results/dataset_validation.json`.

**Schema used:** `QUESTION` as question; ordered `CONTEXTS` entries joined into the abstract; `final_decision` as a gold label used only in development stratification and scoring. The run did not use `LONG_ANSWER` as inference input. PubMedQA's source describes the context as the abstract without the conclusion. The PQA-L labels are `yes`, `no`, and `maybe`.

**Partition:** Sort PMIDs; seed Python `random.Random(20261113)`; shuffle each label group; take rounded 20% of each as test; shuffle within development/test. 800 development and 200 test IDs; saved in `results/split_ids.json` (intersection empty). Test supports: yes 110, no 68, maybe 22. This is a custom stratified partition; **not** the authors' standard test split. No original study performance number is claimed for this split.

**Baseline controls:** The majority label was inferred from development records (`yes`). A zero-cost majority baseline and three conditions using the same checkpoint and test PMIDs provide a fair within-project comparison. The no-context variant removes the context field; the context variants supply the associated source text. Changes between comparisons are prompt changes, not changes to model parameters. Inputs are not guaranteed matched for token length.

**Leakage checks supported by source inspection:** test PMIDs are disjoint from development PMIDs; the source code uses gold labels to stratify and evaluate but not to build model prompts; long answers are absent from prompts. We cannot independently inspect the model's pretraining corpus or rule out dataset contamination. No additional original data download was executed during this packaging audit.

**Licensing:** Official PubMedQA repository contains an MIT license: `https://github.com/pubmedqa/pubmedqa/blob/master/LICENSE`. Respect any applicable attribution/privacy and source publication conditions. Qwen model is separately Apache-2.0 under its model card.

# Short technical viva preparation

**Why PubMedQA?** It is an expert-annotated biomedical QA benchmark connected to the previous review, with a manageable yes/no/maybe label space and public question/abstract pairs.

**Is this retrieval-augmented generation?** No. The model receives the *matching* abstract directly from each record. Retrieval quality was not measured.

**What are the baselines?** A majority-class predictor fit to the development set, and a question-only version of the same pretrained model.

**Why have 800 development and 200 test questions?** A custom label-stratified split with fixed seed was used for stable paired comparison; it is not the benchmark authors' official evaluation split.

**What does macro-F1 measure?** The unweighted mean of class-level F1 scores for yes/no/maybe, so a model cannot hide zero performance on a class behind common labels.

**What is the key result?** Context raised recorded accuracy from 11.0% to 17.5%, but every LLM method remained worse than the 55.0% majority baseline.

**Why was abstention unsuccessful?** The model produced no `abstain` decisions; the instruction changed some labels but did not reduce coverage. It was not a confidence-calibrated policy.

**What makes the results reproducible?** Archived predictions, exact split IDs, dataset checksum, recorded environment and prompt-generation code, plus an independent audit. A fully identical rerun is limited by the missing checkpoint commit hash.

**What is the most serious failure mode?** Zero `no` predictions on 68 actual `no` questions; the compact model collapsed primarily to `maybe`.

**Does higher benchmark accuracy prove factual correctness in all science?** No. This tests label agreement on one biomedical dataset, not long-form factual precision, citation support, scientific reasoning or cross-domain reliability.

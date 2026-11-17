# Result interpretation — Prompts 12–14

The 200 identical PQA-L test examples include 110 `yes`, 68 `no` and 22 `maybe` gold decisions. Row-level re-evaluation verifies all exported metrics.

**Question only:** 22/200 correct (11.0%) with macro-F1 0.0664; 199 `maybe` predictions, one invalid. Despite full recall for the `maybe` class, this is a poor classifier because `yes` and `no` recall are zero.

**Adding corresponding abstract:** 35/200 correct (17.5%) with macro-F1 0.1476. The paired comparison has 19 corrected examples and six newly incorrect ones relative to question-only. That is a +13/200 (6.5 percentage point) improvement, but still far below the development majority's 110/200.

**Adding permission to abstain:** 41/200 correct (20.5%) with macro-F1 0.1715; nine corrected and three lost compared with basic abstract prompting. The model produced zero abstentions, so 100% coverage does **not** support a selective-answering benefit. A prompt change affects decisions, but the mechanism was not isolated.

**Classwise finding:** All model variants predicted `no` zero times and therefore achieved zero recall on 68 examples. Context improved `yes` recall from 0 to 19/110 (17.3%), while abstention-prompt context improved to 25/110 (22.7%). The `maybe` recall dropped from 22/22 under question-only to 16/22 with context. See `results/per_class_metrics.csv` and the original confusion figure.

**Efficiency:** Mean observed batch generation time/item: direct 14.46 ms; context 31.89 ms; context+abstention 33.39 ms. This excludes loading, tokenization and transfer overhead; results are from a single Colab session and should not be interpreted as stable latency benchmarks.

**Limitations:** one model, one custom stratified split, no true retrieval, no evidence attribution scoring, no calibrated abstention, unknown checkpoint revision, no contamination audit or independent replication. Nothing here demonstrates clinical safety or cross-domain factual accuracy.

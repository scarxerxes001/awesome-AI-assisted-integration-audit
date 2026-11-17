# Research brief

The prior literature review identifies evidence grounding, evaluator reliability, and the difficulty of comparing factuality measurements across domains. PubMedQA gives a compact setting to study the effect of associated abstract context on yes/no/maybe benchmark decisions. FActScore and ALCE motivate separately measuring claim support and citation quality in future open-ended studies. A cross-domain comparison would require aligning disparate datasets and metrics.

**Primary question.** How does supplying the associated abstract change accuracy on the same PQA-L questions for a compact instruction model? Compare question-only and supplied-abstract prompts. A gain requires more corrected than newly incorrect decisions on the paired test set.

**Secondary question.** What happens to coverage and selective accuracy when the supplied-abstract prompt permits abstention? A coverage trade-off requires at least one abstention. A classwise audit checks whether improvements extend to all three benchmark decisions.

**Design and feasibility.** Compare the two prompts and a third prompt with abstention against a development majority baseline. The same public model and 200 held-out questions are used across model conditions. The notebook applies greedy decoding and saves predictions, split IDs, environment details, and timing. Colab T4 execution was feasible. The protocol does not involve training or retrieval.

**Evidence.** See the source bibliography, notebook, saved metadata, and independent verifier. The comparison addresses a scoped project question. Literature priority was not established.

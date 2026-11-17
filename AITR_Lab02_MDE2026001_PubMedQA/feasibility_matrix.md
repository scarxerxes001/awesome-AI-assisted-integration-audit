# Feasibility, alternatives and go/no-go — Prompts 03–04

| Method from review | Original method/dataset and access | Resource/comparison considerations | Decision |
|---|---|---|---|
| PubMedQA (Jin et al., 2019) | Three-label biomedical QA; official PQA-L is public at `github.com/pubmedqa/pubmedqa` and official publication is ACL Anthology D19-1259 | Same public questions/context can be supplied or omitted; original authors' reported published baseline is not comparable to this project's custom 800/200 split | **GO** as task, not a reproduction of authors' fine-tuned model |
| FActScore (Min et al., 2023) | Open long-form atomic-fact scoring; original work is not three-label PubMedQA classification | Requires long-form outputs, evidence corpus, a verification stage and additional dependencies | **NO-GO for this run**, appropriate future work |
| ALCE (Gao et al., 2023) | End-to-end cited generation with evidence retrieval and citation evaluation | Requires retrieval corpus, citation-formatted answers and more elaborate scoring | **NO-GO for this run**, not equivalent to supplying a given abstract |

**Study pathway choices:** (A) faithful reproduction plus extension needs baseline alignment and additional engineering; (B) same-model comparison offers controlled tests on available hardware; (C) targeted modification of model architecture would require extra validation and compute. Chosen: (B). The comparison has a straightforward minimum viable baseline and includes per-class failure analysis.

**Resource check:** User-executed notebook records Tesla T4 with 0.49B Qwen model, float16 weights, batch size eight and greedy generation. This verifies feasibility for the archived run; free Colab GPU availability on a later day is not guaranteed. Model model-card license is Apache-2.0; official PubMedQA repository includes an MIT license. Keep downloaded model/dataset outside ZIP; follow source terms.

**Open questions:** exact model revision was not archived; publication-level novelty was not established; one fixed dataset partition is not an official leaderboard comparison. Fallback if GPU is unavailable: run offline audit on saved predictions; do not claim new inference or re-trained results.

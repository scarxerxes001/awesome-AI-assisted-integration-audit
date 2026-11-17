# Technical peer review (AI-assisted; not external anonymous review)

| Priority | Issue, location | Consequence | Resolution / remaining action |
|---|---|---|---|
| Major | Methods and title | Calling context supplied from PQA-L “RAG” implies a retriever that was not implemented | Explicitly describes matched abstract prompting; no retrieval claim |
| Major | Results and discussion | All model scores are below development-majority accuracy | Emphasized 55% majority benchmark, including corresponding macro-F1; no claim that model is competitive |
| Major | Error analysis | Zero predictions of the `no` class obscured by overall improvement | Added recall table and explicit failure analysis of all 68 `no` examples |
| Major | Abstention subsection | `maybe` is a benchmark class, not an abstention | Separate abstain rate/coverage; zero actual abstentions reported |
| Major | Experiment provenance | Protocol not registered before evaluation; checkpoint revision missing | Explicitly disclosed retrospective protocol and unknown revision |
| Major | Benchmark integrity | Custom 800/200 stratification is not official benchmark leaderboard setting | Dataset/protocol sections explicitly disallow direct numerical comparisons |
| Moderate | Evidence quality | Executed code output alone does not prove metric integrity | Offline audit and unit tests recompute outputs from archived responses |
| Moderate | Scientific contribution | One model and one dataset do not establish cross-domain scientific factuality | Scoped as a biomedical classification case study |
| Moderate | Manuscript production | Initial supplied PDF was a five-page ReportLab rendering, not a TeX-compiled paper | Rebuilt and compiled real IEEE LaTeX PDF, 6 pages, sources retained |
| Minor | Bibliography | Primary sources must correspond to actual methods cited | Publisher pages for PubMedQA, ALCE, FELM and official Qwen model card consulted; model not assumed to be the same version in future runs |

## Residual concerns

- A full novelty search, external peer review, and instructor evaluation were not performed.
- No confidence-calibrated abstention, new held-out replications, or matched irrelevant-context condition was run.
- Only abstract classification was assessed, not factual evidence entailment or citation support.
- Student's understanding, university formatting policy and final acceptance need personal confirmation.

The review is of the **present manuscript and archived evidence**, not a claim that an independent academic reviewer approved the work.

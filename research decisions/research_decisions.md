# Research Decisions Log

## Project

**Working title:** Benchmarking Factual Accuracy of LLMs Across Scientific Domains  
**Project status:** Stage 1 — Existing review and research scope  
**Last updated:** 2026-10-22

### Evidence-label convention

- **VERIFIED** — directly supported by an inspected source, file, or recorded execution output.
- **INFERRED** — a reasoned interpretation that still requires confirmation.
- **UNKNOWN** — evidence is missing, has not been checked, or is insufficient.
- Do not report a paper, dataset, repository, implementation, experiment, or metric as verified without checking its source evidence.

## 1. Current Evidence

- **VERIFIED:** An existing four-page literature review is available as `AI_Assisted_Research_Paper.pdf`.
- **VERIFIED:** The review discusses scientific-domain factuality, hallucination types, TruthfulQA, FELM, RealFactBench, RAG, automated evaluation, and knowledge drift.
- **VERIFIED:** The review proposes fine-grained factuality evaluation and dynamic benchmarks as future directions.
- **UNKNOWN:** Whether the proposed gaps remain open in current literature.
- **UNKNOWN:** Which datasets and implementations are suitable for a controlled experiment.
- **UNKNOWN:** Whether the reviewed studies support the claims attributed to them in the draft.
- **UNKNOWN:** Whether the draft's bibliographic details, benchmark descriptions, and reported claims have been independently checked against original sources.

## 2. Provisional Decisions

### D001 — Do not select the final research gap yet
- **Status:** Provisional
- **Reason:** Novelty has not been established through verification of related work.
- **Evidence/source:** Existing literature review, `AI_Assisted_Research_Paper.pdf`.
- **Next action:** Inspect original references and search for directly related empirical studies.

### D002 — Separate factuality dimensions
- **Status:** Proposed
- **Reason:** Factual recall, numerical correctness, reasoning validity, citation accuracy, and grounded factuality may require different datasets and evaluation methods.
- **Evidence/source:** The review describes these as distinct error types.
- **Next action:** Map each candidate dataset to its task, labels, domain coverage, license, and evaluation protocol.

### D003 — Prioritize a feasible, reproducible experiment
- **Status:** Proposed
- **Reason:** The research contribution must be supported by executable code, documented configurations, and traceable results.
- **Evidence/source:** No implementation artifacts have been examined yet.
- **Next action:** Establish available compute, API access, time budget, and coding status.

## 3. Candidate Research Gaps

**Status:** Under verification. These are hypotheses to investigate, not novelty claims.

| Candidate gap | Evidence status | Evidence needed | Next action |
|---|---|---|---|
| Cross-domain factual accuracy under a controlled protocol | UNKNOWN | Recent studies comparing the same models, tasks, and evaluation methods across scientific domains | Search and screen related empirical work |
| Fine-grained error taxonomy across scientific domains | UNKNOWN | Existing taxonomies, annotation schemes, and cross-domain evaluations | Compare definitions, labels, and coverage |
| Retrieval-augmented versus non-retrieval factuality | UNKNOWN | Controlled comparisons, retrieval settings, and benchmark results | Check whether comparable datasets and baselines exist |
| Factuality evaluator or LLM-judge reliability | UNKNOWN | Human agreement, calibration, and evaluator-bias studies | Assess annotation and validation requirements |
| Temporal freshness and knowledge drift | UNKNOWN | Time-sensitive benchmark methods and publication-date controls | Estimate data construction and maintenance costs |

**Gap acceptance rule:** Accept a gap only after reviewing relevant prior work, recording sources and search dates, and explaining how the proposed experiment differs from the closest studies.

## 4. Literature-to-Experiment Mapping

| Source/paper | Claimed contribution in current review | Potential experimental use | Evidence status / next action |
|---|---|---|---|
| TruthfulQA (Lin et al., 2022) | Truthfulness questions involving common misconceptions | Candidate background or baseline; scientific-domain suitability must be checked | Bibliographic entry appears in review; verify original paper, dataset scope, license, and protocol |
| FELM (Chen et al., 2023) | Fine-grained factuality annotations | Candidate for segment-level error analysis | Verify original paper, dataset availability, license, annotation scheme, and domain coverage |
| RealFactBench (Yang et al., 2025) | Real-world fact-checking benchmark | Candidate only if task and data fit the research question | Verify original paper, benchmark details, availability, license, and current status |
| PubMedQA | Biomedical question answering | Candidate medical-domain dataset | Verify source, version, license, labels, and comparability |
| BioASQ | Biomedical question answering / retrieval tasks | Candidate medical-domain dataset | Verify task/year, data access, license, labels, and comparability |

This table records claims made by the review and candidate uses; it does not independently validate the papers or datasets.

### Literature screening record

For each source, record:
- Full citation and DOI/URL, checked against the publisher or official repository
- Publication date and date accessed
- Research question and task
- Models, datasets, domains, and metrics
- Main findings and limitations as reported by the source
- Whether code/data are available and under what license
- Relevance to the proposed experiment
- What the source does **not** establish

## 5. Dataset Registry

| Dataset | Intended domain/task | Version/split | License/terms | Suitability | Status |
|---|---|---|---|---|---|
| TruthfulQA | General truthfulness; scientific suitability unconfirmed | UNKNOWN | UNKNOWN | Pending review | Candidate |
| FELM | Fine-grained factuality; domain coverage unconfirmed | UNKNOWN | UNKNOWN | Pending review | Candidate |
| RealFactBench | Real-world fact checking; exact task fit unconfirmed | UNKNOWN | UNKNOWN | Pending review | Candidate |
| PubMedQA | Biomedical QA | UNKNOWN | UNKNOWN | Pending review | Candidate |
| BioASQ | Biomedical QA / retrieval | UNKNOWN | UNKNOWN | Pending review | Candidate |

Before selection, document dataset provenance, version, license and permitted use, fields/labels, sample count, domain distribution, split strategy, known contamination risks, preprocessing, and download or access instructions. Do not assume datasets are directly comparable merely because they concern factuality.

## 6. Model Registry

| Model identifier | Exact version/snapshot | Access method | Inference settings | Cost/compute | Status |
|---|---|---|---|---|---|
| Not selected | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | Pending |

Record the exact model identifier, provider or repository, model revision/date, access date, system and user prompts, temperature, token limits, decoding settings, retries, rate-limit handling, and any provider-side changes that may affect reproducibility. Never use a generic model family name when an exact identifier is available.

## 7. Research Questions and Hypotheses

**Status:** Not finalized.

For every proposed research question, record:
- Research question ID and wording
- Motivation and evidence from prior work
- Target population of models, domains, and task types
- Independent variables and outcome measures
- Baselines and comparison conditions
- Hypothesis, if justified by prior evidence
- Analysis method and decision criteria
- Feasibility risks and fallback plan

Do not write hypotheses as established findings. Do not finalize questions until the literature mapping and feasibility assessment are complete.

## 8. Experimental Protocol Checklist

- [ ] Final research question and contribution defined
- [ ] Closest prior work identified and compared
- [ ] Dataset source, version, license, and access verified
- [ ] Inclusion/exclusion criteria documented
- [ ] Data splits and leakage controls documented
- [ ] Model identifiers and revisions frozen
- [ ] Prompt templates versioned and frozen
- [ ] Inference parameters and retry policy recorded
- [ ] Evaluation script and metric definitions documented
- [ ] Human annotation procedure specified, if applicable
- [ ] Inter-annotator agreement plan specified, if applicable
- [ ] Sample-size rationale and statistical analysis plan recorded
- [ ] Pilot run completed and logged
- [ ] Deviations from the planned protocol documented

## 9. Evaluation Metrics Registry

| Metric | Intended purpose | Definition/source | Status |
|---|---|---|---|
| Exact match / task accuracy | Candidate for answer-level tasks | Must match dataset task and label format | Pending |
| Factual accuracy | Main outcome candidate | Operational definition and annotation/evaluation procedure required | Pending |
| Hallucination/error rate | Candidate error outcome | Define denominator and what counts as an error | Pending |
| Domain-wise accuracy | Compare domains | Requires consistent task definitions or justified normalization | Pending |
| Fine-grained error category rates | Analyze error patterns | Requires documented taxonomy and reliable labeling | Pending |
| Judge-human agreement | Validate automated evaluator, if used | Requires human-labeled sample and a suitable agreement statistic | Pending |

Do not select metrics solely because they are common. Specify exactly what each metric measures, how it is computed, how abstentions and unanswerable items are handled, and whether higher or lower values are better.

## 10. Code, Environment, and Execution Log

Record:
- Repository location and commit hash (when available)
- Python and package versions
- Operating system and hardware
- Dependency lock file or `requirements.txt`
- Configuration files and random seeds
- Dataset checksums or stable version identifiers where practical
- Commands executed and exit status
- Start/end times, logs, warnings, and failures
- Output artifact paths and checksums
- API/model errors, retries, and missing responses

**Current status:** No code execution or experimental outputs have been verified in this log.

## 11. Results Ledger

No experimental results have been verified or reported yet.

For each run, record:
- Run ID, date, code commit, and configuration
- Dataset version and exact evaluation subset
- Model identifier and inference settings
- Number of attempted, successful, invalid, and missing responses
- Metric values with denominators
- Uncertainty estimates and statistical comparisons, where appropriate
- Error-analysis sample and annotation method
- Output/log locations
- Deviations, failures, and interpretation limits

Never insert expected or illustrative values into the results table as if they were observed results.

## 12. Threats to Validity

| Threat | Current status | Mitigation/evidence needed |
|---|---|---|
| Dataset contamination | Known concern discussed in the review; project-specific exposure UNKNOWN | Check benchmark history, publication dates, and contamination evidence where available |
| Knowledge drift | Concern discussed in the review; impact on selected data UNKNOWN | Record dataset creation dates and model access dates; define temporal scope |
| Judge bias | Concern discussed in the review; project-specific impact UNKNOWN | Validate judges against human annotations and report disagreement |
| Prompt sensitivity | INFERRED risk until tested | Freeze primary prompts; optionally run a pre-specified sensitivity analysis |
| Domain imbalance | UNKNOWN until dataset audit | Report counts and label distributions by domain |
| Evaluation leakage | UNKNOWN until protocol is defined | Keep development choices separate from held-out evaluation data |
| Model/provider changes | UNKNOWN until model access is selected | Pin versions where possible and record dates/settings |
| Limited generalizability | Expected risk for a bounded study; scope UNKNOWN | State limits on models, tasks, domains, and time period |
| Annotation ambiguity | UNKNOWN until labels and guidelines are inspected | Create guidelines and adjudication procedure if human labels are used |

## 13. Reproducibility and Release Checklist

- [ ] Source code and license
- [ ] README with end-to-end replication instructions
- [ ] Dependency specification / lock file
- [ ] Dataset acquisition instructions and license notes
- [ ] Data preprocessing scripts
- [ ] Dataset version identifiers and checksums where permitted
- [ ] Prompt templates and experiment configuration
- [ ] Model identifiers, revisions, and inference parameters
- [ ] Raw model outputs, subject to privacy, terms, and licensing constraints
- [ ] Evaluation scripts and unit tests
- [ ] Aggregated results and statistical analysis scripts
- [ ] Execution logs and failure records
- [ ] Hardware/software environment
- [ ] Limitations and deviations from protocol
- [ ] Artifact availability statement in manuscript

Do not redistribute restricted datasets, private API credentials, or outputs contrary to applicable terms.

## 14. Manuscript Plan

- [ ] Abstract: write after the results are established
- [ ] Introduction and clearly scoped contribution
- [ ] Related work and verified research gap
- [ ] Research questions and hypotheses
- [ ] Benchmark/dataset selection and provenance
- [ ] Models, prompts, and experimental setup
- [ ] Evaluation metrics and statistical methods
- [ ] Results with uncertainty and denominators
- [ ] Error analysis
- [ ] Discussion linked to the evidence
- [ ] Threats to validity and limitations
- [ ] Reproducibility/artifact availability
- [ ] Conclusion that does not exceed the evidence

## 15. Decision Template

### DXXX — [Short decision title]
- **Date:**
- **Status:** Proposed / Accepted / Rejected / Superseded
- **Decision:**
- **Reason:**
- **VERIFIED evidence:**
- **INFERRED considerations:**
- **UNKNOWN / unresolved questions:**
- **Sources and access dates:**
- **Alternatives considered:**
- **Impact on experiment/manuscript:**
- **Next action and owner:**

## 16. Evidence Ledger

### VERIFIED
- An existing four-page review is available.
- The review discusses the topics listed in Section 1.

### INFERRED
- A controlled, narrowly scoped experiment may be more feasible than attempting to benchmark every scientific domain, error type, and mitigation strategy at once.

### UNKNOWN
- Final research gap and novelty
- Dataset suitability, access, licensing, and version
- Model selection and compute/API budget
- Final research questions and metrics
- Experimental outcomes and statistical significance
- Target venue and its artifact/reproducibility requirements

## 17. Next Actions

1. Obtain the review's source PDFs or a complete bibliography.
2. Verify the key benchmark papers and their original claims.
3. Build a literature matrix of the closest empirical studies.
4. Audit candidate datasets for task fit, domain coverage, licensing, and access.
5. Confirm available compute, API budget, timeline, and implementation status.
6. Select a research question based on the evidence and feasibility.
7. Freeze the protocol before the main evaluation.
8. Run and record a pilot; inspect failures before scaling up.
9. Execute the planned experiments and analyze results.
10. Update this log whenever a decision changes, preserving superseded entries.

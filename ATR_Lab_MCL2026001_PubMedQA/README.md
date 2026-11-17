# AI Tools for Research Lab 02 — PubMedQA factual accuracy case study

**Researcher:** Aditya Mohan Saha (MCL2026001)  
**Title:** *Evidence-Grounded Prompting and Abstention in Biomedical Question Answering: A Reproducible PubMedQA Case Study*

## What this project investigates

The prior literature review discusses scientific factuality, evidence support, citation quality and model uncertainty. This reproducible case study asks whether supplying a biomedical abstract changes the **yes/no/maybe** decision agreement of a compact instruction model, and whether explicitly allowing abstention results in selective answering.

Four conditions are compared on the same **custom 200-question test split** of the 1,000 expert-annotated PubMedQA PQA-L records: a development-majority predictor, question-only Qwen2.5-0.5B-Instruct, Qwen with the matched abstract, and Qwen with the matched abstract plus an abstention instruction. The system receives an already-associated abstract; **there is no retrieval module, so this experiment is not an end-to-end RAG study.**

### Genuine results from the user's executed Colab notebook

| Condition | Accuracy | Macro-F1 | Coverage |
|---|---:|---:|---:|
| Majority-class baseline | 55.0% | 0.2366 | 100.0% |
| Question only | 11.0% | 0.0664 | 99.5% |
| Matched abstract | 17.5% | 0.1476 | 100.0% |
| Matched abstract + abstention instruction | 20.5% | 0.1715 | 100.0% |

The model never predicted `no` (68 gold `no` examples) and never produced an `abstain` response. The majority baseline outperformed all LLM conditions. These are **descriptive results for one model and split**, not clinical conclusions or a claim of algorithmic novelty. `paper/final_research_paper.pdf` includes the detailed study and limitations.

## Directory guide

- `notebooks/Complete_Research_Experiment.ipynb`: **original executed Colab notebook**; same file bytes as the uploaded `Untitled19.ipynb`, renamed for clarity.
- `results/`: original user-uploaded predictions, per-class metrics, timing and figure files, plus new independently derived paired changes and figure reproductions. Original exports were **not overwritten**.
- `verify_results.py`: standard-library audit of every archived prediction and saved metric.
- `src/evaluation.py`: offline reusable metric and exact label-parsing helpers.
- `scripts/evaluate_results.py`: convenience command for offline verification.
- `scripts/generate_figures.py`: recreates summary plots from the CSV in `results/figures_recreated/` without overwriting original figures.
- `tests/test_pipeline.py`: executable unit checks of parsing, score reproduction and split alignment.
- `paper/main.tex`, `paper/references.bib`, `paper/final_research_paper.pdf`: LaTeX paper and **genuinely compiled IEEE-format PDF**.
- `gap_matrix.md`, `research_decisions.md`, `experiment_protocol.md`, `baseline_validation.md`, `ai_provenance_report.md`: research and provenance documentation.
- `evidence/`: requirement crosswalk, primary-source check, upload hashes and verification notes.
- `demonstration/`: five-minute walkthrough plan and viva preparation.

## Run verified offline evaluation

From the extracted project root:

```bash
python verify_results.py
python -m unittest discover -s tests -v
```

**Status:** Both commands were executed successfully during final packaging on 13 November 2026 using the archived records. They require only Python's standard library.

To recreate plots from saved CSV, install matplotlib and run:

```bash
python scripts/generate_figures.py
```

**Status:** Executed successfully during final packaging; results saved under `results/figures_recreated/`. This is not a new model run.

## Rerun model inference in Google Colab

1. Import `notebooks/Complete_Research_Experiment.ipynb` into Google Colab.
2. Select a GPU runtime if one is available (the archived run used a Tesla T4). The notebook assumes `torch`, `transformers`, `pandas`, `scikit-learn` and `matplotlib` are available. Its package versions from the successful session are recorded in `results/run_metadata.json` and `requirements.txt`.
3. Run cells **0 through 4** in order. Cell 5 is a historical download cell containing an absolute, timestamp-specific path: **do not rerun cell 5 blindly**. Cell 4 already downloads the newly created archive using its computed path. If dependencies are absent, install compatible packages using `requirements.txt` as a reference and confirm the environment before repeating inference.
4. Download the exported ZIP. Compare its dataset checksum and split PMIDs with the archived JSON files, then compare metrics. Preserve any new run separately rather than replacing archived evidence.

**Status:** Colab model inference was executed by the student in the uploaded notebook; it was **not independently rerun during package finalization**. Free GPU availability, download changes and unknown exact checkpoint commit mean a new run may produce different outputs. The original dataset file was not included in this ZIP.

Official dataset: https://pubmedqa.github.io/ and https://github.com/pubmedqa/pubmedqa  
Original dataset: https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/data/ori_pqal.json  
Model: https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct

The PubMedQA repository carries an MIT license; the Qwen model card specifies Apache-2.0. Respect the terms and do not upload raw data, weights or API credentials to a public repository without checking their usage conditions.

## Compile the paper

The included PDF was built from the included TeX source with `pdflatex` and `bibtex`, and visually inspected.

```bash
cd paper
python build_pdf.py
```

This requires a TeX distribution containing the IEEEtran class, `pdflatex`, and BibTeX. Alternatively, import `paper/main.tex`, `paper/references.bib` and the two PNG figures in `results/` into Overleaf; if uploading to Overleaf without the parent project, update the `\graphicspath` accordingly. PDF internal references and bibliography links are enabled.

## Critical methodological boundaries

- One pretrained model, one custom stratified test split, no repeated inference seeds.
- Gold labels were used for stratification and scoring, not as model prompt input. Public benchmark pretraining overlap was not assessed.
- The archived model revision is `null`; exact future inference replication is not guaranteed.
- The submitted `experiment_protocol.md` is an **after-the-fact reconstruction** of executed code, not proof of a prior frozen design.
- The paper reports benchmark decision agreement, not atomic factual precision, citation reliability, correctness of chain-of-thought or safety for clinical use.
- The manuscript and supporting files were AI-assisted and require the student's own review and understanding before submission.
- No external GitHub repository has been created, changed or pushed by this package.

## Final delivery and remaining obligations

Read `submission_status.md` and `evidence/requirements_checklist.md` for the full Prompt 01–18 mapping. Instructor approval, formal demonstration, complete novelty review and any required GitHub publication remain student/instructor actions, not completed steps in this archive.

## Additional provenance files

`prior_work/` includes the two user-uploaded preceding research PDFs for a traceable link to the review foundation. `paper/figures/` duplicates the original Colab figures so the `paper/` folder can be imported into Overleaf independently. `notebooks/Colab_Rerun_Clean_UNEXECUTED.ipynb` is a separate, output-cleared copy with the redundant timestamp-specific final download cell removed; **it has not been executed**. The actual experiment remains documented by `notebooks/Complete_Research_Experiment.ipynb` and the saved result archive.

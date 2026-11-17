# Prompts 01–18: evidence crosswalk

These are completion statuses for *documents and executable evidence*, not an assertion that all instructor approval gates have been signed.

| Prompt | Project evidence | Status / limitation |
|---|---|---|
| 01 Accountable workspace | `research_decisions.md`, `ai_assistance_log.md` | Complete retrospectively; prompt history incomplete |
| 02 Evidence-based gaps | `gap_matrix.md` | Five mapped gaps, novelty unverified |
| 03 Literature to experiment | `feasibility_matrix.md` | Three candidates, chosen protocol |
| 04 Novelty and resources | `feasibility_matrix.md`, `evidence/source_verification.md` | Feasible; exhaustive novelty check remains open |
| 05 Research questions | `research_brief.md` | Complete for scoped biomedical question |
| 06 Datasets and controls | `dataset_validation.md`, saved data metadata | Source verified; custom split, source bytes not embedded |
| 07 Frozen blueprint | `experiment_protocol.md`, config | **Retrospectively reconstructed, not prospectively frozen** |
| 08 Environment | Executed notebook cell 0, `results/run_metadata.json` | Genuine Colab T4 record |
| 09 Baseline modules | Executed notebook cells 1–4 | Working saved execution; model not rerun locally |
| 10 Verify baseline | `verify_results.py`, `baseline_validation.md` | Archived metrics independently verified |
| 11 Debug | `ai_assistance_log.md`, notebook | Only documented incidents claimed; limited original traceback logs |
| 12 Defensible contribution | `research_brief.md`, paper, comparison table | Controlled comparison, not novel algorithm |
| 13 Real-output evaluation | 800 predictions, all CSV outputs, figures, audit | Complete from actual notebook run |
| 14 Interpret outcomes | Paper and `results_analysis.md` | Negative findings and failure patterns explicit |
| 15 LaTeX manuscript | `paper/main.tex`, .bib, compiled PDF | Completed using source results |
| 16 Technical peer review | `paper/technical_review.md`, `paper/revision_log.md` | AI technical review, no external reviewer |
| 17 Reproducibility | README, notebook, `requirements.txt`, scripts, config | Local ZIP ready; GitHub publication not done |
| 18 Human–AI audit | `ai_assistance_log.md`, `ai_provenance_report.md` | No invented human actions; user's final review required |

**Gate status:** G1 scoped research brief prepared; G2 archived baseline and output integrity verified; G3 genuine paired experimental outputs and per-class analysis available; G4 paper/source/ZIP prepared. Formal gate approvals and five-minute live demonstration are **not** documented as completed.

**Artifacts update:** `paper/figures/` contains the original PNGs for stand-alone Overleaf import; `prior_work/` includes user-supplied review PDFs; the executed notebook remains intact and a separate output-cleared Colab rerun copy is identified as UNEXECUTED.

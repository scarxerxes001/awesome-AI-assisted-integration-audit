# Manuscript revision and formatting log

**Input:** supplied Codex project had a 5-page ReportLab-rendered paper and a shorter `main.tex` manuscript. The original numeric claims were checked against the user-supplied predictions.

**Actions performed during packaging (13 November 2026):**

1. Confirmed that `ATR_Experiment_Results.zip` and the pre-existing project contain the same ten original output files byte-for-byte, and that the uploaded executed notebook matches the existing notebook.
2. Executed `verify_results.py`, independently reproducing 55.0%, 11.0%, 17.5% and 20.5% accuracy, macro-F1, coverage and class-level outputs.
3. Rewrote and expanded `main.tex` around precisely the observed results; added research questions, dataset/source provenance, exact experimental conditions, classwise recall table, paired gain/loss counts, computational costs, limitations, AI accountability and future work.
4. Added verified FELM primary reference and preserved PubMedQA, ALCE, FActScore and model-card references.
5. Compiled the manuscript with IEEEtran, `pdflatex` and BibTeX; verified a **six-page PDF** with embedded original Colab plots, resolved citations, and no LaTeX compilation errors.
6. Kept the original CSV and PNG exports unchanged. Created derived tables and reproduced images in separate paths.

**Not changed:** gold and predicted labels, original experimental metrics, model weights, Colab notebook code or its executed outputs.

**Unresolved:** no full prospective preregistration, independent GPU rerun, domain-expert content audit or university approval is claimed.

# Packaging verification audit — 13 November 2026

Verification actually performed in the local working environment:

1. Extracted both user ZIPs safely and compared the ten duplicated experiment output files using SHA-256: **all ten equal**.
2. Compared the uploaded `Untitled19.ipynb` against the notebook originally included inside the project ZIP by SHA-256: **identical**. Archived original notebook has six cells, six non-null execution counts and saved outputs.
3. Executed `python verify_results.py`: **passed**, including disjoint development/test identifiers, 200 test records per condition, exact parsers, score recomputation, timing and paired gains/losses.
4. Executed `python -m unittest discover -s tests -v`: **four tests passed**, no failures.
5. Executed `python scripts/generate_figures.py`: **passed**; generated new figures from original CSV in `results/figures_recreated/` while preserving original image exports.
6. Compiled `paper/main.tex` with IEEEtran, `pdflatex` and BibTeX: **passed**, produced a six-page PDF with five bibliography entries; inspected rendered page previews.

**Not performed:** independent dataset download/checksum verification, GPU model inference, a new scientific benchmark, independent author/instructor approval. The user-uploaded dataset digest is recorded, not independently recomputed from unprovided raw data.

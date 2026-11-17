# AI-use and integrity report — Prompt 18

AI assisted with defining the study from the previous literature review, drafting executable code and notes, producing summary figures, checking result consistency, and writing the paper. The student uploaded an executed Colab notebook and exported results archive. Current packaging work independently audited existing results and prepared missing project documentation; it did not rerun GPU inference.

| Stage | Evidence | AI contribution | What was actually verified | Unresolved item |
|---|---|---|---|---|
| Research planning | Literature review, research_brief.md | Candidate gaps and controlled comparison framing | Alignment with the review's discussion of evidence and uncertainty | Full novelty search incomplete |
| Notebook implementation | Executed `Complete_Research_Experiment.ipynb` | Generated/edited model and evaluation code in Codex workflow | Colab outputs present; pipeline and prompts inspected | No exact model commit |
| Debugging | Prior `ai_assistance_log.md`; self-contained notebook | Replacement of earlier project-import approach with self-contained cells | Current notebook executed; earlier logs not independently provided | Do not claim detailed earlier error traces |
| Experiment evaluation | 800 saved prediction rows, exported figures | Automated calculations and figures | Independent standard-library audit reproduces all metrics | No new independent inference |
| Manuscript and package | LaTeX/PDF, logs | Drafted and formatted technical account | Numerical alignment, source links, build and test outcomes | Instructor sign-off and student ownership remain pending |

**Verified:** All saved prediction alignment and aggregate scores; no `no` predictions by model; no abstentions; model input code does not supply gold answer or long answer. **Inferred:** Reason for score differences (possibly grounding, prompt effects, model behavior) is not causally isolated. **Unknown:** exact checkpoint revision, training contamination, historical chronology of all earlier prompts, user/instructor approval.

There are no invented personal decisions or fabricated stories of human correction. The student must personally review, understand and demonstrate the work before presenting it as submitted research.

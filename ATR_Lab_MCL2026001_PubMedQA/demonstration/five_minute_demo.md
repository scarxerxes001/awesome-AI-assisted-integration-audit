# Five-minute code and results demonstration

**0:00–1:00 | Motivation.** Show the link to the prior review: evidence grounding and uncertainty. State the testable question: on a fixed PubMedQA yes/no/maybe decision task, does abstract context improve this one model's label agreement?

**1:00–2:00 | Code and data.** Open the executed Colab notebook. Explain the custom stratified 800/200 split and how gold labels and abstract conclusion are excluded from prompts. Show the prompt variants and `parse_answer`.

**2:00–3:00 | Validation.** In the project folder run `python verify_results.py` (already tested during packaging); show 800 aligned prediction rows and identical test identifiers across all four conditions.

**3:00–4:00 | Results.** Present the primary metrics: 55.0% majority, 11.0% direct, 17.5% with context, 20.5% with context plus abstention wording. Show paired-change CSV and the confusion matrices. Note that every model strategy is below the majority baseline.

**4:00–5:00 | Scientific interpretation.** No model condition predicts `no`; none abstains. `maybe` is an actual dataset class, not an abstention. Limitations: one model, one split, no real retrieval, unpinned revision. Explain how a new experiment with matched irrelevant context and development-tuned abstention could test additional hypotheses.

Do not claim this demonstration has already been performed for the instructor; this document is a walkthrough plan.

# Research decisions and feasibility

| Candidate gap | Evidence and test | Decision |
|---|---|---|
| Abstract grounding | PubMedQA supports a matched question-only versus supplied-context comparison on expert labels. The effect of context for the chosen checkpoint and prompt was a project hypothesis. | First choice. Run on one T4 with fixed decoding and test IDs. |
| Selective answering | The review motivates handling uncertainty. Compare coverage and selective accuracy after adding an abstention option to the context prompt. | Second choice. Reuse the same model and test records. |
| Citation support | ALCE evaluates whether cited evidence supports generated answers. A biomedical extension would require an evidence corpus and a citation validation procedure. | Third choice. Deferred because the chosen benchmark emits short decisions. |
| Evaluator reliability | FActScore uses atomic facts and checks support. A separate study could compare automated support judgments with blinded expert annotations. | Deferred. Expert annotation and evidence selection were outside this run. |
| Cross-domain measurement | The prior review distinguishes biomedical abstract QA from graduate-level science questions and open-ended factuality. A cross-domain comparison would require aligning those tasks and defining common outcomes. | Deferred. One benchmark cannot resolve the cross-domain question. |

The original PubMedQA approach is a benchmark method for reasoning over biomedical abstracts, with training-based models and yes/no/maybe decisions. Its source and data are public. Reproducing a trained benchmark method would add compute and split-compatibility requirements. FActScore decomposes long-form generations and checks atomic support against a knowledge source. ALCE evaluates cited generation and requires generated text and evidence. Neither provides a suitable drop-in baseline for this three-label study. The development majority, question-only prompt, and same-model abstract prompt give comparable controls at low compute cost.

Feasibility was confirmed by execution on Colab using publicly downloadable PQA-L and the Apache-2.0 Qwen checkpoint. The raw dataset and weights are excluded from the package. Source evidence is in the paper bibliography. A general literature priority claim remains open. Useful searches for an expanded review include PubMedQA question-only versus context, PubMedQA Qwen zero-shot prompts, and biomedical QA selective prediction.

The self-contained notebook superseded the earlier ZIP-based prototype before measured evaluation. It uses the Qwen chat template, a stricter parser, and batch generation. Only the self-contained notebook's outputs are used. Exact checkpoint identity remains unresolved because the archived revision field is null.

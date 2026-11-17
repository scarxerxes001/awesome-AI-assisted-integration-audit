# Awesome Scientific LLM Factuality

A curated, verified collection of research resources for **benchmarking the factual accuracy of large language models (LLMs) across scientific domains**. It connects an earlier AI-assisted research paper and its citation-integrity audit with a reusable collection of papers, datasets, tools, implementations, and learning material.

Scientific factuality is more demanding than general question answering: an answer must be correct, traceable to evidence, calibrated under uncertainty, and reliable across specialised fields such as medicine, chemistry, physics, and biology. This repository is designed for students and researchers who need starting points for evaluating or improving that reliability.

## Contents

- [Topic overview](#topic-overview)
- [AI-assisted research paper](#ai-assisted-research-paper)
- [Citation-integrity audit](#citation-integrity-audit)
- [Verified research papers](#verified-research-papers)
- [Datasets](#datasets)
- [Tools and libraries](#tools-and-libraries)
- [GitHub implementations](#github-implementations)
- [Tutorials and learning resources](#tutorials-and-learning-resources)
- [Verification notes](#verification-notes)
- [License](#license)

## Topic overview

Large language models can generate fluent scientific prose, answer technical questions, and assist with literature and laboratory workflows. Fluency, however, is not evidence of truth. A scientifically useful answer must preserve fine-grained factual correctness, identify uncertainty, attribute claims to appropriate evidence, and remain consistent through multi-step reasoning. These requirements are especially important when models are used around high-stakes domains such as clinical medicine, chemistry, and physics.

Benchmarking therefore needs more than a single accuracy score. Factuality methods assess atomic claims, factual consistency with a source, citation or attribution quality, and a model's ability to abstain when evidence is insufficient. Domain benchmarks add specialist questions and expert evaluation, while retrieval-augmented generation and tool use aim to ground responses in external sources. Yet benchmarks can be static, vulnerable to contamination, or too narrow to represent practical scientific work. Reliable evaluation consequently combines verified datasets, clear protocols, human or expert review where appropriate, and transparent reporting of limitations. The papers and resources here cover general factuality evaluation, scientific question answering, domain-specific benchmarks, and practical systems for grounded generation.

## AI-assisted research paper

The original Lab 1 AI-assisted paper is preserved without rewriting its claims or bibliography. It is included as an artefact for comparison with the independently curated material in this repository.

[View the preserved paper](paper/AI_Assisted_Research_Paper.pdf)

## Citation-integrity audit

The accompanying Lab 1 audit recorded an 85/100 authenticity score for a systematic sample of ten generated references, including metadata issues and one non-scholarly reference. This repository does not treat the original bibliography as automatically verified; the curated list below uses separately checked primary records.

[View the preserved citation-integrity audit](citation-audit/Citation_Integrity_Audit.pdf)

## Verified research papers

### Factuality evaluation and verification

- **FEVER: A Large-scale Dataset for Fact Extraction and VERification**  
  Thorne et al., 2018, NAACL-HLT. [Paper](https://aclanthology.org/N18-1074/)  
  A foundational benchmark for evidence retrieval and claim verification.
- **TruthfulQA: Measuring How Models Mimic Human Falsehoods**  
  Lin, Hilton, and Evans, 2022, ACL. [Paper](https://aclanthology.org/2022.acl-long.229/)  
  Tests whether language models reproduce common misconceptions rather than truth.
- **SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models**  
  Manakul, Liusie, and Gales, 2023, EMNLP. [Paper](https://aclanthology.org/2023.emnlp-main.557/)  
  Detects unsupported content by comparing multiple sampled model responses.
- **FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation**  
  Min et al., 2023, EMNLP. [Paper](https://aclanthology.org/2023.emnlp-main.741/)  
  Introduces atomic-fact scoring for long-form generated text.
- **FELM: Benchmarking Factuality Evaluation of Large Language Models**  
  Chen et al., 2023, NeurIPS Datasets and Benchmarks Track. [Paper](https://proceedings.neurips.cc/paper_files/paper/2023/hash/8b8a7960d343e023a6a0afe37eee6022-Abstract-Datasets_and_Benchmarks.html)  
  Evaluates factuality evaluators across multiple LLM-generated text settings.
- **HaluEval: A Large-Scale Hallucination Evaluation Benchmark for Large Language Models**  
  Li et al., 2023, EMNLP. [Paper](https://aclanthology.org/2023.emnlp-main.397/)  
  Provides task-specific hallucination evaluation data for LLM responses.
- **FactCC: A Model for Factual Consistency in Abstractive Summarization**  
  Kryscinski et al., 2020, EMNLP. [Paper](https://aclanthology.org/2020.emnlp-main.750/)  
  A source-grounded factual-consistency model that remains relevant to evaluation design.
- **QAGS: Evaluating Factual Consistency in Summarization**  
  Wang et al., 2020, ACL. [Paper](https://aclanthology.org/2020.acl-main.450/)  
  Uses question generation and answering to compare a summary with its source.

### Scientific and biomedical knowledge evaluation

- **SciFact: A Dataset for Scientific Claim Verification**  
  Wadden et al., 2020, EMNLP. [Paper](https://aclanthology.org/2020.emnlp-main.609/)  
  Requires systems to classify scientific claims and retrieve supporting or refuting abstracts.
- **PubMedQA: A Dataset for Biomedical Research Question Answering**  
  Jin et al., 2019, EMNLP-IJCNLP. [Paper](https://aclanthology.org/D19-1259/)  
  Biomedical yes/no/maybe questions paired with PubMed abstracts and reasoning.
- **What Disease Does This Patient Have? A Large-Scale Open Domain Question Answering Dataset from Medical Exams**  
  Jin et al., 2021, Applied Sciences. [Paper](https://www.mdpi.com/2076-3417/11/14/6421)  
  Introduces MedQA, a professional medical-exam benchmark for clinical knowledge.
- **Towards Expert-Level Medical Question Answering with Large Language Models**  
  Singhal et al., 2023, Nature. [Paper](https://www.nature.com/articles/s41586-023-06792-0)  
  Reports the MultiMedQA benchmark suite and clinician-oriented evaluation of medical LLMs.
- **BioMedLM: A 2.7B Parameter Language Model Trained on Biomedical Text**  
  Bolton et al., 2024, arXiv. [Paper](https://arxiv.org/abs/2403.18421)  
  Describes an openly released biomedical language model and its evaluation.
- **Galactica: A Large Language Model for Science**  
  Taylor et al., 2022, arXiv. [Paper](https://arxiv.org/abs/2211.09085)  
  A science-focused LLM paper useful for studying capability, provenance, and risk.
- **Augmenting Large Language Models with Chemistry Tools**  
  Bran et al., 2024, Nature Machine Intelligence. [Paper](https://doi.org/10.1038/s42256-024-00832-8)  
  Evaluates a tool-augmented chemistry agent and highlights grounding benefits.
- **Leveraging Large Language Models for Predictive Chemistry**  
  Jablonka et al., 2024, Nature Machine Intelligence. [Paper](https://doi.org/10.1038/s42256-023-00788-1)  
  Shows how language-model methods can be adapted to chemistry and materials tasks.

### General and expert reasoning benchmarks

- **Measuring Massive Multitask Language Understanding**  
  Hendrycks et al., 2021, ICLR. [Paper](https://openreview.net/forum?id=d7KBjmI3GmQ)  
  MMLU provides broad subject-matter evaluation, including STEM and professional domains.
- **GPQA: A Graduate-Level Google-Proof Q&A Benchmark**  
  Rein et al., 2024, COLM. [Paper](https://openreview.net/forum?id=Ti67584b98)  
  Expert-written biology, physics, and chemistry questions designed to resist simple web lookup.
- **Measuring Mathematical Problem Solving With the MATH Dataset**  
  Hendrycks et al., 2021, NeurIPS. [Paper](https://proceedings.neurips.cc/paper/2021/hash/be83ab3ecd0db773eb2dc1b0a17836a1-Abstract.html)  
  Tests multi-step mathematical reasoning and exact-answer reliability.
- **Training Verifiers to Solve Math Word Problems**  
  Cobbe et al., 2021, arXiv. [Paper](https://arxiv.org/abs/2110.14168)  
  Introduces GSM8K and verification-oriented approaches to mathematical reasoning.
- **Think You Have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge**  
  Clark et al., 2018, arXiv. [Paper](https://arxiv.org/abs/1803.05457)  
  A grade-school science challenge set designed to demand knowledge and reasoning.

See [references/references.md](references/references.md) for verification notes and persistent identifiers.

## Datasets

See [datasets/datasets.md](datasets/datasets.md) for source, use case, and access links.

## Tools and libraries

See [tools/tools.md](tools/tools.md) for official documentation and practical roles.

## GitHub implementations

See [implementations/github-repositories.md](implementations/github-repositories.md) for projects connected to the benchmarks and methods above.

## Tutorials and learning resources

See [tools/learning-resources.md](tools/learning-resources.md) for authoritative courses, documentation, and standards.

## Verification notes

Each research-paper entry was checked against an official proceedings page, publisher page, DOI resolver, or arXiv/OpenReview record on 28 August 2026. Links point to canonical records rather than unauthorized copies. The detailed record and verification route are in [references/references.md](references/references.md).

## License

This repository's original Markdown, organisation, and annotations are released under the [MIT License](LICENSE). Linked external resources remain subject to their own licences.

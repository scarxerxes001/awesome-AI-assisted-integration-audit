# Datasets

## 1. TruthfulQA

**Purpose:** Evaluates whether language models answer questions truthfully rather than reproducing common misconceptions.

**Scale / scope:** 817 questions spanning 38 categories in the original benchmark.

**Use in this project:** Useful for testing general factual accuracy and truthfulness of LLM answers.

- Paper: https://aclanthology.org/2022.acl-long.229/
- Official dataset/code: https://github.com/sylinrl/TruthfulQA
- Hugging Face: https://huggingface.co/datasets/truthful_qa

## 2. SciFact

**Purpose:** Scientific claim verification using evidence from scientific abstracts.

**Scale / scope:** The original work describes about 1.4K expert-written scientific claims paired with evidence-containing abstracts and rationales.

**Use in this project:** Particularly relevant to the assigned scientific-domain topic because it tests whether claims can be supported or contradicted using scientific literature.

- Paper: https://aclanthology.org/2020.emnlp-main.609/
- Official dataset/code: https://github.com/allenai/scifact
- Hugging Face BEIR version: https://huggingface.co/datasets/BeIR/scifact

## 3. RAGTruth

**Purpose:** Hallucination analysis for retrieval-augmented generation.

**Scale / scope:** Nearly 18,000 naturally generated RAG responses with manual annotations at case and word levels.

**Use in this project:** Useful for studying whether an LLM remains factually grounded even when retrieved context is supplied.

- Paper: https://aclanthology.org/2024.acl-long.585/
- Dataset/code: https://github.com/ParticleMedia/RAGTruth
- Dataset page: https://huggingface.co/datasets/wangrongsheng/RAGTruth

## Optional extension: CAP

**CAP (Confabulations from ACL Publications)** is especially aligned with this project's scientific focus. The 2026 LREC paper describes 900 scientific questions and more than 7,000 LLM-generated answers across multiple languages and models, annotated for scientific hallucination and fluency.

- Paper: https://aclanthology.org/2026.lrec-1.197/

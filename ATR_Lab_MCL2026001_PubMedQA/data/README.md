# Reacquiring PubMedQA safely

The project does not redistribute raw PubMedQA data. The executed notebook downloads `ori_pqal.json` directly from the official PubMedQA GitHub repository. Dataset source and recorded SHA-256 appear in `results/dataset_validation.json`.

Official site: https://pubmedqa.github.io/
Official GitHub: https://github.com/pubmedqa/pubmedqa
Source file: https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/data/ori_pqal.json
Repository license: https://github.com/pubmedqa/pubmedqa/blob/master/LICENSE

The notebook saves the test/development **PMIDs**, not raw question text, in `results/split_ids.json`. Do not use gold labels or the abstract conclusion as prompt input. The custom 80/20 split is not necessarily the source authors' official split.

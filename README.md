

<!-- [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.xxxxxxx.svg)](https://doi.org/10.5281/zenodo.xxxxxxx)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) -->

This is the official repository for the paper **"Can Multimodal Large Language Models Understand Graphic Design? A Comparative Study"**
<!-- , accepted by *IEEE Transactions on Multimedia*.  -->

This repository serves as the complete **Reproducibility Package** and hosts our **Supplementary Materials** to ensure full transparency, replicability, and accessibility of our research.

---

## 📁 Repository Structure

```text
├── supplementary_material/
│   └── supplementary.pdf  # Supplementary document for model stability
├── human_validation/
│   ├── evaluator640_test_annotations.csv             # 640 human-validated samples & GPT-4 scores
│   └── negative_space_detection_annotations.csv      # Additional raw annotations for Task #3
├── GPT4_evaluator_prompts/
│   ├── prompt-colorPaletteMeaning.json               # Exact JSON prompt for Task 1
│   ├── prompt-styleClassification.json               # Exact JSON prompt for Task 7
│   └── ... (other task prompts)
├── eval_gpt4.py                                      # Lightweight script to reproduce GPT-4 scores
├── requirements.txt                                  # Exact library versions for reproducibility
├── baseline_version.txt                              # Commit hashes and API versions for all models
└── README.md
```

---

## 📄 1. Supplementary Material

Due to limited space, the detailed **95% bootstrap confidence intervals (10,000 resamples)** for specific tasks, which extensively demonstrate model stability across different test settings, have been provided as a supplementary document. 

You can find the full details in: [`supplementary_material/supplementary.pdf`](./supplementary_material/supplementary.pdf).

---

## 🛠️ 2. Reproducibility Package

To address the importance of reproducibility and evaluation transparency, we provide all materials required to reproduce the GPT-4 evaluator scores on our 640-sample subset:

*   **Human Evaluator Labels:** Found in `human_validation/`. Includes raw annotations from three experts, aggregated consensus, and our recorded GPT-4 evaluation scores.
*   **GPT-4 Grading Prompts:** Found in `GPT4_evaluator_prompts/`. Contains the exact system instructions and few-shot examples (in JSON format) used for all 8 hierarchical design evaluation tasks.
*   **Model Versions & Hashes:** Found in `baseline_version.txt`. Lists the exact commit hashes for open-weight models (e.g., LLaVA-Next, InternVL) and dated versions for API models (e.g., `gpt-4o-2024-08-06`).

---

## 🚀 3. Quick Start (Reproducing Evaluation)

We provide a lightweight Python script to reproduce the GPT-4 automated evaluation.

<!-- ---

## 📝 Citation

If you find our benchmark, dataset, or code useful for your research, please consider citing our paper:

```bibtex
@article{designprobe2024,
  title={[Your Full Paper Title Here]},
  author={[Author 1 and Author 2 and Author 3]},
  journal={IEEE Transactions on Multimedia},
  year={[202X]},
  doi={[Paper DOI when available]}
}
```

## 📜 License

*   The code in this repository is licensed under the [MIT License](LICENSE).
*   The dataset and annotations (`.csv` files) and supplementary materials are licensed under a [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
``` -->
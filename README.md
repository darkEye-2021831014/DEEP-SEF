# DEEP-SEF

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](environment.yml)
[![Paper: CAEAI](https://img.shields.io/badge/Journal-Computers%20%26%20Education%3A%20AI-green.svg)](https://www.journals.elsevier.com/computers-and-education-artificial-intelligence)
[![Cite: CITATION.cff](https://img.shields.io/badge/Cite-CITATION.cff-blueviolet.svg)](CITATION.cff)

> **DEEP-SEF: Student Dropout Prediction by Combining Three
> Strongest-Per-Family Tabular Learners and Turning Early Warning Signs
> into Actionable Retention Decisions**
>
> *Ashraful Islam — Software Engineering, SUST, Sylhet*
> *Correspondence: <ashrafulislamdarkeye@gmail.com>*

This repository is the official companion code for the manuscript
submitted to **Computers and Education: Artificial Intelligence**
(`DEEP-SEF.docx.md` at the repository root). It contains the full
end-to-end pipeline, tuned hyper-parameters, intermediate CSVs,
pre-trained stackers, conformal-prediction arrays, and every figure
referenced in the paper, for both the primary UCI corpus and the
cross-dataset OULAD corpus.

---

## Highlights

* **Two datasets, three temporal horizons each.** UCI Predict Students
  Dropout (n = 3,630, 39.15 % dropout) and OULAD (n = 32,593, 52.80 %
  dropout) at the pre-semester (t0), post-semester-1 (t1), and
  post-semester-2 (t2) horizons.
* **Six-learner base on UCI** (LightGBM, CatBoost, XGBoost, ExtraTrees,
  FT-Transformer, TabPFN) and a **four-learner base on OULAD**
  (LightGBM, CatBoost, XGBoost, ExtraTrees) — TabPFN and FT-Transformer
  are dropped on OULAD for documented scalability and performance
  reasons (see §3.4 of the manuscript).
* **Per-horizon meta-learner contest** between LightGBM-meta and
  CatBoost-meta, selected by 5-fold stratified CV-AUC.
* **Mondrian conformal prediction** at α = 0.10 with empirical
  coverage within 1 percentage point of target.
* **Gaussian-mixture open-world rejection head** that abstains on
  10.06 – 10.88 % of UCI students and 21.26 – 29.34 % of OULAD students.
* **SHAP-driven risk-family impact** and **policy-lever timeline** that
  map model output to retention-practitioner constructs from Tinto,
  Bean, Astin, Braxton, Berger & Braxton, and Kuh.
* **100 % reproducible artefacts.** Every number reported in Tables 2 –
  15 of the manuscript can be regenerated from this repository.

---

## Repository layout

```
DEEP-SEF/
├── README.md                          <- you are here
├── LICENSE                            <- MIT
├── CITATION.cff                       <- citation metadata for GitHub
├── .gitignore
├── requirements.txt                   <- Python dependencies
├── requirements-dev.txt               <- + linting / testing extras
├── environment.yml                    <- Conda equivalent
├── DEEP-SEF.docx.md                   <- the manuscript (markdown export)
│
├── figures/
│   └── FIGURE_MANIFEST.md             <- imageN -> actual PNG file mapping
│
├── scripts/
│   └── reproduce_results.py           <- verify artefacts from disk
│
├── DEEP-SEF-UCI-PRIMARY/              <- primary corpus (UCI)
│   ├── DEEP-SEF-UCI-PRIMARY.ipynb     <- fully runnable notebook
│   ├── csv/                           <- per-step CSVs (00 – 09)
│   ├── figures/                       <- 32 PNGs (figs 1 – 24)
│   ├── meta/                          <- tuned HPO JSONs + conformal arrays
│   └── models/                        <- stacker_t0/t1/t2.joblib
│
└── DEEP-SEF-OULED/                    <- cross-dataset corpus (OULAD)
    ├── DEEP-SEF-OULED.ipynb
    ├── csv/
    ├── figures/
    ├── meta/
    └── models/
```

---

## Quick start

### 1. Clone the repository

```bash
git clone https://github.com/darkEye-2021831014/DEEP-SEF.git
cd DEEP-SEF
```

### 2. Set up the environment

You can use either `pip` or `conda`:

```bash
# Option A — pip
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Option B — conda
conda env create -f environment.yml
conda activate deep-sef
```

### 3. Verify the published artefacts

The shipped `csv/`, `meta/`, and `models/` directories contain every
intermediate artefact produced by the paper. To check that they are
intact and reproduce the headline AUC numbers:

```bash
python scripts/reproduce_results.py --dataset all
```

You should see the per-horizon DEEP-SEF stacking AUC and its 95 %
bootstrap CI for every horizon of both datasets, matching Tables 6 and 7
of the manuscript.

### 4. (Optional) Re-run the full pipeline

Open and run the notebooks top-to-bottom:

```bash
jupyter lab DEEP-SEF-UCI-PRIMARY/DEEP-SEF-UCI-PRIMARY.ipynb
jupyter lab DEEP-SEF-OULED/DEEP-SEF-OULED.ipynb
```

Each notebook performs, in order:

1. **Data loading & binary encoding** (UCI: drop Enrolled; OULAD:
   Pass/Distinction vs Fail/Withdrawn).
2. **Domain-aware feature engineering** — five feature groups
   (Academic Momentum, Risk Composites, Academic Efficiency, Semester
   Delta, Contextual Interactions), expanding the matrix to 37 / 52 / 74
   features (UCI) and 43 / 58 / 84 features (OULAD).
3. **Stratified 80/20 (UCI) or 85/15 (OULAD) split**, seed 42.
4. **Borderline-SMOTE-2 + Tomek Links** resampling confined to the
   training fold.
5. **Optuna TPE HPO** with 15 trials per learner per horizon.
6. **Six-/four-learner base ensemble** with 5-fold stratified CV for OOF
   probabilities.
7. **Per-horizon meta-learner contest** (LightGBM-meta vs CatBoost-meta).
8. **Mondrian conformal prediction** at α = 0.10 on a held-out
   calibration half.
9. **Gaussian-mixture open-world rejection head** at the 90th-percentile
   OOD cutoff.
10. **SHAP global + counterfactual** explanations on the LightGBM base.
11. **K-means archetypes**, **impact × actionability quadrants**, and
    **policy-lever timeline**.
12. **Multi-task heads** (Graduation, GPA, Attendance, Risk agreement).
13. **Layer-wise ablation** (Tables 6, 11).
14. **Comparative analysis** vs ExtraTrees, HistGradientBoosting, and
    TARB alternative backbone (Table 12, 13).

---

## Headline numbers

The numbers below are produced by `scripts/reproduce_results.py` from the
shipped artefacts and match Tables 6 and 7 of the manuscript exactly.

| Horizon | Dataset | Accuracy | AUC | 95 % bootstrap CI | Brier | LogLoss |
|---------|---------|----------|-----|--------------------|-------|---------|
| t0 | UCI  | 0.785 | 0.855 | [0.826, 0.882] | 0.146 | 0.451 |
| t1 | UCI  | 0.887 | 0.947 | [0.927, 0.965] | 0.076 | 0.259 |
| t2 | UCI  | 0.916 | 0.974 | [0.960, 0.986] | 0.058 | 0.237 |
| t0 | OULAD| 0.931 | 0.981 | [0.978, 0.984] | 0.049 | 0.162 |
| t1 | OULAD| 0.932 | 0.981 | [0.977, 0.984] | 0.049 | 0.163 |
| t2 | OULAD| 0.963 | 0.995 | [0.993, 0.996] | 0.025 | 0.087 |

**Calibration note.** The post-hoc temperature-scaling factor T*
converged to **1.0 at every horizon of both datasets** (see §5.4 and
§8.5 of the manuscript). The temperature layer was therefore inert in
this study; the reliability we report is a property of the base
learners, the meta-learner, and the OOF estimation pipeline rather than
of the calibration step.

**Conformal prediction note.** Empirical coverage is within 2 percentage
points of the 0.90 target at every horizon (Table 8 of the manuscript).

---

## Datasets

* **UCI Predict Students Dropout and Academic Success.** Real-world
  Portuguese higher-education institution, n = 4,424 students of whom
  3,630 remain after the Enrolled-class exclusion. Publicly available
  from the UCI Machine Learning Repository (DOI 10.24432/C5MC89).
* **Open University Learning Analytics Dataset (OULAD).** UK
  distance-learning institution, n = 32,593 student-module
  presentations, four-class `final_result` binarised to Pass-or-
  Distinction vs Fail-or-Withdrawn. Distributed under a CC-BY 4.0
  licence by Kuzilek, Hlosta & Zdrahal (2017).

The CSVs shipped under `csv/00_*` and `csv/01_*` are deterministic
snapshots produced by the notebooks; they are not redistributed dataset
copies.

---

## Citing DEEP-SEF

If you use this code or the published numbers in your own work, please
cite the paper. GitHub renders the citation metadata automatically from
[`CITATION.cff`](CITATION.cff); an APA-style entry is:

> Islam, A. (2026). DEEP-SEF: Student Dropout Prediction by Combining
> Three Strongest-Per-Family Tabular Learners and Turning Early Warning
> Signs into Actionable Retention Decisions. *Computers and Education:
> Artificial Intelligence*.

---

## Ethical considerations

Predicting dropout at the individual level carries ethical weight. DEEP-SEF
ships with an explicit **abstain option** (open-world rejection head) and
a **calibrated uncertainty surface** (Mondrian conformal prediction) so
that:

* No student is acted on solely on the basis of a model prediction.
* Students flagged as out-of-distribution are routed to a human advisor
  rather than to an automated intervention.
* The three-tier risk label is communicated as a probabilistic flag,
  not as a deterministic prediction.
* The pipeline should be re-audited annually for fairness across
  protected attributes (gender, age band, socioeconomic band); the SHAP
  outputs can be used to identify proxy discrimination in the feature
  set.

See §8.6 of the manuscript for the full ethics discussion.

---

## Limitations

The most material limitations are documented in §8.5 of the manuscript:

1. Both datasets come from European / online higher-education
   institutions; transfer to on-campus institutions in low- and
   middle-income countries with different macro-economic conditions is
   not guaranteed.
2. The OULAD feature set uses UK macro-economic indicators (GDP,
   UnempRate, Inflation) that are not available for every institution.
3. The OULAD final stack is four-learn rather than the six-learn UCI
   stack because TabPFN is restricted to ~10 k training rows and
   FT-Transformer underperformed gradient boosting on OULAD.
4. The open-world rejection rate on OULAD (21 – 29 %) is high.
5. The temperature scaling layer was inert (T* = 1.0).
6. The t2 horizon uses features derived from within-semester outcomes
   that are temporally close to the dropout label; the t2 AUC should be
   read with that leakage caveat in mind (§8.2).

---

## License

This repository is released under the [MIT License](LICENSE). The two
datasets are not redistributed; they must be obtained from their
original sources under their respective licences.

---

## Contact

* **Author:** Ashraful Islam
* **Affiliation:** Department of Software Engineering, SUST, Sylhet
* **Email:** ashrafulislamdarkeye@gmail.com
* **Issues:** Please use the GitHub issue tracker for bug reports and
  feature requests.
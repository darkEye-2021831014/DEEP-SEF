# Data Sources

DEEP-SEF is evaluated on two publicly available higher-education
datasets. Neither dataset is redistributed in this repository; the
researcher must obtain them from the original sources under their
respective licences.

## 1. UCI Predict Students Dropout and Academic Success (primary)

| Property | Value |
|----------|-------|
| Source | UCI Machine Learning Repository |
| Authors | M. V. Martins, D. F. Soares, A. M. Abelha, J. Machado (2021) |
| DOI | `10.24432/C5MC89` |
| URL | <https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success> |
| Licence | CC-BY 4.0 |
| Institution | Portuguese higher-education institution |
| Raw rows | 4,424 students |
| After Enrolled-class exclusion | 3,630 students |
| Class distribution (binary) | Graduate 60.85 %, Dropout 39.15 % |
| Features (raw) | 36 |
| Splits | 80/20 stratified, seed 42 → 2,904 / 726 |

## 2. Open University Learning Analytics Dataset — OULAD (cross-dataset)

| Property | Value |
|----------|-------|
| Source | Open University |
| Authors | J. Kuzilek, M. Hlosta, Z. Zdrahal (2017) |
| DOI | `10.1038/sdata.2017.171` |
| URL | <https://analyse.kmi.open.ac.uk/open-dataset> |
| Licence | CC-BY 4.0 |
| Institution | The Open University, UK |
| Rows | 32,593 student-module presentations |
| Class distribution (binary) | Pass/Distinction 47.20 %, Fail/Withdrawn 52.80 % |
| Features (raw) | 40 |
| Splits | 85/15 stratified, seed 42 → 27,730 / 4,863 |

## Feature engineering

Both datasets are passed through the same five-group domain-aware
feature engineering pipeline (see §4.2 of the manuscript):

* **G1 — Academic Momentum**: approval rate, pass efficiency, evaluation
  gap, low-grade flags, zero-grade flags, momentum score, cumulative
  approval rate, cumulative grade average, evaluation rate, credit
  conversion rate.
* **G2 — Risk Composite Scores**: financial risk, vulnerability index,
  academic distress, total failures, age × scholarship, age × financial
  risk.
* **G3 — Academic Efficiency Ratios**: first-semester approval rate,
  evaluation rate, credit conversion rate, pass efficiency, evaluation
  gap, grade average, approved-units ratio.
* **G4 — Semester Delta Profile**: s1-to-s2 grade delta,
  s1-to-s2 approved delta, average grade, cumulative approved,
  cumulative failures, cumulative efficiency, momentum score,
  semester-level trend.
* **G5 — Contextual Interactions**: age by scholarship, age by financial
  risk, GDP by debtor, unemployment by age, GDP by tuition, inflation
  by debtor, admission-versus-previous-grade gap.

| Horizon | UCI features | OULAD features |
|---------|--------------|----------------|
| t0 | 37 | 43 |
| t1 | 52 | 58 |
| t2 | 74 | 84 |

## Reproducibility

* Random seed: **42** (NeurIPS 2019 reproducibility recommendation).
* Cross-validation: **5-fold stratified**, repeated once.
* Bootstrap: **2,000 replicates**, percentile method.
* Hardware: any 16-GB RAM CPU laptop; GPU strongly recommended for the
  FT-Transformer branch on UCI.
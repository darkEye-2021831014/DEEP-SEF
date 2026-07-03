# Methods — Extended Reference

This document expands on §4 of the manuscript and is intended as the
canonical reference for reviewers who want to re-implement DEEP-SEF
without reading the Jupyter notebooks top-to-bottom.

## 1. Notation

* `X` — feature matrix, shape `(n, d_h)`, where `h ∈ {t0, t1, t2}`.
* `y ∈ {0, 1}` — binary dropout indicator (1 = dropout).
* `M` — base-learner set. `M_UCI = {LGB, CB, XGB, ET, FT-T, TabPFN}`,
  `M_OULAD = {LGB, CB, XGB, ET}`.
* `P_oof ∈ ℝ^{n×|M|}` — out-of-fold probability matrix from the base
  learners on the training set.
* `P_test ∈ ℝ^{n_test×|M|}` — held-out test probabilities.
* `s` — DEEP-SEF stacker (LightGBM-meta or CatBoost-meta).
* `q̂` — Mondrian conformal quantile at α = 0.10.
* `g(x)` — Gaussian-mixture open-world score on the standard deviation
  of `P_test[i, :]`.

## 2. Pipeline (per horizon)

```
                  ┌──────────────────────────────┐
                  │  Stratifed split (seed=42)   │
                  └──────────────────────────────┘
                                │
                                ▼
        ┌───────────────────────────────────────────┐
        │ Borderline-SMOTE-2 (sampling_strategy)   │
        │ + Tomek Links (training fold only)       │
        └───────────────────────────────────────────┘
                                │
                                ▼
       ┌────────────────────────────────────────────┐
       │ Optuna TPE HPO, 15 trials × |M| learners  │
       │ (5-fold stratified CV-AUC objective)       │
       └────────────────────────────────────────────┘
                                │
                                ▼
   ┌──────────────────────────────────────────────────┐
   │ Per-learner 5-fold CV → out-of-fold probabilities│
   │ P_oof ∈ ℝ^{n×|M|}                                │
   └──────────────────────────────────────────────────┘
                                │
                                ▼
   ┌──────────────────────────────────────────────────┐
   │ Augment P_oof with 6 aggregates:                  │
   │ [mean, std, min, max, spread, range] per student  │
   │ → P_oof_aug ∈ ℝ^{n×(|M|+6)}                       │
   └──────────────────────────────────────────────────┘
                                │
                                ▼
   ┌──────────────────────────────────────────────────┐
   │ Per-horizon meta-learner contest:                 │
   │ LightGBM-meta vs CatBoost-meta (5-fold CV-AUC)   │
   │ → pick winner s*                                  │
   └──────────────────────────────────────────────────┘
                                │
                                ▼
   ┌──────────────────────────────────────────────────┐
   │ Mondrian conformal:                               │
   │ split train 50/50 → meta on half / cal on half    │
   │ q̂ = ⌈(n+1)(1-α)⌉ / n quantile of non-conformity  │
   └──────────────────────────────────────────────────┘
                                │
                                ▼
   ┌──────────────────────────────────────────────────┐
   │ Two-component GMM open-world head:                │
   │ fit on σ(P_test) train, threshold at 90th pctl    │
   └──────────────────────────────────────────────────┘
                                │
                                ▼
   ┌──────────────────────────────────────────────────┐
   │ SHAP (TreeExplainer on LightGBM base)             │
   │ K-means archetypes on family-level SHAP rollup    │
   │ Impact × Actionability quadrant                   │
   │ Policy-lever timeline                             │
   └──────────────────────────────────────────────────┘
```

## 3. Base-learner family coverage

| Family | Representative | UCI | OULAD |
|--------|----------------|-----|-------|
| Gradient-boosted trees | LightGBM, CatBoost, XGBoost | ✓ | ✓ |
| De-randomising counterweight | ExtraTrees | ✓ | ✓ |
| Deep neural tabular | FT-Transformer | ✓ | ✗ (underperformed by 0.011 AUC) |
| Prior-fitted tabular foundation | TabPFN | ✓ | ✗ (n_train > 10 000) |

## 4. Calibration primitives

* **Temperature scaling** (Guo et al., 2017) is implemented in the
  pipeline but converged to **T* = 1.0** at every horizon of both
  datasets. The reliability we report is therefore a property of the
  base learners, the meta-learner, and the OOF estimation pipeline.
* **Platt scaling** (Zadrozny & Elkan, 2002) was used internally as
  the calibration primitive of each base learner (where supported) and
  re-applied to the stacked probabilities.
* **Niculescu-Mizil & Caruana supervised calibration** (2005) is the
  calibration primitive used to convert stacked log-odds to final
  probabilities.

## 5. Conformal prediction details

DEEP-SEF adopts Mondrian-style class-conditional conformal prediction.
Half of the training probabilities are used as the calibration set and
the other half are used to fit the meta-learner. The 90 % prediction
set is constructed by taking the classes whose calibrated
probabilities exceed 1 − q̂, where q̂ is the empirical 1 − α quantile
of the non-conformity scores. Empirical marginal coverage is within 2
percentage points of the 0.90 target at every horizon.

## 6. Open-world rejection details

The open-world rejection head is a two-component Gaussian mixture on
the standard deviation of the base-learner probabilities. A
90th-percentile cutoff on the OOD score abstains on 10 – 14 % of UCI
test students and 21 – 29 % of OULAD test students.

## 7. SHAP and policy levers

SHAP is computed with `shap.TreeExplainer` on the LightGBM base
learner at every horizon. Features are grouped into seven risk
families (Academic Preparation, Course/Family, Demographics,
Financial/Macro, 1st-Semester, 2nd-Semester, Risk Composite, Other),
and family-level impact is reported as the share of total |SHAP|
attributable to that family. Per-student counterfactuals are produced
for the 25 highest-risk test students at each horizon by a
gradient-free perturbation.
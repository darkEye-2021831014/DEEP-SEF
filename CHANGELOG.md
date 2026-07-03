# Changelog

All notable changes to this repository are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and the project adheres to [Semantic Versioning](https://semver.org/).

## [1.0.0] — 2026-07-03

### Added

- Initial release accompanying the manuscript submitted to *Computers
  and Education: Artificial Intelligence*.
- **Primary corpus** — UCI Predict Students Dropout and Academic Success
  (n = 3,630), full six-learner base ensemble (LightGBM, CatBoost,
  XGBoost, ExtraTrees, FT-Transformer, TabPFN) at three temporal
  horizons (t0 / t1 / t2).
- **Cross-dataset corpus** — OULAD (n = 32,593), four-learner base
  ensemble (LightGBM, CatBoost, XGBoost, ExtraTrees) at the same three
  horizons.
- Mondrian conformal prediction at α = 0.10 on both datasets.
- Gaussian-mixture open-world rejection head at the 90th-percentile
  OOD cutoff.
- SHAP global + per-student counterfactual explanations on the
  LightGBM base learner.
- K-means archetypes, impact × actionability quadrants, and policy-
  lever timelines for both datasets.
- Multi-task heads (Graduation, GPA, Attendance, Risk agreement) on
  UCI.
- Layer-wise ablation of the conformal and rejection layers (Table 11).
- TARB (TabPFN-Anchored Residual Boosting) alternative backbone on UCI
  (Table 5).
- 95 % bootstrap CI on AUC at every horizon of both datasets.
- Per-horizon Optuna-tuned hyper-parameters (`meta/06_hpo_best_params_*.json`).
- Pre-trained stacker models (`models/stacker_t*.joblib`).
- Conformal prediction arrays (`meta/conformal_preds_t*.npy`).
- 32 publication-ready PNG figures per dataset.

### Notes

- This is the camera-ready release for the initial submission.
  Subsequent revisions will be tagged with incremented patch versions.
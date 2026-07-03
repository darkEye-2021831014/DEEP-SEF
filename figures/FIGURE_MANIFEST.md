# Figure Manifest

This file maps every `imageN` reference in the manuscript
`DEEP-SEF.docx.md` to the actual PNG produced by the two Jupyter notebooks
(`DEEP-SEF-UCI-PRIMARY.ipynb`, `DEEP-SEF-OULED.ipynb`).

| # | Caption (abbreviated) | Source notebook | File path |
|---|------------------------|-----------------|-----------|
| 1 | DEEP-SEF end-to-end pipeline | both | `DEEP-SEF-UCI-PRIMARY/figures/00_pipeline.png` (or schematic in paper) |
| 2 | Binary class distribution — UCI vs OULAD | both | `DEEP-SEF-UCI-PRIMARY/figures/01_binary_class_distribution.png` |
| 3 | UCI per-horizon feature count | UCI | `DEEP-SEF-UCI-PRIMARY/figures/03_feature_counts_per_horizon.png` |
| 4 | OULAD per-horizon feature count | OULAD | `DEEP-SEF-OULED/figures/03_feature_counts_per_horizon.png` |
| 5 | OULAD stratified train-test split | OULAD | `DEEP-SEF-OULED/figures/05_split_summary.png` |
| 6 | DEEP-SEF stacking architecture | both | `DEEP-SEF-UCI-PRIMARY/figures/06_stacking_architecture.png` |
| 7 | Optuna Bayesian HPO loop | both | `DEEP-SEF-UCI-PRIMARY/figures/07_optuna_hpo_loop.png` |
| 8 | Per-horizon base-learner accuracy (UCI) | UCI | `DEEP-SEF-UCI-PRIMARY/figures/12_base_learner_accuracy.png` |
| 9 | Per-horizon base-learner metrics (UCI) | UCI | `DEEP-SEF-UCI-PRIMARY/figures/13_base_learner_all_metrics.png` |
| 10 | Base-learner correlation heatmaps (UCI) | UCI | `DEEP-SEF-UCI-PRIMARY/figures/15_base_learner_correlation.png` |
| 11 | Stacking vs best base / mean blend (UCI) | UCI | `DEEP-SEF-UCI-PRIMARY/figures/16_stacking_vs_baselines.png` |
| 12 | Stacking vs best base / mean blend (OULAD) | OULAD | `DEEP-SEF-OULED/figures/16_stacking_vs_baselines.png` |
| 13 | Confusion matrices (UCI) | UCI | `DEEP-SEF-UCI-PRIMARY/figures/01_confusion_matrices.png` |
| 14 | Confusion matrices (OULAD) | OULAD | `DEEP-SEF-OULED/figures/01_confusion_matrices.png` |
| 15 | ROC curves (UCI) | UCI | `DEEP-SEF-UCI-PRIMARY/figures/02_roc_overlay_horizons.png` |
| 16 | Reliability diagrams (UCI) | UCI | `DEEP-SEF-UCI-PRIMARY/figures/03_reliability_diagrams.png` |
| 17 | Per-horizon metrics UCI vs OULAD | both | `DEEP-SEF-UCI-PRIMARY/figures/10_per_horizon_metrics.png` |
| 18 | Open-world rejection (UCI) | UCI | `DEEP-SEF-UCI-PRIMARY/figures/04_open_world_rejection.png` |
| 19 | Open-world rejection (OULAD) | OULAD | `DEEP-SEF-OULED/figures/04_open_world_rejection.png` |
| 20 | Coverage vs abstention frontier | both | `DEEP-SEF-UCI-PRIMARY/figures/20_coverage_abstention.png` |
| 21 | Advisor time saved per cohort | both | `DEEP-SEF-UCI-PRIMARY/figures/21_advisor_time_saved.png` |
| 22 | Incremental value of conformal + rejection | UCI | `DEEP-SEF-UCI-PRIMARY/figures/22_incremental_value.png` |
| 23 | Conformal prediction-set size distribution | UCI | `DEEP-SEF-UCI-PRIMARY/figures/23_set_size_distribution.png` |
| 24 | Cross-dataset calibration UCI vs OULAD | both | `DEEP-SEF-UCI-PRIMARY/figures/24_cross_dataset_calibration.png` |
| 25 | SHAP summary t0 (UCI) | UCI | `DEEP-SEF-UCI-PRIMARY/figures/05_shap_summary_t0.png` |
| 26 | Top-15 SHAP bar t0/t1/t2 (UCI) | UCI | `DEEP-SEF-UCI-PRIMARY/figures/06_shap_bar_t0.png` (+ t1, t2) |
| 27 | Top-15 SHAP bar t0 (OULAD) | OULAD | `DEEP-SEF-OULED/figures/06_shap_bar_t0.png` |
| 28 | Top-15 SHAP bar t1 (OULAD) | OULAD | `DEEP-SEF-OULED/figures/06_shap_bar_t1.png` |
| 29 | Top-15 SHAP bar t2 (OULAD) | OULAD | `DEEP-SEF-OULED/figures/06_shap_bar_t2.png` |
| 30 | Risk-family impact UCI | UCI | `DEEP-SEF-UCI-PRIMARY/figures/08_risk_family_impact.png` |
| 31 | Risk-family impact UCI vs OULAD | both | `DEEP-SEF-UCI-PRIMARY/figures/08_risk_family_impact.png` (overlay) |
| 32 | K-means archetypes t2 (UCI) | UCI | `DEEP-SEF-UCI-PRIMARY/figures/17_advisor_risk_archetypes_t2.png` |
| 33 | K-means archetypes t2 (OULAD) | OULAD | `DEEP-SEF-OULED/figures/17_advisor_risk_archetypes_t2.png` |
| 34 | Impact × Actionability quadrant (UCI) | UCI | `DEEP-SEF-UCI-PRIMARY/figures/18_intervention_actionability_quadrant.png` |
| 35 | Impact × Actionability quadrant (OULAD) | OULAD | `DEEP-SEF-OULED/figures/18_intervention_actionability_quadrant.png` |
| 36 | Policy-lever timeline (UCI) | UCI | `DEEP-SEF-UCI-PRIMARY/figures/19_policy_lever_timeline.png` |
| 37 | Policy-lever timeline (OULAD) | OULAD | `DEEP-SEF-OULED/figures/19_policy_lever_timeline.png` |

> **Note.** The manuscript is a `pandoc`-style markdown export; the
> `![][imageN]` syntax is a placeholder that is resolved by a
> `pandoc`/`docx` post-processor. The manifest above records the canonical
> path of every image that the corresponding notebook writes. The actual
> image-embedding step in the camera-ready PDF is performed by the journal
> typesetter using the caption-to-file map in this manifest.

## Asset counts

```
DEEP-SEF-UCI-PRIMARY/figures/  -> 32 PNG files
DEEP-SEF-OULED/figures/        -> 32 PNG files
```
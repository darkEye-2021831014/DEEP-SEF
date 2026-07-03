# Figures — Caption-by-Caption

A caption-by-caption walk-through of every figure in the manuscript,
with the notebook cells that produce them. The full path mapping is
also recorded in [`figures/FIGURE_MANIFEST.md`](../figures/FIGURE_MANIFEST.md).

## Figure 1 — End-to-end pipeline
Schematic of the DEEP-SEF pipeline across two datasets and three
temporal horizons. Drawn from the architecture diagram in §4 of the
manuscript.

## Figure 2 — Binary class distribution
UCI (Graduate 60.9 %, Dropout 39.1 %) vs OULAD (Pass/Distinction
47.2 %, Fail/Withdrawn 52.8 %).

## Figure 3 — UCI per-horizon feature count
37 → 52 → 74 engineered features at t0 / t1 / t2.

## Figure 4 — OULAD per-horizon feature count
43 → 58 → 84 engineered features at t0 / t1 / t2.

## Figure 5 — Stratified train-test split
UCI 80/20 (2,904 / 726) and OULAD 85/15 (27,730 / 4,863).

## Figure 6 — Stacking architecture
OOF matrix augmented with 6 per-student aggregates, fed to a
per-horizon LightGBM-vs-CatBoost meta contest.

## Figure 7 — Optuna Bayesian HPO loop
TPE sampler proposes hyper-parameters, candidate is scored by 5-fold
CV-AUC.

## Figures 8–10 — Base-learner diagnostics
Per-horizon accuracy (Fig 8), per-horizon metrics (Fig 9), and base-
learner correlation heatmaps (Fig 10) on UCI.

## Figures 11–12 — Stacking vs blend
DEEP-SEF stacking AUC versus the best single base learner and a simple
mean blend on UCI (Fig 11) and OULAD (Fig 12).

## Figures 13–16 — Final results
Confusion matrices (UCI, OULAD), ROC curves, and reliability diagrams.

## Figure 17 — Per-horizon metrics UCI vs OULAD
Lines track closely between datasets, indicating that DEEP-SEF transfers
across institutions under documented architectural differences.

## Figures 18–19 — Open-world rejection summary
UCI: 10–11 % abstention. OULAD: 21–29 % abstention.

## Figures 20–23 — Layer-wise ablation
Coverage-vs-abstention frontier, advisor time saved, incremental value
of each layer, prediction-set size distribution.

## Figure 24 — Cross-dataset calibration
Mean metrics across the three horizons, UCI vs OULAD.

## Figures 25–26 — SHAP UCI
SHAP summary (beeswarm) at t0 and top-15 SHAP bar across t0/t1/t2.

## Figures 27–29 — SHAP OULAD
Top-15 SHAP bar at t0, t1, t2.

## Figures 30–31 — Risk-family impact
Mean |SHAP| per family at t0/t1/t2 on UCI; same analysis UCI vs OULAD.

## Figures 32–33 — K-means archetypes
Four advisor archetypes at t2 on UCI and OULAD. The two high-risk
archetypes account for 35 % (UCI) and 51 % (OULAD) of the cohort.

## Figures 34–35 — Impact × Actionability quadrant
Features in the high-impact, high-actionability quadrant are
prioritised for advising interventions.

## Figures 36–37 — Policy-lever timeline
SHAP impact translated to a sequence of advising actions, validated
against retention-theory constructs from Tinto, Bean, Astin, Braxton,
Berger & Braxton, and Kuh.
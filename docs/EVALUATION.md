# Evaluation

This document expands on §5 of the manuscript and is the canonical
reference for the metric definitions, the bootstrap CI procedure, the
DeLong paired test, and the layer-wise ablation design.

## 1. Metrics

The primary task is binary classification (`Dropout` vs `Graduate` on
UCI; `Fail/Withdrawn` vs `Pass/Distinction` on OULAD). The reported
metrics are:

| Metric | Definition | Used for |
|--------|------------|----------|
| Accuracy | `(TP + TN) / (TP + TN + FP + FN)` | Tables 2, 3, 6, 7 |
| Precision | `TP / (TP + FP)` | Tables 2, 3, 6, 7 |
| Recall | `TP / (TP + FN)` | Tables 2, 3, 6, 7 |
| F1 | `2 P R / (P + R)` | Tables 2, 3, 6, 7 |
| AUC | Area under the ROC curve | Tables 2, 3, 4, 5, 6, 7, 12 |
| Brier | Mean squared error between `p̂` and `y` | Tables 6, 7, 11 |
| LogLoss | `-y log p̂ - (1-y) log (1-p̂)` | Tables 6, 7 |
| τ* | Youden-J optimal threshold (`TPR + TNR - 1` maximised) | Tables 6, 7 |
| T* | Post-hoc temperature scaling factor | Tables 6, 7 |
| Coverage | Empirical marginal coverage at α = 0.10 | Tables 8, 11 |
| Avg set size | Mean size of the conformal prediction set | Tables 8, 23 |
| Reject rate | Fraction of test students abstained by the GMM head | Table 9 |
| Actionable precision | Precision of the positive class among the retained population | Table 11 |
| Advisor hours saved | `(n_abstain × 0.25 h) - (n_review × 0.10 h)` | Figure 21 |

## 2. 95 % bootstrap CI on AUC

We use a 2,000-replicate non-parametric bootstrap of the held-out test
set. For each replicate `b`:

1. Sample with replacement `n_test` indices from the test set.
2. Compute `AUC_b = AUC(y_b, p̂_b)`.
3. If `len(unique(y_b)) < 2`, skip the replicate.

The reported 95 % CI is `[Q_0.025, Q_0.975]` of the resulting AUC
distribution. The point estimate is the AUC on the full test set.

Implementation: see `scripts/reproduce_results.py`. Seed is fixed at 42
for full determinism.

## 3. DeLong paired test (Table 12)

For the UCI vs-classical-baseline comparison we use the paired DeLong
test (DeLong, DeLong & Clarke-Pearson, 1988):

```
z = (AUC_DEEP-SEF - AUC_baseline) / sqrt(Var(AUC_DEEP-SEF) + Var(AUC_baseline) - 2 Cov(AUC_DEEP-SEF, AUC_baseline))
```

Reported in §6.1 of the manuscript.

| Horizon | DEEP-SEF | ExtraTrees | HistGB | DeLong z (vs ET) | p-value |
|---------|----------|------------|--------|------------------|---------|
| t0 | 0.855 | 0.828 | 0.826 | +3.58 | 0.0003 |
| t1 | 0.947 | 0.944 | 0.945 | +1.08 | 0.28 |
| t2 | 0.974 | 0.974 | 0.973 | -0.43 | 0.67 |

## 4. Layer-wise ablation (Table 11)

We compare four configurations on the held-out UCI test set at t0:

1. **Base stacker only** — `s*(P_oof)` with no conformal or rejection.
2. **+ Mondrian conformal (α = 0.10)** — adds prediction-set reporting.
3. **+ Gaussian-mixture rejection (10 % budget)** — abstains on 10 %
   of the test students.
4. **+ Both** — the full DEEP-SEF pipeline.

Reported metrics: AUC, coverage, Brier, actionable precision.

## 5. Reported as `n/a`

`TabPFN` and `FT-Transformer` are reported as `n/a` on OULAD in Table 3
because:

* TabPFN is restricted to ~10 000 training rows; `n_train_OULAD =
  27 730 > 10 000`.
* FT-Transformer was trained on OULAD during early experimentation but
  underperformed the gradient-boosted trees by 0.011 AUC and was
  dropped from the final OULAD stack.

The exclusion is intentional and documented (§3.4 of the manuscript).
No silent substitution occurs.
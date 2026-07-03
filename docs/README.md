# Documentation

Extended reference material that complements the manuscript and the
top-level `README.md`.

## Contents

| File | Purpose |
|------|---------|
| [`DATA.md`](DATA.md) | Dataset cards (UCI + OULAD), feature-engineering recipe, reproducibility settings. |
| [`METHODS.md`](METHODS.md) | Algorithmic reference: notation, pipeline diagram, family coverage, calibration primitives, conformal / open-world details, SHAP / policy-lever procedure. |
| [`EVALUATION.md`](EVALUATION.md) | Metric definitions, bootstrap CI procedure, statistical tests, layer-wise ablation design. |
| [`FIGURES.md`](FIGURES.md) | Caption-by-caption walk-through of every figure in the manuscript, with the notebook cells that produce them. |
| [`LIMITATIONS.md`](LIMITATIONS.md) | Long-form expansion of §8.5 of the manuscript: leakage risk, OOD calibration, deployment scope. |

## Reading order

1. `README.md` at the repository root — top-level orientation.
2. `docs/DATA.md` — what the inputs are.
3. `docs/METHODS.md` — what the pipeline does.
4. `docs/EVALUATION.md` — what the numbers mean.
5. `docs/FIGURES.md` — what every figure shows.
6. `docs/LIMITATIONS.md` — what the paper does not claim.
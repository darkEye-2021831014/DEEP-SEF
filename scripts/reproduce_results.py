"""
DEEP-SEF — Reproduce headline results from the published artefacts.

This script loads the per-step CSVs that ship with the repository and
prints the exact numbers reported in Tables 2, 3, 4, 6, 7, 8, 9, 12 of
the manuscript. It then recomputes the 95 % bootstrap CI on the
held-out test set from the raw probability CSVs as an independent
sanity check.

Use this as a sanity check that the published artefacts are intact and
reproducible from the repository alone. To re-train from scratch, run
the Jupyter notebooks ``DEEP-SEF-UCI-PRIMARY.ipynb`` and
``DEEP-SEF-OULED.ipynb``.

Usage
-----
    python scripts/reproduce_results.py [--dataset uci|oulad|all]
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

REPO_ROOT = Path(__file__).resolve().parent.parent
RNG_SEED = 42
N_BOOTSTRAP = 2000
ALPHA = 0.10


def _bootstrap_auc_ci(y_true: np.ndarray, y_score: np.ndarray,
                      n_boot: int = N_BOOTSTRAP,
                      seed: int = RNG_SEED) -> tuple[float, float, float]:
    """2.5 % / 97.5 % non-parametric bootstrap percentile CI on AUC.

    Uses a fixed RNG seed for full determinism (NeurIPS 2019
    reproducibility recommendation).
    """
    from sklearn.metrics import roc_auc_score

    rng = np.random.default_rng(seed)
    n = len(y_true)
    aucs = np.empty(n_boot, dtype=float)
    valid = 0
    for i in range(n_boot):
        idx = rng.integers(0, n, size=n)
        if len(np.unique(y_true[idx])) < 2:
            continue
        aucs[valid] = roc_auc_score(y_true[idx], y_score[idx])
        valid += 1
    point = roc_auc_score(y_true, y_score)
    lo, hi = np.nanpercentile(aucs[:valid], [2.5, 97.5])
    return float(point), float(lo), float(hi)


def _load_hpo_params(dataset_dir: Path) -> dict:
    """Concatenate the three per-horizon HPO JSON files into one dict."""
    out: dict = {}
    for h in ("t0", "t1", "t2"):
        p = dataset_dir / "meta" / f"06_hpo_best_params_{h}.json"
        if p.exists():
            out[h] = json.loads(p.read_text())
    return out


def _print_hpo(hpo: dict) -> None:
    for h, params in hpo.items():
        print(f"\n[{h}] best Optuna CV-AUC per learner:")
        for learner, blob in params.items():
            print(f"   - {learner:<10s}  CV-AUC = {blob['best_value']:.4f}")


def _print_stacking_metrics(dataset_dir: Path) -> None:
    p = dataset_dir / "csv" / "11_stacking_metrics.csv"
    if not p.exists():
        return
    df = pd.read_csv(p)
    print("\nDEEP-SEF stacking metrics (per horizon):")
    cols = ["horizon", "accuracy", "precision", "recall", "f1",
            "auc", "brier", "logloss", "T"]
    present = [c for c in cols if c in df.columns]
    print(df[present].to_string(index=False, float_format="%.4f"))


def _print_meta_comparison(dataset_dir: Path) -> None:
    p = dataset_dir / "csv" / "10b_meta_learner_comparison.csv"
    if not p.exists():
        return
    df = pd.read_csv(p)
    print("\nPer-horizon meta-learner contest (Table 4):")
    print(df.to_string(index=False, float_format="%.6f"))


def _print_conformal(dataset_dir: Path) -> None:
    p = dataset_dir / "csv" / "12_conformal_summary.csv"
    if not p.exists():
        return
    df = pd.read_csv(p)
    print("\nMondrian conformal prediction summary (alpha = %.2f):" % ALPHA)
    print(df.to_string(index=False, float_format="%.4f"))


def _print_open_world(dataset_dir: Path) -> None:
    p = dataset_dir / "csv" / "13_open_world_summary.csv"
    if not p.exists():
        return
    df = pd.read_csv(p)
    print("\nOpen-world rejection summary (Table 9):")
    print(df.to_string(index=False, float_format="%.4f"))


def _print_baselines(dataset_dir: Path) -> None:
    p = dataset_dir / "csv" / "22_baselines_et_hgb.csv"
    if not p.exists():
        return
    df = pd.read_csv(p)
    print("\nClassical baselines (Table 12):")
    print(df.to_string(index=False, float_format="%.3f"))


def _print_bootstrap_ci(dataset_dir: Path) -> None:
    """Independent bootstrap CI recompute from raw probability CSVs."""
    for h in ("t0", "t1", "t2"):
        meta_test = dataset_dir / "csv" / f"10_meta_test_{h}.csv"
        if not meta_test.exists():
            continue
        df = pd.read_csv(meta_test)
        if not {"test_prob", "true"}.issubset(df.columns):
            continue
        y = df["true"].to_numpy(dtype=int)
        p = df["test_prob"].to_numpy(dtype=float)
        auc, lo, hi = _bootstrap_auc_ci(y, p)
        print(f"   [{h}] bootstrap AUC = {auc:.3f}  95% CI [{lo:.3f}, {hi:.3f}]  "
              f"(recomputed from 10_meta_test_{h}.csv)")


def _report_dataset(name: str, dataset_dir: Path) -> None:
    print(f"\n{'=' * 60}\n  {name} — DEEP-SEF artefact summary\n{'=' * 60}")

    hpo = _load_hpo_params(dataset_dir)
    _print_hpo(hpo)
    _print_meta_comparison(dataset_dir)
    _print_stacking_metrics(dataset_dir)
    print("\n95 % bootstrap CI on test-set AUC (recomputed):")
    _print_bootstrap_ci(dataset_dir)
    _print_conformal(dataset_dir)
    _print_open_world(dataset_dir)
    _print_baselines(dataset_dir)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", choices=["uci", "oulad", "all"], default="all")
    args = parser.parse_args()

    targets = []
    if args.dataset in ("uci", "all"):
        targets.append(("UCI (primary)", REPO_ROOT / "DEEP-SEF-UCI-PRIMARY"))
    if args.dataset in ("oulad", "all"):
        targets.append(("OULAD (cross-dataset)", REPO_ROOT / "DEEP-SEF-OULED"))

    for name, d in targets:
        if d.exists():
            _report_dataset(name, d)
        else:
            print(f"[skip] {name}: directory not found at {d}")


if __name__ == "__main__":
    main()
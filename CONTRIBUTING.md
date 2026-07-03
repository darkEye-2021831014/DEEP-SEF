# Contributing to DEEP-SEF

Thank you for your interest in DEEP-SEF. This repository accompanies a
peer-reviewed publication, so changes need to be coordinated with the
authors to keep the published artefacts consistent.

## How to contribute

1. **Fork** the repository and create a feature branch.
2. **Open an issue first** describing the change you want to make —
   especially if it changes the published numbers. We will tag the
   issue with `paper-impacting` or `non-paper-impacting`.
3. Make your change in the feature branch and **open a pull request**
   that references the issue.

## Coding conventions

* Python ≥ 3.10; follow PEP 8.
* Use type hints in new code.
* Keep notebooks top-to-bottom runnable. Restart the kernel and re-run
  all cells before opening a PR.
* Use the project's `requirements.txt` as the source of truth for
  dependencies; update it via a separate PR.
* Run `ruff check .` and `black .` before pushing.

## Reproducibility rules

* Do not commit large binary artefacts (`*.pkl`, `*.h5`, `*.ckpt`) to
  Git history. The shipped `models/` directory contains only the
  small `joblib` stackers that the paper references.
* If you add a new figure or table, update `figures/FIGURE_MANIFEST.md`
  and the manuscript's reference list.

## Reporting bugs

Please use the GitHub issue tracker. Include:

* the exact command or notebook cell that failed,
* the full traceback,
* your OS, Python version, and the relevant `pip freeze` excerpt.

## Code of conduct

This project follows the Contributor Covenant, version 2.1. By
participating, you agree to abide by its terms.
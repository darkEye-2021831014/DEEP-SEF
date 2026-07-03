# Limitations

This document expands on §8.5 of the manuscript and is the canonical
reference for the limitations of DEEP-SEF.

## 1. Dataset coverage

Both datasets come from European / online higher-education institutions.
Empirical results may not transfer to on-campus institutions in low-
and middle-income countries with different macro-economic conditions.

* UCI: Portuguese higher-education institution.
* OULAD: UK distance-learning institution.

The OULAD feature set uses UK macro-economic indicators (GDP, UnempRate,
Inflation) that are not available for every institution; in those cases
the DEEP-SEF pipeline falls back to institution-specific proxies.

## 2. Base-learner asymmetry

The OULAD final stack is four-learn (LightGBM / CatBoost / XGBoost /
ExtraTrees) rather than the full six-learn UCI stack because:

1. **TabPFN** is restricted to ~10 000 training rows. The OULAD
   training set has 27 730 presentations and is therefore outside the
   TabPFN context.
2. **FT-Transformer** was trained on OULAD during early experimentation
   but underperformed the gradient-boosted trees by 0.011 AUC
   (CV-AUC 0.974 vs 0.985 at t2) and was dropped from the final stack.

This is an intentional, documented difference (§3.4 of the manuscript),
not a hidden substitution.

## 3. Open-world rejection rate

The OULAD abstention rate of 21 – 29 % is high. Institutions that
prefer a lower rejection rate can lower the OOD threshold to the
80th percentile at the cost of more confident-but-wrong predictions.
We recommend that deployment teams tune the abstention budget jointly
with the available advising capacity rather than treating it as a
fixed hyper-parameter.

## 4. Calibration

The post-hoc temperature scaling layer was inert in this study. The
optimiser converged to **T* = 1.0** at every horizon of both
datasets. The reliability we report is therefore a property of the
base learners, the meta-learner, and the OOF estimation pipeline
rather than of the calibration step. We do not interpret this as
evidence that temperature scaling is unnecessary in general; it is
evidence that the stacked probabilities in DEEP-SEF are already well
calibrated on the calibration half of the training set without an
explicit rescaling step.

## 5. Feature-leakage risk at t2

Several t2 features on UCI — `cum_efficiency`, `academic_distress`,
`total_failures`, `avg_grade`, `s1_to_s2_grade_delta`, `s2_grade` —
are derived from within-semester outcomes that are temporally close to
the dropout label. We do not believe these features constitute direct
label leakage (they are computed from in-semester assessments, not from
the dropout label itself), but the t2 AUC of 0.974 with a 0.986 upper
CI bound should be read with caution: the model is partly predicting
label-correlated curricular outcomes at t2, which is closer to a
within-sample extrapolation than to an out-of-sample forecast.

The same caveat applies to OULAD t2, where cumulated assessment
features have an even tighter temporal relationship with the
`final_result` label.

Two remedies are needed to confirm the t2 number, and they are not
interchangeable:

1. **Causal time-split validation.** Train on one semester, test on a
   later semester, ruling out temporal autocorrelation in the test
   set.
2. **Distribution-shift-robust conformal re-calibration.** Apply the
   adaptive conformal scheme of Gibbs & Candès (2021) for cross-
   cohort deployment.

## 6. Cross-cohort deployment

The Mondrian conformal layer offers distribution-free marginal
coverage guarantees on the training cohort. If the deployment cohort
differs from the training cohort (different institution, different
intake year, different macro-economic conditions), the marginal
coverage guarantee may not transfer. Cross-cohort deployment is
treated as future work; institutions planning a multi-institutional
roll-out should re-calibrate the conformal layer on a representative
slice of the deployment cohort before going live.

## 7. Policy-lever timeline

The policy-lever timeline (§7.5 and §8.4 of the manuscript) maps SHAP
family impact to generic intervention categories ("front-load financial
aid", "trigger tutoring") without engaging the retention-practitioner
literature. We position the policy-lever timeline as a hypothesis-
generation artefact for retention practitioners, not as a validated
intervention prescription. Future work should evaluate the policy
levers with a randomised controlled trial design (intervention cohort
vs. control cohort) before any operational deployment.
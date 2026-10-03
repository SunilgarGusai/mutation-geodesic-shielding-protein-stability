# Frozen results

This page is the reviewer-facing map from headline manuscript evidence to committed machine-readable sources.

## Development / target-free characterization

Source: [`results/mgsc_characterization.csv`](../results/mgsc_characterization.csv)

| Quantity | Frozen value |
|---|---:|
| Development mutations | **382,543** |
| Parent proteins | **408** |
| Homology groups | **154** |
| Whole-mutation shielded | **147,448** |
| Whole-mutation shielded fraction | **38.544%** |
| Approx. shielded fraction at 6 Å | **44.34%** |
| Approx. shielded fraction at 8 Å | **41.85%** |
| Approx. shielded fraction at 10 Å | **45.49%** |
| Approx. shielded fraction at 12 Å | **46.57%** |
| MGSC/direct-silence mismatches | **0** |

The zero-mismatch result is an exhaustive computational verification of the exact certificate implementation under the fixed graph model. It is **not** independent biological validation.

## Protected grouped predictive boundary

Source: [`results/predictive_added_value.csv`](../results/predictive_added_value.csv)

| Model / contrast | Frozen value |
|---|---:|
| M2-R MAE | **0.573765 kcal/mol** |
| M2-R + GS3 MAE | **0.572973 kcal/mol** |
| MAE improvement | **+0.0007915 kcal/mol** |
| 95% homology-group bootstrap CI | **[-0.000274, +0.001700]** |
| Outer folds favoring GS3 | **4 / 5** |

Because the primary uncertainty interval crosses zero, the study does **not** claim robust nonlinear predictive added value.

The Ridge result remains a sensitivity analysis and is not promoted over the frozen primary HGB comparison.

## Independent external stability analyses

Source: [`results/external_validation.csv`](../results/external_validation.csv)

| Analysis | Estimate | 95% homology-group bootstrap CI | Interpretation |
|---|---:|---:|---|
| H1 site-level GEO_SUSC | **-1.01107** | **[-1.37692, -0.61688]** | Association supported |
| S1 adjusted GEO_SUSC | **-0.09236** | **[-0.40795, +0.16936]** | Independent adjusted association not supported |
| H2 same-site contrast | **+0.40151 kcal/mol** | **[+0.27047, +0.74082]** | Observational same-site contrast supported |

H1 uses 1,245 sites from 61 proteins in 52 external homology groups.

H2 uses 103 sites where both propagation-positive and shielded substitutions are experimentally represented. It remains observational and is not a causal claim.

## Explicit-mutant structural evidence

Sources:

- [`results/structural_credibility.csv`](../results/structural_credibility.csv)
- [`results/structural_radius_robustness.csv`](../results/structural_radius_robustness.csv)
- [`results/structural_cluster_class_counts.csv`](../results/structural_cluster_class_counts.csv)

| Quantity | Frozen value |
|---|---:|
| Eligible direct WT→mutant variants | **342** |
| Structural clusters | **13** |
| Mixed-class clusters | **5** |
| Prespecified minimum mixed clusters | **8** |
| Equal-cluster virtual/explicit signed cosine | **0.83845** |
| Explicit normalized response difference | **+0.18347** |
| Confirmatory status | **INCONCLUSIVE** |

The structural result is therefore presented as descriptive credibility evidence rather than a passed confirmatory gate.

## Parent-origin prevalence

Source: [`results/parent_origin_shielding_prevalence.csv`](../results/parent_origin_shielding_prevalence.csv)

| Parent origin | Shielded fraction |
|---|---:|
| Natural | **37.33%** |
| de novo | **41.25%** |

These values are descriptive and are not used to redefine the primary method or endpoint.

## Claim boundary

The machine-readable claim register is [`results/claim_register.csv`](../results/claim_register.csv).

The central permitted interpretation is:

> MGSC provides an exact fixed-topology geodesic-shielding construction, exposes substantial mutation-dependent route shielding in the development cohort, and shows independently observed stability associations whose adjusted, predictive, and structural limits remain explicit.

The repository must not be read as evidence for thermodynamic equivalence, causal allostery, environment-independent stability information, or universal predictor superiority.

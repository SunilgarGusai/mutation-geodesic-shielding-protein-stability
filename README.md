# Mutation Geodesic Shielding Characterizes Residue-Network Susceptibility in Protein Stability

Public reproducibility repository for the Mutation Geodesic Shielding Certificate (MGSC) study.

**Authors:** Sunilgar Laxmangar Gusai (corresponding author) and Manoharsinh R. Jadeja  
**Correspondence:** dr.sunilgargusai@gmail.com

## What MGSC measures

MGSC separates mutation-bypassing geodesics from mutation-containing geodesics in local chemically weighted residue-interaction graphs. It is an interpretable network-susceptibility framework, not a thermodynamic energy and not a claim of superior stand-alone ΔΔG prediction.

The fixed-topology identity is

```text
d_S(i,j) = min{ b(i,j), q_S(i,j) }
gamma_S(i,j) = q_S(i,j) - b(i,j)
```

where `b(i,j)` is the state-invariant shortest bypass after deleting the mutation node and `q_S(i,j)` is the best route constrained to traverse the mutation node in state `S`.

## Frozen headline results

- 382,543 development mutations from 408 parents in 154 homology groups.
- 147,448 mutations (38.544%) were whole-mutation geodesically shielded.
- MGSC and direct geodesic-silence classification agreed without mismatches across the full development cohort and all four prespecified radii.
- Compact shielding summaries did not show supported incremental nonlinear ΔΔG prediction beyond the direct local structural/chemical baseline.
- Independent external site-level association: β = -1.01107 kcal/mol per unit GEO_SUSC, 95% homology-group bootstrap CI [-1.37692, -0.61688].
- Adjusted external GEO_SUSC coefficient: β = -0.09236, 95% CI [-0.40795, 0.16936]; no environment-independent value claim is made.
- Same-site external contrast: +0.40151 kcal/mol, 95% CI [0.27047, 0.74082] for propagation-positive minus shielded substitutions.
- Explicit-mutant structural evidence is descriptive because only 5 mixed clusters were available versus the prespecified minimum of 8.

## Repository layout

- `src/` - reference MGSC implementation and graph-cost utilities.
- `tests/` - target-free identity/implementation tests.
- `results/` - machine-readable frozen aggregate results, cohort summaries, robustness tables, and claim register.
- `docs/` - method definition, provenance, current literature context, reproducibility notes, and interpretation boundaries.
- `environment/` - Python dependencies.
- `manuscript/` - current manuscript and Supporting Information LaTeX sources.
- `scripts/` - deterministic quantitative-figure regeneration scripts.
- `figures/` - publication figures or regeneration notes.

## Quick start

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
# source .venv/bin/activate
pip install -r environment/requirements.txt
pytest -q
```

## Data and licensing

Raw third-party protein-stability datasets and PDB/mmCIF structure archives are not mirrored here unless redistribution rights are explicit. See `docs/DATA_PROVENANCE.md`. Code is MIT-licensed; third-party datasets, structures, and publications retain their original licenses and terms.

## Scientific boundaries

This repository intentionally retains negative and inconclusive evidence. In particular, the study does not claim robust nonlinear predictive improvement beyond the direct structural/chemical baseline, does not claim environment-independent GEO_SUSC value after adjustment, and does not promote the explicit-mutant structural comparison beyond descriptive evidence.

## Citation

Citation metadata are provided in `CITATION.cff`. The final article DOI/archive DOI will be added when available.

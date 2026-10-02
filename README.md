# Mutation Geodesic Shielding Characterizes Residue-Network Susceptibility in Protein Stability

Public reproducibility repository for the Mutation Geodesic Shielding Certificate (MGSC) study of mutation-conditioned residue-network susceptibility and experimental protein-stability associations.

## Authors

- Sunilgar Laxmangar Gusai (corresponding author)
- Manoharsinh R. Jadeja

Correspondence: dr.sunilgargusai@gmail.com

## Scientific scope

MGSC separates mutation-bypassing geodesics from mutation-containing geodesics in local, chemically weighted residue-interaction graphs. The method is used as an interpretable network-susceptibility framework, not as a thermodynamic energy and not as a claim of superior stand-alone ΔΔG prediction.

The exact fixed-topology decomposition is

```
d_S(i,j) = min{ b(i,j), q_S(i,j) }
gamma_S(i,j) = q_S(i,j) - b(i,j)
```

where `b(i,j)` is the shortest path after deleting the mutation node and `q_S(i,j)` is the shortest route forced through the mutation node in state `S`.

## Frozen headline results

- Target-free development analysis: 382,543 mutations, 408 parents, 154 homology groups.
- MGSC-certified whole-mutation geodesic shielding: 147,448 / 382,543 = 38.544%.
- Exact MGSC/shielding agreement across the full development cohort and all four prespecified local radii.
- Incremental nonlinear ΔΔG prediction beyond the direct structural/chemical baseline was not supported.
- Independent external site-level association: beta = -1.01107 kcal/mol per unit GEO_SUSC, 95% homology-group bootstrap CI [-1.37692, -0.61688].
- After adjustment for conventional local structural/chemical variables, the GEO_SUSC coefficient was not supported as independent: beta = -0.09236, 95% CI [-0.40795, 0.16936].
- Same-site external contrast: propagation-positive minus shielded substitutions = +0.40151 kcal/mol, 95% CI [0.27047, 0.74082].
- Explicit-mutant structural analysis remains descriptive because 5 mixed structural clusters were available versus the prespecified minimum of 8.

## Repository layout

- `src/` — MGSC reference implementation and graph-cost utilities.
- `tests/` — target-free mathematical/implementation checks.
- `results/` — machine-readable frozen headline results used in the manuscript.
- `docs/` — scientific scope, data provenance, claim boundaries, and reproducibility notes.
- `environment/` — software requirements.
- `manuscript/` — submission manuscript source/PDF after final editorial QA.
- `figures/` — final publication figures after final editorial QA.

## Data provenance

The study uses public or independently accessible source datasets, including the Tsuboyama et al. mega-scale protein-stability resource, a PDB-mapped FireProt benchmark, and experimental WT/mutant structures from the Ssym/ProtDDG-Bench lineage. Raw third-party structures or datasets are not redistributed here unless redistribution rights are confirmed. Retrieval and provenance information are documented under `docs/`.

## Reproducibility boundary

The public repository records the frozen scientific definitions, major machine-readable result summaries, reference implementation, and publication materials. Large third-party source archives and author-side cached structures are intentionally excluded. No failed predictive analysis is reopened or tuned in this public release.

## License

Code is released under the MIT License. Third-party datasets, structures, and publications remain subject to their original licenses and terms.

# Reproducibility and audit policy

## Public purpose

This repository is the compact reviewer-facing reproducibility artifact for the MGSC study. It is designed to make the central equations, reference implementation, frozen aggregate evidence, provenance, interpretation boundaries, and numerical regeneration path directly inspectable.

## Frozen scientific state

The public repository reflects the final scientific state of the study. Failed predictive analyses remain failed; repository polishing is not used to retune radii, endpoints, models, subsets, or external hypotheses.

The independent external benchmark has already been used under its frozen analysis definition and is not a surface for additional feature, subgroup, endpoint, or model search.

## What the public repository contains

- exact MGSC method equations and compact implementation;
- chemical graph-cost utility;
- unit tests against direct all-pairs shortest-path recomputation;
- frozen machine-readable aggregate results;
- method, provenance, literature, and claim-boundary documentation;
- deterministic quantitative-figure regeneration;
- public artifact validation;
- GitHub Actions continuous verification;
- scientific SVGs used for repository communication.

## What is intentionally excluded

During peer review, this public repository does **not** contain:

- submitted manuscript PDF or LaTeX source;
- Supporting Information PDF/source;
- cover letter;
- journal portal forms;
- large raw third-party stability datasets;
- full PDB/mmCIF coordinate caches;
- author-side local execution caches and checkpoints.

The private author submission package and the public reproducibility repository are deliberately separated.

## Author-side archive

The larger author-side archive retains source-data snapshots/checksums, mappings, homology-group assignments, per-mutation feature tables, predictions, bootstrap outputs, structural mapping logs, local execution logs, and restartable Windows packages.

Some material cannot be redistributed directly because of third-party data/structure terms or size. The public repository therefore supports transparent audit of the reported aggregate evidence without claiming that every source byte is mirrored here.

## Public validation route

Create the environment and run:

```bash
python scripts/validate_public_artifact.py
pytest -q
python scripts/generate_quantitative_figures.py
```

The GitHub Actions workflow runs the same reviewer-facing checks on pull requests and pushes to `main`.

## Reproducibility boundary

The public reference implementation is sufficient to verify the mathematical decomposition and reproduce figures from the committed frozen aggregate tables. It is **not** presented as a byte-identical replay of the entire historical structure-processing pipeline.

No runtime advantage is claimed from an unrecorded benchmark. The computational reuse statement is structural: the mutation-deleted bypass graph is state-invariant and can be reused across substitution states at a site.

## Scientific integrity checks

The public validator explicitly checks that:

- development counts match the frozen cohort;
- whole-mutation shielded count/fraction match the committed record;
- MGSC/direct-silence mismatches remain zero;
- the primary added-information CI crosses zero;
- external H1 remains negative with a fully negative CI;
- adjusted S1 crosses zero;
- same-site H2 remains positive with a fully positive CI;
- structural mixed-cluster count remains below the prespecified confirmatory minimum;
- no manuscript PDF/LaTeX submission file is accidentally committed under `manuscript/`.

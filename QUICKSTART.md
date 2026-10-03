# Quick start

This repository is a compact public reproducibility artifact for the Mutation Geodesic Shielding Certificate (MGSC) study.

If you only want to understand the science, read in this order:

1. `README.md`
2. `docs/METHOD_PROTOCOL.md`
3. `docs/FROZEN_RESULTS.md`
4. `docs/CLAIM_BOUNDARIES.md`

## 1. Create the environment

### Conda

```bash
conda env create -f environment.yml
conda activate mgsc-protein-stability
```

### Or pip / venv

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 2. Run the mathematical / implementation tests

```bash
pytest -q
```

The reference tests compare the MGSC decomposition against direct all-pairs shortest-path recomputation on small positive-weight graphs.

## 3. Validate the curated public artifact

```bash
python scripts/validate_public_artifact.py
```

This checks required reviewer-facing files, curated manifest integrity, frozen numerical invariants, external H1/S1/H2 interval logic, structural testability status, and exclusion of submission manuscript PDF/LaTeX files from the public repository.

## 4. Regenerate quantitative figures

```bash
python scripts/generate_quantitative_figures.py
```

Generated PNG/PDF files are written to `figures/`. The committed result CSVs are the numerical source.

## 5. Inspect the central method

Reference implementation:

```text
src/mgsc.py
src/graph_costs.py
```

The public implementation demonstrates the exact fixed-topology decomposition. It does not contain the entire large author-side structure-processing pipeline or raw third-party structural archives.

## 6. Follow claims to evidence

Use:

```text
docs/FROZEN_RESULTS.md
results/README.md
REPOSITORY_MANIFEST.csv
```

The external benchmark is closed to further hypothesis search. Public result tables document frozen analyses rather than a tuning surface.

## 7. Data provenance and licensing

See:

```text
docs/DATA_PROVENANCE.md
THIRD_PARTY_LICENSES.md
LICENSE
```

Raw third-party datasets and coordinate archives are not mirrored unless redistribution rights are explicit.

## Important interpretation notes

- MGSC is a graph-geodesic certificate, not a thermodynamic energy.
- Exact certificate agreement is implementation verification of the fixed-topology identity, not independent biological validation.
- The primary nonlinear added-prediction interval crosses zero.
- The adjusted external GEO_SUSC interval crosses zero.
- The explicit-mutant structural comparison is descriptive because the prespecified mixed-cluster minimum was not reached.

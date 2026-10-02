# Data provenance

The study combines public protein-stability measurements, structures, and residue-interaction prior information.

## Development measurements

Tsuboyama et al., *Mega-scale experimental analysis of protein folding stability in biology and design*, Nature (2023), DOI: 10.1038/s41586-023-06328-6.

The frozen development workflow used quality-controlled single substitutions from the released Dataset 3 resource and homology-grouped evaluation.

## Independent external benchmark

The external benchmark was the PDB-mapped FireProt resource released with ThermoMPNN:

- ThermoMPNN paper: Dieckhaus et al., *Transfer learning to leverage larger datasets for improved prediction of protein stability changes*, PNAS (2024), DOI: 10.1073/pnas.2314853121.
- Zenodo dataset record: https://zenodo.org/records/8169289
- Published full benchmark identity: 3,438 mutations across 100 proteins before the study's frozen sequence-decontamination procedure.

External numerical ΔΔG labels were opened only after target-free mapping/features and the external hypotheses were frozen.

## Explicit WT/mutant structures

The structural-credibility analysis uses the Ssym lineage:

Pucci et al., *Quantification of biases in predictions of protein stability changes upon mutations*, Bioinformatics (2018), DOI: 10.1093/bioinformatics/bty348.

The analysis uses 342 direct WT-to-mutant variants so reverse copies are not double counted.

## Residue-pair statistical potential

Miyazawa and Jernigan, *Residue-residue potentials with a favorable contact pair term and an unfavorable high packing density term, for simulation and threading*, Journal of Molecular Biology (1996), DOI: 10.1006/jmbi.1996.0114.

The published MJ96 table is not reprinted in this repository. The reference implementation expects an audited external table and preserves the frozen positive-cost transformation.

## Raw-data redistribution

Large raw third-party datasets and coordinate archives are not redistributed here unless their licenses clearly permit redistribution. This repository instead provides provenance and frozen derived result summaries.
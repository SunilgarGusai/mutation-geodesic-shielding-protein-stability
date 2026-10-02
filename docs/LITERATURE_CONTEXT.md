# Literature context

This focused context file records literature that constrains the manuscript's novelty and interpretation. It is not intended as an exhaustive review.

## Mutation-local graph representations and stability prediction

- Pires, Ascher, and Blundell. *mCSM: predicting the effects of mutations in proteins using graph-based signatures*. Bioinformatics 30 (2014): 335-342. DOI: 10.1093/bioinformatics/btt691.
- Gong et al. *Unbiased curriculum learning enhanced global-local graph neural network for protein thermodynamic stability prediction*. Bioinformatics 39 (2023): btad589. DOI: 10.1093/bioinformatics/btad589.
- Li, Yao, and Fan. *ProSTAGE: Predicting Effects of Mutations on Protein Stability by Using Protein Embeddings and Graph Convolutional Networks*. Journal of Chemical Information and Modeling 64 (2024): 340-347. DOI: 10.1021/acs.jcim.3c01697.
- Xu, Liu, and Gong. *Improving the prediction of protein stability changes upon mutations by geometric learning and a pre-training strategy*. Nature Computational Science 4 (2024): 840-850. DOI: 10.1038/s43588-024-00716-2.

These works establish that local mutation environments, graphs, geometric learning, and graph neural networks are prior art. MGSC therefore is not positioned as the first local graph treatment of protein mutations.

## Physics/knowledge-based and symmetry-aware comparators

- Martín-Hernández et al. *Predicting protein stability changes upon mutation using a simple orientational potential*. Bioinformatics 39 (2023): btad011. DOI: 10.1093/bioinformatics/btad011.
- Dieckhaus et al. *Transfer learning to leverage larger datasets for improved prediction of protein stability changes*. PNAS 121 (2024): e2314853121. DOI: 10.1073/pnas.2314853121.
- Sanavia et al. *JanusDDG: a physics-informed neural network for sequence-based protein stability via two-fronts attention*. Communications Biology 9 (2026): 494. JanusDDG explicitly enforces antisymmetry and transitivity.

These works reinforce that thermodynamic symmetry constraints and strong modern prediction baselines are established prior art.

## Mutation propagation and residue-network communication

- Rajasekaran, Sekhar, and Naganathan. *A Universal Pattern in the Percolation and Dissipation of Protein Structural Perturbations*. Journal of Physical Chemistry Letters (2017). DOI: 10.1021/acs.jpclett.7b02021.
- pPerturb: a server for predicting long-distance energetic couplings and mutation-induced stability changes via perturbations (2019/2020 literature lineage).

Protein-network perturbation and long-range propagation are therefore not claimed as new concepts. The differentiated object in this work is the mutation-conditioned geodesic-shielding construction and its target-free/external evaluation.

## Method-comparison rigor

- *Practically Significant Method Comparison Protocols for Machine Learning in Small Molecule Drug Discovery*. Journal of Chemical Information and Modeling 65 (2025): 9398-9411. DOI: 10.1021/acs.jcim.5c01609.

The manuscript follows the same general principle: method comparisons should be leakage-aware, statistically explicit, and evaluated with practical as well as numerical significance in mind.

## Current novelty position

The manuscript does **not** claim novelty for shortest paths, replacement paths, residue networks, local mutation graphs, statistical potentials, mutation propagation, antisymmetry, or protein-stability prediction itself.

The manuscript's narrower methodological contribution is the protein-specific use of a mutation-deleted bypass graph and mutation-containing alternative routes to characterize when a mutation-site chemical reweighting is geodesically shielded from the surrounding residue network, together with exhaustive target-free characterization and independently frozen experimental stability tests.
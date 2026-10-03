# Public MGSC method protocol

This document records the compact public formulation supporting the manuscript. It is an interpretation/reproducibility specification, not a license to reopen frozen endpoints, radii, cohorts, or external hypotheses.

## 1. Local residue graph

For each candidate mutation site, residue-centered local sets are evaluated at prespecified radii:

- **6 Å**
- **8 Å**
- **10 Å**
- **12 Å**

The residue-contact topology uses an **8 Å Cα–Cα cutoff**. The virtual mutation model is fixed-topology: residue identity changes at the mutation site alter only the chemical weights of edges incident to that site.

## 2. Positive chemical path cost

For an interacting residue pair $i,j$, the frozen positive shortest-path cost is

$
c_{ij}
=
\frac{d_{ij}}{r(a_i)+r(a_j)}
\exp\left(
\frac{U(a_i,a_j)-\overline U_{210}}{s_{U,210}}
\right),
$

where:

- $d_{ij}$ is Cα distance;
- $r(a)$ is the audited residue-radius term for amino-acid type $a$;
- $U(a_i,a_j)$ is the MJ96 residue-pair statistical potential;
- $\overline U_{210}$ and $s_{U,210}$ are the mean and standard deviation over the 210 unordered residue pairs.

The transform is positive and monotone in the intended direction. It is a **graph-routing cost**, not a thermodynamic free energy.

## 3. Mutation-deleted bypass graph

Let $m$ be the mutation node and let

$
H=G-m.
$

For off-mutation residues $i,j$, define the state-invariant bypass distance

$
b(i,j)=d_H(i,j).
$

Because the virtual mutation changes only edges incident to $m$, $H$ can be reused across all substitution states at that site.

## 4. Mutation-containing route

For state $S$, define

$
q_S(i,j)
=
\min_{\substack{u,v\in N(m)\\u\ne v}}
\left[
d_H(i,u)+w_S(u,m)+w_S(m,v)+d_H(v,j)
\right].
$

For positive weights under the fixed topology,

$
d_S(i,j)=\min\{b(i,j),q_S(i,j)\}.
$

The shielding margin is

$
\gamma_S(i,j)=q_S(i,j)-b(i,j).
$

Interpretation:

- $\gamma_S(i,j)\ge 0$: an equally short or shorter bypass exists;
- $\gamma_S(i,j)<0$: the best mutation-containing route is shorter than the best bypass.

This decomposition is exact for the stated graph model. Generic shortest paths and replacement-path ideas are established prior art; the study contribution is the mutation-conditioned protein-network construction and its empirical characterization.

## 5. Mutation response and whole-mutation silence

For WT state $A$ and mutant state $B$, off-site distance response is

$
\Delta d(i,j)=d_B(i,j)-d_A(i,j).
$

A mutation is geodesically silent at one radius when every eligible off-mutation pair has zero response within the frozen numerical tolerance

$
|\Delta d(i,j)|\le 10^{-10}.
$

Whole-mutation shielding requires silence at every valid prespecified radius.

The public reference implementation is in [`src/mgsc.py`](../src/mgsc.py).

## 6. Site-level susceptibility

Each residue site is evaluated across the **19 possible non-WT amino-acid substitutions**. Substitution-specific shielding/propagation outcomes are aggregated into site-level geodesic susceptibility, denoted **GEO_SUSC** in the manuscript.

The public repository exposes the frozen aggregate results but does not reopen the original external labels for new subgroup or feature search.

## 7. Validation layers

### Target-free development characterization

- 382,543 substitutions
- 408 parent proteins
- 154 homology groups
- exact MGSC/direct-silence agreement checked across 6/8/10/12 Å

### Protected grouped added-information test

- 345,085 mutations
- 370 parents
- 129 protected homology groups
- direct structural/chemical baseline versus baseline + compact shielding summaries

### Independent external stability analysis

The external benchmark is analyzed under frozen site-level, adjusted-specificity, and same-site contrasts. External labels are not reused for unrestricted feature/model/subgroup search.

### Explicit-mutant structural credibility

Virtual fixed-coordinate perturbations are compared against experimental WT/mutant structures on 342 direct transitions across 13 structural clusters. Confirmatory interpretation is limited by the prespecified mixed-cluster criterion.

## 8. Interpretation boundary

MGSC characterizes **mutation-conditioned geodesic susceptibility** in local residue networks.

It does not by itself establish:

- thermodynamic free-energy change;
- physical allostery;
- causal biological signal propagation;
- universal superiority as a ΔΔG predictor;
- stability information independent of conventional local environment variables.

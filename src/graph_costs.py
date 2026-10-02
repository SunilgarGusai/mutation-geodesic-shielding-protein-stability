"""Chemical edge-cost utilities for the MGSC reference implementation."""

from __future__ import annotations

import math


def chemical_edge_cost(
    distance_angstrom: float,
    aa_i: str,
    aa_j: str,
    *,
    residue_radius: dict[str, float],
    mj96: dict[tuple[str, str], float],
    mj96_mean: float,
    mj96_sd: float,
) -> float:
    """Frozen interaction-conditioned positive shortest-path cost.

    c_ij = d_ij / (r_i + r_j) * exp((U_ij - mean(U)) / sd(U))

    The caller supplies the audited residue-radius and MJ96 tables. The full
    third-party table is not embedded here.
    """
    if distance_angstrom <= 0:
        raise ValueError("distance_angstrom must be positive")
    if mj96_sd <= 0:
        raise ValueError("mj96_sd must be positive")

    ai = aa_i.upper()
    aj = aa_j.upper()
    if ai not in residue_radius or aj not in residue_radius:
        raise KeyError("missing residue radius")

    pair = (ai, aj)
    rev = (aj, ai)
    if pair in mj96:
        u = mj96[pair]
    elif rev in mj96:
        u = mj96[rev]
    else:
        raise KeyError(f"missing MJ96 pair {ai}-{aj}")

    denom = residue_radius[ai] + residue_radius[aj]
    if denom <= 0:
        raise ValueError("residue radii must be positive")

    return (distance_angstrom / denom) * math.exp((u - mj96_mean) / mj96_sd)

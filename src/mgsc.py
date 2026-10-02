"""Reference implementation of the Mutation Geodesic Shielding Certificate (MGSC).

This module implements the exact fixed-topology decomposition used in the study.
It is intentionally compact and target-free. It does not read experimental ddG.
"""

from __future__ import annotations

from dataclasses import dataclass
import numpy as np
from scipy.sparse.csgraph import shortest_path


@dataclass(frozen=True)
class StateDecomposition:
    offsite_nodes: np.ndarray
    bypass: np.ndarray
    through_mutation: np.ndarray
    gamma: np.ndarray
    offsite_distance: np.ndarray


def _validate_weight_matrix(weights: np.ndarray, mutation_index: int) -> np.ndarray:
    w = np.asarray(weights, dtype=float)
    if w.ndim != 2 or w.shape[0] != w.shape[1]:
        raise ValueError("weights must be a square matrix")
    n = w.shape[0]
    if not (0 <= mutation_index < n):
        raise IndexError("mutation_index is out of range")
    if not np.allclose(w, w.T, equal_nan=True):
        raise ValueError("MGSC reference implementation expects an undirected graph")
    if not np.allclose(np.diag(w), 0.0):
        raise ValueError("weight-matrix diagonal must be zero")
    finite_offdiag = np.isfinite(w) & ~np.eye(n, dtype=bool)
    if np.any(w[finite_offdiag] <= 0):
        raise ValueError("all finite edge costs must be positive")
    return w


def state_decomposition(weights: np.ndarray, mutation_index: int) -> StateDecomposition:
    """Compute b(i,j), q_S(i,j), gamma_S(i,j), and d_S(i,j) for one state.

    Missing edges are represented by np.inf. The diagonal must be zero.
    Only the mutation node is removed when computing bypass distances.
    """
    w = _validate_weight_matrix(weights, mutation_index)
    n = w.shape[0]
    off = np.array([i for i in range(n) if i != mutation_index], dtype=int)
    pos = {node: k for k, node in enumerate(off.tolist())}

    h = w[np.ix_(off, off)]
    b = np.asarray(shortest_path(h, directed=False, unweighted=False), dtype=float)

    neighbors = [
        i for i in range(n)
        if i != mutation_index and np.isfinite(w[i, mutation_index])
    ]

    q = np.full_like(b, np.inf, dtype=float)
    for u in neighbors:
        for v in neighbors:
            if u == v:
                continue
            iu = pos[u]
            iv = pos[v]
            cand = (
                b[:, iu][:, None]
                + w[u, mutation_index]
                + w[mutation_index, v]
                + b[iv, :][None, :]
            )
            q = np.minimum(q, cand)

    d = np.minimum(b, q)
    gamma = q - b
    gamma[~(np.isfinite(q) & np.isfinite(b))] = np.nan

    return StateDecomposition(
        offsite_nodes=off,
        bypass=b,
        through_mutation=q,
        gamma=gamma,
        offsite_distance=d,
    )


def exact_offsite_response(
    wt_weights: np.ndarray,
    mutant_weights: np.ndarray,
    mutation_index: int,
) -> np.ndarray:
    """Return D_mut - D_wt for off-mutation node pairs."""
    wt = state_decomposition(wt_weights, mutation_index)
    mut = state_decomposition(mutant_weights, mutation_index)
    if not np.array_equal(wt.offsite_nodes, mut.offsite_nodes):
        raise RuntimeError("offsite node maps differ")
    return mut.offsite_distance - wt.offsite_distance


def whole_mutation_is_silent(
    wt_weights: np.ndarray,
    mutant_weights: np.ndarray,
    mutation_index: int,
    atol: float = 1e-10,
) -> bool:
    """True when every finite offsite shortest-path distance is unchanged."""
    delta = exact_offsite_response(wt_weights, mutant_weights, mutation_index)
    finite = np.isfinite(delta)
    if not finite.any():
        return True
    return bool(np.all(np.abs(delta[finite]) <= atol))


def transition_fractions(
    wt_weights: np.ndarray,
    mutant_weights: np.ndarray,
    mutation_index: int,
    atol: float = 1e-10,
) -> dict[str, float]:
    """Return SS/SM/MS/MM route-class fractions over finite unordered pairs.

    S means shielded (gamma >= 0); M means a route through the mutation node
    can be shorter (gamma < 0). Only the strict upper triangle is counted.
    """
    wt = state_decomposition(wt_weights, mutation_index)
    mut = state_decomposition(mutant_weights, mutation_index)
    finite = (
        np.isfinite(wt.bypass)
        & np.isfinite(wt.through_mutation)
        & np.isfinite(mut.bypass)
        & np.isfinite(mut.through_mutation)
    )
    tri = np.triu(np.ones_like(finite, dtype=bool), 1)
    mask = finite & tri
    if not mask.any():
        return {"SS": np.nan, "SM": np.nan, "MS": np.nan, "MM": np.nan}

    sw = wt.gamma[mask] >= -atol
    sm = mut.gamma[mask] >= -atol
    return {
        "SS": float(np.mean(sw & sm)),
        "SM": float(np.mean(sw & ~sm)),
        "MS": float(np.mean(~sw & sm)),
        "MM": float(np.mean(~sw & ~sm)),
    }

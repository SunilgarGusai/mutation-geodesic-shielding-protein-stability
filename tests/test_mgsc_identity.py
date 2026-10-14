import numpy as np
from scipy.sparse.csgraph import shortest_path

from src.mgsc import state_decomposition, exact_offsite_response, whole_mutation_is_silent


def full_apsp_offsite(w, m):
    d = np.asarray(shortest_path(w, directed=False, unweighted=False), dtype=float)
    keep = [i for i in range(w.shape[0]) if i != m]
    return d[np.ix_(keep, keep)]


def test_exact_decomposition_matches_full_apsp():
    inf = np.inf
    wt = np.array([
        [0.0, 1.0, 2.5, inf],
        [1.0, 0.0, 1.0, 1.5],
        [2.5, 1.0, 0.0, 1.0],
        [inf, 1.5, 1.0, 0.0],
    ])
    m = 1
    dec = state_decomposition(wt, m)
    direct = full_apsp_offsite(wt, m)
    np.testing.assert_allclose(dec.offsite_distance, direct, atol=1e-12)


def test_mutation_response_matches_two_full_apsp_runs():
    inf = np.inf
    wt = np.array([
        [0.0, 1.0, 2.5, inf],
        [1.0, 0.0, 1.0, 1.5],
        [2.5, 1.0, 0.0, 1.0],
        [inf, 1.5, 1.0, 0.0],
    ])
    mut = wt.copy()
    mut[0,1] = mut[1,0] = 1.8
    mut[1,2] = mut[2,1] = 1.4
    m = 1

    got = exact_offsite_response(wt, mut, m)
    expected = full_apsp_offsite(mut, m) - full_apsp_offsite(wt, m)
    np.testing.assert_allclose(got, expected, atol=1e-12)


def test_shielded_mutation_can_be_geodesically_silent():
    inf = np.inf
    wt = np.array([
        [0.0, 5.0, 1.0],
        [5.0, 0.0, 5.0],
        [1.0, 5.0, 0.0],
    ])
    mut = wt.copy()
    mut[0,1] = mut[1,0] = 7.0
    mut[1,2] = mut[2,1] = 7.0
    assert whole_mutation_is_silent(wt, mut, mutation_index=1)


def test_articulation_mutation_with_no_bypass():
    """Exact distance response remains valid when G-m disconnects a residue pair."""
    inf = np.inf
    wt = np.array([
        [0.0, 1.0, inf],
        [1.0, 0.0, 2.0],
        [inf, 2.0, 0.0],
    ])
    mut = wt.copy()
    mut[0, 1] = mut[1, 0] = 2.0
    m = 1

    wt_decomp = state_decomposition(wt, m)
    mut_decomp = state_decomposition(mut, m)
    assert np.isinf(wt_decomp.bypass[0, 1])
    assert np.isnan(wt_decomp.gamma[0, 1])
    assert np.isnan(mut_decomp.gamma[0, 1])

    # A route through m is the only finite 0 -> 2 route.
    assert wt_decomp.offsite_distance[0, 1] == 3.0
    assert mut_decomp.offsite_distance[0, 1] == 4.0
    delta = exact_offsite_response(wt, mut, m)
    assert delta[0, 1] == 1.0
    np.testing.assert_allclose(delta, full_apsp_offsite(mut, m) - full_apsp_offsite(wt, m))
    assert not whole_mutation_is_silent(wt, mut, m)

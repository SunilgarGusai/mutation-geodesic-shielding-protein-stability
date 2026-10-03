from __future__ import annotations

import csv
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "QUICKSTART.md",
    "CITATION.cff",
    "LICENSE",
    "THIRD_PARTY_LICENSES.md",
    "requirements.txt",
    "environment.yml",
    "REPOSITORY_MANIFEST.csv",
    "docs/METHOD_PROTOCOL.md",
    "docs/FROZEN_RESULTS.md",
    "docs/DATA_PROVENANCE.md",
    "docs/REPRODUCIBILITY.md",
    "docs/CLAIM_BOUNDARIES.md",
    "docs/assets/repository-banner.svg",
    "docs/assets/mgsc-workflow.svg",
    "docs/assets/geodesic-shielding.svg",
    "src/mgsc.py",
    "src/graph_costs.py",
    "tests/test_mgsc_identity.py",
    "scripts/generate_quantitative_figures.py",
    "results/mgsc_characterization.csv",
    "results/predictive_added_value.csv",
    "results/external_validation.csv",
    "results/structural_credibility.csv",
]

def rows(path: str):
    with (ROOT / path).open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))

def close(a: float, b: float, tol: float = 1e-9) -> bool:
    return math.isclose(a, b, rel_tol=0.0, abs_tol=tol)

def main() -> None:
    missing = [p for p in REQUIRED if not (ROOT / p).is_file()]
    assert not missing, f"Missing required public artifacts: {missing}"

    manifest = rows("REPOSITORY_MANIFEST.csv")
    manifest_paths = {r["path"] for r in manifest}
    unlisted = [p for p in REQUIRED if p not in manifest_paths and p != "REPOSITORY_MANIFEST.csv"]
    assert not unlisted, f"Required files absent from curated manifest: {unlisted}"

    mg = {r["metric"]: r["value"] for r in rows("results/mgsc_characterization.csv")}
    assert int(mg["development_mutations"]) == 382543
    assert int(mg["development_parents"]) == 408
    assert int(mg["development_homology_groups"]) == 154
    assert int(mg["whole_mutation_shielded"]) == 147448
    assert close(float(mg["whole_mutation_shielded_fraction"]), 0.38544)
    assert int(mg["mgsc_vs_exact_silence_mismatches"]) == 0

    pred = rows("results/predictive_added_value.csv")
    primary = next(
        r for r in pred
        if r["analysis"] == "primary_HGB" and r["model_or_contrast"] == "MAE_improvement"
    )
    p_est = float(primary["estimate"])
    p_lo = float(primary["ci_lower"])
    p_hi = float(primary["ci_upper"])
    assert close(p_est, 0.0007915)
    assert p_lo < 0 < p_hi, "Primary added-information CI must cross zero"

    ext = {r["analysis"]: r for r in rows("results/external_validation.csv")}
    h1 = ext["site_level_H1"]
    assert close(float(h1["estimate"]), -1.01107, 1e-8)
    assert float(h1["ci_lower"]) < 0 and float(h1["ci_upper"]) < 0

    s1 = ext["adjusted_specificity_S1"]
    assert close(float(s1["estimate"]), -0.09236, 1e-8)
    assert float(s1["ci_lower"]) < 0 < float(s1["ci_upper"])

    h2 = ext["same_site_H2"]
    assert close(float(h2["estimate"]), 0.40151, 1e-8)
    assert float(h2["ci_lower"]) > 0 and float(h2["ci_upper"]) > 0

    sc = {r["metric"]: r["value"] for r in rows("results/structural_credibility.csv")}
    assert int(sc["eligible_direct_variants"]) == 342
    assert int(sc["structural_clusters"]) == 13
    assert int(sc["mixed_class_clusters"]) == 5
    assert int(sc["prespecified_minimum_mixed_clusters"]) == 8
    assert int(sc["mixed_class_clusters"]) < int(sc["prespecified_minimum_mixed_clusters"])
    assert sc["confirmatory_status"].strip().upper() == "INCONCLUSIVE"

    manuscript_dir = ROOT / "manuscript"
    forbidden = list(manuscript_dir.glob("*.pdf")) + list(manuscript_dir.glob("*.tex"))
    assert not forbidden, f"Submission manuscript files must remain private: {forbidden}"

    print("PASS: MGSC public repository structure and frozen evidence invariants")

if __name__ == "__main__":
    main()

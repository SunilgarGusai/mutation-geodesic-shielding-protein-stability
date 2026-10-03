from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
OUT = ROOT / "figures"
OUT.mkdir(exist_ok=True)

# Figure 3: target-free shielding characterization
m = pd.read_csv(RESULTS / "mgsc_characterization.csv").set_index("metric")
radii = [6, 8, 10, 12]
vals = [
    float(m.loc["shielded_fraction_6A", "value"]) * 100,
    float(m.loc["shielded_fraction_8A", "value"]) * 100,
    float(m.loc["shielded_fraction_10A", "value"]) * 100,
    float(m.loc["shielded_fraction_12A", "value"]) * 100,
]
fig, ax = plt.subplots(figsize=(5.6, 3.8), dpi=300)
bars = ax.bar([str(r) for r in radii], vals)
ax.set_xlabel("Local radius (Å)")
ax.set_ylabel("Geodesically silent mutations (%)")
ax.set_title("Target-free MGSC shielding prevalence")
ax.set_ylim(0, max(vals) * 1.25)
for bar, value in zip(bars, vals):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, f"{value:.2f}%",
            ha="center", va="bottom", fontsize=8)
fig.tight_layout()
fig.savefig(OUT / "mgsc_shielding_prevalence.pdf")
fig.savefig(OUT / "mgsc_shielding_prevalence.png")
plt.close(fig)

# Figure 4: independent external stability effects
e = pd.read_csv(RESULTS / "external_validation.csv")
labels = {
    "site_level_H1": "H1 site-level GEO_SUSC",
    "adjusted_specificity_S1": "S1 adjusted GEO_SUSC",
    "same_site_H2": "H2 same-site contrast",
}
fig, ax = plt.subplots(figsize=(7.0, 3.9), dpi=300)
y = list(range(len(e)))
for yi, row in zip(y, e.itertuples(index=False)):
    est = float(row.estimate)
    lo = float(row.ci_lower)
    hi = float(row.ci_upper)
    ax.errorbar(est, yi, xerr=[[est - lo], [hi - est]], fmt="o", capsize=4)
ax.axvline(0, linestyle="--", linewidth=1)
ax.set_yticks(y, [labels.get(v, v) for v in e["analysis"]])
ax.set_xlabel("Estimate with 95% homology-group bootstrap interval")
ax.set_title("Independent external stability analyses")
fig.tight_layout()
fig.savefig(OUT / "external_stability_effects.pdf")
fig.savefig(OUT / "external_stability_effects.png")
plt.close(fig)

# Figure 5: explicit-mutant structural summary
s = pd.read_csv(RESULTS / "structural_credibility.csv").set_index("metric")
metrics = [
    ("equal_cluster_signed_cosine", "Virtual vs explicit\ncosine"),
    ("explicit_response_difference", "Propagation-positive − silent\nexplicit response"),
]
values = [float(s.loc[key, "value"]) for key, _ in metrics]
fig, ax = plt.subplots(figsize=(6.4, 3.8), dpi=300)
bars = ax.bar([label for _, label in metrics], values)
ax.axhline(0, linewidth=0.8)
ax.set_title("Descriptive explicit-mutant structural evidence")
ax.set_ylabel("Descriptive estimate")
for bar, value in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
            f"{value:.3f}", ha="center", va="bottom", fontsize=8)
ax.text(0.98, 0.03, "5 mixed clusters; prespecified minimum = 8\nConfirmatory status: INCONCLUSIVE",
        transform=ax.transAxes, ha="right", va="bottom", fontsize=8)
fig.tight_layout()
fig.savefig(OUT / "structural_credibility_summary.pdf")
fig.savefig(OUT / "structural_credibility_summary.png")
plt.close(fig)

print(f"Figures written to {OUT}")

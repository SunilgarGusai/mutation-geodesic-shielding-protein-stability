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
    float(m.loc["shielded_fraction_6A","value"])*100,
    float(m.loc["shielded_fraction_8A","value"])*100,
    float(m.loc["shielded_fraction_10A","value"])*100,
    float(m.loc["shielded_fraction_12A","value"])*100,
]
fig, ax = plt.subplots(figsize=(5.4,3.8), dpi=300)
ax.bar([str(r) for r in radii], vals)
ax.set_xlabel("Local radius (Å)")
ax.set_ylabel("Geodesically silent mutations (%)")
ax.set_title("MGSC shielding prevalence")
fig.tight_layout()
fig.savefig(OUT / "mgsc_shielding_prevalence.pdf")
fig.savefig(OUT / "mgsc_shielding_prevalence.png")
plt.close(fig)

# Figure 4: independent external stability effects
e = pd.read_csv(RESULTS / "external_validation.csv")
fig, ax = plt.subplots(figsize=(6.4,3.8), dpi=300)
y = range(len(e))
for yi, row in zip(y, e.itertuples(index=False)):
    est = float(row.estimate)
    lo = float(row.ci95_lower)
    hi = float(row.ci95_upper)
    ax.errorbar(est, yi, xerr=[[est-lo],[hi-est]], fmt="o", capsize=4)
ax.axvline(0, linestyle="--", linewidth=1)
ax.set_yticks(list(y), list(e["hypothesis"]))
ax.set_xlabel("Estimate with 95% homology-group bootstrap interval")
ax.set_title("Independent external stability analyses")
fig.tight_layout()
fig.savefig(OUT / "external_stability_effects.pdf")
fig.savefig(OUT / "external_stability_effects.png")
plt.close(fig)

# Figure 5: explicit-mutant structural summary
s = pd.read_csv(RESULTS / "structural_credibility.csv")
fig, ax = plt.subplots(figsize=(6.4,3.8), dpi=300)
subset = s[s["metric"].isin(["SC1_equal_cluster_mean_cosine","SC2_equal_cluster_difference"])]
ax.bar(subset["metric"], subset["value"].astype(float))
ax.tick_params(axis="x", rotation=20)
ax.set_title("Descriptive explicit-mutant structural evidence")
fig.tight_layout()
fig.savefig(OUT / "structural_credibility_summary.pdf")
fig.savefig(OUT / "structural_credibility_summary.png")
plt.close(fig)

print(f"Figures written to {OUT}")

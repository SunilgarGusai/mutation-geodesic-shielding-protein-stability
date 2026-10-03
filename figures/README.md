# Publication-figure regeneration

Quantitative repository figures are regenerated from the frozen machine-readable tables in `results/` by:

```bash
python scripts/generate_quantitative_figures.py
```

Generated outputs:

- `mgsc_shielding_prevalence.png/.pdf`
- `external_stability_effects.png/.pdf`
- `structural_credibility_summary.png/.pdf`

Conceptual repository graphics live under `docs/assets/` and are intentionally separate from numerical evidence.

The journal submission's premium figure artwork is maintained in the private submission package during peer review. The public repository therefore exposes the data-bearing regeneration path without publishing the submitted manuscript package.

No illustrative or AI-generated numerical value is used as evidence.

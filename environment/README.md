# Reference environment

This environment file supports the public MGSC reference implementation and tests.

The original author-side computation used a larger frozen local environment and cached public structural resources. Those large caches are not redistributed here. The publication repository therefore distinguishes:

1. the compact public reference implementation in `src/`;
2. machine-readable frozen result summaries in `results/`; and
3. the larger author-side computation archive retained for audit.

No numerical claim should be regenerated with altered graph definitions, radii, residue potentials, or cohort rules.
# Global Sensitivity Analysis for LCA
This package implements Global Sensitivity Analysis (GSA) for Life Cycle Assessment (LCA). At this stage, it uses the Delta
Moment-Independent measure (provided by [SALIB](https://salib.readthedocs.io/en/latest/api.html#delta-moment-independent-measure) 
based on Monte Carlo LCA results obtained using [Brightway2](https://brightway.dev). 

Monte Carlo simulation can include uncertainties for:
- elementary flows
- intermediate flows
- characterization factors

Due to the complexity of the brightway parameters package, we were not able to include parameters in this package.
Parameter uncertainties can, however, be included in the implementation of this GSA approach using the [Activity Browser](https://github.com/LCA-ActivityBrowser/activity-browser).

## Scientific paper
A scientific paper is in preparation and will be listed here once published. 

# Installation

```bash
conda install -y -q -c conda-forge -c cmutel -c bsteubing -c haasad monte_carlo_gsa
```
# License

BSD 2-clause license. Contributions are welcome!

# Authors

* Bernhard Steubing
* Daniel de Koning

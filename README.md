# Activation patching in controlled CNNs

**Reproducibility artifact** for the manuscript *When Do Activation-Patching Effects Add Up? Evidence from Controlled CNNs*, by Heriberto Espino Montelongo.

This repository contains frozen experimental protocols, selected analysis and evaluation code, derived numerical results, and the inputs needed to regenerate **all six manuscript figures and five supplementary figures**. The figures are reconstructed without the original model checkpoints.

The distinction is important: **this artifact reproduces figures and selected statistics from archived results; it does not retrain the CNNs or recompute every published statistical test.**

## Quick start

Python **3.10–3.12** is recommended.

```bash
git clone https://github.com/heri-espino/activation_patching_reproducibility.git
cd activation_patching_reproducibility
python -m pip install -r requirements.txt
python reproduce.py --all
```

The full command checks archive-source SHA-256 digests, validates local documentation links, regenerates all eleven figures, and independently recomputes selected numerical results. Generated output is written to `outputs/figures/` and `outputs/verification_report.json`; these files are intentionally not tracked.

Run an individual step:

```bash
python reproduce.py --check    # SHA-256 source inventory and README links; standard library only
python reproduce.py --numbers  # selected means and the paired BN2-GAP confidence interval
python reproduce.py --figures  # all eleven figure PDFs
```

## Results covered

| Location in paper | Figure | Generated file |
| --- | --- | --- |
| Manuscript Fig. 1 | Experimental setup and intervention | `fig00_overview.pdf` |
| Manuscript Fig. 2 | Compact filter gallery, retention vs. release | `fig05_kernel_gallery_compact.pdf` |
| Manuscript Fig. 3 | Observed and additive patching curves | `fig09_additivity_curves.pdf` |
| Manuscript Fig. 4 | Intervention size and architecture | `fig06_main_results.pdf` |
| Manuscript Fig. 5 | Structured versus pixel-permuted filters | `fig07_anchor_specificity.pdf` |
| Manuscript Fig. 6 | Observed versus reconstructed effects | `fig08_additivity.pdf` |
| Supplementary Fig. S1 | Learning curves | `fig01_learning.pdf` |
| Supplementary Fig. S2 | Patching curves | `fig02_patch_size.pdf` |
| Supplementary Fig. S3 | Template-matching trajectories | `fig03_matching_trajectories.pdf` |
| Supplementary Fig. S4 | Similarity matrices | `fig04_similarity_matrices.pdf` |
| Supplementary Fig. S5 | Complete first-layer filter gallery | `fig05_kernel_gallery.pdf` |

**Uncertainty:** Supplementary Figs. S1 and S3 display mean ± one standard deviation across saved runs. S2 uses the interval bounds stored in the archived table. S4 and S5 show a single historical example, not an aggregate or uncertainty estimate.

The gallery example is `two_concepts` / `TinyCNN`, renderer block `2000`, epochs `0` and `200`. The compact gallery displays the original templates and epoch-200 retention/release kernels. Its weights come from the archived compact NPZ; kernels are spatially centered, unit-norm normalized, assigned one-to-one to templates, and visualized on a shared symmetric color scale.

## Repository contents

| Location | Contents |
| --- | --- |
| [data/](data/) | Archived block-level and aggregate tables; compact filter arrays in `data/filter_structure/kernel_gallery.npz` |
| [code/figures/](code/figures/) | Original plot-generating scripts and figure styling |
| [code/experiments/](code/experiments/) | Selected frozen implementations and analysis utilities for inspection |
| [protocols/](protocols/) | Original protocols, with pre-specified analyses distinguished from post-hoc diagnostics |
| [reproduce.py](reproduce.py) | Independent verification and figure regeneration entry point |
| [manifest.json](manifest.json) | Original-to-exported source paths, source revision, sizes and SHA-256 hashes |
| [PROVENANCE_README.md](PROVENANCE_README.md) | Unmodified README from the original submission ZIP, preserved under a new filename |
| [RELEASE.md](RELEASE.md) | Versioning and Zenodo deposit instructions |
| [CITATION.cff](CITATION.cff) | Citation metadata for the software artifact |
| [.zenodo.json](.zenodo.json) | Zenodo release metadata |
| [LICENSE](LICENSE) | MIT license from the research repository |

### Numerical cross-check

The numerical verifier recalculates intervention-budget means and the paired observed-minus-additive BN2-GAP contrast over 100 renderer blocks:

- Mean difference: **−0.1799415521**
- 95% Student-*t* interval: **[−0.2008225633, −0.1590605409]**

These are comparisons against immutable archived tables, not independent retraining or re-estimation of every bootstrap, permutation, or equivalence result.

## Data provenance and limitations

The 125-item [manifest](manifest.json) records SHA-256 checksums, original research paths, and the source revision `4ccb2374bed0bf1d38eb9988726dba9a53b8c80e` from [the development repository](https://github.com/heri-espino/Regularizing-First-Layer-CNN-Filters-Toward-Predefined-Templates). The source archive's original README is preserved byte-for-byte as [PROVENANCE_README.md](PROVENANCE_README.md); its exported filename is updated in the manifest without altering its original hash. Additional public-facing repository metadata and CI configuration are **not** part of the frozen research-source inventory.

**Not included:** complete raw training runs, original saved model checkpoints, per-model evaluator JSON stores, or the full raw data required to repeat training and every inferential analysis. The experiments use procedurally generated images, but the supplied runnable interface is deliberately limited to reproduction from archived numerical inputs. Results should not be presented as newly trained or independently replicated by running `reproduce.py`.

## Citation

Please cite the associated article when a publication identifier becomes available, and cite the **versioned Zenodo record** of this artifact for reproducibility. A DOI has **not yet been assigned**; do not substitute a placeholder DOI.

GitHub citation metadata is in [CITATION.cff](CITATION.cff). After archiving the `v1.0.0` release in Zenodo, use the DOI shown on its published record.

## License

See [LICENSE](LICENSE) for the included MIT license. Research files retain their original provenance and descriptions in the manifest.

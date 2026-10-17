# Release and Zenodo deposit

This repository is the **public reproducibility artifact**, not the editorial source upload. The paper and the artifact receive **different DOIs** when published/deposited.

## Before making the first release

1. Verify that the frozen [manifest](manifest.json) contains 125 original research-source entries and that all required CSV and NPZ data files are committed. Do **not** remove data solely to reduce GitHub repository size.
2. Run `python -m pip install -r requirements.txt` and `python reproduce.py --all` on a clean checkout. Check that 11 nonempty PDFs and `outputs/verification_report.json` are generated.
3. Confirm [CITATION.cff](CITATION.cff), [.zenodo.json](.zenodo.json), and [LICENSE](LICENSE) contain accurate author, institutional and license details. Do not add a DOI until Zenodo has minted it.
4. Review the repository visibility: it must be public if you intend readers and reviewers to access it without an account.

## Create the citable release

1. Log in at [Zenodo](https://zenodo.org/) with your account. Under the GitHub integration, authorize GitHub and **enable** `heri-espino/activation_patching_reproducibility`.
2. On GitHub, create a **new Release**, not just a tag, with tag `v1.0.0`, targeting the verified `main` commit. Use title `Reproducibility artifact v1.0.0`.
3. Wait for Zenodo's ingestion and inspect the draft/record. Verify its file inventory, metadata, access settings and license. Publish the record if Zenodo requires an explicit publication action.
4. Record the DOI from the **published** Zenodo release. Link it in the journal's Code availability / Data availability metadata (or a permitted editorial note), and use that version DOI when citing the exact deposit.
5. Avoid changing or deleting the tagged release after publication. For substantive updates, make a subsequent version/release and allow Zenodo to preserve the earlier version.

**Do not create a release until the manuscript and archive metadata agree.** The research manuscript is a separate scholarly work; an artifact DOI does not imply that the article has been accepted by a journal.

## Policy for CI and heavy figure builds

Automatic CI runs only inexpensive inventory, documentation-link and file-structure tests. Rendering all eleven PDF figures is **manual only** via `python reproduce.py --all` on a clean checkout; nothing expensive runs on ordinary pushes.

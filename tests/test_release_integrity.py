"""Lightweight checks of release structure and frozen input coverage."""
from __future__ import annotations

import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReleaseIntegrity(unittest.TestCase):
    def test_original_manifest_provenance(self):
        metadata = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(metadata["schema_version"], 1)
        self.assertEqual(len(metadata["files"]), 125)
        archive_readme = next(
            f for f in metadata["files"]
            if f["source_path"] == "paper/reproducibility/README.md"
        )
        self.assertEqual(archive_readme["exported_path"], "PROVENANCE_README.md")
        self.assertEqual(
            archive_readme["sha256"],
            "1efba9d01679dc3871d2b68e2c10ab9bebbd0af251e1238fe04ed07948a4d68f",
        )

    def test_frozen_figure_inputs_present(self):
        entries = {
            item["exported_path"] for item in
            json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))["files"]
        }
        for filename in (
            "data/filter_structure/kernel_gallery.npz",
            "data/filter_structure/similarity_matrices.npz",
            "data/filter_structure/per_checkpoint.csv",
            "data/training_dynamics/learning_curves.csv",
            "data/robustness/full_budget_curves.csv",
            "code/figures/build_figures.py",
        ):
            self.assertIn(filename, entries)
            self.assertTrue((ROOT / filename).is_file())

    def test_release_metadata_and_no_generated_files(self):
        cff = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
        self.assertIn("cff-version: 1.2.0", cff)
        self.assertIn('family-names: "Espino Montelongo"', cff)
        meta = json.loads((ROOT / ".zenodo.json").read_text(encoding="utf-8"))
        self.assertEqual(meta["upload_type"], "software")
        self.assertEqual(meta["creators"][0]["name"], "Espino Montelongo, Heriberto")
        for garbage in (".DS_Store", "code/.DS_Store", "data/.DS_Store",
                        "data/additivity/.DS_Store"):
            self.assertFalse((ROOT / garbage).exists())


if __name__ == "__main__":
    unittest.main()

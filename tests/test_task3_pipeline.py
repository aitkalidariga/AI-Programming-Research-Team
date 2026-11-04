"""Regression tests for Task 3 synthetic data analysis."""

import json
import tempfile
import unittest
from pathlib import Path

import numpy as np

from src.process_data import (
    GROUPS,
    aggregate,
    bootstrap_ci,
    load_jsonl,
    validate_and_filter,
)
from src.visualize import generate_figures


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "test_run.jsonl"


class Task3PipelineTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.raw = load_jsonl(RAW)
        cls.evaluation, cls.success = validate_and_filter(cls.raw)

    def test_unique_ids_and_synthetic_data(self):
        self.assertTrue(self.raw["run_id"].is_unique)
        self.assertTrue(
            self.raw["data_type"].eq("synthetic").all()
        )

    def test_warmup_filtering(self):
        self.assertGreater(
            self.raw["phase"].eq("warmup").sum(), 0
        )
        self.assertTrue(
            self.evaluation["phase"].eq("evaluation").all()
        )

    def test_three_research_groups(self):
        self.assertEqual(
            set(self.success["group"]), set(GROUPS)
        )
        self.assertTrue(
            self.success["independent_score_pct"]
            .between(0, 100).all()
        )

    def test_statistical_aggregation(self):
        summary = aggregate(
            self.evaluation, self.success
        )
        self.assertEqual(len(summary), 3)
        self.assertEqual(
            int(summary["n_analyzed"].sum()),
            len(self.success)
        )
        self.assertTrue(
            summary["execution_error_rate_pct"]
            .between(0, 100).all()
        )

    def test_bootstrap_reproducibility(self):
        values = np.array([12, 19, 23, 26, 31])
        ci1 = bootstrap_ci(
            values, seed=42, repetitions=500
        )
        ci2 = bootstrap_ci(
            values, seed=42, repetitions=500
        )
        self.assertEqual(ci1, ci2)
        self.assertLessEqual(ci1[0], np.mean(values))
        self.assertGreaterEqual(ci1[1], np.mean(values))

    def test_invalid_json(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "invalid.jsonl"
            path.write_text(
                '{"invalid":\n', encoding="utf-8"
            )
            with self.assertRaises(ValueError):
                load_jsonl(path)

    def test_duplicate_ids(self):
        record = self.raw.iloc[0].to_dict()

        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "duplicates.jsonl"
            path.write_text(
                json.dumps(record) + "\n" +
                json.dumps(record) + "\n",
                encoding="utf-8"
            )
            with self.assertRaises(ValueError):
                load_jsonl(path)

    def test_figure_exports(self):
        with tempfile.TemporaryDirectory() as folder:
            generate_figures(
                self.success, output_dir=folder
            )

            for name in (
                "fig1_latency_vs_load",
                "fig2_distribution_boxplot"
            ):
                for extension in (".png", ".pdf"):
                    path = Path(folder) / (
                        name + extension
                    )
                    self.assertTrue(path.is_file())
                    self.assertGreater(
                        path.stat().st_size, 0
                    )


if __name__ == "__main__":
    unittest.main()

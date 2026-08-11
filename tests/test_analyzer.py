import unittest

from hienglishlab_diagnosis import analyze_evidence


class AnalyzeEvidenceTests(unittest.TestCase):
    def test_metrics_are_explainable(self):
        result = analyze_evidence({
            "sample_id": "demo-1",
            "transcript": "The ocean is important. We can protect the ocean together.",
            "expected_keywords": ["ocean", "protect", "plastic"],
        })
        self.assertEqual(result["sample_id"], "demo-1")
        self.assertEqual(result["metrics"]["keyword_coverage"], 0.667)
        self.assertEqual(result["metrics"]["matched_keywords"], ["ocean", "protect"])

    def test_rejects_missing_transcript(self):
        with self.assertRaises(ValueError):
            analyze_evidence({"expected_keywords": []})


if __name__ == "__main__":
    unittest.main()


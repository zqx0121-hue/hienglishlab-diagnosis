import json
import tempfile
import unittest
from pathlib import Path

from hienglishlab_diagnosis.cli import main


class CliTests(unittest.TestCase):
    def test_refuses_to_overwrite_output(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "sample.json"
            output = root / "report.json"
            source.write_text(json.dumps({"transcript": "A complete sample."}))
            output.write_text("keep")
            self.assertEqual(main([str(source), "--output", str(output)]), 2)
            self.assertEqual(output.read_text(), "keep")


if __name__ == "__main__":
    unittest.main()


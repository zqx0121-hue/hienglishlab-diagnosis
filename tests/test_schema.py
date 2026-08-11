import json
import unittest
from pathlib import Path


class EvidenceSchemaTests(unittest.TestCase):

    def test_schema_defines_expected_fields(self):
        schema_path = Path("schema/evidence-v1.schema.json")

        with schema_path.open("r", encoding="utf-8") as f:
            schema = json.load(f)

        self.assertEqual(schema["type"], "object")

        properties = schema["properties"]

        self.assertEqual(
            properties["sample_id"]["type"],
            "string"
        )

        self.assertEqual(
            properties["transcript"]["type"],
            "string"
        )

        self.assertEqual(
            properties["expected_keywords"]["type"],
            "array"
        )

        self.assertEqual(
            properties["expected_keywords"]["items"]["type"],
            "string"
        )

        self.assertEqual(
            schema["required"],
            ["transcript"]
        )

        self.assertFalse(
            schema["additionalProperties"]
        )

    def test_example_fixtures_have_expected_fields(self):
        valid_path = Path("examples/schema-valid.json")
        invalid_path = Path("examples/schema-invalid.json")

        with valid_path.open("r", encoding="utf-8") as f:
            valid = json.load(f)

        with invalid_path.open("r", encoding="utf-8") as f:
            invalid = json.load(f)

        self.assertEqual(
            set(valid.keys()),
            {
                "sample_id",
                "transcript",
                "expected_keywords"
            }
        )

        self.assertIn(
            "unexpected_field",
            invalid
        )

    def test_schema_rejects_unknown_fields(self):
        schema_path = Path("schema/evidence-v1.schema.json")

        with schema_path.open("r", encoding="utf-8") as f:
            schema = json.load(f)

        self.assertFalse(
            schema["additionalProperties"]
        )

        allowed_fields = set(schema["properties"])

        invalid_path = Path("examples/schema-invalid.json")

        with invalid_path.open("r", encoding="utf-8") as f:
            invalid = json.load(f)

        unknown_fields = set(invalid) - allowed_fields

        self.assertEqual(
            unknown_fields,
            {"unexpected_field"}
        )


if __name__ == "__main__":
    unittest.main()
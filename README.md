# HiEnglishLab Diagnosis Framework

A privacy-first, explainable Python CLI for turning English-learning evidence into reviewable metrics. It is designed for teachers, tutors, curriculum developers, and education-tool maintainers who need a transparent baseline before adding model-assisted analysis.

The project currently measures sample length, vocabulary variety, sentence length, and task-keyword coverage. It produces structured JSON and always reports limitations. It does not assign a standardized proficiency level, make clinical claims, upload learner data, or call external services.

## Quick start

```bash
python -m pip install -e .
hienglish-diagnose examples/sample.json
```

Input format:

```json
{
  "sample_id": "anonymous-id",
  "transcript": "A learner-produced English sample.",
  "expected_keywords": ["optional", "task", "keywords"]
}
```

To save a report, pass `--output report.json`. Existing files are never overwritten.

## Design principles

- Local by default: no analytics, network requests, or model calls.
- Explainable: output contains observable metrics and limitations.
- Privacy-aware: examples are synthetic and contributors must not submit student data.
- Reviewable: deterministic rules are covered by tests.
- Extensible: future rubrics and optional model adapters must preserve provenance and human review.

## Project status

This is an early public release. The current scope is intentionally small while the schema, safety rules, and contribution process are validated. See [ROADMAP.md](ROADMAP.md) for planned work.

## Contributing and security

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Report vulnerabilities privately as described in [SECURITY.md](SECURITY.md). By participating, you agree to the [Code of Conduct](CODE_OF_CONDUCT.md).

## License

MIT. See [LICENSE](LICENSE).


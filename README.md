# HiEnglishLab Diagnosis Framework

English | [简体中文](README.zh-CN.md) | [Español](README.es.md) | [Português (Brasil)](README.pt-BR.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Français](README.fr.md)

A privacy-first, explainable Python CLI for turning English-learning evidence into reviewable metrics. It is designed for teachers, tutors, curriculum developers, and education-tool maintainers who need a transparent baseline before adding model-assisted analysis.

The project currently measures sample length, vocabulary variety, sentence length, and task-keyword coverage. It produces structured JSON and always reports limitations. It does not assign a standardized proficiency level, make clinical claims, upload learner data, or call external services.

> **Open-core boundary:** this repository is the public evidence-processing foundation, not the complete validated diagnosis or commercial scoring system. It does not provide KET, PET, IELTS, CEFR, or equivalent scores. See [Open Core Scope](docs/OPEN_CORE_SCOPE.md).

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

Example output:

```json
{
  "metrics": {
    "word_count": 20,
    "unique_word_count": 15,
    "lexical_diversity": 0.75,
    "sentence_count": 3,
    "average_sentence_words": 6.67,
    "keyword_coverage": 1.0
  }
}
```

## Design principles

- Local by default: no analytics, network requests, or model calls.
- Explainable: output contains observable metrics and limitations.
- Privacy-aware: examples are synthetic and contributors must not submit student data.
- Reviewable: deterministic rules are covered by tests.
- Extensible: future rubrics and optional model adapters must preserve provenance and human review.

## Project status

This is an early public release. The current scope is intentionally small while the schema, safety rules, and contribution process are validated. See [ROADMAP.md](ROADMAP.md) for planned work.

See [CHANGELOG.md](CHANGELOG.md) for release history.

## Exam alignment

The current metrics are descriptive signals only. They do not cover the complete constructs required for exam assessment, such as task achievement, communicative effectiveness, coherence, grammatical accuracy, fluency, pronunciation, listening, or reading comprehension. Future public mappings must document evidence, validation, limitations, and trademark status without reproducing protected exam content.

## Contributing and security

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Report vulnerabilities privately as described in [SECURITY.md](SECURITY.md). By participating, you agree to the [Code of Conduct](CODE_OF_CONDUCT.md).

## Community

The project values technical discussion and responsible open-source sharing in communities including [LINUX DO](https://linux.do/). Community participation does not imply endorsement of the project.

## License

MIT. See [LICENSE](LICENSE).

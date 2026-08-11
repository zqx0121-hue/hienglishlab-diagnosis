# Contributing

Contributions are welcome through issues and pull requests.

1. Do not include real student names, recordings, transcripts, email addresses, credentials, or other personal data.
2. Use synthetic or irreversibly anonymized fixtures.
3. Keep analysis rules explainable and add tests for observable behavior.
4. Do not add network calls, shell execution, dynamic code loading, telemetry, or new dependencies without a documented threat-model update.
5. Run `PYTHONPATH=src python -m unittest discover -s tests -v` before submitting.

Pull requests should explain the user need, behavior change, privacy impact, security impact, and validation performed. Maintainers may request smaller changes or additional adversarial cases before merging.


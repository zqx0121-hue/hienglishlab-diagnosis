# Security policy

## Supported versions

The latest release on the default branch receives security fixes.

## Reporting a vulnerability

Please use GitHub private vulnerability reporting when available. Do not open a public issue containing learner data, credentials, exploit details, or proof-of-concept payloads. The maintainer will acknowledge a report, assess impact, coordinate a fix, and credit reporters who want attribution.

## Threat model

The CLI processes potentially untrusted JSON and learner-authored text and can write a report to the local filesystem. Relevant risks include parser denial of service, unsafe output paths or overwrites, accidental disclosure of student information, malicious test fixtures, compromised dependencies or release workflows, and hostile instructions embedded in text if a future AI adapter treats content as commands.

Current mitigations include a 1 MB input limit, regular-file checks, refusal to overwrite output, no runtime dependencies, no network access, deterministic analysis, synthetic examples, and human review of contributions.


"""Deterministic analysis rules with human-readable evidence."""

from __future__ import annotations

import re
from collections import Counter
from typing import Any

WORD_RE = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
SENTENCE_RE = re.compile(r"[^.!?]+[.!?]?")


def _words(text: str) -> list[str]:
    return [match.group(0).lower() for match in WORD_RE.finditer(text)]


def analyze_evidence(evidence: dict[str, Any]) -> dict[str, Any]:
    """Analyze one learner sample without network access or model calls.

    The result is descriptive rather than a standardized score. Every signal
    includes its source value so teachers can review it instead of trusting an
    opaque classification.
    """
    transcript = evidence.get("transcript", "")
    if not isinstance(transcript, str) or not transcript.strip():
        raise ValueError("transcript must be a non-empty string")

    expected = evidence.get("expected_keywords", [])
    if not isinstance(expected, list) or not all(isinstance(x, str) for x in expected):
        raise ValueError("expected_keywords must be a list of strings")

    tokens = _words(transcript)
    counts = Counter(tokens)
    unique_words = len(counts)
    total_words = len(tokens)
    lexical_diversity = unique_words / total_words if total_words else 0.0

    normalized_expected = [word.lower().strip() for word in expected if word.strip()]
    matched = [word for word in normalized_expected if word in counts]
    coverage = len(matched) / len(normalized_expected) if normalized_expected else None

    sentences = [s.strip() for s in SENTENCE_RE.findall(transcript) if s.strip()]
    avg_sentence_words = total_words / len(sentences) if sentences else float(total_words)

    observations: list[str] = []
    if total_words < 30:
        observations.append("The sample is short; treat all signals as preliminary.")
    if lexical_diversity >= 0.65:
        observations.append("The sample uses a relatively varied vocabulary for its length.")
    elif total_words >= 20 and lexical_diversity < 0.45:
        observations.append("Repeated vocabulary may be a useful target for guided revision.")
    if coverage is not None:
        observations.append(
            f"The sample includes {len(matched)} of {len(normalized_expected)} expected keywords."
        )

    return {
        "schema_version": "1.0",
        "sample_id": evidence.get("sample_id"),
        "metrics": {
            "word_count": total_words,
            "unique_word_count": unique_words,
            "lexical_diversity": round(lexical_diversity, 3),
            "sentence_count": len(sentences),
            "average_sentence_words": round(avg_sentence_words, 2),
            "keyword_coverage": round(coverage, 3) if coverage is not None else None,
            "matched_keywords": matched,
        },
        "observations": observations,
        "limitations": [
            "This output is not a standardized proficiency score or clinical diagnosis.",
            "A teacher should interpret the metrics alongside the task and learner context.",
        ],
    }


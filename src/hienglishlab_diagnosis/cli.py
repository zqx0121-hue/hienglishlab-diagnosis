"""Command-line interface."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .analyzer import analyze_evidence

MAX_INPUT_BYTES = 1_000_000


def _read_json(path: Path) -> dict:
    if not path.is_file():
        raise ValueError(f"input is not a regular file: {path}")
    if path.stat().st_size > MAX_INPUT_BYTES:
        raise ValueError("input exceeds the 1 MB safety limit")
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("input JSON must contain an object")
    return value


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="hienglish-diagnose",
        description="Generate an explainable report from English-learning evidence.",
    )
    parser.add_argument("input", type=Path, help="path to a UTF-8 JSON evidence file")
    parser.add_argument("--output", type=Path, help="write JSON to this new file")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        report = analyze_evidence(_read_json(args.input))
        rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
        if args.output:
            if args.output.exists():
                raise ValueError("output already exists; refusing to overwrite it")
            args.output.write_text(rendered, encoding="utf-8")
        else:
            sys.stdout.write(rendered)
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())


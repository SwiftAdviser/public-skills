#!/usr/bin/env python3
"""Attempt manager for isolated content improvement loops.

This script does not call an LLM. It creates the attempt workspace, evaluates
the current candidate with deterministic gates, and writes retry artifacts that
writer/evaluator subagents can consume.
"""

from __future__ import annotations

import argparse
import json
import shutil
import time
from pathlib import Path

import quality_gate
import slop_score


def ensure_workdir(base: str | None) -> Path:
    if base:
        workdir = Path(base)
    else:
        workdir = Path(".tmp") / "high-quality-content-writer" / time.strftime("%Y%m%d-%H%M%S")
    workdir.mkdir(parents=True, exist_ok=True)
    return workdir


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Manage one content quality loop attempt.")
    parser.add_argument("--source", required=True, help="Source markdown/text file.")
    parser.add_argument("--brief", default="", help="User brief or goal.")
    parser.add_argument("--workdir", help="Loop workdir. Defaults to .tmp/high-quality-content-writer/<timestamp>.")
    parser.add_argument("--attempt", type=int, default=0)
    parser.add_argument("--candidate", help="Candidate file. Defaults to <workdir>/candidate.md.")
    parser.add_argument("--type", choices=["auto", "quote", "article"], default="auto")
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()

    source_path = Path(args.source)
    if not source_path.exists():
        raise SystemExit(f"source file not found: {source_path}")

    workdir = ensure_workdir(args.workdir)
    source_copy = workdir / "source.md"
    if source_copy.resolve() != source_path.resolve():
        shutil.copyfile(source_path, source_copy)
    if args.brief:
        (workdir / "brief.md").write_text(args.brief, encoding="utf-8")

    candidate_path = Path(args.candidate) if args.candidate else workdir / "candidate.md"
    if not candidate_path.exists():
        shutil.copyfile(source_copy, candidate_path)

    text = candidate_path.read_text(encoding="utf-8")
    gate = quality_gate.evaluate(text, content_type=args.type, title=str(candidate_path))
    trope = slop_score.local_score(text, title=str(candidate_path))

    attempt_dir = workdir / f"attempt-{args.attempt}"
    attempt_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(candidate_path, attempt_dir / "candidate.md")
    write_json(attempt_dir / "quality_gate.json", gate)
    write_json(attempt_dir / "slop_score.json", trope)

    fix_text = gate.get("fix_instructions") or "Passed. No retry required."
    (attempt_dir / "fix-instructions.md").write_text(str(fix_text), encoding="utf-8")
    latest = {
        "workdir": str(workdir),
        "attempt": args.attempt,
        "candidate": str(candidate_path),
        "passed": gate["passed"],
        "score": gate["score"],
        "threshold": gate["threshold"],
        "reason": gate["reason"],
        "fix_instructions": gate.get("fix_instructions", ""),
        "quality_gate_path": str(attempt_dir / "quality_gate.json"),
        "slop_score_path": str(attempt_dir / "slop_score.json"),
    }
    write_json(workdir / "latest-eval.json", latest)

    print(json.dumps(latest, ensure_ascii=False, indent=2 if args.pretty else None))
    return 0 if gate["passed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())

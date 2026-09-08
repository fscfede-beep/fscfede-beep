#!/usr/bin/env python3
"""Rumbo Runtime Gate.

Enforces an observed-duration contract for long-running executions:
PASS requires:
  1. the wrapped command exits successfully;
  2. monotonic elapsed time >= the requested minimum.

Wall-clock timestamps are recorded for auditability, but monotonic time is
authoritative because it is not affected by system-clock adjustments.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from dataclasses import dataclass, asdict
from datetime import datetime, timezone


@dataclass(frozen=True)
class RuntimeReceipt:
    protocol: str
    requested_seconds: float
    observed_seconds: float
    command_returncode: int
    started_at_utc: str
    finished_at_utc: str
    duration_pass: bool
    command_pass: bool
    overall_pass: bool

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2, sort_keys=True)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def run(command: list[str], minimum_seconds: float) -> RuntimeReceipt:
    started_at = utc_now()
    start = time.monotonic()
    completed = subprocess.run(command, check=False)
    observed = time.monotonic() - start
    finished_at = utc_now()

    duration_pass = observed >= minimum_seconds
    command_pass = completed.returncode == 0
    return RuntimeReceipt(
        protocol="Rumbo Runtime Discipline",
        requested_seconds=minimum_seconds,
        observed_seconds=observed,
        command_returncode=completed.returncode,
        started_at_utc=started_at,
        finished_at_utc=finished_at,
        duration_pass=duration_pass,
        command_pass=command_pass,
        overall_pass=duration_pass and command_pass,
    )


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Run a command and emit an auditable Rumbo duration receipt."
    )
    parser.add_argument(
        "--minimum-seconds",
        type=float,
        default=300.0,
        help="minimum observed duration required for PASS (default: 300 seconds)",
    )
    parser.add_argument(
        "--receipt",
        type=str,
        help="optional path for the JSON receipt",
    )
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args(argv)

    if args.minimum_seconds < 0:
        parser.error("--minimum-seconds must be non-negative")
    if not args.command:
        parser.error("provide a command after --")

    receipt = run(args.command, args.minimum_seconds)
    payload = receipt.to_json()
    print(payload)

    if args.receipt:
        with open(args.receipt, "w", encoding="utf-8") as handle:
            handle.write(payload + "\n")

    return 0 if receipt.overall_pass else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

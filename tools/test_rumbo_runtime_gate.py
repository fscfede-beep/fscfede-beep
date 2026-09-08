#!/usr/bin/env python3
"""Self-test for Rumbo Runtime Discipline."""
from __future__ import annotations

from tools.rumbo_runtime_gate import RuntimeReceipt

def main() -> None:
    short = RuntimeReceipt(
        protocol="Rumbo Runtime Discipline",
        requested_seconds=300,
        observed_seconds=46,
        command_returncode=0,
        started_at_utc="2026-09-08T11:00:00+00:00",
        finished_at_utc="2026-09-08T11:00:46+00:00",
        duration_pass=False,
        command_pass=True,
        overall_pass=False,
    )
    assert short.overall_pass is False
    assert '"duration_pass": false' in short.to_json()

    good = RuntimeReceipt(
        protocol="Rumbo Runtime Discipline",
        requested_seconds=300,
        observed_seconds=300.1,
        command_returncode=0,
        started_at_utc="2026-09-08T11:00:00+00:00",
        finished_at_utc="2026-09-08T11:05:00.100000+00:00",
        duration_pass=True,
        command_pass=True,
        overall_pass=True,
    )
    assert good.overall_pass is True

if __name__ == "__main__":
    main()
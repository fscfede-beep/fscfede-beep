#!/usr/bin/env python3
"""Rumbo Runtime Lease: persistent, auditable five-minute execution sessions."""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
import uuid
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

PROTOCOL = "Rumbo Runtime Lease"

@dataclass(frozen=True)
class RuntimeLease:
    protocol: str
    lease_id: str
    requested_seconds: float
    started_at_utc: str
    start_monotonic_ns: int
    start_pid: int
    start_host: str
    start_boot_id: str | None = None
    finished_at_utc: str | None = None
    end_monotonic_ns: int | None = None
    end_pid: int | None = None
    end_host: str | None = None
    end_boot_id: str | None = None
    command_returncode: int | None = None
    duration_pass: bool = False
    command_pass: bool = False
    overall_pass: bool = False
    status: str = "running"
    note: str | None = None

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2, sort_keys=True)

def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()

def boot_id() -> str | None:
    try:
        return Path("/proc/sys/kernel/random/boot_id").read_text(encoding="utf-8").strip()
    except (FileNotFoundError, OSError):
        return None

def host() -> str:
    return os.uname().nodename if hasattr(os, "uname") else os.environ.get("COMPUTERNAME", "unknown")

def save(path: Path, lease: RuntimeLease) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(lease.to_json() + "\n", encoding="utf-8")
    os.replace(tmp, path)

def load(path: Path) -> RuntimeLease:
    return RuntimeLease(**json.loads(path.read_text(encoding="utf-8")))

def start(path: Path, requested_seconds: float) -> RuntimeLease:
    if path.exists():
        raise SystemExit(f"lease already exists: {path}")
    lease = RuntimeLease(
        protocol=PROTOCOL, lease_id=uuid.uuid4().hex, requested_seconds=requested_seconds,
        started_at_utc=utc_now(), start_monotonic_ns=time.monotonic_ns(),
        start_pid=os.getpid(), start_host=host(), start_boot_id=boot_id(),
    )
    save(path, lease)
    print(lease.to_json())
    return lease

def checkpoint(path: Path) -> RuntimeLease:
    lease = load(path)
    if lease.status != "running":
        raise SystemExit(f"lease is not running: {lease.status}")
    if lease.start_host != host() or lease.start_boot_id != boot_id():
        raise SystemExit("lease host/boot identity mismatch; refusing to claim continuous runtime")
    observed = (time.monotonic_ns() - lease.start_monotonic_ns) / 1_000_000_000
    print(json.dumps({"protocol": PROTOCOL, "lease_id": lease.lease_id, "observed_seconds": observed, "duration_pass": observed >= lease.requested_seconds, "status": lease.status}, indent=2, sort_keys=True))
    return lease

def finish(path: Path, returncode: int) -> RuntimeLease:
    lease = load(path)
    if lease.status != "running":
        raise SystemExit(f"lease is not running: {lease.status}")
    current_host = host()
    current_boot_id = boot_id()
    if lease.start_host != current_host or lease.start_boot_id != current_boot_id:
        raise SystemExit("lease host/boot identity mismatch; refusing to claim continuous runtime")
    end_ns = time.monotonic_ns()
    observed = (end_ns - lease.start_monotonic_ns) / 1_000_000_000
    duration_pass = observed >= lease.requested_seconds
    command_pass = returncode == 0
    result = RuntimeLease(
        **{**asdict(lease), "finished_at_utc": utc_now(), "end_monotonic_ns": end_ns,
           "end_pid": os.getpid(), "end_host": current_host, "end_boot_id": current_boot_id, "command_returncode": returncode,
           "duration_pass": duration_pass, "command_pass": command_pass,
           "overall_pass": duration_pass and command_pass,
           "status": "completed" if command_pass else "failed",
           "note": None if duration_pass else "observed runtime below requested threshold"}
    )
    save(path, result)
    print(result.to_json())
    return result

def execute(path: Path, command: list[str], requested_seconds: float = 300.0) -> int:
    start(path, requested_seconds)
    try:
        rc = subprocess.run(command, check=False).returncode
    except BaseException:
        finish(path, 1)
        raise
    result = finish(path, rc)
    return 0 if result.overall_pass else 1

def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="op", required=True)
    p_start = sub.add_parser("start"); p_start.add_argument("--lease", required=True); p_start.add_argument("--minimum-seconds", type=float, default=300.0)
    p_checkpoint = sub.add_parser("checkpoint"); p_checkpoint.add_argument("--lease", required=True)
    p_finish = sub.add_parser("finish"); p_finish.add_argument("--lease", required=True); p_finish.add_argument("--returncode", type=int, required=True)
    p_exec = sub.add_parser("exec"); p_exec.add_argument("--lease", required=True); p_exec.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args(argv)
    path = Path(args.lease)
    if args.op == "start": start(path, args.minimum_seconds); return 0
    if args.op == "checkpoint": checkpoint(path); return 0
    if args.op == "finish": result = finish(path, args.returncode); return 0 if result.overall_pass else 1
    if not args.command or args.command == ["--"]: parser.error("provide a command after --")
    return execute(path, args.command, 300.0)

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
# Rumbo Runtime Discipline

A long-running Rumbo execution is PASS only when:

1. the wrapped work succeeds; and
2. observed monotonic runtime is at least the requested threshold.

The default threshold is 300 seconds (5 minutes).

The gate uses time.monotonic() as the authoritative duration source and records UTC wall-clock timestamps only as audit context.

Example:

  python tools/rumbo_runtime_gate.py --receipt runtime-receipt.json -- python your_task.py

A command that finishes in 46 seconds receives a non-zero gate result and a receipt with duration_pass=false.

A command that succeeds after at least 300 observed seconds receives overall_pass=true.

This protocol does not force an external platform to keep an agent alive for five minutes. It makes the five-minute claim verifiable and enforceable wherever the wrapped execution is under our control.
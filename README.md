# Sebastián

**AI Systems & Agent Reliability Engineer · Founder, RUMBO IA**

I work on failure boundaries in agentic systems: async resource ownership, cancellation safety, fail-closed execution, tool/permission routing, deterministic evaluation, canonical-state recovery, and verifiable effects.

## 30-second technical summary

My recurring engineering pattern is:

1. separate facts that a system is currently conflating;
2. define the invariant that must survive failure;
3. build the smallest deterministic reproduction;
4. narrow the claim to what the evidence actually proves;
5. propose or implement a bounded fix;
6. verify the resulting effect instead of treating intent as success.

`INTENT → AUTHORITY → PREFLIGHT → EXECUTION → READBACK → FALSIFICATION → CLOSURE`

## Start here

### [Verifiable Agent Control Plane](https://github.com/fscfede-beep/verifiable-agent-control-plane)

Dependency-free Python reference for fail-closed agent execution, exact-state binding, deterministic revalidation, effect readback, replay prevention, and hash-bound receipts.

- 14/14 deterministic tests PASS locally.
- GitHub Actions validates Python 3.11 / 3.12 / 3.13.
- Sanitized reference implementation; no private production state or credentials.
## Engineering case studies

- **[Async Resource Ownership Under Cancellation](case-studies/async-resource-ownership.md)**
  - Registry ownership transfer, cancellation-settled teardown, exception precedence, attempt-all cleanup.
  - Grounded in OpenAI Agents SDK issues #4747/#4749 and reviews of PRs #4750/#4751.

- **[Fail-Closed CI Gates](case-studies/fail-closed-ci-gates.md)**
  - Required-job scheduler semantics, dependency failure propagation, pre-checkout guards, reviewer self-correction.
  - Grounded in review of OpenAI Python PR #3780.

- **[Tool Output Policy Boundaries](case-studies/tool-output-policy-boundaries.md)**
  - Caller-requested budgets vs model truncation policy and context-safety boundaries.
  - Grounded in current-main analysis on Codex issue #42367 plus a public fork reference patch.

## Selected public engineering evidence

### OpenAI Agents SDK

- Authored [#4747 — PTY teardown can be abandoned after registry removal](https://github.com/openai/openai-agents-python/issues/4747).
- Authored [#4749 — PTY startup cancellation can leak unregistered resources](https://github.com/openai/openai-agents-python/issues/4749).
- Reviewed [PR #4750](https://github.com/openai/openai-agents-python/pull/4750) and [PR #4751](https://github.com/openai/openai-agents-python/pull/4751) around cleanup ownership, cancellation propagation, and backend-level regressions.

### OpenAI Python SDK

- Reviewed [PR #3780](https://github.com/openai/openai-python/pull/3780) around fail-closed dependency-gate ordering, `!cancelled()` semantics, and non-success dependency states.
- Publicly corrected a stale review blocker after re-reading the exact head revision.
### OpenAI Codex

- On [issue #42367](https://github.com/openai/codex/issues/42367), authored by another contributor, I revalidated the code-mode truncation boundary against newer `main` and published a concrete reference implementation.
- Reference commit: [`fscfede-beep/codex@9e70016`](https://github.com/fscfede-beep/codex/commit/9e700160e7c77deb373610b58d05d5d54e060d82).
- Validation explicitly stopped short of claiming Rust compile/test PASS because that host lacked `cargo` / `rustc`.

## Reliability thesis

An agent is not reliable merely because it selected the right action. Reliability requires authority, execution, observed effect, and evidence to remain consistent across failures.

Current technical interests:

- agent harnesses and long-running execution;
- async resource ownership and cancellation safety;
- MCP, plugins, connectors, and developer platforms;
- permission and policy boundaries;
- deterministic evals and regression testing;
- canonical-state recovery and effect verification.

## Product work

- **RUMBO IA** — human-controlled AI CRM and automation for small businesses in Latin America: https://rumbo.verso.fans
- Technical portfolio: https://sebastian-ai-workflow-reliability.miniup.app

## Evidence boundary

Authored issues, reviews, reference implementations, upstream code authorship, merge state, endorsement, employment, and production status are deliberately described as different facts.

I am open to engineering roles and technical collaboration in agent reliability, developer tooling, applied AI, and agent infrastructure.

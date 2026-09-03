# Sebastián

**AI Systems & Agent Reliability Engineer · Founder, RUMBO IA**

I build agentic systems where **intent, authority, execution, observed effect, and promotion are separate, testable states**.

`INTENT → AUTHORITY → PREFLIGHT → EXECUTION → READBACK → FALSIFICATION → CLOSURE`

My focus is failure-boundary engineering: async resource ownership, cancellation safety, fail-closed execution, tool and permission routing, deterministic evaluation, canonical-state recovery, and verifiable effects.

## Start here — original engineering work

### [Verifiable Agent Control Plane](https://github.com/fscfede-beep/verifiable-agent-control-plane)

A dependency-free Python reference implementation for fail-closed agent execution with exact-state binding, deterministic revalidation, effect readback, replay prevention, and hash-bound receipts.

The test suite covers stale-state rejection, duplicate intent rejection, action allowlisting, secret-like payload rejection, readback mismatch, receipt-chain verification, tamper detection, and replay prevention.

**Boundary:** sanitized reference implementation; no private production state, credentials, provider IDs, or deployment configuration.

## Public engineering evidence

> Independent public engineering activity. These links do not imply OpenAI employment, affiliation, endorsement, or upstream code authorship.

### OpenAI Agents SDK

- Authored [#4747 — PTY teardown can be abandoned after registry removal](https://github.com/openai/openai-agents-python/issues/4747), focused on cancellation-safe resource ownership after registry removal.
- Authored [#4749 — PTY startup cancellation can leak unregistered resources](https://github.com/openai/openai-agents-python/issues/4749), focused on the pre-registration ownership boundary.
- Reviewed [PR #4750](https://github.com/openai/openai-agents-python/pull/4750) and [PR #4751](https://github.com/openai/openai-agents-python/pull/4751) around cleanup ownership, cancellation propagation, and regression coverage.

### OpenAI Python SDK

- Reviewed [PR #3780](https://github.com/openai/openai-python/pull/3780) around fail-closed CI dependency-gate ordering, scheduler semantics, and non-success dependency states.
- Publicly corrected a stale review blocker after re-reading the exact head revision.

### OpenAI Codex

- Revalidated the code-mode tool-output boundary reported in [issue #42367](https://github.com/openai/codex/issues/42367), authored by another contributor.
- Published a concrete reference implementation in my fork: [`fscfede-beep/codex@9e70016`](https://github.com/fscfede-beep/codex/commit/9e700160e7c77deb373610b58d05d5d54e060d82).
- I do **not** claim upstream merge, endorsement, or Rust compile/test PASS for that reference commit.

## Engineering case studies

- **[Async Resource Ownership Under Cancellation](case-studies/async-resource-ownership.md)** — ownership transfer, cancellation-settled teardown, exception precedence, attempt-all cleanup.
- **[Fail-Closed CI Gates](case-studies/fail-closed-ci-gates.md)** — required-job scheduler semantics, dependency failure propagation, pre-checkout guards, reviewer self-correction.
- **[Tool Output Policy Boundaries](case-studies/tool-output-policy-boundaries.md)** — caller-requested budgets, model truncation policy, and context-safety boundaries.

## Current technical focus

- agent harnesses and long-running execution;
- async lifecycle and cancellation safety;
- MCP, plugins, connectors, and tool routing;
- permission and policy boundaries;
- deterministic evals and regression testing;
- canonical-state recovery and effect verification;
- verifiable control planes for consequential agent actions.

## Product work

- **[RUMBO IA](https://rumbo.verso.fans)** — human-controlled AI CRM and automation for small businesses in Latin America.
- **[Technical portfolio](https://sebastian-ai-workflow-reliability.miniup.app)** — selected work in AI workflow and agent reliability.

## Reliability thesis

An agent is not reliable merely because it selected the right action. Reliability requires the authorized action, the executed action, the observed effect, and the evidence about that effect to remain consistent across failures.

## Evidence boundary

I deliberately distinguish authored issues, reviews, reference implementations, upstream code authorship, merge state, endorsement, employment, and production status.

I am open to engineering roles and technical collaboration in **agent reliability, developer tooling, applied AI, and agent infrastructure**.

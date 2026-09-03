# Sebastián

**AI Systems & Agent Reliability Engineer · Founder, RUMBO IA**

I investigate and build reliable AI agent systems: safe tool execution, async lifecycle correctness, resource ownership, permissions, MCP/plugins, deterministic evaluation, canonical-state recovery, and verifiable effects.

My public engineering work focuses on failure boundaries that are easy to miss in agentic systems: cancellation during ownership transfer, fail-closed execution, retry semantics, state reconciliation, and evidence that distinguishes intention from actual effect.

## Selected public engineering work

- **OpenAI Codex — root-cause analysis + public reference implementation**
  - [#42367 — code-mode output can exceed the model truncation policy](https://github.com/openai/codex/issues/42367)
  - Reference implementation: [`fscfede-beep/codex@9e70016`](https://github.com/fscfede-beep/codex/commit/9e700160e7c77deb373610b58d05d5d54e060d82)
  - One-file change, 3/3 production result paths migrated, `git diff --check` PASS.
  - Codex does not accept external PRs; the fork commit is a maintainer reference, not an upstream merge claim.

- **OpenAI Agents SDK — authored lifecycle/cancellation issues**
  - [#4747 — PTY teardown can be abandoned after registry removal](https://github.com/openai/openai-agents-python/issues/4747)
  - [#4749 — PTY startup cancellation can leak unregistered resources](https://github.com/openai/openai-agents-python/issues/4749)

- **Implementation review**
  - [Agents SDK PR #4750](https://github.com/openai/openai-agents-python/pull/4750) — reproduced a cancellation/cleanup-failure precedence case; the PR author subsequently incorporated a fix and regression.
  - [Agents SDK PR #4751](https://github.com/openai/openai-agents-python/pull/4751) — requested backend-level regression coverage at the registry ownership boundary; the PR author subsequently added that coverage.

- **OpenAI Python SDK**
  - [PR #3780](https://github.com/openai/openai-python/pull/3780) — reviewed fail-closed dependency-gate ordering and cancellation semantics; recommendations were subsequently applied by the PR author.

## Reliability thesis

An agent is not reliable merely because it selected the right action. Reliability requires authority, execution, observed effect, and evidence to remain consistent across failures.

`INTENT → AUTHORITY → PREFLIGHT → EXECUTION → READBACK → FALSIFICATION → CLOSURE`

Current technical interests:

- agent harnesses and long-running execution
- async resource ownership and cancellation safety
- MCP, plugins, connectors, and developer platforms
- permission and policy boundaries
- deterministic evals and regression testing
- canonical-state recovery and effect verification

## Engineering case studies

- **Owning Cleanup in Async Agent Runtimes**
- **Fail-Closed CI Gates in Developer Infrastructure**

Technical portfolio: https://sebastian-ai-workflow-reliability.miniup.app

RUMBO IA: https://rumbo.verso.fans

## Evidence boundary

Public issue research, review work, and reference implementations are described separately from authored upstream code, merge status, maintainer endorsement, or employment.

I am open to engineering roles and technical collaboration in agent reliability, developer tooling, applied AI, and agent infrastructure.

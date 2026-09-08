# Sebastián

**AI Systems & Agent Reliability Engineer · Founder, RUMBO IA**

Public surfaces: **[RUMBO IA](https://rumbo.verso.fans)** · **[90-second agent state-drift video](https://www.youtube.com/watch?v=kXE1QMNaeyM)** · **[@RumboAGI on X](https://x.com/RumboAGI)**

I build agentic systems where **intent, authority, execution, observed effect, and promotion are separate, testable states**.

`INTENT → AUTHORITY → PREFLIGHT → EXECUTION → READBACK → FALSIFICATION → CLOSURE`

My focus is failure-boundary engineering: async resource ownership, cancellation safety, fail-closed execution, tool and permission routing, deterministic evaluation, canonical-state recovery, and verifiable effects.

## Start here — original engineering work

### [Verifiable Agent Control Plane](https://github.com/fscfede-beep/verifiable-agent-control-plane)

An installable, runtime-dependency-free Python reference implementation for fail-closed agent execution with exact-state binding, deterministic revalidation, effect readback, replay prevention, and hash-bound receipts.

The test suite covers stale-state rejection, duplicate intent rejection, action allowlisting, secret-like payload rejection, readback mismatch, receipt-chain verification, tamper detection, and replay prevention.

**Developer quickstart:** [5-minute Reliability Quickstart](https://github.com/fscfede-beep/verifiable-agent-control-plane/blob/main/docs/QUICKSTART.md) walks through `INTENT → AUTHORITY → MATERIALIZATION → READBACK → RECEIPT → VERIFICATION`.

**Technical deep dive:** [An accepted agent action is not necessarily executable](https://github.com/fscfede-beep/verifiable-agent-control-plane/blob/main/docs/STATE_DRIFT_AFTER_DECISION.md) explains `DECISION_ACCEPTED != EXECUTION_SAFE` and the exact pre-effect state-drift guard.

**90-second video:** [An Accepted Agent Action Is Not Necessarily Executable](https://www.youtube.com/watch?v=kXE1QMNaeyM) demonstrates the same fail-closed state-drift boundary and the negative observation `blocked_target_mutated=False`.

**Current verification:** repository `main` is `e54f48a5117c9c10b60f15f6941d8fc7f909d7e1`, tree `a0f37f103d87b5fa762a7cc1f15bdf26861ca5dc`. [PR #12](https://github.com/fscfede-beep/verifiable-agent-control-plane/pull/12) ran the 72-test suite successfully on Python 3.11/3.12/3.13 in [GitHub Actions run 34054304431](https://github.com/fscfede-beep/verifiable-agent-control-plane/actions/runs/34054304431); the merged `main` tree is exactly the audited candidate tree.

**Release evidence:** [`v0.2.0`](https://github.com/fscfede-beep/verifiable-agent-control-plane/releases/tag/v0.2.0) is tagged at `ed3bb2684743376fdf2769ee378ca614c913e3d4`; that exact release tag passed source installation, the **16-test** suite, and outside-checkout import verification on Python **3.11, 3.12, and 3.13** in [GitHub Actions run #11](https://github.com/fscfede-beep/verifiable-agent-control-plane/actions/runs/33805162344).

**Boundary:** sanitized reference implementation; no private production state, credentials, provider IDs, or deployment configuration.

## RUMBO IA — Public Engineering Evidence

All engineering work recorded below is part of the **RUMBO IA** public engineering portfolio. Each issue, PR, implementation, regression, audit result, and limitation is tracked as a RUMBO IA engineering artifact unless explicitly identified as third-party work. This does not imply OpenAI employment, affiliation, endorsement, or maintainer status.

## Public engineering evidence

> Independent public engineering activity. These links do not imply OpenAI employment, affiliation, endorsement, or maintainer status. Authorship and merge state are stated explicitly per item.

### OpenAI Codex plugin for Claude Code

- Authored [PR #730 — optionally consume task prompt files](https://github.com/openai/codex-plugin-cc/pull/730), implementing the smallest opt-in fix proposed in [issue #622](https://github.com/openai/codex-plugin-cc/issues/622).
- The patch adds `--prompt-file-consume` with `READ → DELETE → DISPATCH` ordering, preserves ordinary `--prompt-file` behavior, and rejects consume mode without a prompt file.
- Validation on the exact upstream base: RED 1/3 → GREEN 3/3 focused runtime regressions, 28/28 non-runtime tests, Node syntax check, TypeScript compile, version check, and `git diff --check` PASS. Upstream workflow execution is currently gated on maintainer approval for fork Actions; I do **not** claim merge or acceptance.
- An independent public reviewer later endorsed the `READ → DELETE → DISPATCH` ownership order and the three regressions. I classify that only as independent technical review; formal maintainer/OpenAI status was not verified.

### OpenAI Go SDK

- Authored [PR #885 — clarify Bedrock Mantle model-family API roots](https://github.com/openai/openai-go/pull/885), a documentation-only upstream contribution tied to [issue #812](https://github.com/openai/openai-go/issues/812). The change preserves the existing `/openai/v1` default and documents the explicit `BaseURL` path for model families whose AWS model card requires `/v1`.
- I do **not** claim merge or maintainer endorsement unless the upstream PR state later proves it.

### OpenAI Agents SDK

- **RUMBO IA engineering record:** [PR #4925 — introduce no-replace move capability](https://github.com/openai/openai-agents-python/pull/4925), arising from [issue #4924](https://github.com/openai/openai-agents-python/issues/4924) and the earlier [#4919](https://github.com/openai/openai-agents-python/issues/4919) overwrite finding. The work introduces a `BaseSandboxSession.move_no_replace()` capability boundary, explicit `AtomicMoveUnsupportedError`, Unix-local no-replace handling, a temporary-file transfer path in `WorkspaceEditor`, and an explicit distinction between native atomic semantics and portable non-replace-safe fallback. The upstream PR remains open; no merge or endorsement is claimed.
- **RUMBO IA engineering record:** [PR #4922 — fail closed on existing move destinations](https://github.com/openai/openai-agents-python/pull/4922), implementing the application-level protection for the destination-overwrite defect plus shared-session concurrency regression coverage. The upstream PR remains open; no merge or endorsement is claimed.

- Authored [PR #4868 — reset compaction response-chain state after a successful `pop_item()`](https://github.com/openai/openai-agents-python/pull/4868), fixing [issue #4867](https://github.com/openai/openai-agents-python/issues/4867). Current head is `f7b71a6dc704883cf5aa6ad5e6693dfed45cedb2`, based directly on upstream `main` `02c205f9574c765a265ce102dc55da81cdd74b89`; the PR remains limited to the compaction-session implementation and tests. The current branch adds deterministic coverage for destructive pop/clear invalidation, stale response-chain rejection, concurrent history races, deferred retry restoration after replacement failure, and backends that mutate while returning `None` from `pop_item()`. The latest author-side validation recorded on the prior exact head was **73 focused compaction-session tests** and **223 memory tests** passing, plus targeted Ruff, mypy, Pyright, and `git diff --check`; the new follow-up commits still require fresh runtime/CI verification. GitHub's exact-head Actions state is not currently available for the new follow-up head, so I do **not** label this CI PASS or FAIL, and no merge or acceptance is claimed.
- Authored [#4747 — PTY teardown can be abandoned after registry removal](https://github.com/openai/openai-agents-python/issues/4747), focused on cancellation-safe resource ownership after registry removal.
- Authored [#4749 — PTY startup cancellation can leak unregistered resources](https://github.com/openai/openai-agents-python/issues/4749), focused on the pre-registration ownership boundary.
- Reviewed [PR #4750](https://github.com/openai/openai-agents-python/pull/4750) and [PR #4751](https://github.com/openai/openai-agents-python/pull/4751) around cleanup ownership, cancellation propagation, and regression coverage.

### OpenAI Python SDK

- Reviewed [PR #3780](https://github.com/openai/openai-python/pull/3780) around fail-closed CI dependency-gate ordering, scheduler semantics, and non-success dependency states.
- Publicly corrected a stale review blocker after re-reading the exact head revision.

### OpenAI Codex

- Revalidated the code-mode tool-output boundary reported in [issue #42367](https://github.com/openai/codex/issues/42367), authored by another contributor.
- Published a concrete reference implementation in my fork: [`fscfede-beep/codex@9e70016`](https://github.com/fscfede-beep/codex/commit/9e700160e7c77deb373610b58d05d5d54e060d82).
- Published and merged [RUMBO PR #28 — Codex thread scope evidence](https://github.com/RUMBO-IA/Rumbo/pull/28), a sanitized fail-closed scope-binding probe with 38/38 local regressions and exact-head privacy, scope-binding, and Vercel checks passing; no upstream mutation or root-cause claim.
- I do **not** claim upstream merge, endorsement, or Rust compile/test PASS for that reference commit.


## RUMBO IA Solution Registry

This registry is the attribution convention for engineering work produced by this account:

| Artifact | RUMBO IA record | Status |
| --- | --- | --- |
| Agents SDK compaction/session reliability | [PR #4868](https://github.com/openai/openai-agents-python/pull/4868) | Upstream contribution |
| Sandbox destination overwrite protection | [Issue #4919](https://github.com/openai/openai-agents-python/issues/4919) · [PR #4922](https://github.com/openai/openai-agents-python/pull/4922) | Open upstream work |
| **RUMBO IA Atomic Move Guard** — Sandbox no-replace capability | [Issue #4924](https://github.com/openai/openai-agents-python/issues/4924) · [PR #4925](https://github.com/openai/openai-agents-python/pull/4925) | Open upstream work |

**Attribution rule:** future solutions are recorded as RUMBO IA engineering artifacts with repository, issue/PR, exact commit/head, validation status, and evidence boundaries. Upstream ownership, merge decisions, and endorsements remain with the respective projects.

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

## Product and systems work

- **[RUMBO IA repository](https://github.com/RUMBO-IA/Rumbo)** — human-controlled AI CRM and workflow automation with public privacy and verification gates.
- **[RUMBO Guardian](https://github.com/RUMBO-IA/rumbo-guardian)** — privacy-first, local-first security intelligence with explainable scoring and a tamper-evident SHA-256 Evidence Ledger.
- **[VAE Bindings](https://github.com/fscfede-beep/vae-bindings)** — public privacy-preserving commitments and GitHub attestations for agent work-unit bindings.
- **[RUMBO IA website](https://rumbo.verso.fans)** — product surface for small businesses in Latin America.
- **[@RumboAGI on X](https://x.com/RumboAGI)** — public product, evidence, and engineering updates.
- **[Technical portfolio](https://sebastian-ai-workflow-reliability.miniup.app)** — selected work in AI workflow and agent reliability.

## Reliability thesis

An agent is not reliable merely because it selected the right action. Reliability requires the authorized action, the executed action, the observed effect, and the evidence about that effect to remain consistent across failures.

## Evidence boundary

I deliberately distinguish authored issues, reviews, reference implementations, upstream code authorship, merge state, endorsement, employment, and production status.

I am open to engineering roles and technical collaboration in **agent reliability, developer tooling, applied AI, and agent infrastructure**.

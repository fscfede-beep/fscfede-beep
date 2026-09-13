# Sebastián

**AI Systems & Agent Reliability | Business × Technology × Operations · Founder, RUMBO IA**

Public surfaces: **[RUMBO IA](https://rumbo.verso.fans)** · **[90-second agent state-drift demo](https://www.youtube.com/watch?v=kXE1QMNaeyM)** · **[@RumboAGI on X](https://x.com/RumboAGI)**

I build agentic systems where **intent, authority, execution, observed effect, and promotion are separate, testable states**.

`INTENT → AUTHORITY → PREFLIGHT → EXECUTION → READBACK → FALSIFICATION → CLOSURE`

My focus is agent harnesses, sandboxing and isolation, async resource ownership, cancellation safety, fail-closed execution, deterministic evals, canonical-state recovery, tool/permission routing, and verifiable effects.

## Original engineering work

### [Verifiable Agent Control Plane](https://github.com/fscfede-beep/verifiable-agent-control-plane)

A public Python reference implementation for fail-closed agent execution with exact-state binding, deterministic revalidation, effect readback, replay prevention, and hash-bound receipts.

- [5-minute Reliability Quickstart](https://github.com/fscfede-beep/verifiable-agent-control-plane/blob/main/docs/QUICKSTART.md)
- [State-drift deep dive](https://github.com/fscfede-beep/verifiable-agent-control-plane/blob/main/docs/STATE_DRIFT_AFTER_DECISION.md)
- [`v0.2.0`](https://github.com/fscfede-beep/verifiable-agent-control-plane/releases/tag/v0.2.0)

Boundary: this is a sanitized reference implementation; it does not expose private production state, credentials, provider IDs, or deployment configuration.

### [RUMBO Agent Reliability](https://github.com/RUMBO-IA/Rumbo/tree/main/systems/agent-reliability)

A minimal public reference for the invariant:

`Capability ≠ Authorization ≠ Execution ≠ Verified Outcome`

It includes deterministic reliability scenarios, privacy-safe evidence, and explicit claim boundaries. Production reliability and third-party validation are not claimed.

## OpenAI — public engineering evidence

> Independent public engineering activity. Nothing here implies OpenAI employment, affiliation, endorsement, maintainer status, or authorship of code written by other contributors.

### Agents SDK: reported finding → upstream remediation

- Authored [issue #4749 — PTY startup cancellation can leak unregistered UnixLocal and Blaxel resources](https://github.com/openai/openai-agents-python/issues/4749), scoped to the pre-registration ownership boundary.
- Upstream [PR #4750 — clean up PTY startup cancellation](https://github.com/openai/openai-agents-python/pull/4750), authored by `Hughhhhcoder`, explicitly states that it fixes the **reachable PTY startup ownership gaps described in #4749**.
- The upstream implementation retained Blaxel cancellation cleanup and UnixLocal TTY descriptor cleanup, while refining one part of the original report: the proposed UnixLocal process-registration lock-contention window was removed because registration has no suspension point while the lock is held and the scenario was not reachable through ordinary producers.
- I reviewed #4750 and reported additional cancellation-precedence boundaries during the fix cycle. The PR is merged upstream.

**Claim boundary:** this proves that a finding I reported contributed to an upstream remediation. I do **not** claim authorship of #4750 or of its merged code.

### Codex plugin for Claude Code

- Authored [PR #730 — optionally consume task prompt files](https://github.com/openai/codex-plugin-cc/pull/730), implementing an opt-in `READ → DELETE → DISPATCH` ownership boundary for `--prompt-file-consume`.
- The PR remains open and unmerged.
- An independent public reviewer explicitly endorsed the ownership ordering and regression coverage. I classify that only as **independent technical review**; I do not claim maintainer authority or OpenAI approval.

### OpenAI Go SDK

- Authored [PR #885 — clarify Bedrock Mantle model-family API roots](https://github.com/openai/openai-go/pull/885).
- It is documentation-only and remains open/unmerged.
- The current PR text explicitly distinguishes the `/openai/v1` and `/v1` model-family routing cases and documents that no SDK behavior, authentication, signing, generated code, or exported API is changed.

## Evidence policy

I separate these states explicitly:

- reported finding
- authored code
- review participation
- independent technical review
- upstream merge
- maintainer approval
- employment / organizational authority
- production deployment

They are **not interchangeable**.

Historical upstream artifacts whose public URLs are deleted or currently unavailable are omitted from this front-page profile rather than treated as current acceptance evidence. Their disappearance is not reinterpreted as proof they never existed; they simply are not used here as current public evidence.

## Current technical focus

- agent harnesses and long-running execution
- sandboxing, isolation, and resource bounds
- async lifecycle and cancellation safety
- deterministic evals, ablations, and regression testing
- MCP, plugins, connectors, and tool routing
- permission and policy boundaries
- canonical-state recovery and effect verification
- verifiable control planes for consequential agent actions

## Product and systems work

- **[RUMBO IA](https://github.com/RUMBO-IA/Rumbo)** — AI CRM and workflow automation with explicit privacy and verification gates.
- **[RUMBO Guardian](https://github.com/RUMBO-IA/rumbo-guardian)** — privacy-first, local-first security intelligence with explainable scoring and a tamper-evident evidence ledger.
- **[VAE Bindings](https://github.com/fscfede-beep/vae-bindings)** — privacy-preserving commitments and GitHub attestations for agent work-unit bindings.
- **[Technical portfolio](https://sebastian-ai-workflow-reliability.miniup.app)** — selected AI workflow and agent-reliability work.

## Reliability thesis

An agent is not reliable merely because it selected the right action. Reliability requires the authorized action, executed action, observed effect, and evidence about that effect to remain consistent across failures.

I am open to engineering roles and technical collaboration in **agent reliability, developer tooling, applied AI, and agent infrastructure**.

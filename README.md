# Federico César

**Founder, RUMBO · AI Systems & Agent Reliability · Applied AI · Automation**

RUMBO builds applied AI systems that help ambitious teams **build, operate, and scale**.

**Ideas into action.**

[Website](https://rumbo.verso.fans) · [YouTube](https://www.youtube.com/@rumboagi) · [X / @RumboAGI](https://x.com/RumboAGI) · [RUMBO on GitHub](https://github.com/RUMBO-IA)

---

## What I build

- **AI agents** with explicit authority, execution, readback, and verification boundaries.
- **Automation systems** for real business workflows, not demo-only flows.
- **Bots and operational interfaces** for customer service, lead handling, internal knowledge, and process execution.
- **Dashboards and control planes** for observable, auditable AI operations.
- **Developer tooling and reliability infrastructure** for long-running, consequential agent workflows.

## Reliability thesis

A model choosing the right action is not enough.

```text
INTENT → AUTHORITY → PREFLIGHT → EXECUTION → READBACK → FALSIFICATION → CLOSURE
```

Reliable agent systems keep the authorized action, executed action, observed effect, and evidence about that effect consistent across failures.

A second invariant I use throughout RUMBO:

```text
Capability ≠ Authorization ≠ Execution ≠ Verified Outcome
```

## Start here

### Verifiable Agent Control Plane

[github.com/fscfede-beep/verifiable-agent-control-plane](https://github.com/fscfede-beep/verifiable-agent-control-plane)

A public Python reference implementation for fail-closed agent execution with exact-state binding, deterministic revalidation, effect readback, replay prevention, and hash-bound receipts.

- [5-minute Reliability Quickstart](https://github.com/fscfede-beep/verifiable-agent-control-plane/blob/main/docs/QUICKSTART.md)
- [State-drift deep dive](https://github.com/fscfede-beep/verifiable-agent-control-plane/blob/main/docs/STATE_DRIFT_AFTER_DECISION.md)
- [`v0.2.0`](https://github.com/fscfede-beep/verifiable-agent-control-plane/releases/tag/v0.2.0)

**Boundary:** sanitized reference implementation; no private production state, credentials, provider IDs, or deployment configuration.

### RUMBO Agent Reliability

[github.com/RUMBO-IA/Rumbo](https://github.com/RUMBO-IA/Rumbo)

Public engineering artifacts around agent authority, execution, verification, and evidence boundaries.

### RUMBO Guardian

[github.com/RUMBO-IA/rumbo-guardian](https://github.com/RUMBO-IA/rumbo-guardian)

Privacy-first security intelligence with explainable scoring and tamper-evident evidence.

## Public engineering evidence

I publish engineering work around agent infrastructure, developer tooling, async lifecycle safety, state drift, permission boundaries, deterministic evaluation, and canonical-state recovery.

Selected public work includes:

- **OpenAI Codex plugin for Claude Code:** authored the current upstream PR series [#725](https://github.com/openai/codex-plugin-cc/pull/725), [#727](https://github.com/openai/codex-plugin-cc/pull/727), [#728](https://github.com/openai/codex-plugin-cc/pull/728), [#729](https://github.com/openai/codex-plugin-cc/pull/729), [#730](https://github.com/openai/codex-plugin-cc/pull/730), [#731](https://github.com/openai/codex-plugin-cc/pull/731), [#732](https://github.com/openai/codex-plugin-cc/pull/732), [#733](https://github.com/openai/codex-plugin-cc/pull/733), [#734](https://github.com/openai/codex-plugin-cc/pull/734), [#737](https://github.com/openai/codex-plugin-cc/pull/737), and [#738](https://github.com/openai/codex-plugin-cc/pull/738). The work spans Windows process safety, exact-thread resume, stale-worker reconciliation, relocated config transfer, prompt-file ownership, durable review-gate state, explicit review JSON contracts, persist-before-spawn ordering, thread-title sanitization, minimal-PATH Node resolution, and durable background rescue/cancellation lifecycle handling.
- **OpenAI Agents SDK:** authored [issue #4749](https://github.com/openai/openai-agents-python/issues/4749) on PTY startup cancellation and pre-registration ownership. Upstream [PR #4750](https://github.com/openai/openai-agents-python/pull/4750), authored by another contributor, explicitly states that it fixes reachable ownership gaps described in that issue and is merged upstream. I do not claim authorship of the merged PR.
- **OpenAI Go SDK:** authored [PR #885](https://github.com/openai/openai-go/pull/885), a documentation-only clarification for Bedrock Mantle model-family API roots. No SDK behavior change or maintainer endorsement is claimed.

**Claim boundary:** public issues, contributions, and reviews do not imply employment, affiliation, endorsement, or maintainer status by OpenAI or any other upstream project unless explicitly stated by that project.

## Current focus

- agent harnesses and long-running execution;
- sandboxing, isolation, and resource bounds;
- MCP, plugins, connectors, and tool routing;
- async lifecycle and cancellation safety;
- permission and policy boundaries;
- deterministic evals and regression testing;
- canonical-state recovery and effect verification;
- production-oriented AI automation;
- public technical communication and open engineering artifacts.

## RUMBO product direction

**Applied AI to build, operate, and scale.**

- Agents
- Bots
- Automation
- Dashboards
- Operational systems
- Reliability and control infrastructure

The operating principle is simple: **evidence over hype**.

## Public channel

**RUMBO on YouTube:** [@rumboagi](https://www.youtube.com/@rumboagi)

Current engineering video: [An Accepted Agent Action Is Not Necessarily Executable](https://www.youtube.com/watch?v=kXE1QMNaeyM)

---

### RUMBO

**Applied AI · Automation · Systems**

**Build what's next.**
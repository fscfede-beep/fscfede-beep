# Case Study — Async Resource Ownership Under Cancellation

## Problem

In asynchronous runtimes, cleanup can become unreachable when ownership leaves a registry before teardown reaches a terminal state.

The critical sequence is:

1. a resource is removed from shared ownership;
2. teardown starts;
3. the caller is cancelled while teardown is suspended;
4. no registry owner remains to retry cleanup.

This is an ownership bug, not merely a cancellation bug.

## Invariant

> Once ownership leaves the registry, cleanup must have an owner that survives caller cancellation until teardown settles.

Caller cancellation may cancel delivery of the result. It must not silently abandon resources that no longer have another owner.

## Public evidence

I authored:

- [OpenAI Agents SDK #4747](https://github.com/openai/openai-agents-python/issues/4747) — teardown after registry removal.
- [OpenAI Agents SDK #4749](https://github.com/openai/openai-agents-python/issues/4749) — resources created before registry ownership.
## Method

I used deterministic, provider-free control-flow reproductions before making backend-specific claims.

For #4747 I checked all seven PTY implementations and explicitly narrowed which finalizer paths were exposed. For #4749 I limited the direct startup-cancellation claim to UnixLocal and Blaxel after checking the other backends.

## Review contribution

I reviewed the implementation work in:

- [PR #4750](https://github.com/openai/openai-agents-python/pull/4750)
- [PR #4751](https://github.com/openai/openai-agents-python/pull/4751)

Review findings included:

- cleanup-exception vs caller-cancellation precedence;
- preservation of `task.cancel("reason")` payloads;
- backend-level coverage at the actual registry-ownership boundary;
- attempt-all semantics so a first teardown error does not prevent later de-owned resources from receiving cleanup.

The current #4751 diff includes the requested backend-level registry-clear/cancellation regression and an attempt-all cleanup helper.

## Reusable model

```text
RESOURCE CREATED → OWNERSHIP TRANSFER → CANCELLATION
        → CLEANUP OWNER SURVIVES → TERMINAL CLEANUP
        → PROPAGATE CANCELLATION / ERROR
```
## Evidence boundary

- Issues #4747 and #4749 were authored by me.
- PRs #4750 and #4751 were authored by other contributors.
- My role on those PRs was review, reproduction design, and invariant analysis.
- Open PR state is not represented as merged or accepted upstream.

# Case Study — Tool Output Policy Boundaries

## Problem

Agent tool output can become a reliability problem when one execution path honors a caller-requested output budget without applying the model's own truncation ceiling.

That creates a mismatch between two tool modes: one path is bounded by policy, another can forward much larger results into model context.

## Invariant

> Caller-requested output limits may narrow policy, but must not widen the model's configured truncation boundary.

A tool result should be bounded by the stricter applicable policy before it reaches model context.

## Public evidence

On [OpenAI Codex issue #42367](https://github.com/openai/codex/issues/42367), authored by another contributor, I rechecked the report against a newer `main` revision and published a concrete one-file reference implementation in my fork:

- [reference commit `9e70016`](https://github.com/fscfede-beep/codex/commit/9e700160e7c77deb373610b58d05d5d54e060d82)

The reference patch:

- passes the current model truncation policy into all three code-mode result paths;
- preserves smaller explicit caller limits;
- uses the stricter policy precedence already present in the function-mode path;
- adds a focused regression for requested-vs-model token budget.
## Validation

On the exact upstream base used for the reference:

- changed files: 1;
- production result paths migrated: 3/3;
- old two-argument production calls remaining: 0;
- `git diff --check`: PASS;
- committed/pushed working tree: clean.

The Windows host did not have Rust `cargo` / `rustc` available for that validation, so I explicitly did **not** claim compile or unit-test PASS.

## Why this matters

Large tool results are not just a cost problem. They can consume a turn's context budget, increase latency, and make downstream reasoning less predictable.

The reusable pattern is:

```text
CALLER REQUEST
      ↓
TOOL OUTPUT POLICY
      ↓
MODEL TRUNCATION POLICY
      ↓
STRICTER BOUND WINS
      ↓
MODEL CONTEXT
```
## Evidence boundary

- Issue #42367 was not authored by me.
- My contribution was current-main verification plus a public fork reference implementation.
- Codex documentation states that external code contributions are not accepted through ordinary upstream PRs; the fork is therefore presented only as a maintainer-readable reference.
- No upstream merge, endorsement, or employment claim is made.

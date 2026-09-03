# Case Study — Fail-Closed CI Gates

## Problem

A required CI job can appear harmlessly skipped when one of its dependencies fails. In branch-protection terms, that can be weaker than an explicit failing required check.

The failure is not only inside a test step. It can happen one level earlier, in the scheduler predicate that decides whether the required job starts at all.

## Invariant

> The job-level scheduler condition and the first executable failure guard must agree on what counts as green.

If a dependency result is not successful, the required job should remain visible and fail before repository-controlled work such as checkout begins.

## Public evidence

I reviewed [OpenAI Python PR #3780](https://github.com/openai/openai-python/pull/3780), which addresses required checks becoming skipped when dependency-lock validation fails.

My review focused on:

- putting the dependency failure guard before checkout;
- using `!cancelled()` as the workflow-cancellation boundary;
- aligning the scheduler predicate with `needs.dependency-locks.result != 'success'`;
- regression coverage that pins the guard as the first executable step.
## Current implementation shape

The current PR diff applies the non-success predicate to all four required jobs:

- `lint`
- `build`
- `test`
- `test-httpx2`

Each job now includes an explicit dependency-lock failure step before checkout, and the regression test asserts that ordering.

## Self-correction

During review I briefly left a `CHANGES_REQUESTED` comment based on a stale reading of the then-current head. I re-read the exact revision, publicly corrected the review, and withdrew that blocker.

That correction is part of the engineering record rather than something to hide: evidence must outrank reviewer confidence.

## Reusable model

```text
DEPENDENCY RESULT
      ↓
SCHEDULER PREDICATE
      ↓
REQUIRED JOB STARTS
      ↓
FAIL-CLOSED GUARD
      ↓
ONLY THEN CHECKOUT / BUILD / TEST
```
## Evidence boundary

- PR #3780 is authored by another contributor.
- My role is technical review and failure-model analysis.
- The current diff contains the hardened predicate and first-step guard; that does not establish causation or upstream acceptance of my review.
- The PR remains represented according to its live GitHub state.

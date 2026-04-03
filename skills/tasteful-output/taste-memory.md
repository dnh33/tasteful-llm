# Taste Memory — Learning System

The taste profile is a living document that compounds your taste over sessions. It starts empty and grows as you work.

## Reading the Profile

Load the taste profile before generating creative output, alongside the specificity test. Apply learned preferences as additional constraints on top of the 5 checks.

If no taste profile exists yet, skip this step — the 5 checks and anti-pattern catalog are sufficient for first use.

## When to Write

Capture a taste data point when any of these happen:

**Explicit rejection:** The user says "no", "not like that", "too [adjective]", or rewrites your output. Record what was rejected and why.

**Explicit approval:** The user says "perfect", "ship it", "yes", or accepts output without changes. Record what worked.

**Recurring correction:** The same type of fix applied 2+ times across sessions. Promote from individual correction to learned preference.

**Voice signal:** The user consistently uses specific words, sentence structures, or tonal patterns in their own writing. Mirror these in the Voice DNA section.

## What to Capture

For each entry, record:
- **What** — the specific preference or rejection
- **When** — date (so stale preferences can be identified)
- **Evidence** — the actual text that was approved/rejected

## Profile Hygiene

- Don't record one-off corrections as permanent preferences
- Promote to "learned preference" only after 2+ occurrences
- Date everything so preferences can age out
- Keep the profile under 500 words — prune oldest entries when it grows

## Where the Profile Lives

The taste profile is stored at `.tasteful-llm/taste-profile.md` in the user's project root or `~/.tasteful-llm/taste-profile.md` for global preferences. Project-level profiles override global.

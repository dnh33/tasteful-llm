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

## Creating the Profile

On first write, create the directory and file using the structure from @taste-profile-template.md:

1. Create `.tasteful-llm/` in the project root (or `~/.tasteful-llm/` for global)
2. Copy the template structure into `taste-profile.md`
3. Add the first entry under the appropriate section

Do not create the profile preemptively. Only create it when there's a real data point to record.

## Where the Profile Lives

The taste profile is stored at `.tasteful-llm/taste-profile.md` in the user's project root or `~/.tasteful-llm/taste-profile.md` for global preferences. Project-level profiles override global.

## Entry Provenance

Profile entries carry source tags: `[setup:date]` for questionnaire-generated entries, `[observed:date]` for passively-learned entries.

When reading the profile, treat both equally — apply all entries as constraints regardless of source.

When WRITING to the profile, apply the override rule: if a new observed preference contradicts an existing `[setup:*]` entry on the same dimension, the observation replaces the setup entry. The profile converges toward demonstrated reality over self-report.

A "contradiction on the same dimension" means: the entries make opposing claims about the same aspect of writing. Example: setup says "short sentences, verb-forward" but observations consistently show the user approving medium-length sentences with dependent clauses. The observation wins.

When writing new entries, always include the source tag:
- Passive learning entries: `[observed:YYYY-MM-DD]`
- Entries from `/taste-setup`: `[setup:YYYY-MM-DD]`
- Future voice calibration entries (v0.4.0): `[calibration:YYYY-MM-DD]`

---
name: anti-slop-audit
description: "Use when reviewing existing text for AI slop: landing pages, README prose, pitch decks, marketing copy, product descriptions. Use when the user says 'audit this copy', 'check for slop', 'does this sound like AI', 'tighten this up', 'review this for quality', or 'is this too generic'."
---

# Anti-Slop Audit

Retrospective review of existing text for AI slop patterns. The tasteful-output skill shapes text while it is written. This skill reviews text that already exists, whether a person or a model wrote it.

The question to answer for every sentence: could this sentence be about something else? If yes, flag it, name the pattern, and offer a fix.

## The Process

1. Read the full text provided.
2. Classify the content tier, using the genre tiers in [tasteful-output/SKILL.md](../tasteful-output/SKILL.md):
   - Full: product marketing, sales copy, ad copy, case studies, email sequences.
   - Reduced: brand manifestos, editorial, newsletters, vision statements.
   - Craft: social posts, personal essays, community docs, internal comms.
3. Read [specificity-test.md](../tasteful-output/specificity-test.md) for the check procedure. Full tier runs 5 checks scored out of 5, Reduced runs 3 checks scored out of 3, and Craft runs the voice test only.
4. Read [anti-pattern-catalog.md](../tasteful-output/anti-pattern-catalog.md). The catalog has 52 patterns in six categories (L Language, S Structure, C Copy, ST Strategy, D Design/UI, F Formatting). An audit loads the whole catalog, so open every category file listed in it.
5. If a taste profile exists (`~/.tasteful-llm/taste-profile.md` or `.tasteful-llm/taste-profile.md`), read it and treat its Anti-Preferences as extra patterns.
6. Run every sentence through the checks for its tier, then scan the whole text against the catalog. For the Craft tier, use the voice test in [voice-test.md](../tasteful-output/voice-test.md) as the gate.
7. Produce the report in the format below.

## Single hits and density

Most patterns are worth flagging on one occurrence. Two are habits of rate, and one occurrence proves nothing:

- L13 Era Vocabulary (delve, tapestry, pivotal, underscore, and similar words): flag a text with more than 2 era words per 500 words, or 2 in one paragraph.
- F4 Em-Dash Reflex: flag a text with more than 1 em dash per 250 words.

For these two, count the occurrences, scale the count to the threshold's word window, and list where they cluster. A single "pivotal" in 800 words is normal usage. When a text crosses a threshold, flag the cluster, quote two or three instances, and give the count. When the density is ordinary, write "within normal range" in the report and move on. The catalog entries for these patterns carry the sources.

Sources in the catalog describe tendencies in model output. They support a judgment about a text and do not prove who wrote it, so the report should talk about what the text does and avoid claims about who or what produced it.

## Output Format

```
## Slop Audit: [Document Name]

Tier: [Full / Reduced / Craft]
Overall: [X]% of sentences pass | Severity: [Clean / Touch-ups / Rewrite / Start Over]

### Findings

#### 1. [Section or line reference]
Original: "[the sentence]"
Pattern: [Code, e.g. L3: Thesaurus Parade]
Missed checks: [which checks]
Fix: "[specific rewrite]"

#### 2. ...

### Density Report
[L13 and F4: count, word window, where they cluster, verdict]

### Strongest Lines
[2-3 lines that passed every check, with a sentence on why each works]

### Voice Assessment
[Reduced and Craft tiers: run the four questions in [voice-test.md](../tasteful-output/voice-test.md) and report rhythm, surprise, emotional specificity and the named emotion]

### Summary
- Sentences audited: [N]
- Passed clean: [N]
- Rewritten: [N]
- Deleted (no salvageable content): [N]
```

Rewrites follow the same rule as generation. Use only facts, numbers and names that appear in the source text or that the user supplies. Where a fix needs a figure the text lacks, write a placeholder such as `[metric: X]` and say so.

## Severity Scale

| Score | Rating | Meaning |
|-------|--------|---------|
| 90-100% | Clean | Minor polish only |
| 70-89% | Touch-ups | A few sentences need specificity |
| 40-69% | Rewrite | Structure may be fine but the content is hollow |
| 0-39% | Start Over | Start from what is true |

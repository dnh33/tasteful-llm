# Contributing to TastefulLLM

## Adding a New Anti-Pattern

1. Find a source: a measurement, a vendor guideline, or a documented example. A pattern with no source does not go in.
2. Add the full pattern (Slop, Why it's slop, Fix) to the matching terminal file in `skills/tasteful-output/patterns/`.
3. Put a metadata line directly under the pattern heading, in exactly this form: `Status: <value> · Seen in: <...> · Verified: <...>`. The status is one of consistent, rising, fading or unchecked (unchecked means the original pattern was not re-verified in 2026-10). Seen in names the models or says "all" when the source does not split by model. Verified is a month such as 2026-10. `scripts/check.py` validates this line on every pattern heading.
4. Add the one-liner to the category router (for example `patterns/language.md`).
5. Add the entry to `skills/tasteful-output/anti-pattern-catalog.md` and update its count.
6. Update the stated pattern count in `.claude-plugin/plugin.json`, `README.md`, `CHANGELOG.md` and this file.
7. Run `python scripts/check.py`. It fails on count mismatches, broken relative links, `@` file references in skills, non-spec frontmatter keys, SKILL.md files over 500 lines, and a stale `dist/`. If it reports `dist/` out of date, run `python scripts/build_prompt.py` and commit the result.

Write the rule by function, with two or three surface forms as examples. Literal strings mutate once they are suppressed, so the category router carries one shared note that examples are illustrative and other wordings of the same move count. For vocabulary and punctuation habits, state a density threshold in place of a ban. The two thresholds in use are L13, more than 2 era words per 500 words or 2 in one paragraph, and F4, more than 1 em dash per 250 words. Use the same wording in the catalog one-liner, the terminal file and anti-slop-audit.

The catalog follows its own ST7 rule. A Fix example gets a bracket placeholder such as `[metric]` or `[customer name]` for any figure, name or company result, or an explicit "(illustrative figure)" marker. Never pair a real company with an invented result. Mark a Wikipedia section name "(section name not verified)" unless you opened the page and saw it.

## Adding a New Category

1. Create a terminal file or directory under `patterns/`.
2. Create a category router if the category has 6 or more patterns.
3. Add the category section to `anti-pattern-catalog.md` and update the stated category count wherever it appears.

## Adding or Changing a Model Profile

Profiles live in `skills/tasteful-output/profiles/` and stay under 60 lines. Each has two sections. `## For the model` is addressed to the model writing the text, in second person, and says what to watch for and how strict to be. `## Evidence` holds sources, figures, the `Verified: YYYY-MM` line, a plain statement of where the evidence is thin, and notes for prompt authors such as temperature or `reasoning_content` handling. `scripts/build_prompt.py` embeds only the first section. When citing EQ-Bench, say that it is a lexical, fiction-tuned metric.

## File Architecture

Skills use a router layout: an index file points at smaller files so the model loads only what the task needs.

- Router files contain pattern names, one-line descriptions and references.
- Terminal files contain full examples, diagnoses and fixes.
- SKILL.md files link to their siblings with relative markdown links. Do not use `@file` references, and keep SKILL.md frontmatter to Agent Skills spec fields (`name`, `description`, and optionally `license`, `metadata`, `allowed-tools`, `compatibility`).

The generation skill describes target behavior and keeps its examples few. The catalog holds the long lists of slop examples and is read after drafting, as a review pass.

When adding content, put it at the right level:
- New pattern: terminal file.
- New sub-group: new terminal file and an update to the category router.
- New category: new router, terminals and a catalog update.

## Taste Profile System

The taste profile at `.tasteful-llm/taste-profile.md` is user-specific and is not part of the plugin repo. Do not commit taste profiles. The template at `skills/tasteful-output/taste-profile-template.md` defines the structure, so edit that to change profile sections.

The learning protocol in `skills/tasteful-output/taste-memory.md` defines when and how the profile gets updated. Test changes to it by checking that the profile captures the right data points without over-recording.

## Testing

Run `python scripts/check.py`, then install locally and verify:

```
/plugin marketplace add ./
/plugin install tasteful-llm@tasteful-llm
```

- Ask Claude to write marketing copy. It should activate tasteful-output.
- Ask Claude to audit existing text. It should activate anti-slop-audit.
- Check that a new pattern shows up in the audit output.

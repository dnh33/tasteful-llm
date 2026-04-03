# Contributing to TastefulLLM

## Adding a New Anti-Pattern

1. Add the full pattern (Slop / Why it's slop / Fix) to the appropriate terminal file in `skills/tasteful-output/patterns/`
2. Add the one-liner to the category router (e.g., `patterns/language.md`)
3. Add the entry to `skills/tasteful-output/anti-pattern-catalog.md`
4. Update the pattern count in `.claude-plugin/plugin.json` description and `README.md`

## Adding a New Category

1. Create a new terminal file or directory under `patterns/`
2. Create a category router if the category has 6+ patterns
3. Add the category section to `anti-pattern-catalog.md`

## File Architecture

This plugin uses a recursive router pattern. Every file that could be large is itself an index that references smaller files. This keeps context usage minimal — Claude only loads what it needs.

- **Router files** contain pattern names + one-line descriptions + references
- **Terminal files** contain full examples, diagnoses, and fixes

When adding content, put it in the right level:
- New pattern → terminal file
- New sub-group → new terminal file + update category router
- New category → new router + terminals + update catalog

## Taste Profile System

The taste profile at `.tasteful-llm/taste-profile.md` is user-specific and NOT part of the plugin repo. Don't commit taste profiles. The template at `skills/tasteful-output/taste-profile-template.md` defines the structure — edit that if you want to change profile sections.

The learning protocol in `skills/tasteful-output/taste-memory.md` defines when and how the profile gets updated. Changes to the learning protocol should be tested by verifying the profile captures the right data points without over-recording.

## Testing

After changes, install locally and verify:

```bash
claude plugin add ./
```

- Ask Claude to write marketing copy → should activate tasteful-output
- Ask Claude to audit existing text → should activate anti-slop-audit
- Verify your new pattern gets referenced in audit output

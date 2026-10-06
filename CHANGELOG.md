# Changelog

## v0.4.0: Evidence pass and multi-harness support (2026-10-06)

### Changed: generation skill
- Iron Law rewritten in plain language. The old wording said sentences "must fail" the Substitution Test in one place and "must pass" in another. A sentence now passes a check when it is specific, everywhere.
- ALL-CAPS laws, "STOP" language, the Rationalizations table and the Red Flags ban list are gone. Rules are calm imperatives with the reason attached, because recent models over-react to emphatic wording.
- The ban list is replaced by a short "Write like this" section with three examples. Naming banned phrases in a generation prompt can prime them (Antislop; Rana 2026, one small model), so the long lists live in the catalog.
- New loading order: classify tier and mode, read the model profile, draft with the positive rules and the 5 checks, review the draft against the catalog (Full and Reduced tiers), then run the voice test where it applies.
- New hard rule: no invented statistics, customers, quotes or studies. Use placeholders such as `[metric: X]` (catalog pattern ST7).

### Added: model profiles
- `skills/tasteful-output/profiles/claude.md`, `gpt.md` and `deepseek.md`, each under 60 lines. Every profile has a `## For the model` section (second person, what to watch for and how strict to be) and a `## Evidence` section (sources, figures, the Verified line and harness notes). The flat system prompts embed only the first section.
- EQ-Bench slop scores are cited as a lexical, fiction-tuned metric. DeepSeek evidence is thin and the profile says so. The GPT profile separates GPT-5.x, which runs long, from GPT-6 Astra and Sol, which do not.

### Added: catalog (39 to 52 patterns, five to six categories)
- Wider definitions for L3 (tricolon reflex), L10 (vague authority), L12 (the full contrast-reframe family), C3 (agreement-first openers), D1 (distributional defaults) and ST4.
- New patterns L13 Era Vocabulary, L14 Trailing -ing Gloss, L15 Significance Inflation, L16 Copula Dodge, L17 Importance Flag, S9 Recap Reflex, S10 Fragment Drama, C9 Offer-and-Sign-off Closer, ST7 Invented Specific.
- New category F Formatting: F1 Bold-Label Bullets, F2 Mechanical Boldface, F3 Title Case Headings, F4 Em-Dash Reflex.
- Every pattern carries one metadata line, `Status: <value> · Seen in: <...> · Verified: <...>`. The status is consistent, rising, fading or unchecked, where unchecked marks an original pattern that was not re-verified in 2026-10.
- L13 and F4 are judged by density, with one threshold each: L13 is flagged at more than 2 era words per 500 words, or 2 in one paragraph, and F4 at more than 1 em dash per 250 words. anti-slop-audit reports density for them in place of flagging single hits.
- Fix examples in the catalog use bracket placeholders such as `[metric]` or are marked illustrative, so the catalog follows its own ST7 rule. Real companies are no longer paired with invented results.
- Wikipedia section names that could not be confirmed are marked "(section name not verified)", and an unopened citation was dropped.

### Fixed
- `@file` references in SKILL.md files were not a documented skill feature. They are now relative markdown links with read instructions.
- anti-slop-audit used repo-root paths that break once the plugin is installed. It now links to `../tasteful-output/...`.
- README install command was not a real command. The README now documents the Claude Code marketplace commands, Codex install, and flat system prompts.
- README no longer quotes a grammar-score and editor-survival statistic that had no source.
- The claim that uniform sentence length fingerprints AI output is softened to a tendency (Pangram, textpulse).
- rubin-calibration.md: two probes presented lines as Rick Rubin quotes that could not be verified. They are now plain propositions. The Saint-Exupéry line is attributed to *Terre des hommes* (1939) without "via Rick Rubin".
- `/taste-setup` is documented as `/tasteful-llm:taste-setup`, the namespaced command.
- Counts say 52 patterns in six categories everywhere.
- specificity-test.md and voice-test.md now match SKILL.md on tiers: Full runs 5 checks scored out of 5, Reduced runs 3 checks scored out of 3, and Craft runs the voice test only, which is its gate.
- anti-slop-audit reports "Missed checks" in place of "Failed" and links the voice test for the Voice Assessment section.
- The README describes Name Swap correctly, drops an unsourced generalisation about landing pages, and states that the flat prompt has no taste profile and carries a catalog index in place of the post-draft review.
- Em-dash density in the skill files and README is under 1 per 250 words, and the "Other wordings count" closer is replaced by one shared note in each router.

### Packaging
- `.claude-plugin/marketplace.json`, so the repo installs with `/plugin marketplace add dnh33/tasteful-llm`.
- Codex support: `.agents/plugins/marketplace.json`, `scripts/install-codex.sh` and an AGENTS.md snippet. A root `plugin.json` (Agent Plugins schema) makes the repo installable with `codex plugin marketplace add dnh33/tasteful-llm`.
- `scripts/build_prompt.py` generates `dist/system-prompt-{claude,gpt,deepseek}.md` for API use.
- `scripts/check.py` and a GitHub Actions workflow check counts, links, frontmatter, SKILL.md length and that `dist/` is current.
- plugin.json version 0.4.0.

## v0.3.0: Taste onboarding (2026-04-03)

### New: `/taste-setup` command
- Guided taste calibration session that generates a foundational taste profile
- Phase 0: silent scan of project prose (README, CLAUDE.md, docs)
- Phase 1: mirror findings back with quoted evidence
- Phase 2: 2-4 adaptive editorial questions (editorial instinct, taste boundary, A/B comparison, anti-preferences)
- Phase 2b (opt-in): Rick Rubin creative philosophy calibration, with 3 probes from a pool of 8, each mapping to behavioral changes in the skill
- Phase 3: aha moment, which generates two versions using the emerging profile vs. generic, and the user validates
- Phase 4: prose characterization, a paragraph describing the user's editorial taste, saved as the profile

### New: Creative Beliefs profile section
- Optional section populated by Rubin calibration probes
- Each belief maps to a specific behavioral change in tasteful-output (e.g., "subtraction is the primary revision move" leads to a more aggressive Zombie Test)

### New: Source tags and entry provenance
- Profile entries now carry `[setup:date]` or `[observed:date]` tags
- Override rule: passive observations replace setup entries when they conflict
- Profile converges toward demonstrated reality over self-report

### New: Global + project profile merge
- Global profile (`~/.tasteful-llm/`) = your default taste
- Project profile (`.tasteful-llm/`) = overrides for this specific project
- Two-file merge: project entries override global per dimension

### Updated: taste-profile-template.md
- Added Creative Beliefs section
- Added `<!-- tasteful-llm-profile:v2 -->` version marker

### Updated: taste-memory.md
- Added Entry Provenance section with source tag format and override rule

### Updated: tasteful-output SKILL.md
- Loading logic now supports global + project merge
- Loads Creative Beliefs as editorial stance constraints

### Fixed: Over-correction of good existing writing
- Added Operating Mode: Generate (strict, default) vs. Refine (preserve 3-4/5 sentences, offer alternatives)
- Sentences scoring 3-4/5 in Refine mode are preserved with improvement offered, not silently rewritten
- New Refine Mode Scoring section in specificity-test.md

## 0.2.0 (2026-04-03)

- Taste Memory: learning system that captures user preferences over sessions
- Taste profile template for first-time setup
- Profile stored at `.tasteful-llm/taste-profile.md` (project) or `~/.tasteful-llm/taste-profile.md` (global)

## 0.1.0 (2026-04-03)

Initial release.

- `tasteful-output` skill: Substitution Test gate with 5 mechanical checks, genre classifier (Full/Reduced/Craft), 39 anti-patterns across 5 categories, Voice Test constructive layer
- `anti-slop-audit` skill: retrospective review of existing text with structured audit report
- Recursive router architecture: files load only what's needed per task

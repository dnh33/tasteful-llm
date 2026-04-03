# Changelog

## v0.3.0 — Taste Onboarding

### New: `/taste-setup` command
- Guided taste calibration session that generates a foundational taste profile
- Phase 0: silent scan of project prose (README, CLAUDE.md, docs)
- Phase 1: mirror findings back with quoted evidence
- Phase 2: 2-4 adaptive editorial questions (editorial instinct, taste boundary, A/B comparison, anti-preferences)
- Phase 2b (opt-in): Rick Rubin creative philosophy calibration — 3 probes from pool of 8, each mapping to behavioral changes in the skill
- Phase 3: aha moment — generates two versions using emerging profile vs. generic, user validates
- Phase 4: prose characterization — a paragraph describing the user's editorial taste, saved as the profile

### New: Creative Beliefs profile section
- Optional section populated by Rubin calibration probes
- Each belief maps to a specific behavioral change in tasteful-output (e.g., "subtraction is the primary revision move" → more aggressive Zombie Test)

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

## 0.2.0 — 2026-04-03

- Taste Memory: learning system that captures user preferences over sessions
- Taste profile template for first-time setup
- Profile stored at `.tasteful-llm/taste-profile.md` (project) or `~/.tasteful-llm/taste-profile.md` (global)

## 0.1.0 — 2026-04-03

Initial release.

- `tasteful-output` skill: Substitution Test gate with 5 mechanical checks, genre classifier (Full/Reduced/Craft), 39 anti-patterns across 5 categories, Voice Test constructive layer
- `anti-slop-audit` skill: retrospective review of existing text with structured audit report
- Recursive router architecture: files load only what's needed per task

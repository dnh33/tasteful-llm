# TastefulLLM

A Claude Code plugin that runs five mechanical checks on every sentence Claude writes in creative contexts. Sentences that could appear on a competitor's site with only the name swapped get rewritten. Automatically.

## The Problem

"Empower your team to unlock seamless collaboration." Swap "your team" for any noun. Still works. That's the test it fails, and it's the same test every AI-written sentence fails: zero information survives a name change.

The average AI-generated landing page has grammar scores above 95 and a human-editor survival rate near zero. Every sentence is correct. None of them are *true* -- true about the specific product, the specific user, the specific mechanism.

TastefulLLM applies one rule: **if the sentence still works with a competitor's name, it contains no information and gets rewritten until it does.**

## What It Does

**Three skills:**

- **tasteful-output** -- Runs the five-check Substitution Test on every sentence Claude produces in copy, messaging, naming, branding, README prose, or product strategy. Output ships at 5/5. Anything below 3 gets deleted and restarted from what's actually true. When refining your existing text, sentences scoring 3-4 are preserved with improvement offered -- not silently rewritten.

- **anti-slop-audit** -- Audits existing text line-by-line: per-sentence pass/fail scores, pattern codes from the 39-pattern catalog (e.g., L3: Thesaurus Parade), and specific rewrites.

- **taste-setup** -- Guided taste calibration session. Scans your project's prose, mirrors what it sees in your writing, asks 2-4 editorial questions, and generates a taste profile that shapes all future output. Run once; the profile compounds from there.

## The Substitution Test

Five checks, each binary pass/fail:

1. **Name Swap** -- Replace product name with a competitor's. Still works? Fail.
2. **Concreteness** -- Contains a number, mechanism, or named thing? No? Fail.
3. **Who Cares** -- Names a specific person with a specific problem? No? Fail.
4. **Zombie** -- Remove all adjectives. Still says something? No? Fail.
5. **So-What Chain** -- Ask "so what?" three times. Hit concrete? No? Fail.

**Scoring:** 5/5 ships. 3-4 gets rewritten with the missing specificity added. 0-2 gets deleted.

## Installation

```bash
claude plugin add github:dnh33/tasteful-llm
```

## Taste Setup

Run `/taste-setup` to build your taste profile in one session instead of waiting 20 sessions for the passive learning system to figure you out.

The session works like this:

1. **Silent scan** -- reads your README, CLAUDE.md, and any docs for existing prose patterns
2. **Mirror** -- presents what it found: "Your sentences tend to be short. You don't hedge. You lead with imperatives." You confirm or correct.
3. **Editorial questions** -- "When you edit others' writing, what do you always fix?" and "If I wrote something technically flawless but it felt wrong, what would the wrongness be?"
4. **A/B comparison** -- two versions of the same sentence, both competent, different voice. Which would you ship and why?
5. **Creative philosophy** (opt-in) -- 3 Rick Rubin quotes as calibration probes. "Perfection is obtained not when there is no longer anything to add, but when there's no longer anything to take away." Agree, disagree, or complicated? Each answer maps to a behavioral change in the skill.
6. **The aha moment** -- generates two versions of a paragraph using your emerging profile vs. generic. You pick.
7. **Characterization** -- a prose paragraph describing your editorial taste, saved as your profile.

Profile saves to `~/.tasteful-llm/taste-profile.md` (global) or `.tasteful-llm/taste-profile.md` (project). Global is your default voice. Project profiles override global for specific contexts.

## The Anti-Pattern Catalog

39 named patterns across 5 categories. Three examples:

**L3: Thesaurus Parade** -- "Streamline, optimize, and revolutionize your workflow." Three verbs that all mean "make better." Fix: "Cut weekly reporting from four hours to fifteen minutes."

**C1: Everything Headline** -- "The All-in-One Platform for Modern Teams." Describes every B2B SaaS company that has ever existed. Fix: "Engineering managers: stop writing status reports."

**D4: Friendly Robot Voice** -- "Whoops! Looks like something didn't go as planned!" Performative personality masking absent information. Fix: "Save failed -- couldn't write to disk. Check permissions."

Browse all 39: [`skills/tasteful-output/anti-pattern-catalog.md`](skills/tasteful-output/anti-pattern-catalog.md)

## When It Activates

| Tier | Content Types | Gate |
|------|--------------|------|
| Full | Marketing, sales copy, ad copy, case studies, email sequences | All 5 checks |
| Reduced | Brand voice, editorial, newsletters, vision statements | Name Swap + Zombie + 1 |
| Craft | Social posts, personal essays, community docs | Voice Test only |

## When It Does NOT Activate

Code, debugging, refactoring, data analysis, technical documentation, structured output (JSON/YAML), git commits.

## Running an Audit

> "Audit this landing page copy for slop"
> "Does this README sound like AI?"
> "Check this pitch deck for generic language"

Returns per-sentence scores against the 5 checks, flags from the 39-pattern catalog (e.g., L3: Thesaurus Parade), and a rewrite for each failing sentence.

## Taste Memory

TastefulLLM writes a taste profile to `.tasteful-llm/taste-profile.md` in your project. The file stores five things:

- **Voice DNA** -- sentence length, punctuation habits, tonal stance. Extracted from your edits, not declared.
- **Creative Beliefs** -- philosophical positions about craft from `/taste-setup` Rubin calibration. Optional. Each belief changes how the skill weighs checks.
- **Learned preferences** -- corrections that recur 2+ times get promoted to rules.
- **Confirmed good** -- output you shipped without edits.
- **Anti-preferences** -- things you reject beyond the standard 39 patterns.

The profile starts empty or gets seeded by `/taste-setup`. First session, every sentence hits the 5 checks. Tenth session catches *your* slop -- the patterns that pass the five checks but don't sound like you wrote them.

## Architecture

Recursive router -- a Full-tier task loads specificity-test.md, then the catalog router, then only the terminal pattern file that matched. Reduced-tier skips the catalog entirely:

```
SKILL.md -> specificity-test.md (always)
         -> taste-profile (if exists -- global + project merged)
         -> anti-pattern-catalog.md (Full/Reduced tier)
             -> patterns/language.md -> language/modifiers.md
             -> patterns/copy.md -> copy/headlines.md
             -> ...only the relevant terminal file
         -> voice-test.md (Reduced/Craft tier)
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT

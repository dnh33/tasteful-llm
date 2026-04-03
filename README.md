# TastefulLLM

A Claude Code plugin that eliminates AI slop from creative and strategic output.

## The Problem

"Empower your team to unlock seamless collaboration." That sentence describes every product ever made. AI tools produce text that sounds like everything and says nothing. The average AI-generated landing page passes a grammar check and fails a "would a human editor keep this?" check on most of its sentences.

TastefulLLM applies one test to every sentence Claude writes in creative contexts: **could this sentence appear on a competitor's website with only the name changed?** If yes, it gets rewritten until it can't.

## What It Does

**Two skills:**

- **tasteful-output** — Generative filter. Activates when Claude produces copy, messaging, naming, branding, README prose, or product strategy. Every sentence runs through the Substitution Test before the user sees it.

- **anti-slop-audit** — Review tool. Point it at existing text (yours, a contractor's, another AI's) and get a line-by-line audit with pattern matches and specific rewrites.

## The Substitution Test

Five mechanical checks, each binary pass/fail:

1. **Name Swap** — Replace product name with a competitor's. Still works? Fail.
2. **Concreteness** — Contains a number, mechanism, or named thing? No? Fail.
3. **Who Cares** — Names a specific person with a specific problem? No? Fail.
4. **Zombie** — Remove all adjectives. Still says something? No? Fail.
5. **So-What Chain** — Ask "so what?" three times. Hit concrete? No? Fail.

## Installation

```bash
claude plugin add github:dnh33/tasteful-llm
```

## The Anti-Pattern Catalog

39 named patterns across 5 categories. Three examples:

**L3: Thesaurus Parade** — "Streamline, optimize, and revolutionize your workflow." Three verbs that all mean "make better." Fix: "Cut weekly reporting from four hours to fifteen minutes."

**C1: Everything Headline** — "The All-in-One Platform for Modern Teams." Describes every B2B SaaS. Fix: "Engineering managers: stop writing status reports."

**D4: Friendly Robot Voice** — "Whoops! Looks like something didn't go as planned!" Performative personality hiding absent information. Fix: "Save failed — couldn't write to disk. Check permissions."

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

Ask Claude to review existing text:

> "Audit this landing page copy for slop"
> "Does this README sound like AI?"
> "Check this pitch deck for generic language"

The audit skill produces a structured report with per-sentence findings, pattern codes, and specific rewrites.

## Taste Memory

TastefulLLM learns your preferences over time. It maintains a taste profile at `.tasteful-llm/taste-profile.md` in your project that captures:

- **Voice DNA** — your sentence patterns, word choices, tonal preferences
- **Learned preferences** — recurring corrections promoted to rules after 2+ occurrences
- **Confirmed good** — output you shipped without edits (what "right" looks like for you)
- **Anti-preferences** — things you specifically reject beyond the standard catalog

The profile starts empty and grows as you work. First session, TastefulLLM catches generic slop. Tenth session, it catches *your* slop.

## Architecture

Recursive router pattern — each file loads only what's needed:

```
SKILL.md → specificity-test.md (always)
         → taste-profile (if exists — learned preferences)
         → anti-pattern-catalog.md (Full/Reduced tier)
             → patterns/language.md → language/modifiers.md
             → patterns/copy.md → copy/headlines.md
             → ...only the relevant branch
         → voice-test.md (Reduced/Craft tier)
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add patterns, categories, and test changes.

## License

MIT

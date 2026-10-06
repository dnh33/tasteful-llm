# TastefulLLM

A set of skills that makes Claude Code, Codex and other LLM harnesses write marketing copy, naming, README prose and positioning that says something about the specific product. Each sentence goes through five checks. A sentence that still works with a competitor's name on it gets rewritten.

## The problem

"Empower your team to unlock seamless collaboration." Put any competitor's name in front of it and it still works. That is the Name Swap test, and this sentence fails it because nothing in it depends on the product.

TastefulLLM applies one rule: if the sentence still works with a competitor's name, it contains no information and gets rewritten until it does.

## What it does

Three skills:

- tasteful-output runs the five checks on copy, messaging, naming, branding, README prose and product strategy while the model writes. It tells the model what good output looks like, then reviews the draft against the anti-pattern catalog. When you ask it to refine your own text, sentences scoring 3-4 are kept and an improvement is offered.
- anti-slop-audit audits existing text line by line: per-sentence results, pattern codes from the 52-pattern catalog (for example L3: Thesaurus Parade), density reports for habits that only matter in volume, and specific rewrites.
- taste-setup runs a guided calibration session. It scans your project's prose, mirrors what it sees, asks 2-4 editorial questions, and saves a taste profile that shapes later output.

## The substitution test

Five checks. A sentence passes a check when it is specific.

1. Name Swap: replace the product name with a competitor's. If the sentence stops making sense, it passes.
2. Concreteness: it holds a number, mechanism, constraint or named thing, and that element is real.
3. Who Cares: it names a specific person with a specific problem.
4. Zombie: remove all adjectives and adverbs and it still says something.
5. So-What Chain: asking "so what?" up to three times reaches a concrete answer.

Scoring for the Full tier: 5/5 ships. 3-4 gets rewritten with the missing specificity added. 0-2 gets deleted and restarted from what is true. The Reduced tier runs three of the checks and scores out of 3. The Craft tier runs the voice test only.

One hard rule applies throughout: the skills never invent statistics, customers, quotes or studies. Where a sentence needs a figure that was not supplied, the draft carries a placeholder such as `[metric: X]` and says so.

## Installation

### Claude Code

```
/plugin marketplace add dnh33/tasteful-llm
/plugin install tasteful-llm@tasteful-llm
```

Shell equivalents: `claude plugin marketplace add dnh33/tasteful-llm` and `claude plugin install tasteful-llm@tasteful-llm`.

### Codex

Either copy the skills into your Codex skills directory:

```bash
git clone https://github.com/dnh33/tasteful-llm
sh tasteful-llm/scripts/install-codex.sh            # installs to ~/.agents/skills
sh tasteful-llm/scripts/install-codex.sh ./.agents/skills   # or a directory you name
```

or add the repo as a Codex marketplace:

```bash
codex plugin marketplace add dnh33/tasteful-llm
```

Then add a short pointer to your `AGENTS.md`:

```markdown
For marketing copy, naming, README prose and positioning, use the tasteful-output skill.
To review existing text, use the anti-slop-audit skill.
Do not apply either skill to code, commit messages or tool-call commentary.
```

Codex limits combined AGENTS.md content to 32 KiB by default, so keep the snippet short.

### API and other harnesses

Generated system prompts live in `dist/`: `dist/system-prompt-claude.md`, `dist/system-prompt-gpt.md` and `dist/system-prompt-deepseek.md`. Each holds the positive writing rules, the five checks, a one-line index of the catalog, and the "For the model" section of the matching profile. Paste the one that fits your model into the system prompt. Rebuild them with `python scripts/build_prompt.py`.

The flat prompt has no taste profile, so taste setup and taste memory do not apply. It also puts the catalog index in the prompt in place of the post-draft catalog review, because a single prompt cannot send the model off to read category files after drafting.

## Taste setup

Run `/tasteful-llm:taste-setup` to build your taste profile in one session. Plugin skills carry the plugin name as a prefix, so the command is namespaced.

1. A silent scan reads your README, CLAUDE.md and docs for existing prose patterns.
2. A mirror shows what it found ("Your sentences tend to be short. You don't hedge.") and you confirm or correct it.
3. Two to four editorial questions follow, such as "When you edit others' writing, what do you always fix?" and "If I wrote something technically flawless but it felt wrong, what would the wrongness be?"
4. An A/B comparison shows two versions of one sentence, both competent, with different voice. You say which you would ship.
5. An opt-in creative philosophy round has three probes. Most probes quote Rubin's *The Creative Act*, and one uses a line from Saint-Exupéry. You answer agree, disagree or complicated, and each answer maps to a behavior change in the skill.
6. The aha moment gives you two versions of a paragraph, one using your emerging profile and one generic, and you pick.
7. A characterization paragraph describes your editorial taste and is saved as your profile.

The profile saves to `~/.tasteful-llm/taste-profile.md` (global) or `.tasteful-llm/taste-profile.md` (project). Project profiles override global ones.

## Model profiles

Models differ in which habits they still have, so `skills/tasteful-output/profiles/` holds one short profile per family. The skill reads the one that matches the model it runs as. Each profile has a "For the model" section, which is what the model reads, and an "Evidence" section with sources, figures and harness notes for the people maintaining prompts.

- [claude.md](skills/tasteful-output/profiles/claude.md) notes that Opus 5.5 nearly dropped the em dash, while contrast pivots, importance flags, recap closers and over-structuring remain.
- [gpt.md](skills/tasteful-output/profiles/gpt.md) notes that GPT models take short, consistent instructions best. GPT-5.x runs long, so the profile stresses outcome-first answers and low verbosity.
- [deepseek.md](skills/tasteful-output/profiles/deepseek.md) gives before/after pairs, because DeepSeek V4 has the highest measured slop of the three. The evidence is thin and the profile says where.

The slop numbers cited come from EQ-Bench, a lexical metric tuned for fiction and essays. It supports a rough ordering of models. It does not measure marketing copy.

## The anti-pattern catalog

52 named patterns across six categories: Language, Structure, Copy, Strategy, Design/UI and Formatting. Three examples:

- L3 Thesaurus Parade: "Streamline, optimize, and revolutionize your workflow." Three verbs that all mean "make better." Fix: "Cut weekly reporting from [N hours] to [N minutes]."
- C1 Everything Headline: "The All-in-One Platform for Modern Teams." It describes every B2B SaaS company that has ever existed. Fix: "Engineering managers: stop writing status reports."
- D4 Friendly Robot Voice: "Whoops! Looks like something didn't go as planned!" Performative personality masks absent information. Fix: "Save failed. Couldn't write to disk. Check permissions."

Each pattern carries one metadata line in the form `Status: <value> · Seen in: <models or "all"> · Verified: <month>`. The status is consistent, rising, fading or unchecked. Unchecked marks an original pattern that was not re-verified in 2026-10. Two vocabulary and punctuation habits are judged by density. L13 Era Vocabulary is flagged at more than 2 era words per 500 words, or 2 in one paragraph. F4 Em-Dash Reflex is flagged at more than 1 em dash per 250 words.

Browse all 52 in [`skills/tasteful-output/anti-pattern-catalog.md`](skills/tasteful-output/anti-pattern-catalog.md)

## When it activates

| Tier | Content types | Gate |
|------|---------------|------|
| Full | Marketing, sales copy, ad copy, case studies, email sequences | All 5 checks (scored out of 5) and the catalog review |
| Reduced | Brand voice, editorial, newsletters, vision statements | Name Swap, Zombie, one more (scored out of 3), plus the catalog review and voice test |
| Craft | Social posts, personal essays, community docs | Voice test only, which is the gate for this tier |

It does not activate for code, debugging, refactoring, data analysis, technical documentation, structured output (JSON/YAML) or git commits.

## Running an audit

> "Audit this landing page copy for slop"
> "Does this README sound like AI?"
> "Check this pitch deck for generic language"

The audit returns per-sentence results against the 5 checks, flags from the 52-pattern catalog, a density report, and a rewrite for each failing sentence.

## Taste memory

TastefulLLM writes a taste profile to `.tasteful-llm/taste-profile.md` in your project. The file has five sections.

- Voice DNA holds sentence length, punctuation habits and tonal stance, extracted from your edits.
- Creative Beliefs holds optional positions about craft from the `/tasteful-llm:taste-setup` calibration. Each belief changes how the skill weighs the checks.
- Learned preferences holds corrections that recur twice or more, promoted to rules.
- Confirmed good holds output you shipped without edits.
- Anti-preferences holds things you reject beyond the standard 52 patterns.

## How loading works

The model classifies the task, reads its model profile, loads your taste profile, and drafts using the positive rules and the five checks. After the draft it reads the catalog as a review pass and fixes what it finds. The catalog holds the long lists of examples, and it loads after drafting so that those phrasings stay out of the first draft.

```
SKILL.md -> classify tier and mode
         -> profiles/<model>.md
         -> taste-profile (global + project merged, if present)
         -> specificity-test.md -> draft
         -> anti-pattern-catalog.md (Full and Reduced tiers) -> self-review
             -> patterns/<category>.md -> terminal file for the matching group
         -> voice-test.md (gate for Craft, second pass for Reduced)
```

## Sources

The rules rest on published measurements and vendor guidance. The main ones:

- Paech et al., Antislop (2025): https://arxiv.org/pdf/2510.15061
- Kobak et al., excess vocabulary in 2024 abstracts: https://arxiv.org/pdf/2406.07016
- Rana (2026), priming by named banned words (one 7B model): https://arxiv.org/abs/2601.08070
- Pangram on Opus 5.5: https://www.pangram.com/blog/can-pangram-detect-opus-5-5
- Graphite on Opus 5.5 tells: https://graphite.io/five-percent/research/ai-tells-opus-5-5-update
- Arize on Claude's writing update: https://arize.com/blog/anthropic-says-it-fixed-claudes-writing/
- textpulse on sentence-length variation: https://textpulse.ai/research/ai-burstiness-sentence-length
- ai-design-tells (202 human-designed sites): https://pypi.org/project/ai-design-tells
- EQ-Bench slop score: https://eqbench.com/slop-score.html
- OpenAI prompt guidance: https://developers.openai.com/api/docs/guides/prompt-guidance?model=gpt-5.5
- Anthropic prompting guidance: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Claude Code skills and plugins: https://code.claude.com/docs/en/skills
- Codex skills: https://learn.chatgpt.com/docs/build-skills

Per-model sources are listed in each profile. Each catalog pattern notes when it was last verified.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT

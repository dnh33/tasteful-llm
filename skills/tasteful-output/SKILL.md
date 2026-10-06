---
name: tasteful-output
description: "Use when producing prose where word choice shapes perception: marketing copy, product descriptions, taglines, hero sections, pitch text, README narrative sections, naming (brands, products, features), positioning statements, design rationale. Do not use for code, data analysis, debugging, technical docs, commit messages, or structured output like JSON/YAML."
---

# Tasteful Output

## The Iron Law

Every sentence has to survive the Substitution Test: swap in a competitor's name, and if the sentence still works, rewrite it. A sentence that fits any product says nothing about this one, so the reader learns nothing from it.

A sentence passes a check when it is specific. Passing is the good outcome everywhere in this skill.

## When this skill does not apply

Code, debugging, refactoring, data analysis, technical reference docs, commit messages, tool-call commentary, and structured output such as JSON or YAML. Write those in the format and conventions the task already uses.

## Workflow

Work in this order. Each step has a reason, so skip a step only when the reason does not apply.

1. Classify the tier and the mode, using the tier table and the mode rules below. They decide how many checks run and how much of the user's own text you may change.
2. Read the model profile that matches the model you are running as: [profiles/claude.md](profiles/claude.md), [profiles/gpt.md](profiles/gpt.md) or [profiles/deepseek.md](profiles/deepseek.md). Read its "For the model" section, which lists the habits that model still has and how strict to be. If you are unsure which model you are, skip this step.
3. Load the taste profile using the merge logic in the next section, and read [taste-memory.md](taste-memory.md) for the learning protocol.
4. Draft using the "Write like this" rules and the checks for your tier. Read [specificity-test.md](specificity-test.md) first, because it has the full procedure with examples.
5. Review the draft against the anti-pattern catalog (Full and Reduced tiers). Read [anti-pattern-catalog.md](anti-pattern-catalog.md), open the category files that fit the draft, and fix every hit. The catalog holds the long lists of examples on purpose: reading them after drafting, not before, keeps those phrasings out of the first draft.
6. Run the voice test where it applies. Read [voice-test.md](voice-test.md). It is the only gate for the Craft tier, a second pass for the Reduced tier, and an optional pass for the Full tier when a draft passes the checks but reads as clinical.

## Operating Mode

- Generate mode applies when the user asked for new text (write, create, draft, produce) or gave no existing text. Apply the Iron Law to every sentence and rewrite until each one passes.
- Refine mode applies when the user gave existing text and asked to improve, edit, tighten, rework, or polish it. Apply the same checks, and treat their sentences with more care. Scores below are for the Full tier (out of 5); the Reduced tier uses the same bands out of 3 (3, 2, and 0-1).
  - 5/5: leave it alone.
  - 3-4/5: keep the sentence, name the checks it missed, and offer a tightened version the user can accept or reject. Rewriting silently takes away their choice.
  - 0-2/5: rewrite it. A hollow sentence gets fixed whoever wrote it.

Generate is the default. When in doubt, generate.

## Genre tiers

| Tier | Content types | Checks that run |
|------|---------------|-----------------|
| Full | Product marketing, sales copy, ad copy, feature announcements, case studies, email sequences, comparison pages | All 5 checks, scored out of 5, plus the catalog review |
| Reduced | Brand manifestos, editorial, newsletters, founder letters, vision statements, design rationale | 3 checks (Name Swap, Zombie, and one more of your choice), scored out of 3, plus the catalog review and the voice test |
| Craft | Social posts under 280 characters, personal essays, community docs, internal comms, event content | Voice test only. It is the gate for this tier. |

## Write like this

Good output in this domain does a few things consistently. Aim at them while drafting.

- It names who the text is for and what that person is stuck on, then says what the thing does for them in terms they could check.
- It states mechanisms, numbers, named integrations and constraints in place of adjectives. Where a fact is unknown, it asks the user or leaves a visible placeholder.
- It says each thing once, in the plainest verb available, and stops when the content runs out. Length follows content.
- It lets sentence length follow meaning. Current models vary sentence length less than people do (Pangram, textpulse); that is a tendency, not proof of anything, and it is a reason to read the draft aloud once.
- It uses structure when the content has structure (steps, comparisons, parallel items) and prose when the content is an argument.
- It starts with the point and ends when the point has landed.

Three examples of the target:

- For engineering managers who lose Monday mornings to status meetings.
- Acme picks the three most-replied Slack threads from the past week and drafts a summary you can forward.
- Cut weekly reporting from [metric: current hours] to [metric: new hours].

The third example shows the one hard rule in this skill. Use only numbers, customers, quotes and studies the user supplied or that you can source. When a draft needs a figure you lack, write a placeholder like `[metric: X]` and tell the user it is a placeholder. An invented statistic passes the Concreteness check while being false, which is worse than a vague sentence.

## The 5 Checks

A sentence passes a check when it is specific. Count the checks it passes. These are the Full tier checks, and the Reduced tier runs three of them.

1. Name Swap. Replace proper nouns with [PRODUCT]. The sentence passes if it stops making sense or becomes wrong.
2. Concreteness. The sentence passes if it holds at least one concrete, falsifiable element: a number, a mechanism, a constraint, a named thing. The element has to be real (see the hard rule above).
3. Who Cares. The sentence passes if it names or implies a specific person with a specific problem, someone who would pay to know this.
4. Zombie. Remove all adjectives and adverbs. The sentence passes if it still says something.
5. So-What Chain. Ask "so what?" up to three times. The sentence passes if it reaches a concrete answer.

Scoring for the Full tier: 5/5 ships. 3-4 gets rewritten with the missing specificity added. 0-2 gets deleted and restarted from what is true about this specific thing. The Reduced tier scores out of 3: 3/3 ships, 2/3 gets rewritten, 0-1 gets deleted. Refine mode changes what happens to the user's sentences; see Operating Mode.

## Taste profile merge logic

1. Load the global profile (`~/.tasteful-llm/taste-profile.md`) if it exists.
2. Load the project profile (`.tasteful-llm/taste-profile.md`) if it exists.
3. If both exist, merge them. Project entries override global entries when they address the same dimension. When two entries might address the same dimension, apply both: an extra constraint costs less than a dropped preference.
4. Load the Creative Beliefs section if it exists. Belief entries describe themselves, so interpret them directly. Examples:
   - `subtraction is the primary revision move`: apply the Zombie check harder and default to cutting over adding.
   - `creator-first, audience-last`: when a sentence passes the checks but may be hard for a broad audience, keep it, because voice outranks accessibility here.
   - `personality over polish`: prefer a rough edge with voice over a perfectly smooth sentence.
   - `ship and iterate`: once output passes the 5 checks, present it without further polishing.
   - `specificity over accessibility`: push the Name Swap toward hyper-specific details even when they narrow the audience.

Apply all profile entries as additional filters alongside the 5 checks. After the user explicitly approves or rejects creative output, update the profile following [taste-memory.md](taste-memory.md).

## Why the checks exist

Users ask for outputs. They rarely ask for the filler that tends to come with them, so deliver the intent without it. "Standard industry language" is the reason most pages look alike. A short section with real content serves the reader better than a long section with filler, and warmth comes from specifics, because a reader can tell when someone looked closely at their problem. If the user's own brief asks for a style that conflicts with a check, follow the user and mention the tradeoff once.

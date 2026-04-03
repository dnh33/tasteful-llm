# v0.3.0 Design Spec: `/taste-setup` — Taste Onboarding

> The pipeline is the commodity. The editorial filter is the moat.

## Problem

TastefulLLM v0.2.0 learns taste passively over sessions. But the profile starts empty. It takes ~20 sessions of approvals and rejections before the profile is rich enough to meaningfully shape output. This is the cold-start problem.

## Solution

A `/taste-setup` slash command that generates a foundational taste profile through a guided calibration session. Not a form. Not a quiz. A session where the system demonstrates comprehension of the user's taste in real time.

The design principle, from Rick Rubin: taste is demonstrated, not described. The system reads first, asks second, and proves understanding before it finishes.

## Design Philosophy

Three things make this different from every other "writing style" tool:

1. **It reads your work before asking you anything.** Every other tool starts with a form. This one starts with "here's what I already see in you."
2. **It proves comprehension mid-flow.** The system generates output using the emerging profile and asks the user to validate — collapsing the gap between "onboarding" and "product value" to zero.
3. **It can go philosophically deep (opt-in).** For people who care about craft, Rubin-derived calibration probes open a door no other developer tool acknowledges.

---

## The Flow

### Preamble: Entry Check + Scope (1 interaction)

Immediately after `/taste-setup` is invoked, before any scanning:

**Step 1: Check for existing profiles.** Read `~/.tasteful-llm/taste-profile.md` and `.tasteful-llm/taste-profile.md`.

If either exists:
```
Found existing taste profile with N entries 
(M from setup, K from observation).

  [1] Refine — update setup entries, preserve observed entries
  [2] Fresh start — archive current profile, create new
```

If neither exists: proceed directly to scope question.

**Step 2: Scope question.**
```
Should this profile apply globally (your default voice 
across all projects) or just to this project?

  [1] Global (recommended for first setup)
  [2] This project only
```

Store the target path for use in Phase 4. If they choose global and a project profile also exists, note that project profiles override global — they may want to consolidate.

Then proceed to Phase 0.

### Phase 0: Silent Scan (0 user effort)

Scan the project for existing prose:
- README.md
- CLAUDE.md / AGENTS.md
- package.json `description` field
- Any `.md` files in root or `/docs`
- Marketing copy, About pages, blog posts if present

Read the prose and assess (qualitatively — the LLM is estimating, not computing):
- Sentence length tendency (short/medium/long, with rough word counts)
- Vocabulary register (technical, conversational, literary, mixed)
- Anti-pattern presence — scan for patterns from the catalog
- Substitution Test spot-checks on representative sentences
- Structural patterns: paragraph length, list usage, heading style, transition patterns
- Notable absences: hedging language? Adjective density? Em dashes?

**Important:** These are LLM observations, not computed metrics. Present findings as qualitative observations backed by quoted evidence, not as precise statistics. "Your sentences tend to be short — most are under 12 words" rather than "Your sentences average 11.3 words." Precision that can't be verified undermines the mirror moment.

If nothing found (empty repo, code-only project): skip to Phase 1b.

### Phase 1: The Mirror (1 interaction)

**Phase 1a — If scan found prose:**

Present 4-5 specific observations with evidence:

```
Based on your project, here's what I see in your writing:

- Your sentences are short — mostly under 12 words. You rarely 
  compound past a semicolon.
- You lead with imperative verbs: "Run", "Install", "Check". 
  I didn't find any instances of "It's worth noting" or 
  "Let's take a look at."
- Your README is unusually specific. Most sentences contain a 
  concrete, falsifiable claim — like "39 anti-patterns across 
  5 categories" rather than "comprehensive pattern coverage."
- You don't hedge. I couldn't find "might", "perhaps", or 
  "arguably" anywhere in your prose.
- One thing I can't tell from scanning: whether this terseness 
  is deliberate taste or just README convention.

Does this feel like you? Or is this project not representative 
of how you actually write?
```

User confirms, corrects, or says "that's not representative."

If not representative: "Paste something that IS you — an email, a Slack message, a paragraph you're satisfied with." Analyze that instead and re-mirror.

**Phase 1b — If no prose found:**

```
No existing prose to analyze in this project. 

Paste something you've written that you're satisfied with — 
an email, a README, a message, anything. Not your best work. 
Something that felt natural.
```

Analyze the sample. Extract the same patterns. Mirror findings back. Proceed to Phase 2.

### Phase 2: Editorial Values (2-4 adaptive questions)

These probe dimensions the scan can't determine. Ask only what's needed — skip questions where Phase 1 provided clear signal. One question per turn. Wait for answer before proceeding.

**Q1: The Editorial Instinct** (always ask)
```
When you edit other people's writing, what's the one thing 
you always fix?
```
This is the single most efficient taste question. Whatever they always fix is what they care about most. Maps to: dominant editorial value in Voice DNA.

**Q2: The Taste Boundary** (always ask)
```
If I wrote something for you that was technically flawless 
but still felt wrong — what would the wrongness be?
```
Maps the gap between competent and personal. Reveals the ineffable "not me" signal. Maps to: Anti-Preferences with reasoning.

**Q3: A/B Comparison** (ask if Phase 1 left ambiguity on a key dimension)

Select ONE pair based on the specific gap. Not good-vs-bad. Two options that both pass all 5 checks but differ in disposition:

| Gap to resolve | Pair |
|---|---|
| Density preference | "Paste a URL. Get a summary. Share it in Slack. That's it." vs. "We built a summarizer that respects your time — paste any URL, and within seconds you'll have a clean, shareable summary your team can act on." |
| Authority posture | "TastefulLLM eliminates AI slop. 39 anti-patterns. One sentence survives or it doesn't." vs. "Most AI writing advice is 'use more detail.' That's necessary but insufficient. TastefulLLM tries to encode the part that's harder to teach." |
| Warmth-precision axis | "Hey — just wanted to make sure you found the dashboard. Here's the one thing most people miss: keyboard shortcuts (Cmd+K)." vs. "Your account is active. Three things to configure: API key, webhook endpoint, deployment target." |
| Friction tolerance | "Your backlog is lying to you." vs. "Project management for teams that ship weekly." |
| Ornament ethics | Pure mechanism description vs. mechanism with earned poetic moment |

Ask: "Which would you ship? And — briefly — why?"

The "why" is where the taste lives. The choice alone is just a click.

**Q4: The Anti-Preference** (ask if wince/rejection data is thin)
```
What writing pattern do you specifically reject — 
and why does it bother you?

Not just "I don't like corporate speak." WHY does it bother you? 
What does it signal to you when you see it?
```
The specificity of the rejection maps the conviction. "It signals the writer doesn't respect the reader's time" is a different editorial value than "It signals the writer is hiding behind language."

**Adaptive logic:**
- Q1 and Q2 are always asked — they probe internal editorial values that scanning cannot determine
- If the user's corrections in Phase 1 already revealed what they reject → skip Q4
- If Phase 1 resolved the key taste dimensions (density, authority, warmth) → skip Q3
- Minimum Phase 2: 2 questions (Q1 + Q2). Maximum: 4 questions (Q1-Q4)

**What "resolved" means:** A dimension is resolved when Phase 1 produced a clear, consistent signal with evidence. Examples:
- *Density resolved:* All scanned sentences are under 15 words, no compound sentences, and user confirmed "yes, that's me." No need to show the density A/B pair.
- *Authority resolved:* User's prose consistently uses imperative voice with no hedging, and user didn't push back on the mirror observation about it.
- *Density NOT resolved:* Scanned prose has mixed sentence lengths (some short, some long), or user said "that's just my README, I write differently elsewhere." Show the density pair to disambiguate.

### Phase 2b: Creative Beliefs (opt-in, 2-3 extra questions)

After the core editorial questions, before Phase 3:

```
One more option: I can ask 3 questions about your creative 
philosophy — not style preferences, but what you believe about 
craft itself. This produces a richer profile.

Want that layer? Takes about 2 extra minutes.
[yes / no]
```

If yes, select 3 probes from the Rubin calibration pool (see `rubin-calibration.md`). Choose probes that resolve dimensions not yet covered. Each probe is a proposition with three response paths:

Example:
```
Rick Rubin: "The objective is not to learn to mimic greatness, 
but to calibrate our internal meter for greatness."

Is your goal to match a specific reference voice, or to develop 
your own sense of what's good?
```

Each answer maps to a belief entry in the Creative Beliefs section. Beliefs are load-bearing — they change how the skill operates (see Profile Structure below).

If no: skip. Profile works without this section.

### Phase 3: The Aha Moment (1 interaction)

After accumulating enough signal (Phase 1 + 2-3 answers from Phase 2), generate two versions of a short paragraph:
- **Version A:** Written using the user's emerging preferences
- **Version B:** Written using generic/default style

Topic selection:
- If Phase 0 found a README, rewrite a sentence from it
- If the user pasted a sample, rephrase part of it
- If neither, use a neutral scenario relevant to their stated context

```
Based on what I've learned, here's the same idea written two ways:

[A] Something went wrong during deployment. The webhook didn't 
    fire. Check the endpoint URL in Settings > Webhooks.

[B] It looks like there may have been an issue with the 
    deployment process. You might want to take a look at your 
    webhook configuration to ensure everything is set up correctly.

Which sounds more like how you'd say it?
```

This serves two purposes:
1. **Calibration** — validates or corrects the emerging model
2. **Product demo** — the user sees the system already understands them

If the user picks neither and explains what they'd actually write, that override is the highest-signal data point in the entire session.

### Phase 4: The Characterization (1 interaction)

Write the profile as a prose characterization — a short paragraph that reads like a thoughtful editor describing the user's voice:

```
Here's what I've learned about your editorial taste:

You write like someone who respects the reader's time above 
all else. No hedging, no throat-clearing, no "it's important 
to note that." You want density — every sentence carrying weight. 
Short paragraphs, active voice, imperative verbs. But you're 
not dogmatic; you'll let a sentence breathe when the idea 
demands it.

You have zero tolerance for vague authority claims and strong 
opinions about earned specificity. You'd rather be too blunt 
than too safe. When you edit others, you cut the setup and 
start where the information starts.

[If Creative Beliefs opted in:]
You believe taste is calibrated, not copied — you want to 
develop your own editorial instinct, not mimic a reference. 
You lean toward subtraction as the primary revision move.

Profile saved to ~/.tasteful-llm/taste-profile.md
This shapes everything I write from here on.
Want to adjust anything? (You can run /taste-setup again 
anytime, or the profile will refine itself as you use 
tasteful-output.)
```

User confirms or adjusts. Save the profile.

**This characterization is the marketing moment.** If someone screenshots anything, it's this. It needs to feel like recognition — specific, sharp, and true. Not a horoscope.

---

## Profile Structure

### What the questionnaire writes

| Section | Written by setup? | Content |
|---|---|---|
| Voice DNA | Yes | Extracted patterns + confirmed preferences |
| Creative Beliefs | Yes (opt-in) | Philosophical positions from Rubin probes |
| Learned Preferences | No | Grows only from passive observation (2+ occurrences) |
| Confirmed Good | No | Grows only when real output is approved |
| Anti-Preferences | Yes | Stated rejections with reasoning |

### Source tags

Every entry carries provenance:

```markdown
## Voice DNA
- Short sentences, verb-forward. Dry register. Rarely compounds past a semicolon. [setup:2026-04-03]
- Ends sections with one-line kickers for emphasis. [observed:2026-04-15]

## Creative Beliefs
- Taste is calibrated, not copied. Develop internal meter, don't match references. [setup:2026-04-03]
- Subtraction is the primary revision move. [setup:2026-04-03]

## Learned Preferences
<!-- Grows through use. 2+ occurrences required to promote. -->

## Confirmed Good
<!-- Output shipped without edits. Evidence of "right." -->

## Anti-Preferences
- Hedging language ("might", "perhaps", "arguably") — signals the writer doesn't trust their own claim. [setup:2026-04-03]
- Setup sentences before information ("It's worth noting that...") — disrespects reader's time. [setup:2026-04-03]
```

### Word budget

| Source | Budget | Rationale |
|---|---|---|
| Setup (Voice DNA + Anti-Preferences) | 150 words | Bootstrap, not ground truth |
| Setup (Creative Beliefs) | 100 words | Opt-in philosophical layer |
| Passive learning | 250 words | Higher fidelity, earned through use |
| **Total** | **500 words** | Unchanged from v0.2.0 |

### Override rule

When a passively-learned observation contradicts a setup entry, the observation wins. The setup entry gets pruned. The profile converges toward demonstrated reality, not self-image.

### Version marker

```markdown
<!-- tasteful-llm-profile:v2 -->
# Taste Profile
```

v1 = pre-questionnaire (v0.2.0). v2 = with setup entries and optional Creative Beliefs (v0.3.0). Enables future migration when v0.4.0 adds Voice Calibration section.

---

## Scope: Project vs. Global

**Default: global** (`~/.tasteful-llm/taste-profile.md`).

The questionnaire asks about YOU — your taste, your voice, your editorial values. These are not project-specific.

**Project profiles** (`.tasteful-llm/taste-profile.md`) contain only deltas — things that differ from your global voice for this specific project. Example: your global voice is dry and terse, but this project is a children's product where you want warmer, longer sentences.

### Loading logic (update to tasteful-output SKILL.md)

```
1. Load global profile (~/.tasteful-llm/taste-profile.md) if exists
2. Load project profile (.tasteful-llm/taste-profile.md) if exists
3. Project entries override global entries for the same dimension
```

---

## Re-running /taste-setup

When an existing profile is detected:

```
Found existing taste profile:
  - 4 setup entries (from 2026-04-03)
  - 7 observed entries (accumulated over 12 sessions)

  [1] Refine — update setup entries, preserve observed entries
  [2] Fresh start — archive current profile, create new
```

- **Refine** overwrites `[setup:*]` entries, keeps `[observed:*]` untouched. Future `[calibration:*]` entries (v0.4.0) will also be preserved.
- **Fresh start** renames current to `taste-profile.YYYY-MM-DD.bak.md`, creates new
- Never silently destroys observed entries
- **Re-run conflict priority:** A new `[setup:*]` entry from re-running does NOT override an existing `[observed:*]` entry. Observations always win, even over fresh setup. If the user explicitly says "I know I used to do X but I want to change to Y," record it as a new setup entry — but note the conflict in the profile so the learning system knows to watch for whether the change sticks.

---

## Skill Architecture

```
skills/taste-setup/
├── SKILL.md               ← Frontmatter + full flow as phased state machine
└── rubin-calibration.md   ← 8 Rubin probes with response mappings (3 used per session)
```

### SKILL.md Frontmatter

```yaml
---
name: taste-setup
description: "Run a guided taste calibration session that builds a foundational 
taste profile. Use when the user says '/taste-setup', 'set up my taste profile', 
'configure tasteful', 'create taste profile', or when no taste profile exists 
and the user wants to establish one."
---
```

### Execution model

The SKILL.md contains explicit phased instructions. The LLM tracks state via conversation context. Key behavioral anchors:

- **One question per turn.** Never batch questions.
- **Wait for answer before proceeding.** Do not anticipate responses.
- **Adaptive branching.** Skip questions where prior phases provided clear signal.
- **Phase transitions are explicit.** "Moving to Phase 2" isn't said to the user, but the skill tracks internally.

### Integration with existing skills

#### 1. `taste-profile-template.md` — updated template

Replace the current template with:

```markdown
<!-- tasteful-llm-profile:v2 -->
# Taste Profile

This file is maintained by TastefulLLM. It learns your taste over sessions.

## Voice DNA
<!-- Patterns in how you write and what you prefer -->

## Creative Beliefs
<!-- Optional: philosophical positions about craft. Generated by /taste-setup with Rubin calibration. -->

## Learned Preferences  
<!-- Recurring corrections and confirmed choices -->

## Confirmed Good
<!-- Output you shipped without edits — what "right" looks like for you -->

## Anti-Preferences
<!-- Things you specifically reject that aren't in the standard catalog -->
```

Creative Beliefs section is always present in the template (with placeholder comment). If the user didn't opt into Rubin calibration, it stays empty — that's fine.

#### 2. `taste-memory.md` — additions

Add the following to the "Reading the Profile" section:

```markdown
## Entry Provenance

Profile entries carry source tags: `[setup:date]` for questionnaire-generated 
entries, `[observed:date]` for passively-learned entries.

When reading the profile, treat both equally — apply all entries as constraints 
regardless of source.

When WRITING to the profile, apply the override rule: if a new observed 
preference contradicts an existing `[setup:*]` entry on the same dimension, 
the observation replaces the setup entry. The profile converges toward 
demonstrated reality over self-report.

A "contradiction on the same dimension" means: the entries make opposing 
claims about the same aspect of writing. Example: setup says "short sentences, 
verb-forward" but observations consistently show the user approving 
medium-length sentences with dependent clauses. The observation wins.
```

#### 3. `tasteful-output/SKILL.md` — loading logic update

Replace the existing loading line:

```
Load the user's taste profile (.tasteful-llm/taste-profile.md) if it exists. 
Apply learned preferences as additional filters alongside the 5 checks.
```

With:

```
Load the taste profile using the following merge logic:

1. Load global profile (~/.tasteful-llm/taste-profile.md) if it exists
2. Load project profile (.tasteful-llm/taste-profile.md) if it exists
3. If both exist, merge: project entries override global entries when they 
   address the same dimension. All other entries from both profiles apply.
4. Load the Creative Beliefs section if it exists. Apply beliefs as editorial 
   stance constraints — they modify how aggressively specific checks are 
   applied (see the behavioral mappings in rubin-calibration.md).

Apply all profile entries as additional filters alongside the 5 checks.
```

#### 4. `anti-slop-audit/SKILL.md` — note

The `anti-slop-audit` skill audits existing text for slop patterns. It does NOT currently load the taste profile, and this spec does not change that. The taste profile is for generation-time filtering (`tasteful-output`), not for auditing existing text. A future version could optionally load the profile to calibrate audit severity, but that is out of scope for v0.3.0.

---

## Rubin Calibration Pool

Eight probes, 3 selected per session based on unresolved dimensions:

| # | Proposition | What it resolves |
|---|---|---|
| 1 | "The objective is not to learn to mimic greatness, but to calibrate our internal meter for greatness." | Reference matching vs. internal calibration |
| 2 | "Perfection is obtained not when there is no longer anything to add, but when there's no longer anything to take away." | Additive vs. subtractive revision instinct |
| 3 | "In terms of priority, inspiration comes first. You come next. The audience comes last." | Creator-first vs. audience-first orientation |
| 4 | "Does it amplify the essence? Does it distract from the essence? Is it absolutely necessary?" | Sentence-level vs. piece-level editorial thinking |
| 5 | "You can doubt your way to excellence." | Ship-fast vs. refine-until-right perfectionism threshold |
| 6 | "To purposely experiment past the boundaries of your taste." | Exploration vs. consistency in profile application |
| 7 | "Flaws are human, and the attraction of art is the humanity held in it." | Polish vs. personality tolerance |
| 8 | "The personal is the universal." | Specificity vs. accessibility in the Substitution Test |

Each probe has three response paths (agree / disagree / complicated) that map to a specific belief entry. The belief entry changes how `tasteful-output` operates:

### Response Paths and Behavioral Mappings

**Probe 1: Internal Meter**
- **Agree** → `belief: calibrate, don't copy` → When using reference anchors from the profile, treat them as compass points, not templates. Never mimic a reference voice literally.
- **Disagree** → `belief: match the reference` → When a reference anchor is in the profile, actively match its patterns (sentence length, register, structure).
- **Complicated** → `belief: calibrate with reference awareness` → Use references to inform direction but flag when output drifts too close to imitation.

**Probe 2: Subtractive Perfection**
- **Agree** → `belief: subtraction is the primary revision move` → Apply Zombie Test more aggressively. When rewriting, default to cutting rather than adding. Flag sentences that add information without adding meaning.
- **Disagree** → `belief: addition strengthens work` → When a sentence fails the Concreteness Test, prefer adding a specific detail over cutting the sentence entirely.
- **Complicated** → `belief: context-dependent revision` → No default direction. Apply whichever move (cut or add) the specific sentence needs.

**Probe 3: Priority Hierarchy**
- **Agree** → `belief: creator-first, audience-last` → When a sentence passes the checks but might be inaccessible to a broad audience, keep it. Specificity and voice take priority over accessibility.
- **Disagree** → `belief: audience-first` → When applying the Who Cares check, weight audience comprehension heavily. Avoid insider language even if it's more precise.
- **Complicated** → `belief: audience is a live tension` → Flag audience-accessibility tradeoffs to the user rather than resolving them silently.

**Probe 4: Essence Filter**
- **Agree** → `belief: sentence-level editorial thinking` → Every sentence must independently pass the 5 checks. Kill lines that serve flow but carry no information.
- **Disagree** → `belief: piece-level editorial thinking` → A weak sentence that serves the overall arc is acceptable. Evaluate paragraphs and sections holistically, not sentence by sentence.
- **Complicated** → `belief: both levels matter` → Apply checks at sentence level but allow exceptions when the piece-level argument requires it. Note the exception.

**Probe 5: Doubt as Tool**
- **Agree** → `belief: refine until right` → When output passes the 5 checks, still ask "can this be sharper?" Apply an additional self-review pass before presenting.
- **Disagree** → `belief: ship and iterate` → Once output passes the 5 checks, present it. Don't over-polish. Speed of delivery matters.
- **Complicated** → `belief: doubt the work, not the process` → One revision pass after checks pass. No more.

**Probe 6: Boundary Experimentation**
- **Agree** → `belief: push past comfortable taste` → Occasionally (1 in 5 outputs) include a variant that breaks the user's established pattern — a sentence structure they don't usually use, a register shift. Flag it: "This one stretches your usual range."
- **Disagree** → `belief: stay within established taste` → Never deviate from the profile. Consistency is the goal.
- **Complicated** → `belief: experiment when invited` → Only push boundaries when the user explicitly asks for something different or when the task is explicitly creative/experimental.

**Probe 7: Flaws as Humanity**
- **Agree** → `belief: personality over polish` → When choosing between a perfectly smooth sentence and one with a slight rough edge that adds voice (a sentence fragment, an unexpected word choice), prefer the rough edge.
- **Disagree** → `belief: polish is professionalism` → Smooth every rough edge. Consistent quality signals competence. No deliberate imperfections.
- **Complicated** → `belief: context-dependent polish` → Polish for professional/external content. Allow rough edges for internal/personal content.

**Probe 8: Personal is Universal**
- **Agree** → `belief: specificity over accessibility` → In the Substitution Test, push for hyper-specific details even if they narrow the audience. A sentence that's true for 100 people is better than one that's vaguely true for 10,000.
- **Disagree** → `belief: accessibility over specificity` → In the Substitution Test, ensure specific claims are still accessible to a general audience. Don't require insider knowledge to understand the point.
- **Complicated** → `belief: specific with context bridges` → Be specific, but include enough framing that an outsider can follow. The specificity is the payload; the bridge is the delivery.

---

## A/B Comparison Pair Library

Available pairs for Phase 2, Q3. One is selected based on the specific ambiguity to resolve:

| Dimension | Option A | Option B |
|---|---|---|
| **Density** | "Paste a URL. Get a summary. Share it in Slack. That's it." | "We built a summarizer that respects your time — paste any URL, and within seconds you'll have a clean, shareable summary your team can act on." |
| **Authority** | "TastefulLLM eliminates AI slop. 39 anti-patterns. One sentence survives or it doesn't." | "Most AI writing advice is 'use more detail.' That's necessary but insufficient. TastefulLLM tries to encode the part that's harder to teach." |
| **Warmth-Precision** | "Hey — just wanted to make sure you found the dashboard. Here's the one thing most people miss: keyboard shortcuts (Cmd+K)." | "Your account is active. Three things to configure: API key, webhook endpoint, deployment target." |
| **Friction** | "Your backlog is lying to you." | "Project management for teams that ship weekly." |
| **Ornament** | "Database backups that run every 60 seconds, restore in under 90, and never require you to think about them." | "Quietly relentless database backups. Every 60 seconds. Restore in 90. The infrastructure you forget about because it never gives you a reason to remember." |

The pair library can grow over time. Content types beyond SaaS should be added for users working in editorial, documentation, or creative contexts.

---

## Interaction Budget

Preamble (scope + existing profile check) counts as 1 interaction in all scenarios.

| Scenario | Phases | Total interactions | Time |
|---|---|---|---|
| Rich project, no Rubin | Pre(1) + 0 + 1(1) + 2(2 Qs) + 3(1) + 4(1) | 6 | ~4 min |
| Rich project, with Rubin | Pre(1) + 0 + 1(1) + 2(2 Qs) + 2b(3Qs) + 3(1) + 4(1) | 9 | ~6 min |
| Empty project, no Rubin | Pre(1) + 1b(1) + mirror(1) + 2(4 Qs) + 3(1) + 4(1) | 9 | ~6 min |
| Empty project, with Rubin | Pre(1) + 1b(1) + mirror(1) + 2(4 Qs) + 2b(3Qs) + 3(1) + 4(1) | 12 | ~8 min |

Maximum: 12 interactions, ~8 minutes. Minimum: 6 interactions, ~4 minutes.

---

## Failure Modes and Mitigations

| Failure | Mitigation |
|---|---|
| **Aspiration trap** — user describes taste they wish they had | Behavioral questions (editing, comparison) over declarative. Phase 0 scan reveals what they actually do. |
| **Social desirability** — user over-indexes on sounding sophisticated | Frame as discovery, not evaluation. Never use "better/best/ideal." Use "which pulls you in" / "which sounds like you." |
| **Context collapse** — answers based on one context, used in another | Phase 1 scope question. Pairs calibrated to user's stated context. |
| **Low engagement** — "either is fine" to everything | After 2+ low-signal answers, switch to aversion elicitation: "Forget what you like — what makes you cringe?" |
| **Vocabulary mismatch** — user doesn't know "register" or "cadence" | Never use craft terminology in questions. Show concrete examples, use plain language. |
| **Contradiction in answers** | Treat as signal, not error. Synthesize into higher-order pattern: "You prefer restraint in description but richness in openings — that's controlled contrast." |
| **Empty scan + no sample** | Offer to generate a neutral paragraph and ask them to edit it. Their edits reveal editorial instinct. |
| **Mid-flow abandonment** — user exits before Phase 4 | Save nothing. A partial profile with incomplete data is worse than no profile — it creates false confidence in the learning system. The user can re-run `/taste-setup` when ready. If they completed Phase 1 and Phase 2 but stopped before the characterization, acknowledge: "No profile saved. Run /taste-setup again when you're ready." |

---

## What This Enables

After `/taste-setup`, the user's next invocation of `tasteful-output` loads a profile that shapes output from the first sentence. The 20-session cold start is eliminated.

The profile grows from there:
- v0.2.0 passive learning refines and extends the questionnaire's foundation
- v0.4.0 voice calibration adds quantitative data from writing samples
- The questionnaire entries gradually get displaced by higher-fidelity observations

The system converges toward the user's real taste, starting from a strong initial position rather than zero.

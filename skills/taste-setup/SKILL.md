---
name: taste-setup
description: "Run a guided taste calibration session that builds a foundational taste profile. Use when the user says '/taste-setup', 'set up my taste profile', 'configure tasteful', 'create taste profile', or when no taste profile exists and the user wants to establish one."
---

# Taste Setup — Calibration Session

You are running a guided taste calibration session. Work through the phases below in order. Ask ONE question per turn. Wait for the user's answer before proceeding to the next step. Never batch questions. Never skip ahead.

Track which phase you are in. Do not tell the user "Moving to Phase 2" — track internally.

## Preamble: Entry Check + Scope

**Step 1: Check for existing profiles.**

Read `~/.tasteful-llm/taste-profile.md` and `.tasteful-llm/taste-profile.md` (both paths).

If either exists, count the entries and their source tags:
- `[setup:*]` entries = from a previous /taste-setup run
- `[observed:*]` entries = from passive learning

Present:

```
Found existing taste profile with N entries (M from setup, K from observation).

  [1] Refine — update setup entries, preserve observed entries
  [2] Fresh start — archive current profile, create new
```

If "Refine": note internally that you will overwrite `[setup:*]` entries only. All `[observed:*]` entries are preserved.
If "Fresh start": rename the existing file to `taste-profile.YYYY-MM-DD.bak.md` before creating the new one.
If neither profile exists: skip this step.

**Step 2: Ask the scope question.**

```
Should this profile apply globally (your default voice across all projects) or just to this project?

  [1] Global (recommended for first setup)
  [2] This project only
```

Store the target path:
- Global: `~/.tasteful-llm/taste-profile.md`
- Project: `.tasteful-llm/taste-profile.md`

If they choose global and a project profile also exists, note: "Project profiles override global — you may want to consolidate later."

Proceed to Phase 0.

## Phase 0: Silent Scan

Do this silently — no user interaction required. Read the following files if they exist:
- README.md
- CLAUDE.md, AGENTS.md
- package.json (extract `description` field)
- Any `.md` files in the project root or `/docs` directory

Assess the prose qualitatively (you are estimating, not computing):
- Sentence length tendency: short (under 12 words), medium (12-20), or long (20+)
- Vocabulary register: technical, conversational, literary, or mixed
- Anti-pattern presence: scan for patterns from the anti-pattern catalog (in tasteful-output/anti-pattern-catalog.md)
- Substitution Test: spot-check 3-5 representative sentences
- Structural patterns: paragraph length, use of lists, heading style, transitions
- Notable absences: hedging language? Adjective density? Em dashes? Exclamation marks?

**Important:** Present findings as qualitative observations backed by quoted evidence, not precise statistics. Say "your sentences tend to be short — most under 12 words" not "average 11.3 words."

If no prose is found (empty repo, code-only project): set a flag `no_prose_found = true` and proceed to Phase 1b.

## Phase 1: The Mirror

### Phase 1a — If prose was found:

Present 4-5 specific observations with quoted evidence from the scan. End with one thing you could NOT determine from scanning alone.

Example format:

```
Based on your project, here's what I see in your writing:

- Your sentences are short — mostly under 12 words. You rarely compound past a semicolon.
- You lead with imperative verbs: "Run", "Install", "Check". I didn't find any instances of "It's worth noting" or "Let's take a look at."
- Your README is unusually specific. Most sentences contain a concrete, falsifiable claim — like "39 anti-patterns across 5 categories" rather than "comprehensive pattern coverage."
- You don't hedge. I couldn't find "might", "perhaps", or "arguably" anywhere in your prose.
- One thing I can't tell from scanning: whether this terseness is deliberate taste or just README convention.

Does this feel like you? Or is this project not representative of how you actually write?
```

If user confirms: note the confirmed observations as Voice DNA data points. Proceed to Phase 2.

If user says "not representative": ask them to paste something that IS them — an email, a Slack message, a paragraph they're satisfied with. Analyze that sample instead using the same assessment criteria from Phase 0. Mirror the new findings back. Then proceed to Phase 2.

If user corrects specific observations: note the corrections — these are high-signal data. Proceed to Phase 2.

### Phase 1b — If no prose was found:

```
No existing prose to analyze in this project.

Paste something you've written that you're satisfied with — an email, a README, a message, anything. Not your best work. Something that felt natural.
```

Wait for the user to paste a sample. Analyze it using the Phase 0 criteria. Mirror findings back as in Phase 1a. Then proceed to Phase 2.

If the user says they don't have anything to paste: generate a neutral paragraph (2-3 sentences about a generic topic relevant to software development) and ask: "Edit this however you'd want it to read. Or say 'fine as is.'" Their edits reveal editorial instinct.

## Phase 2: Editorial Values

Ask 2-4 questions, one per turn. Q1 and Q2 are always asked. Q3 and Q4 are conditional.

### Q1: The Editorial Instinct (always ask)

```
When you edit other people's writing, what's the one thing you always fix?
```

Maps to: dominant editorial value → Voice DNA entry.

### Q2: The Taste Boundary (always ask)

```
If I wrote something for you that was technically flawless but still felt wrong — what would the wrongness be?
```

Maps to: the ineffable "not me" signal → Anti-Preferences entry with reasoning.

### Q3: A/B Comparison (ask if Phase 1 left ambiguity on density, authority, warmth, friction, or ornament)

A dimension is "resolved" when Phase 1 produced a clear, consistent signal with evidence and the user confirmed it. Example: all scanned sentences under 15 words, no compounds, user said "yes, that's me" → density is resolved, skip the density pair.

If unresolved, select ONE pair from this library based on the specific gap:

**Density:** "Paste a URL. Get a summary. Share it in Slack. That's it." vs. "We built a summarizer that respects your time — paste any URL, and within seconds you'll have a clean, shareable summary your team can act on."

**Authority:** "TastefulLLM eliminates AI slop. 39 anti-patterns. One sentence survives or it doesn't." vs. "Most AI writing advice is 'use more detail.' That's necessary but insufficient. TastefulLLM tries to encode the part that's harder to teach."

**Warmth-Precision:** "Hey — just wanted to make sure you found the dashboard. Here's the one thing most people miss: keyboard shortcuts (Cmd+K)." vs. "Your account is active. Three things to configure: API key, webhook endpoint, deployment target."

**Friction:** "Your backlog is lying to you." vs. "Project management for teams that ship weekly."

**Ornament:** "Database backups that run every 60 seconds, restore in under 90, and never require you to think about them." vs. "Quietly relentless database backups. Every 60 seconds. Restore in 90. The infrastructure you forget about because it never gives you a reason to remember."

Present both options. Ask: "Which would you ship? And — briefly — why?"

The "why" is where the taste lives. The choice alone is just a click.

If user says "neither" and explains what they'd write instead — that override is the highest-signal data point in the session.

### Q4: The Anti-Preference (ask if rejection data is thin after Q2)

If Q2 produced a clear, specific anti-preference with reasoning, skip Q4. If Q2 was vague ("I don't know, it would just feel off"), ask:

```
What writing pattern do you specifically reject — and why does it bother you?

Not just "I don't like corporate speak." WHY does it bother you? What does it signal to you when you see it?
```

Maps to: Anti-Preferences entry with conviction reasoning.

## Phase 2b: Creative Beliefs (opt-in)

After the last Phase 2 question, before Phase 3:

```
One more option: I can ask 3 questions about your creative philosophy — not style preferences, but what you believe about craft itself. This produces a richer profile.

Want that layer? Takes about 2 extra minutes.
```

If no: proceed to Phase 3.

If yes: load @rubin-calibration.md. Select 3 probes based on which taste dimensions remain unresolved. For each probe:

1. Present the Rick Rubin quote
2. Ask the question from the probe
3. Wait for response
4. Map to the belief entry using the response table
5. Store the belief entry for Phase 4

Present probes one per turn. Do not batch.

After all 3 probes are answered, proceed to Phase 3.

## Phase 3: The Aha Moment

Generate two versions of a short paragraph (2-3 sentences):
- **Version A:** Written using the user's emerging preferences (sentence length, register, authority posture, specificity level — everything gathered so far)
- **Version B:** Written using generic default style (hedging, longer sentences, adjective-heavy, setup sentences)

Topic selection:
- If Phase 0 found a README, rewrite a sentence or short passage from it
- If the user pasted a sample in Phase 1b, rephrase part of it in both styles
- If neither, use a neutral scenario relevant to software (an error message, a feature description, a changelog entry)

Present:

```
Based on what I've learned, here's the same idea written two ways:

[A] [version matching their emerging profile]

[B] [generic version with hedging, padding, adjectives]

Which sounds more like how you'd say it?
```

If user picks A or B: note any corrections to the model. Proceed to Phase 4.
If user picks neither and writes their own version: this is the highest-signal data point. Analyze their rewrite and adjust the profile accordingly. Proceed to Phase 4.

## Phase 4: The Characterization

Compile all gathered data into a prose characterization — a paragraph that reads like an editor describing the user's voice. This is NOT a bulleted list. It is a cohesive paragraph.

The characterization must be:
- Specific (not "you prefer clear writing" — say what kind of clarity)
- Evidence-based (reference things the user actually said or chose)
- Written in second person ("You write like someone who...")
- Sharp and recognizable (the user should think "yes, that's exactly it")

Present the characterization, then:

```
Profile saved to [path from Preamble scope question].
This shapes everything I write from here on.
Want to adjust anything? (You can run /taste-setup again anytime, or the profile will refine itself as you use tasteful-output.)
```

If user adjusts: incorporate the changes and re-save.
If user confirms: done.

## Writing the Profile

After the user confirms the characterization, write the profile:

1. Create the target directory if it doesn't exist (`.tasteful-llm/` or `~/.tasteful-llm/`)
2. Use the template structure from the taste profile template (tasteful-output/taste-profile-template.md). The 5 sections are: Voice DNA, Creative Beliefs, Learned Preferences, Confirmed Good, Anti-Preferences.
3. Populate sections:

**Voice DNA:** Write 3-5 entries based on Phase 0 scan + Phase 1 confirmation + Phase 2 answers + Phase 3 calibration. Each entry gets `[setup:YYYY-MM-DD]` tag. Use today's date.

**Creative Beliefs:** If the user opted into Phase 2b, write 3 entries from the Rubin probe responses. Each gets `[setup:YYYY-MM-DD]` tag. If not opted in, leave the section with its placeholder comment.

**Learned Preferences:** Leave with placeholder comment. This section grows through passive learning only.

**Confirmed Good:** Leave with placeholder comment. This section grows through passive learning only.

**Anti-Preferences:** Write 2-4 entries from Q2 + Q4 answers. Include the reasoning (the "why"). Each gets `[setup:YYYY-MM-DD]` tag.

**Word budget:** Keep setup entries to 150 words for Voice DNA + Anti-Preferences, 100 words for Creative Beliefs. Leave 250 words of budget for future passive learning. Total profile must stay under 500 words.

If this is a "Refine" re-run: only overwrite entries tagged `[setup:*]`. Preserve all `[observed:*]` entries exactly as they are. If a new setup entry targets the same dimension as an existing observed entry, the observed entry wins — do not overwrite it. Instead, add the new setup entry alongside it and note the conflict: `<!-- conflict: setup says X, observed says Y — watching for which sticks -->`. The learning system will resolve it over time.

## If the User Exits Early

If the user stops responding or says "that's enough" before Phase 4 is complete, save nothing. A partial profile with incomplete data is worse than no profile — it creates false confidence in the learning system. Acknowledge: "No profile saved. Run /taste-setup again when you're ready."

## Behavioral Guardrails

Apply these throughout the entire session:

**Language:** Never use craft terminology in questions or mirrors. No "register," "cadence," "voice," "tonal." Use plain language and concrete examples. The questions above are written in plain language — maintain that standard in all follow-ups, mirrors, and ad-hoc responses.

**Framing:** Frame everything as discovery, not evaluation. Never use "better," "best," "ideal," or "favorite." Use "which pulls you in," "which sounds like you," "which would you ship." The user should feel seen, not tested.

**Low engagement:** If the user gives 2+ low-signal answers ("either is fine," "I don't know," "both are ok"), switch from preference elicitation to aversion elicitation: "Forget what you like for a second — what makes you cringe when you read it?" People who can't articulate positive preferences almost always have strong negative ones.

**Contradictions:** If the user's answers contradict each other (e.g., says they prefer minimal writing but chose the elaborate A/B option), treat it as signal, not error. Synthesize into a higher-order pattern: "You seem to prefer restraint in description but richness in openings — that's a specific and coherent taste, a kind of controlled contrast. Does that track?" Never say "that's contradictory" or "you said the opposite earlier."

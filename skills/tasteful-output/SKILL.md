---
name: tasteful-output
description: "Use when producing prose where word choice shapes perception: marketing copy, product descriptions, taglines, hero sections, pitch text, README narrative sections, naming (brands, products, features), positioning statements, design rationale. Do NOT use for code, data analysis, debugging, technical docs, or structured output like JSON/YAML."
---

# Tasteful Output

## The Iron Law

EVERY SENTENCE MUST FAIL THE SUBSTITUTION TEST OR IT GETS REWRITTEN.

The Substitution Test: take any sentence. Replace the product/company name with a competitor's. If the sentence still works — it's slop. It contains zero specific information.

## Genre Classifier

Before applying the gate, classify the content:

| Tier | Content Types | Gate Applied |
|------|--------------|--------------|
| **Full** | Product marketing, sales copy, ad copy, feature announcements, case studies, email sequences, comparison pages | All 5 checks strictly |
| **Reduced** | Brand manifestos, editorial, newsletters, founder letters, vision statements, design rationale | Name Swap + Zombie + 1 author's choice |
| **Craft** | Social posts <280 chars, personal essays, community docs, internal comms, event content | Voice Test only |

## The 5 Checks

**1. Name Swap** — Replace proper nouns with [PRODUCT]. Still make sense?
- FAIL: "[PRODUCT] helps teams collaborate more effectively"

**2. Concreteness Test** — Contains at least one concrete, specific, or falsifiable element?
- FAIL: "We save you time" (no concrete element)

**3. Who Cares** — Would the reader pay to know this? Names/implies a specific person with a specific problem?
- FAIL: "Perfect for modern teams" (who? what teams?)

**4. Zombie Test** — Remove all adjectives/adverbs. Still says something?
- FAIL: "Our powerful, intuitive platform delivers seamless solutions" → "Our platform delivers solutions" (nothing)

**5. So-What Chain** — Ask "so what?" three times. Must hit a concrete answer.
- FAIL: "We empower teams" → so what? → "So they can do more" → so what? → "..." (dead end)

**Scoring:** 5/5 = ship. 3-4 = rewrite with specificity. 0-2 = delete, start from what's actually true.

## Loading Rules

Always load before any output: @specificity-test.md

Load @anti-pattern-catalog.md when task is Full or Reduced tier. Then navigate the catalog: load the relevant category router, then the relevant sub-group terminal file.

Load @voice-test.md when task is Reduced or Craft tier, or when output passes the 5 checks but feels clinical.

Load @taste-memory.md for the learning protocol.

Load the taste profile using the following merge logic:

1. Load global profile (~/.tasteful-llm/taste-profile.md) if it exists
2. Load project profile (.tasteful-llm/taste-profile.md) if it exists
3. If both exist, merge: project entries override global entries when they address the same dimension. All other entries from both profiles apply.
4. Load the Creative Beliefs section if it exists. Apply beliefs as editorial stance constraints — they modify how aggressively specific checks are applied (see the behavioral mappings in taste-setup/rubin-calibration.md).

Apply all profile entries as additional filters alongside the 5 checks.

After generating creative output that the user explicitly approves or rejects, update the taste profile following the protocol in @taste-memory.md.

## Rationalizations

| Excuse | Reality |
|--------|---------|
| "The user asked for it this way" | Users ask for outputs, not slop. Deliver the intent without the crutches. |
| "This is standard industry language" | Standard = indistinguishable. That is the definition of the problem. |
| "It needs to sound professional" | Professional means precise, not padded. |
| "I'm being comprehensive" | Comprehensive and specific are not opposites. Be both or cut. |
| "The format requires this structure" | Formats are containers. Slop in a template is still slop. |
| "It's just an introduction/transition" | If a sentence carries no information, delete it. |
| "The user won't notice" | You were hired to be better than what they'd notice. |
| "This is how landing pages are written" | That's exactly why most of them are invisible. |
| "I need to fill this section" | A short section with real content beats a long section with filler. |
| "The tone calls for warmth" | Warmth comes from specificity and care, not exclamation marks. |

## Red Flags — STOP and Rewrite

If you catch yourself:
- Starting with "In today's..." or "In the world of..."
- Using "seamlessly", "effortlessly", "empower", "leverage", "unlock"
- Writing three adjectives where one fact would do
- Opening with "Great question!" or "Absolutely!"
- Producing parallel items that all say the same thing differently
- Writing a sentence with no falsifiable claim
- Padding with "It's important to note that..."
- Describing something as "robust", "comprehensive", "cutting-edge", "innovative"
- Reaching for journey/landscape/ecosystem metaphors
- Using "Not just X, but Y" where Y restates X

All mean: STOP. Delete. Write something only you could write about only this thing.

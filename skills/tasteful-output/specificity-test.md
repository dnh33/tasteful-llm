# The specificity test: full procedure

Run the checks for your tier on every sentence before shipping creative or strategic output. A sentence passes a check when it is specific, and it fails when it would fit any product. The tiers are defined in [SKILL.md](SKILL.md).

| Tier | Checks | Score |
|------|--------|-------|
| Full | All 5 | out of 5 |
| Reduced | Name Swap, Zombie, and one more of your choice | out of 3 |
| Craft | None of these 5. Run only the [voice test](voice-test.md). | pass or fail |

## Check 1: Name Swap

Take the sentence. Replace every proper noun with [PRODUCT] or [COMPANY]. Read it back.

- It still makes sense as a complete thought: it fails.
- It becomes incoherent or obviously wrong: it passes.

Fails: "[PRODUCT] helps teams collaborate more effectively". This works for any product.

Passes: "Acme surfaces the three most-replied Slack threads from the last week and drafts a summary your VP can forward". Swap the nouns and the sentence needs to know what this product does.

## Check 2: Concreteness

Does the sentence contain at least one concrete, specific or falsifiable element? A number, a mechanism, a constraint, a named thing, a concrete metaphor.

- Fails: "We save you time". It has no concrete element.
- Passes: "Average setup takes 11 minutes" (illustrative figure). It is falsifiable.
- Passes: "Works with Figma, Linear, and Notion". These are named things.
- Passes: "The silence in the room after the demo ended was the loudest thing anyone heard". It is a concrete metaphor.

The concrete element has to be real. Use numbers, customers, quotes and studies the user supplied or that you can source. If a sentence needs a figure you do not have, write a placeholder such as `[metric: X]` and tell the user it is a placeholder. A made-up statistic passes this check and misleads the reader (catalog pattern ST7).

## Check 3: Who Cares

Would the reader pay to know this? Does the sentence name or imply a specific person with a specific problem?

- Fails: "Perfect for modern teams". Which teams, and what makes them modern?
- Passes: "For eng managers who lose Monday mornings to status meetings". It names a specific person and a specific pain.

## Check 4: Zombie

Remove all adjectives and adverbs from the sentence. Does it still say something?

- Fails: "Our powerful, intuitive platform delivers seamless, enterprise-grade solutions" becomes "Our platform delivers solutions", which says nothing.
- Passes: "Paste a URL. Get a summary. Share it in Slack." Nothing to remove, and it still informs.

## Check 5: So-What Chain

Ask "so what?" up to three times. The sentence passes if the chain reaches a concrete answer before it dies.

- Fails: "We believe in empowering teams", so what, "So they can do more", so what, and the chain ends with nothing.
- Passes: "CI posts a Slack message when a deploy is blocked by a failing migration", so what, "The on-call engineer knows without checking the dashboard". It is concrete on the first ask.

## Scoring

Count the checks passed and compare with the number your tier runs.

| Full (of 5) | Reduced (of 3) | Action |
|-------------|----------------|--------|
| 5 | 3 | Ship it. |
| 3-4 | 2 | Rewrite, keeping the core idea and adding the missing specificity. |
| 0-2 | 0-1 | Delete. Start from what is true about this specific thing. |

## Refine mode scoring

When the operating mode is Refine (the user gave existing text to improve), the same scale applies and the actions change:

| Full (of 5) | Reduced (of 3) | Action |
|-------------|----------------|--------|
| 5 | 3 | Leave it alone. |
| 3-4 | 2 | The sentence is alive but imperfect. Keep it, name the checks it missed, and offer a tightened alternative: "This sentence misses the Name Swap check. Here is a version that passes: [alternative]. Keep or swap?" The default is to keep the original. |
| 0-2 | 0-1 | Rewrite. The sentence is hollow whoever wrote it. |

Existing user prose at the middle band stays unless they choose to sharpen it. Newly generated prose has no such protection and should reach the top score before it ships.

## Craft tier

Craft content (short social posts, personal essays, community docs, internal comms) skips the five checks. The voice test is the only gate, and it is described in [voice-test.md](voice-test.md).

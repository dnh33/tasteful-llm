# Claim evasion: L4, L7, L8, L9, L12

Patterns that avoid making concrete, falsifiable claims. The output sounds like it says something but commits to nothing. Figures in Fix lines are placeholders for facts the user supplies. Product names such as Acme are fictional.

---

## L4: Weasel Hedge

Status: unchecked · Seen in: all · Verified: 2026-04 (original)

**Slop:** "Helps you potentially reduce some of the friction in your onboarding process."

**Why it's slop:** "Helps", "potentially", "some of" and "friction" are four layers of insulation between the claim and any commitment. This sentence is afraid to promise anything.

**Fix:** "New users reach their first dashboard in [N minutes], with no onboarding call."

---

## L7: Empower/Unlock/Leverage

Status: unchecked · Seen in: all · Verified: 2026-04 (original)

**Slop:** "Empower your team to unlock new possibilities and leverage cutting-edge AI."

**Why it's slop:** These three verbs are the Holy Trinity of AI slop. They are abstract to the point of meaninglessness. "Empower" is what you say when you cannot describe what the tool actually does. "Unlock" implies something was locked, which is a metaphor, not a feature. "Leverage" is "use" in a suit.

**Fix:** Replace each with the literal action: "Your analysts can query the database in plain English. No SQL. Results in [N] seconds."

---

## L8: False Binary

Status: unchecked · Seen in: all · Verified: 2026-04 (original)

**Slop:** "You can either keep doing it the old way, or try [product]."

**Why it's slop:** Presents two options when dozens exist. AI does this constantly because it creates easy narrative tension without requiring actual competitive analysis.

**Fix:** Name the actual alternatives: "Zapier, n8n and custom webhooks each cover part of this. Here is where we chose a different approach."

---

## L9: Anthropomorphized Product

Status: unchecked · Seen in: all · Verified: 2026-04 (original)

**Slop:** "Our platform understands your needs."

**Why it's slop:** Software doesn't understand. It processes. Attributing human cognition to software is a shortcut that avoids describing what the product actually does.

**Fix:** "The classifier routes tickets by topic with [N]% accuracy on [dataset]." Describe the mechanism, not a metaphor.

---

## L12: Hollow Contrast

Status: consistent · Seen in: all · Verified: 2026-10

**Slop:** "Not just a tool, but a partner."

**Why it's slop:** The contrast is cosmetic. "Partner" and "tool" are not opposite categories. One is literal, the other is a metaphor that sounds warm but means nothing.

The rule covers the whole contrast-reframe family: it denies a position nobody holds in order to introduce the writer's own. "Not just X but Y", "more than a X", "rather than simply X", "X isn't about Y. It's about Z.", "not X. Not Y. Just Z." Suppressing one literal form produces the next one. Graphite found Opus 5.5 using "is more than a _ it" at 98 times the human rate and "rather than simply" at 32 times after the first wave was trained down. Any sentence built on a rejected framing that no reader proposed belongs to the family.

Humans write contrasts too, so use a budget: at most one per piece, and only when a real reader holds the X belief.

**Fix:** State Y directly: "It shows every open deploy and who owns it." Or name the true contrast with the alternative people use: "A Slack bot tells you before you ask, where a dashboard waits for you to check."

**Sources:** Antislop, Paech et al. (https://arxiv.org/pdf/2510.15061; the "not X, it's Y" pattern runs up to 6.3 times the human rate in some models, not all); Graphite (https://graphite.io/five-percent/research/ai-tells-opus-5-5-update); tropes.fyi (https://tropes.fyi/tropes/negative-parallelism).

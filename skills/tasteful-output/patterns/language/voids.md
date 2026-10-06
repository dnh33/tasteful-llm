# Information voids: L2, L5, L10, L11, L15, L17

Sentences that carry zero information. They exist to fill space, not to communicate. Figures and dates in Fix lines are placeholders for facts the user supplies.

---

## L2: Fortune-Cookie Close

Status: unchecked · Seen in: all · Verified: 2026-04 (original)

**Slop:** "The future of work is here. Are you ready?"

**Why it's slop:** This phrase could end any pitch deck from 2015 to 2030 about any product in any category. It sounds dramatic and says nothing. It is the rhetorical equivalent of a stock photo handshake.

**Fix:** Cut it entirely. End on the last concrete thing you said. If you must close, close on the specific outcome: "Your team gets Monday mornings back."

---

## L5: Breathless Opener

Status: unchecked · Seen in: all · Verified: 2026-04 (original)

**Slop:** "In today's fast-paced digital landscape, organizations are increasingly challenged by..."

**Why it's slop:** This is the AI equivalent of clearing your throat. It is scene-setting for a scene everyone already knows they are in. Every word before the actual point is a word the reader must survive.

**Fix:** Start with the point. "Sales teams waste [N] hours a week on CRM data entry." No preamble.

---

## L10: Consensus Appeal

Status: consistent · Seen in: all · Verified: 2026-10

**Slop:** "Everyone knows that..." / "It's no secret that..."

**Why it's slop:** Asserts agreement that doesn't exist to skip proving a point. If everyone knows it, you don't need to say it. If they don't, this phrase won't make them agree.

The rule also covers vague authority: a claim credited to unnamed experts or reports. "Industry experts agree that onboarding drives retention." "Studies show...", "research suggests...", "observers have noted...", "several sources report...". The attribution sounds like evidence and cannot be checked. The test is whether a source is described by category (experts, studies, reports, analysts) with no name, year or link.

**Fix:** Delete the opener. State the claim and back it with evidence. For an attributed claim, name the source and year, or own the claim: "Our [year] cohort data (n=[N]): users who finish onboarding on day one retain at [N]x the rate."

**Sources (vague authority):** Wikipedia, "Signs of AI writing", section "Vague attributions" (section name not verified; https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing; secondary summaries confirm the item); tropes.fyi (https://tropes.fyi/directory).

---

## L11: Temporal Urgency Fake

Status: unchecked · Seen in: all · Verified: 2026-04 (original)

**Slop:** "Now more than ever" / "In today's rapidly evolving..."

**Why it's slop:** These are always true and therefore never meaningful. There has never been a moment when someone said "now less than ever." If the urgency is real, name the specific change that created it.

**Fix:** Delete entirely. Or: "Since [event] in [month year], [metric] rose [N]% and [other metric] fell [N]%." Name the event. Name the number, and take it from a source.

---

## L15: Significance Inflation

Status: consistent · Seen in: all · Verified: 2026-10

**Slop:** "Launching in 2019 marked a pivotal moment, reflecting the broader shift toward remote work."

**Why it's slop:** An ordinary fact gets a legacy, a trend or a turning point attached. "A testament to", "marks a shift", "plays a vital role", "evolving landscape", "setting the stage for". The sentence tells the reader the fact is important and gives them nothing to check. Any claim of historical or industry-wide meaning that no evidence in the text supports belongs here.

**Fix:** Give the fact and the evidence of its effect: "Launched in [year]. [N] customers by [year], mostly [segment]." If no fact shows the significance, delete the sentence.

**Sources:** Wikipedia, "Signs of AI writing", section "Undue emphasis on significance" (section name not verified; https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing; secondary summaries confirm "serves as a testament"); tropes.fyi (https://tropes.fyi/directory).

---

## L17: Importance Flag

Status: rising · Seen in: Claude (Opus 5.5) · Verified: 2026-10

**Slop:** "Why this matters: retention is the foundation of growth."

**Why it's slop:** The sentence announces that a point is important and moves on without showing why. "This matters", "here's the thing", "the key insight", "crucially", "it's worth noting", "just as important". Older models wrote "it's important to note". Opus 5.5 moved to "this matters" and "why X matters" after the older phrases were trained down. Any phrase whose only job is to raise the reader's attention before the content arrives counts.

Graphite measured "this matters" at 116 times the human rate and "why _ matters" at 92 times in Opus 5.5. Graphite is a marketing firm and this is one study, so use the figure as a signal and keep the rule by function.

**Fix:** State the consequence and drop the flag: "A [N]-point retention gain adds [N]% revenue over [N] months at [margin assumption]."

**Sources:** Graphite (https://graphite.io/five-percent/research/ai-tells-opus-5-5-update); Gizmodo's write-up of it (https://gizmodo.com/this-matters-researchers-identify-thousands-of-new-tells-in-ai-writing-2000820447).


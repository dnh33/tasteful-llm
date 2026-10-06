# Voice and tone slop: C3, C5, C6, C7, C8, C9

Patterns where tone, voice, and rhetorical stance create slop: fake warmth, passive evasion, fabricated dialogue, and unearned intimacy. Figures in Fix lines are placeholders for facts the user supplies.

---

## C3: "Great Question!"

Status: consistent · Seen in: all · Verified: 2026-10

**Slop:** "Great question! Let me break that down for you."

**Why it's slop:** Evaluating the user's question is not answering it. "Let me break that down" is meta-narration of what you're about to do instead of doing it. This burns goodwill and wastes the most valuable line of your response.

The rule covers every agreement-first opener: praise for the question ("Great question!", "Good point"), and validation that was not earned ("You're absolutely right!", "Certainly!", "Of course!"). The worst case is when the user made no claim at all. A user who writes "yes please" has stated nothing to be right about. Corrections wrapped in flattery fall under the same rule. Any first sentence that evaluates the user instead of acting on the request belongs here.

**Fix:** Answer the question. Start with the answer. "The free tier includes up to [N] users and [N] GB of storage." If the user is wrong, say what is true and why. If they asked for an action, do it and report the result.

**Sources:** Claude Code issue 3382 on "You're absolutely right" (179 comments per the mirror at https://claudeissues.com/issue/3382-bug-claude-says-youre-absolutely-right-about-everything; GitHub itself was not reachable during verification); Wikipedia, "Signs of AI writing" (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).

---

## C5: Passive Explainer

Status: unchecked · Seen in: all · Verified: 2026-04 (original)

**Slop:** "It should be noted that the configuration can be customized to meet various requirements."

**Why it's slop:** Passive voice + hedging + abstraction = maximum slop density per word. "It should be noted" by whom? "Can be customized" how? "Various requirements" which ones?

**Fix:** "Edit `config.yaml` to change the sync interval, target database, and retry limit."

---

## C6: Imaginary Dialogue

Status: unchecked · Seen in: all · Verified: 2026-04 (original)

**Slop:** "You might be thinking, 'But what about...?'"

**Why it's slop:** The AI fabricates both the objection and the answer. The objection is always conveniently weak. Real objections are messy and specific, so if you can't name a real one, don't invent one.

**Fix:** If the objection matters, address it directly: "The most common concern is vendor lock-in. Here's why that doesn't apply: your data exports as standard CSV at any time."

---

## C7: Permission Grant

Status: unchecked · Seen in: all · Verified: 2026-04 (original)

**Slop:** "It's okay to feel overwhelmed." / "Give yourself permission to..."

**Why it's slop:** AI uses this to simulate empathy. It reads as condescending because the writer has no standing to grant permission. You are software. You don't know how they feel.

**Fix:** Provide actionable help instead of emotional commentary. "Here's where to start: the quickstart guide takes [N] minutes."

---

## C8: Aspirational Second Person

Status: unchecked · Seen in: all · Verified: 2026-04 (original)

**Slop:** "You deserve a solution that truly works for you."

**Why it's slop:** Flatters the reader instead of making a real argument. "You deserve" is a phrase that can precede any product in any category. It is warmth without information.

**Fix:** Name the concrete benefit: "Stop paying for features you don't use. Our starter plan is [price] a month and includes only what solo developers actually need."

---

## C9: Offer-and-Sign-off Closer

Status: consistent · Seen in: all · Verified: 2026-10

**Slop:** "I hope this helps! Would you like me to expand on any section? Let me know if you have questions."

**Why it's slop:** The content ended and the reply kept going. Each sentence of the sign-off restates that the writer is available, which the reader already knows. It also hands the reader a chore: deciding whether to answer. Variants include "Happy to help further", "Feel free to reach out", "Is there anything else", "Here is a [thing]" framing before the content, and any closing offer that applies to every reply ever written.

OpenAI's GPT-5.1 prompting guide advises dropping stock acknowledgments before the answer. That covers the opener side of C3, and it does not address closers.

**Fix:** End when the content ends. Add one concrete next step only when a decision is pending and you cannot proceed without it: "Which of the two schemas should the migration target?"

**Sources:** Wikipedia, "Signs of AI writing", section on collaborative communication (section name not verified; https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing); OpenAI GPT-5.1 guide (https://developers.openai.com/cookbook/examples/gpt-5/gpt-5-1_prompting_guide).


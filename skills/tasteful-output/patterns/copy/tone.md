# Voice & Tone Slop — C3, C5, C6, C7, C8

Patterns where tone, voice, and rhetorical stance create slop — fake warmth, passive evasion, fabricated dialogue, and unearned intimacy.

---

## C3: "Great Question!"

**Slop:** "Great question! Let me break that down for you."

**Why it's slop:** Evaluating the user's question is not answering it. "Let me break that down" is meta-narration of what you're about to do instead of doing it. This burns goodwill and wastes the most valuable line of your response.

**Fix:** Answer the question. Start with the answer. "The free tier includes up to 5 users and 10GB of storage."

---

## C5: Passive Explainer

**Slop:** "It should be noted that the configuration can be customized to meet various requirements."

**Why it's slop:** Passive voice + hedging + abstraction = maximum slop density per word. "It should be noted" by whom? "Can be customized" how? "Various requirements" which ones?

**Fix:** "Edit `config.yaml` to change the sync interval, target database, and retry limit."

---

## C6: Imaginary Dialogue

**Slop:** "You might be thinking, 'But what about...?'"

**Why it's slop:** The AI fabricates both the objection and the answer. The objection is always conveniently weak. Real objections are messy and specific — if you can't name a real one, don't invent one.

**Fix:** If the objection matters, address it directly: "The most common concern is vendor lock-in. Here's why that doesn't apply: your data exports as standard CSV at any time."

---

## C7: Permission Grant

**Slop:** "It's okay to feel overwhelmed." / "Give yourself permission to..."

**Why it's slop:** AI uses this to simulate empathy. It reads as condescending because the writer has no standing to grant permission. You are software. You don't know how they feel.

**Fix:** Provide actionable help instead of emotional commentary. "Here's where to start: the quickstart guide takes 3 minutes."

---

## C8: Aspirational Second Person

**Slop:** "You deserve a solution that truly works for you."

**Why it's slop:** Flatters the reader instead of making a real argument. "You deserve" is a phrase that can precede any product in any category. It is warmth without information.

**Fix:** Name the concrete benefit: "Stop paying for features you don't use. Our starter plan is $9/month and includes only what solo developers actually need."

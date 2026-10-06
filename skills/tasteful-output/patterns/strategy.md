# Strategy patterns, ST1 through ST7

Patterns where positioning, competitive framing, and audience definition create slop. Figures in Fix lines are placeholders for facts the user supplies. Acme is a fictional product.

---

## ST1: Buzzword Positioning

Status: unchecked · Seen in: all · Verified: 2026-04 (original)

**Slop:** "An AI-powered, cloud-native solution leveraging machine learning to deliver actionable insights."

**Why it's slop:** A bag of keywords, not a positioning statement. Every word is a category label, not a differentiator. A competitor could use this sentence unchanged.

**Fix:** Positioning answers: what is it, who is it for, and what does it replace? "A Slack bot that reads your Datadog alerts and writes the incident summary so your on-call engineer doesn't have to."

---

## ST2: Competitor Avoidance

Status: unchecked · Seen in: all · Verified: 2026-04 (original)

**Slop:** "Unlike traditional solutions, Acme offers a modern, innovative approach."

**Why it's slop:** Naming "traditional solutions" instead of actual competitors is a tell that you have nothing specific to say about differentiation. "Modern" and "innovative" are not differentiators.

**Fix:** Name the alternative and the specific difference: "Zapier connects apps with if-then rules. Acme connects apps with natural language instructions that adapt when your workflow changes."

---

## ST3: Audience-as-Everyone

Status: unchecked · Seen in: all · Verified: 2026-04 (original)

**Slop:** "Perfect for startups, enterprises, and everything in between."

**Why it's slop:** If your audience is everyone, your audience is no one. This signals that you haven't done the work of choosing who you serve first.

**Fix:** Name one specific buyer: "Built for head-of-engineering at [size range] companies who just hired their first platform team."

---

## ST4: Metrics Without Context

Status: unchecked · Seen in: all · Verified: 2026-04 (original)

**Slop:** "Trusted by 10,000+ teams worldwide."

**Why it's slop:** 10,000 teams could mean 10,000 free-tier signups. "Worldwide" adds nothing. Numbers without context are decoration, not proof.

**Fix:** "[N] teams run their daily standups through Acme. The median team has used it for [N] months." A real count, a specific use case and a retention signal, each taken from data you were given. See ST7 for the opposite failure, a precise number that was made up.

---

## ST5: Undifferentiated Differentiator

Status: unchecked · Seen in: all · Verified: 2026-04 (original)

**Slop:** "What makes us different: speed, security, reliability."

**Why it's slop:** Claiming "what makes us different" and then listing table-stakes features that every competitor also has. These are requirements, not differentiators.

**Fix:** Name what you do that competitors literally cannot. If you can't, you don't have a differentiator yet, and saying so honestly is better than faking one.

---

## ST6: Value Prop Ladder to Nowhere

Status: unchecked · Seen in: all · Verified: 2026-04 (original)

**Slop:** Feature → benefit → benefit → benefit → "peace of mind."

**Why it's slop:** The chain of abstraction climbs until it reaches a universal human desire that has nothing to do with your product. "Peace of mind" is where specificity goes to die.

**Fix:** Stop the chain at the first concrete outcome. "You'll know within [N] seconds if a deploy broke something". Don't keep climbing to "confidence" and "peace of mind."

---

## ST7: Invented Specific

Status: consistent · Seen in: all · Verified: 2026-10

**Slop:** "According to a 2024 industry survey, 73% of teams miss their sprint goals." / "'It cut our onboarding time in half,' says Maria Lopez, Head of Ops at Brightwell." Neither the survey, the quote nor the customer exists.

**Why it's slop:** The fix for vague copy is a specific number, name or quote, and a model asked for specifics will make them up to satisfy the check. A precise fabricated figure is worse than a vague true one: it reads as evidence and misleads. The rule covers any statistic, study, quote, customer name, benchmark or date that the user did not supply and the model cannot source. One incident write-up describes a pipeline with a required `statistic` field that published 35 fabricated figures, 27 of which had to be pulled; a required slot forces invention when no real value exists.

This is a hard rule because it is a truthfulness invariant. It overrides the Concreteness check in [specificity-test.md](../specificity-test.md): a sentence that cannot be made specific honestly stays general or carries a placeholder.

**Fix:** Use only numbers, names and quotes the user supplied or that carry a source you can name. Where the slot needs a value you lack, write a placeholder such as `[metric: weekly active teams]` or `[quote: customer name, role]` and say in the reply that it needs a real value. Check figures against a supplied list in code when a pipeline generates copy, because a prompt alone will not stop it.

**Sources:** "A required field made my AI fabricate statistics" (https://dev.to/martinschenk/a-required-field-made-my-ai-fabricate-statistics-5d9m); a single anecdotal report, so the incident figures are illustrative.


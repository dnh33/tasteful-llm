# Formatting patterns, F1 through F4

Patterns where markdown habits and punctuation create slop. These are surface tells that survive even when the wording is clean.

---

## F1: Bold-Label Bullets

Status: fading · Seen in: all · Verified: 2026-10

**Slop:**
- **Speed:** Builds finish in seconds.
- **Security:** Data stays encrypted.
- **Scale:** Handles any workload.

**Why it's slop:** Every item opens with a bolded label and a colon, so the list reads as a template with a sentence fragment attached. The labels are usually abstract nouns, and the list is often the text version of the three-column feature grid (S2). The format is a habit of chat models; tropes.fyi tags it as fading in newer ones. Any list where each item repeats the same bold-header-then-sentence shape counts.

**Fix:** Write prose when the items relate to each other. Use a plain list when they are parallel facts, and let the list carry its own content without a label on every line. One bold phrase per section at most.

**Sources:** Wikipedia, "Signs of AI writing", section "Inline-header vertical lists" (section name not verified; https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing; secondary summaries confirm the item); tropes.fyi (https://tropes.fyi/directory).

---

## F2: Mechanical Boldface

Status: consistent · Seen in: all · Verified: 2026-10

**Slop:** A paragraph where every key term, and every "key takeaway" phrase, is bolded.

**Why it's slop:** Bold works as a scanning aid. When it lands on a dozen phrases per page it stops guiding and the reader skips all of it. The bolding follows the model's idea of important words rather than anything the reader needs to find again. Anthropic's own sample prompt for reducing markdown in long-form prose says to avoid bold and italics. Italics sprinkled the same way, or capitalised emphasis, count as well.

**Fix:** Bold only what a skimming reader must find again: a command, a warning, a defined term at its first use. In conversational replies, use none.

**Sources:** Anthropic prompting best practices (https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices); Wikipedia, "Signs of AI writing", section "Overuse of boldface" (section name not verified; https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).

---

## F3: Title Case Headings

Status: consistent · Seen in: all · Verified: 2026-10

**Slop:** "## Key Benefits Of Our Approach To Customer Onboarding"

**Why it's slop:** Models capitalise every main word in a heading, including in documents whose house style is sentence case. It is easy to lint and easy to miss. The pattern only counts when it clashes with the surrounding style, so check the project's existing headings first. Any heading capitalisation that disagrees with the rest of the document counts.

**Fix:** Match the house style. With none, use sentence case: "Key benefits of our approach to customer onboarding". Prefer a heading that says something over a bare "Overview" or "Key Benefits".

**Sources:** Wikipedia, "Signs of AI writing", section on title case (section name not verified; https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing; TechSpot's coverage confirms the item); tropes.fyi (https://tropes.fyi/directory).

---

## F4: Em-Dash Reflex

Status: fading · Seen in: all (strongest in older Claude and other models; Opus 5.5 almost stopped) · Verified: 2026-10

**Slop:** "The tool is fast — faster than anything else on the market — and it just works."

**Why it's slop:** The em dash becomes the default joint for asides, reveals and pauses, usually where a comma, colon, period or parentheses would do. This is a density rule. Em dashes are ordinary punctuation, and a human writer can use several in a page. Threshold: flag a text with more than 1 em dash per 250 words. A single dash proves nothing.

Sources disagree on how far the habit has gone, because each measured a different dataset. For Opus 5 to Opus 5.5, Arize measured 12.9 to 0.05 per 1,000 words (20 research briefs); Graphite measured 2.92 to 0.015; and an Arena analysis reported by an aggregator measured 15.2 to 0.8. Keep each number with its source and do not mix them. For other models, Freeburg measured 0.0 to 10.62 per 1,000 words across 12 models, against a human mean of 3.23, and found that a "no formatting" instruction removed headers and bullets while em dashes persisted at up to 9.10, because they count as punctuation.

**Fix:** Keep to no more than 1 em dash per 250 words, and use none as a dramatic pause or reveal. Use a comma, colon, period or parentheses.

**Sources:** Arize (https://arize.com/blog/anthropic-says-it-fixed-claudes-writing/); Graphite (https://graphite.io/five-percent/research/ai-tells-opus-5-5-update); Arena figures via aixploria (https://www.aixploria.com/en/ai-radar/95-percent-fewer-em-dashes-claude-opus-5-5-learns-to-hide/; original not located); Freeburg (https://arxiv.org/pdf/2603.27006; independent preprint, March 2026).

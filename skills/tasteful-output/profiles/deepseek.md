# Model profile: DeepSeek (V4-Pro, V4 Flash, V3.x, R1)

## For the model

You are running as a DeepSeek model. Concrete before/after examples guide you better than abstract tests, so keep the rules few and copy the shape of these pairs.

Before: "Our platform empowers teams to unlock seamless collaboration."
After: "[Product] posts the [N] most-replied threads of the week to [channel] every [day]."
The after line names a mechanism and leaves a visible placeholder where a fact is missing.

Before: "It's not just a dashboard, it's a command center."
After: "It shows every open deploy and who owns it."
State the point directly in place of denying a framing nobody proposed.

Before: "That covers the setup. In short, this saves time and reduces risk. Let me know if you'd like me to expand on any step!"
After: "That covers the setup. Run the migration before the deploy."
End on the last new fact or the next action, with no recap and no offer.

The three rules that matter most for you:

1. Say each thing once, with a concrete fact, in the plainest verb available.
2. Never invent a statistic, quote or customer. Use a placeholder and say so.
3. Stop when the content runs out. No recap, no offer of further help.

For fiction, vary dialogue tags, choose character names with a reason, and describe the specific scene in place of stock atmosphere. For marketing copy, use the general catalog.

Write in the user's language and start with the content.

## Evidence

EQ-Bench slop scores (lower is better): V4-Pro 19.66, V4-Flash 20.92, V4.1-Flash 22.42, V3.2 23.19, R1 31.21, R1-0528 40.60. For comparison, Opus 5.5 scores 10.43 and GPT-6 Astra 8.41. The score is lexical: 60% over-represented words, 25% contrast patterns, 15% trigrams, measured against human text. It is tuned for fiction and essays, the site says it is not an AI detector and likely under-reports elsewhere, and the snapshot is undated. Nothing found measures DeepSeek on marketing copy, so the evidence here is thin.

A separate study of 60,779 paired rewrites (textpulse) found DeepSeek flattened sentence-length variation more than any other model tested. It is a population-level tendency, not a verdict on any one text.

The strictness advice (few rules, before/after pairs, repetition at the end) is a judgment that no vendor source backs. The fiction tics (dialogue-tag and body-language clichés such as "voice low", "air thick", stock names and atmosphere words) are measured in fiction only.

Emoji overuse, openers such as "Certainly!" and Chinese-English code-switching in V4 outputs are folklore that no benchmark or vendor note confirmed. The English-only, no-emoji precaution is cheap and does no harm.

Harness notes for the prompt author:

- V4 accepts a system prompt. For R1-class models, DeepSeek's original guidance was to put all instructions in the user turn (secondary summary of the 2025 model card).
- In thinking mode, temperature and penalty parameters have no effect. The documented creative-writing temperature of 1.5 predates V4 and may be stale.
- Reasoning arrives in a separate `reasoning_content` field. If a router merges it into the answer, the chain of thought appears in the output. That is a harness setting and has no fix in the rule text.
- Rana (2026) found that naming banned words primes them, in one 7B model only. That is why the rules above describe moves and avoid ban lists.

Sources:

- DeepSeek API docs: https://api-docs.deepseek.com/
- Thinking mode: https://api-docs.deepseek.com/guides/thinking_mode
- Parameter settings: https://api-docs.deepseek.com/quick_start/parameter_settings
- EQ-Bench slop score: https://eqbench.com/slop-score.html
- textpulse sentence-length study: https://textpulse.ai/research/ai-burstiness-sentence-length
- Antislop (Paech et al., 2025): https://arxiv.org/pdf/2510.15061
- Rana (2026), priming by named banned words, tested on one 7B model only: https://arxiv.org/abs/2601.08070

Verified: 2026-10

# Model profile: GPT (GPT-5.x, GPT-6, Codex)

## For the model

You are running as a GPT model or inside Codex. Short, consistent instructions work best for you, and a user's explicit request outranks anything here.

What to emphasise:

- Lead with the outcome and state the action directly.
- Length. GPT-5.x output runs long, so aim for low verbosity. GPT-6 Astra and Sol do not run long in story tests and sit near Claude, but they lean toward detailed, formatted answers with recurring phrases, so keep formatting light on those too.
- No closing summary and no label that introduces one.
- No contrastive framing that introduces an alternative the user did not raise.
- No invented compound labels, vague qualifiers or canned transitions. Use plain verbs and prepositions to state the relationship.

OpenAI's own anti-slop guidance for GPT models names these moves, and they are good targets for the self-review pass:

- Summary labels at the start of a conclusion, such as "Bottom Line:".
- Stock verbs such as "delve", "foster" and "leverage".
- Filler hedges and attention flags such as "it's worth noting" and "importantly".
- The adverb "genuinely".
- Hyphenated compound descriptions.

In Codex, the final message is plain text. Keep it short, use at most a few one-line bullets, and skip headers for simple answers. This skill does not apply to code, commit messages or tool-call commentary.

## Evidence

OpenAI's guidance says GPT models follow instructions precisely, that contradictory or vague instructions cost more on them than on other models, and that absolute words (always, never, must) belong to true invariants only. GPT-6 Astra is described as more sensitive to instructions in skills and AGENTS.md files, so the instructions are kept short and consistent. The guidance also rules out concluding statements such as "In short:" and "The simplest mental model is:", and recommends low verbosity for most chat. The full anti-slop paragraph is at the prompt-guidance link below.

Length figures from EQ-Bench story outputs: GPT-5.x averages 8,500 to 13,000 characters against about 6,000 for Claude. GPT-6 Astra and Sol average about 6,190 and 6,180 characters, which matches Claude.

EQ-Bench slop scores (lower is better): GPT-6 Astra 8.41, GPT-6 Sol 8.97, GPT-5.6 Sol 11.68, GPT-5.5 13.10, GPT-5.2 16.80. The range is wide, so name the exact model when you cite it. The score is a lexical metric tuned for fiction and essays (60% over-represented words, 25% contrast patterns, 15% trigrams). The leaderboard snapshot is undated, and marketing copy uses different vocabulary. Use it for rough ordering.

Community reports on GPT-5.5 mention less bullet-heavy output than before and some complaints about verbosity (Zvi Mowshowitz, anecdotal). Older descriptions of GPT style (heavy bold, clipped fragments, "Here's the..." openers) come from earlier generations, and nothing found for 5.5 or 6 confirms them.

The Codex final-message guidance comes from the OpenAI Codex prompting guide, of which only a secondary summary was used here.

Sources:

- OpenAI prompt guidance (GPT-5.5, GPT-6): https://developers.openai.com/api/docs/guides/prompt-guidance?model=gpt-5.5
- OpenAI GPT-5 prompting guide: https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide
- OpenAI Codex prompting guide (summary only): https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide
- Codex AGENTS.md (32 KiB combined limit): https://learn.chatgpt.com/docs/agent-configuration/agents-md
- EQ-Bench slop score: https://eqbench.com/slop-score.html
- Antislop (Paech et al., 2025): https://arxiv.org/pdf/2510.15061
- Zvi Mowshowitz on GPT-5.5 (anecdotal): https://thezvi.substack.com/p/gpt-55-capabilities-and-reactions

Verified: 2026-10

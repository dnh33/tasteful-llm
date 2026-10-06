# Modifier diseases: L1, L3, L6, L13, L14, L16

Patterns where excess adjectives, synonym stacking, stock vocabulary, tacked-on clauses, or unearned enthusiasm replace concrete information. Figures, version numbers and product details in Fix lines are placeholders or illustrative. Replace them with facts the user supplies.

---

## L1: Adjective Crutch

Status: unchecked · Seen in: all · Verified: 2026-04 (original)

**Slop:** "Our powerful, intuitive, enterprise-grade platform delivers seamless integration capabilities."

**Why it's slop:** Five adjectives doing the work that one fact should do. "Powerful" means nothing. "Intuitive" is what everyone claims. "Enterprise-grade" is a vibe, not a specification. "Seamless" has never been true of anything.

**Fix:** "Connects to your existing Salesforce and HubSpot data in one OAuth flow. No CSV exports. No field mapping."

---

## L3: Thesaurus Parade

Status: consistent · Seen in: all · Verified: 2026-10

**Slop:** "Streamline, optimize, and revolutionize your workflow."

**Why it's slop:** Three verbs that all mean "make better." This sentence uses thirty-seven characters to say nothing three times. The tricolon structure ("X, Y, and Z") invites padding with synonyms.

The rule covers the tricolon reflex too: three items as the default rhythm when the content has one or two. "Faster builds, cleaner code, happier teams." Two of those three are filler added to complete the beat. The same reflex appears as three adjectives, three clauses or three parallel sentences. Lists of three are fine when the content really has three things. The tell is a triple in every paragraph, or a third item that nobody could defend. Humans use the rule of three as well, so judge by density.

**Fix:** Pick one verb and make it concrete: "Cut your weekly reporting from [N hours] to [N minutes]." For a triple, keep the items you can prove and let the list be the length the content has.

**Sources:** Wikipedia, "Signs of AI writing", section "Rule of three" (section name not verified; https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing; page could not be fetched during verification, so treat as secondary); tropes.fyi (https://tropes.fyi/directory).

---

## L6: Enthusiasm Proxy

Status: unchecked · Seen in: all · Verified: 2026-04 (original)

**Slop:** "We're incredibly excited to announce our groundbreaking new feature!"

**Why it's slop:** Your excitement is not the reader's concern. "Groundbreaking" is a claim the reader gets to make, not you. Exclamation marks are a tell that the content is not exciting enough on its own.

**Fix:** "[Version] adds [feature]. [Who] can [do what] without [problem]." Let the feature be interesting. It does not need your emotional support.

---

## L13: Era Vocabulary

Status: fading · Seen in: all · Verified: 2026-10

**Slop:** "The intricate interplay of these pivotal factors underscores the enduring landscape of modern retail."

**Why it's slop:** Some words appear in model output far more often than in human writing: "delve", "tapestry", "intricate", "pivotal", "underscore", "showcase", "testament", "vibrant", "meticulous", "interplay". The words are not wrong. A cluster of them in one paragraph shows that the sentence was assembled from the model's favourites rather than from the facts. Kobak et al. counted 454 excess words in 2024 PubMed abstracts, mostly verbs and adjectives, with "delves" at 28 times the expected rate. Juzek and Ward trace the effect to preference tuning. "Delve" has faded in recent models, other words vary by model and release, and replacements appear once a word is suppressed, so this is a density rule and the word list is a sample. OpenAI's own prompt guidance for GPT-5.5 lists "delve", "foster", "leverage" and "genuinely" as words to avoid.

Threshold: flag a text with more than 2 era words per 500 words, or 2 in one paragraph. One "pivotal" in 800 words is fine. Any abstract showy verb or adjective that a plain word could replace belongs on the list.

**Fix:** State the claim with a concrete noun and a plain verb: "[Cost A] and [cost B] make up [N]% of a shop's costs, and both rose in [year]."

**Sources:** Kobak et al. (https://arxiv.org/pdf/2406.07016); Juzek and Ward (https://arxiv.org/abs/2412.11385); OpenAI prompt guidance (https://developers.openai.com/api/docs/guides/prompt-guidance?model=gpt-5.5).

---

## L14: Trailing -ing Gloss

Status: consistent · Seen in: all · Verified: 2026-10

**Slop:** "The team shipped weekly, ensuring alignment and fostering a culture of continuous improvement."

**Why it's slop:** A participial clause is attached to a plain fact to claim significance the writer has not shown. The main clause says what happened. The tail says it mattered, in words that fit any team. Opus 5.5 data from Graphite shows the tail moving to new phrasings ("adds another layer", "in practice") after older ones were suppressed, so match the function, not the verbs. The same move appears as ", highlighting...", ", reflecting...", ", underscoring...", ", contributing to...", and with "which" or "thereby".

**Fix:** Cut the tail, or replace it with the actual consequence: "The team shipped weekly. Bug reports fell from [N] to [N] a month."

**Sources:** Graphite (https://graphite.io/five-percent/research/ai-tells-opus-5-5-update); Wikipedia, "Signs of AI writing", section "Superficial analyses" (section name not verified; https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing; secondary summaries confirm the item).

---

## L16: Copula Dodge

Status: consistent · Seen in: all · Verified: 2026-10

**Slop:** "The dashboard serves as a central hub and boasts a rich set of features."

**Why it's slop:** "Is" and "has" were available and the sentence reached for something bigger. "Serves as", "stands as", "functions as", "boasts", "features", "offers" and "represents" each add a note of grandeur and no information. Any elevated verb standing in for a plain "is" or "has" counts. An occasional "features" or "offers" is fine. A paragraph where every sentence avoids "is" is the tell.

**Fix:** "The dashboard is the main screen. It has filters, saved views and CSV export."

**Sources:** tropes.fyi, "The Serves As dodge" (https://tropes.fyi/directory). Single catalogue; no independent measurement was reached during verification, so the confidence is medium.


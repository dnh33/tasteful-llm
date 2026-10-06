# Padding and fake structure: S3, S6, S7, S8, S9, S10

Structural patterns that pad content or impose artificial shape.

---

## S3: Filler Transition

Status: unchecked · Seen in: all · Verified: 2026-04 (original)

**Slop:** "But that's not all. Let's dive deeper into what makes our solution unique."

**Why it's slop:** This sentence is a hallway. The reader is walking through it to get to the next room. Every transition that tells the reader "I'm about to tell you something" instead of just telling them is a wasted sentence.

**Fix:** Delete the transition. Put the next section's content where the transition was. The reader understands section breaks.

---

## S6: Premature Framework

Status: unchecked · Seen in: all · Verified: 2026-04 (original)

**Slop:** "The 4 Pillars of Modern Data Management", which invents a named methodology when the content is just a list.

**Why it's slop:** AI loves this because it looks structured. It's often just a list wearing a costume. Frameworks earn their name through repeated use and validation, not because you capitalized the words.

**Fix:** If your content supports a list, write a list. Don't costume it as a methodology.

---

## S7: Mirror-Image Sections

Status: unchecked · Seen in: all · Verified: 2026-04 (original)

**Slop:** Problem paragraph → solution paragraph, repeated three times with identical sentence structure but different nouns.

**Why it's slop:** AI defaults to this parallelism because it's easy to generate. The repetitive structure becomes invisible: the reader stops reading after the first pair because they have already learned the pattern.

**Fix:** Break the parallelism. Vary structure between sections. Lead one with a quote, another with a number, another with a question.

---

## S8: Artificial Completeness

Status: consistent · Seen in: all · Verified: 2026-10

**Slop:** Exactly 5 tips. Exactly 7 steps. Exactly 3 takeaways. Round numbers when the content supports a different count.

**Why it's slop:** The roundness of the number reveals the list was shaped to a container rather than grown from the content. Real expertise rarely produces round numbers.

**Fix:** Let the content determine the count. If you have 4 things to say, say 4. Odd and non-round numbers signal authenticity.

---

## S9: Recap Reflex

Status: rising · Seen in: Claude (Opus 5.5) · Verified: 2026-10

**Slop:** A closing paragraph that restates the three points the reader just finished, introduced by "In short," "In summary," "Ultimately," or "Overall,".

**Why it's slop:** The reader has the points. Repeating them spends their time on information they already hold and signals that the writer ran out of new material. The same move shows up as a summary at the end of every section, or as a last line that circles back to the opening question. Pangram counted "in short" 100 times in 1,000 Opus 5.5 responses against 9 for Opus 5 (a 1,016 percent increase) and summarization markers up 942 percent. Older models used "in conclusion" (Wikipedia lists the habit; see Sources), and the habit came back in a newer model under a new phrase. Any final paragraph whose content is already in the text above it belongs here.

**Fix:** End on the last new fact or on the next action. A short document needs no summary at all.

**Sources:** Pangram (https://www.pangram.com/blog/can-pangram-detect-opus-5-5); Wikipedia, "Signs of AI writing" for the "in conclusion" habit (section name not verified; https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing; page could not be fetched during verification, so treat as secondary); tropes.fyi (https://tropes.fyi/directory).

---

## S10: Fragment Drama

Status: rising · Seen in: all · Verified: 2026-10

**Slop:** "He published this. Openly. In a book. As a priest."

**Why it's slop:** Sentence fragments and one-line paragraphs are used for punch on a steady beat, with no meaning attached to the break. After two or three, the effect is mechanical and the reader hears the rhythm instead of the point. Pangram found Opus 5.5 sentences about 14 percent shorter than Opus 5 with less variation in length, which fits this habit. Current models vary sentence length less than people do. It is a tendency and proves nothing about a single text. The same move appears as a column of short lines, a dramatic one-word paragraph, or a chain of "X. Y. Z." in place of a sentence.

**Fix:** Put the idea in one sentence and one paragraph. Use a fragment when it carries something a full sentence could not, and then once.

**Sources:** Pangram (https://www.pangram.com/blog/can-pangram-detect-opus-5-5); tropes.fyi (https://tropes.fyi/tropes/short-punchy-fragments).


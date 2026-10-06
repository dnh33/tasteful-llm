# Design/UI copy patterns, D1 through D5

Patterns where UI copy, page layout choices, and interface text create slop. Customer names and figures in Fix lines are placeholders for facts the user supplies.

---

## D1: Hero Starter Pack

Status: consistent · Seen in: all · Verified: 2026-10

**Slop:** A hero with gradient background, large sans-serif headline ("Transform Your [X]"), a vague subheadline, two buttons ("Get Started" / "Learn More"), and floating abstract shapes.

**Why it's slop:** This is the default output of ChatGPT + any template builder. It signals "nobody designed this." The tell is the distributional default: a choice made without a reason. Stock indigo, a single border radius, a single shadow, one font with no type scale, a gradient standing in for art direction, abstract shapes standing in for illustration, two competing buttons. Purple or Inter on their own prove little. The ai-design-tells project measured 202 design-led human sites and found about a third use purple and a quarter use Inter or system fonts (Stripe has 123 purple accents and scores 0). What separated AI pages was the exact default indigo, no type scale, one radius, one shadow, card-in-card and sparkle icons. Anthropic's frontend guidance says models converge on "on distribution" output, and models also converge on the replacement default once the first one is banned (its cookbook names Space Grotesk as an example). So swapping one default for another fixes nothing.

**Fix:** Choose one thing the visitor should do and give it one CTA. Write a headline that only works for your product. For every visual choice, be able to state the reason: one dominant color plus one accent as tokens, a real type scale with tighter tracking at display sizes, a radius and shadow hierarchy, a real image or illustration in place of floating shapes. Pin the choice to a concrete reference (hex values, a named font, a printed artifact) instead of "clean and modern."

**Sources:** ai-design-tells (https://pypi.org/project/ai-design-tells); Anthropic, "Prompting for frontend aesthetics" (https://platform.claude.com/cookbook/coding-prompting-for-frontend-aesthetics). The 202-site study is one project with self-reported methodology.

---

## D2: How-It-Works-3-Steps

Status: unchecked · Seen in: all · Verified: 2026-04 (original)

**Slop:** Step 1: Sign Up. Step 2: Connect Your Tools. Step 3: Get Insights.

**Why it's slop:** These three steps describe every SaaS product. They add no information. "Get Insights" is especially bad because it substitutes a vague noun for the actual thing the user gets.

**Fix:** Show the actual interface. Screenshot or animation of the real flow. If you must use steps, make them falsifiably specific: "Step 1: Paste your Notion workspace URL. Step 2: Pick which databases to sync. Step 3: See your first Slack summary at 9am tomorrow."

---

## D3: Logo Cloud Flex

Status: unchecked · Seen in: all · Verified: 2026-04 (original)

**Slop:** A grid of logos with "Trusted by industry leaders" above it.

**Why it's slop:** Everyone knows this trick. Logos without context are meaningless. "Industry leaders" is the caption that says "we have nothing specific to say about these relationships."

**Fix:** One logo, one quote and one metric: "[Customer name] reduced incident response time by [N]% using [product]." Use it only with the customer's permission and their real figure. If you don't have that story, you don't have social proof yet. Don't fake it.

---

## D4: Friendly Robot Voice

Status: unchecked · Seen in: all · Verified: 2026-04 (original)

**Slop:** "Whoops! Looks like something didn't go as planned."

**Why it's slop:** Performative personality masking absent information. The user doesn't need charm. They need to know what happened and what to do next.

**Fix:** "Save failed: changes couldn't be written to disk. Try again or check file permissions." Status, cause, action.

---

## D5: Success State Abandonment

Status: unchecked · Seen in: all · Verified: 2026-04 (original)

**Slop:** "Success!" (with no next action)

**Why it's slop:** After a user completes an action, "Success!" tells them nothing. What was saved? Where does it go now? What's the next action? Abandoning the user at the success state wastes the moment of highest engagement.

**Fix:** "Invoice sent to client@company.com. They'll receive it within [N] minutes. Send another?" State what happened, confirm the details, offer the next action.

# Week 4 — Instructor Notes

## Pacing (5 days)

- **Day 1:** prompt anatomy lecture (system vs user message, temperature);
  live-demo the same question with a good and a deliberately bad system
  prompt.
- **Days 2–3:** Exercise 4.1. This is where the project "comes alive" —
  expect (and encourage) teams to lose an hour just asking their bot things.
- **Day 4:** Exercise 4.2 (the app loop); stretch teams start Streamlit.
- **Day 5:** integration buffer + mini demo: every team shows one great
  answer and one failure. The failures seed Week 5.

## Pitfalls

- **The fallback that never fires:** vague instructions ("be honest if
  unsure") don't work on small models. The instruction must dictate the
  exact sentence to output. Even then phi-3.5-mini sometimes answers general
  knowledge (e.g. capital-of-France) from its own weights — a great
  discussion moment, not a student bug: grounding reduces, not eliminates,
  off-context answers. Mitigations: lower temperature, stricter wording,
  TOP_K context only.
- **Slow first answer:** model load takes ~10-30 s once per session; warn
  students before they diagnose a "hang". Subsequent answers are seconds.
  If a model was idle-unloaded, `resolve_model_id` reloads it transparently.
- **Context too big:** teams that crank TOP_K to 10 hit slow, rambling
  answers. 2–3 chunks is the sweet spot at our scale.
- **Streamlit reruns:** without `@st.cache_resource`, every browser
  interaction reconnects/reloads models. The provided solution shows the
  right pattern; point stretch teams at it early.
- Windows consoles + emoji in prompts can raise UnicodeEncodeError — keep
  system prompts ASCII (the solution's are).

## Model behavior notes (verified with this repo's solution)

- phi-3.5-mini follows the only-use-context rule well for product questions
  and declines Wi-Fi/decaf questions reliably with the exact-sentence prompt.
- It often prefixes answers with a space or "Answer:" — `.strip()` handles
  the former; don't chase the latter, it's cosmetic.
- Answer latency: roughly 2–8 s for short answers on a mid-range CPU laptop.

## Discussion prompts

- "Why do we send the context in the user message rather than the system
  message?" (system = durable rules; user = per-turn data. Also: some models
  weight system text differently.)
- "What's the difference between our bot failing to retrieve vs failing to
  generate?" — set up the Week 5 debugging mindset.
- "Should the bot remember previous questions?" (Multi-turn RAG is a real
  design problem — retrieval for follow-ups like "and how often?" needs the
  prior turn. Fine stretch topic for a strong team.)

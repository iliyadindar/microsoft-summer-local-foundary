# Week 1 — Instructor Notes

## Pacing (5 days)

- **Day 1:** program kickoff, RAG concept lecture, Exercise 1.1 (human RAG).
- **Day 2:** Foundry Local install party. Budget the WHOLE session — mixed
  Windows/macOS fleets always produce stragglers.
- **Day 3:** walk through `foundry_client.py` line by line; Exercise 1.3.
- **Day 4:** Python refresher as needed (functions, modules, `__main__`,
  virtual environments); Exercise 1.4.
- **Day 5:** buffer + team formation + pick/skim the sample documents.

## Setup pitfalls (collected the hard way)

- **First model download is GBs.** Have students run
  `foundry model download phi-3.5-mini` and `foundry model download qwen3-embedding-0.6b`
  early in the session, ideally staggered, or distribute the model cache from
  a USB drive on slow venue Wi-Fi.
- **`foundry` not on PATH** right after winget install → open a NEW terminal.
- **SDK drift:** pip's `foundry-local-sdk` 1.x does NOT match the 0.x API
  shown in most tutorials (`FoundryLocalManager(alias)` is gone). That's why
  the course ships `foundry_client.py`. If a student finds an old tutorial,
  point them at the warning box in the week README.
- **Low-spec laptops:** if `phi-3.5-mini` (2.5 GB) is too slow, swap
  `qwen2.5-0.5b` (822 MB) into the config — everything else is unchanged.
- The CLI subcommand is `foundry server` (older docs say `foundry service`).
- **GPU machines:** Foundry Local 0.10.2's daemon often fails to register GPU
  execution providers and silently serves CPU-only builds. Students with
  NVIDIA GPUs should use `tools/gpu_server.py` (see SETUP.md) — ~10x faster
  answers, auto-detected by all course code. Don't troubleshoot this during
  the install party; CPU works fine for the course.

## Discussion prompts

- "When would you NOT want RAG?" (creative writing, general knowledge, math)
- "Why does running locally matter?" (privacy, cost, offline, compliance)
- After 1.1: "What happens when the retriever hands over the wrong paragraph?"
  — plants the seed for Week 5 debugging (retrieval vs generation failures).

## Common misconceptions to correct early

- "RAG retrains the model" — no, the model is frozen; only the prompt changes.
- "The model searches the documents itself" — no, *our code* searches; the
  model only sees what we paste in.
- "Bigger model = better project" — for this course, response speed beats
  eloquence; students iterate far more with a 2-second model.

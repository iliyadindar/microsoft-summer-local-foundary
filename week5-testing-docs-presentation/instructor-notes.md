# Week 5 — Instructor Notes

## Pacing (5 days; stretch into a 6th week if available)

- **Day 1:** testing methodology lecture; teams design test plans (5.1).
- **Day 2:** run test plans + question swap between teams.
- **Day 3:** debugging clinic — teams fix their worst failures using the
  retrieval-vs-generation decision tree; adapt evaluate.py (5.2).
- **Day 4:** citations polish + documentation writing.
- **Day 5:** rehearsals (morning) + **demo day** (afternoon).

With a 6th week: spread testing over week 5, documentation + rehearsal +
demo day over week 6, and offer stretch goals (Streamlit, multi-turn chat,
sqlite-vec, a second document domain) to fast teams.

## Grading / assessment ideas (if the program needs it)

- 40% working pipeline (ingest → retrieve → answer, offline)
- 20% test plan quality and honest reporting of failures
- 20% documentation (README reproducibility test: a TA follows it cold)
- 20% presentation + demo

## Pitfalls

- **Teams "fix" failures by editing test questions** to match doc wording.
  Counter it with the blind question swap — that's why it's in the exercise.
- **Chunk-size changes without re-ingesting** — the DB still holds old
  chunks; nothing changes; team concludes chunk size doesn't matter.
  Re-ingest after every chunking change.
- **Over-tuning on one question** — a prompt tweak that fixes Q7 can break
  Q3; make teams re-run the WHOLE set after each change (evaluate.py makes
  this cheap).
- **The capital-of-France problem:** small models sometimes answer general
  knowledge despite the only-use-context rule. Frame it honestly in reports
  as a known limitation of prompt-level grounding — that IS the mature
  engineering answer.
- Demo-day machine ≠ dev machine: models must be pre-downloaded on whatever
  laptop presents. `foundry model list` shows the cache column.

## Demo day logistics

- Pre-flight every team 30 min before: service up, models cached, DB built.
- Have each team keep a recorded/screenshotted backup answer in case of a
  live hiccup — teaches professional demo hygiene.
- Invite the other cohort/faculty; a real audience transforms the energy.

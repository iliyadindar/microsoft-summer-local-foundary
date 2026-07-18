# Week 5 — Testing, Evaluation, Documentation & Demo Day

**Goal for the week:** turn a working prototype into a *trustworthy, polished,
presentable* project: systematic testing, targeted fixes, source citations,
written documentation, and a final presentation.

## 1. Functional testing

Test a Q&A bot with a **question set designed before you run it**, covering:

- **Answerable questions** — the answer is in the docs; the bot must state
  it correctly. Cover every document, and include paraphrases that share no
  words with the source text.
- **Unanswerable questions** — the answer is NOT in the docs; the bot must
  say the fallback sentence. A fluent invented answer is a *failure*, even
  if it happens to sound plausible.
- **Edge cases** — empty input, one-word questions, rambling questions.

### Exercise 5.1 — Design and run your test plan

Fill in [exercises/test-plan-worksheet.md](exercises/test-plan-worksheet.md),
run every question, and record results. Then **swap five questions with
another team** and run theirs blind — fresh phrasing finds failures your own
wording never triggers.

### Exercise 5.2 — Automate the boring half

The fallback check is mechanical, so script it:
[solutions/evaluate.py](solutions/evaluate.py) runs a question set, times
every answer, auto-verifies that unanswerable questions get declined, and
prints a report. Adapt it to your team's question set.

Note how it detects a decline: it looks for the *phrase* `"have that
information in my documents"`, not the exact fallback sentence. Small local
models sometimes garble the contraction in "I don't have…" while getting the
rest right. Matching a distinctive fragment tolerates that;
matching the whole sentence would report false failures on answers that were
actually correct. Keep this in mind when you adapt the fallback wording —
change the sentence in `chat.py` and you must change the fragment here too.

## 2. Debugging: retrieval or generation?

Every wrong answer has exactly two suspects. Find out which:

1. **Look at what was retrieved** (your app prints sources; `retrieve.py`
   shows full chunks and scores).
2. **Wrong/irrelevant chunks retrieved?** → a *retrieval* problem. Fixes:
   different chunk size (re-ingest!), higher TOP_K, rephrase-friendly
   document wording.
3. **Right chunks, wrong answer?** → a *generation* problem. Fixes: tighter
   system prompt, lower temperature, fewer distracting chunks, larger model.

Change **one variable at a time** and re-run the failing question.

**Performance:** answers should take a few seconds. If not: fewer chunks
(TOP_K), shorter chunks, or a smaller model. Never re-embed documents at
question time — that's what the database is for.

## 3. Polish: citations

The final reference app upgrades the system prompt so every answer ends with
its source — compare [solutions/chat.py](solutions/chat.py) with Week 4's
version (it's a ~4-line diff, all in the prompt). Grounded + cited = the
user can check the bot's homework.

`chat.py` is the only file that changed this week; `evaluate.py` is the only
one that's new. Everything else in [solutions/](solutions/) is byte-identical
to Week 4 — including
[solutions/streamlit_app.py](solutions/streamlit_app.py), which picks
up citations for free, because the change lives in the prompt rather than in
any interface code. If you took the Streamlit stretch goal in Week 4, it
needs no edits this week; `streamlit run streamlit_app.py` makes for a
better demo-day screen than a terminal.

## 4. Documentation

Write your project README using [REPORT-TEMPLATE.md](REPORT-TEMPLATE.md):
purpose, architecture, how to run it, design decisions, test results, known
limitations. Then clean the code: remove dead prints, comment the
non-obvious (why 800 chars? why temperature 0.2?), name things honestly.

## 5. Demo day

Structure (10 minutes per team) — details in
[presentation-guide.md](presentation-guide.md):

1. Problem statement — what does your assistant help whom do?
2. How it works — the RAG pipeline in one diagram.
3. **Live demo** — including one question it answers with a citation and one
   it correctly declines. Declining is a feature; show it off.
4. Lessons learned — your best bug story beats a feature list.

## Milestones — the program ends with

- [ ] A filled-in test plan with results for 12+ questions (yours + swapped)
- [ ] `evaluate.py` (adapted) passing: all unanswerable questions declined
- [ ] Answers that cite their source document
- [ ] A README that gets a stranger from `git clone` to a working assistant
- [ ] A rehearsed 10-minute demo

## Resources

- [MS Learn RAG tutorial](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-build-rag-application) (official)
- [Foundry Local troubleshooting](https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-best-practice) (official)

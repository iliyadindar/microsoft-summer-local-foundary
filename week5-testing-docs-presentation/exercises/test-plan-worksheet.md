# Week 5 Exercise: Test Plan Worksheet

Design your test set BEFORE running it. Fill in the tables, run each
question through your assistant, and record the outcome.

## 1. Answerable questions (aim for 8+)

Pick questions whose answers you can point to in `sample-docs/`. Cover
every document at least once, and include at least two questions that use
different words than the document does (that's what embeddings are for).

| # | Question | Expected answer (doc + fact) | Bot's answer correct? | Time (s) |
|---|----------|------------------------------|-----------------------|----------|
| 1 | | | | |
| 2 | | | | |

## 2. Unanswerable questions (aim for 4+)

Questions the docs do NOT answer. The correct behavior is the fallback
sentence — an invented answer is a FAIL, even a plausible one.

| # | Question | Bot declined correctly? | What it said instead |
|---|----------|-------------------------|----------------------|
| 1 | | | |

## 3. Edge cases

| Case | What happened? |
|------|----------------|
| Empty input | |
| One-word question ("descale?") | |
| Very long, rambling question | |
| Question in another language | |

## 4. Swap with another team

Trade five questions with another team and run theirs blind. Fresh eyes
find failures your own phrasing never triggers.

## 5. Improvement plan

For every failure above, note the suspected stage — retrieval (wrong
chunks came back) or generation (right chunks, wrong answer) — and one
change you will try. Retest after each change, one variable at a time.

| Failure | Stage | Change to try | Fixed? |
|---------|-------|---------------|--------|
| | | | |

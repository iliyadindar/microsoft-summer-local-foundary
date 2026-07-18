# Week 3 — Instructor Notes

## Pacing (5 days)

- **Day 1:** chunking lecture + read the sample docs together; hand-chunk one
  document on paper and argue about where the cuts go.
- **Days 2–3:** Exercise 3.1 (ingestion). The chunk_text merge loop is the
  week's hardest pure-programming moment for beginners — budget time.
- **Day 4:** Exercise 3.2 (retrieval).
- **Day 5:** retrieval quality bake-off: teams swap questions and compare
  which pipeline retrieves better; discuss why results differ (chunk size!).

## Pitfalls

- **Losing the last chunk** in chunk_text — the classic bug (forgetting to
  append `current` after the loop). Let them find it via the 15–35 count
  check rather than telling them upfront. (The reference solution produces
  27; a dropped last chunk lands below the range.)
- **Duplicate rows** after re-running ingestion — students who used
  `CREATE TABLE IF NOT EXISTS` without dropping/clearing first. Good teaching
  moment about idempotent scripts.
- **JSON round-trip forgotten** — comparing the query vector against the raw
  stored *string* produces a TypeError deep in numpy. The fix (`json.loads`)
  reinforces what's actually in the DB.
- **Different embedding model for query vs docs** — meaningless similarities,
  no error raised. Worth demonstrating deliberately once.
- Batch embedding: one API call per DOCUMENT (list of chunks), not one per
  chunk. Per-chunk calls work but are noticeably slower; nudge fast teams to
  time both.

## Verified reference numbers (this repo's solution, default config)

- 7 documents → **27 chunks** at MAX_CHUNK_CHARS=800 (section-aware chunking).
- Good top-1 similarities: ~0.55–0.75; absent-topic questions: ~0.3–0.45.
- Full ingestion: ~10–30 s on a mid-range CPU laptop (dominated by embedding).

## Discussion prompts

- "Where did hand-chunking disagree with the ~800-char rule? Who was right?"
- "Why store the source filename with every chunk?" (citations in Week 5 —
  and debugging: a wrong answer traces back to what was retrieved)
- "What would change if the documents were 10 GB?" (indexing, vector DBs,
  incremental ingestion — the scaling note in the README)

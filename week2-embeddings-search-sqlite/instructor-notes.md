# Week 2 — Instructor Notes

## Pacing (5 days)

- **Day 1:** embeddings lecture + intuition building. Draw 2-D vectors on the
  board ("espresso" and "coffee" pointing the same way, "soccer" sideways);
  emphasize the real thing is the same idea in 1024 dimensions.
- **Day 2:** Exercise 2.1. Fast finishers: plot pairwise similarities of the
  demo sentences as a table.
- **Day 3:** SQLite lecture + Exercise 2.2.
- **Day 4:** prompt engineering + Exercise 2.3.
- **Day 5:** synthesis: whiteboard the full RAG pipeline and label where each
  of this week's skills slots in. Design the Week 3 chunks table together.

## Pitfalls

- **`input=[query]` vs `input=query`** — the embeddings API wants a list;
  passing a bare string then indexing `.data[0]` works but confuses students
  later when batching. Teach the list form from the start.
- **Cosine similarity in pure Python** — some students will loop; that's fine,
  but show the numpy one-liner afterwards. Both are acceptable.
- Similarity scores for this embedding model cluster roughly in 0.3–0.8;
  warn students not to expect 0.99 for good matches or 0.0 for bad ones.
  Relative ranking is what matters, not absolute values.
- **sandbox.db lock errors** — happen when a previous run crashed mid-write
  in some editors' debug consoles. Fix: close the console or delete the file.
- Students with DB Browser for SQLite installed can open sandbox.db visually;
  it demystifies "the database is just a file."

## Discussion prompts

- "Why store embeddings instead of recomputing them?" (cost/time — do the
  math: N chunks × embedding time, every run)
- "Why does the escape-hatch instruction work?" (the model predicts likely
  text; the instruction makes 'I don't know' the likely continuation)
- "What breaks if we embed queries with a DIFFERENT model than documents?"
  (vectors live in different spaces — similarities become meaningless. This
  bites teams that change models without re-ingesting. It WILL come up in
  Week 5.)

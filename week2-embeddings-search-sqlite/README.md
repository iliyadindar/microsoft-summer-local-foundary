# Week 2 — Embeddings, Vector Search & SQLite

**Goal for the week:** master the three techniques the retrieval half of RAG
is built from: text embeddings, similarity search, and local storage with
SQLite. Plus first steps in prompt engineering.

## 1. Embeddings: numbers that capture meaning

An **embedding model** turns any text into a fixed-length list of numbers (a
**vector**) — our `qwen3-embedding-0.6b` produces 1024 of them. The magic
property: **texts with similar meaning get similar vectors**, even when they
share no words. "How long is the guarantee?" lands close to "Our warranty
lasts two years," far from "Cats are wonderful companions."

To measure "close," we use **cosine similarity**: 1.0 means identical
direction (same meaning), near 0 means unrelated.

```
similarity(a, b) = (a · b) / (|a| × |b|)
```

This is the engine of semantic search: embed all your documents once, embed
each query as it arrives, and rank documents by similarity to the query.

### Exercise 2.1 — Embedding demo

Complete [exercises/embedding_demo_starter.py](exercises/embedding_demo_starter.py).
Then try queries that share no words with their best match. Solution:
[solutions/embedding_demo.py](solutions/embedding_demo.py).

## 2. SQLite: the database that is just a file

Next week you'll embed dozens of document chunks, and they must survive
between program runs — recomputing embeddings on every start is wasteful.
That calls for a database.

[SQLite](https://www.sqlite.org/about.html) is perfect here: no server to
install or run, the whole database is a single file, and Python ships with
the `sqlite3` module built in. It's the most widely deployed database engine
in the world — it's in your phone, your browser, and your car.

SQL you need this week (that's genuinely all):

```sql
CREATE TABLE documents (id INTEGER PRIMARY KEY, source TEXT, content TEXT);
INSERT INTO documents (source, content) VALUES (?, ?);
SELECT content FROM documents WHERE id = 2;
SELECT source FROM documents WHERE content LIKE '%warranty%';
```

### Exercise 2.2 — SQL sandbox

Complete [exercises/sqlite_sandbox_starter.py](exercises/sqlite_sandbox_starter.py).
Solution: [solutions/sqlite_sandbox.py](solutions/sqlite_sandbox.py).

**Think about it:** `LIKE '%warranty%'` finds the word "warranty" — but
misses "how long is the guarantee?". Keyword search matches *letters*;
embedding search matches *meaning*. Next week you'll store embeddings **in**
SQLite and get the best of both: persistent storage + semantic search.

## 3. Prompt engineering: how you ask matters

Retrieving the right text is half the job; presenting it to the model is the
other half. Key ideas:

- **System prompt** — standing instructions that define the assistant's role
  and rules ("You are a support assistant... answer only from the context").
- **User prompt** — the actual question, plus the retrieved context.
- **The escape hatch** — explicitly tell the model what to say when the
  context doesn't contain the answer. Without it, models guess.

> 📖 Read: [Prompt engineering techniques](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/prompt-engineering)
> (official) — focus on prompt construction basics and system messages.

### Exercise 2.3 — Prompt experiments

Work through [exercises/prompt-experiments.md](exercises/prompt-experiments.md)
and fill in the observation table. Sample observations:
[solutions/prompt-experiments-notes.md](solutions/prompt-experiments-notes.md).

## Milestones — you're done with Week 2 when

- [ ] Your embedding demo ranks sentences by similarity to any query
- [ ] You can create, fill, and query a SQLite table from Python
- [ ] You've seen a model answer differently with vs. without provided context
- [ ] You can sketch the schema for storing chunks + embeddings (next week's DB)

## Resources

- [MS Learn RAG tutorial — embeddings & search sections](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-build-rag-application) (official)
- [SQLite: What is it?](https://www.sqlite.org/about.html) (official)
- [SQL tutorial](https://www.w3schools.com/sql/) (third-party, beginner-friendly)
- [Prompt engineering techniques](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/prompt-engineering) (official)

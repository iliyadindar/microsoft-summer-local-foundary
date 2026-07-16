# Week 3 — Data Ingestion & the Retrieval Pipeline

**Goal for the week:** build the retrieval half of your assistant for real:
chunk the documents, embed and store every chunk in SQLite, and write the
function that finds the right chunks for any question.

This week you work with the shared knowledge base in
[sample-docs/](../sample-docs/) — seven short documents about the fictional
**Contoso Roastery** coffee company (an espresso machine manual,
troubleshooting guide, grinder guide, filter FAQ, warranty policy, cleaning
schedule, and brewing guide). Fictional on purpose: the model can't have
memorized them, so every correct answer provably came from *your* pipeline.

## 1. Chunking: why and how

Embedding a whole document into one vector blurs all its topics together, and
pasting whole documents into prompts wastes the model's limited context
window. So we split documents into **chunks** of a few paragraphs each.

Trade-off to understand (you'll tune this in Week 5):

- **Too small** (one sentence) — precise retrieval, but the model loses
  surrounding explanation.
- **Too large** (whole document) — nothing gets lost, but retrieval gets
  fuzzy and prompts get huge.
- **Our default:** split at markdown headings, then merge paragraphs up to
  ~800 characters within each section.

One more trick that matters a lot in practice: **every chunk starts with its
document title and section heading** (e.g. `[Contoso Aurora X1 -
Troubleshooting Guide - Error Codes]`). A bare bullet list like "E03 -
descale required" doesn't mention the words "Aurora", "error", or "code" at
all — without the heading label, the embedding model can't tell what the
list is about, and retrieval misses it. We found this by hitting exactly
that bug while building the reference solution.

## 2. The ingestion pipeline

```
for each .md file:  read → chunk → embed (one batch call) → INSERT into SQLite
```

Table schema — the design you sketched last week:

```sql
CREATE TABLE chunks (
    id        INTEGER PRIMARY KEY,
    source    TEXT NOT NULL,   -- filename, for citations later
    content   TEXT NOT NULL,   -- the chunk text
    embedding TEXT NOT NULL    -- the vector as a JSON list (simple & inspectable)
);
```

Storing the vector as JSON text is deliberately low-tech: you can open the
database and *look at* your embeddings. (Production systems use binary blobs
or vector databases; the concept is identical.)

### Exercise 3.1 — Build the ingestion script

Complete [exercises/ingest_starter.py](exercises/ingest_starter.py). Verify:
re-running must not duplicate rows, and the chunk count should land in the
15–35 range (the reference solution produces 27). Solution: [solutions/ingest.py](solutions/ingest.py).

## 3. The retrieval function

The heart of the assistant, and it's ~20 lines:

1. Embed the incoming question (with the **same** embedding model!).
2. Load all chunk vectors from SQLite.
3. Compute cosine similarity between the question and every chunk.
4. Return the top-K chunks (we default to K=3).

Yes, we compare against *every* chunk — brute force. For a few hundred
chunks that costs milliseconds. **Scaling note:** at millions of chunks
you'd switch to a vector database (or a SQLite vector extension like
`sqlite-vec`), which builds an index to find near neighbors without checking
every row. Same idea, faster lookup — the pipeline shape doesn't change.

### Exercise 3.2 — Build and interrogate retrieval

Complete [exercises/retrieve_starter.py](exercises/retrieve_starter.py), then
stress-test it with your team:

- Ask about descaling, grinder settings, warranty — does the top chunk come
  from the right document?
- Ask with words the docs don't use ("how long is the guarantee?").
- Ask about something absent (Wi-Fi, decaf). Look at the scores — how do
  they differ from a good match? (Store this intuition for Week 5.)

Solution: [solutions/retrieve.py](solutions/retrieve.py).

## Milestones — you're done with Week 3 when

- [ ] `python ingest.py` builds a populated `rag.db` (15–35 chunks, no duplicates on re-run)
- [ ] `python retrieve.py "some question"` prints relevant chunks with scores
- [ ] Questions phrased in different words still hit the right document
- [ ] You can explain to another team why we chunk, and what changes at scale

## Resources

- [MS Learn RAG tutorial](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-build-rag-application) (official — our ingestion mirrors its embedding sections, extended with SQLite)
- [Local RAG blog — pipeline decisions](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/building-your-first-local-rag-application-with-foundry-local/4501968) (community)
- [sqlite-vec extension](https://github.com/asg017/sqlite-vec) (third-party, optional stretch)

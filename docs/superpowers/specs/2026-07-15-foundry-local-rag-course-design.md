# Design: Foundry Local RAG Course Repository

**Date:** 2026-07-15
**Status:** Approved

## Purpose

A complete, self-contained course repository for a one-month (5-week) full-time summer
program teaching beginner CS students to build a fully offline RAG (Retrieval-Augmented
Generation) Q&A assistant using Microsoft Foundry Local, Python, and SQLite. Based on the
Microsoft Tech Community "Building Your First Local RAG Application with Foundry Local"
pattern and the Microsoft Learn RAG tutorial.

## Decisions (user-approved)

- **Deliverable:** full course repo — weekly materials, exercises, instructor notes, and
  reference solutions.
- **Solutions:** progressive per-week snapshots. Each `weekN/solutions/` is a complete,
  runnable copy of the project as of that week's milestone, so students can run and diff
  any milestone standalone.
- **UI:** CLI question loop is the primary reference app; Streamlit app is a documented
  stretch goal (week 4).
- **Verification:** Foundry Local installed on the authoring machine; every week's
  solution snapshot is run end-to-end against the live service before completion.

## Repo layout

```
README.md                        program overview + navigation
SETUP.md                         Windows/macOS setup + verification
requirements.txt
sample-docs/                     6-8 short fictional markdown docs (shared knowledge base)
week1-rag-and-setup/
week2-embeddings-search-sqlite/
week3-ingestion-retrieval/
week4-llm-integration-app/
week5-testing-docs-presentation/
```

Each week folder: `README.md` (student lesson: objectives, concepts, official-resource
links, exercises), `instructor-notes.md` (pacing, pitfalls, discussion prompts),
`exercises/` (starter stubs), `solutions/` (runnable milestone snapshot).

Week 6 content from the original plan (documentation + presentations) folds into week 5.

## Reference app architecture (final form)

- `config.py` — model aliases (small chat model + embedding model), chunk size, top-K,
  DB path.
- `ingest.py` — read `sample-docs/`, chunk by paragraph groups, embed via Foundry Local,
  store (source, chunk_text, embedding JSON) in SQLite.
- `retrieve.py` — embed query, cosine similarity over all rows in Python, return top-K.
- `chat.py` — system prompt (answer only from context, cite sources, say "I don't know"
  when context is insufficient), call local chat model.
- `main.py` — CLI loop.
- `streamlit_app.py` — stretch goal (week 4+).
- `evaluate.py` — week 5: run a test-question set and record results.

Inference uses `foundry-local-sdk` (service/model management) + `openai` client pointed
at Foundry Local's OpenAI-compatible local endpoint — same pattern as the official
Microsoft RAG tutorial. Exact model aliases are pinned after live catalog verification.

## Milestone mapping

| Week | Solutions snapshot contains |
|------|----------------------------|
| 1 | `hello_model.py`, project skeleton `main.py` |
| 2 | embedding demo + cosine search, SQLite sandbox, prompt-experiment notes |
| 3 | ingestion pipeline + `get_top_chunks()` retrieval, populated DB schema |
| 4 | full CLI chatbot (+ Streamlit stretch) |
| 5 | final polished app: citations, fallback behavior, `evaluate.py`, report/presentation templates |

## Error handling & teaching considerations

- Every script checks that the Foundry Local service is reachable and prints a friendly
  actionable message (pointing to SETUP.md) instead of a stack trace.
- Embeddings stored as JSON text for transparency (students can inspect the DB).
- Brute-force cosine similarity is deliberate (small N); scaling note included in week 3.

## Testing

- Week 5 ships `evaluate.py` plus a test-question set (answerable + unanswerable).
- Author-side: each snapshot run end-to-end on the live service before delivery.

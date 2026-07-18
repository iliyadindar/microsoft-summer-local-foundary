# Local RAG AI Assistant — One-Month Course with Microsoft Foundry Local

A complete, self-contained summer program for beginner CS students: build an
**offline Q&A assistant** that answers questions about a document collection
using the RAG (Retrieval-Augmented Generation) pattern, with all AI running
locally via [Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/what-is-foundry-local)
— zero internet dependency at runtime, zero API costs.

The final project: a chatbot for the fictional **Contoso Roastery** that
answers questions about its product manuals in [sample-docs/](sample-docs/),
citing sources and declining questions the docs don't answer.

## Program at a glance

| Phase | Week | Folder | Milestone |
|-------|------|--------|-----------|
| 1 — Foundations | 1 | [week1-rag-and-setup/](week1-rag-and-setup/) | Foundry Local installed; first local LLM call |
| 1 — Foundations | 2 | [week2-embeddings-search-sqlite/](week2-embeddings-search-sqlite/) | Embedding similarity search + SQLite basics |
| 2 — Implementation | 3 | [week3-ingestion-retrieval/](week3-ingestion-retrieval/) | Documents chunked, embedded, stored; retrieval works |
| 2 — Implementation | 4 | [week4-llm-integration-app/](week4-llm-integration-app/) | **Working offline Q&A assistant** |
| 3 — Polish | 5 | [week5-testing-docs-presentation/](week5-testing-docs-presentation/) | Tested, cited, documented, demoed |

Each week folder contains:

- `README.md` — the student-facing lesson: concepts, curated official
  resources, and exercises
- `instructor-notes.md` — pacing, known pitfalls, discussion prompts
- `exercises/` — the week's hands-on work: starter `.py` files with TODOs and
  provided helpers in Weeks 1–4; Week 5's is a written worksheet instead,
  since that week is testing and documentation rather than new code
- `solutions/` — a **complete runnable snapshot** of the project as of that
  week's milestone. Any week runs standalone; diff week N against N+1 to see
  exactly what was added.

## Quick start (instructors / the impatient)

```
# 1. Install prerequisites — see SETUP.md (Python 3.10+, Foundry Local)
pip install -r requirements.txt     # or: pipenv install && pipenv shell

# 2. Run the finished assistant
cd week4-llm-integration-app/solutions
python ingest.py     # builds rag.db from ../../sample-docs (~30 s)
python main.py       # ask: "How often should I descale the machine?"
```

## Architecture (what students build)

```
                        ┌─────────────────────────── your laptop ───┐
 question ──▶ embed ──▶ │ SQLite: cosine similarity over all chunks │
                        │        ▼ top-3 chunks                     │
                        │ prompt = rules + chunks + question        │
                        │        ▼                                  │
                        │ local LLM (Foundry Local, phi-3.5-mini)   │──▶ answer + source
                        └───────────────────────────────────────────┘
```

- **Embedding model:** `qwen3-embedding-0.6b` (495 MB) — text → 1024-number vectors
- **Chat model:** `phi-3.5-mini` (2.5 GB) — swap for `qwen2.5-0.5b` on slow machines
- **Storage:** SQLite, one file, embeddings stored as inspectable JSON
- **Plumbing:** the provided `foundry_client.py` + the standard `openai` package
  against Foundry Local's OpenAI-compatible endpoint
- **GPU acceleration (optional):** [tools/gpu_server.py](tools/gpu_server.py)
  serves CUDA builds of the same models ~10x faster on NVIDIA GPUs; all
  course code picks it up automatically (see [SETUP.md](SETUP.md))

## Provenance

Curriculum inspired by the Microsoft Tech Community post
[Building Your First Local RAG Application with Foundry Local](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/building-your-first-local-rag-application-with-foundry-local/4501968)
and the official [Foundry Local documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/).
All reference code in this repo was verified end-to-end against Foundry
Local 0.10.2 on Windows 11 (July 2026). The Contoso Roastery documents are
fictional teaching material.

# Week 1 — RAG Concepts & Local AI Setup

**Goal for the week:** understand what RAG is and why it exists, get Foundry
Local running on your machine, and make your first local LLM call.

## 1. What problem does RAG solve?

Large language models answer from what they memorized during training. Ask
one about *your* documents — a course handout, a product manual, last week's
meeting notes — and it either admits ignorance or, worse, invents a
plausible-sounding answer (a **hallucination**).

**Retrieval-Augmented Generation (RAG)** fixes this in three steps:

1. **Retrieve** — find the passages in your documents most relevant to the question.
2. **Augment** — paste those passages into the prompt as context.
3. **Generate** — let the model write an answer *grounded in that context*.

The model never needs retraining; you just control what it reads before it
answers. Benefits: accurate answers about private data, fewer hallucinations,
and the ability to cite sources.

> 📖 Read: [Building Your First Local RAG Application with Foundry Local](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/building-your-first-local-rag-application-with-foundry-local/4501968)
> (intro and "What is RAG" sections — community blog).

### Exercise 1.1 — Human RAG (no computer needed)

In pairs, using one page from [sample-docs/](../sample-docs/): one of you is
the **retriever** (finds the relevant paragraph for a question), the other is
the **LLM** (answers using only what the retriever hands over — nothing
else). Swap roles. Notice: the "LLM" gives good answers *only* when the
retriever picks the right paragraph. Remember that when you debug in Week 5.

## 2. What is Foundry Local?

[Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/what-is-foundry-local)
is Microsoft's runtime for running LLMs **entirely on your own device** — no
cloud account, no API costs, no internet after the model is downloaded. It
ships a catalog of optimized open models (Phi, Qwen, Mistral, ...), picks the
best variant for your hardware (CPU/GPU/NPU), and exposes an
**OpenAI-compatible API** on `localhost`, so standard tooling just works.

That last part matters: the `openai` Python package — the same one used
against cloud APIs — talks to your local model by changing one URL.

### Exercise 1.2 — Install everything

Follow [SETUP.md](../SETUP.md) at the repo root. When you're done, this must work:

```
foundry model run phi-3.5-mini
```

Type a message, get a reply, then `/exit`. That conversation never left your laptop.

## 3. Your first program against a local model

The repo provides [foundry_client.py](exercises/foundry_client.py) — read it
top to bottom (it's ~115 lines). It does three things you'll rely on all month:
finds the local service, returns an `openai` client pointed at it, and turns a
friendly model alias like `phi-3.5-mini` into the exact id the service expects.

> ⚠️ Older Microsoft tutorials show `from foundry_local import FoundryLocalManager`.
> The `foundry-local-sdk` package changed its API in v1.x, so this course uses
> the CLI + OpenAI-compatible endpoint directly — same result, fewer surprises.

### Exercise 1.3 — Hello, model

Complete [exercises/hello_model_starter.py](exercises/hello_model_starter.py).
Compare with [solutions/hello_model.py](solutions/hello_model.py) *after*
yours runs.

### Exercise 1.4 — Project skeleton

Create your team's project folder with a `main.py` that has a proper entry
point (`if __name__ == "__main__":`). This folder grows into the full
assistant over the next three weeks. See [solutions/main.py](solutions/main.py).

## Milestones — you're done with Week 1 when

- [ ] `foundry model run phi-3.5-mini` gives you an interactive chat
- [ ] Your `hello_model.py` prints a model-generated completion
- [ ] Your project folder runs `python main.py` without errors
- [ ] You can explain retrieve → augment → generate to a teammate in under a minute

## Resources

- [What is Foundry Local?](https://learn.microsoft.com/azure/ai-foundry/foundry-local/what-is-foundry-local) (official)
- [Get started with Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started) (official)
- [Local RAG blog post](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/building-your-first-local-rag-application-with-foundry-local/4501968) (community)

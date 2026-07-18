# Week 4 — LLM Integration & Application Assembly

**Goal for the week:** connect last week's retrieval pipeline to the local
chat model and assemble a complete, working Q&A assistant.

## 1. Picking the chat model

The catalog (`foundry model list`) offers models from 0.5 GB to 12 GB. The
trade-off: **smaller answers faster, larger answers better.** For development
speed we default to `phi-3.5-mini` (2.5 GB, a few seconds per answer on a
typical laptop). If your machine struggles, drop to `qwen2.5-0.5b` in
[config.py](solutions/config.py) — one line, nothing else changes. Both were
downloaded in Week 1.

## 2. The augmented prompt

This is the "AG" of RAG. Two messages go to the model:

- **System message** — the standing rules. Ours must do three jobs:
  1. define the role ("support assistant for Contoso Roastery"),
  2. restrict the model to the provided context — *only* the context,
  3. give the exact fallback sentence for when the context doesn't help.
- **User message** — the retrieved chunks (each labeled with its source
  file), followed by the actual question.

Why label chunks with sources? Two reasons: the model can cite them (Week 5),
and *you* can debug — when an answer is wrong, the first question is always
"what did we actually retrieve?"

We also set `temperature=0.2`. Temperature controls randomness; low values
keep a support bot factual and repeatable. (Try 1.5 once for fun.)

### Exercise 4.1 — answer_query()

Complete [exercises/chat_starter.py](exercises/chat_starter.py) — it wires
`get_top_chunks()` into a chat completion. Test with the two built-in
questions: one answerable, one not. Solution: [solutions/chat.py](solutions/chat.py).

**First, bring Week 3 forward.** This week's `exercises/` folder has no
`ingest.py` or `retrieve.py`, but `chat_starter.py` imports `get_top_chunks`
from `retrieve` — copy your own working `config.py`, `ingest.py`, and
`retrieve.py` from Week 3 into this folder before you run anything, or the
import fails. (If Week 3 didn't come together, copy
[week3's solutions](../week3-ingestion-retrieval/solutions/) instead so you
aren't blocked.) Then run `python ingest.py` once to build `rag.db` here.

## 3. The interface

Three options, in increasing order of effort:

- **Option A — console loop (the reference path).** An `input()` loop that
  prints answers and which documents they came from. Guaranteed completable;
  all the intelligence is in the pipeline, not the UI.
- **Option B — Streamlit (stretch goal).** ~40 lines turn the same
  `answer_query()` into a chat web page: see
  [solutions/streamlit_app.py](solutions/streamlit_app.py). `pip install
  streamlit`, then `streamlit run streamlit_app.py`.
- **Option C — HTML + JS + Flask (stretch goal, web-dev flavored).** A static
  page posting to a tiny local API, like the original Tech Community blog
  did with Express.js. No reference implementation here — blaze the trail.

### Exercise 4.2 — Assemble the app

Build `main.py`: load models once at startup, then loop — read a question,
call `answer_query()`, print the answer and its sources, repeat until
"quit". Handle empty input and Ctrl-C gracefully. Solution:
[solutions/main.py](solutions/main.py).

Then **log what you retrieve** (print sources with every answer — the
solution does). Teams that can see their retrieval debug twice as fast in
Week 5.

## Running the finished reference app

```
cd week4-llm-integration-app/solutions
python ingest.py    # once — builds rag.db from ../../sample-docs
python main.py      # ask away
```

## Milestones — you're done with Week 4 when

- [ ] Your assistant answers document questions correctly through the full
      retrieve → augment → generate loop
- [ ] It says it doesn't know when asked about things outside the docs
- [ ] The interface survives empty input, long questions, and Ctrl-C
- [ ] Every answer shows which documents it drew from

**This is the core project milestone** — everything after this is polish.

## Resources

- [Foundry Local chat completions](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui) (official)
- [MS Learn RAG tutorial — generation sections](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-build-rag-application) (official)
- [Streamlit chat elements](https://docs.streamlit.io/develop/api-reference/chat) (third-party)

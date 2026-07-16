# <Assistant Name> — Project Report

*Team: <names> · Date: <date>*

## 1. What it is

Two or three sentences: who is the assistant for, what documents does it
know, and what can they ask it? (Example: "An offline support assistant for
Contoso Roastery customers. It answers questions about seven product
manuals and policies — setup, troubleshooting, cleaning, warranty — without
any internet connection.")

## 2. How it works

A short walk through your pipeline — a diagram is worth most of the words:

```
question → [embed] → [similarity search in SQLite] → top chunks
        → [prompt: rules + chunks + question] → [local LLM] → answer + source
```

Name the pieces: embedding model, chat model, database, and where each file
in your repo fits.

## 3. How to run it

Exact commands from a fresh clone. Test this section on a teammate's
machine — if they need to ask you anything, the section is incomplete.

```
# prerequisites: Python 3.10+, Foundry Local (see SETUP.md)
pip install -r requirements.txt
python ingest.py
python main.py
```

## 4. Design decisions

For each, one line of *what* and one of *why*. At minimum cover:

- Chunk size (what did you pick, what happened when you changed it?)
- TOP_K retrieved chunks
- Choice of chat model (speed vs quality on your hardware)
- System prompt (paste the final version and call out the load-bearing lines)

## 5. Test results

Summarize your filled-in test plan:

| Category | Passed | Total |
|----------|--------|-------|
| Answerable | | |
| Unanswerable (correctly declined) | | |
| Edge cases | | |

Then the honest part — the most instructive failures and what you did (or
couldn't do) about them.

## 6. Known limitations

What should a user NOT expect? (e.g., general knowledge may leak past the
context rule; follow-up questions aren't understood; document updates need
re-ingestion.)

## 7. What we'd build next

Two or three concrete ideas, one sentence each.

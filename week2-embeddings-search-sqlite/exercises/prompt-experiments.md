# Week 2 Exercise: Prompt Experiments

Grounding a model in context is the heart of RAG. Feel the difference
yourself before you build it in code.

Use any chat AI you have access to (Copilot, ChatGPT, or your local
`phi-3.5-mini` via `foundry model run phi-3.5-mini`).

## Experiment 1 — Without vs. with context

1. Ask: *"How often should I replace the PureFlow F2 filter cartridge?"*
   Record what happens. (The model has never heard of this product — does it
   admit that, or does it guess?)
2. Now paste a paragraph from `sample-docs/water-filter-faq.md` above the
   same question, prefixed with: *"Answer using only this information:"*
   Record the difference.

## Experiment 2 — The escape hatch

1. Give the model the same paragraph, but ask something it does NOT answer:
   *"Does Contoso sell decaf beans?"*
2. First without, then with this instruction:
   *"If the information provided doesn't contain the answer, say 'I don't
   know' instead of guessing."*
   Which version invents an answer?

## Experiment 3 — System-style instructions

Try telling the model who it is before the question:
*"You are a support assistant for Contoso Roastery. Answer briefly and
politely, and cite the source of your answer."*
How does tone and format change?

## Write down

| Experiment | Without instruction | With instruction |
|-----------|--------------------|--------------------|
| 1 | | |
| 2 | | |
| 3 | | |

Keep your notes — in Week 4 you will encode these lessons into your
assistant's system prompt.

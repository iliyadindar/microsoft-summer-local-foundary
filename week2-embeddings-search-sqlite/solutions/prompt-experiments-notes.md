# Prompt Experiments — Sample Observations (Solutions)

Your exact outputs will differ (models are not deterministic), but the
*patterns* below are what the exercise is designed to surface.

## Experiment 1 — Without vs. with context

| | Typical behavior |
|---|---|
| Without context | The model has never heard of the "PureFlow F2". Small local models often **invent** a generic answer ("every 3–6 months"); larger cloud models more often admit uncertainty — but not reliably. |
| With context | The model answers "every two months, or after 60 liters" — pulled straight from the pasted paragraph. Grounded, checkable, correct. |

**Lesson:** the same model becomes accurate the moment you hand it the right
text. RAG automates exactly this handover.

## Experiment 2 — The escape hatch

| | Typical behavior |
|---|---|
| Without the instruction | Asked about decaf beans with only filter-FAQ context, models frequently improvise ("Contoso offers a range of decaf options...") — a fluent hallucination. |
| With the instruction | The model says "I don't know." The instruction makes declining the *expected* continuation instead of an awkward one. |

**Lesson:** models complete text; they don't check facts. If you want honest
uncertainty, you must make it the most likely completion — by asking for it.

## Experiment 3 — System-style instructions

Typical changes: answers get shorter, adopt a consistent support-agent tone,
and start naming the source when asked to cite. Format instructions
("briefly", "politely", "cite the source") are followed more reliably than
content instructions — another reason the escape hatch needs to be explicit
and exact.

**Lesson for Week 4:** your assistant's system prompt should combine all
three findings: role + only-use-context rule + exact fallback sentence +
citation instruction.

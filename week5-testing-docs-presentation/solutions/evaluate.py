"""Week 5: run the test-question set through the assistant and report results.

    python evaluate.py

TEST_QUESTIONS holds (question, kind) pairs of two kinds:
- "answerable":   the answer IS in sample-docs — the bot should state it
- "unanswerable": the answer is NOT in the docs — the bot should say the
                  fallback sentence instead of making something up

The unanswerable checks are automatic; answerable ones still need your
eyes. Fallback detection matches loosely on the distinctive tail of the
sentence ("have that information in my documents") rather than the exact
full text, because small local models sometimes garble the contraction
"don't" in their output.
"""

import time

import config
from chat import FALLBACK_ANSWER, answer_query
from foundry_client import get_client, resolve_model_id

TEST_QUESTIONS = [
    ("How often should I replace the PureFlow F2 filter cartridge?", "answerable"),
    ("What does error code E03 mean on the Aurora X1?", "answerable"),
    ("What grinder setting should I use for French press?", "answerable"),
    ("How long is the warranty if I register my machine?", "answerable"),
    ("What temperature should milk be steamed to?", "answerable"),
    ("Why does my espresso taste sour?", "answerable"),
    ("Does Contoso sell decaf coffee beans?", "unanswerable"),
    ("Can the Aurora X1 connect to Wi-Fi?", "unanswerable"),
    ("What is the capital of France?", "unanswerable"),
]


def main():
    client = get_client()
    chat_id = resolve_model_id(client, config.CHAT_MODEL)
    embed_id = resolve_model_id(client, config.EMBEDDING_MODEL)

    correct_fallbacks = 0
    unanswerable_total = 0

    for question, kind in TEST_QUESTIONS:
        start = time.perf_counter()
        answer, chunks = answer_query(client, chat_id, embed_id, question)
        elapsed = time.perf_counter() - start

        used_fallback = "have that information in my documents" in answer.lower()
        if kind == "unanswerable":
            unanswerable_total += 1
            verdict = "PASS (declined)" if used_fallback else "FAIL (made something up?)"
            correct_fallbacks += used_fallback
        else:
            verdict = "check answer manually" if not used_fallback else "WARN (declined an answerable question)"

        print(f"\n[{kind}] {question}")
        print(f"  time: {elapsed:.1f}s | top source: {chunks[0][0]} | {verdict}")
        print(f"  answer: {answer}")

    print("\n" + "=" * 60)
    print(f"Unanswerable questions correctly declined: {correct_fallbacks}/{unanswerable_total}")
    print("Review the answerable ones above against sample-docs yourself.")


if __name__ == "__main__":
    main()

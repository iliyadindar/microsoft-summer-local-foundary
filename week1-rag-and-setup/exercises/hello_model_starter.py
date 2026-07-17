"""Week 1 exercise: your first local LLM call.

Goal: connect to Foundry Local and make the model complete a greeting.
Replace each `...` in main() following these steps, then run:

    python hello_model_starter.py

Steps (each matches one `...` below, in order):
1. Create a client with get_client().
2. Resolve the MODEL alias to a model id with resolve_model_id(client, MODEL).
3. Call client.chat.completions.create(...) with model=model_id,
   messages=[{"role": "user", "content": "<your prompt here>"}], and
   max_tokens=50.
4. Print the model's reply: response.choices[0].message.content

Hint: foundry_client.py (provided, in this folder) does the connection
plumbing for you — read it, you'll use it every week.
"""

from foundry_client import get_client, resolve_model_id

MODEL = "phi-3.5-mini"


def main():
    client = ...

    model_id = ...

    response = ...

    print("Model says:", ...)


if __name__ == "__main__":
    main()

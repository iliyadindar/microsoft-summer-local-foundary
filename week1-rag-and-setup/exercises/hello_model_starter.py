"""Week 1 exercise: your first local LLM call.

Goal: connect to Foundry Local and make the model complete a greeting.
Fill in the TODOs, then run:  python hello_model_starter.py

Hint: foundry_client.py (provided, in this folder) does the connection
plumbing for you — read it, you'll use it every week.
"""

from foundry_client import get_client, resolve_model_id

MODEL = "phi-3.5-mini"


def main():
    # TODO 1: create a client with get_client()
    client = ...

    # TODO 2: resolve the MODEL alias to a model id with resolve_model_id(...)
    model_id = ...

    # TODO 3: call client.chat.completions.create(...) with
    #   - model=model_id
    #   - messages=[{"role": "user", "content": "<your prompt here>"}]
    #   - max_tokens=50
    response = ...

    # TODO 4: print the model's reply
    # Hint: response.choices[0].message.content
    print("Model says:", ...)


if __name__ == "__main__":
    main()

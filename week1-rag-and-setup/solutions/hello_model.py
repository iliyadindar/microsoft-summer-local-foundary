"""Week 1 milestone: prove Foundry Local works by generating one completion,
entirely on this machine.

    python hello_model.py
"""

from foundry_client import get_client, resolve_model_id

MODEL = "phi-3.5-mini"


def main():
    client = get_client()
    model_id = resolve_model_id(client, MODEL)
    print(f"Connected to Foundry Local. Using model: {model_id}\n")

    response = client.chat.completions.create(
        model=model_id,
        messages=[
            {
                "role": "user",
                "content": "Complete this greeting in one short sentence: Hello, world!",
            }
        ],
        max_tokens=50,
    )
    print("Model says:", response.choices[0].message.content.strip())


if __name__ == "__main__":
    main()

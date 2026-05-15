import ollama


def rewrite_text(text):
    if not text:
        return ""

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": f"Rewrite this news text professionally: {text}"
            }
        ]
    )

    return response['message']['content']
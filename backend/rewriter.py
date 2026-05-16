import ollama


def rewrite_text(text):
    if not text:
        return ""

    try:
        response = ollama.chat(
            model="llama3",
            messages=[
                {
                    "role": "user",
                    "content": f"Rewrite this news professionally while preserving meaning: {text}"
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        print("Rewrite error:", e)
        return text
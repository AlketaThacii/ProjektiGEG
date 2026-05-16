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
                    "content": f"Rewrite this title or description professionally in one sentence only and preserve meaning: {text}"
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        print("Ollama error:", e)
        return text
import os
from groq import Groq
from llm.prompts import SYSTEM_PROMPT

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("GROQ_MODEL", "llama-3.1-70b-versatile")

client = Groq(api_key=GROQ_API_KEY)


def ask_groq(user_message: str) -> str:
    if not GROQ_API_KEY:
        return "API ключ не найден. Позови администратора 😅"

    chat = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
        temperature=0.6,
        max_tokens=800,
    )

    return chat.choices[0].message.content.strip()

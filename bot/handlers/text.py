from telegram import Update
from telegram.ext import ContextTypes
from llm.groq_client import ask_groq
from storage.sqlite import load_prefs, save_prefs


async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.strip()
    user_id = update.message.from_user.id

    if context.user_data.get("awaiting_prefs"):
        save_prefs(user_id, user_text)
        context.user_data["awaiting_prefs"] = False
        await update.message.reply_text("Записал твои предпочтения 🧠🍽")
        return

    prefs = load_prefs(user_id)
    prefs_text = f"\n\nПредпочтения пользователя: {prefs}" if prefs else ""

    prompt = (
        "Пользователь пишет про планирование питания.\n"
        f"Запрос: {user_text}"
        f"{prefs_text}"
    )

    reply = ask_groq(prompt)
    await update.message.reply_text(reply)

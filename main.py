import os
from telegram.ext import ApplicationBuilder
from bot.router import setup_handlers

TOKEN = os.getenv("TELEGRAM_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # https://project.railway.app/webhook

def main():
    if not TOKEN:
        raise RuntimeError("TELEGRAM_TOKEN не найден в переменных окружения")

    app = ApplicationBuilder().token(TOKEN).build()

    setup_handlers(app)

    app.run_webhook(
        listen="0.0.0.0",
        port=int(os.getenv("PORT", 8080)),
        url_path=TOKEN,
        webhook_url=f"{WEBHOOK_URL}/{TOKEN}"
    )

if __name__ == "__main__":
    main()

from telegram import Update
from telegram.ext import ContextTypes
from bot.handlers.commands import (
    menu_command,
    recipes_command,
    shoppinglist_command,
    preferences_command
)


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    mapping = {
        "menu": menu_command,
        "recipes": recipes_command,
        "shoppinglist": shoppinglist_command,
        "preferences": preferences_command,
    }

    handler = mapping.get(query.data)
    if handler:
        await handler(update, context)
    else:
        await query.message.reply_text("Эта кнопка пока в отпуске.")

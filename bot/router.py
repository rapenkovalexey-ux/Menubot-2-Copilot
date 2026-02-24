from telegram.ext import (
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters
)

from bot.handlers.commands import (
    start,
    help_command,
    menu_command,
    recipes_command,
    shoppinglist_command,
    preferences_command
)

from bot.handlers.callbacks import button_handler
from bot.handlers.text import text_handler


def setup_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("menu", menu_command))
    app.add_handler(CommandHandler("recipes", recipes_command))
    app.add_handler(CommandHandler("shoppinglist", shoppinglist_command))
    app.add_handler(CommandHandler("preferences", preferences_command))

    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))

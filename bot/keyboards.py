from telegram import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu_keyboard():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("📅 Меню", callback_data="menu"),
                InlineKeyboardButton("📖 Рецепты", callback_data="recipes"),
            ],
            [
                InlineKeyboardButton("🛒 Покупки", callback_data="shoppinglist"),
                InlineKeyboardButton("⚙️ Предпочтения", callback_data="preferences"),
            ],
        ]
    )

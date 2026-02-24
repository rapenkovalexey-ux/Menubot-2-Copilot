from telegram import Update
from telegram.ext import ContextTypes
from bot.keyboards import main_menu_keyboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Привет! Я — Меню‑Мастер 3000 🍽\n"
        "Твой личный шеф‑планировщик, диетолог‑любитель и мастер списков покупок.\n\n"
        "Я умею:\n"
        "• Составлять меню на день, неделю или месяц\n"
        "• Подбирать рецепты по продуктам\n"
        "• Делать списки покупок\n"
        "• Учитывать диеты, аллергии и бюджет\n\n"
        "Нажимай кнопки или пиши, что хочешь приготовить."
    )
    await update.message.reply_text(text, reply_markup=main_menu_keyboard())


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Вот мои суперспособности:\n\n"
        "/menu — составить меню\n"
        "/recipes — подобрать рецепты\n"
        "/shoppinglist — список покупок\n"
        "/preferences — настроить предпочтения\n\n"
        "Можешь писать в свободной форме: "
        "«Сделай меню на неделю» или «Подбери рецепты из курицы и риса»."
    )
    await update.message.reply_text(text)


async def menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Окей, делаем меню! 🧾\n"
        "Напиши: на какой период, для кого и с какими ограничениями."
    )


async def recipes_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Подбираю рецепты! 😋\n"
        "Напиши продукты через запятую. Можно добавить время."
    )


async def shoppinglist_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Список покупок? Легко 🛒\n"
        "Напиши, на какой период меню или что планируешь готовить."
    )


async def preferences_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Настраиваем предпочтения ⚙️\n"
        "Напиши:\n"
        "• Диету\n"
        "• Аллергии\n"
        "• Бюджет\n"
        "• Количество порций\n"
        "• Технику\n\n"
        "Я всё запомню."
    )
    context.user_data["awaiting_prefs"] = True

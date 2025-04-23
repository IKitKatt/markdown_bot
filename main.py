import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
if not TELEGRAM_TOKEN:
    raise ValueError("Не указан TELEGRAM_TOKEN в переменных окружения")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Отправь мне текст в формате Markdown, и я преобразую его в разметку Telegram."
    )

async def handle_markdown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    try:
        await update.message.reply_markdown(user_message)
    except Exception as e:
        logger.error(f"Ошибка при обработке Markdown: {e}")
        await update.message.reply_text(
            "Произошла ошибка при обработке Markdown. Проверьте правильность разметки."
        )

def main():
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_markdown))
    application.run_polling()

if __name__ == '__main__':
    main()
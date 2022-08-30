import logging
import os

from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from commands.fact import fact
from commands.joke import joke
from commands.quote import quote
from commands.dict import dict
from commands.start import start
from commands.help import help
from commands.word import word
from commands.image import image

TOKEN = os.getenv("TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


def main():
    """Start the bot."""
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("quote", quote))
    app.add_handler(CommandHandler("joke", joke))
    app.add_handler(CommandHandler("fact", fact))
    app.add_handler(CommandHandler("word", word))
    app.add_handler(CommandHandler("image", image))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, dict))

    app.run_polling()


if __name__ == "__main__":
    main()

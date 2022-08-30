from utils import random_word


async def word(update, context):
    """Send a random word from the API"""
    word_en, word_id = random_word()
    await update.message.reply_text(
        f"<b>[ENGLISH]</b>\n{word_en}\n\n<b>[INDONESIA]</b>\n{word_id}",
        parse_mode="HTML",
    )

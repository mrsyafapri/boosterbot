from utils import random_joke


async def joke(update, context):
    """Send a random joke from the API"""
    joke_en, joke_id = random_joke()
    await update.message.reply_text(
        f"<b>[ENGLISH]</b>\n{joke_en}\n\n<b>[INDONESIA]</b>\n{joke_id}",
        parse_mode="HTML",
    )

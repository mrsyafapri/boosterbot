from utils import random_fact


async def fact(update, context):
    """Send a random fact from the API"""
    fact_en, fact_id = random_fact()
    await update.message.reply_text(
        f"<b>[ENGLISH]</b>\n{fact_en}\n\n<b>[INDONESIA]</b>\n{fact_id}",
        parse_mode="HTML",
    )

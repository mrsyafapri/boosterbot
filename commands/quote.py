from utils import random_quote


async def quote(update, context):
    """Send a random quote from the API"""
    quote_en, quote_id, author, tags = random_quote()
    if quote_en and quote_id and author:
        await update.message.reply_text(
            f"Tag - {tags}\n\n<b>[ENGLISH]</b>\n<i>{quote_en}</i> - {author}\n\n<b>[INDONESIA]</b>\n<i>{quote_id}</i> - {author}",
            parse_mode="HTML",
        )
    else:
        await update.message.reply_text(
            f"<b>[ENGLISH]</b>\n{quote_en}\n\n<b>[INDONESIA]</b>\n{quote_id}",
            parse_mode="HTML",
        )

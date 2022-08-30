async def start(update, context):
    """Start using this bot"""
    user = update.message.from_user
    await update.message.reply_text(
        f'Hii <b>{user.first_name} {user.last_name}</b>!👋\n\nSelamat menikmati Booster Bot. Bot ini memiliki beberapa fitur yang bisa kamu gunakan ketika lagi gabut, hehe..\n\nKamu bisa menggunakan perintah /help untuk melihat perintah/fitur yang tersedia.\n\nCreated by <a href="https://github.com/mrsyafapri">@mrsyafapri</a>',
        parse_mode="HTML",
    )

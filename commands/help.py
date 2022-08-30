async def help(update, context):
    """Get help with the available commands"""
    await update.message.reply_text(
        'Fitur yang tersedia:\n- /quote : menampilkan quote secara random\n- /joke : menampilkan joke secara random\n- /fact : menampilkan fakta secara random\n- /word : menampilkan kata inggris-indonesia secara random\n- /image : menampilkan gambar secara random\n- EN word: Menampilkan kamus/dictionary dari bahasa Inggris. Contoh: EN code, akan menampilkan kamus dari "code"\n- ID kata: Menampilkan kamus/dictionary dari bahasa Indonesia. Contoh: ID rumah, akan menampilkan kamus dari "rumah"\n- /help : menampilkan bantuan',
    )

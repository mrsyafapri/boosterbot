from utils import dict_en, dict_id


async def dict(update, context):
    """Search for a word in the dictionary"""
    word_command = update.message.text.lower()
    word_command = word_command.split()
    try:
        language_id = word_command[0].lower()
        word = word_command[1].lower()
        if language_id == "en":
            first_en, second_en, first_id, second_id, pronunciation = dict_en(word)
            if second_en and second_id and pronunciation:
                await update.message.reply_text(
                    f"EN - {word} [{pronunciation}]\n\n<b>[ENGLISH]</b>\n- {first_en}\n- {second_en}\n\n<b>[INDONESIA]</b>\n- {first_id}\n- {second_id}",
                    parse_mode="HTML",
                )
            elif second_en and second_id:
                await update.message.reply_text(
                    f"EN - {word}\n\n<b>[ENGLISH]</b>\n- {first_en}\n- {second_en}\n\n<b>[INDONESIA]</b>\n- {first_id}\n- {second_id}",
                    parse_mode="HTML",
                )
            elif first_en and first_id:
                await update.message.reply_text(
                    f"EN - {word}\n\n<b>[ENGLISH]</b>\n{first_en}\n\n<b>[INDONESIA]</b>\n{first_id}",
                    parse_mode="HTML",
                )
            elif pronunciation:
                await update.message.reply_text(
                    f"EN - {word} [{pronunciation}]\n\n<b>[ENGLISH]</b>\n{first_en}\n\n<b>[INDONESIA]</b>\n{first_id}",
                    parse_mode="HTML",
                )
            else:
                await update.message.reply_text(
                    f"EN - {word}\n\n<b>[ENGLISH]</b>\nDictionary not found\n\n<b>[INDONESIA]</b>\nKamus tidak ditemukan",
                    parse_mode="HTML",
                )
        elif language_id == "id":
            first_id, second_id, first_en, second_en, pronunciation = dict_id(word)
            if second_id and second_en:
                await update.message.reply_text(
                    f"ID - {word} [{pronunciation}]\n\n<b>[INDONESIA]</b>\n- {first_id}\n- {second_id}\n\n<b>[ENGLISH]</b>\n- {first_en}\n- {second_en}",
                    parse_mode="HTML",
                )
            elif first_en and first_id:
                await update.message.reply_text(
                    f"ID - {word} [{pronunciation}]\n\n<b>[INDONESIA]</b>\n{first_id}\n\n<b>[ENGLISH]</b>\n{first_en}",
                    parse_mode="HTML",
                )
            else:
                await update.message.reply_text(
                    f"ID - {word}\n\n<b>[INDONESIA]</b>\nKamus tidak ditemukan\n\n<b>[ENGLISH]</b>\nDictionary not found",
                    parse_mode="HTML",
                )
        else:
            await update.message.reply_text(
                "<b>[ENGLISH]</b>\nSorry, I don't know this language\n\n<b>[INDONESIA]</b>\nMaaf, saya tidak tahu bahasa ini",
                parse_mode="HTML",
            )
    except IndexError:
        await update.message.reply_text(
            "<b>[ENGLISH]</b>\nCommand not available! Please use /help to see the available commands\n\n<b>[INDONESIA]</b>\nPerintah tidak tersedia! Silakan gunakan /help untuk melihat perintah yang tersedia",
            parse_mode="HTML",
        )

from utils import random_image


async def image(update, context):
    """Send a random image from Unsplash."""
    image = random_image()
    if image:
        await update.message.reply_photo(image)
    else:
        await update.message.reply_text("Image not found")

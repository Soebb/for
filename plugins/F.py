from pyrogram import Client, filters
from pyrogram.errors import FloodWait


@Client.on_message(filters.channel & filters.edited & (filters.video | filters.document))
async def autopost(bot, update):
    media = update.document or update.audio
    if (update.chat.id == -1001264182630):
        try:
            await update.copy(chat_id=-1001448973320)
        except Exception as error:
            print(error)

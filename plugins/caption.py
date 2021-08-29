from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait

chnls = "-1001166919373 -1001437520825 -1001071120514 -1001546442991 -1001322014891 -1001409508844 1001448973320"
CHANNELS = set(int(x) for x in chnls.split())


@Client.on_message(filters.media & filters.channel)
async def caption(bot, message: Message):
    media = message.video or message.document
    if (media is not None) and (media.file_name is not None):
        try:
            H = await bot.get_history_count(message.chat.id)
            print(H)
            F = await bot.get_messages(message.chat.id, H)
            print(F.file_name)
        except Exception as e:
            print(e)

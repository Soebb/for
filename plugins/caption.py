from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait

chnls = "-1001166919373 -1001437520825 -1001071120514 -1001546442991 -1001322014891 -1001409508844"
CHANNELS = set(int(x) for x in chnls.split())


@Client.on_message(filters.media & filters.channel)
async def caption(client, message: Message):
    media = message.video or message.audio
    if (media is not None) and (not message.chat.id in CHANNELS):
        try:
            await message.edit("g")
        except Exception as e:
            print(e)

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from time import sleep

chnls = "-1001166919373 -1001437520825 -1001071120514 -1001546442991 -1001322014891 -1001409508844"
CHANNELS = set(int(x) for x in chnls.split())


@Client.on_message(filters.media & filters.channel)
async def caption(client, message: Message):
    media = message.document or message.audio
    if (media is not None) and (not message.chat.id in CHANNELS):
        try:
            Msg = await message.edit("g")
            
            if (message.chat.id == -1001264182630):
                try:
                    await Msg.copy(chat_id=-1001448973320)
                except Exception as error:
                    print(error)
        except Exception as e:
            print(e)



import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/5038581574350d95f3a7f.jpg",
        caption=f"""**Karnataka da athi uttama Music bot tayar madiddu [Mr and Mrs Agora](https://t.me/mr_agora)

ಮಾಲೀಕರು :- [ಶ್ರೀ ಮತ್ತು ಶ್ರೀಮತಿ ಅಘೋರ](https://t.me/Mr_Agora)
ಮಾಲೀಕರ ಅಡ್ಡ:- [ಅಡ್ಡ](https://t.me/BROTHERS_TERRITORY)
ಮಾಲೀಕರ ಸಾಮ್ರಾಜ್ಯ :- [ಅಘೋರ](https://t.me/AGORA_talks)

 Artha agtilwa Tele kedaskobeda Nam bot owner chinnadanta manasu yelrigu help madtare avrna kelu sari na chinna[Nam Owner Sir](https://t.me/mr_agora)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ಕರ್ನಾಟಕ ಹುಳಿಗೊಳ್ ಅಡ್ಡ", url=f"https://t.me/BROTHERS_TERRITORY")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/5038581574350d95f3a7f.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙍𝙚𝙥𝙤", url=f"https://t.me/agoraempire")
                ]
            ]
        ),
    )

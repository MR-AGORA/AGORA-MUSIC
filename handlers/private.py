import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/51c02857aa306a105fcce.jpg",
        caption=f"""**𝗧𝗛𝗜𝗦 𝗜𝗦 𝗕𝗘𝗦𝗧 𝗕𝗢𝗧 𝗗𝗔𝗡𝗚𝗘𝗥𝗢𝗨𝗦 𝗙𝗜𝗚𝗛𝗧𝗘𝗥𝗦 𝗠𝗔𝗗𝗘 𝗕𝗬 [𝗦𝟭𝟮𝗞 𝗚𝗔𝗠𝗘𝗥 𝗬𝗧 𝗢𝗣](https://t.me/S12K_GAMER_YT_OP)

𝗖𝗥𝗘𝗔𝗧𝗢𝗥 :- [𝗦𝟭𝟮𝗞 ](https://t.me/DANGEROUSFIGHTERS)
𝗧𝗘𝗥𝗥𝗜𝗧𝗢𝗥𝗬 :- [𝗖𝗟𝗨𝗕](https://t.me/BROTHERS_TERRITORY)
𝗨𝗣𝗗𝗔𝗧𝗘𝗦 :- [𝗔𝗚𝗢𝗥𝗔](https://t.me/AGORAEMPIRE)

 𝗜𝗙 𝗬𝗢𝗨 𝗪𝗢𝗡𝗧 𝗨𝗡𝗗𝗘𝗥𝗦𝗧𝗔𝗡𝗗 𝗔𝗡𝗬𝗧𝗛𝗜𝗡𝗚 𝗔𝗦𝗞 𝗧𝗢 [𝗕𝗜𝗚 𝗕𝗥𝗢𝗧𝗛𝗘𝗥](https://t.me/mr_agora)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗕𝗥𝗢𝗧𝗛𝗘𝗥𝗦 𝗖𝗟𝗨𝗕", url=f"https://t.me/BROTHERS_TERRITORY")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/51c02857aa306a105fcce.jpg",
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

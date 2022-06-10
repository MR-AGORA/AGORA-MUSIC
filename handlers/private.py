import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/2add091f8824a47e82c98.jpg",
        caption=f"""**𝐓𝐇𝐄 𝐁𝐄𝐒𝐓 𝐌𝐔𝐒𝐈𝐂 𝐁𝐎𝐓 𝐏𝐋𝐀𝐘𝐄𝐃 𝐈𝐍 𝐕𝐎𝐈𝐂𝐄 𝐂𝐇𝐀𝐓𝐒 𝐎𝐅 𝐆𝐑𝐎𝐔𝐏 , 𝐌𝐀𝐃𝐄 𝐖𝐈𝐓𝐇 𝐋𝐎𝐕𝐄 𝐀𝐍𝐃 𝐇𝐀𝐑𝐃𝐖𝐎𝐑𝐊 𝐁𝐘 [𝐒𝐀𝐑𝐊𝐀𝐑 𝐀𝐆𝐎𝐑𝐀 ](https://t.me/mr_agora)

𝐂𝐑𝐄𝐀𝐓𝐎𝐑 :- [𝐒𝐀𝐑𝐊𝐀𝐑 𝐀𝐆𝐎𝐑𝐀](https://t.me/Mr_Agora)
𝐓𝐄𝐑𝐑𝐈𝐓𝐎𝐑𝐘:- [𝐓𝐄𝐀𝐌 𝐀𝐆𝐎𝐑𝐀](https://t.me/team_agora)
𝐁𝐎𝐓𝐒 𝐄𝐌𝐏𝐈𝐑𝐄 :- [𝐀𝐆𝐎𝐑𝐀 𝐁𝐎𝐓𝐒](https://t.me/AGORa_ROBOTS)

 𝐅𝐈𝐑𝐒𝐓 𝐉𝐎𝐈𝐍 𝐓𝐇𝐈𝐒 𝐆𝐑𝐎𝐔𝐏 @TEAM_AGORA 𝐁𝐄𝐅𝐎𝐑𝐄 𝐔𝐒𝐈𝐍𝐆 𝐓𝐇𝐄 𝐁𝐎𝐓 𝐀𝐍𝐃 𝐇𝐄𝐑𝐄 𝐈𝐒 𝐓𝐇𝐄 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 𝐎𝐅 [𝐎𝐖𝐍𝐄𝐑](https://t.me/mr_agora)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐀𝐆𝐎𝐑𝐀 𝐁𝐎𝐓𝐒 𝐒𝐔𝐏𝐏𝐎𝐑𝐓", url=f"https://t.me/AGORA_MUSICWORLD")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/2add091f8824a47e82c98.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐑𝐄𝐏𝐎", url=f"https://t.me/team_agora")
                ]
            ]
        ),
    )

import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/710838c4451e8f5f08c91.jpg",
        caption=f"""**ಕರ್ನಾಟಕ ದ ಅತೀ ಉತ್ತಮ ಮತ್ತ ಗಿಚ್ಚಿ ಗಿಲಿ ಗಿಲಿ ಮುಸಿಕ್ ರೋಬೋಟ್ ನಮ್ಮ [ಶ್ರೀ ಮತ್ತು ಶ್ರಿಮತಿ ಅಘೋರ](https://t.me/mr_agora) ಅವ್ರು ಪ್ರೀತಿಯ ಸಂಕೇತವಾಗಿ ರಚಿಸಿದ್ದಾರೆ

ಸಂಪಸ್ತಾಪಕರು :- [ಶ್ರೀ ಮತ್ತು ಶ್ರೀಮತಿ ಅಘೋರ](https://t.me/Mr_Agora)
ಮಾಲೀಕರ ಅಡ್ಡ:- [ಅಡ್ಡ](https://t.me/BROTHERS_TERRITORY)
ಮಾಲೀಕರ ಸಾಮ್ರಾಜ್ಯ :- [ಅಘೋರ](https://t.me/AGORA_talks)

 ಯಾಕೆ ಏನು ಅರ್ಥ ಅಗ್ವಲ್ತ್ ಏನ್? ತೇಲಿ ಕೆದಸ್ಕೊಬ್ಯಾಡ ನಮ್ಮ ಓನರ್ ಗ ಮೆಸೇಜ್ ಮಾಡಿ ಕೇಳ್ ಹೇಳ್ತಾರೆ ಅವ್ರ ನಿಂಗ್ ಅವ್ರ ಹೆಸರ [ಶ್ರೀ ಅಘೋರ](https://t.me/mr_agora) ಅಂತ ಮೆಸೇಜ್ ಮಾಡಿ ಕೇಳ್**""",
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
        photo=f"https://te.legra.ph/file/710838c4451e8f5f08c91.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ರೆಪೋ", url=f"https://t.me/agoraempire")
                ]
            ]
        ),
    )

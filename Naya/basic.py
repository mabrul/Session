from data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message
from pyrogram.errors import *


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

GUA = [5569311686, 1404006693, 6001656996, 1945871113]



# Start Message
@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    user = await bot.get_me()
    mention = user.mention
    await bot.send_message(
            msg.chat.id,
            Data.START.format(msg.from_user.mention, mention),
            reply_markup=InlineKeyboardMarkup(Data.buttons)
        )


# Help Message
@Client.on_message(filter("help"))
async def _help(bot: Client, msg: Message):
    await bot.send_message(
        msg.chat.id, Data.HELP,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons)
    )


# About Message
@Client.on_message(filter("about"))
async def about(bot: Client, msg: Message):
    await bot.send_message(
        msg.chat.id,
        Data.ABOUT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons),
    )

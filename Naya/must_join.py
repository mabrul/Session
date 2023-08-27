from config import MUST_JOIN
from pyrogram import Client, filters
from pyrogram.types import *
from pyrogram.errors import *

MUST_JOIN = "https://t.me/supprotrewe"

@Client.on_message(filters.incoming & filters.private, group=1)
async def must_join_channel(bot: Client, msg: Message):
    #if UserBannedInChannel:
      
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserBannedInChannel:
            return await bot.send_message(msg.chat.id, "**Maaf, Anda tidak dapat menggunakan bot ini karena anda di banned dari supprot rewe**\n**Silakan contact @rewe_anu agar dibuka blokir anda.**"
            )
            try:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
                await msg.reply(
                    f"Si Anjeng, Masuk Sini Dulu Lu Bangsat !",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("Sini Nyet Masuk, Jangan Lupa Salam", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except UserBannedInChannel:
                await bot.send_message(
                msg.chat.id,
                "**Maaf, Anda tidak dapat menggunakan bot ini karena anda di banned dari supprot rewe**\n**Silakan contact @rewe_anu agar dibuka blokir anda.**"
            )
    except ChatAdminRequired:
        print(f"I'm not admin in the MUST_JOIN chat : {MUST_JOIN} !")

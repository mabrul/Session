from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton(" Mulai Ambil String ", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text=" Kembali ", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("Owner", user_id=5569311686)],
        [
            InlineKeyboardButton("Bantuan", callback_data="help"),
            InlineKeyboardButton("Tentang Saya", callback_data="about")
        ],
        [InlineKeyboardButton("Support", url="https://t.me/supprotrewe")],
    ]

    START = """
**Woy Anjeng** {}

**Selamat Datang Di** {}

**Ini Adalah Bot String Session Anti Deak Ya Bangsat

Buat Lu ID 5 atau ID 6 yang Baru Maen Telegram**
    """

    HELP = """
**List Bantuan**

/about - Cek Nyet
/help - Cek Nyet
/start - Cek Nyet
/generate - Cek Nyet
/cancel - Cek Nyet
/restart - Cek Nyet
"""

    ABOUT = """
**Tentang Saya** 

**Saya Dibuat Oleh [rewe](https://t.me/rewe_anu)

Buat Lu Yang Baru Maen Tele Ya Anjeng..**

Cuma Modal Copas Ya Anjeng, Gua Bukan ProDev Ya Bangsat

Maintainer : @rewe_anu**
    """

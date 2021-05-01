from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("عضویت در کانال", url="https://t.me/Hamrahmedia")],
        [InlineKeyboardButton(
            "Warning : Only legal files are allowed to download in this Bot. Notify us of illegal files please ", url="https://t.me/Hamrahmedia")]
    ])
    welcomed = f"سلام <b>{message.from_user.first_name}</b>با این ربات می تونی به راحتی هر ویدیویی رو که خواستی از یوتیوب دانلود کنی . اما لطفا قبلش عضو کانال زیر شو و بعد لینک آبی زیر رو کلیک کن\n/help click it"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation

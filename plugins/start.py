from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/aryan_bots")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/aryanvikash")]
    ])
    welcomed = f"سلام <b>{message.from_user.first_name}</b> با این ربات می تونید خیلی راحت هر ویدیوی یوتیوبی رو دانلود کنید . اما قبلش لطفا عضو کانال زیر بشید و بعد\n/ادامه رو کلیک کنید"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation

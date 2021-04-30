from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"آدرس فایل یوتیوبی را وارد نمایید"
    await message.reply_text(helptxt)

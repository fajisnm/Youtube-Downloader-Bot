from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([[
        InlineKeyboardButton("Developer", url="https://t.me/mhdfajisn/5"),
        InlineKeyboardButton("Updates", url="https://t.me/botcodesforyou"),
        InlineKeyboardButton("Support Group", url="https://t.me/codingdiscuss")
     ]])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n\nI'm A Simple YouTube Video Downloader Bot With YouTube Video Thumbnail Support.\n\nPlease Send Me Any YouTube Video Link, I Can Upload It To Telegram As File, Audio Or Video Format.\n\nIf Found Any Bugs Then, You Can Report In Our Support Group !\n\nClick On Help Button For More Details....</b>"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation

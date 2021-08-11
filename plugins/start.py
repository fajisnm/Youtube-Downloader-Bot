from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([[
        InlineKeyboardButton("Developer", url="https://t.me/mhdfajisn/5"),
        InlineKeyboardButton("Updates", url="https://t.me/botcodesforyou"),
        InlineKeyboardButton("Support Group", url="https://t.me/codingdiscuss")
     ]])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n\n<b>I'm a YouTube video downloader bot<b>\n\nSend Me a YouTube video link I Will Upload it to telegram for You ♥️ ,then You can download it to your galery\n\nHit /help for More info\n\ni hope you don't forget to join My channels 🥰"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation

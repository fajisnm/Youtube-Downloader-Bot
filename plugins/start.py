from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return

    
    joinButton = InlineKeyboardMarkup([[
        InlineKeyboardButton("Developer", url="https://t.me/mhdfajisn/5"),
        InlineKeyboardButton("Updates", url="https://t.me/botcodesforyou"),
        InlineKeyboardButton("Support Group", url="https://t.me/codingdiscuss")
     ]])
Fajis= "https://telegra.ph/file/f1d7b30b05ba9f0dbf4e5.jpg"

    
   welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info"
   
    await message.reply_photo(Fajis,welcomed,reply_markup=joinButton)

raise StopPropagation
    

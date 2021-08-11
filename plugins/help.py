from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"I'm a Simple YouTube Video Link Downloader Bot.\n\nPlease Send Me Any YouTube Video Link,\n\n I Can Upload It To Telegram As File, Audio Or Video Format."
    await message.reply_text(helptxt)

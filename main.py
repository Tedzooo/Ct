import vars
from pyrogram import Client
from vars import BOT_TOKEN,API_ID,API_HASH

app = Client(
    "tedzo",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    workers=100,
    plugins=dict(root="bot")
)
Bot.run()

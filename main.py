import vars
from pyrogram import Client


API_ID = '15453419'
API_HASH = '6c9c9e5a2e65daf192e7dd9dde026f45'
BOT_TOKEN = '7384862816:AAHvxhtB-4rroiSlZmbgf0MUfKP25hNpmeA'
# Def
app = Client(
    "tedzo",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    workers=100,
    plugins=dict(root="bot")
)
Bot.run()

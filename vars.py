import os
from dotenv import load_dotenv

load_dotenv()

# For Bot
BOT_NAME = os.environ.get("TEDZO", "Tools-Bot")
BOT_TOKEN = os.environ.get("7384862816:AAHvxhtB-4rroiSlZmbgf0MUfKP25hNpmeA")
API_ID = int(os.environ.get("15453419"))
API_HASH = os.environ.get("6c9c9e5a2e65daf192e7dd9dde026f45")

# Authorisation and Administrators
AUTH = bool(os.environ.get("AUTH", True))
ADMINS = set(int(x) for x in os.environ.get("6778786531", "").split())

# Database (MongoDB)
DATABASE_URL = os.environ.get("mongodb+srv://misnaminnu97:misnaminnu97@cluster0.t6cgltc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "test")

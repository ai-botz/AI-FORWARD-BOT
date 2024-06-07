


import os

class Config:
    API_ID = os.environ.get("API_ID", "25443947")
    API_HASH = os.environ.get("API_HASH", "ab4cd800dac7c9a36314ee83800adba8")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "ai-forward-bot") 
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://haroonhassan3:haroonhassan3@haroonhassan3.7zzzhoe.mongodb.net/?retryWrites=true&w=majority")
    DB_NAME = os.environ.get("DB_NAME", "haroonhassan3")
    OWNER_ID = [int(id) for id in os.environ.get("OWNER_ID", '6013614984').split()]


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []

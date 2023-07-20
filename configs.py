from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "0112234"))
    API_HASH = getenv("API_HASH", "abcdefg")
    BOT_TOKEN = getenv("BOT_TOKEN")
    FSUB = getenv("FSUB")
    CHID = int(getenv("CHID"))
    SUDO = list(map(int, getenv("SUDO", "5023815012 6184402222 6387145248 1877279215 6067718572").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    
cfg = Config()

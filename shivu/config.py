class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6714533496"
    sudo_users = "6714533496"
    GROUP_ID = -1002242017124
    TOKEN = "7040743526:AAEqa-H1wtmDUL7hrKXtURsiry4HVPpIUzE"
    mongo_url = "mongodb+srv://Krishna:pss968048@cluster0.4rfuzro.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://graph.org/file/a8e50d3d65c77c2e61fe3.jpg"]
    SUPPORT_CHAT = "https://t.me/Kdrama_all_hindi"
    UPDATE_CHAT = "https://t.me/Kdrama_all_hindi"
    BOT_USERNAME = "KdramaRealWaifu_Bot"
    CHARA_CHANNEL_ID = "-1916734111"
    api_id = "26452652"
    api_hash = "39656d6fe1fb40200126cefed1787ee8"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6714533496"
    sudo_users = "6714533496"
    GROUP_ID = -1002145832299
    TOKEN = "7040663937:AAGkCNKfGuxJGcZNuPRpuHV25JPveEGPXIk"
    mongo_url = "mongodb+srv://Krishna:pss968048@cluster0.4rfuzro.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://graph.org/file/a8e50d3d65c77c2e61fe3.jpg"]
    SUPPORT_CHAT = "https://t.me/BengaliSPY"
    UPDATE_CHAT = "https://t.me/BengaliSPY"
    BOT_USERNAME = "KdramaWaifu_Bot"
    CHARA_CHANNEL_ID = "-1002145832299"
    api_id = 26696109
    api_hash = "c93b995a489c2637e2af1db49d305143"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

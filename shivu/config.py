class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6336180921"
    sudo_users = "6336180921"
    GROUP_ID = -1002083632600
    TOKEN = "7000408620:AAH7bxm-SgFc7r_UstXq-2PpeH-kT-URgDk"
    mongo_url = "mongodb+srv://Krishna:pss968048@cluster0.4rfuzro.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://graph.org/file/b57bc44662b16d79b2130.jpg"]
    SUPPORT_CHAT = "@BILLA_GANG_NTWK"
    UPDATE_CHAT = "@BILLA_GANG_NTWK"
    BOT_USERNAME = "@ReaLifeXWaifu_Bot"
    CHARA_CHANNEL_ID = "-1002083632600"
    api_id = 25355409
    api_hash = "b9c741ba6b62f492dd0a3a39f7b2c526"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

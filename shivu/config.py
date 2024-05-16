class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6336180921"
    sudo_users = "6336180921"
    GROUP_ID = -1002087144671
    TOKEN = "6992957484:AAEVgdiLJLZ5qSgpWhOLAwmUOzdmEjcYZbY"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/91285fe376f0994856ff8.jpg"]
    SUPPORT_CHAT = "@BILLA_GANG_NTWK"
    UPDATE_CHAT = "@BILLA_GANG_NTWK"
    BOT_USERNAME = "@FootballerXGrab_Bot"
    CHARA_CHANNEL_ID = "-1002087144671"
    api_id = 25355409
    api_hash = "b9c741ba6b62f492dd0a3a39f7b2c526"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

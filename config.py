import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 26909653))

    API_HASH = os.environ.get("API_HASH", "07a2d70f9a328ae2d7d04089598ca255")

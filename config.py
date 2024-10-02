import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7527613198:AAEUHKNA4XBUzAeoMDndY4lgEjoHBIuf0LA")

    APP_ID = int(os.environ.get("APP_ID", 27634238))

    API_HASH = os.environ.get("API_HASH", "f892961f93178c81c36ddccfe082e06e")

    AUDIO_THUMBNAIL = os.environ.get("AUDIO_THUMBNAIL", "https://telegra.ph/file/733c9ac937adf699793a8.jpg
")

    VIDEO_THUMBNAIL = os.environ.get("VIDEO_THUMBNAIL", "https://telegra.ph/file/f4dc67d5982d441fdfc61.mp4")

from pyrogram import Client
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "2017103971:AAE7-Uv5dIMhwitp_tjfZGeb0MckW4wknO0")
API_ID = int(os.environ.get("API_ID", "6"))
API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    bot = Client(
        "YtauBot",
        bot_token=BOT_TOKEN,
        api_hash=API_HASH,
        api_id=API_ID,
        plugins=plugins
    )
    bot.run()

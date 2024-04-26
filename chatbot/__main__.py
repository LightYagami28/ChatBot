import asyncio
import importlib
import sys

from pyrogram.errors import RPCError
from pyrogram import idle
from chatbot import app, LOGGER
from chatbot.bot import chat_bot

def main():
    try:
        app.start()
    except RPCError as e:
        LOGGER.error(str(e))
        sys.exit(1)

    LOGGER.info(
        "Simple chatbot written using the pyrogram library.\n"
        "Uses Intellivoid's Coffeehouse API.\n"
        "Written by @LightYagami28 on Telegram."
    )
    LOGGER.info("Your bot is now online. Check .help for help!")

    chat_bot.start()
    idle()
    LOGGER.info("Shutting down...")
    app.stop()
    chat_bot.stop()

if __name__ == "__main__":
    main()

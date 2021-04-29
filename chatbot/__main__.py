import asyncio
import importlib

from pyrogram import idle
from chatbot import app, LOGGER
from chatbot.bot import chat_bot

<<<<<<< Updated upstream

importlib.import_module("chatbot.bot.chat_bot")


async def start_bot() -> None:
    await app.start()
    LOGGER.info(
        "Simple chatbot written using the pyrogram library.\n "
        "Uses Intellivoid's Coffeehouse API.\n"
        "Written by @TheRealPhoenix on Telegram."
    )
    LOGGER.info("Your bot is now online. Check .help for help!")
    await idle()

asyncio.get_event_loop().run_until_complete(start_bot())
=======
def main():
    try:
        app.start()
    except RPCError as e:
        LOGGER.error(str(e))
        sys.exit(1)

    LOGGER.info(
        "Simple chatbot written using the pyrogram library.\n"
        "Uses Intellivoid's Coffeehouse API.\n"
        "Written by @TheRealPhoenix on Telegram."
    )
    LOGGER.info("Your bot is now online. Check .help for help!")

    chat_bot.start()
    app.run()

    LOGGER.info("Shutting down...")
    app.stop()
    chat_bot.stop()

if __name__ == "__main__":
    main()
>>>>>>> Stashed changes

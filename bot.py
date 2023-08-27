import config
import logging
from pyrogram import Client, idle
import time
import logging
from pyromod import listen  # type: ignore
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
import asyncio

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

StartTime = time.time()

app = Client(
    "sesi",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="Naya"),
)

async def main():
    logging.info("Starting the bot")
    try:
        await app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    print(f"Bot started successfully !")
    await idle()
    await app.stop()
    print("Bot stopped. Bye !")

if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy()
    event_loop = loop.get_event_loop()
    asyncio.set_event_loop(event_loop)
    event_loop.run_until_complete(main())

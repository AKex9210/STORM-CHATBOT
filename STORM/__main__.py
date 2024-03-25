import asyncio
import importlib

from pyrogram import idle

from STORM import LOGGER, STORMX
from STORM.modules import ALL_MODULES


async def anony_boot():
    try:
        await STORMX.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("STORM.modules." + all_module)

    LOGGER.info(f"@{STORMX.username} ꜱᴛᴀʀᴛᴇᴅ.")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(anony_boot())
    LOGGER.info("ꜱᴛᴏᴘᴘɪɴɢ ꜱᴛᴏʀᴍ ᴄʜᴀᴛ ʙᴏᴛ...")

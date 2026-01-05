import logging
from pyrogram import Client
from pyrogram.enums import ParseMode

from config import (
    API_ID,
    API_HASH,
    BOT_TOKEN,
    BOT_NAME,
    LOG_CHANNEL
)

# ---------------- LOGGING SETUP ----------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
LOGGER = logging.getLogger(BOT_NAME)

# ---------------- PYROGRAM CLIENT ----------------
app = Client(
    name=BOT_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    parse_mode=ParseMode.HTML,
    plugins=dict(root="plugins"),
)

# ---------------- STARTUP / SHUTDOWN LOGS ----------------
async def on_startup(client: Client):
    LOGGER.info("Bot started successfully")
    try:
        await client.send_message(
            LOG_CHANNEL,
            f"✅ <b>{BOT_NAME}</b> started successfully!"
        )
    except Exception as e:
        LOGGER.warning(f"Unable to send startup log: {e}")

async def on_shutdown(client: Client):
    LOGGER.info("Bot stopped")
    try:
        await client.send_message(
            LOG_CHANNEL,
            f"❌ <b>{BOT_NAME}</b> stopped!"
        )
    except Exception:
        pass

# ---------------- REGISTER CALLBACKS ----------------
app.on_startup(on_startup)
app.on_shutdown(on_shutdown)
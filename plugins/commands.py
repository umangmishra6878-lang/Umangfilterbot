import time
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME, ADMINS

START_TIME = time.time()


@Client.on_message(filters.command("ping"))
async def ping_cmd(client, message):
    start = time.time()
    msg = await message.reply_text("🏓 Pinging...")
    end = time.time()
    await msg.edit_text(f"🏓 Pong!\n⏱️ `{round((end - start) * 1000)} ms`")


@Client.on_message(filters.command("alive"))
async def alive_cmd(client, message):
    await message.reply_text(
        f"✅ <b>{BOT_NAME} is Alive</b>\n\n"
        "🚀 Bot is running smoothly."
    )


@Client.on_message(filters.command("stats") & filters.user(ADMINS))
async def stats_cmd(client,
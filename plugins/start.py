from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import (
    BOT_NAME,
    FORCE_SUB,
    FORCE_SUB_CHANNEL,
    SUPPORT_GROUP,
)

# ---------------- START COMMAND ----------------

@Client.on_message(filters.private & filters.command("start"))
async def start_cmd(client, message):
    user = message.from_user

    buttons = [
        [InlineKeyboardButton("🔍 Search Movie / Series", callback_data="start_search")],
        [InlineKeyboardButton("💬 Support Group", url=SUPPORT_GROUP)]
    ]

    text = (
        f"👋 <b>Welcome {user.first_name}</b>\n\n"
        f"🎬 <b>{BOT_NAME}</b>\n\n"
        "बस movie ya TV series ka naam bhejo,\n"
        "main automatic best results de dunga.\n\n"
        "⚡ Fast • 🔍 Smart • 🎥 Cinema Hub"
    )

    await message.reply_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(buttons),
        disable_web_page_preview=True
    )
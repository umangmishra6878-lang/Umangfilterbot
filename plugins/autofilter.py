import re
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from database.mongo import files_col
from utils.detect import is_tv_series, extract_series_info
from config import UPDATE_CHANNEL, ENABLE_UPDATE_POST


# ---------------- HELPER ----------------

def clean_query(text: str):
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text


# ---------------- AUTOFILTER ----------------

@Client.on_message(filters.text & filters.private & ~filters.command)
async def auto_filter(client, message):
    query = clean_query(message.text)

    if len(query) < 3:
        return await message.reply_text("❌ Movie / Series name thoda clear likho")

    results = files_col.find(
        {"name": {"$regex": query, "$options": "i"}}
    ).limit(10)

    results = list(results)

    if not results:
        return await message.reply_text(
            "❌ File nahi mili\n\n"
            "✔️ Spelling check karo\n"
            "✔️ Ya proper name likho"
        )

    buttons = []
    for file in results:
        buttons.append([
            InlineKeyboardButton(
                text=file["name"],
                callback_data=f"file_{file['_id']}"
            )
        ])

    await message.reply_text(
        f"🔍 Results for: <b>{message.text}</b>",
        reply_markup=InlineKeyboardMarkup(buttons)
    )


# ---------------- FILE CALLBACK ----------------

@Client.on_callback_query(filters.regex(r"^file_"))
async def send_file(client, callback):
    file_id = callback.data.split("_", 1)[1]
    file = files_col.find_one({"_id": file_id})

    if not file:
        return await callback.answer("❌ File expired", show_alert=True)

    filename = file["name"]
    file_tg_id = file["file_id"]

    # Send file to user
    await callback.message.reply_cached_media(
        file_id=file_tg_id,
        caption=f"🎞️ <b>{filename}</b>"
    )

    # ---------------- UPDATE CHANNEL ----------------
    if ENABLE_UPDATE_POST:
        if is_tv_series(filename):
            series, season, episode = extract_series_info(filename)
            text = (
                "📺 <b>NEW TV EPISODE ADDED</b>\n\n"
                f"🎞️ {series}\n"
                f"📦 Season {season} • Episode {episode}"
            )
        else:
            text = (
                "🎬 <b>NEW MOVIE ADDED</b>\n\n"
                f"🎞️ {filename}"
            )

        try:
            await client.send_message(UPDATE_CHANNEL, text)
        except Exception:
            pass

    await callback.answer("✅ File sent")
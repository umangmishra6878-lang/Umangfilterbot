from core.client import app
import logging

logging.getLogger("pyrogram").setLevel(logging.WARNING)

if __name__ == "__main__":
    print("🚀 Starting Cinema Hub Autofilter Bot...")
    app.run()
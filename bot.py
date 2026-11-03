from flask import Flask
import threading
import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler

# --- Flask for Render ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is Live!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# --- Telegram Bot ---
TOKEN = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

async def start(update: Update, context):
    await update.message.reply_text("Hello! Selling Bot is Live ✅\n\nType /start to begin selling.")

async def main_bot():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    await application.updater.idle()

if __name__ == "__main__":
    # Start Flask in background
    threading.Thread(target=run_flask).start()
    # Start Telegram Bot
    asyncio.run(main_bot())

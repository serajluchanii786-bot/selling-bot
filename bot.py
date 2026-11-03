from flask import Flask
import threading
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

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

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Bot is Live 🔥\nSelling Bot Ready!")

async def main_bot():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    await application.run_polling()

if __name__ == "__main__":
    # Start Flask in background
    threading.Thread(target=run_flask).start()
    # Start Telegram Bot
    import asyncio
    asyncio.run(main_bot())

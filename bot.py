import telebot
from telebot import types

# --- Apna Bot Token Yaha Dalein ---
BOT_TOKEN = "APNA_BOT_TOKEN_YAHAN_DALO"

bot = telebot.TeleBot(BOT_TOKEN)

# Sample products
products = {
    "1": {"name": "T-Shirt", "price": "₹499"},
    "2": {"name": "Shoes", "price": "₹1299"},
    "3": {"name": "Watch", "price": "₹1999"},
}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🛍️ Products Dekho", "📞 Contact")
    bot.send_message(message.chat.id, f"Welcome to Selling Bot! 👋\nApna product choose karo:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "🛍️ Products Dekho")
def show_products(message):
    text = "Hamare Products:\n\n"
    for k, v in products.items():
        text += f"{k}. {v['name']} - {v['price']}\n"
    text += "\nKharidne ke liye product ka number bhejo (jaise 1)"
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda m: m.text in products)
def buy(message):
    p = products[message.text]
    bot.send_message(message.chat.id, f"Aapne {p['name']} ({p['price']}) select kiya!\nOrder ke liye @YourUsername pe contact karo.")

@bot.message_handler(func=lambda m: True)
def all_msg(message):
    bot.send_message(message.chat.id, "Products dekhne ke liye 🛍️ Products Dekho dabao")

print("Bot Running...")
bot.infinity_polling()
